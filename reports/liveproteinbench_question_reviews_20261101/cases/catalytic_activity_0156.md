# catalytic_activity_0156

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDMKAIHFGGGNIGRGFVAEFLHKSGYEVVFVDVMDAIINALQQNKSYTVTEVGTSETKSKTIDNYRAINSKTDEDKVVEEIATADIVTCAVGPNILKFIAPVIAKGIENRKKDSPIAVIACENAIGATDTLRKFIEEKLSDSTKSNIQDKARFANSAIDRIVPMQDENAGLNVKIEKFYEWCVESKPFLPSQPPKIEGVHFVEDLTPFIERKLFTVNTGHATAAYYGYNRGKECIHDVLQDKELNEIVRNTLKETAHLIVNKHEISEEDQNQYVEKIIKRISNPVLKDNVERVGRAPLRKLSRNERFIGPAAHLAEMGAKYDALLGGIEMCLRFQNVEGDDESFELAKILKENSSSDATEKITGLERNHTLFPAVEEVVKKVQA

[Multiple Choices]
A. L-tyrosine + reduced [NADPH--hemoprotein reductase] + O2 = L-dopa + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
B. (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(ethyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)
C. D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)
D. vinorine + reduced [NADPH--hemoprotein reductase] + O2 = vomilenine + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
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

> The exact sequence matches a UniProt entry annotated as mannitol-1-phosphate 5-dehydrogenase with the reaction in choice C. The annotation supports the key, but its EC assignment is transferred by similarity, not shown here as direct experimental verification for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal glycine-rich region is consistent with a dinucleotide-binding oxidoreductase, and choice C is the only NAD(+)/NADH-dependent reaction. The alternatives instead invoke oxygen-dependent hemoprotein-reductase chemistry or SAM-dependent chemistry, for which the sequence provides no comparable signature.


**Missing item-specific fact**

> The motif does not by itself establish mannitol-1-phosphate as the substrate or prove the exact product; that specificity is supported by the reviewer-only annotation.


**Reason**

> Sequence-based cofactor and enzyme-class clues meaningfully distinguish the listed reaction classes, although they do not independently establish the precise substrate conversion.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, only C matches an NAD(+)-dependent dehydrogenase reaction.


### Important caveats

- The sequence match is exact, but the supplied database annotation assigns EC 1.1.1.17 by similarity; the excerpts do not establish direct experimental measurement of this sequence's activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich region is consistent with a dinucleotide-binding oxidoreductase, and choice C is the only NAD(+)/NADH-dependent reaction. The alternatives instead invoke oxygen-dependent hemoprotein-reductase chemistry or SAM-dependent chemistry, for which the sequence provides no comparable signature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The motif does not by itself establish mannitol-1-phosphate as the substrate or prove the exact product; that specificity is supported by the reviewer-only annotation.",
    "reason": "Sequence-based cofactor and enzyme-class clues meaningfully distinguish the listed reaction classes, although they do not independently establish the precise substrate conversion."
  },
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as mannitol-1-phosphate 5-dehydrogenase with the reaction in choice C. The annotation supports the key, but its EC assignment is transferred by similarity, not shown here as direct experimental verification for this sequence."
  },
  "important_caveats": [
    "The sequence match is exact, but the supplied database annotation assigns EC 1.1.1.17 by similarity; the excerpts do not establish direct experimental measurement of this sequence's activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, only C matches an NAD(+)-dependent dehydrogenase reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as mannitol-1-phosphate 5-dehydrogenase with the reaction in choice C. The annotation supports the key, but its EC assignment is transferred by similarity, not shown here as direct experimental verification for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal glycine-rich region is consistent with a dinucleotide-binding oxidoreductase, and choice C is the only NAD(+)/NADH-dependent reaction. The alternatives instead invoke oxygen-dependent hemoprotein-reductase chemistry or SAM-dependent chemistry, for which the sequence provides no comparable signature.",
    "missing_item_specific_fact": "The motif does not by itself establish mannitol-1-phosphate as the substrate or prove the exact product; that specificity is supported by the reviewer-only annotation.",
    "reason": "Sequence-based cofactor and enzyme-class clues meaningfully distinguish the listed reaction classes, although they do not independently establish the precise substrate conversion."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, only C matches an NAD(+)-dependent dehydrogenase reaction."
  },
  "important_caveats": [
    "The sequence match is exact, but the supplied database annotation assigns EC 1.1.1.17 by similarity; the excerpts do not establish direct experimental measurement of this sequence's activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence (386 AA) matches UniProt entry A0A223HDH4 (MPDH_AURME), which is annotated as Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17). The catalytic activity annotation explicitly states: D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+), matching Choice C verbatim. The EC assignment carries evidence code ECO:0000250 (similarity to Q4X1A4), but the entry also cites PubMed 32003433 for FUNCTION and DISRUPTION PHENOTYPE, providing experimental support for the enzymatic role in Aureobasidium melanogenum. The sequence match is exact (sha256 confirmed) across both current and historical (v15) snapshots.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Partial elimination is possible: the sequence lacks the canonical P450 heme-binding motif (FxxGxxxCxG), arguing against Choices A and D (both cytochrome P450 monooxygenases), and lacks the radical SAM CxxxCxxC motif, arguing against Choice B. A Rossmann-like GxGxxG pattern (GGGNIGRGF) near the N-terminus is consistent with NAD-binding dehydrogenases. However, this only narrows the class to 'NAD-dependent dehydrogenase'—it does not identify the specific substrate as mannitol-1-phosphate rather than glucose-6-phosphate, lactate, sorbitol, or hundreds of other possible substrates.


**Missing item-specific fact**

> The specific substrate identity (mannitol-1-phosphate vs. other sugar-phosphate or alcohol substrates) cannot be determined from the 386-residue sequence by general biological reasoning alone. Identification requires either database lookup of this exact protein or memorization of the A0A223HDH4 / MPDH_AURME annotation.


**Reason**

> While negative evidence (absence of P450 and radical SAM motifs) provides some reasoning-based elimination of three choices, the positive identification of the specific catalytic reaction (mannitol-1-phosphate oxidation) from a bare amino-acid sequence demands item-specific external knowledge. No general sequence heuristic distinguishes mannitol-1-phosphate 5-dehydrogenase from other NAD-dependent sugar-phosphate dehydrogenases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A and D are P450 reactions, B is a radical SAM reaction; all three are reasonably excluded by absence of their diagnostic motifs. Among the four options, C is the only NAD-dependent dehydrogenase reaction, making it the sole remaining candidate after elimination. No genuine ambiguity among the four choices exists given the sequence.


### Important caveats

- The EC assignment for A0A223HDH4 is by similarity (ECO:0000250 to Q4X1A4), not direct in-vitro characterization of this specific protein; however, a separate PubMed reference (32003433) provides genetic/experimental evidence for the function in the organism.
- The reviewer-only accession was inferred from dataset metadata and was absent from the evaluated model's input.
- The elimination of P450 and radical SAM options by motif absence is a valid but coarse-grained reasoning step; it does not constitute positive identification of the specific substrate.
- The historical entry (v15) was first released in January 2026; the author's construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Partial elimination is possible: the sequence lacks the canonical P450 heme-binding motif (FxxGxxxCxG), arguing against Choices A and D (both cytochrome P450 monooxygenases), and lacks the radical SAM CxxxCxxC motif, arguing against Choice B. A Rossmann-like GxGxxG pattern (GGGNIGRGF) near the N-terminus is consistent with NAD-binding dehydrogenases. However, this only narrows the class to 'NAD-dependent dehydrogenase'—it does not identify the specific substrate as mannitol-1-phosphate rather than glucose-6-phosphate, lactate, sorbitol, or hundreds of other possible substrates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (mannitol-1-phosphate vs. other sugar-phosphate or alcohol substrates) cannot be determined from the 386-residue sequence by general biological reasoning alone. Identification requires either database lookup of this exact protein or memorization of the A0A223HDH4 / MPDH_AURME annotation.",
    "reason": "While negative evidence (absence of P450 and radical SAM motifs) provides some reasoning-based elimination of three choices, the positive identification of the specific catalytic reaction (mannitol-1-phosphate oxidation) from a bare amino-acid sequence demands item-specific external knowledge. No general sequence heuristic distinguishes mannitol-1-phosphate 5-dehydrogenase from other NAD-dependent sugar-phosphate dehydrogenases."
  },
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence (386 AA) matches UniProt entry A0A223HDH4 (MPDH_AURME), which is annotated as Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17). The catalytic activity annotation explicitly states: D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+), matching Choice C verbatim. The EC assignment carries evidence code ECO:0000250 (similarity to Q4X1A4), but the entry also cites PubMed 32003433 for FUNCTION and DISRUPTION PHENOTYPE, providing experimental support for the enzymatic role in Aureobasidium melanogenum. The sequence match is exact (sha256 confirmed) across both current and historical (v15) snapshots."
  },
  "important_caveats": [
    "The EC assignment for A0A223HDH4 is by similarity (ECO:0000250 to Q4X1A4), not direct in-vitro characterization of this specific protein; however, a separate PubMed reference (32003433) provides genetic/experimental evidence for the function in the organism.",
    "The reviewer-only accession was inferred from dataset metadata and was absent from the evaluated model's input.",
    "The elimination of P450 and radical SAM options by motif absence is a valid but coarse-grained reasoning step; it does not constitute positive identification of the specific substrate.",
    "The historical entry (v15) was first released in January 2026; the author's construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and D are P450 reactions, B is a radical SAM reaction; all three are reasonably excluded by absence of their diagnostic motifs. Among the four options, C is the only NAD-dependent dehydrogenase reaction, making it the sole remaining candidate after elimination. No genuine ambiguity among the four choices exists given the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence (386 AA) matches UniProt entry A0A223HDH4 (MPDH_AURME), which is annotated as Mannitol-1-phosphate 5-dehydrogenase (EC 1.1.1.17). The catalytic activity annotation explicitly states: D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+), matching Choice C verbatim. The EC assignment carries evidence code ECO:0000250 (similarity to Q4X1A4), but the entry also cites PubMed 32003433 for FUNCTION and DISRUPTION PHENOTYPE, providing experimental support for the enzymatic role in Aureobasidium melanogenum. The sequence match is exact (sha256 confirmed) across both current and historical (v15) snapshots.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Partial elimination is possible: the sequence lacks the canonical P450 heme-binding motif (FxxGxxxCxG), arguing against Choices A and D (both cytochrome P450 monooxygenases), and lacks the radical SAM CxxxCxxC motif, arguing against Choice B. A Rossmann-like GxGxxG pattern (GGGNIGRGF) near the N-terminus is consistent with NAD-binding dehydrogenases. However, this only narrows the class to 'NAD-dependent dehydrogenase'—it does not identify the specific substrate as mannitol-1-phosphate rather than glucose-6-phosphate, lactate, sorbitol, or hundreds of other possible substrates.",
    "missing_item_specific_fact": "The specific substrate identity (mannitol-1-phosphate vs. other sugar-phosphate or alcohol substrates) cannot be determined from the 386-residue sequence by general biological reasoning alone. Identification requires either database lookup of this exact protein or memorization of the A0A223HDH4 / MPDH_AURME annotation.",
    "reason": "While negative evidence (absence of P450 and radical SAM motifs) provides some reasoning-based elimination of three choices, the positive identification of the specific catalytic reaction (mannitol-1-phosphate oxidation) from a bare amino-acid sequence demands item-specific external knowledge. No general sequence heuristic distinguishes mannitol-1-phosphate 5-dehydrogenase from other NAD-dependent sugar-phosphate dehydrogenases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and D are P450 reactions, B is a radical SAM reaction; all three are reasonably excluded by absence of their diagnostic motifs. Among the four options, C is the only NAD-dependent dehydrogenase reaction, making it the sole remaining candidate after elimination. No genuine ambiguity among the four choices exists given the sequence."
  },
  "important_caveats": [
    "The EC assignment for A0A223HDH4 is by similarity (ECO:0000250 to Q4X1A4), not direct in-vitro characterization of this specific protein; however, a separate PubMed reference (32003433) provides genetic/experimental evidence for the function in the organism.",
    "The reviewer-only accession was inferred from dataset metadata and was absent from the evaluated model's input.",
    "The elimination of P450 and radical SAM options by motif absence is a valid but coarse-grained reasoning step; it does not constitute positive identification of the specific substrate.",
    "The historical entry (v15) was first released in January 2026; the author's construction date is unknown, so the annotation may or may not have been available when the benchmark was assembled."
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

**Accession:** `A0A223HDH4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 15. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
"A0A223HDH4"
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1A4","source":"UniProtKB"}],"value":"1.1.1.17"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Mannitol-1-phosphate 5-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"MPDH"}]}}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.1.1.17","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1A4","source":"UniProtKB"}],"name":"D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19661"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57634"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:61381"}]}}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:43.559987+00:00.  

```json
{"citation":{"authors":["Xue S.J.","Liu G.L.","Chi Z.","Gao Z.C.","Hu Z.","Chi Z.M."],"citationCrossReferences":[{"database":"PubMed","id":"32003433"},{"database":"DOI","id":"10.1042/bcj20190922"}],"citationType":"journal article","firstPage":"887","id":"32003433","journal":"Biochem. J.","lastPage":"903","publicationDate":"2020","title":"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.","volume":"477"},"referenceNumber":4,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
ID   MPDH_AURME              Reviewed;         386 AA.
AC   A0A223HDH4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   25-OCT-2017, sequence version 1.
DT   28-JAN-2026, entry version 15.
DE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};
DE            Short=MPDH {ECO:0000303|PubMed:32003433};
DE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};
OS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.
OX   NCBI_TaxID=46634;
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
DE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};
DE            Short=MPDH {ECO:0000303|PubMed:32003433};
DE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
RN   [4]
RP   FUNCTION, AND DISRUPTION PHENOTYPE.
RX   PubMed=32003433; DOI=10.1042/bcj20190922;
RA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;
RT   "Genetic evidences for the core biosynthesis pathway, regulation, transport
RT   and secretion of liamocins in yeast-like fungal cells.";
RL   Biochem. J. 477:887-903(2020).
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)  
**Locator:** `lines 53-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:24:46.025296+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate
CC         + NADH + H(+); Xref=Rhea:RHEA:19661, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57634, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:61381; EC=1.1.1.17;
CC         Evidence={ECO:0000250|UniProtKB:Q4X1A4};
```

Source SHA-256: `cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 156. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
