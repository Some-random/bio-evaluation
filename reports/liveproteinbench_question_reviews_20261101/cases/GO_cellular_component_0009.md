# GO_cellular_component_0009

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — mitochondrion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. SCF ubiquitin ligase complex
B. inclusion body
C. mitochondrion
D. egg chorion
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

> The exact sequence matches a UniProt entry annotated as mitochondrial. The location annotation is supported by similarity-based evidence, and the GO annotation is inferred by sequence similarity; these support the key but are not direct experimental localization evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with an Arg-rich, Ser/Thr-containing N-terminal region lacking acidic residues, a pattern consistent with a mitochondrial targeting peptide. This provides a meaningful reason to favor mitochondrion over the listed alternatives.


**Missing item-specific fact**

> No external protein-specific fact is essential to distinguish these choices from the sequence, though direct experimental localization would be needed to establish the protein’s localization independently.


**Reason**

> A recognizable targeting-signal pattern in the supplied sequence supports a biological inference toward mitochondria; this is more than identifying the exact protein or relying on a database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The N-terminal targeting-signal pattern favors mitochondrion, while the other options are not comparably supported by the sequence.


### Important caveats

- The reviewer-only database evidence is not information supplied to the original model.
- The cited localization annotation is similarity-based rather than direct experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with an Arg-rich, Ser/Thr-containing N-terminal region lacking acidic residues, a pattern consistent with a mitochondrial targeting peptide. This provides a meaningful reason to favor mitochondrion over the listed alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external protein-specific fact is essential to distinguish these choices from the sequence, though direct experimental localization would be needed to establish the protein’s localization independently.",
    "reason": "A recognizable targeting-signal pattern in the supplied sequence supports a biological inference toward mitochondria; this is more than identifying the exact protein or relying on a database lookup."
  },
  "case_id": "GO_cellular_component_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as mitochondrial. The location annotation is supported by similarity-based evidence, and the GO annotation is inferred by sequence similarity; these support the key but are not direct experimental localization evidence."
  },
  "important_caveats": [
    "The reviewer-only database evidence is not information supplied to the original model.",
    "The cited localization annotation is similarity-based rather than direct experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The N-terminal targeting-signal pattern favors mitochondrion, while the other options are not comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as mitochondrial. The location annotation is supported by similarity-based evidence, and the GO annotation is inferred by sequence similarity; these support the key but are not direct experimental localization evidence.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with an Arg-rich, Ser/Thr-containing N-terminal region lacking acidic residues, a pattern consistent with a mitochondrial targeting peptide. This provides a meaningful reason to favor mitochondrion over the listed alternatives.",
    "missing_item_specific_fact": "No external protein-specific fact is essential to distinguish these choices from the sequence, though direct experimental localization would be needed to establish the protein’s localization independently.",
    "reason": "A recognizable targeting-signal pattern in the supplied sequence supports a biological inference toward mitochondria; this is more than identifying the exact protein or relying on a database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The N-terminal targeting-signal pattern favors mitochondrion, while the other options are not comparably supported by the sequence."
  },
  "important_caveats": [
    "The reviewer-only database evidence is not information supplied to the original model.",
    "The cited localization annotation is similarity-based rather than direct experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q0CPG9) annotates this protein as 'Dihydroxy-acid dehydratase astD, mitochondrial' (C4) with SUBCELLULAR LOCATION: Mitochondrion (C5, H3). The GO annotation is GO:0005739 mitochondrion (C6, H4). The evidence code is ISS (ECO:0000250), inferred from similarity to yeast DHAD P39522, rather than direct experimental localization of this specific Aspergillus protein. However, the protein name, the DHAD function (EC 4.2.1.9, confirmed by PubMed:29995859), and the well-established mitochondrial localization of branched-chain amino acid biosynthesis enzymes in eukaryotes collectively support the answer. The 'Precursor' flag (C4) is consistent with a cleavable mitochondrial targeting peptide.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved dihydroxy-acid dehydratase (DHAD) active-site motif 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELE' and the 'ACGGMYTANTLATAIETMGMTVPGSSSC' region, which are diagnostic of the DHAD family. In eukaryotes, branched-chain amino acid biosynthesis (valine, leucine, isoleucine), for which DHAD is the penultimate enzyme, occurs exclusively in the mitochondrial matrix. The N-terminal ~50 residues are enriched in Arg, Ser, and Thr with a notable absence of acidic residues, consistent with a mitochondrial targeting presequence, and the entry is flagged as 'Precursor.' The other options are eliminable by general biology: no F-box, Skp1, or cullin motifs are present (rules out SCF complex); inclusion bodies are nonspecific aggregates, not a functional compartment for an enzyme; and egg chorion is an extracellular structure in animals, irrelevant for a fungal protein.


**Missing item-specific fact**

> None critical. The DHAD domain identification and the established mitochondrial localization of eukaryotic branched-chain amino acid biosynthesis are general biological knowledge. The N-terminal targeting-sequence features are visible in the supplied sequence.


**Reason**

> A model with knowledge of enzyme families and organelle-specific metabolic pathways can identify the DHAD domain from the sequence, recall that DHAD functions in the mitochondrial branched-chain amino acid pathway, and note the N-terminal presequence-like features. The distractors are readily excluded by domain architecture and organismal context (fungal protein vs. animal egg chorion; absence of SCF subunit motifs).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span vastly different cellular contexts (a multi-protein degradation complex, a nonspecific aggregation compartment, an organelle, and an extracellular animal structure). Only 'mitochondrion' is consistent with the identified DHAD function and the fungal organism. The other three are not defensible for this protein.


### Important caveats

- The mitochondrial localization annotation is ISS (inferred from similarity to yeast DHAD P39522), not a direct experimental measurement on this Aspergillus terreus protein. However, DHAD mitochondrial localization is a deeply conserved and well-established fact across eukaryotes.
- The GO annotation carries IEA (Inferred from Electronic Annotation) status, meaning it was propagated computationally rather than curated from direct evidence for this specific entry.
- Recognizing the DHAD domain from raw sequence requires familiarity with enzyme-family motifs; this is general biological knowledge but not trivial for all models.
- The reviewer-only evidence was not available to the evaluated model; the reasoning path described relies on general knowledge of DHAD biology and mitochondrial targeting sequences.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved dihydroxy-acid dehydratase (DHAD) active-site motif 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELE' and the 'ACGGMYTANTLATAIETMGMTVPGSSSC' region, which are diagnostic of the DHAD family. In eukaryotes, branched-chain amino acid biosynthesis (valine, leucine, isoleucine), for which DHAD is the penultimate enzyme, occurs exclusively in the mitochondrial matrix. The N-terminal ~50 residues are enriched in Arg, Ser, and Thr with a notable absence of acidic residues, consistent with a mitochondrial targeting presequence, and the entry is flagged as 'Precursor.' The other options are eliminable by general biology: no F-box, Skp1, or cullin motifs are present (rules out SCF complex); inclusion bodies are nonspecific aggregates, not a functional compartment for an enzyme; and egg chorion is an extracellular structure in animals, irrelevant for a fungal protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The DHAD domain identification and the established mitochondrial localization of eukaryotic branched-chain amino acid biosynthesis are general biological knowledge. The N-terminal targeting-sequence features are visible in the supplied sequence.",
    "reason": "A model with knowledge of enzyme families and organelle-specific metabolic pathways can identify the DHAD domain from the sequence, recall that DHAD functions in the mitochondrial branched-chain amino acid pathway, and note the N-terminal presequence-like features. The distractors are readily excluded by domain architecture and organismal context (fungal protein vs. animal egg chorion; absence of SCF subunit motifs)."
  },
  "case_id": "GO_cellular_component_0009",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q0CPG9) annotates this protein as 'Dihydroxy-acid dehydratase astD, mitochondrial' (C4) with SUBCELLULAR LOCATION: Mitochondrion (C5, H3). The GO annotation is GO:0005739 mitochondrion (C6, H4). The evidence code is ISS (ECO:0000250), inferred from similarity to yeast DHAD P39522, rather than direct experimental localization of this specific Aspergillus protein. However, the protein name, the DHAD function (EC 4.2.1.9, confirmed by PubMed:29995859), and the well-established mitochondrial localization of branched-chain amino acid biosynthesis enzymes in eukaryotes collectively support the answer. The 'Precursor' flag (C4) is consistent with a cleavable mitochondrial targeting peptide."
  },
  "important_caveats": [
    "The mitochondrial localization annotation is ISS (inferred from similarity to yeast DHAD P39522), not a direct experimental measurement on this Aspergillus terreus protein. However, DHAD mitochondrial localization is a deeply conserved and well-established fact across eukaryotes.",
    "The GO annotation carries IEA (Inferred from Electronic Annotation) status, meaning it was propagated computationally rather than curated from direct evidence for this specific entry.",
    "Recognizing the DHAD domain from raw sequence requires familiarity with enzyme-family motifs; this is general biological knowledge but not trivial for all models.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning path described relies on general knowledge of DHAD biology and mitochondrial targeting sequences."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span vastly different cellular contexts (a multi-protein degradation complex, a nonspecific aggregation compartment, an organelle, and an extracellular animal structure). Only 'mitochondrion' is consistent with the identified DHAD function and the fungal organism. The other three are not defensible for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0009",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q0CPG9) annotates this protein as 'Dihydroxy-acid dehydratase astD, mitochondrial' (C4) with SUBCELLULAR LOCATION: Mitochondrion (C5, H3). The GO annotation is GO:0005739 mitochondrion (C6, H4). The evidence code is ISS (ECO:0000250), inferred from similarity to yeast DHAD P39522, rather than direct experimental localization of this specific Aspergillus protein. However, the protein name, the DHAD function (EC 4.2.1.9, confirmed by PubMed:29995859), and the well-established mitochondrial localization of branched-chain amino acid biosynthesis enzymes in eukaryotes collectively support the answer. The 'Precursor' flag (C4) is consistent with a cleavable mitochondrial targeting peptide.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved dihydroxy-acid dehydratase (DHAD) active-site motif 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELE' and the 'ACGGMYTANTLATAIETMGMTVPGSSSC' region, which are diagnostic of the DHAD family. In eukaryotes, branched-chain amino acid biosynthesis (valine, leucine, isoleucine), for which DHAD is the penultimate enzyme, occurs exclusively in the mitochondrial matrix. The N-terminal ~50 residues are enriched in Arg, Ser, and Thr with a notable absence of acidic residues, consistent with a mitochondrial targeting presequence, and the entry is flagged as 'Precursor.' The other options are eliminable by general biology: no F-box, Skp1, or cullin motifs are present (rules out SCF complex); inclusion bodies are nonspecific aggregates, not a functional compartment for an enzyme; and egg chorion is an extracellular structure in animals, irrelevant for a fungal protein.",
    "missing_item_specific_fact": "None critical. The DHAD domain identification and the established mitochondrial localization of eukaryotic branched-chain amino acid biosynthesis are general biological knowledge. The N-terminal targeting-sequence features are visible in the supplied sequence.",
    "reason": "A model with knowledge of enzyme families and organelle-specific metabolic pathways can identify the DHAD domain from the sequence, recall that DHAD functions in the mitochondrial branched-chain amino acid pathway, and note the N-terminal presequence-like features. The distractors are readily excluded by domain architecture and organismal context (fungal protein vs. animal egg chorion; absence of SCF subunit motifs)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span vastly different cellular contexts (a multi-protein degradation complex, a nonspecific aggregation compartment, an organelle, and an extracellular animal structure). Only 'mitochondrion' is consistent with the identified DHAD function and the fungal organism. The other three are not defensible for this protein."
  },
  "important_caveats": [
    "The mitochondrial localization annotation is ISS (inferred from similarity to yeast DHAD P39522), not a direct experimental measurement on this Aspergillus terreus protein. However, DHAD mitochondrial localization is a deeply conserved and well-established fact across eukaryotes.",
    "The GO annotation carries IEA (Inferred from Electronic Annotation) status, meaning it was propagated computationally rather than curated from direct evidence for this specific entry.",
    "Recognizing the DHAD domain from raw sequence requires familiarity with enzyme-family motifs; this is general biological knowledge but not trivial for all models.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning path described relies on general knowledge of DHAD biology and mitochondrial targeting sequences."
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

**Accession:** `Q0CPG9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 90. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
"Q0CPG9"
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase astD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/comments/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39522","source":"UniProtKB"}],"id":"SL-0173","value":"Mitochondrion"}}]}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"database":"GO","id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
ID   ASTD_ASPTN              Reviewed;         598 AA.
AC   Q0CPG9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   17-OCT-2006, sequence version 1.
DT   28-JAN-2026, entry version 90.
DE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};
DE            Short=DHAD astD {ECO:0000303|PubMed:29995859};
DE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};
DE   Flags: Precursor;
GN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;
OS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=341663;
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 82-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion {ECO:0000250|UniProtKB:P39522}.
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 113-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IEA:UniProtKB-SubCell.
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 9. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
