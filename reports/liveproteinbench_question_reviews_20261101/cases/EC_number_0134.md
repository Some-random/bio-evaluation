# EC_number_0134

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 1.14.13.238

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLTFKPLESYREDFSFRNSPAAIARFPFPFPEDQYMYSVNLEPAVSRDPGSVFEHQFDVDEHYVSEMAERARVLELDPGRCLVMPHMAQAAWDTLAMLMEHLARDYPQHFRLTRQGDAWHWQNLALGIDQRFTFGDPASLPCEPLEYITRQMQGDFAVLDQRDGDLFMDAGMVTCPADWSLRFDAGMSFKQWHSPVPMAHQMGVFDRALKYLLNIQVGAPVRRLNWTLTINPRLDTSPETYHEWGNDRGKVTPDNVGRLVHLRVELQLMARLPRSNALLFGIRTYLISLDELVSNPAWAQRLHRVMRDLPDPIADYKGITRYRQTLVDWLRRFDPEA

[Multiple Choices]
A. 1.14.14.126
B. 2.1.1.34
C. 1.14.13.238
D. 2.7.8.43
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

> The supplied sequence exactly matches the UniProt entry for this protein, which assigns EC 1.14.13.238 and links that assignment to experimental evidence and a specific catalytic reaction. This supports choice C; the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices span distinct enzyme classes, but the sequence and choices alone do not provide a concrete basis for identifying this protein's exact catalytic reaction and complete EC number.


**Missing item-specific fact**

> The protein-specific annotation or experimental evidence that this enzyme catalyzes oxidative N-demethylation of dimethylamine, corresponding to EC 1.14.13.238.


**Reason**

> Identifying the precise EC requires a protein-specific function or reaction fact not supplied in the question. General sequence reasoning does not establish the exact four-part EC classification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports choice C; the supplied evidence does not support another listed option.


### Important caveats

- The annotation attributes experimental evidence to PubMed 27851736, but that primary study was not independently validated here.
- The sequence match is exact; the source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices span distinct enzyme classes, but the sequence and choices alone do not provide a concrete basis for identifying this protein's exact catalytic reaction and complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or experimental evidence that this enzyme catalyzes oxidative N-demethylation of dimethylamine, corresponding to EC 1.14.13.238.",
    "reason": "Identifying the precise EC requires a protein-specific function or reaction fact not supplied in the question. General sequence reasoning does not establish the exact four-part EC classification."
  },
  "case_id": "EC_number_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein, which assigns EC 1.14.13.238 and links that assignment to experimental evidence and a specific catalytic reaction. This supports choice C; the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The annotation attributes experimental evidence to PubMed 27851736, but that primary study was not independently validated here.",
    "The sequence match is exact; the source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports choice C; the supplied evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein, which assigns EC 1.14.13.238 and links that assignment to experimental evidence and a specific catalytic reaction. This supports choice C; the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices span distinct enzyme classes, but the sequence and choices alone do not provide a concrete basis for identifying this protein's exact catalytic reaction and complete EC number.",
    "missing_item_specific_fact": "The protein-specific annotation or experimental evidence that this enzyme catalyzes oxidative N-demethylation of dimethylamine, corresponding to EC 1.14.13.238.",
    "reason": "Identifying the precise EC requires a protein-specific function or reaction fact not supplied in the question. General sequence reasoning does not establish the exact four-part EC classification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports choice C; the supplied evidence does not support another listed option."
  },
  "important_caveats": [
    "The annotation attributes experimental evidence to PubMed 27851736, but that primary study was not independently validated here.",
    "The sequence match is exact; the source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry A4XXY9 (sequence SHA256 matched, 338 AA) annotates EC 1.14.13.238 with evidence code ECO:0000269 (experimental) from PubMed:27851736 (Ortmayer et al., Nature 539:593-597, 2016). The annotation is supported by X-ray crystallography at 1.65 Å with heme B and dimethylamine complexes (PDB: 5LTE, 5LTH, 5LTI), catalytic activity assays, and mutagenesis studies. The catalytic reaction (dimethylamine + NADPH + O2 + H+ → methylamine + formaldehyde + NADP+ + H2O) is experimentally confirmed. This is a genuine experimental annotation, not computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could partially narrow the EC class by recognizing the sequence lacks P450-specific motifs (the conserved FxxGxxxCxG with Cys as axial heme ligand characteristic of EC 1.14.14.x), potentially distinguishing 1.14.13 (NADPH-dependent non-P450 heme monooxygenase) from 1.14.14 (P450). Eliminating transferases (B: 2.1.1.34, D: 2.7.8.43) is conceivable if oxidoreductase-like features are recognized. However, the specific 4th digit (238 vs 126) encodes the particular substrate (dimethylamine) and reaction mechanism, which cannot be derived from general biological reasoning applied to the sequence alone.


**Missing item-specific fact**

> The specific substrate specificity (dimethylamine N-demethylation) and the assignment of serial number 238 by IUBMB. Distinguishing 1.14.13.238 from 1.14.14.126 at the 4th-digit level requires knowing this is the HODM alpha subunit acting on dimethylamine, which is a protein-specific experimental finding not inferable from sequence motifs alone.


**Reason**

> While partial reasoning might eliminate transferases (EC 2.x) and potentially distinguish 1.14.13 from 1.14.14 via heme-ligand motif inspection, the complete 4-digit EC number—especially the 4th digit '238'—is an IUBMB-assigned identifier for a specific substrate-reaction pair (dimethylamine oxidative N-demethylation). No general biological principle maps a 338-aa sequence to the serial number 238. Selection of the correct option fundamentally depends on recognizing this protein's specific identity or its annotated function, which is a database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence unambiguously supports EC 1.14.13.238. Options B (methyltransferase) and D (phosphotransferase) are entirely different enzyme classes. Option A (P450, 1.14.14.126) differs in mechanism and heme coordination. The experimental crystallographic and biochemical evidence clearly establishes C as correct.


### Important caveats

- The EC annotation is based on experimental evidence (ECO:0000269) including X-ray crystallography and enzyme assays, not merely computational prediction or similarity transfer.
- The entry was first publicly released on 2025-02-05, meaning this protein's function was characterized relatively recently (2016 Nature paper), which may affect training-data availability for models.
- The sequence is 338 amino acids and contains a PAS domain repurposed as an enzyme domain—a rare and notable finding that makes motif-based classification less straightforward.
- The 4th EC digit (238) is an IUBMB-assigned serial number with no algorithmic derivation from sequence features; it encodes a specific chemical reaction identity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could partially narrow the EC class by recognizing the sequence lacks P450-specific motifs (the conserved FxxGxxxCxG with Cys as axial heme ligand characteristic of EC 1.14.14.x), potentially distinguishing 1.14.13 (NADPH-dependent non-P450 heme monooxygenase) from 1.14.14 (P450). Eliminating transferases (B: 2.1.1.34, D: 2.7.8.43) is conceivable if oxidoreductase-like features are recognized. However, the specific 4th digit (238 vs 126) encodes the particular substrate (dimethylamine) and reaction mechanism, which cannot be derived from general biological reasoning applied to the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity (dimethylamine N-demethylation) and the assignment of serial number 238 by IUBMB. Distinguishing 1.14.13.238 from 1.14.14.126 at the 4th-digit level requires knowing this is the HODM alpha subunit acting on dimethylamine, which is a protein-specific experimental finding not inferable from sequence motifs alone.",
    "reason": "While partial reasoning might eliminate transferases (EC 2.x) and potentially distinguish 1.14.13 from 1.14.14 via heme-ligand motif inspection, the complete 4-digit EC number—especially the 4th digit '238'—is an IUBMB-assigned identifier for a specific substrate-reaction pair (dimethylamine oxidative N-demethylation). No general biological principle maps a 338-aa sequence to the serial number 238. Selection of the correct option fundamentally depends on recognizing this protein's specific identity or its annotated function, which is a database lookup."
  },
  "case_id": "EC_number_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry A4XXY9 (sequence SHA256 matched, 338 AA) annotates EC 1.14.13.238 with evidence code ECO:0000269 (experimental) from PubMed:27851736 (Ortmayer et al., Nature 539:593-597, 2016). The annotation is supported by X-ray crystallography at 1.65 Å with heme B and dimethylamine complexes (PDB: 5LTE, 5LTH, 5LTI), catalytic activity assays, and mutagenesis studies. The catalytic reaction (dimethylamine + NADPH + O2 + H+ → methylamine + formaldehyde + NADP+ + H2O) is experimentally confirmed. This is a genuine experimental annotation, not computational inference."
  },
  "important_caveats": [
    "The EC annotation is based on experimental evidence (ECO:0000269) including X-ray crystallography and enzyme assays, not merely computational prediction or similarity transfer.",
    "The entry was first publicly released on 2025-02-05, meaning this protein's function was characterized relatively recently (2016 Nature paper), which may affect training-data availability for models.",
    "The sequence is 338 amino acids and contains a PAS domain repurposed as an enzyme domain—a rare and notable finding that makes motif-based classification less straightforward.",
    "The 4th EC digit (238) is an IUBMB-assigned serial number with no algorithmic derivation from sequence features; it encodes a specific chemical reaction identity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence unambiguously supports EC 1.14.13.238. Options B (methyltransferase) and D (phosphotransferase) are entirely different enzyme classes. Option A (P450, 1.14.14.126) differs in mechanism and heme coordination. The experimental crystallographic and biochemical evidence clearly establishes C as correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry A4XXY9 (sequence SHA256 matched, 338 AA) annotates EC 1.14.13.238 with evidence code ECO:0000269 (experimental) from PubMed:27851736 (Ortmayer et al., Nature 539:593-597, 2016). The annotation is supported by X-ray crystallography at 1.65 Å with heme B and dimethylamine complexes (PDB: 5LTE, 5LTH, 5LTI), catalytic activity assays, and mutagenesis studies. The catalytic reaction (dimethylamine + NADPH + O2 + H+ → methylamine + formaldehyde + NADP+ + H2O) is experimentally confirmed. This is a genuine experimental annotation, not computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could partially narrow the EC class by recognizing the sequence lacks P450-specific motifs (the conserved FxxGxxxCxG with Cys as axial heme ligand characteristic of EC 1.14.14.x), potentially distinguishing 1.14.13 (NADPH-dependent non-P450 heme monooxygenase) from 1.14.14 (P450). Eliminating transferases (B: 2.1.1.34, D: 2.7.8.43) is conceivable if oxidoreductase-like features are recognized. However, the specific 4th digit (238 vs 126) encodes the particular substrate (dimethylamine) and reaction mechanism, which cannot be derived from general biological reasoning applied to the sequence alone.",
    "missing_item_specific_fact": "The specific substrate specificity (dimethylamine N-demethylation) and the assignment of serial number 238 by IUBMB. Distinguishing 1.14.13.238 from 1.14.14.126 at the 4th-digit level requires knowing this is the HODM alpha subunit acting on dimethylamine, which is a protein-specific experimental finding not inferable from sequence motifs alone.",
    "reason": "While partial reasoning might eliminate transferases (EC 2.x) and potentially distinguish 1.14.13 from 1.14.14 via heme-ligand motif inspection, the complete 4-digit EC number—especially the 4th digit '238'—is an IUBMB-assigned identifier for a specific substrate-reaction pair (dimethylamine oxidative N-demethylation). No general biological principle maps a 338-aa sequence to the serial number 238. Selection of the correct option fundamentally depends on recognizing this protein's specific identity or its annotated function, which is a database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence unambiguously supports EC 1.14.13.238. Options B (methyltransferase) and D (phosphotransferase) are entirely different enzyme classes. Option A (P450, 1.14.14.126) differs in mechanism and heme coordination. The experimental crystallographic and biochemical evidence clearly establishes C as correct."
  },
  "important_caveats": [
    "The EC annotation is based on experimental evidence (ECO:0000269) including X-ray crystallography and enzyme assays, not merely computational prediction or similarity transfer.",
    "The entry was first publicly released on 2025-02-05, meaning this protein's function was characterized relatively recently (2016 Nature paper), which may affect training-data availability for models.",
    "The sequence is 338 amino acids and contains a PAS domain repurposed as an enzyme domain—a rare and notable finding that makes motif-based classification less straightforward.",
    "The 4th EC digit (238) is an IUBMB-assigned serial number with no algorithmic derivation from sequence features; it encodes a specific chemical reaction identity."
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

**Accession:** `A4XXY9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.391884+00:00.  

```json
"A4XXY9"
```

Source SHA-256: `65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.391884+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27851736","source":"PubMed"}],"value":"1.14.13.238"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27851736","source":"PubMed"}],"value":"Heme-dependent oxidative N-demethylase alpha subunit"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27851736","source":"PubMed"}],"value":"HODM alpha subunit"}]}}
```

Source SHA-256: `65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.391884+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"27851736","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:54829"}}],"reaction":{"ecNumber":"1.14.13.238","evidences":[{"evidenceCode":"ECO:0000269","id":"27851736","source":"PubMed"}],"name":"dimethylamine + NADPH + O2 + H(+) = methylamine + formaldehyde + NADP(+) + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:54828"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16842"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58040"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:59338"}]}}
```

Source SHA-256: `65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.391884+00:00.  

```json
{"citation":{"authors":["Ortmayer M.","Lafite P.","Menon B.R.","Tralau T.","Fisher K.","Denkhaus L.","Scrutton N.S.","Rigby S.E.","Munro A.W.","Hay S.","Leys D."],"citationCrossReferences":[{"database":"PubMed","id":"27851736"},{"database":"DOI","id":"10.1038/nature20159"}],"citationType":"journal article","firstPage":"593","id":"27851736","journal":"Nature","lastPage":"597","publicationDate":"2016","title":"An oxidative N-demethylase reveals PAS transition from ubiquitous sensor to enzyme.","volume":"539"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5LTE","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5LTH","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5LTI","source":"PDB"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.65 ANGSTROMS) IN COMPLEXES WITH HEME B AND DIMETHYLAMINE","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN","MUTAGENESIS OF TRP-180; ARG-224 AND GLU-266"]}
```

Source SHA-256: `65d3c1576347e504fed534849c54776f620bd7f146082e8f553e0f17d025fbba`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-01T06:27:45.629873+00:00.  

```text
DE   RecName: Full=Heme-dependent oxidative N-demethylase alpha subunit {ECO:0000303|PubMed:27851736};
DE            Short=HODM alpha subunit {ECO:0000303|PubMed:27851736};
DE            EC=1.14.13.238 {ECO:0000269|PubMed:27851736};
```

Source SHA-256: `89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)  
**Locator:** `lines 24-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-01T06:27:45.629873+00:00.  

```text
RN   [2] {ECO:0007744|PDB:5LTE, ECO:0007744|PDB:5LTH, ECO:0007744|PDB:5LTI}
RP   X-RAY CRYSTALLOGRAPHY (1.65 ANGSTROMS) IN COMPLEXES WITH HEME B AND
RP   DIMETHYLAMINE, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES,
RP   SUBUNIT, DOMAIN, AND MUTAGENESIS OF TRP-180; ARG-224 AND GLU-266.
RX   PubMed=27851736; DOI=10.1038/nature20159;
RA   Ortmayer M., Lafite P., Menon B.R., Tralau T., Fisher K., Denkhaus L.,
RA   Scrutton N.S., Rigby S.E., Munro A.W., Hay S., Leys D.;
RT   "An oxidative N-demethylase reveals PAS transition from ubiquitous sensor
RT   to enzyme.";
RL   Nature 539:593-597(2016).
```

Source SHA-256: `89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY9?format=txt&versions=74)  
**Locator:** `lines 41-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-01T06:27:45.629873+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=dimethylamine + NADPH + O2 + H(+) = methylamine + formaldehyde
CC         + NADP(+) + H2O; Xref=Rhea:RHEA:54828, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:16842,
CC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58040, ChEBI:CHEBI:58349,
CC         ChEBI:CHEBI:59338; EC=1.14.13.238;
CC         Evidence={ECO:0000269|PubMed:27851736};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:54829;
CC         Evidence={ECO:0000305|PubMed:27851736};
```

Source SHA-256: `89b08a06f96b1f3860d8b7d5d12c92348e7bae650952f557ad480f020fea1521`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
