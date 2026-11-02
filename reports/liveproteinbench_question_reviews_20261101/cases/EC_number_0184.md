# EC_number_0184

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 3.2.1.31

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLFPKDTLTREIKDLSGIWRFKADPDNRGREEKWHHQPLQDTIPMPVPASYNDITQDAALRDHIGDVWYEQTFIVPRSWSGDRMMLWIGSACHHAVVWVNGVEVASHKGGFLPFEADITRVAVPGRENRVTIVVNNVLNWQTLPPGRIKTFDDEKHPEGYRVQEYFHDFFNYAGLHRPVKLYRTSGLFIQDITITTDVQGESGVVGYSIECSQPEGEVRVKLLDEDGKEAATGKGSSGTLQVENARLWKPLQAYLYTLHVELLDSYGQLADHYQLQVGIRTVKVEGTRFLINGERFYFKGFGKHEDSDIRGKGLDQAVNVKDFNLLKWINANSFRTSHYPYAEELLELADREGIVVIGEVPAVGFTFFNYNDKVYTPDQANEETLAHHHDVLSDLIARDKNHPSVVMWSLANEAATFQDEAVPYFRQLADTARRLDPQRPITIVQWPLPDKCKVAQFFDVICVNRYYSWYQDPGALELVEHQVEWELTNWYRNFGKPVIMTEYGADAIAGFHQDPPVMFTEEYQEELLTRYHNVFDRLDFVIGEHVWAFADFATKQGITRINGNKKGVFTRQRQPKAAARMLRSRWGEMGEYPEKL

[Multiple Choices]
A. 3.2.1.8
B. 6.3.2.35
C. 3.2.1.31
D. 1.14.15.9
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the UniProt entry annotated as beta-glucuronidase, EC 3.2.1.31. The catalytic-activity annotation assigns this reaction with experimental evidence code ECO:0000269 citing PubMed 35947916; the matching historical entry also carries that annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a reliable, specific basis for distinguishing beta-glucuronidase activity from the other listed enzyme activities. Identifying a likely enzyme family would not by itself establish the precise substrate specificity required for this EC number.


**Missing item-specific fact**

> The protein-specific catalytic activity—hydrolysis of beta-D-glucuronosides to D-glucuronate and an alcohol—established by experimental characterization or a specific external annotation.


**Reason**

> The decisive substrate-specific activity is not supplied in the question. The reviewer-only matched-sequence annotation supports the key, but it was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports C; it does not support another listed option for this matched protein.


### Important caveats

- The UniProt annotation cites experimental evidence, but the primary paper was not independently retrieved or validated here.
- The author’s exact source snapshot is unknown; the supplied evidence includes a sequence-matched historical entry as well as a current entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a reliable, specific basis for distinguishing beta-glucuronidase activity from the other listed enzyme activities. Identifying a likely enzyme family would not by itself establish the precise substrate specificity required for this EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—hydrolysis of beta-D-glucuronosides to D-glucuronate and an alcohol—established by experimental characterization or a specific external annotation.",
    "reason": "The decisive substrate-specific activity is not supplied in the question. The reviewer-only matched-sequence annotation supports the key, but it was not available to the evaluated model."
  },
  "case_id": "EC_number_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as beta-glucuronidase, EC 3.2.1.31. The catalytic-activity annotation assigns this reaction with experimental evidence code ECO:0000269 citing PubMed 35947916; the matching historical entry also carries that annotation."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently retrieved or validated here.",
    "The author’s exact source snapshot is unknown; the supplied evidence includes a sequence-matched historical entry as well as a current entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C; it does not support another listed option for this matched protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as beta-glucuronidase, EC 3.2.1.31. The catalytic-activity annotation assigns this reaction with experimental evidence code ECO:0000269 citing PubMed 35947916; the matching historical entry also carries that annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a reliable, specific basis for distinguishing beta-glucuronidase activity from the other listed enzyme activities. Identifying a likely enzyme family would not by itself establish the precise substrate specificity required for this EC number.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—hydrolysis of beta-D-glucuronosides to D-glucuronate and an alcohol—established by experimental characterization or a specific external annotation.",
    "reason": "The decisive substrate-specific activity is not supplied in the question. The reviewer-only matched-sequence annotation supports the key, but it was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C; it does not support another listed option for this matched protein."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently retrieved or validated here.",
    "The author’s exact source snapshot is unknown; the supplied evidence includes a sequence-matched historical entry as well as a current entry."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A089LCJ8 (Paenibacillus borealis, 596 AA, sequence match confirmed) annotates this protein as Beta-glucuronidase with EC 3.2.1.31, supported by experimental evidence (ECO:0000269, PubMed:35947916). The catalytic activity is explicitly stated as 'a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol' (Rhea:RHEA:17633). Note: the primary publication (Isono et al. 2022) characterizes a GH94 glycoside phosphorylase, yet UniProt assigns the hydrolase EC 3.2.1.31 with direct-assay evidence, suggesting the enzyme also exhibits hydrolytic activity or the annotation reflects a separate characterization. The sequence matches exactly in both current and archived (v41) records.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices span three EC classes (hydrolases 3.2.1.x, ligase 6.3.2.x, oxidoreductase 1.14.15.x), so general reasoning can eliminate B (ligase) and D (copper monooxygenase) as implausible for a ~600-residue bacterial protein lacking copper-binding motifs or ligase architecture. However, distinguishing 3.2.1.8 (endo-1,4-beta-xylanase, GH10/GH11) from 3.2.1.31 (beta-glucuronidase, GH2) from sequence alone requires recognition of family-specific catalytic motifs (e.g., GH2 'NEP' motif, specific Glu catalytic residues) and substrate-binding pocket architecture that are not provided in the question context. The annotation itself is somewhat counterintuitive given the source paper describes a GH94 phosphorylase, further complicating reasoning-based prediction.


**Missing item-specific fact**

> The specific GH-family assignment (GH2 vs GH10/11 vs GH94) and the experimentally demonstrated hydrolase activity of this particular Paenibacillus borealis enzyme (PubMed:35947916) are not derivable from the bare sequence without either recognizing the exact protein or possessing detailed family-level catalytic-motif knowledge.


**Reason**

> While the broad enzyme class (glycoside hydrolase) is inferable from general sequence features, the precise 4-digit EC number (3.2.1.8 vs 3.2.1.31) depends on item-specific annotation or memorization of the protein's experimental characterization. The GH94-vs-GH2 discrepancy in the literature makes even expert reasoning unreliable without the specific experimental result.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both 3.2.1.8 (xylanase) and 3.2.1.31 (beta-glucuronidase) are glycoside hydrolases acting on beta-linked sugar polymers. Without explicit family-level motif information or the experimental substrate-specificity data, a knowledgeable model could plausibly argue for either GH family based on partial sequence homology. The distractors B and D are clearly eliminable, but A vs C is genuinely ambiguous from sequence alone.


### Important caveats

- The primary publication (PubMed:35947916) characterizes a GH94 glycoside phosphorylase, yet UniProt assigns EC 3.2.1.31 (a GH2-type hydrolase). This apparent family/activity discrepancy means even a model familiar with GH94 phosphorylases might not predict EC 3.2.1.31.
- The evidence code ECO:0000269 (inferred from direct assay) indicates experimental support, but the reviewer did not independently validate the primary paper's full experimental design.
- The UniProt entry was first publicly released in April 2025; the author's data-construction snapshot is unknown, so the annotation may or may not have been available at question creation time.
- Sequence match is confirmed (SHA-256 identical across current and archived v41 records), so the annotation applies to the exact benchmark sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices span three EC classes (hydrolases 3.2.1.x, ligase 6.3.2.x, oxidoreductase 1.14.15.x), so general reasoning can eliminate B (ligase) and D (copper monooxygenase) as implausible for a ~600-residue bacterial protein lacking copper-binding motifs or ligase architecture. However, distinguishing 3.2.1.8 (endo-1,4-beta-xylanase, GH10/GH11) from 3.2.1.31 (beta-glucuronidase, GH2) from sequence alone requires recognition of family-specific catalytic motifs (e.g., GH2 'NEP' motif, specific Glu catalytic residues) and substrate-binding pocket architecture that are not provided in the question context. The annotation itself is somewhat counterintuitive given the source paper describes a GH94 phosphorylase, further complicating reasoning-based prediction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific GH-family assignment (GH2 vs GH10/11 vs GH94) and the experimentally demonstrated hydrolase activity of this particular Paenibacillus borealis enzyme (PubMed:35947916) are not derivable from the bare sequence without either recognizing the exact protein or possessing detailed family-level catalytic-motif knowledge.",
    "reason": "While the broad enzyme class (glycoside hydrolase) is inferable from general sequence features, the precise 4-digit EC number (3.2.1.8 vs 3.2.1.31) depends on item-specific annotation or memorization of the protein's experimental characterization. The GH94-vs-GH2 discrepancy in the literature makes even expert reasoning unreliable without the specific experimental result."
  },
  "case_id": "EC_number_0184",
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
    "reason": "The UniProt entry A0A089LCJ8 (Paenibacillus borealis, 596 AA, sequence match confirmed) annotates this protein as Beta-glucuronidase with EC 3.2.1.31, supported by experimental evidence (ECO:0000269, PubMed:35947916). The catalytic activity is explicitly stated as 'a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol' (Rhea:RHEA:17633). Note: the primary publication (Isono et al. 2022) characterizes a GH94 glycoside phosphorylase, yet UniProt assigns the hydrolase EC 3.2.1.31 with direct-assay evidence, suggesting the enzyme also exhibits hydrolytic activity or the annotation reflects a separate characterization. The sequence matches exactly in both current and archived (v41) records."
  },
  "important_caveats": [
    "The primary publication (PubMed:35947916) characterizes a GH94 glycoside phosphorylase, yet UniProt assigns EC 3.2.1.31 (a GH2-type hydrolase). This apparent family/activity discrepancy means even a model familiar with GH94 phosphorylases might not predict EC 3.2.1.31.",
    "The evidence code ECO:0000269 (inferred from direct assay) indicates experimental support, but the reviewer did not independently validate the primary paper's full experimental design.",
    "The UniProt entry was first publicly released in April 2025; the author's data-construction snapshot is unknown, so the annotation may or may not have been available at question creation time.",
    "Sequence match is confirmed (SHA-256 identical across current and archived v41 records), so the annotation applies to the exact benchmark sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both 3.2.1.8 (xylanase) and 3.2.1.31 (beta-glucuronidase) are glycoside hydrolases acting on beta-linked sugar polymers. Without explicit family-level motif information or the experimental substrate-specificity data, a knowledgeable model could plausibly argue for either GH family based on partial sequence homology. The distractors B and D are clearly eliminable, but A vs C is genuinely ambiguous from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A089LCJ8 (Paenibacillus borealis, 596 AA, sequence match confirmed) annotates this protein as Beta-glucuronidase with EC 3.2.1.31, supported by experimental evidence (ECO:0000269, PubMed:35947916). The catalytic activity is explicitly stated as 'a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol' (Rhea:RHEA:17633). Note: the primary publication (Isono et al. 2022) characterizes a GH94 glycoside phosphorylase, yet UniProt assigns the hydrolase EC 3.2.1.31 with direct-assay evidence, suggesting the enzyme also exhibits hydrolytic activity or the annotation reflects a separate characterization. The sequence matches exactly in both current and archived (v41) records.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices span three EC classes (hydrolases 3.2.1.x, ligase 6.3.2.x, oxidoreductase 1.14.15.x), so general reasoning can eliminate B (ligase) and D (copper monooxygenase) as implausible for a ~600-residue bacterial protein lacking copper-binding motifs or ligase architecture. However, distinguishing 3.2.1.8 (endo-1,4-beta-xylanase, GH10/GH11) from 3.2.1.31 (beta-glucuronidase, GH2) from sequence alone requires recognition of family-specific catalytic motifs (e.g., GH2 'NEP' motif, specific Glu catalytic residues) and substrate-binding pocket architecture that are not provided in the question context. The annotation itself is somewhat counterintuitive given the source paper describes a GH94 phosphorylase, further complicating reasoning-based prediction.",
    "missing_item_specific_fact": "The specific GH-family assignment (GH2 vs GH10/11 vs GH94) and the experimentally demonstrated hydrolase activity of this particular Paenibacillus borealis enzyme (PubMed:35947916) are not derivable from the bare sequence without either recognizing the exact protein or possessing detailed family-level catalytic-motif knowledge.",
    "reason": "While the broad enzyme class (glycoside hydrolase) is inferable from general sequence features, the precise 4-digit EC number (3.2.1.8 vs 3.2.1.31) depends on item-specific annotation or memorization of the protein's experimental characterization. The GH94-vs-GH2 discrepancy in the literature makes even expert reasoning unreliable without the specific experimental result."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both 3.2.1.8 (xylanase) and 3.2.1.31 (beta-glucuronidase) are glycoside hydrolases acting on beta-linked sugar polymers. Without explicit family-level motif information or the experimental substrate-specificity data, a knowledgeable model could plausibly argue for either GH family based on partial sequence homology. The distractors B and D are clearly eliminable, but A vs C is genuinely ambiguous from sequence alone."
  },
  "important_caveats": [
    "The primary publication (PubMed:35947916) characterizes a GH94 glycoside phosphorylase, yet UniProt assigns EC 3.2.1.31 (a GH2-type hydrolase). This apparent family/activity discrepancy means even a model familiar with GH94 phosphorylases might not predict EC 3.2.1.31.",
    "The evidence code ECO:0000269 (inferred from direct assay) indicates experimental support, but the reviewer did not independently validate the primary paper's full experimental design.",
    "The UniProt entry was first publicly released in April 2025; the author's data-construction snapshot is unknown, so the annotation may or may not have been available at question creation time.",
    "Sequence match is confirmed (SHA-256 identical across current and archived v41 records), so the annotation applies to the exact benchmark sequence."
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

**Accession:** `A0A089LCJ8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 41. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.179702+00:00.  

```json
"A0A089LCJ8"
```

Source SHA-256: `f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.179702+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"value":"3.2.1.31"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35947916","source":"PubMed"}],"value":"Beta-glucuronidase"}}}
```

Source SHA-256: `f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.179702+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.31","evidences":[{"evidenceCode":"ECO:0000269","id":"35947916","source":"PubMed"}],"name":"a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17633"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30879"},{"database":"ChEBI","id":"CHEBI:58720"},{"database":"ChEBI","id":"CHEBI:83411"}]}}
```

Source SHA-256: `f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:37.179702+00:00.  

```json
{"citation":{"authors":["Isono N.","Mizutani E.","Hayashida H.","Katsuzaki H.","Saburi W."],"citationCrossReferences":[{"database":"PubMed","id":"35947916"},{"database":"DOI","id":"10.1016/j.bbrc.2022.07.098"}],"citationType":"journal article","firstPage":"60","id":"35947916","journal":"Biochem. Biophys. Res. Commun.","lastPage":"65","publicationDate":"2022","title":"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.","volume":"625"},"referenceComments":[{"type":"STRAIN","value":"DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:15.466546+00:00.  

```text
ID   BGLR_PAEBO              Reviewed;         596 AA.
AC   A0A089LCJ8;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-NOV-2014, sequence version 1.
DT   28-JAN-2026, entry version 41.
DE   RecName: Full=Beta-glucuronidase {ECO:0000303|PubMed:35947916};
DE            EC=3.2.1.31 {ECO:0000269|PubMed:35947916};
GN   ORFNames=PBOR_13360 {ECO:0000312|EMBL:AIQ57810.1};
OS   Paenibacillus borealis.
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Paenibacillaceae;
OC   Paenibacillus.
OX   NCBI_TaxID=160799;
```

Source SHA-256: `7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:15.466546+00:00.  

```text
DE   RecName: Full=Beta-glucuronidase {ECO:0000303|PubMed:35947916};
DE            EC=3.2.1.31 {ECO:0000269|PubMed:35947916};
```

Source SHA-256: `7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)  
**Locator:** `lines 19-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:15.466546+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.
RC   STRAIN=DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19;
RX   PubMed=35947916; DOI=10.1016/j.bbrc.2022.07.098;
RA   Isono N., Mizutani E., Hayashida H., Katsuzaki H., Saburi W.;
RT   "Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-
RT   beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of
RT   the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.";
RL   Biochem. Biophys. Res. Commun. 625:60-65(2022).
```

Source SHA-256: `7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)  
**Locator:** `lines 34-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:15.466546+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol;
CC         Xref=Rhea:RHEA:17633, ChEBI:CHEBI:15377, ChEBI:CHEBI:30879,
CC         ChEBI:CHEBI:58720, ChEBI:CHEBI:83411; EC=3.2.1.31;
CC         Evidence={ECO:0000269|PubMed:35947916};
```

Source SHA-256: `7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
