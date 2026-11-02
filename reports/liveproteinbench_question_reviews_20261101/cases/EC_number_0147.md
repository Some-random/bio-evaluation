# EC_number_0147

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.2.5

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVKVDLESKRYGEKLKEVFLMLDNNVVECIKEITESSRNGKLVFFVGAGVSTLSDYPQWWRLVDKYHEELYGSPKKGNYSSDEYLRIPQIFYNVKGEMAFDGILKDFFQVDKPTNPIHDKILAMNPAHVITTNYDNLIDTACWKRGKYFSVISAEEDVANATSSRYLLKVHGDFRKGFKGENVVLKEDDYLNYDQNYPLISNLMKTIIATHTIVFIGYGLGDYNINMLLNWVRKLQKDSFHKPFFIRTDPSPIENETLIYYENKGLRIIDAASLIDSNEYDYLERYSAVMDLLIESQENKFITKDDEVIDYIYGKISPLFALQYIRKIDLKHVFEYDYHFEVNGTVVRHKNKGFGYMERFFELKESCDERSKLSKKQYERFNALFNFFEKNGVICMAKDAGTLNTSIEINSLAYHGKYDVMKKFIEEQSVSIEDDYKKAFFLACLGRWEESYDLYSNIILNSIDESNGCVYYLSQINRYRIYQSITQAVTQFNGLGLLTFGRHYKPFTDEFLARIEREMTNFNIDDLFNGMPFEFQKKYKILEFLSDNQFLYDDTVKLFELTNKVRSEMSEGSYSFGMSSDIVVLLRLYDNLRFLYENCLWSVSFHEFHQYIRNSMSLLIEKAEYERTRDIDELGFSFFGKKSGFFMEYYDFVNISRHFKIDDIKNLERSCSIDKIRFGEQEKIEEYLVGIAEEITKQFSANGMNVVFYTQFISEAKAALYFAKYVKLSEEGLGKIVKALLFYFPERDLDIGKRYVWLERLTKCNELPKSIISIIDDFLVLQAEKHIDQNYSEVSSNGLYSRDYGALIKHFEKNFISKRLSEITLCLTQDKQKQIDFLFKLLPLLSTNAKSHLLSFKSVENINDLMNGIRIGLIDEFTPEHEELIIEYLETRKVNYIVEKEKGIQTFSSNDYMSTFGIWYFLEEINNSKMEEFIGMDDQYDFFVDPENFDYKKFIPSWLKNYNDKLLGKIAGNKHMKHHVIEVLKERVKNSNDKRYLEILMNYFI

[Multiple Choices]
A. 3.2.2.5
B. 3.2.2.27
C. 1.11.1.24
D. 5.4.99.14
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

> The supplied sequence exactly matches the 1005-aa UniProtKB P0DXN8 sequence. Its historical UniProt entry assigns EC 3.2.2.5 and gives the reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+), with ECO:0000269 evidence linked to publications. This supports choice A for the matched protein, while the cited evidence has not been independently checked here.

Citations as saved: [H1](#evidence-h1), [H9](#evidence-h9), [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support recognizing a large protein with a sirtuin-like NAD-related enzyme domain, which makes the hydrolase-class option more plausible than the oxidoreductase or isomerase options. But that does not establish the precise EC subclass or this protein's NADase reaction.


**Missing item-specific fact**

> The protein-specific catalytic activity—hydrolysis of NAD(+) to ADP-D-ribose and nicotinamide, assigned EC 3.2.2.5—is not supplied in the question and is needed to distinguish the exact answer.


**Reason**

> The reviewer-only records support the key, but the evaluated input contains only sequence and choices. Inferring the complete EC number requires protein-specific functional knowledge or external annotation; recognizing the sequence or asserting a predictor could identify it would be lookup dependence, not reasoning support.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein's cited catalytic-activity annotation supports A; the other choices describe different EC classes or subclasses and are not supported by the supplied sequence alone.


### Important caveats

- The source accession and annotations are reviewer-only and were absent from the evaluated model input.
- The historical sequence match establishes source applicability, but the author's exact data-source snapshot is unknown.
- The annotation cites experimental evidence codes and publications; those primary studies were not independently retrieved or validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support recognizing a large protein with a sirtuin-like NAD-related enzyme domain, which makes the hydrolase-class option more plausible than the oxidoreductase or isomerase options. But that does not establish the precise EC subclass or this protein's NADase reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—hydrolysis of NAD(+) to ADP-D-ribose and nicotinamide, assigned EC 3.2.2.5—is not supplied in the question and is needed to distinguish the exact answer.",
    "reason": "The reviewer-only records support the key, but the evaluated input contains only sequence and choices. Inferring the complete EC number requires protein-specific functional knowledge or external annotation; recognizing the sequence or asserting a predictor could identify it would be lookup dependence, not reasoning support."
  },
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H9",
      "C1",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1005-aa UniProtKB P0DXN8 sequence. Its historical UniProt entry assigns EC 3.2.2.5 and gives the reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+), with ECO:0000269 evidence linked to publications. This supports choice A for the matched protein, while the cited evidence has not been independently checked here."
  },
  "important_caveats": [
    "The source accession and annotations are reviewer-only and were absent from the evaluated model input.",
    "The historical sequence match establishes source applicability, but the author's exact data-source snapshot is unknown.",
    "The annotation cites experimental evidence codes and publications; those primary studies were not independently retrieved or validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's cited catalytic-activity annotation supports A; the other choices describe different EC classes or subclasses and are not supported by the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 1005-aa UniProtKB P0DXN8 sequence. Its historical UniProt entry assigns EC 3.2.2.5 and gives the reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+), with ECO:0000269 evidence linked to publications. This supports choice A for the matched protein, while the cited evidence has not been independently checked here.",
    "evidence_ids": ["H1", "H9", "C1", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support recognizing a large protein with a sirtuin-like NAD-related enzyme domain, which makes the hydrolase-class option more plausible than the oxidoreductase or isomerase options. But that does not establish the precise EC subclass or this protein's NADase reaction.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—hydrolysis of NAD(+) to ADP-D-ribose and nicotinamide, assigned EC 3.2.2.5—is not supplied in the question and is needed to distinguish the exact answer.",
    "reason": "The reviewer-only records support the key, but the evaluated input contains only sequence and choices. Inferring the complete EC number requires protein-specific functional knowledge or external annotation; recognizing the sequence or asserting a predictor could identify it would be lookup dependence, not reasoning support."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's cited catalytic-activity annotation supports A; the other choices describe different EC classes or subclasses and are not supported by the supplied sequence alone."
  },
  "important_caveats": [
    "The source accession and annotations are reviewer-only and were absent from the evaluated model input.",
    "The historical sequence match establishes source applicability, but the author's exact data-source snapshot is unknown.",
    "The annotation cites experimental evidence codes and publications; those primary studies were not independently retrieved or validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt P0DXN8 (DSR2, Defense-associated sirtuin 2 from Bacillus subtilis) is annotated with EC 3.2.2.5 (NAD(+) glycohydrolase) backed by experimental evidence (ECO:0000269) from six independent PubMed publications (36192536, 38538592, 38555355, 38729958, 39039073, 39059542). The catalytic reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+) is confirmed. The sequence matches the benchmark input exactly (1005 AA, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~1005 AA) contains sirtuin-like catalytic domain features (conserved motifs associated with NAD+ binding and the sirtuin fold). Sirtuins are well-established NAD+-dependent enzymes. Among the four options, EC 1.11.1.24 (oxidoreductase/peroxidase) and EC 5.4.99.14 (isomerase/translocase) belong to entirely different enzyme classes and are incompatible with a sirtuin-like hydrolase. EC 3.2.2.27 does not correspond to a recognized NAD+-related glycosylase. EC 3.2.2.5 (NAD+ glycohydrolase) is the canonical EC number for NAD+ cleavage, the hallmark reaction of sirtuin-family enzymes. A model recognizing sirtuin-like sequence features can eliminate C and D by enzyme class and select A over B by associating the sirtuin fold with NAD+ glycohydrolase activity.


**Missing item-specific fact**

> The specific discovery that DSR2 functions as an NADase (rather than a protein deacetylase) is a 2022 experimental finding. However, since no deacetylase EC number (e.g., EC 3.5.1.-) appears among the options, this distinction does not impede selection of the correct answer from the given choices.


**Reason**

> The reasoning path—recognize sirtuin-like sequence → NAD+-dependent hydrolase → NAD+ glycohydrolase (EC 3.2.2.5)—relies on general knowledge of sirtuin biochemistry and EC classification logic. The distractors C and D are in wholly different enzyme classes, and B is not a recognized NAD+-cleaving glycosylase. This provides meaningful grounds to distinguish the answer without memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> EC 1.11.1.24 (oxidoreductase) and EC 5.4.99.14 (isomerase) are in incompatible enzyme classes for a sirtuin-like protein. EC 3.2.2.27 is not a recognized NAD+-related glycosylase. Only EC 3.2.2.5 aligns with both the sirtuin fold and NAD+ cleavage chemistry.


### Important caveats

- The annotation of DSR2 as EC 3.2.2.5 was established experimentally starting in 2022 (Garb et al., Nat. Microbiol.), so the entry is relatively recent. A model trained on older data might not have this specific association, but the sirtuin→NAD+→EC 3.2.2.5 reasoning path remains valid.
- The distinction between sirtuin NADase activity and sirtuin deacetylase activity is mechanistically specific; however, no deacetylase EC number is offered as a distractor, so this does not create ambiguity in the answer set.
- Sequence-match is confirmed (SHA256 identical), so the evidence applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~1005 AA) contains sirtuin-like catalytic domain features (conserved motifs associated with NAD+ binding and the sirtuin fold). Sirtuins are well-established NAD+-dependent enzymes. Among the four options, EC 1.11.1.24 (oxidoreductase/peroxidase) and EC 5.4.99.14 (isomerase/translocase) belong to entirely different enzyme classes and are incompatible with a sirtuin-like hydrolase. EC 3.2.2.27 does not correspond to a recognized NAD+-related glycosylase. EC 3.2.2.5 (NAD+ glycohydrolase) is the canonical EC number for NAD+ cleavage, the hallmark reaction of sirtuin-family enzymes. A model recognizing sirtuin-like sequence features can eliminate C and D by enzyme class and select A over B by associating the sirtuin fold with NAD+ glycohydrolase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific discovery that DSR2 functions as an NADase (rather than a protein deacetylase) is a 2022 experimental finding. However, since no deacetylase EC number (e.g., EC 3.5.1.-) appears among the options, this distinction does not impede selection of the correct answer from the given choices.",
    "reason": "The reasoning path—recognize sirtuin-like sequence → NAD+-dependent hydrolase → NAD+ glycohydrolase (EC 3.2.2.5)—relies on general knowledge of sirtuin biochemistry and EC classification logic. The distractors C and D are in wholly different enzyme classes, and B is not a recognized NAD+-cleaving glycosylase. This provides meaningful grounds to distinguish the answer without memorizing this specific protein's database entry."
  },
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H9"
    ],
    "judgment": "supported",
    "reason": "UniProt P0DXN8 (DSR2, Defense-associated sirtuin 2 from Bacillus subtilis) is annotated with EC 3.2.2.5 (NAD(+) glycohydrolase) backed by experimental evidence (ECO:0000269) from six independent PubMed publications (36192536, 38538592, 38555355, 38729958, 39039073, 39059542). The catalytic reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+) is confirmed. The sequence matches the benchmark input exactly (1005 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The annotation of DSR2 as EC 3.2.2.5 was established experimentally starting in 2022 (Garb et al., Nat. Microbiol.), so the entry is relatively recent. A model trained on older data might not have this specific association, but the sirtuin→NAD+→EC 3.2.2.5 reasoning path remains valid.",
    "The distinction between sirtuin NADase activity and sirtuin deacetylase activity is mechanistically specific; however, no deacetylase EC number is offered as a distractor, so this does not create ambiguity in the answer set.",
    "Sequence-match is confirmed (SHA256 identical), so the evidence applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 1.11.1.24 (oxidoreductase) and EC 5.4.99.14 (isomerase) are in incompatible enzyme classes for a sirtuin-like protein. EC 3.2.2.27 is not a recognized NAD+-related glycosylase. Only EC 3.2.2.5 aligns with both the sirtuin fold and NAD+ cleavage chemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0147",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt P0DXN8 (DSR2, Defense-associated sirtuin 2 from Bacillus subtilis) is annotated with EC 3.2.2.5 (NAD(+) glycohydrolase) backed by experimental evidence (ECO:0000269) from six independent PubMed publications (36192536, 38538592, 38555355, 38729958, 39039073, 39059542). The catalytic reaction NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+) is confirmed. The sequence matches the benchmark input exactly (1005 AA, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "H2", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~1005 AA) contains sirtuin-like catalytic domain features (conserved motifs associated with NAD+ binding and the sirtuin fold). Sirtuins are well-established NAD+-dependent enzymes. Among the four options, EC 1.11.1.24 (oxidoreductase/peroxidase) and EC 5.4.99.14 (isomerase/translocase) belong to entirely different enzyme classes and are incompatible with a sirtuin-like hydrolase. EC 3.2.2.27 does not correspond to a recognized NAD+-related glycosylase. EC 3.2.2.5 (NAD+ glycohydrolase) is the canonical EC number for NAD+ cleavage, the hallmark reaction of sirtuin-family enzymes. A model recognizing sirtuin-like sequence features can eliminate C and D by enzyme class and select A over B by associating the sirtuin fold with NAD+ glycohydrolase activity.",
    "missing_item_specific_fact": "The specific discovery that DSR2 functions as an NADase (rather than a protein deacetylase) is a 2022 experimental finding. However, since no deacetylase EC number (e.g., EC 3.5.1.-) appears among the options, this distinction does not impede selection of the correct answer from the given choices.",
    "reason": "The reasoning path—recognize sirtuin-like sequence → NAD+-dependent hydrolase → NAD+ glycohydrolase (EC 3.2.2.5)—relies on general knowledge of sirtuin biochemistry and EC classification logic. The distractors C and D are in wholly different enzyme classes, and B is not a recognized NAD+-cleaving glycosylase. This provides meaningful grounds to distinguish the answer without memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 1.11.1.24 (oxidoreductase) and EC 5.4.99.14 (isomerase) are in incompatible enzyme classes for a sirtuin-like protein. EC 3.2.2.27 is not a recognized NAD+-related glycosylase. Only EC 3.2.2.5 aligns with both the sirtuin fold and NAD+ cleavage chemistry."
  },
  "important_caveats": [
    "The annotation of DSR2 as EC 3.2.2.5 was established experimentally starting in 2022 (Garb et al., Nat. Microbiol.), so the entry is relatively recent. A model trained on older data might not have this specific association, but the sirtuin→NAD+→EC 3.2.2.5 reasoning path remains valid.",
    "The distinction between sirtuin NADase activity and sirtuin deacetylase activity is mechanistically specific; however, no deacetylase EC number is offered as a distractor, so this does not create ambiguity in the answer set.",
    "Sequence-match is confirmed (SHA256 identical), so the evidence applies directly to the supplied sequence."
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

**Accession:** `P0DXN8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:34.653615+00:00.  

```json
"P0DXN8"
```

Source SHA-256: `3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:34.653615+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36192536","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38538592","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38555355","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38729958","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39039073","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39059542","source":"PubMed"}],"value":"3.2.2.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36192536","source":"PubMed"}],"value":"Defense-associated sirtuin 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36192536","source":"PubMed"}],"value":"DSR2"}]}}
```

Source SHA-256: `3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXN8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:34.653615+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36192536","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38538592","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38555355","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38729958","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39039073","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39059542","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:16302"}}],"reaction":{"ecNumber":"3.2.2.5","evidences":[{"evidenceCode":"ECO:0000269","id":"36192536","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38538592","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38555355","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38729958","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39039073","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39059542","source":"PubMed"}],"name":"NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:16301"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17154"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57967"}]}}
```

Source SHA-256: `3c07906d055c6870519730595577eb2c2e5fa9c182dccdb9715a585974ad83cf`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:41.291631+00:00.  

```text
ID   DSR2_BACIU              Reviewed;        1005 AA.
AC   P0DXN8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Defense-associated sirtuin 2 {ECO:0000303|PubMed:36192536};
DE            Short=DSR2 {ECO:0000303|PubMed:36192536};
DE            EC=3.2.2.5 {ECO:0000269|PubMed:36192536, ECO:0000269|PubMed:38538592, ECO:0000269|PubMed:38555355, ECO:0000269|PubMed:38729958, ECO:0000269|PubMed:39039073, ECO:0000269|PubMed:39059542};
GN   ORFNames=BKP58_08510;
OS   Bacillus subtilis.
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus.
OX   NCBI_TaxID=1423;
```

Source SHA-256: `10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:41.291631+00:00.  

```text
DE   RecName: Full=Defense-associated sirtuin 2 {ECO:0000303|PubMed:36192536};
DE            Short=DSR2 {ECO:0000303|PubMed:36192536};
DE            EC=3.2.2.5 {ECO:0000269|PubMed:36192536, ECO:0000269|PubMed:38538592, ECO:0000269|PubMed:38555355, ECO:0000269|PubMed:38729958, ECO:0000269|PubMed:39039073, ECO:0000269|PubMed:39059542};
```

Source SHA-256: `10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXN8?format=txt&versions=4)  
**Locator:** `lines 119-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:41.291631+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=NAD(+) + H2O = ADP-D-ribose + nicotinamide + H(+);
CC         Xref=Rhea:RHEA:16301, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:17154, ChEBI:CHEBI:57540, ChEBI:CHEBI:57967; EC=3.2.2.5;
CC         Evidence={ECO:0000269|PubMed:36192536, ECO:0000269|PubMed:38538592,
CC         ECO:0000269|PubMed:38555355, ECO:0000269|PubMed:38729958,
CC         ECO:0000269|PubMed:39039073, ECO:0000269|PubMed:39059542};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16302;
CC         Evidence={ECO:0000269|PubMed:36192536, ECO:0000269|PubMed:38538592,
CC         ECO:0000269|PubMed:38555355, ECO:0000269|PubMed:38729958,
CC         ECO:0000269|PubMed:39039073, ECO:0000269|PubMed:39059542};
```

Source SHA-256: `10090b1b85e4938487d7ee1b0a9f6e082df0be587b4db02b25ff121b2c41b87e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 147. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
