# EC_number_0170

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.1.1.29

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAIKLIVGLANPGAEYAATRHNAGAWYVDLLAERLRAPLREEPKFFGYTSRITLEGEDVRLLVPTTFMNLSGKAVGAMASFYRIQPDEILVAHDELDLPPGVAKFKLGGGHGGHNGLKDIISKLGNNPNFHRLRVGIGHPGDKNKVVGFVLGKPPVSEQKLIDEAIDEAARCTELWFKEGLAKATSRLHTFKAQ

[Multiple Choices]
A. 3.1.1.80
B. 3.1.1.29
C. 2.3.2.27
D. 1.1.1.12
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

> The exact sequence matches a UniProt entry annotated as peptidyl-tRNA hydrolase, EC 3.1.1.29, by a HAMAP rule. The entry also records a specific catalytic reaction with PubMed-based experimental evidence. This supports choice B, while the HAMAP EC annotation itself is computational rather than direct experimental proof of the full classification.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a compact enzyme, but the supplied sequence and context do not provide a sufficiently specific biological clue to distinguish peptidyl-tRNA hydrolysis from the reactions represented by the other EC choices.


**Missing item-specific fact**

> The protein-specific identification as peptidyl-tRNA hydrolase, or equivalent evidence of its substrate and catalytic activity, is absent from the input.


**Reason**

> Selecting B requires identifying the sequence's particular enzyme family or knowing its specific function; generic sequence-based enzyme reasoning does not establish this EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports the keyed EC number, and the choices specify distinct classifications.


### Important caveats

- The sequence match and EC annotation are established in reviewer-only database evidence, not information available to the evaluated model.
- The UniProt EC assignment is attributed to a computational HAMAP rule; the entry separately reports PubMed-supported catalytic activity.
- The exact source snapshot used by the benchmark author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a compact enzyme, but the supplied sequence and context do not provide a sufficiently specific biological clue to distinguish peptidyl-tRNA hydrolysis from the reactions represented by the other EC choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as peptidyl-tRNA hydrolase, or equivalent evidence of its substrate and catalytic activity, is absent from the input.",
    "reason": "Selecting B requires identifying the sequence's particular enzyme family or knowing its specific function; generic sequence-based enzyme reasoning does not establish this EC number."
  },
  "case_id": "EC_number_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C6",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as peptidyl-tRNA hydrolase, EC 3.1.1.29, by a HAMAP rule. The entry also records a specific catalytic reaction with PubMed-based experimental evidence. This supports choice B, while the HAMAP EC annotation itself is computational rather than direct experimental proof of the full classification."
  },
  "important_caveats": [
    "The sequence match and EC annotation are established in reviewer-only database evidence, not information available to the evaluated model.",
    "The UniProt EC assignment is attributed to a computational HAMAP rule; the entry separately reports PubMed-supported catalytic activity.",
    "The exact source snapshot used by the benchmark author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the keyed EC number, and the choices specify distinct classifications."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as peptidyl-tRNA hydrolase, EC 3.1.1.29, by a HAMAP rule. The entry also records a specific catalytic reaction with PubMed-based experimental evidence. This supports choice B, while the HAMAP EC annotation itself is computational rather than direct experimental proof of the full classification.",
    "evidence_ids": ["C1", "C4", "C6", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a compact enzyme, but the supplied sequence and context do not provide a sufficiently specific biological clue to distinguish peptidyl-tRNA hydrolysis from the reactions represented by the other EC choices.",
    "missing_item_specific_fact": "The protein-specific identification as peptidyl-tRNA hydrolase, or equivalent evidence of its substrate and catalytic activity, is absent from the input.",
    "reason": "Selecting B requires identifying the sequence's particular enzyme family or knowing its specific function; generic sequence-based enzyme reasoning does not establish this EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the keyed EC number, and the choices specify distinct classifications."
  },
  "important_caveats": [
    "The sequence match and EC annotation are established in reviewer-only database evidence, not information available to the evaluated model.",
    "The UniProt EC assignment is attributed to a computational HAMAP rule; the entry separately reports PubMed-supported catalytic activity.",
    "The exact source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 194-aa sequence matches UniProt entry A0A0F6B281 (PTH_SALT1, Salmonella typhimurium 14028s) exactly. The UniProt annotation assigns EC 3.1.1.29 (peptidyl-tRNA hydrolase) via HAMAP-Rule MF_00083 (ECO:0000255, computational inference). This is corroborated by experimental catalytic-activity data from PubMed 27264868 and 29777131 (ECO:0000305) demonstrating hydrolysis of N-acetylglycyl-tRNA(Gly). The EC assignment is present in both the current entry (v43) and the historical archived record (v42). The key is supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains well-known catalytic motifs diagnostic of peptidyl-tRNA hydrolase (Pth): the 'VAHDELD' segment (positions ~78-84) encodes the AHDE catalytic dyad/triad, and the 'GGGHGGHN' segment (positions ~110-117) encodes the histidine-rich catalytic region characteristic of the Pth superfamily. These motifs are standard biochemistry knowledge. The small size (194 aa) is consistent with Pth. The absence of any oxidoreductase cofactor-binding motifs (e.g., Rossmann fold for NAD(P)+) eliminates D (1.1.1.12, alcohol dehydrogenase). The absence of transferase signatures (e.g., GNAT fold, acetyltransferase motifs) eliminates C (2.3.2.27). Between the two esterase/hydrolase options, the specific AHDE + HGGH catalytic architecture is a hallmark of Pth (EC 3.1.1.29) rather than a phospholipase A2-type esterase (EC 3.1.1.80).


**Missing item-specific fact**

> None strictly absent; the Pth-specific catalytic motifs (AHDE, HGGH) are present in the supplied sequence and are well-documented in standard biochemistry references. However, confidently distinguishing 3.1.1.29 from 3.1.1.80 at the 4-digit level does require familiarity with Pth family motifs, which is specialized but not obscure knowledge.


**Reason**

> The sequence itself encodes identifiable catalytic motifs that a knowledgeable biochemist can use to narrow from four EC classes to the correct one. The reasoning path (eliminate oxidoreductase and transferase by absence of cofactor/transfer motifs, then identify Pth-specific AHDE/HGGH architecture among the two hydrolase options) is grounded in the supplied sequence rather than requiring an external database lookup of this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three EC classes (1.x.x.x oxidoreductase, 2.x.x.x transferase, 3.1.1.x hydrolase). The two hydrolase sub-options (3.1.1.29 vs 3.1.1.80) are distinguishable by the Pth-specific catalytic motifs present in the sequence. No other option is defensible given the sequence features.


### Important caveats

- The primary EC annotation in UniProt is via HAMAP-Rule (computational, ECO:0000255), not direct experimental measurement of the full peptidyl-tRNA hydrolysis reaction. The experimental evidence (PubMed 27264868, 29777131) confirms a related but narrower activity: N-acetylglycyl-tRNA(Gly) hydrolysis.
- The reviewer-only accession (A0A0F6B281) and its metadata were absent from the evaluated model input; the model sees only the raw sequence and four EC numbers.
- Distinguishing EC 3.1.1.29 from EC 3.1.1.80 at the 4-digit level relies on recognizing Pth-family motifs; a model without specific Pth biochemistry knowledge would struggle at this granularity even though the broader class (3.1.1.x) is clear.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains well-known catalytic motifs diagnostic of peptidyl-tRNA hydrolase (Pth): the 'VAHDELD' segment (positions ~78-84) encodes the AHDE catalytic dyad/triad, and the 'GGGHGGHN' segment (positions ~110-117) encodes the histidine-rich catalytic region characteristic of the Pth superfamily. These motifs are standard biochemistry knowledge. The small size (194 aa) is consistent with Pth. The absence of any oxidoreductase cofactor-binding motifs (e.g., Rossmann fold for NAD(P)+) eliminates D (1.1.1.12, alcohol dehydrogenase). The absence of transferase signatures (e.g., GNAT fold, acetyltransferase motifs) eliminates C (2.3.2.27). Between the two esterase/hydrolase options, the specific AHDE + HGGH catalytic architecture is a hallmark of Pth (EC 3.1.1.29) rather than a phospholipase A2-type esterase (EC 3.1.1.80).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly absent; the Pth-specific catalytic motifs (AHDE, HGGH) are present in the supplied sequence and are well-documented in standard biochemistry references. However, confidently distinguishing 3.1.1.29 from 3.1.1.80 at the 4-digit level does require familiarity with Pth family motifs, which is specialized but not obscure knowledge.",
    "reason": "The sequence itself encodes identifiable catalytic motifs that a knowledgeable biochemist can use to narrow from four EC classes to the correct one. The reasoning path (eliminate oxidoreductase and transferase by absence of cofactor/transfer motifs, then identify Pth-specific AHDE/HGGH architecture among the two hydrolase options) is grounded in the supplied sequence rather than requiring an external database lookup of this particular protein."
  },
  "case_id": "EC_number_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied 194-aa sequence matches UniProt entry A0A0F6B281 (PTH_SALT1, Salmonella typhimurium 14028s) exactly. The UniProt annotation assigns EC 3.1.1.29 (peptidyl-tRNA hydrolase) via HAMAP-Rule MF_00083 (ECO:0000255, computational inference). This is corroborated by experimental catalytic-activity data from PubMed 27264868 and 29777131 (ECO:0000305) demonstrating hydrolysis of N-acetylglycyl-tRNA(Gly). The EC assignment is present in both the current entry (v43) and the historical archived record (v42). The key is supported."
  },
  "important_caveats": [
    "The primary EC annotation in UniProt is via HAMAP-Rule (computational, ECO:0000255), not direct experimental measurement of the full peptidyl-tRNA hydrolysis reaction. The experimental evidence (PubMed 27264868, 29777131) confirms a related but narrower activity: N-acetylglycyl-tRNA(Gly) hydrolysis.",
    "The reviewer-only accession (A0A0F6B281) and its metadata were absent from the evaluated model input; the model sees only the raw sequence and four EC numbers.",
    "Distinguishing EC 3.1.1.29 from EC 3.1.1.80 at the 4-digit level relies on recognizing Pth-family motifs; a model without specific Pth biochemistry knowledge would struggle at this granularity even though the broader class (3.1.1.x) is clear."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three EC classes (1.x.x.x oxidoreductase, 2.x.x.x transferase, 3.1.1.x hydrolase). The two hydrolase sub-options (3.1.1.29 vs 3.1.1.80) are distinguishable by the Pth-specific catalytic motifs present in the sequence. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 194-aa sequence matches UniProt entry A0A0F6B281 (PTH_SALT1, Salmonella typhimurium 14028s) exactly. The UniProt annotation assigns EC 3.1.1.29 (peptidyl-tRNA hydrolase) via HAMAP-Rule MF_00083 (ECO:0000255, computational inference). This is corroborated by experimental catalytic-activity data from PubMed 27264868 and 29777131 (ECO:0000305) demonstrating hydrolysis of N-acetylglycyl-tRNA(Gly). The EC assignment is present in both the current entry (v43) and the historical archived record (v42). The key is supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains well-known catalytic motifs diagnostic of peptidyl-tRNA hydrolase (Pth): the 'VAHDELD' segment (positions ~78-84) encodes the AHDE catalytic dyad/triad, and the 'GGGHGGHN' segment (positions ~110-117) encodes the histidine-rich catalytic region characteristic of the Pth superfamily. These motifs are standard biochemistry knowledge. The small size (194 aa) is consistent with Pth. The absence of any oxidoreductase cofactor-binding motifs (e.g., Rossmann fold for NAD(P)+) eliminates D (1.1.1.12, alcohol dehydrogenase). The absence of transferase signatures (e.g., GNAT fold, acetyltransferase motifs) eliminates C (2.3.2.27). Between the two esterase/hydrolase options, the specific AHDE + HGGH catalytic architecture is a hallmark of Pth (EC 3.1.1.29) rather than a phospholipase A2-type esterase (EC 3.1.1.80).",
    "missing_item_specific_fact": "None strictly absent; the Pth-specific catalytic motifs (AHDE, HGGH) are present in the supplied sequence and are well-documented in standard biochemistry references. However, confidently distinguishing 3.1.1.29 from 3.1.1.80 at the 4-digit level does require familiarity with Pth family motifs, which is specialized but not obscure knowledge.",
    "reason": "The sequence itself encodes identifiable catalytic motifs that a knowledgeable biochemist can use to narrow from four EC classes to the correct one. The reasoning path (eliminate oxidoreductase and transferase by absence of cofactor/transfer motifs, then identify Pth-specific AHDE/HGGH architecture among the two hydrolase options) is grounded in the supplied sequence rather than requiring an external database lookup of this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three EC classes (1.x.x.x oxidoreductase, 2.x.x.x transferase, 3.1.1.x hydrolase). The two hydrolase sub-options (3.1.1.29 vs 3.1.1.80) are distinguishable by the Pth-specific catalytic motifs present in the sequence. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The primary EC annotation in UniProt is via HAMAP-Rule (computational, ECO:0000255), not direct experimental measurement of the full peptidyl-tRNA hydrolysis reaction. The experimental evidence (PubMed 27264868, 29777131) confirms a related but narrower activity: N-acetylglycyl-tRNA(Gly) hydrolysis.",
    "The reviewer-only accession (A0A0F6B281) and its metadata were absent from the evaluated model input; the model sees only the raw sequence and four EC numbers.",
    "Distinguishing EC 3.1.1.29 from EC 3.1.1.80 at the 4-digit level relies on recognizing Pth-family motifs; a model without specific Pth biochemistry knowledge would struggle at this granularity even though the broader class (3.1.1.x) is clear."
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

**Accession:** `A0A0F6B281` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 42. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
"A0A0F6B281"
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"3.1.1.29"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"Peptidyl-tRNA hydrolase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"Pth"}]}}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.1.1.29","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"name":"an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:54448"},{"database":"Rhea","id":"RHEA-COMP:10123"},{"database":"Rhea","id":"RHEA-COMP:13883"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:59874"},{"database":"ChEBI","id":"CHEBI:78442"},{"database":"ChEBI","id":"CHEBI:138191"}]}}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"27264868","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"29777131","source":"PubMed"}],"name":"N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81979"},{"database":"Rhea","id":"RHEA-COMP:9664"},{"database":"Rhea","id":"RHEA-COMP:19766"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:61887"},{"database":"ChEBI","id":"CHEBI:78442"},{"database":"ChEBI","id":"CHEBI:232036"}]}}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"citation":{"authors":["Cheverton A.M.","Gollan B.","Przydacz M.","Wong C.T.","Mylona A.","Hare S.A.","Helaine S."],"citationCrossReferences":[{"database":"PubMed","id":"27264868"},{"database":"DOI","id":"10.1016/j.molcel.2016.05.002"}],"citationType":"journal article","firstPage":"86","id":"27264868","journal":"Mol. Cell","lastPage":"96","publicationDate":"2016","title":"A Salmonella Toxin Promotes Persister Formation through Acetylation of tRNA.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"citation":{"authors":["Rycroft J.A.","Gollan B.","Grabe G.J.","Hall A.","Cheverton A.M.","Larrouy-Maumus G.","Hare S.A.","Helaine S."],"citationCrossReferences":[{"database":"PubMed","id":"29777131"},{"database":"DOI","id":"10.1038/s41467-018-04472-6"}],"citationType":"journal article","firstPage":"1993","id":"29777131","journal":"Nat. Commun.","lastPage":"1993","publicationDate":"2018","title":"Activity of acetyltransferase toxins involved in Salmonella persister formation during macrophage infection.","volume":"9"},"referenceComments":[{"type":"STRAIN","value":"ATCC 14028 / SGSC 2980 / CDC 6516-60 / NCTC 12023"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
DE   RecName: Full=Peptidyl-tRNA hydrolase {ECO:0000255|HAMAP-Rule:MF_00083};
DE            Short=Pth {ECO:0000255|HAMAP-Rule:MF_00083};
DE            EC=3.1.1.29 {ECO:0000255|HAMAP-Rule:MF_00083};
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 52-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino
CC         acid + a tRNA + H(+); Xref=Rhea:RHEA:54448, Rhea:RHEA-COMP:10123,
CC         Rhea:RHEA-COMP:13883, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:59874, ChEBI:CHEBI:78442, ChEBI:CHEBI:138191;
CC         EC=3.1.1.29; Evidence={ECO:0000255|HAMAP-Rule:MF_00083};
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 58-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) +
CC         H(+); Xref=Rhea:RHEA:81979, Rhea:RHEA-COMP:9664, Rhea:RHEA-
CC         COMP:19766, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:61887,
CC         ChEBI:CHEBI:78442, ChEBI:CHEBI:232036;
CC         Evidence={ECO:0000305|PubMed:27264868, ECO:0000305|PubMed:29777131};
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
