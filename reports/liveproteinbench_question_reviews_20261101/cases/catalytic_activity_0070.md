# catalytic_activity_0070

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. 3 malonyl-CoA + acetyl-CoA + 2 S-adenosyl-L-methionine = 3,5-dimethylorsellinate + 2 S-adenosyl-L-homocysteine + 3 CO2 + 4 CoA
B. 2-hydroxyspirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
C. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
D. a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA
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

> The exact sequence matches the annotated Aspergillus terreus protein, whose catalytic-activity record gives the reaction in choice C with ECO:0000269 evidence. The archived entry available by the historical cutoff records the same reaction.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a long soluble enzyme and does not, from general biochemical principles alone, establish which precise reaction among these choices it catalyzes.


**Missing item-specific fact**

> The protein-specific functional assignment as dihydroxy-acid dehydratase, or equivalent sequence-homology/functional annotation, is needed to select the reaction in C.


**Reason**

> The reviewer-only annotation supports the key, but was not provided to the evaluated model. Inferring the particular catalytic reaction would require protein-specific identification rather than a sufficiently discriminating argument from the input alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported annotation matches choice C; the other options describe different reactions.


### Important caveats

- The evidence is a database annotation carrying experimental evidence code ECO:0000269 and a PubMed citation; the primary paper was not independently reviewed here.
- The exact sequence matches both the current and historical database records, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long soluble enzyme and does not, from general biochemical principles alone, establish which precise reaction among these choices it catalyzes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment as dihydroxy-acid dehydratase, or equivalent sequence-homology/functional annotation, is needed to select the reaction in C.",
    "reason": "The reviewer-only annotation supports the key, but was not provided to the evaluated model. Inferring the particular catalytic reaction would require protein-specific identification rather than a sufficiently discriminating argument from the input alone."
  },
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Aspergillus terreus protein, whose catalytic-activity record gives the reaction in choice C with ECO:0000269 evidence. The archived entry available by the historical cutoff records the same reaction."
  },
  "important_caveats": [
    "The evidence is a database annotation carrying experimental evidence code ECO:0000269 and a PubMed citation; the primary paper was not independently reviewed here.",
    "The exact sequence matches both the current and historical database records, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported annotation matches choice C; the other options describe different reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Aspergillus terreus protein, whose catalytic-activity record gives the reaction in choice C with ECO:0000269 evidence. The archived entry available by the historical cutoff records the same reaction.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a long soluble enzyme and does not, from general biochemical principles alone, establish which precise reaction among these choices it catalyzes.",
    "missing_item_specific_fact": "The protein-specific functional assignment as dihydroxy-acid dehydratase, or equivalent sequence-homology/functional annotation, is needed to select the reaction in C.",
    "reason": "The reviewer-only annotation supports the key, but was not provided to the evaluated model. Inferring the particular catalytic reaction would require protein-specific identification rather than a sufficiently discriminating argument from the input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported annotation matches choice C; the other options describe different reactions."
  },
  "important_caveats": [
    "The evidence is a database annotation carrying experimental evidence code ECO:0000269 and a PubMed citation; the primary paper was not independently reviewed here.",
    "The exact sequence matches both the current and historical database records, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 598-aa sequence matches UniProt entry Q0CPG9 (ASTD_ASPTN, Aspergillus terreus) exactly (SHA256 confirmed). The UniProt annotation lists EC 4.2.1.9 (dihydroxy-acid dehydratase astD) with the catalytic reaction '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O', supported by experimental evidence (ECO:0000269, PubMed:29995859, Nature 2018). This matches Choice C verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~598 aa) exhibits the two-domain architecture characteristic of the ILV3/DHAD enzyme family, with a C-terminal domain containing cysteine residues in a pattern consistent with 4Fe-4S cluster coordination (a hallmark of DHAD enzymes). Among the four choices, only DHAD (Choice C) requires a 4Fe-4S cluster. Choice A (polyketide synthase) would require acyltransferase, ketosynthase, and ACP domains absent here. Choice B (carotenoid hydroxylase) would require di-iron or Rieske-type motifs and membrane association. Choice D (enoyl-CoA isomerase) is typically a small (~200–300 aa) protein without metal clusters. The combination of the 4Fe-4S cluster-binding cysteine pattern, the ~600-aa two-domain architecture, and the absence of PKS/carotenoid-hydroxylase/isomerase signatures provides a concrete biological argument favoring DHAD.


**Missing item-specific fact**

> None strictly required; however, recognizing the DHAD-specific 4Fe-4S cluster motif (CX2CX2C) in a fungal DHAD sequence requires specialized enzyme-family knowledge beyond generic sequence heuristics.


**Reason**

> The 4Fe-4S cluster coordination motif and the overall two-domain DHAD architecture are general, teachable features of the ILV3 enzyme family. A knowledgeable reader can eliminate the other three choices by noting the absence of PKS catalytic domains, carotenoid-hydroxylase di-iron motifs, and the atypical size for an enoyl-CoA isomerase. This constitutes a concrete biological reasoning path, though it demands specialized enzyme-family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor corresponds to a structurally and mechanistically distinct enzyme class (PKS, carotenoid hydroxylase, DHAD, enoyl-CoA isomerase). The 4Fe-4S cluster motif and two-domain architecture uniquely point to DHAD among the four choices. No other option is defensible given the sequence features.


### Important caveats

- The 4Fe-4S cluster CX2CX2C motif is not trivially identifiable by a naive pattern scan in this fungal DHAD sequence; expert recognition of the DHAD C-terminal domain architecture is needed.
- The experimental evidence (ECO:0000269, Nature 2018) confirms the DHAD activity, but the annotation also lists a second, broader-specificity reaction (C6) with only similarity-based evidence (ECO:0000250); this does not affect the correctness of Choice C.
- The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the reasoning assessment is based solely on what a model could extract from the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~598 aa) exhibits the two-domain architecture characteristic of the ILV3/DHAD enzyme family, with a C-terminal domain containing cysteine residues in a pattern consistent with 4Fe-4S cluster coordination (a hallmark of DHAD enzymes). Among the four choices, only DHAD (Choice C) requires a 4Fe-4S cluster. Choice A (polyketide synthase) would require acyltransferase, ketosynthase, and ACP domains absent here. Choice B (carotenoid hydroxylase) would require di-iron or Rieske-type motifs and membrane association. Choice D (enoyl-CoA isomerase) is typically a small (~200–300 aa) protein without metal clusters. The combination of the 4Fe-4S cluster-binding cysteine pattern, the ~600-aa two-domain architecture, and the absence of PKS/carotenoid-hydroxylase/isomerase signatures provides a concrete biological argument favoring DHAD.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, recognizing the DHAD-specific 4Fe-4S cluster motif (CX2CX2C) in a fungal DHAD sequence requires specialized enzyme-family knowledge beyond generic sequence heuristics.",
    "reason": "The 4Fe-4S cluster coordination motif and the overall two-domain DHAD architecture are general, teachable features of the ILV3 enzyme family. A knowledgeable reader can eliminate the other three choices by noting the absence of PKS catalytic domains, carotenoid-hydroxylase di-iron motifs, and the atypical size for an enoyl-CoA isomerase. This constitutes a concrete biological reasoning path, though it demands specialized enzyme-family knowledge."
  },
  "case_id": "catalytic_activity_0070",
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
    "reason": "The supplied 598-aa sequence matches UniProt entry Q0CPG9 (ASTD_ASPTN, Aspergillus terreus) exactly (SHA256 confirmed). The UniProt annotation lists EC 4.2.1.9 (dihydroxy-acid dehydratase astD) with the catalytic reaction '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O', supported by experimental evidence (ECO:0000269, PubMed:29995859, Nature 2018). This matches Choice C verbatim."
  },
  "important_caveats": [
    "The 4Fe-4S cluster CX2CX2C motif is not trivially identifiable by a naive pattern scan in this fungal DHAD sequence; expert recognition of the DHAD C-terminal domain architecture is needed.",
    "The experimental evidence (ECO:0000269, Nature 2018) confirms the DHAD activity, but the annotation also lists a second, broader-specificity reaction (C6) with only similarity-based evidence (ECO:0000250); this does not affect the correctness of Choice C.",
    "The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the reasoning assessment is based solely on what a model could extract from the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor corresponds to a structurally and mechanistically distinct enzyme class (PKS, carotenoid hydroxylase, DHAD, enoyl-CoA isomerase). The 4Fe-4S cluster motif and two-domain architecture uniquely point to DHAD among the four choices. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 598-aa sequence matches UniProt entry Q0CPG9 (ASTD_ASPTN, Aspergillus terreus) exactly (SHA256 confirmed). The UniProt annotation lists EC 4.2.1.9 (dihydroxy-acid dehydratase astD) with the catalytic reaction '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O', supported by experimental evidence (ECO:0000269, PubMed:29995859, Nature 2018). This matches Choice C verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~598 aa) exhibits the two-domain architecture characteristic of the ILV3/DHAD enzyme family, with a C-terminal domain containing cysteine residues in a pattern consistent with 4Fe-4S cluster coordination (a hallmark of DHAD enzymes). Among the four choices, only DHAD (Choice C) requires a 4Fe-4S cluster. Choice A (polyketide synthase) would require acyltransferase, ketosynthase, and ACP domains absent here. Choice B (carotenoid hydroxylase) would require di-iron or Rieske-type motifs and membrane association. Choice D (enoyl-CoA isomerase) is typically a small (~200–300 aa) protein without metal clusters. The combination of the 4Fe-4S cluster-binding cysteine pattern, the ~600-aa two-domain architecture, and the absence of PKS/carotenoid-hydroxylase/isomerase signatures provides a concrete biological argument favoring DHAD.",
    "missing_item_specific_fact": "None strictly required; however, recognizing the DHAD-specific 4Fe-4S cluster motif (CX2CX2C) in a fungal DHAD sequence requires specialized enzyme-family knowledge beyond generic sequence heuristics.",
    "reason": "The 4Fe-4S cluster coordination motif and the overall two-domain DHAD architecture are general, teachable features of the ILV3 enzyme family. A knowledgeable reader can eliminate the other three choices by noting the absence of PKS catalytic domains, carotenoid-hydroxylase di-iron motifs, and the atypical size for an enoyl-CoA isomerase. This constitutes a concrete biological reasoning path, though it demands specialized enzyme-family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor corresponds to a structurally and mechanistically distinct enzyme class (PKS, carotenoid hydroxylase, DHAD, enoyl-CoA isomerase). The 4Fe-4S cluster motif and two-domain architecture uniquely point to DHAD among the four choices. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The 4Fe-4S cluster CX2CX2C motif is not trivially identifiable by a naive pattern scan in this fungal DHAD sequence; expert recognition of the DHAD C-terminal domain architecture is needed.",
    "The experimental evidence (ECO:0000269, Nature 2018) confirms the DHAD activity, but the annotation also lists a second, broader-specificity reaction (C6) with only similarity-based evidence (ECO:0000250); this does not affect the correctness of Choice C.",
    "The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the reasoning assessment is based solely on what a model could extract from the raw sequence."
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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24810"}}],"reaction":{"ecNumber":"4.2.1.9","evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"name":"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24809"},{"database":"ChEBI","id":"CHEBI:11851"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:49072"}]}}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P05791","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:27695"}}],"reaction":{"ecNumber":"4.2.1.9","evidences":[{"evidenceCode":"ECO:0000250","id":"P05791","source":"UniProtKB"}],"name":"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:27694"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:35146"},{"database":"ChEBI","id":"CHEBI:49258"}]}}
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

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
DE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};
DE            Short=DHAD astD {ECO:0000303|PubMed:29995859};
DE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};
DE   Flags: Precursor;
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 52-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate
CC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:49072; EC=4.2.1.9;
CC         Evidence={ECO:0000269|PubMed:29995859};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;
CC         Evidence={ECO:0000269|PubMed:29995859};
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
