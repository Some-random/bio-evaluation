# EC_number_0125

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.1.1.348

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNGREHRRGDEAARREARSILFQNQDRSIVLIDVPTSIEEAQASPEEVGCDAGPLRKRRRLISSEPPHLPFKTPEPKAGSGGLTESVSDLMIAAAATEALRVLQESYAGPFCLPRVTRPNPLKSAFVPKGSFFLHGTVSSERDRFAAEAPVFDLIVLDPPWPNRSARRKQRNYRVADSLGSIRETLSLIPIAAHLAPDGLLAVWITNKAGVVELLTGPRGLFAQWGLEQVDEWTWLKITTSGEPIVDVGSTWRKPWERILIARRRGSSRKPACRGRVLVSVPDLHSRKPNLRGLFEDVLVPSNKGLEIFARNLTAGWWSWGDEVLKFQQPEYWVES

[Multiple Choices]
A. 2.1.1.395
B. 2.1.1.348
C. 1.97.1.13
D. 2.4.2.14
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

> The supplied sequence exactly matches the 336-aa UniProt entry for CpMTA1. That entry assigns EC 2.1.1.348 and describes methylation of an adenosine in mRNA to N6-methyladenosine, with experimental-evidence codes citing publications. The matching historical entry also carried this annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest a SAM-dependent methyltransferase, which broadly favors a methyltransferase choice over the transferase alternatives. They do not establish the specific RNA substrate and N6-methylation reaction needed to identify EC 2.1.1.348 rather than another methyltransferase.


**Missing item-specific fact**

> The protein-specific catalytic assignment that CpMTA1 methylates adenosine in mRNA at N6, as established by annotation and cited experimental work.


**Reason**

> The sequence and choices provide broad functional clues but not enough to distinguish the exact four-part EC number; selecting B requires the protein-specific function or its annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation assigns the stated reaction to EC 2.1.1.348; no other listed option is supported by the supplied evidence.


### Important caveats

- The UniProt annotation cites experimental evidence, but the primary papers were not independently retrieved or validated here.
- The exact author source snapshot is unknown; the sequence-matched historical record available by the stated cutoff also contains the EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest a SAM-dependent methyltransferase, which broadly favors a methyltransferase choice over the transferase alternatives. They do not establish the specific RNA substrate and N6-methylation reaction needed to identify EC 2.1.1.348 rather than another methyltransferase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic assignment that CpMTA1 methylates adenosine in mRNA at N6, as established by annotation and cited experimental work.",
    "reason": "The sequence and choices provide broad functional clues but not enough to distinguish the exact four-part EC number; selecting B requires the protein-specific function or its annotation."
  },
  "case_id": "EC_number_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 336-aa UniProt entry for CpMTA1. That entry assigns EC 2.1.1.348 and describes methylation of an adenosine in mRNA to N6-methyladenosine, with experimental-evidence codes citing publications. The matching historical entry also carried this annotation."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary papers were not independently retrieved or validated here.",
    "The exact author source snapshot is unknown; the sequence-matched historical record available by the stated cutoff also contains the EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation assigns the stated reaction to EC 2.1.1.348; no other listed option is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 336-aa UniProt entry for CpMTA1. That entry assigns EC 2.1.1.348 and describes methylation of an adenosine in mRNA to N6-methyladenosine, with experimental-evidence codes citing publications. The matching historical entry also carried this annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest a SAM-dependent methyltransferase, which broadly favors a methyltransferase choice over the transferase alternatives. They do not establish the specific RNA substrate and N6-methylation reaction needed to identify EC 2.1.1.348 rather than another methyltransferase.",
    "missing_item_specific_fact": "The protein-specific catalytic assignment that CpMTA1 methylates adenosine in mRNA at N6, as established by annotation and cited experimental work.",
    "reason": "The sequence and choices provide broad functional clues but not enough to distinguish the exact four-part EC number; selecting B requires the protein-specific function or its annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation assigns the stated reaction to EC 2.1.1.348; no other listed option is supported by the supplied evidence."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary papers were not independently retrieved or validated here.",
    "The exact author source snapshot is unknown; the sequence-matched historical record available by the stated cutoff also contains the EC assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A9P5CQV5 (MTA1_CRYP1, Cryphonectria parasitica) annotates this exact 336-aa sequence as N6-methyladenosine RNA methyltransferase MTA1 with EC 2.1.1.348, supported by experimental evidence (ECO:0000269) from PubMed:39159278 and PubMed:39611846. The catalytic reaction (adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+) is confirmed experimentally. Sequence match is exact (SHA-256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could argue that general methyltransferase-like sequence features (e.g., a Rossmann-fold-like SAM-binding motif) might help eliminate EC 1.97.1.13 (oxidoreductase) and EC 2.4.2.14 (glycosyltransferase), narrowing to EC 2.1.1.x methyltransferases. However, distinguishing EC 2.1.1.348 (N6-methyladenosine RNA methyltransferase) from EC 2.1.1.395 (another specific methyltransferase) requires knowing the exact substrate specificity of this particular enzyme, which is an item-specific fact not derivable from general sequence heuristics.


**Missing item-specific fact**

> The specific substrate identity (adenosine in mRNA, producing N6-methyladenosine) and the recognition of this protein as a METTL3/METTL14 homolog in a fungal m6A writer complex. Without database lookup or memorization of this exact protein's annotation, the 4th digit (348 vs 395) cannot be resolved from sequence features alone.


**Reason**

> The sequence provides no uniquely identifiable catalytic motif that distinguishes m6A writers from other SAM-dependent methyltransferases. Correct selection depends on recognizing this exact sequence as MTA1 from Cryphonectria parasitica or knowing the specific EC assignment, which is a database annotation fact rather than a generalizable biological inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both EC 2.1.1.395 and EC 2.1.1.348 are methyltransferases (EC 2.1.1.x). Without specific knowledge of the substrate (N6-adenosine in mRNA vs. whatever substrate 2.1.1.395 targets), a model relying solely on sequence analysis cannot reliably distinguish between these two options. The broader EC class (2.1.1 vs 1.97 vs 2.4) might be partially inferable, but the 4th digit is not.


### Important caveats

- The UniProt annotation is based on experimental evidence (ECO:0000269) from two published papers (2024, 2025), lending strong support to the key.
- The entry was first publicly released 2025-04-09; the benchmark construction date is unknown, so the author may or may not have had access to this annotation at construction time.
- The identity origin note states the accession was inferred mechanically from image-path metadata absent from the model input, meaning the model had no accession hint.
- EC 2.1.1.395 is a relatively obscure EC number; if it refers to a different specific methyltransferase, the distinction from 2.1.1.348 is entirely substrate-specific and not inferable from general fold recognition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could argue that general methyltransferase-like sequence features (e.g., a Rossmann-fold-like SAM-binding motif) might help eliminate EC 1.97.1.13 (oxidoreductase) and EC 2.4.2.14 (glycosyltransferase), narrowing to EC 2.1.1.x methyltransferases. However, distinguishing EC 2.1.1.348 (N6-methyladenosine RNA methyltransferase) from EC 2.1.1.395 (another specific methyltransferase) requires knowing the exact substrate specificity of this particular enzyme, which is an item-specific fact not derivable from general sequence heuristics.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (adenosine in mRNA, producing N6-methyladenosine) and the recognition of this protein as a METTL3/METTL14 homolog in a fungal m6A writer complex. Without database lookup or memorization of this exact protein's annotation, the 4th digit (348 vs 395) cannot be resolved from sequence features alone.",
    "reason": "The sequence provides no uniquely identifiable catalytic motif that distinguishes m6A writers from other SAM-dependent methyltransferases. Correct selection depends on recognizing this exact sequence as MTA1 from Cryphonectria parasitica or knowing the specific EC assignment, which is a database annotation fact rather than a generalizable biological inference."
  },
  "case_id": "EC_number_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A9P5CQV5 (MTA1_CRYP1, Cryphonectria parasitica) annotates this exact 336-aa sequence as N6-methyladenosine RNA methyltransferase MTA1 with EC 2.1.1.348, supported by experimental evidence (ECO:0000269) from PubMed:39159278 and PubMed:39611846. The catalytic reaction (adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+) is confirmed experimentally. Sequence match is exact (SHA-256 identical)."
  },
  "important_caveats": [
    "The UniProt annotation is based on experimental evidence (ECO:0000269) from two published papers (2024, 2025), lending strong support to the key.",
    "The entry was first publicly released 2025-04-09; the benchmark construction date is unknown, so the author may or may not have had access to this annotation at construction time.",
    "The identity origin note states the accession was inferred mechanically from image-path metadata absent from the model input, meaning the model had no accession hint.",
    "EC 2.1.1.395 is a relatively obscure EC number; if it refers to a different specific methyltransferase, the distinction from 2.1.1.348 is entirely substrate-specific and not inferable from general fold recognition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both EC 2.1.1.395 and EC 2.1.1.348 are methyltransferases (EC 2.1.1.x). Without specific knowledge of the substrate (N6-adenosine in mRNA vs. whatever substrate 2.1.1.395 targets), a model relying solely on sequence analysis cannot reliably distinguish between these two options. The broader EC class (2.1.1 vs 1.97 vs 2.4) might be partially inferable, but the 4th digit is not."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A9P5CQV5 (MTA1_CRYP1, Cryphonectria parasitica) annotates this exact 336-aa sequence as N6-methyladenosine RNA methyltransferase MTA1 with EC 2.1.1.348, supported by experimental evidence (ECO:0000269) from PubMed:39159278 and PubMed:39611846. The catalytic reaction (adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+) is confirmed experimentally. Sequence match is exact (SHA-256 identical).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could argue that general methyltransferase-like sequence features (e.g., a Rossmann-fold-like SAM-binding motif) might help eliminate EC 1.97.1.13 (oxidoreductase) and EC 2.4.2.14 (glycosyltransferase), narrowing to EC 2.1.1.x methyltransferases. However, distinguishing EC 2.1.1.348 (N6-methyladenosine RNA methyltransferase) from EC 2.1.1.395 (another specific methyltransferase) requires knowing the exact substrate specificity of this particular enzyme, which is an item-specific fact not derivable from general sequence heuristics.",
    "missing_item_specific_fact": "The specific substrate identity (adenosine in mRNA, producing N6-methyladenosine) and the recognition of this protein as a METTL3/METTL14 homolog in a fungal m6A writer complex. Without database lookup or memorization of this exact protein's annotation, the 4th digit (348 vs 395) cannot be resolved from sequence features alone.",
    "reason": "The sequence provides no uniquely identifiable catalytic motif that distinguishes m6A writers from other SAM-dependent methyltransferases. Correct selection depends on recognizing this exact sequence as MTA1 from Cryphonectria parasitica or knowing the specific EC assignment, which is a database annotation fact rather than a generalizable biological inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both EC 2.1.1.395 and EC 2.1.1.348 are methyltransferases (EC 2.1.1.x). Without specific knowledge of the substrate (N6-adenosine in mRNA vs. whatever substrate 2.1.1.395 targets), a model relying solely on sequence analysis cannot reliably distinguish between these two options. The broader EC class (2.1.1 vs 1.97 vs 2.4) might be partially inferable, but the 4th digit is not."
  },
  "important_caveats": [
    "The UniProt annotation is based on experimental evidence (ECO:0000269) from two published papers (2024, 2025), lending strong support to the key.",
    "The entry was first publicly released 2025-04-09; the benchmark construction date is unknown, so the author may or may not have had access to this annotation at construction time.",
    "The identity origin note states the accession was inferred mechanically from image-path metadata absent from the model input, meaning the model had no accession hint.",
    "EC 2.1.1.395 is a relatively obscure EC number; if it refers to a different specific methyltransferase, the distinction from 2.1.1.348 is entirely substrate-specific and not inferable from general fold recognition."
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

**Accession:** `A0A9P5CQV5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
"A0A9P5CQV5"
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39159278","source":"PubMed"}],"value":"M6A writer MTA1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"}],"value":"2.1.1.348"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39159278","source":"PubMed"}],"value":"N6-methyladenosine RNA methyltransferase MTA1"}}}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:55585"}}],"reaction":{"ecNumber":"2.1.1.348","evidences":[{"evidenceCode":"ECO:0000269","id":"39159278","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"name":"an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:55584"},{"database":"Rhea","id":"RHEA-COMP:12414"},{"database":"Rhea","id":"RHEA-COMP:12417"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:74411"},{"database":"ChEBI","id":"CHEBI:74449"}]}}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"citation":{"authors":["Zhao L.","Wei X.","Chen F.","Yuan L.","Chen B.","Li R."],"citationCrossReferences":[{"database":"PubMed","id":"39159278"},{"database":"DOI","id":"10.1371/journal.ppat.1012476"}],"citationType":"journal article","firstPage":"e1012476","id":"39159278","journal":"PLoS Pathog.","lastPage":"e1012476","publicationDate":"2024","title":"N6-methyladenosine RNA methyltransferase CpMTA1 mediates CpAphA mRNA stability through a YTHDF1-dependent m6A modification in the chestnut blight fungus.","volume":"20"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P5CQV5.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:17.608993+00:00.  

```json
{"citation":{"authors":["Zhao L.","Wei X.","Chen F.","Chen B.","Li R."],"citationCrossReferences":[{"database":"PubMed","id":"39611846"},{"database":"DOI","id":"10.1128/mbio.01844-24"}],"citationType":"journal article","firstPage":"e0184424","id":"39611846","journal":"MBio","lastPage":"e0184424","publicationDate":"2025","title":"m6A demethylase CpALKBH regulates CpZap1 mRNA stability to modulate the development and virulence of chestnut blight fungus.","volume":"16"},"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE","SUBCELLULAR LOCATION","MUTAGENESIS OF ASP-158 AND TRP-161"]}
```

Source SHA-256: `f80f2e398397ced5f8091de379dc036e65d2569acedc4ca68eae952f6dcf1313`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
DE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:39159278};
DE            EC=2.1.1.348 {ECO:0000269|PubMed:39159278};
DE   AltName: Full=M6A writer MTA1 {ECO:0000303|PubMed:39159278};
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 33-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.
RX   PubMed=39159278; DOI=10.1371/journal.ppat.1012476;
RA   Zhao L., Wei X., Chen F., Yuan L., Chen B., Li R.;
RT   "N6-methyladenosine RNA methyltransferase CpMTA1 mediates CpAphA mRNA
RT   stability through a YTHDF1-dependent m6A modification in the chestnut
RT   blight fungus.";
RL   PLoS Pathog. 20:e1012476-e1012476(2024).
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 41-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
RN   [4]
RP   FUNCTION, CATALYTIC ACTIVITY, DISRUPTION PHENOTYPE, SUBCELLULAR LOCATION,
RP   AND MUTAGENESIS OF ASP-158 AND TRP-161.
RX   PubMed=39611846; DOI=10.1128/mbio.01844-24;
RA   Zhao L., Wei X., Chen F., Chen B., Li R.;
RT   "m6A demethylase CpALKBH regulates CpZap1 mRNA stability to modulate the
RT   development and virulence of chestnut blight fungus.";
RL   MBio 16:e0184424-e0184424(2025).
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P5CQV5?format=txt&versions=12)  
**Locator:** `lines 62-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:22.443513+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-
CC         methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+);
CC         Xref=Rhea:RHEA:55584, Rhea:RHEA-COMP:12414, Rhea:RHEA-COMP:12417,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:74411, ChEBI:CHEBI:74449; EC=2.1.1.348;
CC         Evidence={ECO:0000269|PubMed:39159278, ECO:0000269|PubMed:39611846};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:55585;
CC         Evidence={ECO:0000269|PubMed:39159278, ECO:0000269|PubMed:39611846};
```

Source SHA-256: `7683f1f2026d2d3f7a56a5510cd29c967cf7add9eaf84cb7e8e224b27899b8cc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 125. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
