# EC_number_0056

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 5.1.1.24

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDGKVQVLDFIKINPAGNITILIDNFDIYDKNIPKLSEEIMKETNLYAEQVGFIKEKHLQMMGGEFCGNASRSFASLLAFRDKDFSEQKNYSITCSGESEVLDVDVRTDGAKNKFLAKIKMPKFISLEEISIDEYKLGLVRFSGISHFIFNIKENKETSFENIIDLVKKYLSNEDYSAFGIMFFDKDNLSMKPYVYVKELESGIYENSCASGTTALGYYLKKYKNLDRAKVVQPNGWLEYIIENDEMYIDGPVEIVAEGKVYI

[Multiple Choices]
A. 5.1.1.24
B. 5.1.1.25
C. 4.3.3.9
D. 5.3.1.16
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

> The exact sequence matches the UniProt entry annotated as histidine racemase, EC 5.1.1.24. The entry links that EC number and the L-histidine = D-histidine reaction to experimental evidence (ECO:0000269) and a 2024 publication.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include different reaction classes, so identifying a racemase could narrow the options. But the supplied sequence and choices do not provide a sufficiently specific biological basis to establish histidine racemase activity or distinguish the exact EC number.


**Missing item-specific fact**

> The protein-specific function and substrate specificity: that this sequence catalyzes L-histidine/D-histidine racemization.


**Reason**

> The supported key depends on an item-specific functional assignment that is absent from the input; recognizing the sequence from an external database would be lookup, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation and cited catalytic reaction support choice A; the supplied reviewer evidence does not support another listed option.


### Important caveats

- The sequence match and experimental-evidence attribution come from reviewer-only database excerpts, not information supplied to the evaluated model.
- The referenced primary paper was not independently retrieved or validated here; the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include different reaction classes, so identifying a racemase could narrow the options. But the supplied sequence and choices do not provide a sufficiently specific biological basis to establish histidine racemase activity or distinguish the exact EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific function and substrate specificity: that this sequence catalyzes L-histidine/D-histidine racemization.",
    "reason": "The supported key depends on an item-specific functional assignment that is absent from the input; recognizing the sequence from an external database would be lookup, not reasoning from the supplied evidence."
  },
  "case_id": "EC_number_0056",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as histidine racemase, EC 5.1.1.24. The entry links that EC number and the L-histidine = D-histidine reaction to experimental evidence (ECO:0000269) and a 2024 publication."
  },
  "important_caveats": [
    "The sequence match and experimental-evidence attribution come from reviewer-only database excerpts, not information supplied to the evaluated model.",
    "The referenced primary paper was not independently retrieved or validated here; the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and cited catalytic reaction support choice A; the supplied reviewer evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as histidine racemase, EC 5.1.1.24. The entry links that EC number and the L-histidine = D-histidine reaction to experimental evidence (ECO:0000269) and a 2024 publication.",
    "evidence_ids": ["C4", "C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include different reaction classes, so identifying a racemase could narrow the options. But the supplied sequence and choices do not provide a sufficiently specific biological basis to establish histidine racemase activity or distinguish the exact EC number.",
    "missing_item_specific_fact": "The protein-specific function and substrate specificity: that this sequence catalyzes L-histidine/D-histidine racemization.",
    "reason": "The supported key depends on an item-specific functional assignment that is absent from the input; recognizing the sequence from an external database would be lookup, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and cited catalytic reaction support choice A; the supplied reviewer evidence does not support another listed option."
  },
  "important_caveats": [
    "The sequence match and experimental-evidence attribution come from reviewer-only database excerpts, not information supplied to the evaluated model.",
    "The referenced primary paper was not independently retrieved or validated here; the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry D5RFM4 (HISR_FUSN2) is annotated as Histidine racemase with EC 5.1.1.24, supported by experimental evidence (ECO:0000269) from PubMed:39424140 (Lamer et al., J. Biol. Chem. 2024). The catalytic activity is explicitly stated as L-histidine = D-histidine (Rhea:RHEA:59188). The supplied sequence matches the UniProt sequence exactly (SHA256 confirmed). The annotation is based on a 2024 experimental characterization paper, not mere computational inference.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could reason that the absence of canonical PLP-binding motifs might suggest a cofactor-independent enzyme, and the overall size/fold might hint at a racemase/isomerase class (5.x) rather than a lyase (4.x). However, distinguishing EC 5.1.1.24 (histidine racemase) from EC 5.1.1.25 (another amino acid racemase) requires knowing the specific amino acid substrate, which cannot be reliably inferred from sequence alone for a newly characterized enzyme. The distinction between racemase (5.1.1.x) and intramolecular oxidoreductase (5.3.1.x) also depends on the specific reaction mechanism, not obvious from primary sequence.


**Missing item-specific fact**

> The specific substrate identity (histidine) and the cofactor-independent mechanism of this enzyme, established only by the 2024 experimental characterization (Lamer et al., JBC 300:107896). The EC 5.1.1.24 assignment is a database annotation derived from that experimental work, not a computationally derivable property from the 263-aa sequence.


**Reason**

> This enzyme was characterized experimentally in 2024 and integrated into Swiss-Prot in April 2025. The specific EC number 5.1.1.24 depends on knowing the substrate is histidine and the mechanism is cofactor-independent racemization. No general sequence motif or fold-level reasoning reliably distinguishes histidine racemase from other amino acid racemases (5.1.1.24 vs 5.1.1.25) or from an intramolecular oxidoreductase (5.3.1.16). Selection of the correct answer effectively requires recalling the specific database annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the exact sequence and the experimental evidence, EC 5.1.1.24 is the only correct assignment. The distractors (5.1.1.25, 4.3.3.9, 5.3.1.16) represent different reaction types or substrates that are not supported by the experimental data. There is no ambiguity in the correct answer itself, though the question is difficult to answer by reasoning alone.


### Important caveats

- The EC 5.1.1.24 annotation carries evidence code ECO:0000269 (experimental evidence from PubMed:39424140, published 2024), making this a well-supported experimental assignment rather than a computational prediction.
- The protein was first integrated into Swiss-Prot on 2025-04-09; the author's source snapshot date is unknown, so the benchmark may have been constructed from TrEMBL or a pre-annotation source.
- The sequence is 263 aa and lacks obvious PLP-binding motifs, consistent with the described cofactor-independent mechanism, but this absence alone does not uniquely identify the substrate as histidine.
- The identity of the protein was inferred from dataset image-path metadata (reviewer-only); this accession was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could reason that the absence of canonical PLP-binding motifs might suggest a cofactor-independent enzyme, and the overall size/fold might hint at a racemase/isomerase class (5.x) rather than a lyase (4.x). However, distinguishing EC 5.1.1.24 (histidine racemase) from EC 5.1.1.25 (another amino acid racemase) requires knowing the specific amino acid substrate, which cannot be reliably inferred from sequence alone for a newly characterized enzyme. The distinction between racemase (5.1.1.x) and intramolecular oxidoreductase (5.3.1.x) also depends on the specific reaction mechanism, not obvious from primary sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (histidine) and the cofactor-independent mechanism of this enzyme, established only by the 2024 experimental characterization (Lamer et al., JBC 300:107896). The EC 5.1.1.24 assignment is a database annotation derived from that experimental work, not a computationally derivable property from the 263-aa sequence.",
    "reason": "This enzyme was characterized experimentally in 2024 and integrated into Swiss-Prot in April 2025. The specific EC number 5.1.1.24 depends on knowing the substrate is histidine and the mechanism is cofactor-independent racemization. No general sequence motif or fold-level reasoning reliably distinguishes histidine racemase from other amino acid racemases (5.1.1.24 vs 5.1.1.25) or from an intramolecular oxidoreductase (5.3.1.16). Selection of the correct answer effectively requires recalling the specific database annotation for this protein."
  },
  "case_id": "EC_number_0056",
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
    "reason": "UniProt entry D5RFM4 (HISR_FUSN2) is annotated as Histidine racemase with EC 5.1.1.24, supported by experimental evidence (ECO:0000269) from PubMed:39424140 (Lamer et al., J. Biol. Chem. 2024). The catalytic activity is explicitly stated as L-histidine = D-histidine (Rhea:RHEA:59188). The supplied sequence matches the UniProt sequence exactly (SHA256 confirmed). The annotation is based on a 2024 experimental characterization paper, not mere computational inference."
  },
  "important_caveats": [
    "The EC 5.1.1.24 annotation carries evidence code ECO:0000269 (experimental evidence from PubMed:39424140, published 2024), making this a well-supported experimental assignment rather than a computational prediction.",
    "The protein was first integrated into Swiss-Prot on 2025-04-09; the author's source snapshot date is unknown, so the benchmark may have been constructed from TrEMBL or a pre-annotation source.",
    "The sequence is 263 aa and lacks obvious PLP-binding motifs, consistent with the described cofactor-independent mechanism, but this absence alone does not uniquely identify the substrate as histidine.",
    "The identity of the protein was inferred from dataset image-path metadata (reviewer-only); this accession was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the exact sequence and the experimental evidence, EC 5.1.1.24 is the only correct assignment. The distractors (5.1.1.25, 4.3.3.9, 5.3.1.16) represent different reaction types or substrates that are not supported by the experimental data. There is no ambiguity in the correct answer itself, though the question is difficult to answer by reasoning alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry D5RFM4 (HISR_FUSN2) is annotated as Histidine racemase with EC 5.1.1.24, supported by experimental evidence (ECO:0000269) from PubMed:39424140 (Lamer et al., J. Biol. Chem. 2024). The catalytic activity is explicitly stated as L-histidine = D-histidine (Rhea:RHEA:59188). The supplied sequence matches the UniProt sequence exactly (SHA256 confirmed). The annotation is based on a 2024 experimental characterization paper, not mere computational inference.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could reason that the absence of canonical PLP-binding motifs might suggest a cofactor-independent enzyme, and the overall size/fold might hint at a racemase/isomerase class (5.x) rather than a lyase (4.x). However, distinguishing EC 5.1.1.24 (histidine racemase) from EC 5.1.1.25 (another amino acid racemase) requires knowing the specific amino acid substrate, which cannot be reliably inferred from sequence alone for a newly characterized enzyme. The distinction between racemase (5.1.1.x) and intramolecular oxidoreductase (5.3.1.x) also depends on the specific reaction mechanism, not obvious from primary sequence.",
    "missing_item_specific_fact": "The specific substrate identity (histidine) and the cofactor-independent mechanism of this enzyme, established only by the 2024 experimental characterization (Lamer et al., JBC 300:107896). The EC 5.1.1.24 assignment is a database annotation derived from that experimental work, not a computationally derivable property from the 263-aa sequence.",
    "reason": "This enzyme was characterized experimentally in 2024 and integrated into Swiss-Prot in April 2025. The specific EC number 5.1.1.24 depends on knowing the substrate is histidine and the mechanism is cofactor-independent racemization. No general sequence motif or fold-level reasoning reliably distinguishes histidine racemase from other amino acid racemases (5.1.1.24 vs 5.1.1.25) or from an intramolecular oxidoreductase (5.3.1.16). Selection of the correct answer effectively requires recalling the specific database annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the exact sequence and the experimental evidence, EC 5.1.1.24 is the only correct assignment. The distractors (5.1.1.25, 4.3.3.9, 5.3.1.16) represent different reaction types or substrates that are not supported by the experimental data. There is no ambiguity in the correct answer itself, though the question is difficult to answer by reasoning alone."
  },
  "important_caveats": [
    "The EC 5.1.1.24 annotation carries evidence code ECO:0000269 (experimental evidence from PubMed:39424140, published 2024), making this a well-supported experimental assignment rather than a computational prediction.",
    "The protein was first integrated into Swiss-Prot on 2025-04-09; the author's source snapshot date is unknown, so the benchmark may have been constructed from TrEMBL or a pre-annotation source.",
    "The sequence is 263 aa and lacks obvious PLP-binding motifs, consistent with the described cofactor-independent mechanism, but this absence alone does not uniquely identify the substrate as histidine.",
    "The identity of the protein was inferred from dataset image-path metadata (reviewer-only); this accession was not provided to the evaluated model."
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

**Accession:** `D5RFM4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:49.723120+00:00.  

```json
"D5RFM4"
```

Source SHA-256: `9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:49.723120+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39424140","source":"PubMed"}],"value":"5.1.1.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39424140","source":"PubMed"}],"value":"Histidine racemase"}}}
```

Source SHA-256: `9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:49.723120+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.1.1.24","evidences":[{"evidenceCode":"ECO:0000269","id":"39424140","source":"PubMed"}],"name":"L-histidine = D-histidine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:59188"},{"database":"ChEBI","id":"CHEBI:57595"},{"database":"ChEBI","id":"CHEBI:142967"}]}}
```

Source SHA-256: `9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D5RFM4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:49.723120+00:00.  

```json
{"citation":{"authors":["Lamer T.","Chen P.","Venter M.J.","van Belkum M.J.","Wijewardane A.","Wu C.","Lemieux M.J.","Vederas J.C."],"citationCrossReferences":[{"database":"PubMed","id":"39424140"},{"database":"DOI","id":"10.1016/j.jbc.2024.107896"}],"citationType":"journal article","firstPage":"107896","id":"39424140","journal":"J. Biol. Chem.","lastPage":"107896","publicationDate":"2024","title":"Discovery, characterization, and structure of a cofactor-independent histidine racemase from the oral pathogen Fusobacterium nucleatum.","volume":"300"},"referenceComments":[{"type":"STRAIN","value":"ATCC 23726 / VPI 4351"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `9d534f1baac31e4cc070d3002eca79de8e3da489ec484522b9820ff39ad10ecd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:27:51.450216+00:00.  

```text
ID   HISR_FUSN2              Reviewed;         263 AA.
AC   D5RFM4;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-JUL-2010, sequence version 1.
DT   28-JAN-2026, entry version 32.
DE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};
DE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};
GN   Name=hisR {ECO:0000303|PubMed:39424140};
GN   ORFNames=HMPREF0397_2009 {ECO:0000312|EMBL:EFG94488.1};
OS   Fusobacterium nucleatum subsp. nucleatum (strain ATCC 23726 / VPI 4351).
OC   Bacteria; Fusobacteriati; Fusobacteriota; Fusobacteriia; Fusobacteriales;
OC   Fusobacteriaceae; Fusobacterium.
OX   NCBI_TaxID=525283;
```

Source SHA-256: `b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:27:51.450216+00:00.  

```text
DE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};
DE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};
```

Source SHA-256: `b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)  
**Locator:** `lines 28-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:27:51.450216+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND DISRUPTION
RP   PHENOTYPE.
RC   STRAIN=ATCC 23726 / VPI 4351;
RX   PubMed=39424140; DOI=10.1016/j.jbc.2024.107896;
RA   Lamer T., Chen P., Venter M.J., van Belkum M.J., Wijewardane A., Wu C.,
RA   Lemieux M.J., Vederas J.C.;
RT   "Discovery, characterization, and structure of a cofactor-independent
RT   histidine racemase from the oral pathogen Fusobacterium nucleatum.";
RL   J. Biol. Chem. 300:107896-107896(2024).
```

Source SHA-256: `b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D5RFM4?format=txt&versions=32)  
**Locator:** `lines 42-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-02T04:27:51.450216+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-histidine = D-histidine; Xref=Rhea:RHEA:59188,
CC         ChEBI:CHEBI:57595, ChEBI:CHEBI:142967; EC=5.1.1.24;
CC         Evidence={ECO:0000269|PubMed:39424140};
```

Source SHA-256: `b43d619ca52111b53572f98986c14dc86b988a025a0364b36dd5b2547453e3cc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 56. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
