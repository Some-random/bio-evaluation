# EC_number_0180

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.1.1.136

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. 1.1.1.136
B. 1.1.1.336
C. 3.6.1.5
D. 3.2.1.31
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

> The supplied sequence matches UniProt entry Q9RHD7, which annotates it as UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136, with experimental evidence cited to PubMed 18065759. The annotation and reaction are also present in a historical matched entry.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General sequence features might suggest an oxidoreductase, helping distinguish the EC 1.1 choices from the hydrolase choices, but they do not establish the exact substrate-specific EC number.


**Missing item-specific fact**

> The protein's specific catalytic activity—UDP-N-acetyl-D-glucosamine 6-dehydrogenase activity—is needed to distinguish EC 1.1.1.136 from the other choices.


**Reason**

> The exact reaction and substrate specificity are protein-specific facts absent from the input; inferring them requires an annotation, experimental result, or equivalent item-specific knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited annotation assigns the matched sequence EC 1.1.1.136, and the choices describe distinct EC classifications.


### Important caveats

- The UniProt annotation cites experimental evidence, but the primary paper was not independently retrieved or validated here.
- The author’s exact source snapshot is unknown; both current and historical matched records support the same EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General sequence features might suggest an oxidoreductase, helping distinguish the EC 1.1 choices from the hydrolase choices, but they do not establish the exact substrate-specific EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific catalytic activity—UDP-N-acetyl-D-glucosamine 6-dehydrogenase activity—is needed to distinguish EC 1.1.1.136 from the other choices.",
    "reason": "The exact reaction and substrate specificity are protein-specific facts absent from the input; inferring them requires an annotation, experimental result, or equivalent item-specific knowledge."
  },
  "case_id": "EC_number_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt entry Q9RHD7, which annotates it as UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136, with experimental evidence cited to PubMed 18065759. The annotation and reaction are also present in a historical matched entry."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently retrieved or validated here.",
    "The author’s exact source snapshot is unknown; both current and historical matched records support the same EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited annotation assigns the matched sequence EC 1.1.1.136, and the choices describe distinct EC classifications."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt entry Q9RHD7, which annotates it as UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136, with experimental evidence cited to PubMed 18065759. The annotation and reaction are also present in a historical matched entry.",
    "evidence_ids": ["C1", "C4", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General sequence features might suggest an oxidoreductase, helping distinguish the EC 1.1 choices from the hydrolase choices, but they do not establish the exact substrate-specific EC number.",
    "missing_item_specific_fact": "The protein's specific catalytic activity—UDP-N-acetyl-D-glucosamine 6-dehydrogenase activity—is needed to distinguish EC 1.1.1.136 from the other choices.",
    "reason": "The exact reaction and substrate specificity are protein-specific facts absent from the input; inferring them requires an annotation, experimental result, or equivalent item-specific knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited annotation assigns the matched sequence EC 1.1.1.136, and the choices describe distinct EC classifications."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently retrieved or validated here.",
    "The author’s exact source snapshot is unknown; both current and historical matched records support the same EC assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9RHD7 (WBPO_PSEAI, Pseudomonas aeruginosa) has an exact sequence match to the provided 422-aa sequence and is annotated as EC 1.1.1.136 (UDP-N-acetyl-D-glucosamine 6-dehydrogenase) with experimental evidence (ECO:0000269, PubMed:18065759, J. Biol. Chem. 2008). The catalytic activity (UDP-N-acetyl-alpha-D-glucosamine + 2 NAD+ + H2O → UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H+) is experimentally validated.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a clear Rossmann-fold NAD-binding motif (VAVVGLGYVGLPLAV, GxGxxG variant), identifying the protein as an oxidoreductase/dehydrogenase and eliminating the hydrolase options C (3.6.1.5, apyrase) and D (3.2.1.31, beta-glucosidase). The sequence also contains a 'GHC' catalytic motif (LVGGHCIGVDPYY), which is a hallmark of UDP-sugar 6-dehydrogenases where the cysteine acts as the catalytic nucleophile. The two-domain architecture (N-terminal Rossmann + C-terminal sugar-binding domain) is consistent with UDP-GlcNAc 6-dehydrogenase. These general biochemical features provide a reasoning path toward EC 1.1.1.136.


**Missing item-specific fact**

> The distinction between EC 1.1.1.136 and EC 1.1.1.336 (if the latter is a valid EC number) may require knowing which specific EC numbers exist and their exact substrate assignments. However, if 1.1.1.336 is not a valid/assigned EC number, it is simply a non-existent distractor.


**Reason**

> The Rossmann fold and GHC catalytic motif provide concrete, general biological reasoning to classify the protein as a sugar dehydrogenase, eliminating hydrolases (C, D). The GHC motif specifically points toward UDP-sugar 6-dehydrogenase (EC 1.1.1.136). While the final A-vs-B distinction has a minor lookup component (knowing whether 1.1.1.336 is valid), the overall reasoning chain from sequence features to the correct answer is defensible using general enzymology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (apyrase) and D (beta-glucosidase) are clearly eliminated by the oxidoreductase architecture. Option B (1.1.1.336) is either a non-existent EC number or a very obscure entry; even if valid, the GHC catalytic motif and domain architecture favor 1.1.1.136. No ambiguity among the provided choices given the sequence evidence.


### Important caveats

- The EC 1.1.1.136 annotation is experimentally supported (ECO:0000269), not merely computational inference.
- The identity of the protein as WbpO from P. aeruginosa was inferred by the reviewer from dataset metadata; the evaluated model had only the raw sequence.
- Whether EC 1.1.1.336 is a valid assigned EC number was not independently verified in this audit; if it does not exist, option B is trivially wrong.
- The GHC motif is characteristic of UDP-sugar 6-dehydrogenases but is not absolutely unique to this EC class; however, combined with the Rossmann fold and two-domain architecture, it provides strong inferential support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a clear Rossmann-fold NAD-binding motif (VAVVGLGYVGLPLAV, GxGxxG variant), identifying the protein as an oxidoreductase/dehydrogenase and eliminating the hydrolase options C (3.6.1.5, apyrase) and D (3.2.1.31, beta-glucosidase). The sequence also contains a 'GHC' catalytic motif (LVGGHCIGVDPYY), which is a hallmark of UDP-sugar 6-dehydrogenases where the cysteine acts as the catalytic nucleophile. The two-domain architecture (N-terminal Rossmann + C-terminal sugar-binding domain) is consistent with UDP-GlcNAc 6-dehydrogenase. These general biochemical features provide a reasoning path toward EC 1.1.1.136.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The distinction between EC 1.1.1.136 and EC 1.1.1.336 (if the latter is a valid EC number) may require knowing which specific EC numbers exist and their exact substrate assignments. However, if 1.1.1.336 is not a valid/assigned EC number, it is simply a non-existent distractor.",
    "reason": "The Rossmann fold and GHC catalytic motif provide concrete, general biological reasoning to classify the protein as a sugar dehydrogenase, eliminating hydrolases (C, D). The GHC motif specifically points toward UDP-sugar 6-dehydrogenase (EC 1.1.1.136). While the final A-vs-B distinction has a minor lookup component (knowing whether 1.1.1.336 is valid), the overall reasoning chain from sequence features to the correct answer is defensible using general enzymology knowledge."
  },
  "case_id": "EC_number_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9RHD7 (WBPO_PSEAI, Pseudomonas aeruginosa) has an exact sequence match to the provided 422-aa sequence and is annotated as EC 1.1.1.136 (UDP-N-acetyl-D-glucosamine 6-dehydrogenase) with experimental evidence (ECO:0000269, PubMed:18065759, J. Biol. Chem. 2008). The catalytic activity (UDP-N-acetyl-alpha-D-glucosamine + 2 NAD+ + H2O → UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H+) is experimentally validated."
  },
  "important_caveats": [
    "The EC 1.1.1.136 annotation is experimentally supported (ECO:0000269), not merely computational inference.",
    "The identity of the protein as WbpO from P. aeruginosa was inferred by the reviewer from dataset metadata; the evaluated model had only the raw sequence.",
    "Whether EC 1.1.1.336 is a valid assigned EC number was not independently verified in this audit; if it does not exist, option B is trivially wrong.",
    "The GHC motif is characteristic of UDP-sugar 6-dehydrogenases but is not absolutely unique to this EC class; however, combined with the Rossmann fold and two-domain architecture, it provides strong inferential support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (apyrase) and D (beta-glucosidase) are clearly eliminated by the oxidoreductase architecture. Option B (1.1.1.336) is either a non-existent EC number or a very obscure entry; even if valid, the GHC catalytic motif and domain architecture favor 1.1.1.136. No ambiguity among the provided choices given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9RHD7 (WBPO_PSEAI, Pseudomonas aeruginosa) has an exact sequence match to the provided 422-aa sequence and is annotated as EC 1.1.1.136 (UDP-N-acetyl-D-glucosamine 6-dehydrogenase) with experimental evidence (ECO:0000269, PubMed:18065759, J. Biol. Chem. 2008). The catalytic activity (UDP-N-acetyl-alpha-D-glucosamine + 2 NAD+ + H2O → UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H+) is experimentally validated.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a clear Rossmann-fold NAD-binding motif (VAVVGLGYVGLPLAV, GxGxxG variant), identifying the protein as an oxidoreductase/dehydrogenase and eliminating the hydrolase options C (3.6.1.5, apyrase) and D (3.2.1.31, beta-glucosidase). The sequence also contains a 'GHC' catalytic motif (LVGGHCIGVDPYY), which is a hallmark of UDP-sugar 6-dehydrogenases where the cysteine acts as the catalytic nucleophile. The two-domain architecture (N-terminal Rossmann + C-terminal sugar-binding domain) is consistent with UDP-GlcNAc 6-dehydrogenase. These general biochemical features provide a reasoning path toward EC 1.1.1.136.",
    "missing_item_specific_fact": "The distinction between EC 1.1.1.136 and EC 1.1.1.336 (if the latter is a valid EC number) may require knowing which specific EC numbers exist and their exact substrate assignments. However, if 1.1.1.336 is not a valid/assigned EC number, it is simply a non-existent distractor.",
    "reason": "The Rossmann fold and GHC catalytic motif provide concrete, general biological reasoning to classify the protein as a sugar dehydrogenase, eliminating hydrolases (C, D). The GHC motif specifically points toward UDP-sugar 6-dehydrogenase (EC 1.1.1.136). While the final A-vs-B distinction has a minor lookup component (knowing whether 1.1.1.336 is valid), the overall reasoning chain from sequence features to the correct answer is defensible using general enzymology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (apyrase) and D (beta-glucosidase) are clearly eliminated by the oxidoreductase architecture. Option B (1.1.1.336) is either a non-existent EC number or a very obscure entry; even if valid, the GHC catalytic motif and domain architecture favor 1.1.1.136. No ambiguity among the provided choices given the sequence evidence."
  },
  "important_caveats": [
    "The EC 1.1.1.136 annotation is experimentally supported (ECO:0000269), not merely computational inference.",
    "The identity of the protein as WbpO from P. aeruginosa was inferred by the reviewer from dataset metadata; the evaluated model had only the raw sequence.",
    "Whether EC 1.1.1.336 is a valid assigned EC number was not independently verified in this audit; if it does not exist, option B is trivially wrong.",
    "The GHC motif is characteristic of UDP-sugar 6-dehydrogenases but is not absolutely unique to this EC class; however, combined with the Rossmann fold and two-domain architecture, it provides strong inferential support."
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

**Accession:** `Q9RHD7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 111. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
"Q9RHD7"
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"1.1.1.136"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-D-glucosamine 6-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-GlcNAc 6-dehydrogenase"}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13326"}}],"reaction":{"ecNumber":"1.1.1.136","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13325"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:65040"}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"citation":{"authors":["Miller W.L.","Matewish M.J.","McNally D.J.","Ishiyama N.","Anderson E.M.","Brewer D.","Brisson J.R.","Berghuis A.M.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"18065759"},{"database":"DOI","id":"10.1074/jbc.m708894200"}],"citationType":"journal article","firstPage":"3507","id":"18065759","journal":"J. Biol. Chem.","lastPage":"3518","publicationDate":"2008","title":"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.","volume":"283"},"referenceComments":[{"type":"STRAIN","value":"PAK / Serotype O6"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
DE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000305};
DE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000305};
DE            EC=1.1.1.136 {ECO:0000269|PubMed:18065759};
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 47-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
RN   [5]
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, AND DISRUPTION PHENOTYPE.
RC   STRAIN=PAK / Serotype O6;
RX   PubMed=18065759; DOI=10.1074/jbc.m708894200;
RA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,
RA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;
RT   "Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-
RT   antigen biosynthesis enzyme WbpO.";
RL   J. Biol. Chem. 283:3507-3518(2008).
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 67-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-
CC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);
CC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:65040; EC=1.1.1.136;
CC         Evidence={ECO:0000269|PubMed:18065759};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;
CC         Evidence={ECO:0000269|PubMed:18065759};
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 180. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
