# EC_number_0058

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.2.1.46

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGNRGVVYLGPGKVEVQNIPYPKMQDPQGRQIDHGVILRVVSTNICGSDQHMVRGRTTAPEGLVLGHEITGEVVEIGRGVETMKIGDLVSVPFNVACGHCRTCKEQHTGVCLTVNPARAGGAYGYVDMGGWVGGQAEYVLVPYADFNLLKLPNREAAMEKIRDLTCLSDILPTGYHGAVTAGVGPGSTVYIAGAGPVGLAAAASARLLGAAVVIVGDVNPTRLAHAKKQGFEIADLSKDTPLHEQIAALLGEPEVDCAVDAVGFEARGHGHSGSQQEAPATVLNSLMGITRVAGKIGIPGLYVTEDPGAVDAAAKHGALSIRFGLGWAKSHSFHTGQTPVMKYNRQLMQAIMWDRIKIADIVGVEVITLDDAPKGYGEFDAGVPKKFVIDPHNLFRAA

[Multiple Choices]
A. 1.2.1.46
B. 1.1.1.336
C. 4.2.99.18
D. 3.4.21.90
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

> The exact 399-aa sequence matches the Pseudomonas aeruginosa LESB58 entry, which assigns EC 1.2.1.46 and describes formaldehyde oxidation to formate. The annotation cites experimental evidence (ECO:0000269), though the underlying papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support identifying an enzyme family, but the choices include two oxidoreductases, and general sequence reasoning does not establish which substrate-specific EC number applies.


**Missing item-specific fact**

> The protein-specific catalytic activity and its formaldehyde substrate assignment, established by annotation or experimental characterization.


**Reason**

> The input supplies only the sequence and candidate EC numbers. Distinguishing the exact EC requires protein-specific functional information not given in the question; recognizing the sequence from a database would be lookup, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports A for the assigned formaldehyde dehydrogenase EC. The reported acetaldehyde activity does not match another listed option.


### Important caveats

- The sequence match and functional annotations are reviewer-only evidence, not information supplied to the evaluated model.
- The annotation cites experimental evidence, but the primary studies were not independently validated here; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support identifying an enzyme family, but the choices include two oxidoreductases, and general sequence reasoning does not establish which substrate-specific EC number applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity and its formaldehyde substrate assignment, established by annotation or experimental characterization.",
    "reason": "The input supplies only the sequence and candidate EC numbers. Distinguishing the exact EC requires protein-specific functional information not given in the question; recognizing the sequence from a database would be lookup, not reasoning from supplied context."
  },
  "case_id": "EC_number_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact 399-aa sequence matches the Pseudomonas aeruginosa LESB58 entry, which assigns EC 1.2.1.46 and describes formaldehyde oxidation to formate. The annotation cites experimental evidence (ECO:0000269), though the underlying papers were not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match and functional annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The annotation cites experimental evidence, but the primary studies were not independently validated here; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports A for the assigned formaldehyde dehydrogenase EC. The reported acetaldehyde activity does not match another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 399-aa sequence matches the Pseudomonas aeruginosa LESB58 entry, which assigns EC 1.2.1.46 and describes formaldehyde oxidation to formate. The annotation cites experimental evidence (ECO:0000269), though the underlying papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support identifying an enzyme family, but the choices include two oxidoreductases, and general sequence reasoning does not establish which substrate-specific EC number applies.",
    "missing_item_specific_fact": "The protein-specific catalytic activity and its formaldehyde substrate assignment, established by annotation or experimental characterization.",
    "reason": "The input supplies only the sequence and candidate EC numbers. Distinguishing the exact EC requires protein-specific functional information not given in the question; recognizing the sequence from a database would be lookup, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports A for the assigned formaldehyde dehydrogenase EC. The reported acetaldehyde activity does not match another listed option."
  },
  "important_caveats": [
    "The sequence match and functional annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The annotation cites experimental evidence, but the primary studies were not independently validated here; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXZ0 (sequence SHA256 matched) is annotated as Glutathione-independent formaldehyde dehydrogenase with EC 1.2.1.46, supported by experimental evidence codes ECO:0000269 from PubMed:23989142 (X-ray crystallography of NAD complex, PDB 4JLW) and PubMed:24125754 (expression, purification, and enzymatic characterization). The catalytic activity (formaldehyde + NAD+ + H2O = formate + NADH + 2H+) is experimentally confirmed. The expected answer A (1.2.1.46) is directly supported by these experimental annotations.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable Rossmann-fold NAD-binding motifs (e.g., 'GPGKVEVQN', 'GDLVSVPFNVACGHCRTC', 'GPGSTVYIAGAGPVGL'), indicating an NAD-dependent oxidoreductase and effectively ruling out D (serine protease, 3.4.21.90, which would require a GDSGG catalytic triad) and C (lyase, 4.2.99.18). The presence of a cysteine-rich region ('ACGHCRTC') with multiple cysteines and a histidine is characteristic of the catalytic zinc/cysteine site of aldehyde dehydrogenases (EC 1.2.x.x), where a catalytic cysteine nucleophile attacks the aldehyde substrate. This contrasts with alcohol dehydrogenases (EC 1.1.1.x), which typically use a zinc-dependent mechanism with catalytic serine/tyrosine and lack this specific cysteine cluster. This narrows the choice to A (1.2.1.46) over B (1.1.1.336). The specific 4th digit is resolved by the fact that only one 1.2.1.x option is offered.


**Missing item-specific fact**

> The exact substrate specificity (formaldehyde vs. acetaldehyde vs. other aldehydes) that defines the 4th digit '46' as glutathione-independent formaldehyde dehydrogenase cannot be determined from sequence alone; however, since only one 1.2.1.x option is presented, the 4th-digit identification is effectively supplied by the answer set.


**Reason**

> A trained biologist can identify NAD-binding Rossmann motifs to classify the enzyme as an oxidoreductase, recognize the cysteine/histidine catalytic signature as more consistent with aldehyde dehydrogenase (EC 1.2) than alcohol dehydrogenase (EC 1.1), and eliminate the protease and lyase options. The remaining ambiguity in the 4th digit is resolved by the single 1.2.1.x option. This constitutes a defensible multi-step reasoning path from sequence features to the correct choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (1, 3, 4), and within class 1 they differ at the second digit (1.1 vs 1.2). The sequence features (Rossmann fold, catalytic cysteine cluster, absence of protease triad or lyase motifs) provide a clear reasoning path that eliminates B, C, and D, leaving A as the only defensible choice.


### Important caveats

- The specific identification of EC 1.2.1.46 (vs. other 1.2.1.x aldehyde dehydrogenases) from sequence alone is not possible; the question is made tractable by offering only one 1.2.1.x option.
- The protein also shows secondary activity on acetaldehyde (EC 1.2.1.22-like), but the primary annotated activity is formaldehyde oxidation.
- The UniProt entry was first public in April 2025; the author's source snapshot is unknown, though the sequence matches at all checked versions.
- The reasoning relies on recognizing specialized aldehyde dehydrogenase sequence signatures (catalytic cysteine in context of Rossmann fold), which is graduate-level enzymology knowledge but does not require memorizing this specific protein's database entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable Rossmann-fold NAD-binding motifs (e.g., 'GPGKVEVQN', 'GDLVSVPFNVACGHCRTC', 'GPGSTVYIAGAGPVGL'), indicating an NAD-dependent oxidoreductase and effectively ruling out D (serine protease, 3.4.21.90, which would require a GDSGG catalytic triad) and C (lyase, 4.2.99.18). The presence of a cysteine-rich region ('ACGHCRTC') with multiple cysteines and a histidine is characteristic of the catalytic zinc/cysteine site of aldehyde dehydrogenases (EC 1.2.x.x), where a catalytic cysteine nucleophile attacks the aldehyde substrate. This contrasts with alcohol dehydrogenases (EC 1.1.1.x), which typically use a zinc-dependent mechanism with catalytic serine/tyrosine and lack this specific cysteine cluster. This narrows the choice to A (1.2.1.46) over B (1.1.1.336). The specific 4th digit is resolved by the fact that only one 1.2.1.x option is offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate specificity (formaldehyde vs. acetaldehyde vs. other aldehydes) that defines the 4th digit '46' as glutathione-independent formaldehyde dehydrogenase cannot be determined from sequence alone; however, since only one 1.2.1.x option is presented, the 4th-digit identification is effectively supplied by the answer set.",
    "reason": "A trained biologist can identify NAD-binding Rossmann motifs to classify the enzyme as an oxidoreductase, recognize the cysteine/histidine catalytic signature as more consistent with aldehyde dehydrogenase (EC 1.2) than alcohol dehydrogenase (EC 1.1), and eliminate the protease and lyase options. The remaining ambiguity in the 4th digit is resolved by the single 1.2.1.x option. This constitutes a defensible multi-step reasoning path from sequence features to the correct choice."
  },
  "case_id": "EC_number_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ0 (sequence SHA256 matched) is annotated as Glutathione-independent formaldehyde dehydrogenase with EC 1.2.1.46, supported by experimental evidence codes ECO:0000269 from PubMed:23989142 (X-ray crystallography of NAD complex, PDB 4JLW) and PubMed:24125754 (expression, purification, and enzymatic characterization). The catalytic activity (formaldehyde + NAD+ + H2O = formate + NADH + 2H+) is experimentally confirmed. The expected answer A (1.2.1.46) is directly supported by these experimental annotations."
  },
  "important_caveats": [
    "The specific identification of EC 1.2.1.46 (vs. other 1.2.1.x aldehyde dehydrogenases) from sequence alone is not possible; the question is made tractable by offering only one 1.2.1.x option.",
    "The protein also shows secondary activity on acetaldehyde (EC 1.2.1.22-like), but the primary annotated activity is formaldehyde oxidation.",
    "The UniProt entry was first public in April 2025; the author's source snapshot is unknown, though the sequence matches at all checked versions.",
    "The reasoning relies on recognizing specialized aldehyde dehydrogenase sequence signatures (catalytic cysteine in context of Rossmann fold), which is graduate-level enzymology knowledge but does not require memorizing this specific protein's database entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (1, 3, 4), and within class 1 they differ at the second digit (1.1 vs 1.2). The sequence features (Rossmann fold, catalytic cysteine cluster, absence of protease triad or lyase motifs) provide a clear reasoning path that eliminates B, C, and D, leaving A as the only defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ0 (sequence SHA256 matched) is annotated as Glutathione-independent formaldehyde dehydrogenase with EC 1.2.1.46, supported by experimental evidence codes ECO:0000269 from PubMed:23989142 (X-ray crystallography of NAD complex, PDB 4JLW) and PubMed:24125754 (expression, purification, and enzymatic characterization). The catalytic activity (formaldehyde + NAD+ + H2O = formate + NADH + 2H+) is experimentally confirmed. The expected answer A (1.2.1.46) is directly supported by these experimental annotations.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable Rossmann-fold NAD-binding motifs (e.g., 'GPGKVEVQN', 'GDLVSVPFNVACGHCRTC', 'GPGSTVYIAGAGPVGL'), indicating an NAD-dependent oxidoreductase and effectively ruling out D (serine protease, 3.4.21.90, which would require a GDSGG catalytic triad) and C (lyase, 4.2.99.18). The presence of a cysteine-rich region ('ACGHCRTC') with multiple cysteines and a histidine is characteristic of the catalytic zinc/cysteine site of aldehyde dehydrogenases (EC 1.2.x.x), where a catalytic cysteine nucleophile attacks the aldehyde substrate. This contrasts with alcohol dehydrogenases (EC 1.1.1.x), which typically use a zinc-dependent mechanism with catalytic serine/tyrosine and lack this specific cysteine cluster. This narrows the choice to A (1.2.1.46) over B (1.1.1.336). The specific 4th digit is resolved by the fact that only one 1.2.1.x option is offered.",
    "missing_item_specific_fact": "The exact substrate specificity (formaldehyde vs. acetaldehyde vs. other aldehydes) that defines the 4th digit '46' as glutathione-independent formaldehyde dehydrogenase cannot be determined from sequence alone; however, since only one 1.2.1.x option is presented, the 4th-digit identification is effectively supplied by the answer set.",
    "reason": "A trained biologist can identify NAD-binding Rossmann motifs to classify the enzyme as an oxidoreductase, recognize the cysteine/histidine catalytic signature as more consistent with aldehyde dehydrogenase (EC 1.2) than alcohol dehydrogenase (EC 1.1), and eliminate the protease and lyase options. The remaining ambiguity in the 4th digit is resolved by the single 1.2.1.x option. This constitutes a defensible multi-step reasoning path from sequence features to the correct choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (1, 3, 4), and within class 1 they differ at the second digit (1.1 vs 1.2). The sequence features (Rossmann fold, catalytic cysteine cluster, absence of protease triad or lyase motifs) provide a clear reasoning path that eliminates B, C, and D, leaving A as the only defensible choice."
  },
  "important_caveats": [
    "The specific identification of EC 1.2.1.46 (vs. other 1.2.1.x aldehyde dehydrogenases) from sequence alone is not possible; the question is made tractable by offering only one 1.2.1.x option.",
    "The protein also shows secondary activity on acetaldehyde (EC 1.2.1.22-like), but the primary annotated activity is formaldehyde oxidation.",
    "The UniProt entry was first public in April 2025; the author's source snapshot is unknown, though the sequence matches at all checked versions.",
    "The reasoning relies on recognizing specialized aldehyde dehydrogenase sequence signatures (catalytic cysteine in context of Rossmann fold), which is graduate-level enzymology knowledge but does not require memorizing this specific protein's database entry."
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

**Accession:** `P0DXZ0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.597114+00:00.  

```json
"P0DXZ0"
```

Source SHA-256: `8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.597114+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23989142","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24125754","source":"PubMed"}],"value":"1.2.1.46"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24125754","source":"PubMed"}],"value":"Glutathione-independent formaldehyde dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"FALDH"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"24125754","source":"PubMed"}],"value":"FDH"}]}}
```

Source SHA-256: `8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.597114+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.2.1.46","evidences":[{"evidenceCode":"ECO:0000269","id":"23989142","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24125754","source":"PubMed"}],"name":"formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:16425"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15740"},{"database":"ChEBI","id":"CHEBI:16842"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"}]}}
```

Source SHA-256: `8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.597114+00:00.  

```json
{"citation":{"authors":["Zhang W.","Chen S.","Liao Y.","Wang D.","Ding J.","Wang Y.","Ran X.","Lu D.","Zhu H."],"citationCrossReferences":[{"database":"PubMed","id":"24125754"},{"database":"DOI","id":"10.1016/j.pep.2013.09.017"}],"citationType":"journal article","firstPage":"208","id":"24125754","journal":"Protein Expr. Purif.","lastPage":"213","publicationDate":"2013","title":"Expression, purification, and characterization of formaldehyde dehydrogenase from Pseudomonas aeruginosa.","volume":"92"},"referenceComments":[{"type":"STRAIN","value":"LESB58"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.597114+00:00.  

```json
{"citation":{"authors":["Liao Y.","Chen S.","Wang D.","Zhang W.","Wang S.","Ding J.","Wang Y.","Cai L.","Ran X.","Wang X.","Zhu H."],"citationCrossReferences":[{"database":"PubMed","id":"23989142"},{"database":"DOI","id":"10.1107/s174430911302160x"}],"citationType":"journal article","firstPage":"967","id":"23989142","journal":"Acta Crystallogr. F","lastPage":"972","publicationDate":"2013","title":"Structure of formaldehyde dehydrogenase from Pseudomonas aeruginosa: the binary complex with the cofactor NAD+.","volume":"69"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4JLW","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"LESB58"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) IN COMPLEX WITH NAD AND ZINC","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:03.050160+00:00.  

```text
DE   RecName: Full=Glutathione-independent formaldehyde dehydrogenase {ECO:0000303|PubMed:24125754};
DE            Short=FALDH {ECO:0000305};
DE            Short=FDH {ECO:0000303|PubMed:24125754};
DE            EC=1.2.1.46 {ECO:0000269|PubMed:23989142, ECO:0000269|PubMed:24125754};
```

Source SHA-256: `f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)  
**Locator:** `lines 28-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:03.050160+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.
RC   STRAIN=LESB58;
RX   PubMed=24125754; DOI=10.1016/j.pep.2013.09.017;
RA   Zhang W., Chen S., Liao Y., Wang D., Ding J., Wang Y., Ran X., Lu D.,
RA   Zhu H.;
RT   "Expression, purification, and characterization of formaldehyde
RT   dehydrogenase from Pseudomonas aeruginosa.";
RL   Protein Expr. Purif. 92:208-213(2013).
```

Source SHA-256: `f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)  
**Locator:** `lines 37-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:03.050160+00:00.  

```text
RN   [3] {ECO:0007744|PDB:4JLW}
RP   X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) IN COMPLEX WITH NAD AND ZINC,
RP   CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.
RC   STRAIN=LESB58;
RX   PubMed=23989142; DOI=10.1107/s174430911302160x;
RA   Liao Y., Chen S., Wang D., Zhang W., Wang S., Ding J., Wang Y., Cai L.,
RA   Ran X., Wang X., Zhu H.;
RT   "Structure of formaldehyde dehydrogenase from Pseudomonas aeruginosa: the
RT   binary complex with the cofactor NAD+.";
RL   Acta Crystallogr. F 69:967-972(2013).
```

Source SHA-256: `f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)  
**Locator:** `lines 51-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:03.050160+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+);
CC         Xref=Rhea:RHEA:16425, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:15740, ChEBI:CHEBI:16842, ChEBI:CHEBI:57540,
CC         ChEBI:CHEBI:57945; EC=1.2.1.46;
CC         Evidence={ECO:0000269|PubMed:23989142, ECO:0000269|PubMed:24125754};
```

Source SHA-256: `f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 58. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
