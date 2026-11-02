# transmembrane_0012

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 287..307

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLPILLGWFLTLCSSHIVRSCLQCDQVIRYVHEDFLSTVKGIRVRDQIELKKIIDHAYTNYRETSKLLSGVIDPTTLYRARTEYQSEFKRHWKEDRTNSLQWDLITIVEKGKRILQKHLEIFIAEGLCPNKCGLLYQRVMNCTSCQYGLFTCLSAKPPLDCGEHHLEADEGEEVVLDCFLSWHTLVVGQTEYHYSWHPGETNVLFDGEYEELVVTKESKIVLNQLSVSEEGSYRCLLKDQKGTALSRTFFQLEVKPFPSTSPRQVVTLPSLPLGYENTPYSLQKSSFLTVLILLTVLSITGSLIIIEYLRKSLKRQEEARGRDSRTAGDIELNTE

[Multiple Choices]
A. 27..47; 59..79; 109..129; 142..162; 168..188; 225..245
B. 291..304
C. 287..307; 298..318
D. 287..307
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies residues 287–307 as a helical transmembrane region. The cited evidence code indicates computational evidence, not experimental validation.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a continuous, strongly hydrophobic C-terminal stretch consistent with a single membrane-spanning helix. The 287–307 interval captures that span; 291–304 is a short subset, while 298–318 extends beyond the hydrophobic segment into the less suitable tail.


**Missing item-specific fact**

> No additional item-specific fact is needed to distinguish the plausible membrane-spanning interval from the listed alternatives, though exact boundary conventions can vary.


**Reason**

> The hydrophobic segment and the contrasting lengths and endpoints in the choices provide a concrete sequence-based basis for selecting D. The database annotation corroborates the answer but is not the only basis for it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C includes the 287–307 interval but also proposes a second overlapping span extending past the hydrophobic region; it is not as defensible as D as a complete answer.


### Important caveats

- The supporting UniProt feature is computationally evidenced (ECO:0000255), not an experimentally established boundary.
- The historical and current source sequences match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a continuous, strongly hydrophobic C-terminal stretch consistent with a single membrane-spanning helix. The 287–307 interval captures that span; 291–304 is a short subset, while 298–318 extends beyond the hydrophobic segment into the less suitable tail.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional item-specific fact is needed to distinguish the plausible membrane-spanning interval from the listed alternatives, though exact boundary conventions can vary.",
    "reason": "The hydrophobic segment and the contrasting lengths and endpoints in the choices provide a concrete sequence-based basis for selecting D. The database annotation corroborates the answer but is not the only basis for it."
  },
  "case_id": "transmembrane_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 287–307 as a helical transmembrane region. The cited evidence code indicates computational evidence, not experimental validation."
  },
  "important_caveats": [
    "The supporting UniProt feature is computationally evidenced (ECO:0000255), not an experimentally established boundary.",
    "The historical and current source sequences match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C includes the 287–307 interval but also proposes a second overlapping span extending past the hydrophobic region; it is not as defensible as D as a complete answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residues 287–307 as a helical transmembrane region. The cited evidence code indicates computational evidence, not experimental validation.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a continuous, strongly hydrophobic C-terminal stretch consistent with a single membrane-spanning helix. The 287–307 interval captures that span; 291–304 is a short subset, while 298–318 extends beyond the hydrophobic segment into the less suitable tail.",
    "missing_item_specific_fact": "No additional item-specific fact is needed to distinguish the plausible membrane-spanning interval from the listed alternatives, though exact boundary conventions can vary.",
    "reason": "The hydrophobic segment and the contrasting lengths and endpoints in the choices provide a concrete sequence-based basis for selecting D. The database annotation corroborates the answer but is not the only basis for it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C includes the 287–307 interval but also proposes a second overlapping span extending past the hydrophobic region; it is not as defensible as D as a complete answer."
  },
  "important_caveats": [
    "The supporting UniProt feature is computationally evidenced (ECO:0000255), not an experimentally established boundary.",
    "The historical and current source sequences match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry A0A2R8QHQ6 (IZUM1_DANRE, zebrafish Izumo sperm-egg fusion protein 1, 336 AA) annotates a single transmembrane helix at positions 287..307 (evidence ECO:0000255, inferred by similarity). Both the current entry (C5) and the archived historical entry (H2, entry version 30) confirm TRANSMEM 287..307 with sequence match. The benchmark sequence matches the UniProt sequence exactly (SHA-256 identical). Choice D (287..307) corresponds precisely to this annotation. The annotation is computational (similarity-based), not experimental, but it is the standard reference annotation and is consistent with the clearly hydrophobic 21-residue segment (FLTVLILLTVLSITGSLIII) identified in the C-terminal region of the sequence.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four choices can be distinguished by standard transmembrane biology and sequence analysis: (1) Choice A proposes six TM helices across the N-terminal region, but this region is a soluble immunoglobulin-like domain rich in charged/polar residues (Cys pairs, D, E, K, R) with no contiguous hydrophobic stretches of ≥18 residues—clearly incompatible with multi-pass membrane topology. (2) Choice B (291..304) is only 14 residues, well below the ~18–25 residue minimum needed for an α-helix to span the ~30 Å hydrophobic core of a lipid bilayer. (3) Choice C adds a second TM region at 298..318, but that segment (SITGSLIIIEYLRKSLKRQEE) contains multiple charged residues (R, K, R, Q, E, E) and is unambiguously hydrophilic, making a TM assignment impossible. (4) Choice D (287..307) is a 21-residue predominantly hydrophobic segment (FLTVLILLTVLSITGSLIII) of standard TM helix length, preceded by a polar linker and followed by a charged cytoplasmic tail—consistent with a type-I single-pass membrane protein architecture. Only D survives biological elimination.


**Missing item-specific fact**

> None required. The exact boundaries (287 vs 285, 307 vs 309) are not among the competing choices; the question is structured so that only one option is biologically defensible by general TM-helix criteria (length, hydrophobicity, domain context).


**Reason**

> A knowledgeable student can eliminate A (soluble Ig-fold domain, not 6 TM passes), B (too short for bilayer spanning), and C (second region is charged) using general membrane-protein biology and hydrophobicity analysis of the supplied sequence. D is the sole remaining option and matches the standard TM-helix length and composition. No protein-specific database lookup is strictly necessary to arrive at D among these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor fails on a clear biological criterion: A violates domain architecture, B violates minimum helix length, C includes a charged segment as TM. Only D is consistent with all criteria simultaneously. The exact boundary precision (±1–2 residues) is not tested because no alternative boundary choice is offered.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (inferred by similarity), meaning it is a computational/homology-based prediction rather than an experimentally determined boundary. The true boundaries could differ by 1–3 residues in a high-resolution structure.
- The reviewer-only evidence confirms sequence match and annotation, but the evaluated model did not have access to the UniProt accession or annotation—only the raw sequence and choices.
- The annotation is for the full 336-residue precursor (including signal peptide); no isoform or construct numbering issues apply here.
- The question tests recognition of a single-pass TM protein topology, which is a standard reasoning task in membrane-protein biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices can be distinguished by standard transmembrane biology and sequence analysis: (1) Choice A proposes six TM helices across the N-terminal region, but this region is a soluble immunoglobulin-like domain rich in charged/polar residues (Cys pairs, D, E, K, R) with no contiguous hydrophobic stretches of ≥18 residues—clearly incompatible with multi-pass membrane topology. (2) Choice B (291..304) is only 14 residues, well below the ~18–25 residue minimum needed for an α-helix to span the ~30 Å hydrophobic core of a lipid bilayer. (3) Choice C adds a second TM region at 298..318, but that segment (SITGSLIIIEYLRKSLKRQEE) contains multiple charged residues (R, K, R, Q, E, E) and is unambiguously hydrophilic, making a TM assignment impossible. (4) Choice D (287..307) is a 21-residue predominantly hydrophobic segment (FLTVLILLTVLSITGSLIII) of standard TM helix length, preceded by a polar linker and followed by a charged cytoplasmic tail—consistent with a type-I single-pass membrane protein architecture. Only D survives biological elimination.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The exact boundaries (287 vs 285, 307 vs 309) are not among the competing choices; the question is structured so that only one option is biologically defensible by general TM-helix criteria (length, hydrophobicity, domain context).",
    "reason": "A knowledgeable student can eliminate A (soluble Ig-fold domain, not 6 TM passes), B (too short for bilayer spanning), and C (second region is charged) using general membrane-protein biology and hydrophobicity analysis of the supplied sequence. D is the sole remaining option and matches the standard TM-helix length and composition. No protein-specific database lookup is strictly necessary to arrive at D among these choices."
  },
  "case_id": "transmembrane_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry A0A2R8QHQ6 (IZUM1_DANRE, zebrafish Izumo sperm-egg fusion protein 1, 336 AA) annotates a single transmembrane helix at positions 287..307 (evidence ECO:0000255, inferred by similarity). Both the current entry (C5) and the archived historical entry (H2, entry version 30) confirm TRANSMEM 287..307 with sequence match. The benchmark sequence matches the UniProt sequence exactly (SHA-256 identical). Choice D (287..307) corresponds precisely to this annotation. The annotation is computational (similarity-based), not experimental, but it is the standard reference annotation and is consistent with the clearly hydrophobic 21-residue segment (FLTVLILLTVLSITGSLIII) identified in the C-terminal region of the sequence."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (inferred by similarity), meaning it is a computational/homology-based prediction rather than an experimentally determined boundary. The true boundaries could differ by 1–3 residues in a high-resolution structure.",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model did not have access to the UniProt accession or annotation—only the raw sequence and choices.",
    "The annotation is for the full 336-residue precursor (including signal peptide); no isoform or construct numbering issues apply here.",
    "The question tests recognition of a single-pass TM protein topology, which is a standard reasoning task in membrane-protein biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor fails on a clear biological criterion: A violates domain architecture, B violates minimum helix length, C includes a charged segment as TM. Only D is consistent with all criteria simultaneously. The exact boundary precision (±1–2 residues) is not tested because no alternative boundary choice is offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry A0A2R8QHQ6 (IZUM1_DANRE, zebrafish Izumo sperm-egg fusion protein 1, 336 AA) annotates a single transmembrane helix at positions 287..307 (evidence ECO:0000255, inferred by similarity). Both the current entry (C5) and the archived historical entry (H2, entry version 30) confirm TRANSMEM 287..307 with sequence match. The benchmark sequence matches the UniProt sequence exactly (SHA-256 identical). Choice D (287..307) corresponds precisely to this annotation. The annotation is computational (similarity-based), not experimental, but it is the standard reference annotation and is consistent with the clearly hydrophobic 21-residue segment (FLTVLILLTVLSITGSLIII) identified in the C-terminal region of the sequence.",
    "evidence_ids": ["C5", "H2", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four choices can be distinguished by standard transmembrane biology and sequence analysis: (1) Choice A proposes six TM helices across the N-terminal region, but this region is a soluble immunoglobulin-like domain rich in charged/polar residues (Cys pairs, D, E, K, R) with no contiguous hydrophobic stretches of ≥18 residues—clearly incompatible with multi-pass membrane topology. (2) Choice B (291..304) is only 14 residues, well below the ~18–25 residue minimum needed for an α-helix to span the ~30 Å hydrophobic core of a lipid bilayer. (3) Choice C adds a second TM region at 298..318, but that segment (SITGSLIIIEYLRKSLKRQEE) contains multiple charged residues (R, K, R, Q, E, E) and is unambiguously hydrophilic, making a TM assignment impossible. (4) Choice D (287..307) is a 21-residue predominantly hydrophobic segment (FLTVLILLTVLSITGSLIII) of standard TM helix length, preceded by a polar linker and followed by a charged cytoplasmic tail—consistent with a type-I single-pass membrane protein architecture. Only D survives biological elimination.",
    "missing_item_specific_fact": "None required. The exact boundaries (287 vs 285, 307 vs 309) are not among the competing choices; the question is structured so that only one option is biologically defensible by general TM-helix criteria (length, hydrophobicity, domain context).",
    "reason": "A knowledgeable student can eliminate A (soluble Ig-fold domain, not 6 TM passes), B (too short for bilayer spanning), and C (second region is charged) using general membrane-protein biology and hydrophobicity analysis of the supplied sequence. D is the sole remaining option and matches the standard TM-helix length and composition. No protein-specific database lookup is strictly necessary to arrive at D among these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor fails on a clear biological criterion: A violates domain architecture, B violates minimum helix length, C includes a charged segment as TM. Only D is consistent with all criteria simultaneously. The exact boundary precision (±1–2 residues) is not tested because no alternative boundary choice is offered."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (inferred by similarity), meaning it is a computational/homology-based prediction rather than an experimentally determined boundary. The true boundaries could differ by 1–3 residues in a high-resolution structure.",
    "The reviewer-only evidence confirms sequence match and annotation, but the evaluated model did not have access to the UniProt accession or annotation—only the raw sequence and choices.",
    "The annotation is for the full 336-residue precursor (including signal peptide); no isoform or construct numbering issues apply here.",
    "The question tests recognition of a single-pass TM protein topology, which is a standard reasoning task in membrane-protein biology."
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

**Accession:** `A0A2R8QHQ6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8QHQ6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:50.294214+00:00.  

```json
"A0A2R8QHQ6"
```

Source SHA-256: `1f080979fe7048e78f2edfaa03e82a529e0dcfffb47df84982e5f47bec07c233`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8QHQ6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:50.294214+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"value":"Izumo sperm-egg fusion protein 1"}}}
```

Source SHA-256: `1f080979fe7048e78f2edfaa03e82a529e0dcfffb47df84982e5f47bec07c233`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8QHQ6.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:50.294214+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":307},"start":{"modifier":"EXACT","value":287}},"type":"Transmembrane"}
```

Source SHA-256: `1f080979fe7048e78f2edfaa03e82a529e0dcfffb47df84982e5f47bec07c233`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8QHQ6?format=txt&versions=30)  
**Locator:** `lines 132-134`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:52.546075+00:00.  

```text
FT   TRANSMEM        287..307
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `98dd15dd75468aa1c87c8374da8af70b6254d13862c620694aed67db56c75e75`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
