# catalytic_activity_0115

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRTCGTSSEGQDECCLYGLSAMQGWRISMEDAHAAVLDLQAKSTGGSEKPTDPDKRLAFFGVYDGHGGDKVALFAGENVHKIVAKQEAFAKGDIEQALKDGFLATDRAILEDPKYEEEVSGCTAAVSVISKNKIWVANAGDSRSVLGVKGRAKPLSFDHKPQNEGEKARISAAGGFVDFGRVNGNLALSRAIGDFEFKKSPELSPEQQIVTAYPDVTVHEVTDDDEFLVIACDGIWDCQSSQSVVEFVRRGIAAKQELYRICENMMDNCLASNSETGGVGCDNMTMIIIGLLNGKTKEEWYNQISERVANGDGPCAPPEYGKSEFRGPGIRNQFEETPDNYDLENDRSRGFSVRSGRIILLGDGTELIPEQNDEELFDQREENRDVTNHLQHDKAEETSTAANLSESPSSANKNSSGSGTEATEKSASS

[Multiple Choices]
A. D-proline + 2-oxoglutarate + O2 = cis-4-hydroxy-D-proline + succinate + CO2
B. UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-galactosamine
C. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
D. (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches the 429-aa Q4WTH5 entry, annotated as a PP2C homolog with EC 3.1.3.16. That annotation includes the reaction in choice C. The reaction annotation is supported by a PROSITE-ProRule inference, while the EC assignment is transferred by similarity; this is not direct experimental confirmation for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains conserved motifs characteristic of a PP2C-family phosphatase, whose biological activity is removal of phosphate from phosphorylated proteins. That points to choice C over the unrelated dioxygenase, sugar epimerase, and terpene-related reactions.


**Missing item-specific fact**

> The exact protein-specific annotation or experimental characterization is not supplied, but it is not essential to distinguish these choices at the enzyme-family level.


**Reason**

> The sequence provides a defensible family-level catalytic clue that meaningfully separates C from the distractors, though it does not independently establish experimental activity for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C describes protein dephosphorylation; the other choices describe distinct reaction types.


### Important caveats

- The annotation applies to the exact matched sequence, but its evidence is computational or transferred by similarity rather than direct experimental validation in the supplied evidence.
- The entry also annotates dephosphorylation of phosphothreonyl proteins, a related activity not represented among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains conserved motifs characteristic of a PP2C-family phosphatase, whose biological activity is removal of phosphate from phosphorylated proteins. That points to choice C over the unrelated dioxygenase, sugar epimerase, and terpene-related reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein-specific annotation or experimental characterization is not supplied, but it is not essential to distinguish these choices at the enzyme-family level.",
    "reason": "The sequence provides a defensible family-level catalytic clue that meaningfully separates C from the distractors, though it does not independently establish experimental activity for this exact protein."
  },
  "case_id": "catalytic_activity_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the 429-aa Q4WTH5 entry, annotated as a PP2C homolog with EC 3.1.3.16. That annotation includes the reaction in choice C. The reaction annotation is supported by a PROSITE-ProRule inference, while the EC assignment is transferred by similarity; this is not direct experimental confirmation for this protein."
  },
  "important_caveats": [
    "The annotation applies to the exact matched sequence, but its evidence is computational or transferred by similarity rather than direct experimental validation in the supplied evidence.",
    "The entry also annotates dephosphorylation of phosphothreonyl proteins, a related activity not represented among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C describes protein dephosphorylation; the other choices describe distinct reaction types."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the 429-aa Q4WTH5 entry, annotated as a PP2C homolog with EC 3.1.3.16. That annotation includes the reaction in choice C. The reaction annotation is supported by a PROSITE-ProRule inference, while the EC assignment is transferred by similarity; this is not direct experimental confirmation for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains conserved motifs characteristic of a PP2C-family phosphatase, whose biological activity is removal of phosphate from phosphorylated proteins. That points to choice C over the unrelated dioxygenase, sugar epimerase, and terpene-related reactions.",
    "missing_item_specific_fact": "The exact protein-specific annotation or experimental characterization is not supplied, but it is not essential to distinguish these choices at the enzyme-family level.",
    "reason": "The sequence provides a defensible family-level catalytic clue that meaningfully separates C from the distractors, though it does not independently establish experimental activity for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C describes protein dephosphorylation; the other choices describe distinct reaction types."
  },
  "important_caveats": [
    "The annotation applies to the exact matched sequence, but its evidence is computational or transferred by similarity rather than direct experimental validation in the supplied evidence.",
    "The entry also annotates dephosphorylation of phosphothreonyl proteins, a related activity not represented among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WTH5 (PP2C2_ASPFU, sequence matched) explicitly annotates the catalytic reaction 'O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate' under EC 3.1.3.16 (evidence ECO:0000255|PROSITE-ProRule:PRU01082 for the reaction, ECO:0000305 for physiological direction). The protein is named 'Protein phosphatase 2C homolog 2' and the sequence contains canonical PP2C motifs. The annotation is computational/similarity-based (PROSITE-ProRule and transfer from P39966) rather than direct experimental measurement on this specific protein, but it is a well-established family-level assignment consistent with the sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark PP2C family motif 'DGHGGD' (DxGxG signature, visible in 'GVYDGHGGDKVALF') along with aspartate-rich regions consistent with Mg2+/Mn2+ coordination typical of PP2C phosphatases. PP2C is a well-known family of Ser/Thr protein phosphatases whose catalytic function (hydrolysis of phosphoester bonds on phospho-Ser/Thr residues in proteins) is standard biochemistry. The four options represent entirely different enzyme classes: (A) a 2-oxoglutarate-dependent dioxygenase, (B) a UDP-sugar epimerase, (C) a Ser/Thr protein phosphatase, (D) a diterpene synthase. Identifying the PP2C motif and knowing its well-characterized catalytic role allows elimination of A, B, and D without any item-specific lookup.


**Missing item-specific fact**

> None critical. The PP2C DxGxG motif is a widely taught, distinctive sequence signature, and the catalytic function of PP2C phosphatases is general biochemistry knowledge. No protein-specific experimental measurement is needed.


**Reason**

> The PP2C family signature is identifiable from the sequence and its Ser/Thr phosphatase function is textbook knowledge. The distractors belong to unrelated enzyme classes with no sequence overlap with PP2C motifs, making the correct choice distinguishable through general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (C) corresponds to a phosphatase reaction. The annotation also lists a threonine dephosphorylation reaction, but that is not offered as a choice. The remaining options (dioxygenase, epimerase, terpene synthase) are incompatible with PP2C sequence features.


### Important caveats

- The EC assignment and catalytic annotation are based on PROSITE-ProRule motif matching (ECO:0000255) and similarity transfer from P39966 (ECO:0000250), not direct experimental kinetics on Q4WTH5 itself.
- The protein is annotated as 'homolog 2' and the threonine dephosphorylation reaction is also listed; the question's single serine option is the primary annotated reaction but the enzyme likely acts on both Ser and Thr residues.
- Sequence identity confirmed: benchmark sequence SHA256 matches UniProt Q4WTH5 sequence version 1 (429 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark PP2C family motif 'DGHGGD' (DxGxG signature, visible in 'GVYDGHGGDKVALF') along with aspartate-rich regions consistent with Mg2+/Mn2+ coordination typical of PP2C phosphatases. PP2C is a well-known family of Ser/Thr protein phosphatases whose catalytic function (hydrolysis of phosphoester bonds on phospho-Ser/Thr residues in proteins) is standard biochemistry. The four options represent entirely different enzyme classes: (A) a 2-oxoglutarate-dependent dioxygenase, (B) a UDP-sugar epimerase, (C) a Ser/Thr protein phosphatase, (D) a diterpene synthase. Identifying the PP2C motif and knowing its well-characterized catalytic role allows elimination of A, B, and D without any item-specific lookup.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PP2C DxGxG motif is a widely taught, distinctive sequence signature, and the catalytic function of PP2C phosphatases is general biochemistry knowledge. No protein-specific experimental measurement is needed.",
    "reason": "The PP2C family signature is identifiable from the sequence and its Ser/Thr phosphatase function is textbook knowledge. The distractors belong to unrelated enzyme classes with no sequence overlap with PP2C motifs, making the correct choice distinguishable through general biological reasoning."
  },
  "case_id": "catalytic_activity_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WTH5 (PP2C2_ASPFU, sequence matched) explicitly annotates the catalytic reaction 'O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate' under EC 3.1.3.16 (evidence ECO:0000255|PROSITE-ProRule:PRU01082 for the reaction, ECO:0000305 for physiological direction). The protein is named 'Protein phosphatase 2C homolog 2' and the sequence contains canonical PP2C motifs. The annotation is computational/similarity-based (PROSITE-ProRule and transfer from P39966) rather than direct experimental measurement on this specific protein, but it is a well-established family-level assignment consistent with the sequence."
  },
  "important_caveats": [
    "The EC assignment and catalytic annotation are based on PROSITE-ProRule motif matching (ECO:0000255) and similarity transfer from P39966 (ECO:0000250), not direct experimental kinetics on Q4WTH5 itself.",
    "The protein is annotated as 'homolog 2' and the threonine dephosphorylation reaction is also listed; the question's single serine option is the primary annotated reaction but the enzyme likely acts on both Ser and Thr residues.",
    "Sequence identity confirmed: benchmark sequence SHA256 matches UniProt Q4WTH5 sequence version 1 (429 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (C) corresponds to a phosphatase reaction. The annotation also lists a threonine dephosphorylation reaction, but that is not offered as a choice. The remaining options (dioxygenase, epimerase, terpene synthase) are incompatible with PP2C sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WTH5 (PP2C2_ASPFU, sequence matched) explicitly annotates the catalytic reaction 'O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate' under EC 3.1.3.16 (evidence ECO:0000255|PROSITE-ProRule:PRU01082 for the reaction, ECO:0000305 for physiological direction). The protein is named 'Protein phosphatase 2C homolog 2' and the sequence contains canonical PP2C motifs. The annotation is computational/similarity-based (PROSITE-ProRule and transfer from P39966) rather than direct experimental measurement on this specific protein, but it is a well-established family-level assignment consistent with the sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark PP2C family motif 'DGHGGD' (DxGxG signature, visible in 'GVYDGHGGDKVALF') along with aspartate-rich regions consistent with Mg2+/Mn2+ coordination typical of PP2C phosphatases. PP2C is a well-known family of Ser/Thr protein phosphatases whose catalytic function (hydrolysis of phosphoester bonds on phospho-Ser/Thr residues in proteins) is standard biochemistry. The four options represent entirely different enzyme classes: (A) a 2-oxoglutarate-dependent dioxygenase, (B) a UDP-sugar epimerase, (C) a Ser/Thr protein phosphatase, (D) a diterpene synthase. Identifying the PP2C motif and knowing its well-characterized catalytic role allows elimination of A, B, and D without any item-specific lookup.",
    "missing_item_specific_fact": "None critical. The PP2C DxGxG motif is a widely taught, distinctive sequence signature, and the catalytic function of PP2C phosphatases is general biochemistry knowledge. No protein-specific experimental measurement is needed.",
    "reason": "The PP2C family signature is identifiable from the sequence and its Ser/Thr phosphatase function is textbook knowledge. The distractors belong to unrelated enzyme classes with no sequence overlap with PP2C motifs, making the correct choice distinguishable through general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (C) corresponds to a phosphatase reaction. The annotation also lists a threonine dephosphorylation reaction, but that is not offered as a choice. The remaining options (dioxygenase, epimerase, terpene synthase) are incompatible with PP2C sequence features."
  },
  "important_caveats": [
    "The EC assignment and catalytic annotation are based on PROSITE-ProRule motif matching (ECO:0000255) and similarity transfer from P39966 (ECO:0000250), not direct experimental kinetics on Q4WTH5 itself.",
    "The protein is annotated as 'homolog 2' and the threonine dephosphorylation reaction is also listed; the question's single serine option is the primary annotated reaction but the enzyme likely acts on both Ser and Thr residues.",
    "Sequence identity confirmed: benchmark sequence SHA256 matches UniProt Q4WTH5 sequence version 1 (429 aa)."
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

**Accession:** `Q4WTH5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 119. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
"Q4WTH5"
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein phosphatase 2C homolog 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PP2C-2"}]}}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01082","source":"PROSITE-ProRule"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
ID   PP2C2_ASPFU             Reviewed;         429 AA.
AC   Q4WTH5;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2005, sequence version 1.
DT   28-JAN-2026, entry version 119.
DE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000305};
DE            Short=PP2C-2 {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000250|UniProtKB:P39966};
GN   Name=ptcB {ECO:0000303|PubMed:25597841};
GN   ORFNames=AFUA_1G09280 {ECO:0000312|EMBL:EAL90257.1};
OS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /
OS   Af293) (Neosartorya fumigata).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Fumigati.
OX   NCBI_TaxID=330879 {ECO:0000312|Proteomes:UP000002530};
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
DE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000305};
DE            Short=PP2C-2 {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000250|UniProtKB:P39966};
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 55-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16; Evidence={ECO:0000255|PROSITE-
CC         ProRule:PRU01082};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
