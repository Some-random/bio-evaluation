# catalytic_activity_0196

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
METVESSSSAELLRAQTHFSRQVFSFQNFAALKCALQLGIPDAIKQHGKPMNLSELTSALPINPSKAPCIHRLMRLLVNAGYFAQENECFALTSLGRLLLKDDPLHIRALVLSEFHTALVMPWFALSEWFKNDDVAPFATAHGKSFWDYTSCDPELRNVFDGAMACDSHLIAKALVTEFKYLFEGLKSLVDVGGGNGTLARSIAKAFTNLKCTVCDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKSILHDWSDENCVKILKNCKRAISGKDKGGKVIVIDGVVELQKKAGNDDPGLDNMDMQMLVLFNSKERNEKEWAKLFSDAGFSDYGIVRTFGWWCIMELSP

[Multiple Choices]
A. tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-adenosyl-L-homocysteine + H(+)
B. L-proline betaine + NADPH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NADP(+) + H2O
C. cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)
D. N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
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

> The supplied sequence exactly matches the archived and current UniProt sequence for IpeOMT1. Its catalytic-activity annotation names the cephaeline-to-emetine reaction and cites experimental evidence (ECO:0000269, PubMed 20061395), supporting choice C. The primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest a SAM-dependent plant O-methyltransferase, making the O-methylation in C more plausible than the N-methylations in A and D or the oxidative reaction in B. They do not establish that this protein acts on cephaeline specifically.


**Missing item-specific fact**

> The substrate specificity of this particular protein—its ability to methylate cephaeline to emetine—is not given in the input and requires protein-specific annotation or experimental knowledge.


**Reason**

> General enzyme-family clues can narrow the reaction type, but distinguishing the exact substrate and product requires an item-specific fact absent from the sequence prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched annotation supports C among the listed choices; the evidence provided does not establish another listed reaction for this protein.


### Important caveats

- The cited evidence is a UniProt annotation with an experimental evidence code, not an independent review of the underlying study.
- The actual source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest a SAM-dependent plant O-methyltransferase, making the O-methylation in C more plausible than the N-methylations in A and D or the oxidative reaction in B. They do not establish that this protein acts on cephaeline specifically.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The substrate specificity of this particular protein—its ability to methylate cephaeline to emetine—is not given in the input and requires protein-specific annotation or experimental knowledge.",
    "reason": "General enzyme-family clues can narrow the reaction type, but distinguishing the exact substrate and product requires an item-specific fact absent from the sequence prompt."
  },
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived and current UniProt sequence for IpeOMT1. Its catalytic-activity annotation names the cephaeline-to-emetine reaction and cites experimental evidence (ECO:0000269, PubMed 20061395), supporting choice C. The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The cited evidence is a UniProt annotation with an experimental evidence code, not an independent review of the underlying study.",
    "The actual source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports C among the listed choices; the evidence provided does not establish another listed reaction for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived and current UniProt sequence for IpeOMT1. Its catalytic-activity annotation names the cephaeline-to-emetine reaction and cites experimental evidence (ECO:0000269, PubMed 20061395), supporting choice C. The primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest a SAM-dependent plant O-methyltransferase, making the O-methylation in C more plausible than the N-methylations in A and D or the oxidative reaction in B. They do not establish that this protein acts on cephaeline specifically.",
    "missing_item_specific_fact": "The substrate specificity of this particular protein—its ability to methylate cephaeline to emetine—is not given in the input and requires protein-specific annotation or experimental knowledge.",
    "reason": "General enzyme-family clues can narrow the reaction type, but distinguishing the exact substrate and product requires an item-specific fact absent from the sequence prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports C among the listed choices; the evidence provided does not establish another listed reaction for this protein."
  },
  "important_caveats": [
    "The cited evidence is a UniProt annotation with an experimental evidence code, not an independent review of the underlying study.",
    "The actual source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt D3KY98 (OMT1_CARIP) exactly (350 AA, SHA256 confirmed). The recommended name is 'Cephaeline 6'-O-methyltransferase IpeOMT1' (EC 2.1.1.396), and the primary catalytic activity annotation (evidence ECO:0000269|PubMed:20061395, experimental) states exactly: cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+). This matches Choice C verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a 'VIVIDG' motif consistent with the Rossmann-like methyltransferase fold and SAM-binding, which could narrow the enzyme to a SAM-dependent methyltransferase. If one could also establish plant origin, choices A (animal PNMT) and D (animal COMT) might be disfavored, and B (oxidative demethylation requiring NADPH/O2) is mechanistically inconsistent with an OMT fold. However, determining that the specific substrate is cephaeline (a complex benzylisoquinoline alkaloid) rather than any of the thousands of other plant OMT substrates requires knowing this is IpeOMT1 from the ipecac alkaloid biosynthesis pathway (Nomura & Kutchan 2010). No sequence feature visible in the primary structure identifies cephaeline as the substrate.


**Missing item-specific fact**

> The specific identity of this protein as IpeOMT1 from Carapichea ipecacuanha and its experimentally determined preference for cephaeline 6'-O-methylation (EC 2.1.1.396), which is only obtainable from the UniProt annotation or the primary literature (PubMed:20061395).


**Reason**

> While the methyltransferase fold can be inferred from sequence motifs, the precise substrate (cephaeline vs. tyramine vs. a catecholamine vs. any of hundreds of other plant OMT substrates) cannot be deduced from the primary sequence. Selection of C over A and D ultimately depends on recognizing this as a plant O-methyltransferase acting on a benzylisoquinoline alkaloid, which is an item-specific database/literature fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the experimental annotation, C is the unique recommended catalytic activity. The other choices describe reactions catalyzed by mechanistically or taxonomically distinct enzymes (animal N-methyltransferases for A and D; a P450-type oxidative demethylase for B). No ambiguity in the correct answer itself, though the reasoning path to select C from sequence alone is weak.


### Important caveats

- The UniProt entry also lists multiple alternative OMT activities (norcoclaurine, deacetylisoipecoside, norprotosinomenine methylation) for this same protein, meaning the enzyme is promiscuous. The 'recommended' activity (cephaeline → emetine) is the one used for the question key.
- The entry was first publicly released in 2025-06-18; the underlying experimental data (PubMed:20061395, 2010) predates this. The evaluated model would not have had access to this Swiss-Prot entry at typical training cutoffs, making the question effectively a memorization test of the 2010 paper.
- Sequence-based identification of plant OMTs is possible in principle (VIVIDG motif, ~350 AA, plant-like composition), but distinguishing among hundreds of plant OMT substrates from sequence alone is not feasible without structural or database information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a 'VIVIDG' motif consistent with the Rossmann-like methyltransferase fold and SAM-binding, which could narrow the enzyme to a SAM-dependent methyltransferase. If one could also establish plant origin, choices A (animal PNMT) and D (animal COMT) might be disfavored, and B (oxidative demethylation requiring NADPH/O2) is mechanistically inconsistent with an OMT fold. However, determining that the specific substrate is cephaeline (a complex benzylisoquinoline alkaloid) rather than any of the thousands of other plant OMT substrates requires knowing this is IpeOMT1 from the ipecac alkaloid biosynthesis pathway (Nomura & Kutchan 2010). No sequence feature visible in the primary structure identifies cephaeline as the substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as IpeOMT1 from Carapichea ipecacuanha and its experimentally determined preference for cephaeline 6'-O-methylation (EC 2.1.1.396), which is only obtainable from the UniProt annotation or the primary literature (PubMed:20061395).",
    "reason": "While the methyltransferase fold can be inferred from sequence motifs, the precise substrate (cephaeline vs. tyramine vs. a catecholamine vs. any of hundreds of other plant OMT substrates) cannot be deduced from the primary sequence. Selection of C over A and D ultimately depends on recognizing this as a plant O-methyltransferase acting on a benzylisoquinoline alkaloid, which is an item-specific database/literature fact."
  },
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt D3KY98 (OMT1_CARIP) exactly (350 AA, SHA256 confirmed). The recommended name is 'Cephaeline 6'-O-methyltransferase IpeOMT1' (EC 2.1.1.396), and the primary catalytic activity annotation (evidence ECO:0000269|PubMed:20061395, experimental) states exactly: cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+). This matches Choice C verbatim."
  },
  "important_caveats": [
    "The UniProt entry also lists multiple alternative OMT activities (norcoclaurine, deacetylisoipecoside, norprotosinomenine methylation) for this same protein, meaning the enzyme is promiscuous. The 'recommended' activity (cephaeline → emetine) is the one used for the question key.",
    "The entry was first publicly released in 2025-06-18; the underlying experimental data (PubMed:20061395, 2010) predates this. The evaluated model would not have had access to this Swiss-Prot entry at typical training cutoffs, making the question effectively a memorization test of the 2010 paper.",
    "Sequence-based identification of plant OMTs is possible in principle (VIVIDG motif, ~350 AA, plant-like composition), but distinguishing among hundreds of plant OMT substrates from sequence alone is not feasible without structural or database information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental annotation, C is the unique recommended catalytic activity. The other choices describe reactions catalyzed by mechanistically or taxonomically distinct enzymes (animal N-methyltransferases for A and D; a P450-type oxidative demethylase for B). No ambiguity in the correct answer itself, though the reasoning path to select C from sequence alone is weak."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt D3KY98 (OMT1_CARIP) exactly (350 AA, SHA256 confirmed). The recommended name is 'Cephaeline 6'-O-methyltransferase IpeOMT1' (EC 2.1.1.396), and the primary catalytic activity annotation (evidence ECO:0000269|PubMed:20061395, experimental) states exactly: cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+). This matches Choice C verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a 'VIVIDG' motif consistent with the Rossmann-like methyltransferase fold and SAM-binding, which could narrow the enzyme to a SAM-dependent methyltransferase. If one could also establish plant origin, choices A (animal PNMT) and D (animal COMT) might be disfavored, and B (oxidative demethylation requiring NADPH/O2) is mechanistically inconsistent with an OMT fold. However, determining that the specific substrate is cephaeline (a complex benzylisoquinoline alkaloid) rather than any of the thousands of other plant OMT substrates requires knowing this is IpeOMT1 from the ipecac alkaloid biosynthesis pathway (Nomura & Kutchan 2010). No sequence feature visible in the primary structure identifies cephaeline as the substrate.",
    "missing_item_specific_fact": "The specific identity of this protein as IpeOMT1 from Carapichea ipecacuanha and its experimentally determined preference for cephaeline 6'-O-methylation (EC 2.1.1.396), which is only obtainable from the UniProt annotation or the primary literature (PubMed:20061395).",
    "reason": "While the methyltransferase fold can be inferred from sequence motifs, the precise substrate (cephaeline vs. tyramine vs. a catecholamine vs. any of hundreds of other plant OMT substrates) cannot be deduced from the primary sequence. Selection of C over A and D ultimately depends on recognizing this as a plant O-methyltransferase acting on a benzylisoquinoline alkaloid, which is an item-specific database/literature fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the experimental annotation, C is the unique recommended catalytic activity. The other choices describe reactions catalyzed by mechanistically or taxonomically distinct enzymes (animal N-methyltransferases for A and D; a P450-type oxidative demethylase for B). No ambiguity in the correct answer itself, though the reasoning path to select C from sequence alone is weak."
  },
  "important_caveats": [
    "The UniProt entry also lists multiple alternative OMT activities (norcoclaurine, deacetylisoipecoside, norprotosinomenine methylation) for this same protein, meaning the enzyme is promiscuous. The 'recommended' activity (cephaeline → emetine) is the one used for the question key.",
    "The entry was first publicly released in 2025-06-18; the underlying experimental data (PubMed:20061395, 2010) predates this. The evaluated model would not have had access to this Swiss-Prot entry at typical training cutoffs, making the question effectively a memorization test of the 2010 paper.",
    "Sequence-based identification of plant OMTs is possible in principle (VIVIDG motif, ~350 AA, plant-like composition), but distinguishing among hundreds of plant OMT substrates from sequence alone is not feasible without structural or database information."
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

**Accession:** `D3KY98` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 56. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:02.422509+00:00.  

```json
"D3KY98"
```

Source SHA-256: `19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:02.422509+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.128"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"(R,S)-norcoclaurine 6-O-methyltransferase IpeOMT1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Coclaurine synthase IpeOMT1"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"(R,S)-norprotosinomenine 6-O-methyltransferase IpeOMT1"}},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"7-O-methyl-N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1"}},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Ipecac/benzylisoquinoline alkaloid O-methyltransferase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"},{"evidenceCode":"ECO:0000312","id":"BAI79243.1","source":"EMBL"}],"value":"IpeOMT1"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Isococlaurine 6-O-methyltransferase IpeOMT1"}},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.396"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Cephaeline 6'-O-methyltransferase IpeOMT1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Emetine synthase IpeOMT1"}]}}
```

Source SHA-256: `19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:02.422509+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:80660"}}],"reaction":{"ecNumber":"2.1.1.396","evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"name":"cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80659"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:149548"},{"database":"ChEBI","id":"CHEBI:231587"}]}}
```

Source SHA-256: `19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)  
**Locator:** `lines 1-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-01T06:27:56.372657+00:00.  

```text
ID   OMT1_CARIP              Reviewed;         350 AA.
AC   D3KY98;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-APR-2010, sequence version 1.
DT   28-JAN-2026, entry version 56.
DE   RecName: Full=Cephaeline 6'-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            Short=Emetine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.396 {ECO:0000269|PubMed:20061395};
DE   AltName: Full=(R,S)-norcoclaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            Short=Coclaurine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.128 {ECO:0000269|PubMed:20061395};
DE   AltName: Full=(R,S)-norprotosinomenine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
DE   AltName: Full=7-O-methyl-N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
DE   AltName: Full=Ipecac/benzylisoquinoline alkaloid O-methyltransferase 1 {ECO:0000303|PubMed:20061395};
DE            Short=IpeOMT1 {ECO:0000303|PubMed:20061395, ECO:0000312|EMBL:BAI79243.1};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
DE   AltName: Full=Isococlaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
DE   AltName: Full=N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
GN   Name=OMT1 {ECO:0000303|PubMed:20061395};
OS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;
OC   Carapichea.
OX   NCBI_TaxID=77880;
```

Source SHA-256: `249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)  
**Locator:** `lines 54-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-01T06:27:56.372657+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cephaeline + S-adenosyl-L-methionine = emetine + S-adenosyl-L-
CC         homocysteine + H(+); Xref=Rhea:RHEA:80659, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:149548,
CC         ChEBI:CHEBI:231587; EC=2.1.1.396;
CC         Evidence={ECO:0000269|PubMed:20061395};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80660;
CC         Evidence={ECO:0000269|PubMed:20061395};
```

Source SHA-256: `249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 196. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
