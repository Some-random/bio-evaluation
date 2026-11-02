# catalytic_activity_0157

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — dTMP + ATP = dTDP + ADP

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSAGKRGALIIFEGCDRSGKTTQSRLLVELLKSKGIPTLPMNFPERSSSIGQVINSYLTNSKDLPDEVIHLMFSANRWEHINQVKEKLLEGTTLVVDRYSFSGVAYSAAKGLDFDWCYAPERGLIKPDAVFYLRAPPNDLTHRGQYGKERYEKVEFQGRVAEVFNRICSKEGSYFHQFDARQSVEDLHAQIASITEELLPKVATRPLDTLS

[Multiple Choices]
A. dopamine + S-adenosyl-L-methionine = 4-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
B. dTMP + ATP = dTDP + ADP
C. O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)
D. L-isoleucyl-tRNA(Ile) + acetyl-CoA = N-acetyl-L-isoleucyl-tRNA(Ile) + CoA + H(+)
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

> The supplied sequence exactly matches the reviewed Drosophila melanogaster thymidylate kinase entry, whose cited catalytic activity includes dTMP + ATP = dTDP + ADP. The annotation assigns experimental evidence to this reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Walker-A-like nucleotide-binding motif (GxxxxGKT), consistent with an ATP-dependent kinase. Among the choices, B is the nucleotide-phosphorylation reaction; the other options describe methyltransferase, PLP-dependent condensation, and acetyltransferase reactions.


**Missing item-specific fact**

> The exact substrate specificity—thymidylate kinase activity—is not established by the motif alone, though the options make B the biologically supported kinase candidate.


**Reason**

> A sequence motif and the contrasting reaction classes provide a meaningful basis to favor B without recognizing the exact sequence or consulting its database entry. The precise dTMP substrate assignment would otherwise require protein-specific evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the kinase-like sequence motif and the reaction classes listed, B is the only defensible choice.


### Important caveats

- The experimental-support judgment reflects the cited UniProt annotation and its evidence code; the primary paper was not independently reviewed here.
- The annotation and sequence match are reviewer-only evidence and were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Walker-A-like nucleotide-binding motif (GxxxxGKT), consistent with an ATP-dependent kinase. Among the choices, B is the nucleotide-phosphorylation reaction; the other options describe methyltransferase, PLP-dependent condensation, and acetyltransferase reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate specificity—thymidylate kinase activity—is not established by the motif alone, though the options make B the biologically supported kinase candidate.",
    "reason": "A sequence motif and the contrasting reaction classes provide a meaningful basis to favor B without recognizing the exact sequence or consulting its database entry. The precise dTMP substrate assignment would otherwise require protein-specific evidence."
  },
  "case_id": "catalytic_activity_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Drosophila melanogaster thymidylate kinase entry, whose cited catalytic activity includes dTMP + ATP = dTDP + ADP. The annotation assigns experimental evidence to this reaction."
  },
  "important_caveats": [
    "The experimental-support judgment reflects the cited UniProt annotation and its evidence code; the primary paper was not independently reviewed here.",
    "The annotation and sequence match are reviewer-only evidence and were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the kinase-like sequence motif and the reaction classes listed, B is the only defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Drosophila melanogaster thymidylate kinase entry, whose cited catalytic activity includes dTMP + ATP = dTDP + ADP. The annotation assigns experimental evidence to this reaction.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Walker-A-like nucleotide-binding motif (GxxxxGKT), consistent with an ATP-dependent kinase. Among the choices, B is the nucleotide-phosphorylation reaction; the other options describe methyltransferase, PLP-dependent condensation, and acetyltransferase reactions.",
    "missing_item_specific_fact": "The exact substrate specificity—thymidylate kinase activity—is not established by the motif alone, though the options make B the biologically supported kinase candidate.",
    "reason": "A sequence motif and the contrasting reaction classes provide a meaningful basis to favor B without recognizing the exact sequence or consulting its database entry. The precise dTMP substrate assignment would otherwise require protein-specific evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the kinase-like sequence motif and the reaction classes listed, B is the only defensible choice."
  },
  "important_caveats": [
    "The experimental-support judgment reflects the cited UniProt annotation and its evidence code; the primary paper was not independently reviewed here.",
    "The annotation and sequence match are reviewer-only evidence and were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer-only evidence (C4, C5, H2, H4) confirms the protein (UniProt A1ZB29, Drosophila melanogaster thymidylate kinase, EC 2.7.4.9) catalyzes dTMP + ATP = dTDP + ADP, supported by experimental evidence (ECO:0000269, PubMed:38518117). The 211-aa sequence in the question matches the UniProt entry exactly (SHA256 confirmed). The expected answer B is directly stated in the UniProt catalytic activity annotation with experimental backing.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [C7](#evidence-c7), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 211 residues long and contains a P-loop (Walker A) motif (GCDRSGK at ~residues 13-19), identifying it as a small nucleotide-binding kinase. Among the four choices: (A) COMT is a ~271-aa methyltransferase with a different fold; (C) cystathionine gamma-synthase is a ~400+ aa PLP-dependent enzyme; (D) an aminoacyl-tRNA synthetase-related acetyltransferase would be substantially larger (~500+ aa). Only TMPK (option B) is characteristically ~200-210 aa and a P-loop kinase. The size constraint alone eliminates all three distractors, and the P-loop motif confirms kinase activity on nucleotides.


**Missing item-specific fact**

> None critical. One could note that distinguishing TMPK from other small P-loop kinases (e.g., adenylate kinase) would require additional specificity, but adenylate kinase is not among the choices, so the four options are separable by size and fold class.


**Reason**

> The 211-aa length and P-loop motif provide a concrete biological argument to eliminate options A (~271 aa methyltransferase), C (~400 aa PLP enzyme), and D (large synthetase-related enzyme), leaving B as the only kinetically and structurally consistent choice. This relies on general knowledge of enzyme class sizes and folds rather than memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct enzyme classes with markedly different sizes and folds. The 211-aa P-loop kinase is unambiguously inconsistent with COMT, cystathionine gamma-synthase, and an aminoacyl-tRNA synthetase-related enzyme. The secondary activity on dUMP (confirmed experimentally) is not among the choices and does not create ambiguity.


### Important caveats

- The protein also catalyzes dUMP + ATP = dUDP + ADP (evidence C6/H5), but this reaction is not among the answer choices and does not affect the answer.
- The experimental evidence (PubMed:38518117, 2024) postdates the sequence deposition (2007); the annotation was added to UniProt in 2025. The author's source snapshot is unknown.
- The size-based elimination argument assumes general knowledge of typical enzyme-class sizes; a model without this knowledge might struggle, but the reasoning path is valid for a knowledgeable biologist.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 211 residues long and contains a P-loop (Walker A) motif (GCDRSGK at ~residues 13-19), identifying it as a small nucleotide-binding kinase. Among the four choices: (A) COMT is a ~271-aa methyltransferase with a different fold; (C) cystathionine gamma-synthase is a ~400+ aa PLP-dependent enzyme; (D) an aminoacyl-tRNA synthetase-related acetyltransferase would be substantially larger (~500+ aa). Only TMPK (option B) is characteristically ~200-210 aa and a P-loop kinase. The size constraint alone eliminates all three distractors, and the P-loop motif confirms kinase activity on nucleotides.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. One could note that distinguishing TMPK from other small P-loop kinases (e.g., adenylate kinase) would require additional specificity, but adenylate kinase is not among the choices, so the four options are separable by size and fold class.",
    "reason": "The 211-aa length and P-loop motif provide a concrete biological argument to eliminate options A (~271 aa methyltransferase), C (~400 aa PLP enzyme), and D (large synthetase-related enzyme), leaving B as the only kinetically and structurally consistent choice. This relies on general knowledge of enzyme class sizes and folds rather than memorizing this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "C7",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only evidence (C4, C5, H2, H4) confirms the protein (UniProt A1ZB29, Drosophila melanogaster thymidylate kinase, EC 2.7.4.9) catalyzes dTMP + ATP = dTDP + ADP, supported by experimental evidence (ECO:0000269, PubMed:38518117). The 211-aa sequence in the question matches the UniProt entry exactly (SHA256 confirmed). The expected answer B is directly stated in the UniProt catalytic activity annotation with experimental backing."
  },
  "important_caveats": [
    "The protein also catalyzes dUMP + ATP = dUDP + ADP (evidence C6/H5), but this reaction is not among the answer choices and does not affect the answer.",
    "The experimental evidence (PubMed:38518117, 2024) postdates the sequence deposition (2007); the annotation was added to UniProt in 2025. The author's source snapshot is unknown.",
    "The size-based elimination argument assumes general knowledge of typical enzyme-class sizes; a model without this knowledge might struggle, but the reasoning path is valid for a knowledgeable biologist."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes with markedly different sizes and folds. The 211-aa P-loop kinase is unambiguously inconsistent with COMT, cystathionine gamma-synthase, and an aminoacyl-tRNA synthetase-related enzyme. The secondary activity on dUMP (confirmed experimentally) is not among the choices and does not create ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only evidence (C4, C5, H2, H4) confirms the protein (UniProt A1ZB29, Drosophila melanogaster thymidylate kinase, EC 2.7.4.9) catalyzes dTMP + ATP = dTDP + ADP, supported by experimental evidence (ECO:0000269, PubMed:38518117). The 211-aa sequence in the question matches the UniProt entry exactly (SHA256 confirmed). The expected answer B is directly stated in the UniProt catalytic activity annotation with experimental backing.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "C7", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 211 residues long and contains a P-loop (Walker A) motif (GCDRSGK at ~residues 13-19), identifying it as a small nucleotide-binding kinase. Among the four choices: (A) COMT is a ~271-aa methyltransferase with a different fold; (C) cystathionine gamma-synthase is a ~400+ aa PLP-dependent enzyme; (D) an aminoacyl-tRNA synthetase-related acetyltransferase would be substantially larger (~500+ aa). Only TMPK (option B) is characteristically ~200-210 aa and a P-loop kinase. The size constraint alone eliminates all three distractors, and the P-loop motif confirms kinase activity on nucleotides.",
    "missing_item_specific_fact": "None critical. One could note that distinguishing TMPK from other small P-loop kinases (e.g., adenylate kinase) would require additional specificity, but adenylate kinase is not among the choices, so the four options are separable by size and fold class.",
    "reason": "The 211-aa length and P-loop motif provide a concrete biological argument to eliminate options A (~271 aa methyltransferase), C (~400 aa PLP enzyme), and D (large synthetase-related enzyme), leaving B as the only kinetically and structurally consistent choice. This relies on general knowledge of enzyme class sizes and folds rather than memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct enzyme classes with markedly different sizes and folds. The 211-aa P-loop kinase is unambiguously inconsistent with COMT, cystathionine gamma-synthase, and an aminoacyl-tRNA synthetase-related enzyme. The secondary activity on dUMP (confirmed experimentally) is not among the choices and does not create ambiguity."
  },
  "important_caveats": [
    "The protein also catalyzes dUMP + ATP = dUDP + ADP (evidence C6/H5), but this reaction is not among the answer choices and does not affect the answer.",
    "The experimental evidence (PubMed:38518117, 2024) postdates the sequence deposition (2007); the annotation was added to UniProt in 2025. The author's source snapshot is unknown.",
    "The size-based elimination argument assumes general knowledge of typical enzyme-class sizes; a model without this knowledge might struggle, but the reasoning path is valid for a knowledgeable biologist."
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

**Accession:** `A1ZB29` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 156. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:47.024723+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0034299","source":"FlyBase"}],"value":"Deoxythymidylate kinase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38518117","source":"PubMed"}],"value":"2.7.4.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38518117","source":"PubMed"}],"value":"Thymidylate kinase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38518117","source":"PubMed"}],"value":"DmTMPK"}]}}
```

Source SHA-256: `8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:47.024723+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38518117","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13518"}}],"reaction":{"ecNumber":"2.7.4.9","evidences":[{"evidenceCode":"ECO:0000269","id":"38518117","source":"PubMed"}],"name":"dTMP + ATP = dTDP + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13517"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:58369"},{"database":"ChEBI","id":"CHEBI:63528"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:47.024723+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38518117","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:30656"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38518117","source":"PubMed"}],"name":"dUMP + ATP = dUDP + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:30655"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:60471"},{"database":"ChEBI","id":"CHEBI:246422"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:47.024723+00:00.  

```json
{"citation":{"authors":["Hu Frisk J.","Wang L."],"citationCrossReferences":[{"database":"PubMed","id":"38518117"},{"database":"DOI","id":"10.1080/15257770.2024.2332410"}],"citationType":"journal article","firstPage":"1","id":"38518117","journal":"Nucleosides Nucleotides Nucleic Acids","lastPage":"9","publicationDate":"2024","title":"Molecular characterization of Drosophila melanogaster thymidylate kinase.","volume":"43"},"referenceNumber":6,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:26:49.964915+00:00.  

```text
DE   RecName: Full=Thymidylate kinase {ECO:0000303|PubMed:38518117};
DE            Short=DmTMPK {ECO:0000303|PubMed:38518117};
DE            EC=2.7.4.9 {ECO:0000269|PubMed:38518117};
DE   AltName: Full=Deoxythymidylate kinase {ECO:0000312|FlyBase:FBgn0034299};
```

Source SHA-256: `bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)  
**Locator:** `lines 99-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:26:49.964915+00:00.  

```text
RN   [6]
RP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=38518117; DOI=10.1080/15257770.2024.2332410;
RA   Hu Frisk J., Wang L.;
RT   "Molecular characterization of Drosophila melanogaster thymidylate
RT   kinase.";
RL   Nucleosides Nucleotides Nucleic Acids 43:1-9(2024).
```

Source SHA-256: `bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)  
**Locator:** `lines 113-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:26:49.964915+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=dTMP + ATP = dTDP + ADP; Xref=Rhea:RHEA:13517,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:58369, ChEBI:CHEBI:63528,
CC         ChEBI:CHEBI:456216; EC=2.7.4.9;
CC         Evidence={ECO:0000269|PubMed:38518117};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13518;
CC         Evidence={ECO:0000269|PubMed:38518117};
```

Source SHA-256: `bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)  
**Locator:** `lines 120-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:26:49.964915+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=dUMP + ATP = dUDP + ADP; Xref=Rhea:RHEA:30655,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:60471, ChEBI:CHEBI:246422,
CC         ChEBI:CHEBI:456216; Evidence={ECO:0000269|PubMed:38518117};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:30656;
CC         Evidence={ECO:0000269|PubMed:38518117};
```

Source SHA-256: `bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 157. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
