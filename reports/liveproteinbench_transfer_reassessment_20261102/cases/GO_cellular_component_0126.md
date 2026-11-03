# GO_cellular_component_0126: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_cellular_component_0126.txt)

**Task:** `GO_cellular_component`  
**Author key, unchanged:** **C** — mitochondrial outer membrane

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
MRAGRVRPLRASDMKKDVRILLVGEPRVGKTSLIMSLVSEEFPEEVPPRAEEITIPADVTPERVPTHIVDYSEAEQSDEQLHQEISQANVICIVYAVNNKHSIDKVTSRWIPLINERTDKDSRLPLILVGNKSDLVEYSSMETILPIMNQYTEIETCVECSAKNLKNISELFYYAQKAVLHPTGPLYCPEEKEMKPACIKALTRIFKISDQDNDGTLNDAELNFFQRICFNTPLAPQALEDVKNVVRKHLSDGVADSGLTLRGFLFLHTLFIQRGRHETTWTVLRRFGYDDDLDLTPEYLFPLLKIPPDCTTELNHHAYLFLQSTFDKHDLDRDCALSPDELKDLFQVFPYIPWGPDVNNTVCTNESGWITYQGFLSQWTLTTYLDVQRCLEYLGYLGYSILTEQESQASAITVTRDKKIDLQKKQTQRNVFRCNVIGVKGCGKTGVLQSLLGRNLMRQKKIRDDHKSYYAINTVYVYGQEKYLLLHDISESEFLTEAEIVCDVVCLVYDVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLKSSTFWLRASFGATVFAVVGFAMYRALLKQR

[Multiple Choices]
A. nuclear envelope
B. vitelline envelope
C. mitochondrial outer membrane
D. nematocyst
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches rat MIRO-1/Rhot1. UniProt annotates it at the mitochondrial outer membrane, and the matching historical entry carries the same localization annotation. The support is chiefly transferred or computationally inferred rather than direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The GTPase-rich sequence and C-terminal hydrophobic membrane anchor support a membrane-associated protein, but those features alone do not distinguish the mitochondrial outer membrane from the nuclear envelope.


**Missing item-specific fact**

> The protein-specific association of MIRO-1/Rhot1 with the mitochondrial outer membrane is needed to select C; that localization is not supplied in the question.


**Reason**

> The sequence offers clues to protein architecture and membrane association, but identifying the correct organelle requires protein-specific localization knowledge or an external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence has no general targeting feature that makes the nuclear envelope a comparably supported choice; the external sequence-matched annotation supports C.


### Important caveats

- The reviewed localization annotation is transferred from UniProtKB:Q8IXI2 (ECO:0000250), while the GO mitochondrial outer membrane annotation is marked ISS; neither excerpt establishes direct experimental localization of this rat sequence.
- The source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The GTPase-rich sequence and C-terminal hydrophobic membrane anchor support a membrane-associated protein, but those features alone do not distinguish the mitochondrial outer membrane from the nuclear envelope.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific association of MIRO-1/Rhot1 with the mitochondrial outer membrane is needed to select C; that localization is not supplied in the question.",
    "reason": "The sequence offers clues to protein architecture and membrane association, but identifying the correct organelle requires protein-specific localization knowledge or an external annotation."
  },
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches rat MIRO-1/Rhot1. UniProt annotates it at the mitochondrial outer membrane, and the matching historical entry carries the same localization annotation. The support is chiefly transferred or computationally inferred rather than direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewed localization annotation is transferred from UniProtKB:Q8IXI2 (ECO:0000250), while the GO mitochondrial outer membrane annotation is marked ISS; neither excerpt establishes direct experimental localization of this rat sequence.",
    "The source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence has no general targeting feature that makes the nuclear envelope a comparably supported choice; the external sequence-matched annotation supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches rat MIRO-1/Rhot1. UniProt annotates it at the mitochondrial outer membrane, and the matching historical entry carries the same localization annotation. The support is chiefly transferred or computationally inferred rather than direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The GTPase-rich sequence and C-terminal hydrophobic membrane anchor support a membrane-associated protein, but those features alone do not distinguish the mitochondrial outer membrane from the nuclear envelope.",
    "missing_item_specific_fact": "The protein-specific association of MIRO-1/Rhot1 with the mitochondrial outer membrane is needed to select C; that localization is not supplied in the question.",
    "reason": "The sequence offers clues to protein architecture and membrane association, but identifying the correct organelle requires protein-specific localization knowledge or an external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence has no general targeting feature that makes the nuclear envelope a comparably supported choice; the external sequence-matched annotation supports C."
  },
  "important_caveats": [
    "The reviewed localization annotation is transferred from UniProtKB:Q8IXI2 (ECO:0000250), while the GO mitochondrial outer membrane annotation is marked ISS; neither excerpt establishes direct experimental localization of this rat sequence.",
    "The source snapshot used by the author is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A1L1L6 (MIRO1_RAT) annotates the subcellular location as 'Mitochondrion outer membrane' with topology 'Single-pass type IV membrane protein' (C5, H2). GO annotation GO:0005741 (mitochondrial outer membrane) is present (C8, H5). The protein is named 'Mitochondrial Rho GTPase' (C4, H1). The evidence code is ECO:0000250 / ISS:UniProtKB, indicating inference by similarity to human MIRO1 (Q8IXI2) rather than direct experimental evidence for this specific rat sequence. However, MIRO1 localization to the mitochondrial outer membrane is well-established experimentally in the human ortholog and broadly in the literature. The annotation is computational in this specific entry but rests on a well-characterized protein family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains three recognizable functional modules: (1) an N-terminal Ras-superfamily GTPase domain (GKT, NKxD, SAK, NxxD motifs), (2) two EF-hand calcium-binding domains in the middle region (DxDxDGxDG patterns), and (3) a C-terminal hydrophobic single-pass transmembrane anchor. This tripartite architecture (GTPase + EF-hands + C-terminal TM) is the hallmark of MIRO proteins, which are textbook examples of mitochondrial outer membrane proteins regulating mitochondrial transport along microtubules. The C-terminal type-IV topology (N-terminus cytoplasmic) is consistent with outer-membrane anchoring rather than inner-membrane insertion. Distractors are eliminable by domain logic: nematocyst (D) is a cnidarian stinging organelle with no GTPase/EF-hand architecture; vitelline envelope (B) is an egg-coat glycoprotein structure, not a GTPase; nuclear envelope (A) proteins carry NLS motifs, nucleoporin FG-repeats, or lamina-binding domains, none of which are present.


**Missing item-specific fact**

> None strictly required. The final step—MIRO family → mitochondrial outer membrane—is well-established cell biology, though a model unfamiliar with MIRO proteins might hesitate between 'mitochondrial membrane' options. No experimental measurement or obscure annotation beyond standard domain-to-localization inference is needed.


**Reason**

> A knowledgeable model can reason from the GTPase + EF-hand + C-terminal TM architecture to the MIRO protein family and then to mitochondrial outer membrane localization using general cell biology. The three distractors are eliminated by incompatible domain architectures and organismal context (a vertebrate GTPase cannot reside in a cnidarian nematocyst or an egg coat).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (nuclear envelope, vitelline envelope, nematocyst) are clearly incompatible with the observed GTPase/EF-hand/TM architecture. No other supplied option is defensible.


### Important caveats

- The UniProt annotation for this rat entry (A1L1L6) uses evidence code ECO:0000250 (inferred by similarity to human Q8IXI2), not direct experimental evidence for the rat protein. The human ortholog MIRO1 is experimentally well-characterized as an outer-membrane protein.
- The organism (Rattus norvegicus) is not stated in the question; the model must infer vertebrate origin from the sequence itself. This does not affect answerability because the domain architecture is diagnostic regardless.
- The reviewer-only accession and metadata were absent from the evaluated model input; the model must work from the raw sequence and choices alone.
- The GO annotation evidence type in the current snapshot is ISS (sequence similarity) while the historical snapshot (entry v147) lists ISO:RGD; both are computational inferences, not direct experiments on this rat protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains three recognizable functional modules: (1) an N-terminal Ras-superfamily GTPase domain (GKT, NKxD, SAK, NxxD motifs), (2) two EF-hand calcium-binding domains in the middle region (DxDxDGxDG patterns), and (3) a C-terminal hydrophobic single-pass transmembrane anchor. This tripartite architecture (GTPase + EF-hands + C-terminal TM) is the hallmark of MIRO proteins, which are textbook examples of mitochondrial outer membrane proteins regulating mitochondrial transport along microtubules. The C-terminal type-IV topology (N-terminus cytoplasmic) is consistent with outer-membrane anchoring rather than inner-membrane insertion. Distractors are eliminable by domain logic: nematocyst (D) is a cnidarian stinging organelle with no GTPase/EF-hand architecture; vitelline envelope (B) is an egg-coat glycoprotein structure, not a GTPase; nuclear envelope (A) proteins carry NLS motifs, nucleoporin FG-repeats, or lamina-binding domains, none of which are present.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The final step—MIRO family → mitochondrial outer membrane—is well-established cell biology, though a model unfamiliar with MIRO proteins might hesitate between 'mitochondrial membrane' options. No experimental measurement or obscure annotation beyond standard domain-to-localization inference is needed.",
    "reason": "A knowledgeable model can reason from the GTPase + EF-hand + C-terminal TM architecture to the MIRO protein family and then to mitochondrial outer membrane localization using general cell biology. The three distractors are eliminated by incompatible domain architectures and organismal context (a vertebrate GTPase cannot reside in a cnidarian nematocyst or an egg coat)."
  },
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A1L1L6 (MIRO1_RAT) annotates the subcellular location as 'Mitochondrion outer membrane' with topology 'Single-pass type IV membrane protein' (C5, H2). GO annotation GO:0005741 (mitochondrial outer membrane) is present (C8, H5). The protein is named 'Mitochondrial Rho GTPase' (C4, H1). The evidence code is ECO:0000250 / ISS:UniProtKB, indicating inference by similarity to human MIRO1 (Q8IXI2) rather than direct experimental evidence for this specific rat sequence. However, MIRO1 localization to the mitochondrial outer membrane is well-established experimentally in the human ortholog and broadly in the literature. The annotation is computational in this specific entry but rests on a well-characterized protein family."
  },
  "important_caveats": [
    "The UniProt annotation for this rat entry (A1L1L6) uses evidence code ECO:0000250 (inferred by similarity to human Q8IXI2), not direct experimental evidence for the rat protein. The human ortholog MIRO1 is experimentally well-characterized as an outer-membrane protein.",
    "The organism (Rattus norvegicus) is not stated in the question; the model must infer vertebrate origin from the sequence itself. This does not affect answerability because the domain architecture is diagnostic regardless.",
    "The reviewer-only accession and metadata were absent from the evaluated model input; the model must work from the raw sequence and choices alone.",
    "The GO annotation evidence type in the current snapshot is ISS (sequence similarity) while the historical snapshot (entry v147) lists ISO:RGD; both are computational inferences, not direct experiments on this rat protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (nuclear envelope, vitelline envelope, nematocyst) are clearly incompatible with the observed GTPase/EF-hand/TM architecture. No other supplied option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A1L1L6 (MIRO1_RAT) annotates the subcellular location as 'Mitochondrion outer membrane' with topology 'Single-pass type IV membrane protein' (C5, H2). GO annotation GO:0005741 (mitochondrial outer membrane) is present (C8, H5). The protein is named 'Mitochondrial Rho GTPase' (C4, H1). The evidence code is ECO:0000250 / ISS:UniProtKB, indicating inference by similarity to human MIRO1 (Q8IXI2) rather than direct experimental evidence for this specific rat sequence. However, MIRO1 localization to the mitochondrial outer membrane is well-established experimentally in the human ortholog and broadly in the literature. The annotation is computational in this specific entry but rests on a well-characterized protein family.",
    "evidence_ids": ["C4", "C5", "C8", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains three recognizable functional modules: (1) an N-terminal Ras-superfamily GTPase domain (GKT, NKxD, SAK, NxxD motifs), (2) two EF-hand calcium-binding domains in the middle region (DxDxDGxDG patterns), and (3) a C-terminal hydrophobic single-pass transmembrane anchor. This tripartite architecture (GTPase + EF-hands + C-terminal TM) is the hallmark of MIRO proteins, which are textbook examples of mitochondrial outer membrane proteins regulating mitochondrial transport along microtubules. The C-terminal type-IV topology (N-terminus cytoplasmic) is consistent with outer-membrane anchoring rather than inner-membrane insertion. Distractors are eliminable by domain logic: nematocyst (D) is a cnidarian stinging organelle with no GTPase/EF-hand architecture; vitelline envelope (B) is an egg-coat glycoprotein structure, not a GTPase; nuclear envelope (A) proteins carry NLS motifs, nucleoporin FG-repeats, or lamina-binding domains, none of which are present.",
    "missing_item_specific_fact": "None strictly required. The final step—MIRO family → mitochondrial outer membrane—is well-established cell biology, though a model unfamiliar with MIRO proteins might hesitate between 'mitochondrial membrane' options. No experimental measurement or obscure annotation beyond standard domain-to-localization inference is needed.",
    "reason": "A knowledgeable model can reason from the GTPase + EF-hand + C-terminal TM architecture to the MIRO protein family and then to mitochondrial outer membrane localization using general cell biology. The three distractors are eliminated by incompatible domain architectures and organismal context (a vertebrate GTPase cannot reside in a cnidarian nematocyst or an egg coat)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (nuclear envelope, vitelline envelope, nematocyst) are clearly incompatible with the observed GTPase/EF-hand/TM architecture. No other supplied option is defensible."
  },
  "important_caveats": [
    "The UniProt annotation for this rat entry (A1L1L6) uses evidence code ECO:0000250 (inferred by similarity to human Q8IXI2), not direct experimental evidence for the rat protein. The human ortholog MIRO1 is experimentally well-characterized as an outer-membrane protein.",
    "The organism (Rattus norvegicus) is not stated in the question; the model must infer vertebrate origin from the sequence itself. This does not affect answerability because the domain architecture is diagnostic regardless.",
    "The reviewer-only accession and metadata were absent from the evaluated model input; the model must work from the raw sequence and choices alone.",
    "The GO annotation evidence type in the current snapshot is ISS (sequence similarity) while the historical snapshot (entry v147) lists ISO:RGD; both are computational inferences, not direct experiments on this rat protein."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the protein to the mitochondrial outer membrane. The GO annotation is computationally transferred (ISS), and the subcellular-location annotation is based on another UniProt protein, so this supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the characteristic organization of a Miro/RHOT-family mitochondrial Rho GTPase: GTPase motifs, EF-hand-like regions, and a hydrophobic C-terminal membrane anchor. Knowledge of this protein family and its membrane-anchoring pattern provides a meaningful basis for choosing the mitochondrial outer membrane over the nuclear envelope, vitelline envelope, or nematocyst.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence architecture distinguishes the offered mitochondrial option without requiring the exact protein's database annotation. The inference is strong but does not itself constitute experimental localization evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the family-level sequence features favor mitochondrial outer-membrane localization; the other choices are not comparably supported.


### Important caveats

- The supplied evidence supports the key through annotations that are computationally transferred or based on a homolog, rather than demonstrating direct experimental localization for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristic organization of a Miro/RHOT-family mitochondrial Rho GTPase: GTPase motifs, EF-hand-like regions, and a hydrophobic C-terminal membrane anchor. Knowledge of this protein family and its membrane-anchoring pattern provides a meaningful basis for choosing the mitochondrial outer membrane over the nuclear envelope, vitelline envelope, or nematocyst.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence architecture distinguishes the offered mitochondrial option without requiring the exact protein's database annotation. The inference is strong but does not itself constitute experimental localization evidence."
  },
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the mitochondrial outer membrane. The GO annotation is computationally transferred (ISS), and the subcellular-location annotation is based on another UniProt protein, so this supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied evidence supports the key through annotations that are computationally transferred or based on a homolog, rather than demonstrating direct experimental localization for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the family-level sequence features favor mitochondrial outer-membrane localization; the other choices are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the mitochondrial outer membrane. The GO annotation is computationally transferred (ISS), and the subcellular-location annotation is based on another UniProt protein, so this supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "C8", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the characteristic organization of a Miro/RHOT-family mitochondrial Rho GTPase: GTPase motifs, EF-hand-like regions, and a hydrophobic C-terminal membrane anchor. Knowledge of this protein family and its membrane-anchoring pattern provides a meaningful basis for choosing the mitochondrial outer membrane over the nuclear envelope, vitelline envelope, or nematocyst.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence architecture distinguishes the offered mitochondrial option without requiring the exact protein's database annotation. The inference is strong but does not itself constitute experimental localization evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the family-level sequence features favor mitochondrial outer-membrane localization; the other choices are not comparably supported."
  },
  "important_caveats": [
    "The supplied evidence supports the key through annotations that are computationally transferred or based on a homolog, rather than demonstrating direct experimental localization for this exact protein."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A1L1L6, MIRO1_RAT) annotates the protein as 'Mitochondrial Rho GTPase' (MIRO-1) with subcellular location 'Mitochondrion outer membrane; Single-pass type IV membrane protein' and GO:0005741 (mitochondrial outer membrane). However, the evidence code is ECO:0000250/ISS:UniProtKB (inferred from similarity to human Q8IXI2), not direct experimental evidence. The protein name itself contains 'Mitochondrial,' and the annotation is consistent with well-established family knowledge about MIRO/RHOT proteins. The key is supported by annotation, though the annotation is computational inference from homolog similarity rather than independent experimental validation.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays recognizable features of the MIRO/RHOT protein family: (1) Two Ras-superfamily GTPase domains with identifiable P-loop (GKTSLIMSL, matching GxxxxGK&#91;ST&#93; motif), NKxD switch-region motifs (NKSDLVEYSS), and downstream effector-binding regions; (2) Two EF-hand calcium-binding domains in the central region (recognizable by the DxDxDGxD loop patterns in 'DVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLK'); (3) A C-terminal hydrophobic transmembrane segment ('GATVFAVVGFAMYRALLKQR') consistent with a single-pass TM anchor. The combination of two GTPase domains + two EF-hands + C-terminal TM is the hallmark architecture of MIRO/RHOT proteins, a well-characterized family of mitochondrial outer membrane proteins involved in mitochondrial trafficking. This family-level knowledge allows elimination of distractors: nematocyst (D) is a cnidarian-specific organelle, impossible in a mammalian sequence; vitelline envelope (B) is an extracellular egg-coat glycoprotein structure, inconsistent with an intracellular GTPase; nuclear envelope (A) would require nuclear targeting signals absent here. The TM anchor at the C-terminus is specifically associated with outer membrane insertion (type IV topology), not inner membrane or matrix localization.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the Ras-like GTPase motifs, EF-hand calcium-binding domains, and C-terminal hydrophobic TM segment from the sequence. The combination of these three domain types is a well-established signature of the MIRO/RHOT protein family, which is broadly known from other species (human, Drosophila, yeast) to localize to the mitochondrial outer membrane. This family-level inference meaningfully distinguishes choice C from the alternatives without requiring recall of this specific rat protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are highly distinct: nuclear envelope (A), vitelline envelope (B), mitochondrial outer membrane (C), and nematocyst (D). The protein's domain architecture (GTPase + EF-hand + TM) and mammalian origin clearly point to C and eliminate B (egg coat glycoprotein), D (cnidarian stinging organelle), and A (would require NLS or nuclear membrane targeting). No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation for mitochondrial outer membrane is based on ISS/ECO:0000250 (similarity to human MIRO1), not direct experimental evidence for this rat sequence. However, the family-level inference from transferable knowledge is strong and well-supported.
- The protein also carries GO annotations for cytoplasm, cytoplasmic stress granule, and ribonucleoprotein complex (ISO:RGD), but these are secondary locations and the question asks for the primary cellular component.
- The reviewer identified the accession A1L1L6 from dataset metadata, but the model was given only the sequence. The reasoning above relies solely on sequence features and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays recognizable features of the MIRO/RHOT protein family: (1) Two Ras-superfamily GTPase domains with identifiable P-loop (GKTSLIMSL, matching GxxxxGK[ST] motif), NKxD switch-region motifs (NKSDLVEYSS), and downstream effector-binding regions; (2) Two EF-hand calcium-binding domains in the central region (recognizable by the DxDxDGxD loop patterns in 'DVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLK'); (3) A C-terminal hydrophobic transmembrane segment ('GATVFAVVGFAMYRALLKQR') consistent with a single-pass TM anchor. The combination of two GTPase domains + two EF-hands + C-terminal TM is the hallmark architecture of MIRO/RHOT proteins, a well-characterized family of mitochondrial outer membrane proteins involved in mitochondrial trafficking. This family-level knowledge allows elimination of distractors: nematocyst (D) is a cnidarian-specific organelle, impossible in a mammalian sequence; vitelline envelope (B) is an extracellular egg-coat glycoprotein structure, inconsistent with an intracellular GTPase; nuclear envelope (A) would require nuclear targeting signals absent here. The TM anchor at the C-terminus is specifically associated with outer membrane insertion (type IV topology), not inner membrane or matrix localization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the Ras-like GTPase motifs, EF-hand calcium-binding domains, and C-terminal hydrophobic TM segment from the sequence. The combination of these three domain types is a well-established signature of the MIRO/RHOT protein family, which is broadly known from other species (human, Drosophila, yeast) to localize to the mitochondrial outer membrane. This family-level inference meaningfully distinguishes choice C from the alternatives without requiring recall of this specific rat protein's database entry."
  },
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A1L1L6, MIRO1_RAT) annotates the protein as 'Mitochondrial Rho GTPase' (MIRO-1) with subcellular location 'Mitochondrion outer membrane; Single-pass type IV membrane protein' and GO:0005741 (mitochondrial outer membrane). However, the evidence code is ECO:0000250/ISS:UniProtKB (inferred from similarity to human Q8IXI2), not direct experimental evidence. The protein name itself contains 'Mitochondrial,' and the annotation is consistent with well-established family knowledge about MIRO/RHOT proteins. The key is supported by annotation, though the annotation is computational inference from homolog similarity rather than independent experimental validation."
  },
  "important_caveats": [
    "The UniProt annotation for mitochondrial outer membrane is based on ISS/ECO:0000250 (similarity to human MIRO1), not direct experimental evidence for this rat sequence. However, the family-level inference from transferable knowledge is strong and well-supported.",
    "The protein also carries GO annotations for cytoplasm, cytoplasmic stress granule, and ribonucleoprotein complex (ISO:RGD), but these are secondary locations and the question asks for the primary cellular component.",
    "The reviewer identified the accession A1L1L6 from dataset metadata, but the model was given only the sequence. The reasoning above relies solely on sequence features and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are highly distinct: nuclear envelope (A), vitelline envelope (B), mitochondrial outer membrane (C), and nematocyst (D). The protein's domain architecture (GTPase + EF-hand + TM) and mammalian origin clearly point to C and eliminate B (egg coat glycoprotein), D (cnidarian stinging organelle), and A (would require NLS or nuclear membrane targeting). No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A1L1L6, MIRO1_RAT) annotates the protein as 'Mitochondrial Rho GTPase' (MIRO-1) with subcellular location 'Mitochondrion outer membrane; Single-pass type IV membrane protein' and GO:0005741 (mitochondrial outer membrane). However, the evidence code is ECO:0000250/ISS:UniProtKB (inferred from similarity to human Q8IXI2), not direct experimental evidence. The protein name itself contains 'Mitochondrial,' and the annotation is consistent with well-established family knowledge about MIRO/RHOT proteins. The key is supported by annotation, though the annotation is computational inference from homolog similarity rather than independent experimental validation.",
    "evidence_ids": ["C5", "C8", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays recognizable features of the MIRO/RHOT protein family: (1) Two Ras-superfamily GTPase domains with identifiable P-loop (GKTSLIMSL, matching GxxxxGK[ST] motif), NKxD switch-region motifs (NKSDLVEYSS), and downstream effector-binding regions; (2) Two EF-hand calcium-binding domains in the central region (recognizable by the DxDxDGxD loop patterns in 'DVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLK'); (3) A C-terminal hydrophobic transmembrane segment ('GATVFAVVGFAMYRALLKQR') consistent with a single-pass TM anchor. The combination of two GTPase domains + two EF-hands + C-terminal TM is the hallmark architecture of MIRO/RHOT proteins, a well-characterized family of mitochondrial outer membrane proteins involved in mitochondrial trafficking. This family-level knowledge allows elimination of distractors: nematocyst (D) is a cnidarian-specific organelle, impossible in a mammalian sequence; vitelline envelope (B) is an extracellular egg-coat glycoprotein structure, inconsistent with an intracellular GTPase; nuclear envelope (A) would require nuclear targeting signals absent here. The TM anchor at the C-terminus is specifically associated with outer membrane insertion (type IV topology), not inner membrane or matrix localization.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the Ras-like GTPase motifs, EF-hand calcium-binding domains, and C-terminal hydrophobic TM segment from the sequence. The combination of these three domain types is a well-established signature of the MIRO/RHOT protein family, which is broadly known from other species (human, Drosophila, yeast) to localize to the mitochondrial outer membrane. This family-level inference meaningfully distinguishes choice C from the alternatives without requiring recall of this specific rat protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are highly distinct: nuclear envelope (A), vitelline envelope (B), mitochondrial outer membrane (C), and nematocyst (D). The protein's domain architecture (GTPase + EF-hand + TM) and mammalian origin clearly point to C and eliminate B (egg coat glycoprotein), D (cnidarian stinging organelle), and A (would require NLS or nuclear membrane targeting). No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for mitochondrial outer membrane is based on ISS/ECO:0000250 (similarity to human MIRO1), not direct experimental evidence for this rat sequence. However, the family-level inference from transferable knowledge is strong and well-supported.",
    "The protein also carries GO annotations for cytoplasm, cytoplasmic stress granule, and ribonucleoprotein complex (ISO:RGD), but these are secondary locations and the question asks for the primary cellular component.",
    "The reviewer identified the accession A1L1L6 from dataset metadata, but the model was given only the sequence. The reasoning above relies solely on sequence features and family-level knowledge."
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
  "requested_accession": "A1L1L6",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "a7756948eb1b32092363ec26631ecb58f113dac469b17c79f967f052e05b6ef8",
  "benchmark_sequence_length": 631,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 149,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-02-06",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "current_source_sequence_sha256": "a7756948eb1b32092363ec26631ecb58f113dac469b17c79f967f052e05b6ef8",
  "current_source_sequence_length": 631,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 147,
  "selected_historical_version": {
    "accession": "A1L1L6",
    "database": "Swiss-Prot",
    "entryVersion": 147,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MIRO1_RAT",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "selected_historical_source_sequence_sha256": "a7756948eb1b32092363ec26631ecb58f113dac469b17c79f967f052e05b6ef8",
  "selected_historical_source_sequence_length": 631,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 147,
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A1L1L6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":149,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-02-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Rat\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAI29124.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"1307023\",\"source\":\"RGD\"}],\"value\":\"Ras homolog gene family member T1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IXI2\",\"source\":\"UniProtKB\"}],\"value\":\"3.6.5.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PIRNR037488\",\"source\":\"PIRNR\"}],\"value\":\"Mitochondrial Rho GTPase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"MIRO-1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IXI2\",\"source\":\"UniProtKB\"}],\"value\":\"Colocalizes with MGARP and RHOT2 at the mitochondria\"}]},\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IXI2\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0172\",\"value\":\"Mitochondrion outer membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8IXI2\",\"source\":\"UniProtKB\"}],\"id\":\"SL-9908\",\"value\":\"Single-pass type IV membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "json_pointer": "/uniProtKBCrossReferences/22",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005737\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:RGD\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "json_pointer": "/uniProtKBCrossReferences/23",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0010494\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytoplasmic stress granule\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:RGD\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "json_pointer": "/uniProtKBCrossReferences/24",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005741\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrial outer membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A1L1L6.json",
  "source_sha256": "c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3",
  "retrieved_utc": "2026-11-02T04:26:46.803603+00:00",
  "json_pointer": "/uniProtKBCrossReferences/25",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:1990904\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:ribonucleoprotein complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISO:RGD\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   MIRO1_RAT               Reviewed;         631 AA.\nAC   A1L1L6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-FEB-2007, sequence version 1.\nDT   28-JAN-2026, entry version 147.\nDE   RecName: Full=Mitochondrial Rho GTPase {ECO:0000255|PIRNR:PIRNR037488};\nDE            Short=MIRO-1 {ECO:0000305};\nDE            EC=3.6.5.- {ECO:0000250|UniProtKB:Q8IXI2};\nDE   AltName: Full=Ras homolog gene family member T1 {ECO:0000312|RGD:1307023};\nGN   Name=Rhot1 {ECO:0000312|RGD:1307023};\nGN   Synonyms=Rnf135 {ECO:0000312|RGD:1307023};\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116 {ECO:0000312|EMBL:AAI29124.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 147,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "source_locator": "lines 72-75",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Mitochondrion outer membrane\nCC       {ECO:0000250|UniProtKB:Q8IXI2}; Single-pass type IV membrane protein\nCC       {ECO:0000250|UniProtKB:Q8IXI2}. Note=Colocalizes with MGARP and RHOT2\nCC       at the mitochondria. {ECO:0000250|UniProtKB:Q8IXI2}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 147,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "source_locator": "lines 113-113",
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 147,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "source_locator": "lines 114-114",
  "excerpt": "DR   GO; GO:0010494; C:cytoplasmic stress granule; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 147,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "source_locator": "lines 115-115",
  "excerpt": "DR   GO; GO:0005741; C:mitochondrial outer membrane; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 147,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147",
  "source_sha256": "f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e",
  "retrieved_utc": "2026-11-02T04:26:49.663865+00:00",
  "source_locator": "lines 116-116",
  "excerpt": "DR   GO; GO:1990904; C:ribonucleoprotein complex; ISO:RGD.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 147,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 58026-58039",
  "excerpt": "[Term]\nid: GO:0005635\nname: nuclear envelope\nnamespace: cellular_component\nalt_id: GO:0005636\ndef: \"The double lipid bilayer that encloses the nucleus, separating its contents from the cytoplasm. It consists of an inner and outer nuclear membrane, with an intermembrane space (20-40 nm wide, also called the perinuclear space) between them. The envelope is supported by the nuclear lamina and contains nuclear pore complexes, which regulate molecular transport.\" [ISBN:0198547684, PMID:16164970]\nsubset: goslim_chembl\nsubset: goslim_generic\nsubset: goslim_plant\nxref: Wikipedia:Nuclear_envelope\nis_a: GO:0031967 ! organelle envelope\nrelationship: part_of GO:0005634 ! nucleus\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005635"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 59009-59021",
  "excerpt": "[Term]\nid: GO:0005741\nname: mitochondrial outer membrane\nnamespace: cellular_component\ndef: \"The outer, i.e. cytoplasm-facing, lipid bilayer of the mitochondrial envelope.\" [GOC:ai]\nsynonym: \"mitochondrion outer membrane\" EXACT []\nsynonym: \"outer mitochondrial membrane\" EXACT []\nsynonym: \"outer mitochondrion membrane\" EXACT []\nxref: NIF_Subcellular:sao1289741256\nxref: Wikipedia:Outer_mitochondrial_membrane\nis_a: GO:0031966 ! mitochondrial membrane\nis_a: GO:0031968 ! organelle outer membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0005741"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 234754-234763",
  "excerpt": "[Term]\nid: GO:0042151\nname: nematocyst\nnamespace: cellular_component\ndef: \"An organelle found in cnidoblast (nematoblast) cells. When matured, these stinging organelles store toxins and can deliver them when the cnidocil (a short extension of the cnidocyst) is stimulated by a prey or another stimulus.\" [DOI:10.1139/z02-135, GOC:jl]\nsynonym: \"cnidocyst\" EXACT []\nxref: Wikipedia:Cnidocyte\nis_a: GO:0043232 ! intracellular membraneless organelle\nrelationship: part_of GO:0005938 ! cell cortex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0042151"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 347268-347275",
  "excerpt": "[Term]\nid: GO:0060388\nname: vitelline envelope\nnamespace: cellular_component\ndef: \"A glycoprotein-based structure that lies outside the plasma membrane and surrounds the egg before fertilization.\" [GOC:dph, ISBN:0878932437]\nsynonym: \"fertilization membrane\" RELATED []\nis_a: GO:0035805 ! egg coat\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0060388"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 126. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
