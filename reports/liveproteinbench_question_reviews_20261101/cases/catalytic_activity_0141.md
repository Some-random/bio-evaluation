# catalytic_activity_0141

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — an N(6)-methyladenosine in mRNA + 2-oxoglutarate + O2 = an adenosine in mRNA + formaldehyde + succinate + CO2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVNLTELDAHEQPSDQMRAIWKSYSRADKEELLLNGAIDDLEKPEKAAEFVVAGTVPAATLTKGFAFLGSGFDAAASDAPIYYHPLLPGLLIFPSIVPLEVQKTLLSKLIHRDLSVPAHQTNMHLHYELPYVERKPTDGEGEPEDCRQSFFSHSPDSPVRFQPKDPDVHKPLSMKQVMDRRLHWVTLGGQYDWTNRVYPEEEPPKFPPDVAGFLETVFPDTIAQAAIVNFYTPGDTMMMHRDVSEETDKGLVSLSLGCDGLFMIAPSDIGKMSEEERPEDVKKQYLLLRLRSGDAIYMIKESRYAWHGVPKVLKGTCPEALEDWPAEDGRFEEWRGWMKNKRINLNVRQMRE

[Multiple Choices]
A. alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate
B. an N(6)-methyladenosine in mRNA + 2-oxoglutarate + O2 = an adenosine in mRNA + formaldehyde + succinate + CO2
C. Cs(+)(in) = Cs(+)(out)
D. 2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2 H2O
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

> The exact sequence matches UniProt entry G4MZ21, whose catalytic-activity annotation gives the reaction in choice B. The reaction annotation is transferred by similarity (ECO:0000250), so this supports the key as a database annotation but is not direct evidence that this exact protein was experimentally assayed for the reaction.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice B describes an Fe(II)/2-oxoglutarate-dependent dioxygenase reaction, which is compatible with a protein of this broad class; however, that does not establish this protein's substrate or distinguish m6A demethylation from other possible functions.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence identifying this sequence as an m6A RNA demethylase is absent from the input.


**Reason**

> The sequence and choices do not provide a reliable basis for identifying the specific substrate transformation. Selecting B requires the item-specific functional assignment, not merely recognizing a broad enzyme class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied information does not establish another choice as the reaction, but it also does not independently distinguish B from the alternatives at the required substrate-specific level.


### Important caveats

- The sequence match is exact, but the evidence supporting the catalytic reaction is transferred by similarity; the cited experimental evidence for EC assignment does not by itself show that this exact protein was assayed.
- The reviewer-only database evidence supports the expected answer but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice B describes an Fe(II)/2-oxoglutarate-dependent dioxygenase reaction, which is compatible with a protein of this broad class; however, that does not establish this protein's substrate or distinguish m6A demethylation from other possible functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence identifying this sequence as an m6A RNA demethylase is absent from the input.",
    "reason": "The sequence and choices do not provide a reliable basis for identifying the specific substrate transformation. Selecting B requires the item-specific functional assignment, not merely recognizing a broad enzyme class."
  },
  "case_id": "catalytic_activity_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry G4MZ21, whose catalytic-activity annotation gives the reaction in choice B. The reaction annotation is transferred by similarity (ECO:0000250), so this supports the key as a database annotation but is not direct evidence that this exact protein was experimentally assayed for the reaction."
  },
  "important_caveats": [
    "The sequence match is exact, but the evidence supporting the catalytic reaction is transferred by similarity; the cited experimental evidence for EC assignment does not by itself show that this exact protein was assayed.",
    "The reviewer-only database evidence supports the expected answer but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied information does not establish another choice as the reaction, but it also does not independently distinguish B from the alternatives at the required substrate-specific level."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry G4MZ21, whose catalytic-activity annotation gives the reaction in choice B. The reaction annotation is transferred by similarity (ECO:0000250), so this supports the key as a database annotation but is not direct evidence that this exact protein was experimentally assayed for the reaction.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice B describes an Fe(II)/2-oxoglutarate-dependent dioxygenase reaction, which is compatible with a protein of this broad class; however, that does not establish this protein's substrate or distinguish m6A demethylation from other possible functions.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence identifying this sequence as an m6A RNA demethylase is absent from the input.",
    "reason": "The sequence and choices do not provide a reliable basis for identifying the specific substrate transformation. Selecting B requires the item-specific functional assignment, not merely recognizing a broad enzyme class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied information does not establish another choice as the reaction, but it also does not independently distinguish B from the alternatives at the required substrate-specific level."
  },
  "important_caveats": [
    "The sequence match is exact, but the evidence supporting the catalytic reaction is transferred by similarity; the cited experimental evidence for EC assignment does not by itself show that this exact protein was assayed.",
    "The reviewer-only database evidence supports the expected answer but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt G4MZ21 (ALKB1_PYRO7), annotated as N6-methyladenosine RNA demethylase ALKB1 (EC 1.14.11.53). The catalytic activity reaction in the UniProt entry is verbatim identical to choice B. The EC assignment carries ECO:0000269 (experimental evidence, PubMed:30535195); the specific Rhea reaction is annotated via ECO:0000250 (similarity to A0A9P4XUZ4). The protein name is supported by literature (ECO:0000303). The annotation is consistent across both current and historical (v55) records.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 353-residue sequence contains recognizable ALKB-family structural motifs: a putative HxD…H…H Fe(II)-coordinating triad (e.g., H…H…H in the 'HQTNMHLHYEL' region, conserved Asp in 'GGQYDWTNRV'), a 2-oxoglutarate-binding region ('GCDGLFMIAPSDIG'), and an overall jelly-roll domain architecture. The protein size (353 aa) is consistent with the small ALKB/ALKBH subfamily but too small for TET (~1000 aa) or FTO (~505 aa). Among the four choices, only B describes a Fe(II)/2-oxoglutarate-dependent dioxygenase reaction; A is a TIM-barrel isomerase, C is a transmembrane ion transporter, and D is a flavin-dependent oxidase. Recognizing the sequence as an ALKB-family dioxygenase eliminates A, C, and D, leaving B.


**Missing item-specific fact**

> None that is strictly required. Distinguishing ALKB1 (m6A RNA demethylase) from other ALKB members (DNA-repair ALKBs, ALKBH5, FTO) by sequence alone is non-trivial, but the question only requires identifying the enzyme class (dioxygenase) to select B over the three structurally unrelated distractors.


**Reason**

> A knowledgeable reader can identify ALKB-family sequence features (size, HxD…H…H triad, 2OG-binding region, jelly-roll fold) and use the fact that only option B is a dioxygenase reaction to select the answer. This constitutes a concrete biological reasoning pathway from the supplied sequence to the correct choice, without needing to memorize the specific UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four fundamentally different enzyme classes (isomerase, dioxygenase, transporter, flavin oxidase). The sequence features unambiguously point to a dioxygenase, making B the only defensible choice. No other option is compatible with the observed domain architecture.


### Important caveats

- The UniProt catalytic-activity annotation for this entry is transferred by similarity (ECO:0000250) from A0A9P4XUZ4, not independently demonstrated for this exact protein; however, the EC number assignment itself is backed by experimental evidence (ECO:0000269, PubMed:30535195).
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark input and the UniProt entry, so the annotation applies to the exact sequence presented.
- While recognizing the ALKB family from a 353-aa fungal sequence is feasible for an expert, it is not trivial for all readers; the question is moderately difficult but reasoning-grounded rather than pure lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 353-residue sequence contains recognizable ALKB-family structural motifs: a putative HxD…H…H Fe(II)-coordinating triad (e.g., H…H…H in the 'HQTNMHLHYEL' region, conserved Asp in 'GGQYDWTNRV'), a 2-oxoglutarate-binding region ('GCDGLFMIAPSDIG'), and an overall jelly-roll domain architecture. The protein size (353 aa) is consistent with the small ALKB/ALKBH subfamily but too small for TET (~1000 aa) or FTO (~505 aa). Among the four choices, only B describes a Fe(II)/2-oxoglutarate-dependent dioxygenase reaction; A is a TIM-barrel isomerase, C is a transmembrane ion transporter, and D is a flavin-dependent oxidase. Recognizing the sequence as an ALKB-family dioxygenase eliminates A, C, and D, leaving B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is strictly required. Distinguishing ALKB1 (m6A RNA demethylase) from other ALKB members (DNA-repair ALKBs, ALKBH5, FTO) by sequence alone is non-trivial, but the question only requires identifying the enzyme class (dioxygenase) to select B over the three structurally unrelated distractors.",
    "reason": "A knowledgeable reader can identify ALKB-family sequence features (size, HxD…H…H triad, 2OG-binding region, jelly-roll fold) and use the fact that only option B is a dioxygenase reaction to select the answer. This constitutes a concrete biological reasoning pathway from the supplied sequence to the correct choice, without needing to memorize the specific UniProt annotation."
  },
  "case_id": "catalytic_activity_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt G4MZ21 (ALKB1_PYRO7), annotated as N6-methyladenosine RNA demethylase ALKB1 (EC 1.14.11.53). The catalytic activity reaction in the UniProt entry is verbatim identical to choice B. The EC assignment carries ECO:0000269 (experimental evidence, PubMed:30535195); the specific Rhea reaction is annotated via ECO:0000250 (similarity to A0A9P4XUZ4). The protein name is supported by literature (ECO:0000303). The annotation is consistent across both current and historical (v55) records."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation for this entry is transferred by similarity (ECO:0000250) from A0A9P4XUZ4, not independently demonstrated for this exact protein; however, the EC number assignment itself is backed by experimental evidence (ECO:0000269, PubMed:30535195).",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark input and the UniProt entry, so the annotation applies to the exact sequence presented.",
    "While recognizing the ALKB family from a 353-aa fungal sequence is feasible for an expert, it is not trivial for all readers; the question is moderately difficult but reasoning-grounded rather than pure lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four fundamentally different enzyme classes (isomerase, dioxygenase, transporter, flavin oxidase). The sequence features unambiguously point to a dioxygenase, making B the only defensible choice. No other option is compatible with the observed domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt G4MZ21 (ALKB1_PYRO7), annotated as N6-methyladenosine RNA demethylase ALKB1 (EC 1.14.11.53). The catalytic activity reaction in the UniProt entry is verbatim identical to choice B. The EC assignment carries ECO:0000269 (experimental evidence, PubMed:30535195); the specific Rhea reaction is annotated via ECO:0000250 (similarity to A0A9P4XUZ4). The protein name is supported by literature (ECO:0000303). The annotation is consistent across both current and historical (v55) records.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 353-residue sequence contains recognizable ALKB-family structural motifs: a putative HxD…H…H Fe(II)-coordinating triad (e.g., H…H…H in the 'HQTNMHLHYEL' region, conserved Asp in 'GGQYDWTNRV'), a 2-oxoglutarate-binding region ('GCDGLFMIAPSDIG'), and an overall jelly-roll domain architecture. The protein size (353 aa) is consistent with the small ALKB/ALKBH subfamily but too small for TET (~1000 aa) or FTO (~505 aa). Among the four choices, only B describes a Fe(II)/2-oxoglutarate-dependent dioxygenase reaction; A is a TIM-barrel isomerase, C is a transmembrane ion transporter, and D is a flavin-dependent oxidase. Recognizing the sequence as an ALKB-family dioxygenase eliminates A, C, and D, leaving B.",
    "missing_item_specific_fact": "None that is strictly required. Distinguishing ALKB1 (m6A RNA demethylase) from other ALKB members (DNA-repair ALKBs, ALKBH5, FTO) by sequence alone is non-trivial, but the question only requires identifying the enzyme class (dioxygenase) to select B over the three structurally unrelated distractors.",
    "reason": "A knowledgeable reader can identify ALKB-family sequence features (size, HxD…H…H triad, 2OG-binding region, jelly-roll fold) and use the fact that only option B is a dioxygenase reaction to select the answer. This constitutes a concrete biological reasoning pathway from the supplied sequence to the correct choice, without needing to memorize the specific UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four fundamentally different enzyme classes (isomerase, dioxygenase, transporter, flavin oxidase). The sequence features unambiguously point to a dioxygenase, making B the only defensible choice. No other option is compatible with the observed domain architecture."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation for this entry is transferred by similarity (ECO:0000250) from A0A9P4XUZ4, not independently demonstrated for this exact protein; however, the EC number assignment itself is backed by experimental evidence (ECO:0000269, PubMed:30535195).",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark input and the UniProt entry, so the annotation applies to the exact sequence presented.",
    "While recognizing the ALKB family from a 353-aa fungal sequence is feasible for an expert, it is not trivial for all readers; the question is moderately difficult but reasoning-grounded rather than pure lookup."
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

**Accession:** `G4MZ21` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MZ21.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:43.333607+00:00.  

```json
"G4MZ21"
```

Source SHA-256: `912b707615953e09c752dc6d954d39172df78da8b465c36f8304f450ed73836b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MZ21.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:43.333607+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"M6A eraser ALKB1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Nucleic acid dioxygenase ALKB1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30535195","source":"PubMed"}],"value":"1.14.11.53"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30535195","source":"PubMed"}],"value":"N6-methyladenosine RNA demethylase ALKB1"}}}
```

Source SHA-256: `912b707615953e09c752dc6d954d39172df78da8b465c36f8304f450ed73836b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MZ21.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:43.333607+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A9P4XUZ4","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:49521"}}],"reaction":{"ecNumber":"1.14.11.53","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A9P4XUZ4","source":"UniProtKB"}],"name":"an N(6)-methyladenosine in mRNA + 2-oxoglutarate + O2 = an adenosine in mRNA + formaldehyde + succinate + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:49520"},{"database":"Rhea","id":"RHEA-COMP:12414"},{"database":"Rhea","id":"RHEA-COMP:12417"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:16810"},{"database":"ChEBI","id":"CHEBI:16842"},{"database":"ChEBI","id":"CHEBI:30031"},{"database":"ChEBI","id":"CHEBI:74411"},{"database":"ChEBI","id":"CHEBI:74449"}]}}
```

Source SHA-256: `912b707615953e09c752dc6d954d39172df78da8b465c36f8304f450ed73836b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MZ21?format=txt&versions=55)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:28:46.833043+00:00.  

```text
DE   RecName: Full=N6-methyladenosine RNA demethylase ALKB1 {ECO:0000303|PubMed:30535195};
DE            EC=1.14.11.53 {ECO:0000269|PubMed:30535195};
DE   AltName: Full=M6A eraser ALKB1 {ECO:0000305};
DE   AltName: Full=Nucleic acid dioxygenase ALKB1 {ECO:0000305};
```

Source SHA-256: `e832e85da73e8a1dac05b9fac1aca7862c0ad15ede95319cb354b3e45fe3fb4e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MZ21?format=txt&versions=55)  
**Locator:** `lines 41-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:28:46.833043+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an N(6)-methyladenosine in mRNA + 2-oxoglutarate + O2 = an
CC         adenosine in mRNA + formaldehyde + succinate + CO2;
CC         Xref=Rhea:RHEA:49520, Rhea:RHEA-COMP:12414, Rhea:RHEA-COMP:12417,
CC         ChEBI:CHEBI:15379, ChEBI:CHEBI:16526, ChEBI:CHEBI:16810,
CC         ChEBI:CHEBI:16842, ChEBI:CHEBI:30031, ChEBI:CHEBI:74411,
CC         ChEBI:CHEBI:74449; EC=1.14.11.53;
CC         Evidence={ECO:0000250|UniProtKB:A0A9P4XUZ4};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49521;
CC         Evidence={ECO:0000250|UniProtKB:A0A9P4XUZ4};
```

Source SHA-256: `e832e85da73e8a1dac05b9fac1aca7862c0ad15ede95319cb354b3e45fe3fb4e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
