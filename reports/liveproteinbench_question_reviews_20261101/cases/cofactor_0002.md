# cofactor_0002

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGSKETKNTSRRDFLIKGAGAAALGAGAFAISQVPLLEKLASANEDTVKDLLPFPELIESDEIIIRMQNDVRRALKKPLNEIQWIMVIDLKKCVGCSSCTVACVSENVLPPGVVYRPVIEEEIGTFPNVTKKFTPRPCMQCEHPPCTKVCPIGATYKSEDGIVAIDYDKCIGCRYCITACPYGARTFDWGEYHTENTPEIMQYEKEPNYEYGVERVREKKNSPIGNARKCHFCKHRLHKGMLSMCVTTCIGRATYIGDKNDPESLVAELIASPRVMRLKEELGTEPNVYYLT

[Multiple Choices]
A. Cu(2+)
B. FMN
C. [4Fe-4S] cluster
D. Co(2+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt record, whose cofactor annotation names a &#91;4Fe-4S&#93; cluster. The annotation is transferred by similarity from UniProtKB:Q7WTT9 (ECO:0000250), so it supports the key but is not direct experimental confirmation for this protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several repeated, cysteine-rich motifs, a recognizable pattern for iron-sulfur cluster coordination. Among the choices, that provides a meaningful biological basis for preferring the &#91;4Fe-4S&#93; option over FMN or the individual Cu(2+) and Co(2+) ions.


**Missing item-specific fact**

> Direct experimental confirmation that this particular protein binds &#91;4Fe-4S&#93; clusters, including the number and type of clusters, is not supplied.


**Reason**

> The sequence motifs and answer choices support a reasoned prediction of an iron-sulfur cofactor, though they do not establish exact cluster occupancy or replace protein-specific experimental evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cysteine-rich sequence pattern favors the only iron-sulfur-cluster option; the choices do not include another iron-sulfur cluster type.


### Important caveats

- The supporting database cofactor annotation is similarity-transferred, not shown here as a direct measurement on the supplied protein.
- The protein-specific annotation and identity were reviewer-only and were not part of the evaluated input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several repeated, cysteine-rich motifs, a recognizable pattern for iron-sulfur cluster coordination. Among the choices, that provides a meaningful biological basis for preferring the [4Fe-4S] option over FMN or the individual Cu(2+) and Co(2+) ions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Direct experimental confirmation that this particular protein binds [4Fe-4S] clusters, including the number and type of clusters, is not supplied.",
    "reason": "The sequence motifs and answer choices support a reasoned prediction of an iron-sulfur cofactor, though they do not establish exact cluster occupancy or replace protein-specific experimental evidence."
  },
  "case_id": "cofactor_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record, whose cofactor annotation names a [4Fe-4S] cluster. The annotation is transferred by similarity from UniProtKB:Q7WTT9 (ECO:0000250), so it supports the key but is not direct experimental confirmation for this protein."
  },
  "important_caveats": [
    "The supporting database cofactor annotation is similarity-transferred, not shown here as a direct measurement on the supplied protein.",
    "The protein-specific annotation and identity were reviewer-only and were not part of the evaluated input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cysteine-rich sequence pattern favors the only iron-sulfur-cluster option; the choices do not include another iron-sulfur cluster type."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record, whose cofactor annotation names a [4Fe-4S] cluster. The annotation is transferred by similarity from UniProtKB:Q7WTT9 (ECO:0000250), so it supports the key but is not direct experimental confirmation for this protein.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several repeated, cysteine-rich motifs, a recognizable pattern for iron-sulfur cluster coordination. Among the choices, that provides a meaningful biological basis for preferring the [4Fe-4S] option over FMN or the individual Cu(2+) and Co(2+) ions.",
    "missing_item_specific_fact": "Direct experimental confirmation that this particular protein binds [4Fe-4S] clusters, including the number and type of clusters, is not supplied.",
    "reason": "The sequence motifs and answer choices support a reasoned prediction of an iron-sulfur cofactor, though they do not establish exact cluster occupancy or replace protein-specific experimental evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cysteine-rich sequence pattern favors the only iron-sulfur-cluster option; the choices do not include another iron-sulfur cluster type."
  },
  "important_caveats": [
    "The supporting database cofactor annotation is similarity-transferred, not shown here as a direct measurement on the supplied protein.",
    "The protein-specific annotation and identity were reviewer-only and were not part of the evaluated input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A0A8X5N4 (Selenate reductase subunit B, EC 1.97.1.14), annotated with &#91;4Fe-4S&#93; cluster (4 copies). The annotation evidence code is ECO:0000250 (inferred by similarity from Q7WTT9), not direct experimental determination, but the sequence itself is highly consistent: it contains multiple cysteine-rich motifs with spacing patterns characteristic of &#91;4Fe-4S&#93; coordination (e.g., C-V-G-C-S-S-C-T-V-A-C-V ≈ C-x-x-C-x-x-C-x-x-C; C-I-G-C-R-Y-C-I-T-A-C-P; P-C-M-Q-C-E-H-P-P-C-T-K-V-C-P). The protein is described as an electron transport subunit, a role classically fulfilled by Fe-S clusters. The expected answer C is well supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains at least three distinct cysteine-rich motifs with 2–4 residue spacing between Cys residues (C-x-x-C-x-x-C-x-x-C and variants), which is the canonical coordination signature for &#91;4Fe-4S&#93; clusters. In contrast, the N-terminal 'GAGAAALGAGAF' is only a very weak resemblance to a GxGxxG Rossmann flavin-binding motif and lacks the full β-sheet Rossmann fold context needed for FMN binding. Cu(2+) sites typically require 2His+Cys+Met (type-1) or 3His (type-2) arrangements, which are absent. Co(2+) as a cofactor is rare outside corrinoid/B12-dependent enzymes and no corrinoid-binding motifs are present. The dominant Cys-cluster pattern and the electron-transport context (multiple small Cys-rich domains) allow a knowledgeable reader to select &#91;4Fe-4S&#93; over the other three options by general sequence-feature reasoning.


**Missing item-specific fact**

> None critical. The protein's specific identity as selenate reductase subunit B and the transferred annotation (ECO:0000250 from Q7WTT9) are not needed; the Cys-cluster motifs are directly observable in the supplied sequence.


**Reason**

> A model equipped with standard knowledge of Fe-S cluster binding motifs (Cys spacing patterns), flavin-binding Rossmann folds, and Cu/Co coordination chemistry can distinguish option C from A, B, and D using only the provided sequence. The multiple well-spaced Cys quartets are a concrete, sequence-visible argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically distinct cofactor classes. The Cys-rich motifs overwhelmingly favor Fe-S clusters; FMN, Cu(2+), and Co(2+) lack supporting sequence features. No other option is defensible from the sequence alone.


### Important caveats

- The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity transfer from Q7WTT9), not direct experimental proof for this specific protein. The primary paper (PubMed:21357486) characterized the srdBCA operon and confirmed selenate reductase activity but did not independently resolve the Fe-S cluster stoichiometry for subunit B.
- Distinguishing &#91;4Fe-4S&#93; from &#91;2Fe-2S&#93; purely from sequence is challenging; however, among the given choices only &#91;4Fe-4S&#93; is offered, so this sub-distinction does not affect the answer.
- The N-terminal GAGAAALGAGAF motif is a weak, non-diagnostic resemblance to a Rossmann flavin-binding motif and should not be over-interpreted as evidence for FMN.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains at least three distinct cysteine-rich motifs with 2–4 residue spacing between Cys residues (C-x-x-C-x-x-C-x-x-C and variants), which is the canonical coordination signature for [4Fe-4S] clusters. In contrast, the N-terminal 'GAGAAALGAGAF' is only a very weak resemblance to a GxGxxG Rossmann flavin-binding motif and lacks the full β-sheet Rossmann fold context needed for FMN binding. Cu(2+) sites typically require 2His+Cys+Met (type-1) or 3His (type-2) arrangements, which are absent. Co(2+) as a cofactor is rare outside corrinoid/B12-dependent enzymes and no corrinoid-binding motifs are present. The dominant Cys-cluster pattern and the electron-transport context (multiple small Cys-rich domains) allow a knowledgeable reader to select [4Fe-4S] over the other three options by general sequence-feature reasoning.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The protein's specific identity as selenate reductase subunit B and the transferred annotation (ECO:0000250 from Q7WTT9) are not needed; the Cys-cluster motifs are directly observable in the supplied sequence.",
    "reason": "A model equipped with standard knowledge of Fe-S cluster binding motifs (Cys spacing patterns), flavin-binding Rossmann folds, and Cu/Co coordination chemistry can distinguish option C from A, B, and D using only the provided sequence. The multiple well-spaced Cys quartets are a concrete, sequence-visible argument."
  },
  "case_id": "cofactor_0002",
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
    "reason": "The sequence matches UniProt A0A0A8X5N4 (Selenate reductase subunit B, EC 1.97.1.14), annotated with [4Fe-4S] cluster (4 copies). The annotation evidence code is ECO:0000250 (inferred by similarity from Q7WTT9), not direct experimental determination, but the sequence itself is highly consistent: it contains multiple cysteine-rich motifs with spacing patterns characteristic of [4Fe-4S] coordination (e.g., C-V-G-C-S-S-C-T-V-A-C-V ≈ C-x-x-C-x-x-C-x-x-C; C-I-G-C-R-Y-C-I-T-A-C-P; P-C-M-Q-C-E-H-P-P-C-T-K-V-C-P). The protein is described as an electron transport subunit, a role classically fulfilled by Fe-S clusters. The expected answer C is well supported."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity transfer from Q7WTT9), not direct experimental proof for this specific protein. The primary paper (PubMed:21357486) characterized the srdBCA operon and confirmed selenate reductase activity but did not independently resolve the Fe-S cluster stoichiometry for subunit B.",
    "Distinguishing [4Fe-4S] from [2Fe-2S] purely from sequence is challenging; however, among the given choices only [4Fe-4S] is offered, so this sub-distinction does not affect the answer.",
    "The N-terminal GAGAAALGAGAF motif is a weak, non-diagnostic resemblance to a Rossmann flavin-binding motif and should not be over-interpreted as evidence for FMN."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct cofactor classes. The Cys-rich motifs overwhelmingly favor Fe-S clusters; FMN, Cu(2+), and Co(2+) lack supporting sequence features. No other option is defensible from the sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A0A8X5N4 (Selenate reductase subunit B, EC 1.97.1.14), annotated with [4Fe-4S] cluster (4 copies). The annotation evidence code is ECO:0000250 (inferred by similarity from Q7WTT9), not direct experimental determination, but the sequence itself is highly consistent: it contains multiple cysteine-rich motifs with spacing patterns characteristic of [4Fe-4S] coordination (e.g., C-V-G-C-S-S-C-T-V-A-C-V ≈ C-x-x-C-x-x-C-x-x-C; C-I-G-C-R-Y-C-I-T-A-C-P; P-C-M-Q-C-E-H-P-P-C-T-K-V-C-P). The protein is described as an electron transport subunit, a role classically fulfilled by Fe-S clusters. The expected answer C is well supported.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains at least three distinct cysteine-rich motifs with 2–4 residue spacing between Cys residues (C-x-x-C-x-x-C-x-x-C and variants), which is the canonical coordination signature for [4Fe-4S] clusters. In contrast, the N-terminal 'GAGAAALGAGAF' is only a very weak resemblance to a GxGxxG Rossmann flavin-binding motif and lacks the full β-sheet Rossmann fold context needed for FMN binding. Cu(2+) sites typically require 2His+Cys+Met (type-1) or 3His (type-2) arrangements, which are absent. Co(2+) as a cofactor is rare outside corrinoid/B12-dependent enzymes and no corrinoid-binding motifs are present. The dominant Cys-cluster pattern and the electron-transport context (multiple small Cys-rich domains) allow a knowledgeable reader to select [4Fe-4S] over the other three options by general sequence-feature reasoning.",
    "missing_item_specific_fact": "None critical. The protein's specific identity as selenate reductase subunit B and the transferred annotation (ECO:0000250 from Q7WTT9) are not needed; the Cys-cluster motifs are directly observable in the supplied sequence.",
    "reason": "A model equipped with standard knowledge of Fe-S cluster binding motifs (Cys spacing patterns), flavin-binding Rossmann folds, and Cu/Co coordination chemistry can distinguish option C from A, B, and D using only the provided sequence. The multiple well-spaced Cys quartets are a concrete, sequence-visible argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct cofactor classes. The Cys-rich motifs overwhelmingly favor Fe-S clusters; FMN, Cu(2+), and Co(2+) lack supporting sequence features. No other option is defensible from the sequence alone."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (similarity transfer from Q7WTT9), not direct experimental proof for this specific protein. The primary paper (PubMed:21357486) characterized the srdBCA operon and confirmed selenate reductase activity but did not independently resolve the Fe-S cluster stoichiometry for subunit B.",
    "Distinguishing [4Fe-4S] from [2Fe-2S] purely from sequence is challenging; however, among the given choices only [4Fe-4S] is offered, so this sub-distinction does not affect the answer.",
    "The N-terminal GAGAAALGAGAF motif is a weak, non-diagnostic resemblance to a Rossmann flavin-binding motif and should not be over-interpreted as evidence for FMN."
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

**Accession:** `A0A0A8X5N4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 28. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:58.709600+00:00.  

```json
"A0A0A8X5N4"
```

Source SHA-256: `ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:58.709600+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Selenate reductase electron transport subunit"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"21357486","source":"PubMed"}],"value":"1.97.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Selenate reductase subunit B"}}}
```

Source SHA-256: `ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0A8X5N4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:58.709600+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:49883"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q7WTT9","source":"UniProtKB"}],"name":"[4Fe-4S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q7WTT9","source":"UniProtKB"}],"value":"Binds 4 [4Fe-4S] cluster."}]}}
```

Source SHA-256: `ad4296ea74491ed50535947ea88c00f59f9264d4b7e02a26604d154b65d36999`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:01.544310+00:00.  

```text
ID   SRDB_MESS1              Reviewed;         292 AA.
AC   A0A0A8X5N4; E9RFC9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   04-MAR-2015, sequence version 1.
DT   28-JAN-2026, entry version 28.
DE   RecName: Full=Selenate reductase subunit B {ECO:0000305};
DE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};
DE   AltName: Full=Selenate reductase electron transport subunit {ECO:0000305};
DE   Flags: Precursor;
GN   Name=srdB {ECO:0000303|PubMed:21357486};
GN   ORFNames=SAMD00020551_1550 {ECO:0000312|EMBL:GAM13406.1};
OS   Mesobacillus selenatarsenatis (strain DSM 18680 / JCM 14380 / FERM P-15431
OS   / SF-1).
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;
OC   Mesobacillus.
OX   NCBI_TaxID=1321606;
```

Source SHA-256: `d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:01.544310+00:00.  

```text
DE   RecName: Full=Selenate reductase subunit B {ECO:0000305};
DE            EC=1.97.1.14 {ECO:0000305|PubMed:21357486};
DE   AltName: Full=Selenate reductase electron transport subunit {ECO:0000305};
DE   Flags: Precursor;
```

Source SHA-256: `d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0A8X5N4?format=txt&versions=28)  
**Locator:** `lines 47-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:01.544310+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;
CC         Evidence={ECO:0000250|UniProtKB:Q7WTT9};
CC       Note=Binds 4 [4Fe-4S] cluster. {ECO:0000250|UniProtKB:Q7WTT9};
```

Source SHA-256: `d0917601898661906f576d07a10b60378261919ac0854faebd606db893a6272d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
