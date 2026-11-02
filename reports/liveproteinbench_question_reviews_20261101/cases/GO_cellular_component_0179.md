# GO_cellular_component_0179

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — extracellular region

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIKMLQLPFNKKGQVSFDFIIAMLFLLLIFAFMGQNVLNMAKSFRDSETAEHAHAILDSFENYAIMAYSKDVTVNATFEPIGNLNYTIMLSNKSISVNSSTNIIFQPETDANGDYVSIKCNNVDNSVNTIPLNAVRISFGDFTVSKDEMEVNIR

[Multiple Choices]
A. NF-kappaB p50/p65 complex
B. peroxisomal matrix
C. extracellular region
D. cytoplasm
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record describes this protein as a minor structural pilin and annotates it as secreted, at the cell surface, and in a fimbrial structure. It also assigns GO:0005576, extracellular region, matching choice C. The GO assignment is computational (IEA), while the localization statement cites literature; these support the key but are not equivalent evidence types.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The hydrophobic N-terminal segment is compatible with export or membrane targeting, making an external location plausible, but by itself does not establish that this protein is a secreted pilin rather than membrane-associated or intracellular.


**Missing item-specific fact**

> Identifying the protein as the archaeal minor pilin EpdC, and knowing its reported secretion/fimbrial localization, is needed to distinguish the keyed external location confidently.


**Reason**

> The input supplies only the sequence and choices. The sequence offers a suggestive targeting clue, but the decisive pilin identity and localization are protein-specific facts absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports extracellular region among the listed choices. The protein is also annotated to the cell surface and a fimbrium, but neither is a separate option.


### Important caveats

- The sequence matches the cited UniProt record, but the author’s exact source snapshot is unknown.
- The GO extracellular-region annotation is IEA; the record also reports cell-surface and fimbrial localization, so extracellular region should not be read as the protein’s only location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The hydrophobic N-terminal segment is compatible with export or membrane targeting, making an external location plausible, but by itself does not establish that this protein is a secreted pilin rather than membrane-associated or intracellular.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying the protein as the archaeal minor pilin EpdC, and knowing its reported secretion/fimbrial localization, is needed to distinguish the keyed external location confidently.",
    "reason": "The input supplies only the sequence and choices. The sequence offers a suggestive targeting clue, but the decisive pilin identity and localization are protein-specific facts absent from the question."
  },
  "case_id": "GO_cellular_component_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes this protein as a minor structural pilin and annotates it as secreted, at the cell surface, and in a fimbrial structure. It also assigns GO:0005576, extracellular region, matching choice C. The GO assignment is computational (IEA), while the localization statement cites literature; these support the key but are not equivalent evidence types."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the author’s exact source snapshot is unknown.",
    "The GO extracellular-region annotation is IEA; the record also reports cell-surface and fimbrial localization, so extracellular region should not be read as the protein’s only location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports extracellular region among the listed choices. The protein is also annotated to the cell surface and a fimbrium, but neither is a separate option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes this protein as a minor structural pilin and annotates it as secreted, at the cell surface, and in a fimbrial structure. It also assigns GO:0005576, extracellular region, matching choice C. The GO assignment is computational (IEA), while the localization statement cites literature; these support the key but are not equivalent evidence types.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The hydrophobic N-terminal segment is compatible with export or membrane targeting, making an external location plausible, but by itself does not establish that this protein is a secreted pilin rather than membrane-associated or intracellular.",
    "missing_item_specific_fact": "Identifying the protein as the archaeal minor pilin EpdC, and knowing its reported secretion/fimbrial localization, is needed to distinguish the keyed external location confidently.",
    "reason": "The input supplies only the sequence and choices. The sequence offers a suggestive targeting clue, but the decisive pilin identity and localization are protein-specific facts absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports extracellular region among the listed choices. The protein is also annotated to the cell surface and a fimbrium, but neither is a separate option."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the author’s exact source snapshot is unknown.",
    "The GO extracellular-region annotation is IEA; the record also reports cell-surface and fimbrial localization, so extracellular region should not be read as the protein’s only location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q6M0N3 (Minor structural pilin EpdC) is annotated as Secreted, Cell surface, and Fimbrium (C5/H4, ECO:0000305 from PubMed:17114255 and PubMed:21075925). GO cross-references include GO:0005576 (extracellular region) and GO:0009986 (cell surface), both IEA:UniProtKB-SubCell (C6/C7, H5/H6). The entry is flagged as Precursor, confirming a signal peptide and secretion. Among the four options, 'extracellular region' is the only one consistent with a secreted pilin subunit. One minor caveat: the GO definition for extracellular region notes it is intended for products NOT attached to the cell surface, and 'cell surface' is also annotated; however, 'cell surface' is not among the answer choices, making C the best available option.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6), [C4](#evidence-c4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region (MIKMLQLPFNKKGQVSFDFIIAMLFLLLIFAFMG) exhibits a classic prokaryotic signal peptide architecture: a positively charged n-region (K, K), a strongly hydrophobic h-region (IIAMLFLLLIFAFMG), and a cleavage-site region. This indicates the protein is targeted for secretion, eliminating cytoplasm (D). The small size (154 aa) and lack of any PTS1 (SKL) or PTS2 peroxisomal targeting motif eliminate peroxisomal matrix (B). NF-kappaB p50/p65 complex (A) is a vertebrate-specific heterodimer; a protein bearing a prokaryotic-type signal peptide cannot be a component of it. The signal peptide in a prokaryotic context points to secretion/extracellular localization, supporting C.


**Missing item-specific fact**

> None critical. The signal peptide is discernible from the sequence. Exact identification as a pilin subunit requires database lookup, but is not needed to distinguish among the four given options.


**Reason**

> The hydrophobic N-terminal stretch with flanking positive charges is a recognizable signal peptide motif. Combined with general knowledge that (a) signal peptides in prokaryotes direct secretion, (b) peroxisomes are eukaryotic organelles, and (c) NF-kappaB is vertebrate-specific, a model can eliminate B, D, and A through biological reasoning. The remaining option C follows from the secretion signal.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (NF-kappaB complex, vertebrate-specific), B (peroxisomal matrix, eukaryotic organelle), and D (cytoplasm, contradicted by signal peptide) are all clearly incompatible with a secreted prokaryotic pilin. C is the only defensible choice among the four.


### Important caveats

- The GO annotation for extracellular region (GO:0005576) carries IEA evidence (inferred from UniProt subcellular location), not direct experimental evidence. The primary experimental annotations are 'Secreted,' 'Cell surface,' and 'Fimbrium' (ECO:0000305, curator inference from PubMed literature).
- The GO definition for extracellular region notes it applies to products NOT attached to the cell surface; a pilin is part of a surface-attached pilus. 'Cell surface' (GO:0009986) is also annotated but is not among the answer choices, so C remains the best fit.
- The organism (Methanococcus maripaludis, an archaeon) is not stated in the model input; the model must infer prokaryotic context from the signal peptide type and absence of eukaryotic features.
- Distinguishing a signal peptide from a transmembrane domain purely from sequence can be non-trivial, though the overall context (small protein, charge pattern, lack of multiple hydrophobic segments) favors signal peptide.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region (MIKMLQLPFNKKGQVSFDFIIAMLFLLLIFAFMG) exhibits a classic prokaryotic signal peptide architecture: a positively charged n-region (K, K), a strongly hydrophobic h-region (IIAMLFLLLIFAFMG), and a cleavage-site region. This indicates the protein is targeted for secretion, eliminating cytoplasm (D). The small size (154 aa) and lack of any PTS1 (SKL) or PTS2 peroxisomal targeting motif eliminate peroxisomal matrix (B). NF-kappaB p50/p65 complex (A) is a vertebrate-specific heterodimer; a protein bearing a prokaryotic-type signal peptide cannot be a component of it. The signal peptide in a prokaryotic context points to secretion/extracellular localization, supporting C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The signal peptide is discernible from the sequence. Exact identification as a pilin subunit requires database lookup, but is not needed to distinguish among the four given options.",
    "reason": "The hydrophobic N-terminal stretch with flanking positive charges is a recognizable signal peptide motif. Combined with general knowledge that (a) signal peptides in prokaryotes direct secretion, (b) peroxisomes are eukaryotic organelles, and (c) NF-kappaB is vertebrate-specific, a model can eliminate B, D, and A through biological reasoning. The remaining option C follows from the secretion signal."
  },
  "case_id": "GO_cellular_component_0179",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H6",
      "C4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q6M0N3 (Minor structural pilin EpdC) is annotated as Secreted, Cell surface, and Fimbrium (C5/H4, ECO:0000305 from PubMed:17114255 and PubMed:21075925). GO cross-references include GO:0005576 (extracellular region) and GO:0009986 (cell surface), both IEA:UniProtKB-SubCell (C6/C7, H5/H6). The entry is flagged as Precursor, confirming a signal peptide and secretion. Among the four options, 'extracellular region' is the only one consistent with a secreted pilin subunit. One minor caveat: the GO definition for extracellular region notes it is intended for products NOT attached to the cell surface, and 'cell surface' is also annotated; however, 'cell surface' is not among the answer choices, making C the best available option."
  },
  "important_caveats": [
    "The GO annotation for extracellular region (GO:0005576) carries IEA evidence (inferred from UniProt subcellular location), not direct experimental evidence. The primary experimental annotations are 'Secreted,' 'Cell surface,' and 'Fimbrium' (ECO:0000305, curator inference from PubMed literature).",
    "The GO definition for extracellular region notes it applies to products NOT attached to the cell surface; a pilin is part of a surface-attached pilus. 'Cell surface' (GO:0009986) is also annotated but is not among the answer choices, so C remains the best fit.",
    "The organism (Methanococcus maripaludis, an archaeon) is not stated in the model input; the model must infer prokaryotic context from the signal peptide type and absence of eukaryotic features.",
    "Distinguishing a signal peptide from a transmembrane domain purely from sequence can be non-trivial, though the overall context (small protein, charge pattern, lack of multiple hydrophobic segments) favors signal peptide."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (NF-kappaB complex, vertebrate-specific), B (peroxisomal matrix, eukaryotic organelle), and D (cytoplasm, contradicted by signal peptide) are all clearly incompatible with a secreted prokaryotic pilin. C is the only defensible choice among the four."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0179",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q6M0N3 (Minor structural pilin EpdC) is annotated as Secreted, Cell surface, and Fimbrium (C5/H4, ECO:0000305 from PubMed:17114255 and PubMed:21075925). GO cross-references include GO:0005576 (extracellular region) and GO:0009986 (cell surface), both IEA:UniProtKB-SubCell (C6/C7, H5/H6). The entry is flagged as Precursor, confirming a signal peptide and secretion. Among the four options, 'extracellular region' is the only one consistent with a secreted pilin subunit. One minor caveat: the GO definition for extracellular region notes it is intended for products NOT attached to the cell surface, and 'cell surface' is also annotated; however, 'cell surface' is not among the answer choices, making C the best available option.",
    "evidence_ids": ["C5", "C7", "H4", "H6", "C4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region (MIKMLQLPFNKKGQVSFDFIIAMLFLLLIFAFMG) exhibits a classic prokaryotic signal peptide architecture: a positively charged n-region (K, K), a strongly hydrophobic h-region (IIAMLFLLLIFAFMG), and a cleavage-site region. This indicates the protein is targeted for secretion, eliminating cytoplasm (D). The small size (154 aa) and lack of any PTS1 (SKL) or PTS2 peroxisomal targeting motif eliminate peroxisomal matrix (B). NF-kappaB p50/p65 complex (A) is a vertebrate-specific heterodimer; a protein bearing a prokaryotic-type signal peptide cannot be a component of it. The signal peptide in a prokaryotic context points to secretion/extracellular localization, supporting C.",
    "missing_item_specific_fact": "None critical. The signal peptide is discernible from the sequence. Exact identification as a pilin subunit requires database lookup, but is not needed to distinguish among the four given options.",
    "reason": "The hydrophobic N-terminal stretch with flanking positive charges is a recognizable signal peptide motif. Combined with general knowledge that (a) signal peptides in prokaryotes direct secretion, (b) peroxisomes are eukaryotic organelles, and (c) NF-kappaB is vertebrate-specific, a model can eliminate B, D, and A through biological reasoning. The remaining option C follows from the secretion signal."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (NF-kappaB complex, vertebrate-specific), B (peroxisomal matrix, eukaryotic organelle), and D (cytoplasm, contradicted by signal peptide) are all clearly incompatible with a secreted prokaryotic pilin. C is the only defensible choice among the four."
  },
  "important_caveats": [
    "The GO annotation for extracellular region (GO:0005576) carries IEA evidence (inferred from UniProt subcellular location), not direct experimental evidence. The primary experimental annotations are 'Secreted,' 'Cell surface,' and 'Fimbrium' (ECO:0000305, curator inference from PubMed literature).",
    "The GO definition for extracellular region notes it applies to products NOT attached to the cell surface; a pilin is part of a surface-attached pilus. 'Cell surface' (GO:0009986) is also annotated but is not among the answer choices, so C remains the best fit.",
    "The organism (Methanococcus maripaludis, an archaeon) is not stated in the model input; the model must infer prokaryotic context from the signal peptide type and absence of eukaryotic features.",
    "Distinguishing a signal peptide from a transmembrane domain purely from sequence can be non-trivial, though the overall context (small protein, charge pattern, lack of multiple hydrophobic segments) favors signal peptide."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q6M0N3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 69. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:40.884710+00:00.  

```json
"Q6M0N3"
```

Source SHA-256: `7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:40.884710+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17114255","source":"PubMed"}],"value":"EppA-dependent protein C"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Minor structural pilin EpdC"}}}
```

Source SHA-256: `7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:40.884710+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"17114255","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"17114255","source":"PubMed"}],"id":"SL-0310","value":"Cell surface"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"17114255","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"21075925","source":"PubMed"}],"id":"SL-0113","value":"Fimbrium"}}]}
```

Source SHA-256: `7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:40.884710+00:00.  

```json
{"database":"GO","id":"GO:0009986","properties":[{"key":"GoTerm","value":"C:cell surface"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N3.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:40.884710+00:00.  

```json
{"database":"GO","id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `7a72c62f63d289235c8aa24d85564bf3e0b121ea8158124580fd20d99dc69ad7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69)  
**Locator:** `lines 50-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:31:42.932189+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:17114255}. Cell
CC       surface {ECO:0000305|PubMed:17114255}. Fimbrium
CC       {ECO:0000305|PubMed:17114255, ECO:0000305|PubMed:21075925}.
```

Source SHA-256: `8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69)  
**Locator:** `lines 73-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:31:42.932189+00:00.  

```text
DR   GO; GO:0009986; C:cell surface; IEA:UniProtKB-SubCell.
```

Source SHA-256: `8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N3?format=txt&versions=69)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:31:42.932189+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.
```

Source SHA-256: `8d3f258c3600722e2394e319abab1f897ad0742562802d75ec4ba67a7bd6afaa`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 57481-57505`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005576
name: extracellular region
namespace: cellular_component
def: "The space external to the outermost structure of a cell. For cells without external protective or external encapsulating structures this refers to space outside of the plasma membrane. This term covers the host cell environment outside an intracellular parasite." [GOC:curators]
comment: Note that this term is intended to annotate gene products that are not attached to the cell surface. For gene products at the cell surface, consider annotating to external side of plasma membrane ; GO:0009897.
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "extracellular" EXACT []
xref: Wikipedia:Extracellular
is_a: GO:0110165 ! cellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 179. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
