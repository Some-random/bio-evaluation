# active_site_0040

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 58 (Proton donor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKQVQIPEIELNSGHKMPLVGFGTCVPDPIPPLEELAGIFLEAIKVGYRHFDTASSYGTEEALGRAVAQAIETGLVNGREEFFISSKLWCEDADLDLILPALKKTLGNMGLDYLDLSMIHMPVRVRKGAEMFNYTKEDLLPFDIQGTWKAMEECNKLGLAKSIGVSNYSCEKLTKLLENATVPPAVNQVEMNVVWQQRKLLPFCKEKNIHVTAWSPLLSYGAVWGSNAVMENPILVEIAASKNKTVAQVALRWIYEQGASFIMRTFNKDRMFENVQIFDWELTKEELDKIQKIPQRRGTLGEDFIHPEGPIKSVEDLWDGDL

[Multiple Choices]
A. Position 4848 (Proton donor; for dehydratase activity 2)
B. Position 118 (Nucleophile)
C. Position 58 (Proton donor)
D. Position 343 (Nucleophile)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry annotates residue 58 as an active-site proton donor. This supports choice C, though the annotation is transferred by similarity rather than direct experimental evidence for this protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is 323 residues long, so choices at 343 and 4848 are inconsistent with its length. But sequence length or general biochemical reasoning does not establish that residue 58 is the proton donor rather than another in-range candidate.


**Missing item-specific fact**

> The protein-specific active-site annotation assigning residue 58 the proton-donor role, or equivalent evidence from a characterized homolog.


**Reason**

> Distinguishing the in-range choices requires a specific residue-function assignment not supplied by the sequence and choices. The supporting database annotation is reviewer-only and does not make the original question reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C is supported by the sequence-matched annotation; the other listed positions do not provide a competing supported assignment, and two are beyond the sequence length.


### Important caveats

- The residue-58 proton-donor annotation cites evidence transferred from UniProtKB:Q8CG76 (ECO:0000250); it is not shown here to be an experimental determination for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 323 residues long, so choices at 343 and 4848 are inconsistent with its length. But sequence length or general biochemical reasoning does not establish that residue 58 is the proton donor rather than another in-range candidate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning residue 58 the proton-donor role, or equivalent evidence from a characterized homolog.",
    "reason": "Distinguishing the in-range choices requires a specific residue-function assignment not supplied by the sequence and choices. The supporting database annotation is reviewer-only and does not make the original question reasoning-supported."
  },
  "case_id": "active_site_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates residue 58 as an active-site proton donor. This supports choice C, though the annotation is transferred by similarity rather than direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The residue-58 proton-donor annotation cites evidence transferred from UniProtKB:Q8CG76 (ECO:0000250); it is not shown here to be an experimental determination for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is supported by the sequence-matched annotation; the other listed positions do not provide a competing supported assignment, and two are beyond the sequence length."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates residue 58 as an active-site proton donor. This supports choice C, though the annotation is transferred by similarity rather than direct experimental evidence for this protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is 323 residues long, so choices at 343 and 4848 are inconsistent with its length. But sequence length or general biochemical reasoning does not establish that residue 58 is the proton donor rather than another in-range candidate.",
    "missing_item_specific_fact": "The protein-specific active-site annotation assigning residue 58 the proton-donor role, or equivalent evidence from a characterized homolog.",
    "reason": "Distinguishing the in-range choices requires a specific residue-function assignment not supplied by the sequence and choices. The supporting database annotation is reviewer-only and does not make the original question reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is supported by the sequence-matched annotation; the other listed positions do not provide a competing supported assignment, and two are beyond the sequence length."
  },
  "important_caveats": [
    "The residue-58 proton-donor annotation cites evidence transferred from UniProtKB:Q8CG76 (ECO:0000250); it is not shown here to be an experimental determination for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7S518 (Rhazimal reductase 1, EC 1.1.1.440, an SDR-family enzyme from Alstonia scholaris) annotates position 58 (Tyr) as 'Active site: Proton donor' (evidence C5/H3). The sequence is 323 residues, so positions 4848 (A) and 343 (D) are out of range. Position 118 is Ser, but it is not annotated as an active site or nucleophile in the entry. The annotation is ECO:0000250 (by similarity to Q8CG76), a computational transfer, but is consistent with the well-established SDR catalytic mechanism in which the conserved Tyr serves as the proton donor. The sequence context (Y58 in the 'DTASSY' region, with K88 annotated as 'Lowers pKa of active site Tyr') is consistent with the SDR Tyr-Lys catalytic dyad architecture.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C11](#evidence-c11), [H1](#evidence-h1), [H3](#evidence-h3), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A (position 4848) and D (position 343) are trivially eliminated because the protein is only 323 residues long. Between B (position 118, Ser, 'Nucleophile') and C (position 58, Tyr, 'Proton donor'), a model recognizing the SDR (Short-chain Dehydrogenase/Reductase) fold from the sequence (Rossmann-like NAD-binding region, GxxGxxG-like motifs near positions 22-26 and 59-65) can apply the well-established SDR catalytic tetrad mechanism: Tyr is the proton donor, Ser is the nucleophile, Lys lowers the Tyr pKa, and Asn orients the substrate. The Tyr at position 58 sits in the conserved 'Y' of the SDR catalytic region, and the Lys at position 88 (30 residues downstream, consistent with SDR Tyr-Lys spacing) is annotated as lowering the Tyr pKa. In SDR enzymes, the proton donor role belongs to Tyr, not Ser, making C the mechanistically correct assignment for position 58.


**Missing item-specific fact**

> Identifying which of the seven Tyr residues in the sequence (positions 49, 58, 114, 135, 169, 221, 256) is the catalytic one requires either 3D structural knowledge or database annotation. However, the SDR fold context and the Tyr-Lys dyad spacing provide reasonable sequence-based clues.


**Reason**

> The SDR catalytic mechanism (Tyr = proton donor) is textbook biochemistry applicable to any SDR enzyme. Eliminating A and D requires only a length check. Distinguishing B from C requires knowing that in SDR enzymes the proton donor is Tyr (not Ser) and identifying the catalytic Tyr from sequence context. This is achievable with general enzymology knowledge and pattern recognition of the SDR fold, though pinpointing the exact catalytic Tyr among several Tyr residues adds some difficulty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are immediately invalid (positions exceed the 323-residue protein). Option B labels position 118 (Ser) as 'Nucleophile,' but the UniProt entry does not annotate position 118 as an active site, and in the SDR mechanism the catalytic Ser nucleophile is typically in a different conserved region. Only position 58 is annotated as 'Active site: Proton donor.' While a student familiar with SDR catalysis might note that a Ser nucleophile also exists in the tetrad, the annotation and the specific position assignment support C as the uniquely correct choice.


### Important caveats

- The active-site annotation (ECO:0000250) is inferred by similarity to Q8CG76, not directly experimentally validated for this specific Rhazimal reductase 1 sequence.
- The protein was experimentally characterized (PubMed 36349266) for function, catalytic activity, and biophysical properties, but the specific active-site residue assignment relies on homology transfer.
- The reviewer identified the UniProt accession from dataset metadata not available to the evaluated model; the model must work from the raw sequence alone.
- The question format (single residue, single role) is a simplification: the SDR catalytic center involves a tetrad (Tyr-Lys-Ser-Asn), but the question asks for the single 'proton donor' residue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A (position 4848) and D (position 343) are trivially eliminated because the protein is only 323 residues long. Between B (position 118, Ser, 'Nucleophile') and C (position 58, Tyr, 'Proton donor'), a model recognizing the SDR (Short-chain Dehydrogenase/Reductase) fold from the sequence (Rossmann-like NAD-binding region, GxxGxxG-like motifs near positions 22-26 and 59-65) can apply the well-established SDR catalytic tetrad mechanism: Tyr is the proton donor, Ser is the nucleophile, Lys lowers the Tyr pKa, and Asn orients the substrate. The Tyr at position 58 sits in the conserved 'Y' of the SDR catalytic region, and the Lys at position 88 (30 residues downstream, consistent with SDR Tyr-Lys spacing) is annotated as lowering the Tyr pKa. In SDR enzymes, the proton donor role belongs to Tyr, not Ser, making C the mechanistically correct assignment for position 58.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Identifying which of the seven Tyr residues in the sequence (positions 49, 58, 114, 135, 169, 221, 256) is the catalytic one requires either 3D structural knowledge or database annotation. However, the SDR fold context and the Tyr-Lys dyad spacing provide reasonable sequence-based clues.",
    "reason": "The SDR catalytic mechanism (Tyr = proton donor) is textbook biochemistry applicable to any SDR enzyme. Eliminating A and D requires only a length check. Distinguishing B from C requires knowing that in SDR enzymes the proton donor is Tyr (not Ser) and identifying the catalytic Tyr from sequence context. This is achievable with general enzymology knowledge and pattern recognition of the SDR fold, though pinpointing the exact catalytic Tyr among several Tyr residues adds some difficulty."
  },
  "case_id": "active_site_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C11",
      "H1",
      "H3",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S518 (Rhazimal reductase 1, EC 1.1.1.440, an SDR-family enzyme from Alstonia scholaris) annotates position 58 (Tyr) as 'Active site: Proton donor' (evidence C5/H3). The sequence is 323 residues, so positions 4848 (A) and 343 (D) are out of range. Position 118 is Ser, but it is not annotated as an active site or nucleophile in the entry. The annotation is ECO:0000250 (by similarity to Q8CG76), a computational transfer, but is consistent with the well-established SDR catalytic mechanism in which the conserved Tyr serves as the proton donor. The sequence context (Y58 in the 'DTASSY' region, with K88 annotated as 'Lowers pKa of active site Tyr') is consistent with the SDR Tyr-Lys catalytic dyad architecture."
  },
  "important_caveats": [
    "The active-site annotation (ECO:0000250) is inferred by similarity to Q8CG76, not directly experimentally validated for this specific Rhazimal reductase 1 sequence.",
    "The protein was experimentally characterized (PubMed 36349266) for function, catalytic activity, and biophysical properties, but the specific active-site residue assignment relies on homology transfer.",
    "The reviewer identified the UniProt accession from dataset metadata not available to the evaluated model; the model must work from the raw sequence alone.",
    "The question format (single residue, single role) is a simplification: the SDR catalytic center involves a tetrad (Tyr-Lys-Ser-Asn), but the question asks for the single 'proton donor' residue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are immediately invalid (positions exceed the 323-residue protein). Option B labels position 118 (Ser) as 'Nucleophile,' but the UniProt entry does not annotate position 118 as an active site, and in the SDR mechanism the catalytic Ser nucleophile is typically in a different conserved region. Only position 58 is annotated as 'Active site: Proton donor.' While a student familiar with SDR catalysis might note that a Ser nucleophile also exists in the tetrad, the annotation and the specific position assignment support C as the uniquely correct choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S518 (Rhazimal reductase 1, EC 1.1.1.440, an SDR-family enzyme from Alstonia scholaris) annotates position 58 (Tyr) as 'Active site: Proton donor' (evidence C5/H3). The sequence is 323 residues, so positions 4848 (A) and 343 (D) are out of range. Position 118 is Ser, but it is not annotated as an active site or nucleophile in the entry. The annotation is ECO:0000250 (by similarity to Q8CG76), a computational transfer, but is consistent with the well-established SDR catalytic mechanism in which the conserved Tyr serves as the proton donor. The sequence context (Y58 in the 'DTASSY' region, with K88 annotated as 'Lowers pKa of active site Tyr') is consistent with the SDR Tyr-Lys catalytic dyad architecture.",
    "evidence_ids": ["C1", "C4", "C5", "C11", "H1", "H3", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A (position 4848) and D (position 343) are trivially eliminated because the protein is only 323 residues long. Between B (position 118, Ser, 'Nucleophile') and C (position 58, Tyr, 'Proton donor'), a model recognizing the SDR (Short-chain Dehydrogenase/Reductase) fold from the sequence (Rossmann-like NAD-binding region, GxxGxxG-like motifs near positions 22-26 and 59-65) can apply the well-established SDR catalytic tetrad mechanism: Tyr is the proton donor, Ser is the nucleophile, Lys lowers the Tyr pKa, and Asn orients the substrate. The Tyr at position 58 sits in the conserved 'Y' of the SDR catalytic region, and the Lys at position 88 (30 residues downstream, consistent with SDR Tyr-Lys spacing) is annotated as lowering the Tyr pKa. In SDR enzymes, the proton donor role belongs to Tyr, not Ser, making C the mechanistically correct assignment for position 58.",
    "missing_item_specific_fact": "Identifying which of the seven Tyr residues in the sequence (positions 49, 58, 114, 135, 169, 221, 256) is the catalytic one requires either 3D structural knowledge or database annotation. However, the SDR fold context and the Tyr-Lys dyad spacing provide reasonable sequence-based clues.",
    "reason": "The SDR catalytic mechanism (Tyr = proton donor) is textbook biochemistry applicable to any SDR enzyme. Eliminating A and D requires only a length check. Distinguishing B from C requires knowing that in SDR enzymes the proton donor is Tyr (not Ser) and identifying the catalytic Tyr from sequence context. This is achievable with general enzymology knowledge and pattern recognition of the SDR fold, though pinpointing the exact catalytic Tyr among several Tyr residues adds some difficulty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are immediately invalid (positions exceed the 323-residue protein). Option B labels position 118 (Ser) as 'Nucleophile,' but the UniProt entry does not annotate position 118 as an active site, and in the SDR mechanism the catalytic Ser nucleophile is typically in a different conserved region. Only position 58 is annotated as 'Active site: Proton donor.' While a student familiar with SDR catalysis might note that a Ser nucleophile also exists in the tetrad, the annotation and the specific position assignment support C as the uniquely correct choice."
  },
  "important_caveats": [
    "The active-site annotation (ECO:0000250) is inferred by similarity to Q8CG76, not directly experimentally validated for this specific Rhazimal reductase 1 sequence.",
    "The protein was experimentally characterized (PubMed 36349266) for function, catalytic activity, and biophysical properties, but the specific active-site residue assignment relies on homology transfer.",
    "The reviewer identified the UniProt accession from dataset metadata not available to the evaluated model; the model must work from the raw sequence alone.",
    "The question format (single residue, single role) is a simplification: the SDR catalytic center involves a tetrad (Tyr-Lys-Ser-Asn), but the question asks for the single 'proton donor' residue."
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

**Accession:** `A0A9E7S518` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
"A0A9E7S518"
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.1.1.440"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Rhazimal reductase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsRHR1"}]}}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"description":"Proton donor","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8CG76","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":58},"start":{"modifier":"EXACT","value":58}},"type":"Active site"}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:12.223906+00:00.  

```json
{"description":"Lowers pKa of active site Tyr","evidences":[{"evidenceCode":"ECO:0000250","id":"P46336","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":88},"start":{"modifier":"EXACT","value":88}},"type":"Site"}
```

Source SHA-256: `48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
ID   RHR1_ALSSC              Reviewed;         323 AA.
AC   A0A9E7S518;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 12.
DE   RecName: Full=Rhazimal reductase 1 {ECO:0000303|PubMed:36349266};
DE            Short=AsRHR1 {ECO:0000303|PubMed:36349266};
DE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};
GN   Name=RHR1 {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 75-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
FT   ACT_SITE        58
FT                   /note="Proton donor"
FT                   /evidence="ECO:0000250|UniProtKB:Q8CG76"
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:14.092631+00:00.  

```text
FT   SITE            88
FT                   /note="Lowers pKa of active site Tyr"
FT                   /evidence="ECO:0000250|UniProtKB:P46336"
```

Source SHA-256: `9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 40. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
