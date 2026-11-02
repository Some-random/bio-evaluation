# EC_number_0030

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.7.11.24

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAEFIRAQIFGTTFEITSRYTDLQPVGMGAFGLVCSAKDQLTGQPVAIKKIMKPFSTPVLSKRTYRELKLLKHLKHENVISLSDIFISPLEDIYFVTELLGTDLHRLLTSRPLEKQFIQYFLYQILRGLKYVHSAGVIHRDLKPSNILVNENCDLKICDFGLARIQDPQMTGYVSTRYYRAPEIMLTWQKYDVEVDIWSAGCIFAEMLEGKPLFPGKDHVNQFSIITELLGSPPEDVIHTICSENTLRFVQSLPKRERIPLSQKFKNADPAAVDLLERMLVFDPKKRISAAQALAHEYLAPYHDPSDEPVAAEKFDWSFNDADLPVDTWKIMMYSEILDYHNVDQNDTPL

[Multiple Choices]
A. 2.7.11.1
B. 3.5.2.6
C. 2.3.1.322
D. 2.7.11.24
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

> The exact sequence matches a UniProt entry annotated as MAP kinase HOG1 with EC 2.7.11.24. The catalytic-activity annotations are consistent with serine/threonine protein phosphorylation, but their evidence is transferred by similarity from UniProtKB:P32485 (ECO:0000250), not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a protein-kinase catalytic domain, including the HRD and DFG motifs, and a T-x-Y activation-loop motif characteristic of MAP kinases. That provides a biological basis for choosing the MAP-kinase EC option D over the broader serine/threonine kinase option A; options B and C are inconsistent with this kinase-domain evidence.


**Missing item-specific fact**

> No external identity fact is strictly necessary for a defensible class-level choice, though certainty about this particular protein's MAPK subtype and its assigned EC would benefit from annotation or experimental evidence.


**Reason**

> The sequence contains recognizable kinase and MAPK-subfamily features that meaningfully distinguish the offered MAP kinase classification. The reviewer-only database annotation supports the key but is not being treated as information supplied to the original model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A is a broader serine/threonine kinase classification, but the MAPK-like sequence features favor the more specific MAP kinase EC 2.7.11.24 when a complete EC number is requested.


### Important caveats

- The matched UniProt annotation and catalytic-activity records assign EC 2.7.11.24 by similarity to another entry; they do not establish direct experimental characterization of this exact protein.
- The historical UniProt record available by the stated cutoff also matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a protein-kinase catalytic domain, including the HRD and DFG motifs, and a T-x-Y activation-loop motif characteristic of MAP kinases. That provides a biological basis for choosing the MAP-kinase EC option D over the broader serine/threonine kinase option A; options B and C are inconsistent with this kinase-domain evidence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external identity fact is strictly necessary for a defensible class-level choice, though certainty about this particular protein's MAPK subtype and its assigned EC would benefit from annotation or experimental evidence.",
    "reason": "The sequence contains recognizable kinase and MAPK-subfamily features that meaningfully distinguish the offered MAP kinase classification. The reviewer-only database annotation supports the key but is not being treated as information supplied to the original model."
  },
  "case_id": "EC_number_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as MAP kinase HOG1 with EC 2.7.11.24. The catalytic-activity annotations are consistent with serine/threonine protein phosphorylation, but their evidence is transferred by similarity from UniProtKB:P32485 (ECO:0000250), not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The matched UniProt annotation and catalytic-activity records assign EC 2.7.11.24 by similarity to another entry; they do not establish direct experimental characterization of this exact protein.",
    "The historical UniProt record available by the stated cutoff also matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is a broader serine/threonine kinase classification, but the MAPK-like sequence features favor the more specific MAP kinase EC 2.7.11.24 when a complete EC number is requested."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as MAP kinase HOG1 with EC 2.7.11.24. The catalytic-activity annotations are consistent with serine/threonine protein phosphorylation, but their evidence is transferred by similarity from UniProtKB:P32485 (ECO:0000250), not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a protein-kinase catalytic domain, including the HRD and DFG motifs, and a T-x-Y activation-loop motif characteristic of MAP kinases. That provides a biological basis for choosing the MAP-kinase EC option D over the broader serine/threonine kinase option A; options B and C are inconsistent with this kinase-domain evidence.",
    "missing_item_specific_fact": "No external identity fact is strictly necessary for a defensible class-level choice, though certainty about this particular protein's MAPK subtype and its assigned EC would benefit from annotation or experimental evidence.",
    "reason": "The sequence contains recognizable kinase and MAPK-subfamily features that meaningfully distinguish the offered MAP kinase classification. The reviewer-only database annotation supports the key but is not being treated as information supplied to the original model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A is a broader serine/threonine kinase classification, but the MAPK-like sequence features favor the more specific MAP kinase EC 2.7.11.24 when a complete EC number is requested."
  },
  "important_caveats": [
    "The matched UniProt annotation and catalytic-activity records assign EC 2.7.11.24 by similarity to another entry; they do not establish direct experimental characterization of this exact protein.",
    "The historical UniProt record available by the stated cutoff also matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G1XJZ4 (HOG1_ARTOA) is annotated with EC=2.7.11.24 (MAP kinase) with sequence match confirmed. The annotation is based on similarity to S. cerevisiae HOG1 (P32485, ECO:0000250), which is a computational inference rather than direct experimental evidence for this specific protein. However, the sequence-level kinase motifs (VAIK, HRD, DFG, APE) and the TGY activation-loop motif are consistent with MAP kinase classification. The EC number 2.7.11.24 is supported by the annotation and is consistent with the sequence features.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical protein kinase motifs (glycine-rich loop GAFGLVCS, VAIK motif, HRD motif 'HRDLKPSN', DFG motif 'DFGLARI', APE motif 'APEIMLTW'), which immediately eliminates B (3.5.2.6, a hydrolase) and C (2.3.1.322, an acetyltransferase) since neither is a kinase. The critical discrimination is between A (2.7.11.1, PKA) and D (2.7.11.24, MAP kinase). Between the DFG and APE motifs, the activation loop contains a T-G-Y motif ('...DFGLARIQDPQMTGYVSTRYYRAPE...'), which is the hallmark TXY phosphorylation motif of MAP kinases (p38, ERK, JNK, HOG1). PKA lacks this TXY architecture and instead has a distinct activation-loop conformation. The overall domain architecture, insertion lengths, and the specific glycine-rich loop sequence ('GAFGLVCS' vs PKA's 'GTGSFGRV') further distinguish this from PKA.


**Missing item-specific fact**

> None critical. The TXY motif is a textbook MAP kinase signature recognizable from general biochemistry knowledge.


**Reason**

> A biologist familiar with kinase classification can: (1) identify the protein as a kinase from VAIK/HRD/DFG/APE motifs, eliminating B and C; (2) recognize the TGY motif in the activation loop as diagnostic of MAP kinases (EC 2.7.11.24) rather than PKA (EC 2.7.11.1). This is a concrete, general-knowledge-based argument not dependent on memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The TGY motif and overall kinase architecture clearly favor MAP kinase (D) over PKA (A). Choices B and C are non-kinase EC numbers trivially eliminated by recognizing kinase motifs. No ambiguity among the four options.


### Important caveats

- The EC annotation for G1XJZ4 is based on similarity to P32485 (S. cerevisiae HOG1) via ECO:0000250, not direct experimental characterization of this specific protein.
- The TXY motif argument is strong but relies on the model recognizing this specific motif pattern; a model unfamiliar with kinase subfamily signatures might struggle between A and D.
- The reviewer-only evidence confirms sequence match and annotation but was not available to the evaluated model.
- The entry was first publicly released 2025-06-18; the author source snapshot is unknown but the sequence has not changed since 2011.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs (glycine-rich loop GAFGLVCS, VAIK motif, HRD motif 'HRDLKPSN', DFG motif 'DFGLARI', APE motif 'APEIMLTW'), which immediately eliminates B (3.5.2.6, a hydrolase) and C (2.3.1.322, an acetyltransferase) since neither is a kinase. The critical discrimination is between A (2.7.11.1, PKA) and D (2.7.11.24, MAP kinase). Between the DFG and APE motifs, the activation loop contains a T-G-Y motif ('...DFGLARIQDPQMTGYVSTRYYRAPE...'), which is the hallmark TXY phosphorylation motif of MAP kinases (p38, ERK, JNK, HOG1). PKA lacks this TXY architecture and instead has a distinct activation-loop conformation. The overall domain architecture, insertion lengths, and the specific glycine-rich loop sequence ('GAFGLVCS' vs PKA's 'GTGSFGRV') further distinguish this from PKA.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The TXY motif is a textbook MAP kinase signature recognizable from general biochemistry knowledge.",
    "reason": "A biologist familiar with kinase classification can: (1) identify the protein as a kinase from VAIK/HRD/DFG/APE motifs, eliminating B and C; (2) recognize the TGY motif in the activation loop as diagnostic of MAP kinases (EC 2.7.11.24) rather than PKA (EC 2.7.11.1). This is a concrete, general-knowledge-based argument not dependent on memorizing this specific protein's database entry."
  },
  "case_id": "EC_number_0030",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G1XJZ4 (HOG1_ARTOA) is annotated with EC=2.7.11.24 (MAP kinase) with sequence match confirmed. The annotation is based on similarity to S. cerevisiae HOG1 (P32485, ECO:0000250), which is a computational inference rather than direct experimental evidence for this specific protein. However, the sequence-level kinase motifs (VAIK, HRD, DFG, APE) and the TGY activation-loop motif are consistent with MAP kinase classification. The EC number 2.7.11.24 is supported by the annotation and is consistent with the sequence features."
  },
  "important_caveats": [
    "The EC annotation for G1XJZ4 is based on similarity to P32485 (S. cerevisiae HOG1) via ECO:0000250, not direct experimental characterization of this specific protein.",
    "The TXY motif argument is strong but relies on the model recognizing this specific motif pattern; a model unfamiliar with kinase subfamily signatures might struggle between A and D.",
    "The reviewer-only evidence confirms sequence match and annotation but was not available to the evaluated model.",
    "The entry was first publicly released 2025-06-18; the author source snapshot is unknown but the sequence has not changed since 2011."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The TGY motif and overall kinase architecture clearly favor MAP kinase (D) over PKA (A). Choices B and C are non-kinase EC numbers trivially eliminated by recognizing kinase motifs. No ambiguity among the four options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0030",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G1XJZ4 (HOG1_ARTOA) is annotated with EC=2.7.11.24 (MAP kinase) with sequence match confirmed. The annotation is based on similarity to S. cerevisiae HOG1 (P32485, ECO:0000250), which is a computational inference rather than direct experimental evidence for this specific protein. However, the sequence-level kinase motifs (VAIK, HRD, DFG, APE) and the TGY activation-loop motif are consistent with MAP kinase classification. The EC number 2.7.11.24 is supported by the annotation and is consistent with the sequence features.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs (glycine-rich loop GAFGLVCS, VAIK motif, HRD motif 'HRDLKPSN', DFG motif 'DFGLARI', APE motif 'APEIMLTW'), which immediately eliminates B (3.5.2.6, a hydrolase) and C (2.3.1.322, an acetyltransferase) since neither is a kinase. The critical discrimination is between A (2.7.11.1, PKA) and D (2.7.11.24, MAP kinase). Between the DFG and APE motifs, the activation loop contains a T-G-Y motif ('...DFGLARIQDPQMTGYVSTRYYRAPE...'), which is the hallmark TXY phosphorylation motif of MAP kinases (p38, ERK, JNK, HOG1). PKA lacks this TXY architecture and instead has a distinct activation-loop conformation. The overall domain architecture, insertion lengths, and the specific glycine-rich loop sequence ('GAFGLVCS' vs PKA's 'GTGSFGRV') further distinguish this from PKA.",
    "missing_item_specific_fact": "None critical. The TXY motif is a textbook MAP kinase signature recognizable from general biochemistry knowledge.",
    "reason": "A biologist familiar with kinase classification can: (1) identify the protein as a kinase from VAIK/HRD/DFG/APE motifs, eliminating B and C; (2) recognize the TGY motif in the activation loop as diagnostic of MAP kinases (EC 2.7.11.24) rather than PKA (EC 2.7.11.1). This is a concrete, general-knowledge-based argument not dependent on memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The TGY motif and overall kinase architecture clearly favor MAP kinase (D) over PKA (A). Choices B and C are non-kinase EC numbers trivially eliminated by recognizing kinase motifs. No ambiguity among the four options."
  },
  "important_caveats": [
    "The EC annotation for G1XJZ4 is based on similarity to P32485 (S. cerevisiae HOG1) via ECO:0000250, not direct experimental characterization of this specific protein.",
    "The TXY motif argument is strong but relies on the model recognizing this specific motif pattern; a model unfamiliar with kinase subfamily signatures might struggle between A and D.",
    "The reviewer-only evidence confirms sequence match and annotation but was not available to the evaluated model.",
    "The entry was first publicly released 2025-06-18; the author source snapshot is unknown but the sequence has not changed since 2011."
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

**Accession:** `G1XJZ4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 75. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.162410+00:00.  

```json
"G1XJZ4"
```

Source SHA-256: `f5b753e70271d02ae2ec5247fd47012239dae51babd7c3bfee2e3ab06ec877a6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.162410+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"value":"2.7.11.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38331317","source":"PubMed"}],"value":"Mitogen-activated protein kinase HOG1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38331317","source":"PubMed"}],"value":"MAP kinase HOG1"}]}}
```

Source SHA-256: `f5b753e70271d02ae2ec5247fd47012239dae51babd7c3bfee2e3ab06ec877a6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.162410+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:17990"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `f5b753e70271d02ae2ec5247fd47012239dae51babd7c3bfee2e3ab06ec877a6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:06.162410+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:46609"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `f5b753e70271d02ae2ec5247fd47012239dae51babd7c3bfee2e3ab06ec877a6`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ4?format=txt&versions=75)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-01T06:28:00.750098+00:00.  

```text
DE   RecName: Full=Mitogen-activated protein kinase HOG1 {ECO:0000303|PubMed:38331317};
DE            Short=MAP kinase HOG1 {ECO:0000303|PubMed:38331317};
DE            EC=2.7.11.24 {ECO:0000250|UniProtKB:P32485};
```

Source SHA-256: `1dbfbafd92615ed42a2463236664f6723834d2affbd80a5568b72ba7335909ca`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ4?format=txt&versions=75)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-01T06:28:00.750098+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:17990;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
```

Source SHA-256: `1dbfbafd92615ed42a2463236664f6723834d2affbd80a5568b72ba7335909ca`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ4?format=txt&versions=75)  
**Locator:** `lines 50-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-01T06:28:00.750098+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:46609;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
```

Source SHA-256: `1dbfbafd92615ed42a2463236664f6723834d2affbd80a5568b72ba7335909ca`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 30. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
