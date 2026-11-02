# EC_number_0078

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.1.1.27

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGSYHDEKNVMGGSDQGELCSLAMTIASGSVPAMVLKALIELDVLELIKRAGPGAQLSPAQIVAQLPTKNPDAGTMLDRMLRLLASYEILSCSTQTLPDGRVERLYGLAPVCQFFTNNEDGATLGAIVQLSQEKLVVESWYHLKDAVLDGGIPFKKAQGMTIYEYPKTDPRFNQVFNSGMSNYSTIIMRDLLERYKGFEGISTLVDIAGGTGASINMVVSKYPTIKGINFDLPHVIKDAPSYDGVEHVGGDMFESVTKADAMLIKWTLCDWSDEHCLKLLKNCYNALPDNGKVIVCDYVLPMAPETSNAAKTVFLLDAIMLANFVGGKGRTKQEFEALARKVGFEGFEVPCSSYDFSVMELFKKKNN

[Multiple Choices]
A. 2.1.1.353
B. 2.1.1.27
C. 5.4.99.14
D. 2.5.1.76
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

> The exact sequence matches the cited UniProt entry, which assigns EC 2.1.1.27 and records the tyramine + SAM methylation reaction with PubMed experimental evidence. The historical entry also contains this assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad methyltransferase inference, but that does not establish the exact substrate specificity or distinguish EC 2.1.1.27 from another methyltransferase option.


**Missing item-specific fact**

> The protein's demonstrated reaction—methyl transfer from SAM to tyramine and related amines—is not supplied in the question.


**Reason**

> Choosing the precise four-part EC number depends on protein-specific substrate and reaction evidence absent from the sequence prompt; recognizing the sequence or recalling its annotation would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Reviewer-only evidence supports B for this exact sequence, though the input alone does not establish that specific EC assignment.


### Important caveats

- The cited UniProt entry and sequence match are reviewer-only information, not information available to the evaluated model.
- The EC assignment is supported by a recorded experimental-evidence citation; the primary papers were not independently reviewed here.
- The author's exact source snapshot is unknown, but a historical entry within the stated cutoff also matches the sequence and gives the same EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad methyltransferase inference, but that does not establish the exact substrate specificity or distinguish EC 2.1.1.27 from another methyltransferase option.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's demonstrated reaction—methyl transfer from SAM to tyramine and related amines—is not supplied in the question.",
    "reason": "Choosing the precise four-part EC number depends on protein-specific substrate and reaction evidence absent from the sequence prompt; recognizing the sequence or recalling its annotation would be lookup or memorization."
  },
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the cited UniProt entry, which assigns EC 2.1.1.27 and records the tyramine + SAM methylation reaction with PubMed experimental evidence. The historical entry also contains this assignment."
  },
  "important_caveats": [
    "The cited UniProt entry and sequence match are reviewer-only information, not information available to the evaluated model.",
    "The EC assignment is supported by a recorded experimental-evidence citation; the primary papers were not independently reviewed here.",
    "The author's exact source snapshot is unknown, but a historical entry within the stated cutoff also matches the sequence and gives the same EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports B for this exact sequence, though the input alone does not establish that specific EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the cited UniProt entry, which assigns EC 2.1.1.27 and records the tyramine + SAM methylation reaction with PubMed experimental evidence. The historical entry also contains this assignment.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad methyltransferase inference, but that does not establish the exact substrate specificity or distinguish EC 2.1.1.27 from another methyltransferase option.",
    "missing_item_specific_fact": "The protein's demonstrated reaction—methyl transfer from SAM to tyramine and related amines—is not supplied in the question.",
    "reason": "Choosing the precise four-part EC number depends on protein-specific substrate and reaction evidence absent from the sequence prompt; recognizing the sequence or recalling its annotation would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports B for this exact sequence, though the input alone does not establish that specific EC assignment."
  },
  "important_caveats": [
    "The cited UniProt entry and sequence match are reviewer-only information, not information available to the evaluated model.",
    "The EC assignment is supported by a recorded experimental-evidence citation; the primary papers were not independently reviewed here.",
    "The author's exact source snapshot is unknown, but a historical entry within the stated cutoff also matches the sequence and gives the same EC assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AA51VIL7 (sequence SHA256 matched) explicitly annotates EC=2.1.1.27 (Tyramine N-methyltransferase 1) with evidence codes ECO:0000269 (PubMed:38835170, experimental) and ECO:0000255 (PROSITE-ProRule PRU01020). The catalytic reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is confirmed by experimental evidence. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a VQEGFEG motif (~residues 290-296) characteristic of plant class-I SAM-dependent methyltransferases, which could help eliminate C (isomerase, EC 5.4.99.14) and D (alkyl/aryl transferase, EC 2.5.1.76). However, this motif is shared by both O-methyltransferases and N-methyltransferases in plants. The enzyme was initially misnamed 'O-methyltransferase 4' (LwOMT4) and only reclassified as an N-methyltransferase (EC 2.1.1.27) through experimental substrate assays (PubMed:38835170, 2024). Distinguishing 2.1.1.27 from 2.1.1.353 (another specific methyltransferase) from sequence alone is not feasible.


**Missing item-specific fact**

> The specific experimental determination that this enzyme catalyzes N-methylation of tyramine (rather than O-methylation or methylation of another substrate) required in vitro enzyme assays and product identification (PubMed:38835170, PubMed:37675639). No sequence motif in the provided 367-aa sequence uniquely identifies tyramine as the substrate or nitrogen as the methylation acceptor.


**Reason**

> While general methyltransferase motifs allow elimination of C and D, the final choice between A (2.1.1.353) and B (2.1.1.27) depends entirely on the experimentally determined substrate specificity of this particular peyote enzyme. The PROSITE-ProRule PRU01020 only confirms the general SAM-dependent methyltransferase fold, not the specific reaction. This is a recently characterized enzyme (first published 2023-2024) whose EC assignment was resolved only through targeted biochemical experiments.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (2.1.1.353) and B (2.1.1.27) are methyltransferases. Without experimental knowledge of this enzyme's specific substrate (tyramine) and methylation position (nitrogen), a model relying solely on sequence features would see a typical plant SAM-dependent methyltransferase with the VQEGFEG motif and could plausibly assign either EC number. The initial annotation of this enzyme as 'O-methyltransferase 4' further confounds sequence-based inference.


### Important caveats

- The UniProt annotation carries ECO:0000269 (PubMed) evidence, indicating experimental validation, not mere computational prediction.
- The enzyme was initially misclassified as an O-methyltransferase (LwOMT4) in the 2023 paper and only reclassified as an N-methyltransferase (LwNMT1, EC 2.1.1.27) in the 2024 paper, making sequence-based inference particularly unreliable for this entry.
- The PROSITE-ProRule PRU01020 evidence (ECO:0000255) only supports the general methyltransferase classification, not the specific EC 2.1.1.27 assignment.
- The sequence is from a recently characterized enzyme (first public release 2025-06-18), limiting the training data available to models for this specific entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a VQEGFEG motif (~residues 290-296) characteristic of plant class-I SAM-dependent methyltransferases, which could help eliminate C (isomerase, EC 5.4.99.14) and D (alkyl/aryl transferase, EC 2.5.1.76). However, this motif is shared by both O-methyltransferases and N-methyltransferases in plants. The enzyme was initially misnamed 'O-methyltransferase 4' (LwOMT4) and only reclassified as an N-methyltransferase (EC 2.1.1.27) through experimental substrate assays (PubMed:38835170, 2024). Distinguishing 2.1.1.27 from 2.1.1.353 (another specific methyltransferase) from sequence alone is not feasible.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimental determination that this enzyme catalyzes N-methylation of tyramine (rather than O-methylation or methylation of another substrate) required in vitro enzyme assays and product identification (PubMed:38835170, PubMed:37675639). No sequence motif in the provided 367-aa sequence uniquely identifies tyramine as the substrate or nitrogen as the methylation acceptor.",
    "reason": "While general methyltransferase motifs allow elimination of C and D, the final choice between A (2.1.1.353) and B (2.1.1.27) depends entirely on the experimentally determined substrate specificity of this particular peyote enzyme. The PROSITE-ProRule PRU01020 only confirms the general SAM-dependent methyltransferase fold, not the specific reaction. This is a recently characterized enzyme (first published 2023-2024) whose EC assignment was resolved only through targeted biochemical experiments."
  },
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AA51VIL7 (sequence SHA256 matched) explicitly annotates EC=2.1.1.27 (Tyramine N-methyltransferase 1) with evidence codes ECO:0000269 (PubMed:38835170, experimental) and ECO:0000255 (PROSITE-ProRule PRU01020). The catalytic reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is confirmed by experimental evidence. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (PubMed) evidence, indicating experimental validation, not mere computational prediction.",
    "The enzyme was initially misclassified as an O-methyltransferase (LwOMT4) in the 2023 paper and only reclassified as an N-methyltransferase (LwNMT1, EC 2.1.1.27) in the 2024 paper, making sequence-based inference particularly unreliable for this entry.",
    "The PROSITE-ProRule PRU01020 evidence (ECO:0000255) only supports the general methyltransferase classification, not the specific EC 2.1.1.27 assignment.",
    "The sequence is from a recently characterized enzyme (first public release 2025-06-18), limiting the training data available to models for this specific entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (2.1.1.353) and B (2.1.1.27) are methyltransferases. Without experimental knowledge of this enzyme's specific substrate (tyramine) and methylation position (nitrogen), a model relying solely on sequence features would see a typical plant SAM-dependent methyltransferase with the VQEGFEG motif and could plausibly assign either EC number. The initial annotation of this enzyme as 'O-methyltransferase 4' further confounds sequence-based inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AA51VIL7 (sequence SHA256 matched) explicitly annotates EC=2.1.1.27 (Tyramine N-methyltransferase 1) with evidence codes ECO:0000269 (PubMed:38835170, experimental) and ECO:0000255 (PROSITE-ProRule PRU01020). The catalytic reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is confirmed by experimental evidence. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a VQEGFEG motif (~residues 290-296) characteristic of plant class-I SAM-dependent methyltransferases, which could help eliminate C (isomerase, EC 5.4.99.14) and D (alkyl/aryl transferase, EC 2.5.1.76). However, this motif is shared by both O-methyltransferases and N-methyltransferases in plants. The enzyme was initially misnamed 'O-methyltransferase 4' (LwOMT4) and only reclassified as an N-methyltransferase (EC 2.1.1.27) through experimental substrate assays (PubMed:38835170, 2024). Distinguishing 2.1.1.27 from 2.1.1.353 (another specific methyltransferase) from sequence alone is not feasible.",
    "missing_item_specific_fact": "The specific experimental determination that this enzyme catalyzes N-methylation of tyramine (rather than O-methylation or methylation of another substrate) required in vitro enzyme assays and product identification (PubMed:38835170, PubMed:37675639). No sequence motif in the provided 367-aa sequence uniquely identifies tyramine as the substrate or nitrogen as the methylation acceptor.",
    "reason": "While general methyltransferase motifs allow elimination of C and D, the final choice between A (2.1.1.353) and B (2.1.1.27) depends entirely on the experimentally determined substrate specificity of this particular peyote enzyme. The PROSITE-ProRule PRU01020 only confirms the general SAM-dependent methyltransferase fold, not the specific reaction. This is a recently characterized enzyme (first published 2023-2024) whose EC assignment was resolved only through targeted biochemical experiments."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (2.1.1.353) and B (2.1.1.27) are methyltransferases. Without experimental knowledge of this enzyme's specific substrate (tyramine) and methylation position (nitrogen), a model relying solely on sequence features would see a typical plant SAM-dependent methyltransferase with the VQEGFEG motif and could plausibly assign either EC number. The initial annotation of this enzyme as 'O-methyltransferase 4' further confounds sequence-based inference."
  },
  "important_caveats": [
    "The UniProt annotation carries ECO:0000269 (PubMed) evidence, indicating experimental validation, not mere computational prediction.",
    "The enzyme was initially misclassified as an O-methyltransferase (LwOMT4) in the 2023 paper and only reclassified as an N-methyltransferase (LwNMT1, EC 2.1.1.27) in the 2024 paper, making sequence-based inference particularly unreliable for this entry.",
    "The PROSITE-ProRule PRU01020 evidence (ECO:0000255) only supports the general methyltransferase classification, not the specific EC 2.1.1.27 assignment.",
    "The sequence is from a recently characterized enzyme (first public release 2025-06-18), limiting the training data available to models for this specific entry."
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

**Accession:** `A0AA51VIL7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 10. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.487954+00:00.  

```json
"A0AA51VIL7"
```

Source SHA-256: `a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.487954+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37675639","source":"PubMed"}],"value":"O-methyltransferase 4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"37675639","source":"PubMed"}],"value":"LwOMT4"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01020","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"value":"2.1.1.27"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"38835170","source":"PubMed"}],"value":"Tyramine N-methyltransferase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38835170","source":"PubMed"}],"value":"LwNMT1"}]}}
```

Source SHA-256: `a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:55.487954+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:14866"}}],"reaction":{"ecNumber":"2.1.1.27","evidences":[{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"name":"tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14865"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:58155"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:327995"}]}}
```

Source SHA-256: `a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 10 / 1.  
**Retrieved:** 2026-11-01T06:27:38.117320+00:00.  

```text
DE   RecName: Full=Tyramine N-methyltransferase 1 {ECO:0000305|PubMed:38835170};
DE            Short=LwNMT1 {ECO:0000303|PubMed:38835170};
DE            EC=2.1.1.27 {ECO:0000255|PROSITE-ProRule:PRU01020, ECO:0000269|PubMed:38835170};
DE   AltName: Full=O-methyltransferase 4 {ECO:0000303|PubMed:37675639};
DE            Short=LwOMT4 {ECO:0000303|PubMed:37675639};
```

Source SHA-256: `e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)  
**Locator:** `lines 18-25`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 10 / 1.  
**Retrieved:** 2026-11-01T06:27:38.117320+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:WMX25282.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RC   STRAIN=cv. Jourdaniana;
RX   PubMed=37675639; DOI=10.1111/tpj.16447;
RA   Watkins J.L., Li Q., Yeaman S., Facchini P.J.;
RT   "Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora
RT   williamsii).";
RL   Plant J. 116:635-649(2023).
```

Source SHA-256: `e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)  
**Locator:** `lines 26-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 10 / 1.  
**Retrieved:** 2026-11-01T06:27:38.117320+00:00.  

```text
RN   [2]
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, MUTAGENESIS OF TRP-266; ASP-270 AND
RP   PHE-324, CATALYTIC ACTIVITY, PATHWAY, AND BIOTECHNOLOGY.
RC   STRAIN=cv. Rehovot 7;
RX   PubMed=38835170; DOI=10.1016/j.molp.2024.05.012;
RA   Berman P., de Haro L.A., Cavaco A.-R., Panda S., Dong Y., Kuzmich N.,
RA   Lichtenstein G., Peleg Y., Harat H., Jozwiak A., Cai J., Heinig U.,
RA   Meir S., Rogachev I., Aharoni A.;
RT   "The biosynthetic pathway of the hallucinogen mescaline and its
RT   heterologous reconstruction.";
RL   Mol. Plant 17:1129-1150(2024).
```

Source SHA-256: `e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)  
**Locator:** `lines 50-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 10 / 1.  
**Retrieved:** 2026-11-01T06:27:38.117320+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-
CC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:14865,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58155,
CC         ChEBI:CHEBI:59789, ChEBI:CHEBI:327995; EC=2.1.1.27;
CC         Evidence={ECO:0000269|PubMed:38835170};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14866;
CC         Evidence={ECO:0000269|PubMed:38835170};
```

Source SHA-256: `e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
