# GO_cellular_component_0011

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — mitochondrion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. mitochondrion
B. nucleus
C. egg coat
D. centrosome
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

> The supplied sequence matches the UniProt entry annotated as mitochondrial. The subcellular-location annotation is transferred from another UniProt protein (ECO:0000250), and the GO annotation is by sequence similarity (ISS), so this supports the key but is not direct experimental localization evidence for this protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus is rich in arginine and other basic residues, contains serine/threonine, and has few acidic residues—features consistent with a mitochondrial targeting presequence. This provides a biological basis for favoring mitochondrion among the choices.


**Missing item-specific fact**

> No additional protein-specific fact is required for a defensible sequence-based prediction, though direct experimental localization would be needed to establish localization independently.


**Reason**

> The N-terminal sequence provides a recognizable, biologically plausible targeting signal that distinguishes mitochondria from the listed alternatives; this is more than identifying a database entry or relying only on a predictor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The mitochondrial targeting-like N-terminus favors A; the other options lack a comparably plausible signal in the supplied sequence.


### Important caveats

- The reviewer-only UniProt and GO annotations match the sequence, but their localization evidence is transferred or similarity-based rather than direct experimental evidence for this protein.
- Sequence targeting signals support a prediction, not certainty about the protein's localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus is rich in arginine and other basic residues, contains serine/threonine, and has few acidic residues—features consistent with a mitochondrial targeting presequence. This provides a biological basis for favoring mitochondrion among the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional protein-specific fact is required for a defensible sequence-based prediction, though direct experimental localization would be needed to establish localization independently.",
    "reason": "The N-terminal sequence provides a recognizable, biologically plausible targeting signal that distinguishes mitochondria from the listed alternatives; this is more than identifying a database entry or relying only on a predictor."
  },
  "case_id": "GO_cellular_component_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt entry annotated as mitochondrial. The subcellular-location annotation is transferred from another UniProt protein (ECO:0000250), and the GO annotation is by sequence similarity (ISS), so this supports the key but is not direct experimental localization evidence for this protein."
  },
  "important_caveats": [
    "The reviewer-only UniProt and GO annotations match the sequence, but their localization evidence is transferred or similarity-based rather than direct experimental evidence for this protein.",
    "Sequence targeting signals support a prediction, not certainty about the protein's localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The mitochondrial targeting-like N-terminus favors A; the other options lack a comparably plausible signal in the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt entry annotated as mitochondrial. The subcellular-location annotation is transferred from another UniProt protein (ECO:0000250), and the GO annotation is by sequence similarity (ISS), so this supports the key but is not direct experimental localization evidence for this protein.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus is rich in arginine and other basic residues, contains serine/threonine, and has few acidic residues—features consistent with a mitochondrial targeting presequence. This provides a biological basis for favoring mitochondrion among the choices.",
    "missing_item_specific_fact": "No additional protein-specific fact is required for a defensible sequence-based prediction, though direct experimental localization would be needed to establish localization independently.",
    "reason": "The N-terminal sequence provides a recognizable, biologically plausible targeting signal that distinguishes mitochondria from the listed alternatives; this is more than identifying a database entry or relying only on a predictor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The mitochondrial targeting-like N-terminus favors A; the other options lack a comparably plausible signal in the supplied sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt and GO annotations match the sequence, but their localization evidence is transferred or similarity-based rather than direct experimental evidence for this protein.",
    "Sequence targeting signals support a prediction, not certainty about the protein's localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5, H3) explicitly states subcellular location as 'Mitochondrion' with evidence code ECO:0000250 (ISS, inferred from similarity to P39522, the yeast mitochondrial DHAD Ilv3p). The protein name itself includes 'mitochondrial' (C4, H1). The GO cross-reference (C6, H4) confirms GO:0005739 C:mitochondrion. The annotation is computational/transferred (ISS), not direct experimental localization, but it is consistent with the well-established biology of fungal dihydroxy-acid dehydratase (EC 4.2.1.9) as a mitochondrial enzyme in branched-chain amino acid biosynthesis, and the N-terminal sequence shows a basic-region signature typical of mitochondrial targeting peptides.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~30 residues (MATSSIRSRALGLSRRARFETTRLPFIGRRYK) contain 8 arginines and 2 lysines with minimal acidic residues, a classic mitochondrial targeting peptide signature. The internal sequence motifs (e.g., 'GACGGMYTANTL', 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPE') identify the protein as a dihydroxy-acid dehydratase (DHAD/ILV3 family, EC 4.2.1.9), which in eukaryotes functions in mitochondrial branched-chain amino acid biosynthesis. Options C (egg coat) and D (centrosome) are animal-specific structures irrelevant to a metabolic enzyme. Option B (nucleus) lacks any recognizable bipartite or monopartite NLS in the sequence and is inconsistent with DHAD enzymatic function.


**Missing item-specific fact**

> None critical. The organism (Penicillium, a fungus) is not stated, but the reasoning does not require it: DHAD is mitochondrial across eukaryotes, and egg coat/centrosome are excluded by their animal-specific nature regardless of organism.


**Reason**

> A biologist with general knowledge of mitochondrial targeting signals (basic N-terminal region), enzyme family recognition (DHAD motifs), and cell biology (egg coat and centrosome are animal-specific) can distinguish option A from B, C, and D without memorizing this specific UniProt entry. The sequence itself provides the discriminating features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Egg coat (GO:0035805) and centrosome (GO:0005813) are animal-specific structures clearly incompatible with a fungal metabolic enzyme. Nucleus lacks any NLS and contradicts DHAD function. Mitochondrion is the only option consistent with both the N-terminal targeting signal and the enzyme family biology.


### Important caveats

- The UniProt subcellular location annotation is ISS (ECO:0000250, inferred from similarity to P39522), not direct experimental localization of this specific protein.
- The protein entry was first released in April 2025; it is a relatively new Swiss-Prot entry.
- The evaluated model is not told the organism (Penicillium brasilianum); however, the reasoning path does not strictly require organism identity.
- The GO annotation is IEA (Inferred from Electronic Annotation), reflecting computational transfer rather than experimental measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~30 residues (MATSSIRSRALGLSRRARFETTRLPFIGRRYK) contain 8 arginines and 2 lysines with minimal acidic residues, a classic mitochondrial targeting peptide signature. The internal sequence motifs (e.g., 'GACGGMYTANTL', 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPE') identify the protein as a dihydroxy-acid dehydratase (DHAD/ILV3 family, EC 4.2.1.9), which in eukaryotes functions in mitochondrial branched-chain amino acid biosynthesis. Options C (egg coat) and D (centrosome) are animal-specific structures irrelevant to a metabolic enzyme. Option B (nucleus) lacks any recognizable bipartite or monopartite NLS in the sequence and is inconsistent with DHAD enzymatic function.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The organism (Penicillium, a fungus) is not stated, but the reasoning does not require it: DHAD is mitochondrial across eukaryotes, and egg coat/centrosome are excluded by their animal-specific nature regardless of organism.",
    "reason": "A biologist with general knowledge of mitochondrial targeting signals (basic N-terminal region), enzyme family recognition (DHAD motifs), and cell biology (egg coat and centrosome are animal-specific) can distinguish option A from B, C, and D without memorizing this specific UniProt entry. The sequence itself provides the discriminating features."
  },
  "case_id": "GO_cellular_component_0011",
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
    "reason": "UniProt annotation (C5, H3) explicitly states subcellular location as 'Mitochondrion' with evidence code ECO:0000250 (ISS, inferred from similarity to P39522, the yeast mitochondrial DHAD Ilv3p). The protein name itself includes 'mitochondrial' (C4, H1). The GO cross-reference (C6, H4) confirms GO:0005739 C:mitochondrion. The annotation is computational/transferred (ISS), not direct experimental localization, but it is consistent with the well-established biology of fungal dihydroxy-acid dehydratase (EC 4.2.1.9) as a mitochondrial enzyme in branched-chain amino acid biosynthesis, and the N-terminal sequence shows a basic-region signature typical of mitochondrial targeting peptides."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation is ISS (ECO:0000250, inferred from similarity to P39522), not direct experimental localization of this specific protein.",
    "The protein entry was first released in April 2025; it is a relatively new Swiss-Prot entry.",
    "The evaluated model is not told the organism (Penicillium brasilianum); however, the reasoning path does not strictly require organism identity.",
    "The GO annotation is IEA (Inferred from Electronic Annotation), reflecting computational transfer rather than experimental measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Egg coat (GO:0035805) and centrosome (GO:0005813) are animal-specific structures clearly incompatible with a fungal metabolic enzyme. Nucleus lacks any NLS and contradicts DHAD function. Mitochondrion is the only option consistent with both the N-terminal targeting signal and the enzyme family biology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) explicitly states subcellular location as 'Mitochondrion' with evidence code ECO:0000250 (ISS, inferred from similarity to P39522, the yeast mitochondrial DHAD Ilv3p). The protein name itself includes 'mitochondrial' (C4, H1). The GO cross-reference (C6, H4) confirms GO:0005739 C:mitochondrion. The annotation is computational/transferred (ISS), not direct experimental localization, but it is consistent with the well-established biology of fungal dihydroxy-acid dehydratase (EC 4.2.1.9) as a mitochondrial enzyme in branched-chain amino acid biosynthesis, and the N-terminal sequence shows a basic-region signature typical of mitochondrial targeting peptides.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~30 residues (MATSSIRSRALGLSRRARFETTRLPFIGRRYK) contain 8 arginines and 2 lysines with minimal acidic residues, a classic mitochondrial targeting peptide signature. The internal sequence motifs (e.g., 'GACGGMYTANTL', 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPE') identify the protein as a dihydroxy-acid dehydratase (DHAD/ILV3 family, EC 4.2.1.9), which in eukaryotes functions in mitochondrial branched-chain amino acid biosynthesis. Options C (egg coat) and D (centrosome) are animal-specific structures irrelevant to a metabolic enzyme. Option B (nucleus) lacks any recognizable bipartite or monopartite NLS in the sequence and is inconsistent with DHAD enzymatic function.",
    "missing_item_specific_fact": "None critical. The organism (Penicillium, a fungus) is not stated, but the reasoning does not require it: DHAD is mitochondrial across eukaryotes, and egg coat/centrosome are excluded by their animal-specific nature regardless of organism.",
    "reason": "A biologist with general knowledge of mitochondrial targeting signals (basic N-terminal region), enzyme family recognition (DHAD motifs), and cell biology (egg coat and centrosome are animal-specific) can distinguish option A from B, C, and D without memorizing this specific UniProt entry. The sequence itself provides the discriminating features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Egg coat (GO:0035805) and centrosome (GO:0005813) are animal-specific structures clearly incompatible with a fungal metabolic enzyme. Nucleus lacks any NLS and contradicts DHAD function. Mitochondrion is the only option consistent with both the N-terminal targeting signal and the enzyme family biology."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation is ISS (ECO:0000250, inferred from similarity to P39522), not direct experimental localization of this specific protein.",
    "The protein entry was first released in April 2025; it is a relatively new Swiss-Prot entry.",
    "The evaluated model is not told the organism (Penicillium brasilianum); however, the reasoning path does not strictly require organism identity.",
    "The GO annotation is IEA (Inferred from Electronic Annotation), reflecting computational transfer rather than experimental measurement."
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

**Accession:** `A0A0F7TWW9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39511739","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase pbrD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/comments/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39522","source":"UniProtKB"}],"id":"SL-0173","value":"Mitochondrion"}}]}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"database":"GO","id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
ID   PBRD_PENBI              Reviewed;         596 AA.
AC   A0A0F7TWW9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 2.
DT   28-JAN-2026, entry version 30.
DE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};
DE            Short=DHAD astD {ECO:0000303|PubMed:39511739};
DE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};
DE   Flags: Precursor;
GN   Name=pbrD {ECO:0000303|PubMed:39511739}; ORFNames=PMG11_09713;
OS   Penicillium brasilianum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=104259;
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion {ECO:0000250|UniProtKB:P39522}.
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 90-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IEA:UniProtKB-SubCell.
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
