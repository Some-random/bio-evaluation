# EC_number_0067

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 1.14.15.9

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQTVTLSIFRFNEFEKRLWVLGQMTANKLGMHYLPKAKFWKMFGSGTGQGFTPKPNWHVWSILAVWPDEETARREVAESPIYQRWTKMADESYTVLLQPTSAWGKWDGKEPFEPVKPASDVRPIAALTRATVKFWKAERFWAREPAISHMIGRNKDVVFKIGVGEVPFVQQVTFSIWPDARSMEEFARGAGGPHGEAIKAVRAENWFKEELYARFQILGTIGKWEGKDPVGEALTARPSEAPKPAPAPAAAQPAPAAEAPKPAPAPVAEKPALAVEMPKPAEPPKPVVEAPKPASAPVASKPMPQGGKPNFKGKPGKGGRKENA

[Multiple Choices]
A. 1.14.14.126
B. 3.2.1.183
C. 1.14.15.9
D. 1.1.1.195
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

> The supplied sequence exactly matches a UniProt entry annotated as EC 1.14.15.9, spheroidene monooxygenase. The EC assignment and catalytic activity are transferred by similarity from UniProtKB:P17055 (ECO:0000250), so this supports the key as a database annotation but is not direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options span distinct enzyme classes, but the supplied sequence and prompt provide no substrate, reaction, organism, or functional annotation that identifies the enzyme's specific activity. Generic sequence reasoning does not establish which precise EC number applies.


**Missing item-specific fact**

> The protein-specific functional assignment that this sequence is a spheroidene monooxygenase catalyzing the annotated reaction(s), corresponding to EC 1.14.15.9.


**Reason**

> Distinguishing the keyed option requires recognizing or looking up this particular protein's function; that fact is absent from the model input. Reviewer-only sequence-matched annotations support the key but do not make the question answerable by reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct EC numbers, and the sequence-matched annotation supports C. The issue is missing functional information in the prompt, not evidence that multiple listed choices fit equally well.


### Important caveats

- The sequence match is exact, including in the historical UniProt record checked.
- The EC annotation for this entry is explicitly transferred by similarity from P17055; the supplied evidence does not independently establish direct experimental validation of this exact protein's EC assignment.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options span distinct enzyme classes, but the supplied sequence and prompt provide no substrate, reaction, organism, or functional annotation that identifies the enzyme's specific activity. Generic sequence reasoning does not establish which precise EC number applies.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that this sequence is a spheroidene monooxygenase catalyzing the annotated reaction(s), corresponding to EC 1.14.15.9.",
    "reason": "Distinguishing the keyed option requires recognizing or looking up this particular protein's function; that fact is absent from the model input. Reviewer-only sequence-matched annotations support the key but do not make the question answerable by reasoning from the supplied information."
  },
  "case_id": "EC_number_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated as EC 1.14.15.9, spheroidene monooxygenase. The EC assignment and catalytic activity are transferred by similarity from UniProtKB:P17055 (ECO:0000250), so this supports the key as a database annotation but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The sequence match is exact, including in the historical UniProt record checked.",
    "The EC annotation for this entry is explicitly transferred by similarity from P17055; the supplied evidence does not independently establish direct experimental validation of this exact protein's EC assignment.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct EC numbers, and the sequence-matched annotation supports C. The issue is missing functional information in the prompt, not evidence that multiple listed choices fit equally well."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated as EC 1.14.15.9, spheroidene monooxygenase. The EC assignment and catalytic activity are transferred by similarity from UniProtKB:P17055 (ECO:0000250), so this supports the key as a database annotation but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options span distinct enzyme classes, but the supplied sequence and prompt provide no substrate, reaction, organism, or functional annotation that identifies the enzyme's specific activity. Generic sequence reasoning does not establish which precise EC number applies.",
    "missing_item_specific_fact": "The protein-specific functional assignment that this sequence is a spheroidene monooxygenase catalyzing the annotated reaction(s), corresponding to EC 1.14.15.9.",
    "reason": "Distinguishing the keyed option requires recognizing or looking up this particular protein's function; that fact is absent from the model input. Reviewer-only sequence-matched annotations support the key but do not make the question answerable by reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct EC numbers, and the sequence-matched annotation supports C. The issue is missing functional information in the prompt, not evidence that multiple listed choices fit equally well."
  },
  "important_caveats": [
    "The sequence match is exact, including in the historical UniProt record checked.",
    "The EC annotation for this entry is explicitly transferred by similarity from P17055; the supplied evidence does not independently establish direct experimental validation of this exact protein's EC assignment.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q3J189 (CRTA_CERS4) exactly (324 AA, SHA256 confirmed). The entry is annotated as Spheroidene monooxygenase with EC 1.14.15.9. The EC assignment carries evidence code ECO:0000250 (similarity to P17055), but the enzyme's function, cofactor, and substrate specificity were experimentally characterized in Lee et al. 2010 (PubMed 20851979), which demonstrated spheroidene monooxygenase activity of CrtA in E. coli. Multiple catalytic reactions (Rhea:33027, 49328, 49332, 49336) are documented. The expected answer C (1.14.15.9) is scientifically supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can reasonably eliminate B (3.2.1.183, a glycosidase/hydrolase) because the sequence lacks recognizable glycosidase folds (TIM barrel, beta-propeller) and shows no catalytic residues typical of glycosidases. One can also argue against D (1.1.1.195, NAD+-dependent dehydrogenase) because no Rossmann-fold motif (GxGxxG) is apparent. However, distinguishing A (1.14.14.126, cytochrome P450 monooxygenase) from C (1.14.15.9, iron-sulfur protein-dependent monooxygenase) requires knowing the specific electron-donor system (ferredoxin vs. P450), and the 4th digit (specific substrate = spheroidene) is entirely protein-specific.


**Missing item-specific fact**

> The identity of this protein as CrtA (spheroidene monooxygenase) from Rhodobacter sphaeroides, its use of reduced ferredoxin &#91;2Fe-2S&#93; as electron donor (rather than cytochrome P450), and its specific substrate spheroidene. Without this annotation, the 3rd-digit distinction (14 vs 15) and the 4th-digit substrate specificity cannot be resolved from sequence alone.


**Reason**

> While broad enzyme-class elimination (hydrolase, dehydrogenase) is feasible from general sequence features, the critical distinction between EC 1.14.14.x (P450) and EC 1.14.15.x (iron-sulfur protein type) and the precise 4th-digit substrate assignment require knowing the specific enzyme identity and its experimentally determined cofactor system. This is an item-specific database/experimental fact not derivable by general biological reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the exact sequence match to a well-annotated Swiss-Prot entry with experimental characterization, the answer 1.14.15.9 is unambiguous. The distractors represent clearly different enzyme classes or subclasses. No other option is defensible for this specific protein.


### Important caveats

- The UniProt EC annotation uses ECO:0000250 (similarity-based inference from P17055), though the 2010 paper (PubMed 20851979) provides experimental characterization of CrtA's spheroidene monooxygenase activity.
- The sequence's C-terminal proline/alanine-rich region (residues ~240-324) is unusual and may reflect a low-complexity linker rather than a functional domain.
- The EC number 1.14.15.9 is a very specific 4-digit designation; even correct identification of the enzyme family would not yield the exact substrate-specific 4th digit without prior knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can reasonably eliminate B (3.2.1.183, a glycosidase/hydrolase) because the sequence lacks recognizable glycosidase folds (TIM barrel, beta-propeller) and shows no catalytic residues typical of glycosidases. One can also argue against D (1.1.1.195, NAD+-dependent dehydrogenase) because no Rossmann-fold motif (GxGxxG) is apparent. However, distinguishing A (1.14.14.126, cytochrome P450 monooxygenase) from C (1.14.15.9, iron-sulfur protein-dependent monooxygenase) requires knowing the specific electron-donor system (ferredoxin vs. P450), and the 4th digit (specific substrate = spheroidene) is entirely protein-specific.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of this protein as CrtA (spheroidene monooxygenase) from Rhodobacter sphaeroides, its use of reduced ferredoxin [2Fe-2S] as electron donor (rather than cytochrome P450), and its specific substrate spheroidene. Without this annotation, the 3rd-digit distinction (14 vs 15) and the 4th-digit substrate specificity cannot be resolved from sequence alone.",
    "reason": "While broad enzyme-class elimination (hydrolase, dehydrogenase) is feasible from general sequence features, the critical distinction between EC 1.14.14.x (P450) and EC 1.14.15.x (iron-sulfur protein type) and the precise 4th-digit substrate assignment require knowing the specific enzyme identity and its experimentally determined cofactor system. This is an item-specific database/experimental fact not derivable by general biological reasoning from the sequence."
  },
  "case_id": "EC_number_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q3J189 (CRTA_CERS4) exactly (324 AA, SHA256 confirmed). The entry is annotated as Spheroidene monooxygenase with EC 1.14.15.9. The EC assignment carries evidence code ECO:0000250 (similarity to P17055), but the enzyme's function, cofactor, and substrate specificity were experimentally characterized in Lee et al. 2010 (PubMed 20851979), which demonstrated spheroidene monooxygenase activity of CrtA in E. coli. Multiple catalytic reactions (Rhea:33027, 49328, 49332, 49336) are documented. The expected answer C (1.14.15.9) is scientifically supported."
  },
  "important_caveats": [
    "The UniProt EC annotation uses ECO:0000250 (similarity-based inference from P17055), though the 2010 paper (PubMed 20851979) provides experimental characterization of CrtA's spheroidene monooxygenase activity.",
    "The sequence's C-terminal proline/alanine-rich region (residues ~240-324) is unusual and may reflect a low-complexity linker rather than a functional domain.",
    "The EC number 1.14.15.9 is a very specific 4-digit designation; even correct identification of the enzyme family would not yield the exact substrate-specific 4th digit without prior knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the exact sequence match to a well-annotated Swiss-Prot entry with experimental characterization, the answer 1.14.15.9 is unambiguous. The distractors represent clearly different enzyme classes or subclasses. No other option is defensible for this specific protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q3J189 (CRTA_CERS4) exactly (324 AA, SHA256 confirmed). The entry is annotated as Spheroidene monooxygenase with EC 1.14.15.9. The EC assignment carries evidence code ECO:0000250 (similarity to P17055), but the enzyme's function, cofactor, and substrate specificity were experimentally characterized in Lee et al. 2010 (PubMed 20851979), which demonstrated spheroidene monooxygenase activity of CrtA in E. coli. Multiple catalytic reactions (Rhea:33027, 49328, 49332, 49336) are documented. The expected answer C (1.14.15.9) is scientifically supported.",
    "evidence_ids": ["C4", "C5", "C9", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can reasonably eliminate B (3.2.1.183, a glycosidase/hydrolase) because the sequence lacks recognizable glycosidase folds (TIM barrel, beta-propeller) and shows no catalytic residues typical of glycosidases. One can also argue against D (1.1.1.195, NAD+-dependent dehydrogenase) because no Rossmann-fold motif (GxGxxG) is apparent. However, distinguishing A (1.14.14.126, cytochrome P450 monooxygenase) from C (1.14.15.9, iron-sulfur protein-dependent monooxygenase) requires knowing the specific electron-donor system (ferredoxin vs. P450), and the 4th digit (specific substrate = spheroidene) is entirely protein-specific.",
    "missing_item_specific_fact": "The identity of this protein as CrtA (spheroidene monooxygenase) from Rhodobacter sphaeroides, its use of reduced ferredoxin [2Fe-2S] as electron donor (rather than cytochrome P450), and its specific substrate spheroidene. Without this annotation, the 3rd-digit distinction (14 vs 15) and the 4th-digit substrate specificity cannot be resolved from sequence alone.",
    "reason": "While broad enzyme-class elimination (hydrolase, dehydrogenase) is feasible from general sequence features, the critical distinction between EC 1.14.14.x (P450) and EC 1.14.15.x (iron-sulfur protein type) and the precise 4th-digit substrate assignment require knowing the specific enzyme identity and its experimentally determined cofactor system. This is an item-specific database/experimental fact not derivable by general biological reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the exact sequence match to a well-annotated Swiss-Prot entry with experimental characterization, the answer 1.14.15.9 is unambiguous. The distractors represent clearly different enzyme classes or subclasses. No other option is defensible for this specific protein."
  },
  "important_caveats": [
    "The UniProt EC annotation uses ECO:0000250 (similarity-based inference from P17055), though the 2010 paper (PubMed 20851979) provides experimental characterization of CrtA's spheroidene monooxygenase activity.",
    "The sequence's C-terminal proline/alanine-rich region (residues ~240-324) is unusual and may reflect a low-complexity linker rather than a functional domain.",
    "The EC number 1.14.15.9 is a very specific 4-digit designation; even correct identification of the enzyme family would not yield the exact substrate-specific 4th digit without prior knowledge."
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

**Accession:** `Q3J189` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.651114+00:00.  

```json
"Q3J189"
```

Source SHA-256: `bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.651114+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P17055","source":"UniProtKB"}],"value":"1.14.15.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20851979","source":"PubMed"}],"value":"Spheroidene monooxygenase"}}}
```

Source SHA-256: `bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.651114+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P17055","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:33028"}}],"reaction":{"ecNumber":"1.14.15.9","evidences":[{"evidenceCode":"ECO:0000250","id":"P17055","source":"UniProtKB"}],"name":"spheroidene + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = spheroiden-2-one + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:33027"},{"database":"Rhea","id":"RHEA-COMP:10000"},{"database":"Rhea","id":"RHEA-COMP:10001"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:33737"},{"database":"ChEBI","id":"CHEBI:33738"},{"database":"ChEBI","id":"CHEBI:35330"},{"database":"ChEBI","id":"CHEBI:62480"}]}}
```

Source SHA-256: `bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.651114+00:00.  

```json
{"citation":{"authors":["Lee P.C.","Holtzapple E.","Schmidt-Dannert C."],"citationCrossReferences":[{"database":"PubMed","id":"20851979"},{"database":"DOI","id":"10.1128/aem.01606-10"}],"citationType":"journal article","firstPage":"7328","id":"20851979","journal":"Appl. Environ. Microbiol.","lastPage":"7331","publicationDate":"2010","title":"Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA expressed in Escherichia coli.","volume":"76"},"referenceNumber":3,"referencePositions":["FUNCTION","COFACTOR","SUBSTRATE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:30:50.636898+00:00.  

```text
DE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:20851979};
DE            EC=1.14.15.9 {ECO:0000250|UniProtKB:P17055};
```

Source SHA-256: `f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)  
**Locator:** `lines 35-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:30:50.636898+00:00.  

```text
RN   [3]
RP   FUNCTION, COFACTOR, SUBSTRATE SPECIFICITY, AND BIOTECHNOLOGY.
RX   PubMed=20851979; DOI=10.1128/aem.01606-10;
RA   Lee P.C., Holtzapple E., Schmidt-Dannert C.;
RT   "Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA
RT   expressed in Escherichia coli.";
RL   Appl. Environ. Microbiol. 76:7328-7331(2010).
```

Source SHA-256: `f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)  
**Locator:** `lines 49-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:30:50.636898+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=spheroidene + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+)
CC         = spheroiden-2-one + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O;
CC         Xref=Rhea:RHEA:33027, Rhea:RHEA-COMP:10000, Rhea:RHEA-COMP:10001,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:35330,
CC         ChEBI:CHEBI:62480; EC=1.14.15.9;
CC         Evidence={ECO:0000250|UniProtKB:P17055};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33028;
CC         Evidence={ECO:0000250|UniProtKB:P17055};
```

Source SHA-256: `f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
