# catalytic_activity_0192

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)

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
A. 2-oxospirilloxanthin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = 2,2'-dioxospirilloxanthin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
B. (2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O
C. formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)
D. 6-O-methyldeacetylisoipecoside + H2O = 6-O-methyldeacetylisoipecoside aglycone + D-glucose
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

> The exact input sequence matches the UniProt entry for Pseudomonas aeruginosa glutathione-independent formaldehyde dehydrogenase. Its catalytic-activity annotation gives the reaction in choice C and cites experimental evidence (ECO:0000269); the cited literature includes a characterization study. This supports C for the supplied sequence, though the primary studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an enzyme that uses a nucleotide cofactor, but general sequence features do not establish that its specific substrate is formaldehyde rather than another substrate or reaction in the choices.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental identification linking this sequence to formaldehyde oxidation is needed to select C.


**Reason**

> The exact reaction is supported by reviewer-only annotation and cited experimental evidence, but that substrate-specific fact is absent from the question input. Inferring broad enzyme features from the sequence does not distinguish the precise reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports choice C; no supplied evidence makes another listed reaction a comparably defensible assignment.


### Important caveats

- The reviewer-only UniProt entry is sequence-matched, but the author's exact source snapshot is unknown.
- The UniProt catalytic-activity annotation cites experimental evidence; the cited primary papers were not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an enzyme that uses a nucleotide cofactor, but general sequence features do not establish that its specific substrate is formaldehyde rather than another substrate or reaction in the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification linking this sequence to formaldehyde oxidation is needed to select C.",
    "reason": "The exact reaction is supported by reviewer-only annotation and cited experimental evidence, but that substrate-specific fact is absent from the question input. Inferring broad enzyme features from the sequence does not distinguish the precise reaction."
  },
  "case_id": "catalytic_activity_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact input sequence matches the UniProt entry for Pseudomonas aeruginosa glutathione-independent formaldehyde dehydrogenase. Its catalytic-activity annotation gives the reaction in choice C and cites experimental evidence (ECO:0000269); the cited literature includes a characterization study. This supports C for the supplied sequence, though the primary studies were not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt entry is sequence-matched, but the author's exact source snapshot is unknown.",
    "The UniProt catalytic-activity annotation cites experimental evidence; the cited primary papers were not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports choice C; no supplied evidence makes another listed reaction a comparably defensible assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact input sequence matches the UniProt entry for Pseudomonas aeruginosa glutathione-independent formaldehyde dehydrogenase. Its catalytic-activity annotation gives the reaction in choice C and cites experimental evidence (ECO:0000269); the cited literature includes a characterization study. This supports C for the supplied sequence, though the primary studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an enzyme that uses a nucleotide cofactor, but general sequence features do not establish that its specific substrate is formaldehyde rather than another substrate or reaction in the choices.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification linking this sequence to formaldehyde oxidation is needed to select C.",
    "reason": "The exact reaction is supported by reviewer-only annotation and cited experimental evidence, but that substrate-specific fact is absent from the question input. Inferring broad enzyme features from the sequence does not distinguish the precise reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports choice C; no supplied evidence makes another listed reaction a comparably defensible assignment."
  },
  "important_caveats": [
    "The reviewer-only UniProt entry is sequence-matched, but the author's exact source snapshot is unknown.",
    "The UniProt catalytic-activity annotation cites experimental evidence; the cited primary papers were not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt P0DXZ0 (FALDH_PSEA8, 399 aa, Pseudomonas aeruginosa LESB58). The entry is annotated as Glutathione-independent formaldehyde dehydrogenase (EC 1.2.1.46) with the catalytic reaction 'formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)' supported by experimental evidence (ECO:0000269, PubMed:23989142 and PubMed:24125754), including X-ray crystallography (PDB 4JLW) in complex with NAD and zinc. The expected answer C matches this annotation exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains 'GPGK' (positions ~10-13), and additional motifs 'GAGPVG' and 'GIGIPGLYVT' appear later in the sequence. These are classic Rossmann-fold (GxGxxG) nucleotide-binding signatures characteristic of NAD(P)-dependent dehydrogenases. Among the four choices, only C (formaldehyde + NAD(+) + H2O → formate + NADH + 2H(+)) is an NAD-dependent oxidoreductase reaction. Choice A requires &#91;2Fe-2S&#93; ferredoxin (no iron-sulfur cluster motifs present), B is a lyase/dehydratase (no cofactor), and D is a glycosidase (hydrolase, no NAD). The Rossmann-fold recognition eliminates A, B, and D, leaving C as the only NAD-dependent dehydrogenase reaction.


**Missing item-specific fact**

> Specific substrate identity (formaldehyde vs. other aldehydes) cannot be determined from sequence motifs alone, but no competing NAD-dependent aldehyde dehydrogenase reaction is offered among the distractors, so the NAD-dependence argument suffices to select C.


**Reason**

> Recognizing the Rossmann fold as an NAD-binding motif is standard biochemistry knowledge. The logical chain—Rossmann fold → NAD-dependent dehydrogenase → eliminate non-NAD reactions—provides a concrete, general biological argument that meaningfully distinguishes C from A, B, and D without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C involves NAD+ as a cofactor. The other three options involve fundamentally different enzyme classes (ferredoxin-dependent oxidoreductase, lyase, glycosidase) that are inconsistent with the Rossmann-fold architecture evident in the sequence. No ambiguity in the correct answer among the given choices.


### Important caveats

- The UniProt entry P0DXZ0 was first published on 2025-04-09; the benchmark construction date is unknown. The historical archived version (entry v3, released 2026-01) already contains the full catalytic activity annotation.
- The enzyme also shows secondary activity toward acetaldehyde (EC not separately assigned), but this is not among the distractors.
- The sequence-match is exact (SHA-256 identical) between the benchmark input and both current and archived UniProt records.
- The identity of the protein as formaldehyde dehydrogenase specifically (vs. a general aldehyde dehydrogenase) relies on the specific substrate preference established experimentally, though the question's distractor set makes this distinction unnecessary for selecting C.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains 'GPGK' (positions ~10-13), and additional motifs 'GAGPVG' and 'GIGIPGLYVT' appear later in the sequence. These are classic Rossmann-fold (GxGxxG) nucleotide-binding signatures characteristic of NAD(P)-dependent dehydrogenases. Among the four choices, only C (formaldehyde + NAD(+) + H2O → formate + NADH + 2H(+)) is an NAD-dependent oxidoreductase reaction. Choice A requires [2Fe-2S] ferredoxin (no iron-sulfur cluster motifs present), B is a lyase/dehydratase (no cofactor), and D is a glycosidase (hydrolase, no NAD). The Rossmann-fold recognition eliminates A, B, and D, leaving C as the only NAD-dependent dehydrogenase reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Specific substrate identity (formaldehyde vs. other aldehydes) cannot be determined from sequence motifs alone, but no competing NAD-dependent aldehyde dehydrogenase reaction is offered among the distractors, so the NAD-dependence argument suffices to select C.",
    "reason": "Recognizing the Rossmann fold as an NAD-binding motif is standard biochemistry knowledge. The logical chain—Rossmann fold → NAD-dependent dehydrogenase → eliminate non-NAD reactions—provides a concrete, general biological argument that meaningfully distinguishes C from A, B, and D without requiring memorization of this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt P0DXZ0 (FALDH_PSEA8, 399 aa, Pseudomonas aeruginosa LESB58). The entry is annotated as Glutathione-independent formaldehyde dehydrogenase (EC 1.2.1.46) with the catalytic reaction 'formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)' supported by experimental evidence (ECO:0000269, PubMed:23989142 and PubMed:24125754), including X-ray crystallography (PDB 4JLW) in complex with NAD and zinc. The expected answer C matches this annotation exactly."
  },
  "important_caveats": [
    "The UniProt entry P0DXZ0 was first published on 2025-04-09; the benchmark construction date is unknown. The historical archived version (entry v3, released 2026-01) already contains the full catalytic activity annotation.",
    "The enzyme also shows secondary activity toward acetaldehyde (EC not separately assigned), but this is not among the distractors.",
    "The sequence-match is exact (SHA-256 identical) between the benchmark input and both current and archived UniProt records.",
    "The identity of the protein as formaldehyde dehydrogenase specifically (vs. a general aldehyde dehydrogenase) relies on the specific substrate preference established experimentally, though the question's distractor set makes this distinction unnecessary for selecting C."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C involves NAD+ as a cofactor. The other three options involve fundamentally different enzyme classes (ferredoxin-dependent oxidoreductase, lyase, glycosidase) that are inconsistent with the Rossmann-fold architecture evident in the sequence. No ambiguity in the correct answer among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt P0DXZ0 (FALDH_PSEA8, 399 aa, Pseudomonas aeruginosa LESB58). The entry is annotated as Glutathione-independent formaldehyde dehydrogenase (EC 1.2.1.46) with the catalytic reaction 'formaldehyde + NAD(+) + H2O = formate + NADH + 2 H(+)' supported by experimental evidence (ECO:0000269, PubMed:23989142 and PubMed:24125754), including X-ray crystallography (PDB 4JLW) in complex with NAD and zinc. The expected answer C matches this annotation exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "C8", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains 'GPGK' (positions ~10-13), and additional motifs 'GAGPVG' and 'GIGIPGLYVT' appear later in the sequence. These are classic Rossmann-fold (GxGxxG) nucleotide-binding signatures characteristic of NAD(P)-dependent dehydrogenases. Among the four choices, only C (formaldehyde + NAD(+) + H2O → formate + NADH + 2H(+)) is an NAD-dependent oxidoreductase reaction. Choice A requires [2Fe-2S] ferredoxin (no iron-sulfur cluster motifs present), B is a lyase/dehydratase (no cofactor), and D is a glycosidase (hydrolase, no NAD). The Rossmann-fold recognition eliminates A, B, and D, leaving C as the only NAD-dependent dehydrogenase reaction.",
    "missing_item_specific_fact": "Specific substrate identity (formaldehyde vs. other aldehydes) cannot be determined from sequence motifs alone, but no competing NAD-dependent aldehyde dehydrogenase reaction is offered among the distractors, so the NAD-dependence argument suffices to select C.",
    "reason": "Recognizing the Rossmann fold as an NAD-binding motif is standard biochemistry knowledge. The logical chain—Rossmann fold → NAD-dependent dehydrogenase → eliminate non-NAD reactions—provides a concrete, general biological argument that meaningfully distinguishes C from A, B, and D without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C involves NAD+ as a cofactor. The other three options involve fundamentally different enzyme classes (ferredoxin-dependent oxidoreductase, lyase, glycosidase) that are inconsistent with the Rossmann-fold architecture evident in the sequence. No ambiguity in the correct answer among the given choices."
  },
  "important_caveats": [
    "The UniProt entry P0DXZ0 was first published on 2025-04-09; the benchmark construction date is unknown. The historical archived version (entry v3, released 2026-01) already contains the full catalytic activity annotation.",
    "The enzyme also shows secondary activity toward acetaldehyde (EC not separately assigned), but this is not among the distractors.",
    "The sequence-match is exact (SHA-256 identical) between the benchmark input and both current and archived UniProt records.",
    "The identity of the protein as formaldehyde dehydrogenase specifically (vs. a general aldehyde dehydrogenase) relies on the specific substrate preference established experimentally, though the question's distractor set makes this distinction unnecessary for selecting C."
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

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:03.050160+00:00.  

```text
ID   FALDH_PSEA8             Reviewed;         399 AA.
AC   P0DXZ0;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=Glutathione-independent formaldehyde dehydrogenase {ECO:0000303|PubMed:24125754};
DE            Short=FALDH {ECO:0000305};
DE            Short=FDH {ECO:0000303|PubMed:24125754};
DE            EC=1.2.1.46 {ECO:0000269|PubMed:23989142, ECO:0000269|PubMed:24125754};
GN   Name=fdhA {ECO:0000312|EMBL:CAW30570.1};
GN   OrderedLocusNames=PLES_58161 {ECO:0000312|EMBL:CAW30570.1};
OS   Pseudomonas aeruginosa (strain LESB58).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.
OX   NCBI_TaxID=557722;
```

Source SHA-256: `f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e`.

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 192. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
