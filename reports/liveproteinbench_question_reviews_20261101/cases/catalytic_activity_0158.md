# catalytic_activity_0158

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAATDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNDMGCFTYPLVPGFETVGTATEVGSKVTKVKVGDKVAVGIMVGSCGKCDECVNDRECYCPEVITSYGRIDHDGTPTYGGFSSETVANEKFVFCFPEKLPMAAGAPLLNAGVSVYSAMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSTSKKGEAINDLGADAFLVSTDAEQMQAGSGTLDGILDTVPVVHPIEALLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVVSTIGGSTKETQEMLDFAAEHDITASVEIIPMDYVNTAMERIEKGDVRYRFVIDIGNTLTPPES

[Multiple Choices]
A. roxarsone (III) + AH2 + O2 = 4-hydroxy-3-nitrocyclohexa-2,5-dien-1-one + arsenite + A + H(+)
B. cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)
C. 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)
D. beta-L-fucose 1-phosphate + GTP + H(+) = GDP-beta-L-fucose + diphosphate
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

> The supplied sequence exactly matches the 363-aa UniProt entry annotated as 1,2-dihydrovomilenine reductase. That entry lists the reaction in choice C and cites experimental evidence for the catalytic activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may support an NAD(P)-dependent oxidoreductase, which is more consistent with C than the methyltransferase or nucleotide-sugar reaction choices. But that class-level inference does not establish the named alkaloid substrate and product.


**Missing item-specific fact**

> The protein-specific functional assignment linking this sequence to 1,2-dihydrovomilenine reductase and its alkaloid reaction.


**Reason**

> Selecting the precise reaction requires a protein-specific substrate/function fact not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence catalytic-activity annotation supports choice C; the evidence provided does not support another listed reaction for this protein.


### Important caveats

- The annotation cites experimental evidence codes, but the primary studies were not independently reviewed here.
- The sequence match is exact, while the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may support an NAD(P)-dependent oxidoreductase, which is more consistent with C than the methyltransferase or nucleotide-sugar reaction choices. But that class-level inference does not establish the named alkaloid substrate and product.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment linking this sequence to 1,2-dihydrovomilenine reductase and its alkaloid reaction.",
    "reason": "Selecting the precise reaction requires a protein-specific substrate/function fact not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "catalytic_activity_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 363-aa UniProt entry annotated as 1,2-dihydrovomilenine reductase. That entry lists the reaction in choice C and cites experimental evidence for the catalytic activity."
  },
  "important_caveats": [
    "The annotation cites experimental evidence codes, but the primary studies were not independently reviewed here.",
    "The sequence match is exact, while the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence catalytic-activity annotation supports choice C; the evidence provided does not support another listed reaction for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 363-aa UniProt entry annotated as 1,2-dihydrovomilenine reductase. That entry lists the reaction in choice C and cites experimental evidence for the catalytic activity.",
    "evidence_ids": ["C1", "C4", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may support an NAD(P)-dependent oxidoreductase, which is more consistent with C than the methyltransferase or nucleotide-sugar reaction choices. But that class-level inference does not establish the named alkaloid substrate and product.",
    "missing_item_specific_fact": "The protein-specific functional assignment linking this sequence to 1,2-dihydrovomilenine reductase and its alkaloid reaction.",
    "reason": "Selecting the precise reaction requires a protein-specific substrate/function fact not supplied in the question. Recognizing the sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence catalytic-activity annotation supports choice C; the evidence provided does not support another listed reaction for this protein."
  },
  "important_caveats": [
    "The annotation cites experimental evidence codes, but the primary studies were not independently reviewed here.",
    "The sequence match is exact, while the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt entry A0A0U3S9Q3 (DHVOR_RAUSE, 1,2-Dihydrovomilenine reductase, EC 1.3.1.73) from Rauvolfia serpentina. The annotated primary catalytic activity is precisely '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)', supported by experimental evidence (ECO:0000269, inferred from direct assay) from PubMed:12391554 and PubMed:38212296. The sequence match is confirmed (SHA256 identical) in both current and historical (entry v32) records.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold-like NAD(P)-binding motif (GATMGSFELPILPLGVGRK), characteristic of medium-chain dehydrogenase/reductase (MDR/CAD-like) enzymes. This motif directly supports NADP+ as a cofactor, eliminating Choice B (SAM-dependent methyltransferase, which would show a distinct SAM-binding fold) and Choice D (GTP-dependent guanylyltransferase, which would show P-loop/GTP-binding motifs). Choice A describes a flavin-dependent oxidase/monooxygenase mechanism using AH2 + O2 (not NADP+), which is inconsistent with the observed NAD(P)-binding Rossmann motif. Choice C is the only option whose cofactor requirement (NADP+) matches the identifiable structural motif in the sequence. Additionally, the overall two-domain CAD-like/MDR architecture is characteristic of plant secondary-metabolism reductases rather than bacterial arsenic-metabolism enzymes.


**Missing item-specific fact**

> The specific substrate identity (17-O-acetylnorajmaline) and the exact stereochemistry of the product ((2R)-1,2-dihydrovomilenine) cannot be deduced from sequence alone; however, for a multiple-choice format, the cofactor/fold reasoning is sufficient to eliminate the other three options.


**Reason**

> While the precise substrate name cannot be derived from the sequence, the choices differ in cofactor chemistry (NADP+ vs. SAM vs. GTP vs. flavin/O2), and the sequence contains an identifiable NAD(P)-binding motif. This provides a concrete structural-biochemistry argument to select C over A, B, and D without needing to memorize the exact UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cofactor chemistry in the four choices is mutually exclusive (NADP+ reductase vs. SAM methyltransferase vs. GTP guanylyltransferase vs. flavin-dependent oxidase), and the sequence's Rossmann-fold motif unambiguously points to an NAD(P)-dependent oxidoreductase, making C the only consistent choice.


### Important caveats

- The enzyme also has a secondary annotated activity (vomilenine reductase 2, EC 1.5.1.-) catalyzing (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+), but this reaction is not among the choices.
- The physiological direction is right-to-left (reduction of 1,2-dihydrovomilenine to 17-O-acetylnorajmaline in vivo), though the written reaction in the choice is the reverse (oxidation direction as listed in Rhea:RHEA:12320). The choice text matches the UniProt/Rhea listing exactly.
- The reasoning path relies on recognizing the GATMGSF motif as an NAD(P)-binding Rossmann fold; a model unfamiliar with this specific motif pattern might struggle to eliminate all distractors.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold-like NAD(P)-binding motif (GATMGSFELPILPLGVGRK), characteristic of medium-chain dehydrogenase/reductase (MDR/CAD-like) enzymes. This motif directly supports NADP+ as a cofactor, eliminating Choice B (SAM-dependent methyltransferase, which would show a distinct SAM-binding fold) and Choice D (GTP-dependent guanylyltransferase, which would show P-loop/GTP-binding motifs). Choice A describes a flavin-dependent oxidase/monooxygenase mechanism using AH2 + O2 (not NADP+), which is inconsistent with the observed NAD(P)-binding Rossmann motif. Choice C is the only option whose cofactor requirement (NADP+) matches the identifiable structural motif in the sequence. Additionally, the overall two-domain CAD-like/MDR architecture is characteristic of plant secondary-metabolism reductases rather than bacterial arsenic-metabolism enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (17-O-acetylnorajmaline) and the exact stereochemistry of the product ((2R)-1,2-dihydrovomilenine) cannot be deduced from sequence alone; however, for a multiple-choice format, the cofactor/fold reasoning is sufficient to eliminate the other three options.",
    "reason": "While the precise substrate name cannot be derived from the sequence, the choices differ in cofactor chemistry (NADP+ vs. SAM vs. GTP vs. flavin/O2), and the sequence contains an identifiable NAD(P)-binding motif. This provides a concrete structural-biochemistry argument to select C over A, B, and D without needing to memorize the exact UniProt annotation."
  },
  "case_id": "catalytic_activity_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A0U3S9Q3 (DHVOR_RAUSE, 1,2-Dihydrovomilenine reductase, EC 1.3.1.73) from Rauvolfia serpentina. The annotated primary catalytic activity is precisely '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)', supported by experimental evidence (ECO:0000269, inferred from direct assay) from PubMed:12391554 and PubMed:38212296. The sequence match is confirmed (SHA256 identical) in both current and historical (entry v32) records."
  },
  "important_caveats": [
    "The enzyme also has a secondary annotated activity (vomilenine reductase 2, EC 1.5.1.-) catalyzing (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+), but this reaction is not among the choices.",
    "The physiological direction is right-to-left (reduction of 1,2-dihydrovomilenine to 17-O-acetylnorajmaline in vivo), though the written reaction in the choice is the reverse (oxidation direction as listed in Rhea:RHEA:12320). The choice text matches the UniProt/Rhea listing exactly.",
    "The reasoning path relies on recognizing the GATMGSF motif as an NAD(P)-binding Rossmann fold; a model unfamiliar with this specific motif pattern might struggle to eliminate all distractors."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cofactor chemistry in the four choices is mutually exclusive (NADP+ reductase vs. SAM methyltransferase vs. GTP guanylyltransferase vs. flavin-dependent oxidase), and the sequence's Rossmann-fold motif unambiguously points to an NAD(P)-dependent oxidoreductase, making C the only consistent choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A0U3S9Q3 (DHVOR_RAUSE, 1,2-Dihydrovomilenine reductase, EC 1.3.1.73) from Rauvolfia serpentina. The annotated primary catalytic activity is precisely '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)', supported by experimental evidence (ECO:0000269, inferred from direct assay) from PubMed:12391554 and PubMed:38212296. The sequence match is confirmed (SHA256 identical) in both current and historical (entry v32) records.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold-like NAD(P)-binding motif (GATMGSFELPILPLGVGRK), characteristic of medium-chain dehydrogenase/reductase (MDR/CAD-like) enzymes. This motif directly supports NADP+ as a cofactor, eliminating Choice B (SAM-dependent methyltransferase, which would show a distinct SAM-binding fold) and Choice D (GTP-dependent guanylyltransferase, which would show P-loop/GTP-binding motifs). Choice A describes a flavin-dependent oxidase/monooxygenase mechanism using AH2 + O2 (not NADP+), which is inconsistent with the observed NAD(P)-binding Rossmann motif. Choice C is the only option whose cofactor requirement (NADP+) matches the identifiable structural motif in the sequence. Additionally, the overall two-domain CAD-like/MDR architecture is characteristic of plant secondary-metabolism reductases rather than bacterial arsenic-metabolism enzymes.",
    "missing_item_specific_fact": "The specific substrate identity (17-O-acetylnorajmaline) and the exact stereochemistry of the product ((2R)-1,2-dihydrovomilenine) cannot be deduced from sequence alone; however, for a multiple-choice format, the cofactor/fold reasoning is sufficient to eliminate the other three options.",
    "reason": "While the precise substrate name cannot be derived from the sequence, the choices differ in cofactor chemistry (NADP+ vs. SAM vs. GTP vs. flavin/O2), and the sequence contains an identifiable NAD(P)-binding motif. This provides a concrete structural-biochemistry argument to select C over A, B, and D without needing to memorize the exact UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cofactor chemistry in the four choices is mutually exclusive (NADP+ reductase vs. SAM methyltransferase vs. GTP guanylyltransferase vs. flavin-dependent oxidase), and the sequence's Rossmann-fold motif unambiguously points to an NAD(P)-dependent oxidoreductase, making C the only consistent choice."
  },
  "important_caveats": [
    "The enzyme also has a secondary annotated activity (vomilenine reductase 2, EC 1.5.1.-) catalyzing (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+), but this reaction is not among the choices.",
    "The physiological direction is right-to-left (reduction of 1,2-dihydrovomilenine to 17-O-acetylnorajmaline in vivo), though the written reaction in the choice is the reverse (oxidation direction as listed in Rhea:RHEA:12320). The choice text matches the UniProt/Rhea listing exactly.",
    "The reasoning path relies on recognizing the GATMGSF motif as an NAD(P)-binding Rossmann fold; a model unfamiliar with this specific motif pattern might struggle to eliminate all distractors."
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

**Accession:** `A0A0U3S9Q3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
"A0A0U3S9Q3"
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Protein RR4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsRR4"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Vomilenine reductase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsVR2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"12391554","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"1.3.1.73"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"1,2-Dihydrovomilenine reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RsDHVR"}]}}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.228210+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"12391554","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:12322"}}],"reaction":{"ecNumber":"1.3.1.73","evidences":[{"evidenceCode":"ECO:0000269","id":"12391554","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"name":"17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:12320"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17372"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:77725"}]}}
```

Source SHA-256: `ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)  
**Locator:** `lines 1-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:20.990872+00:00.  

```text
ID   DHVOR_RAUSE             Reviewed;         363 AA.
AC   A0A0U3S9Q3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-MAR-2016, sequence version 1.
DT   28-JAN-2026, entry version 32.
DE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};
DE            Short=RsDHVR {ECO:0000303|PubMed:26715562};
DE            EC=1.3.1.73 {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};
DE   AltName: Full=Protein RR4 {ECO:0000303|PubMed:26715562};
DE            Short=RsRR4 {ECO:0000303|PubMed:26715562};
DE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};
DE            Short=RsVR2 {ECO:0000303|PubMed:26715562};
DE            EC=1.5.1.- {ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296};
GN   Name=DHVR {ECO:0000303|PubMed:26715562};
GN   Synonyms=RR4 {ECO:0000303|PubMed:26715562},
GN   VR2 {ECO:0000303|PubMed:26715562};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)  
**Locator:** `lines 57-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:20.990872+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine
CC         + NADPH + 2 H(+); Xref=Rhea:RHEA:12320, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:17372, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,
CC         ChEBI:CHEBI:77725; EC=1.3.1.73;
CC         Evidence={ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:12322;
CC         Evidence={ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};
```

Source SHA-256: `d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 158. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
