# catalytic_activity_0042

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKVLQMFFCVILLCVTSVLVEAKSTTKGDETASKRNFAQFAAMTYHTTHRWPKKYVGYGCYCGLGGYGIPVDPIDECCKTHDACYKKVEDSGICSYSWAIYLTIYKRKGGAECSEDNEKCQMEVCKCDSVAAKCLGKYKDIFNEKYAGYDKKGKCDPSFTLS

[Multiple Choices]
A. a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)
B. an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate
C. beta-nicotinamide D-ribonucleotide + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + nicotinamide + H(+)
D. N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-arginine
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

> The exact sequence match is annotated as phospholipase A2 with the reaction in choice A. The reaction annotation is attributed to a PROSITE rule, so it supports the key as a computational database annotation, not as direct experimental validation of this sequence's catalytic activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal signal-peptide-like region and a short, cysteine-rich mature region, features characteristic of small secreted disulfide-rich enzymes such as secreted phospholipase A2. That makes choice A meaningfully more plausible than the nucleotide-processing reactions in B and C or the ADP-ribosylarginine hydrolase reaction in D.


**Missing item-specific fact**

> No specific database accession or experimental measurement is essential to distinguish these choices, though exact functional assignment from sequence alone remains inferential.


**Reason**

> The sequence supplies biological features that favor a secreted phospholipase over the other listed enzyme types. This is a defensible family-level inference, not merely recall of the sequence's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed transformations describe distinct enzyme activities, and the sequence features favor the phospholipase option.


### Important caveats

- The cited catalytic-activity annotation is rule-based; the supplied evidence does not establish direct experimental measurement of this protein's reaction.
- The reviewer-only accession and annotation support the expected key but were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal-peptide-like region and a short, cysteine-rich mature region, features characteristic of small secreted disulfide-rich enzymes such as secreted phospholipase A2. That makes choice A meaningfully more plausible than the nucleotide-processing reactions in B and C or the ADP-ribosylarginine hydrolase reaction in D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No specific database accession or experimental measurement is essential to distinguish these choices, though exact functional assignment from sequence alone remains inferential.",
    "reason": "The sequence supplies biological features that favor a secreted phospholipase over the other listed enzyme types. This is a defensible family-level inference, not merely recall of the sequence's database entry."
  },
  "case_id": "catalytic_activity_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as phospholipase A2 with the reaction in choice A. The reaction annotation is attributed to a PROSITE rule, so it supports the key as a computational database annotation, not as direct experimental validation of this sequence's catalytic activity."
  },
  "important_caveats": [
    "The cited catalytic-activity annotation is rule-based; the supplied evidence does not establish direct experimental measurement of this protein's reaction.",
    "The reviewer-only accession and annotation support the expected key but were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed transformations describe distinct enzyme activities, and the sequence features favor the phospholipase option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as phospholipase A2 with the reaction in choice A. The reaction annotation is attributed to a PROSITE rule, so it supports the key as a computational database annotation, not as direct experimental validation of this sequence's catalytic activity.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal-peptide-like region and a short, cysteine-rich mature region, features characteristic of small secreted disulfide-rich enzymes such as secreted phospholipase A2. That makes choice A meaningfully more plausible than the nucleotide-processing reactions in B and C or the ADP-ribosylarginine hydrolase reaction in D.",
    "missing_item_specific_fact": "No specific database accession or experimental measurement is essential to distinguish these choices, though exact functional assignment from sequence alone remains inferential.",
    "reason": "The sequence supplies biological features that favor a secreted phospholipase over the other listed enzyme types. This is a defensible family-level inference, not merely recall of the sequence's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed transformations describe distinct enzyme activities, and the sequence features favor the phospholipase option."
  },
  "important_caveats": [
    "The cited catalytic-activity annotation is rule-based; the supplied evidence does not establish direct experimental measurement of this protein's reaction.",
    "The reviewer-only accession and annotation support the expected key but were not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DY42 (sequence matched, 162 aa) annotates the protein as Phospholipase A2 (EC 3.1.1.4) from Calliactis polypus, with the catalytic reaction exactly matching choice A. However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU10035, i.e., a computational/prosite-motif inference rather than a direct enzymatic assay. The protein name 'Phospholipase A2' is supported by sequence identification and mass spectrometry (PubMed 36977109, 39018436), but no direct catalytic-activity measurement is cited. The annotation is consistent with the expected answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark PLA2 signature motifs visible in the mature region after the signal peptide (residues ~1-20: MKVLQMFFCVILLCVTSVLVEA): the calcium-binding loop 'YGCYCGLGGYG' (residues ~73-83 in the precursor), the catalytic 'CG' motif within that loop, and the catalytic Asp49 equivalent in 'DPIDECCK'. The small size (~130-140 aa mature), secreted signal peptide, and dense cysteine pattern (multiple disulfide-bonded cysteines: CYCGLGGYG…CCK…ACYK…ICS…EC…CKC…CK) are textbook features of the secreted PLA2 superfamily. None of the distractor enzymes (CMP-sialic acid synthetase, NAD+ pyrophosphorylase, ADP-ribosylarginine hydrolase) share these motifs; they are cytosolic enzymes of completely different fold and size. A biologist familiar with enzyme-family signatures can identify PLA2 from these sequence features.


**Missing item-specific fact**

> None critical. The PLA2 catalytic motif (YGCYCGLGGYG / CG / Asp49) is a well-established, teachable biochemical signature, not an obscure database annotation.


**Reason**

> The sequence displays multiple, mutually reinforcing PLA2-family hallmarks (signal peptide, calcium-binding loop, catalytic CG motif, cysteine-rich small secreted architecture) that are part of standard biochemistry knowledge. These features concretely and meaningfully distinguish choice A from the three structurally and functionally unrelated distractors without requiring recall of this specific protein's UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four entirely different enzyme classes (PLA2, CMP-sialic acid synthetase, NAD+ pyrophosphorylase, ADP-ribosylarginine hydrolase) with no overlapping substrates or mechanisms. The PLA2 sequence signature unambiguously selects A.


### Important caveats

- The EC 3.1.1.4 assignment in UniProt rests on PROSITE-ProRule (ECO:0000255), a computational motif-based inference, not a direct enzymatic assay. No purified-enzyme kinetic data are cited in the annotation.
- The protein is annotated as a precursor (162 aa); the mature PLA2 would be the ~130-140 aa product after signal-peptide cleavage. The catalytic motifs are present in the precursor sequence as supplied.
- The entry was first public on 2025-04-09; the benchmark's author construction date is unknown, so the author may or may not have had access to this Swiss-Prot entry at the time of question creation.
- The identity origin (accession P0DY42) was inferred from dataset image-path metadata and was absent from the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark PLA2 signature motifs visible in the mature region after the signal peptide (residues ~1-20: MKVLQMFFCVILLCVTSVLVEA): the calcium-binding loop 'YGCYCGLGGYG' (residues ~73-83 in the precursor), the catalytic 'CG' motif within that loop, and the catalytic Asp49 equivalent in 'DPIDECCK'. The small size (~130-140 aa mature), secreted signal peptide, and dense cysteine pattern (multiple disulfide-bonded cysteines: CYCGLGGYG…CCK…ACYK…ICS…EC…CKC…CK) are textbook features of the secreted PLA2 superfamily. None of the distractor enzymes (CMP-sialic acid synthetase, NAD+ pyrophosphorylase, ADP-ribosylarginine hydrolase) share these motifs; they are cytosolic enzymes of completely different fold and size. A biologist familiar with enzyme-family signatures can identify PLA2 from these sequence features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PLA2 catalytic motif (YGCYCGLGGYG / CG / Asp49) is a well-established, teachable biochemical signature, not an obscure database annotation.",
    "reason": "The sequence displays multiple, mutually reinforcing PLA2-family hallmarks (signal peptide, calcium-binding loop, catalytic CG motif, cysteine-rich small secreted architecture) that are part of standard biochemistry knowledge. These features concretely and meaningfully distinguish choice A from the three structurally and functionally unrelated distractors without requiring recall of this specific protein's UniProt entry."
  },
  "case_id": "catalytic_activity_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DY42 (sequence matched, 162 aa) annotates the protein as Phospholipase A2 (EC 3.1.1.4) from Calliactis polypus, with the catalytic reaction exactly matching choice A. However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU10035, i.e., a computational/prosite-motif inference rather than a direct enzymatic assay. The protein name 'Phospholipase A2' is supported by sequence identification and mass spectrometry (PubMed 36977109, 39018436), but no direct catalytic-activity measurement is cited. The annotation is consistent with the expected answer."
  },
  "important_caveats": [
    "The EC 3.1.1.4 assignment in UniProt rests on PROSITE-ProRule (ECO:0000255), a computational motif-based inference, not a direct enzymatic assay. No purified-enzyme kinetic data are cited in the annotation.",
    "The protein is annotated as a precursor (162 aa); the mature PLA2 would be the ~130-140 aa product after signal-peptide cleavage. The catalytic motifs are present in the precursor sequence as supplied.",
    "The entry was first public on 2025-04-09; the benchmark's author construction date is unknown, so the author may or may not have had access to this Swiss-Prot entry at the time of question creation.",
    "The identity origin (accession P0DY42) was inferred from dataset image-path metadata and was absent from the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four entirely different enzyme classes (PLA2, CMP-sialic acid synthetase, NAD+ pyrophosphorylase, ADP-ribosylarginine hydrolase) with no overlapping substrates or mechanisms. The PLA2 sequence signature unambiguously selects A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DY42 (sequence matched, 162 aa) annotates the protein as Phospholipase A2 (EC 3.1.1.4) from Calliactis polypus, with the catalytic reaction exactly matching choice A. However, the EC assignment carries evidence code ECO:0000255|PROSITE-ProRule:PRU10035, i.e., a computational/prosite-motif inference rather than a direct enzymatic assay. The protein name 'Phospholipase A2' is supported by sequence identification and mass spectrometry (PubMed 36977109, 39018436), but no direct catalytic-activity measurement is cited. The annotation is consistent with the expected answer.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark PLA2 signature motifs visible in the mature region after the signal peptide (residues ~1-20: MKVLQMFFCVILLCVTSVLVEA): the calcium-binding loop 'YGCYCGLGGYG' (residues ~73-83 in the precursor), the catalytic 'CG' motif within that loop, and the catalytic Asp49 equivalent in 'DPIDECCK'. The small size (~130-140 aa mature), secreted signal peptide, and dense cysteine pattern (multiple disulfide-bonded cysteines: CYCGLGGYG…CCK…ACYK…ICS…EC…CKC…CK) are textbook features of the secreted PLA2 superfamily. None of the distractor enzymes (CMP-sialic acid synthetase, NAD+ pyrophosphorylase, ADP-ribosylarginine hydrolase) share these motifs; they are cytosolic enzymes of completely different fold and size. A biologist familiar with enzyme-family signatures can identify PLA2 from these sequence features.",
    "missing_item_specific_fact": "None critical. The PLA2 catalytic motif (YGCYCGLGGYG / CG / Asp49) is a well-established, teachable biochemical signature, not an obscure database annotation.",
    "reason": "The sequence displays multiple, mutually reinforcing PLA2-family hallmarks (signal peptide, calcium-binding loop, catalytic CG motif, cysteine-rich small secreted architecture) that are part of standard biochemistry knowledge. These features concretely and meaningfully distinguish choice A from the three structurally and functionally unrelated distractors without requiring recall of this specific protein's UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four entirely different enzyme classes (PLA2, CMP-sialic acid synthetase, NAD+ pyrophosphorylase, ADP-ribosylarginine hydrolase) with no overlapping substrates or mechanisms. The PLA2 sequence signature unambiguously selects A."
  },
  "important_caveats": [
    "The EC 3.1.1.4 assignment in UniProt rests on PROSITE-ProRule (ECO:0000255), a computational motif-based inference, not a direct enzymatic assay. No purified-enzyme kinetic data are cited in the annotation.",
    "The protein is annotated as a precursor (162 aa); the mature PLA2 would be the ~130-140 aa product after signal-peptide cleavage. The catalytic motifs are present in the precursor sequence as supplied.",
    "The entry was first public on 2025-04-09; the benchmark's author construction date is unknown, so the author may or may not have had access to this Swiss-Prot entry at the time of question creation.",
    "The identity origin (accession P0DY42) was inferred from dataset image-path metadata and was absent from the evaluated model input."
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

**Accession:** `P0DY42` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY42.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:08.181789+00:00.  

```json
"P0DY42"
```

Source SHA-256: `7c75de950f0fdf913641db8f4a8d9299a670f5c3bddde189822ce1370ac12348`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY42.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:08.181789+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Phosphatidylcholine 2-acylhydrolase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39018436","source":"PubMed"}],"value":"Phospholipase A2 Cpp1a"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39018436","source":"PubMed"}],"value":"PLA2-Cpp1a"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10035","source":"PROSITE-ProRule"}],"value":"3.1.1.4"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36977109","source":"PubMed"}],"value":"Phospholipase A2"},"shortNames":[{"value":"PLA2"}]}}
```

Source SHA-256: `7c75de950f0fdf913641db8f4a8d9299a670f5c3bddde189822ce1370ac12348`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY42.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:08.181789+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.1.1.4","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10035","source":"PROSITE-ProRule"}],"name":"a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15801"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:28868"},{"database":"ChEBI","id":"CHEBI:57643"},{"database":"ChEBI","id":"CHEBI:58168"}]}}
```

Source SHA-256: `7c75de950f0fdf913641db8f4a8d9299a670f5c3bddde189822ce1370ac12348`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY42?format=txt&versions=3)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:12.224282+00:00.  

```text
ID   PLA2_CALPY              Reviewed;         162 AA.
AC   P0DY42;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=Phospholipase A2 {ECO:0000303|PubMed:36977109};
DE            Short=PLA2;
DE            EC=3.1.1.4 {ECO:0000255|PROSITE-ProRule:PRU10035};
DE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;
DE   AltName: Full=Phospholipase A2 Cpp1a {ECO:0000303|PubMed:39018436};
DE            Short=PLA2-Cpp1a {ECO:0000303|PubMed:39018436};
DE   Flags: Precursor;
GN   ORFNames=c56806_g1_i1 {ECO:0000303|PubMed:36977109,
GN   ECO:0000303|PubMed:39018436};
OS   Calliactis polypus (Hermit crab anemone) (Priapus polypus).
OC   Eukaryota; Metazoa; Cnidaria; Anthozoa; Hexacorallia; Actiniaria;
OC   Nynantheae; Hormathiidae; Calliactis.
OX   NCBI_TaxID=656064;
```

Source SHA-256: `dd00dd8be405e70fb669825538e585e62a6604c98be8a7ee96e819b8ecce813e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY42?format=txt&versions=3)  
**Locator:** `lines 6-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:12.224282+00:00.  

```text
DE   RecName: Full=Phospholipase A2 {ECO:0000303|PubMed:36977109};
DE            Short=PLA2;
DE            EC=3.1.1.4 {ECO:0000255|PROSITE-ProRule:PRU10035};
DE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;
DE   AltName: Full=Phospholipase A2 Cpp1a {ECO:0000303|PubMed:39018436};
DE            Short=PLA2-Cpp1a {ECO:0000303|PubMed:39018436};
DE   Flags: Precursor;
```

Source SHA-256: `dd00dd8be405e70fb669825538e585e62a6604c98be8a7ee96e819b8ecce813e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY42?format=txt&versions=3)  
**Locator:** `lines 37-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:12.224282+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-
CC         glycero-3-phosphocholine + a fatty acid + H(+); Xref=Rhea:RHEA:15801,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:28868,
CC         ChEBI:CHEBI:57643, ChEBI:CHEBI:58168; EC=3.1.1.4;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10035};
```

Source SHA-256: `dd00dd8be405e70fb669825538e585e62a6604c98be8a7ee96e819b8ecce813e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 42. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
