# catalytic_activity_0127

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — luteothin + 4 reduced &#91;2Fe-2S&#93;-&#91;ferredoxin&#93; + 2 O2 + 4 H(+) = aureothin + 4 oxidized &#91;2Fe-2S&#93;-&#91;ferredoxin&#93; + 3 H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTTAHTEPSWADLPFLDFTDPNFSWDSPEVAEAREKSWIARTPLALLVLRYAEADQLARDKRLISGFRGLVDMVGTPEGPVRDFMVDFLQSLDGADHRRLRGLATHPFTPRRITAVQPFVRSTVEQLIDKLPQGDFDFVQHFPHPLPALVMCQLLGFPLEDYDTVGRLSIETNLGLALSNDQDILVKVEQGLGRMFDYLVAAIEKRKVEPGDDLTSDIVRAFHDGVLDDYELRTLVATVLVAGYETTNHQLALAMYDFAQHPDQWMKIKENPELAPQAVEEVLRWSPTLPVTATRVAAEDFEVNGVRIPTGTPVFMCAHVAHRDPRVFADADRFDITVKREAPSIAFGGGPHFCLGTALARLELTEAVAALATRLDPPQIAGEITWRHELGVAGPDALPLRFGAA

[Multiple Choices]
A. (6S)-5-methyl-5,6,7,8-tetrahydrofolate(in) + H(+)(in) = (6S)-5-methyl-5,6,7,8-tetrahydrofolate(out) + H(+)(out)
B. 4-methylmuconolactone = 3-methylmuconolactone
C. luteothin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = aureothin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
D. N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
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

> The supplied sequence exactly matches the UniProt sequence for luteothin monooxygenase. Its annotated catalytic reaction is the luteothin-to-aureothin reaction in choice C; the annotation cites experimental evidence as well as a review-level source.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cytochrome P450 heme-binding motif (including the conserved cysteine-containing region), supporting an oxygenase rather than a transporter, an isomerase, or a methyltransferase. Among the choices, C is the oxygenation reaction.


**Missing item-specific fact**

> The precise luteothin substrate and aureothin product are protein-specific facts not established by the P450 motif alone; identifying those exact compounds would require annotation or other protein-specific knowledge.


**Reason**

> The sequence provides a meaningful enzyme-class argument that distinguishes C from the other choices, though it does not independently establish the exact substrate and product.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The P450 sequence signature supports the oxygenase option, while the other choices describe transport, isomerization, or methyl transfer.


### Important caveats

- The sequence match and experimental support come from reviewer-only sources and were not supplied to the evaluated model.
- The sequence supports the enzyme class more directly than the specific luteothin-to-aureothin transformation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cytochrome P450 heme-binding motif (including the conserved cysteine-containing region), supporting an oxygenase rather than a transporter, an isomerase, or a methyltransferase. Among the choices, C is the oxygenation reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise luteothin substrate and aureothin product are protein-specific facts not established by the P450 motif alone; identifying those exact compounds would require annotation or other protein-specific knowledge.",
    "reason": "The sequence provides a meaningful enzyme-class argument that distinguishes C from the other choices, though it does not independently establish the exact substrate and product."
  },
  "case_id": "catalytic_activity_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for luteothin monooxygenase. Its annotated catalytic reaction is the luteothin-to-aureothin reaction in choice C; the annotation cites experimental evidence as well as a review-level source."
  },
  "important_caveats": [
    "The sequence match and experimental support come from reviewer-only sources and were not supplied to the evaluated model.",
    "The sequence supports the enzyme class more directly than the specific luteothin-to-aureothin transformation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The P450 sequence signature supports the oxygenase option, while the other choices describe transport, isomerization, or methyl transfer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for luteothin monooxygenase. Its annotated catalytic reaction is the luteothin-to-aureothin reaction in choice C; the annotation cites experimental evidence as well as a review-level source.",
    "evidence_ids": ["C1", "C5", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cytochrome P450 heme-binding motif (including the conserved cysteine-containing region), supporting an oxygenase rather than a transporter, an isomerase, or a methyltransferase. Among the choices, C is the oxygenation reaction.",
    "missing_item_specific_fact": "The precise luteothin substrate and aureothin product are protein-specific facts not established by the P450 motif alone; identifying those exact compounds would require annotation or other protein-specific knowledge.",
    "reason": "The sequence provides a meaningful enzyme-class argument that distinguishes C from the other choices, though it does not independently establish the exact substrate and product."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The P450 sequence signature supports the oxygenase option, while the other choices describe transport, isomerization, or methyl transfer."
  },
  "important_caveats": [
    "The sequence match and experimental support come from reviewer-only sources and were not supplied to the evaluated model.",
    "The sequence supports the enzyme class more directly than the specific luteothin-to-aureothin transformation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry Q70KH6 (AURH_STRTU, sequence SHA256 exact match) annotates the catalytic activity as 'luteothin + 4 reduced &#91;2Fe-2S&#93;-&#91;ferredoxin&#93; + 2 O2 + 4 H(+) = aureothin + 4 oxidized &#91;2Fe-2S&#93;-&#91;ferredoxin&#93; + 3 H2O' (EC 1.14.15.37), supported by experimental evidence codes (ECO:0000269) from PubMed:18855960 and PubMed:21280577, and confirmed by X-ray crystallography structures (3P3L, 3P3O, 3P3X, 3P3Z) showing heme B binding. The expected answer text matches the database annotation exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif 'FGGGPHFCLG' (residues ~370-379), identifying the protein as a P450 monooxygenase. Among the four choices, only C describes a P450-type reaction (consumes O2, uses reduced ferredoxin as electron donor, produces oxygenated product + water). Choice A is a membrane transporter reaction, B is an isomerase rearrangement, and D is a SAM-dependent methyltransferase reaction — none involve O2 or electron-transfer chains. Recognizing the P450 motif and matching it to the only O2-dependent, ferredoxin-coupled reaction among the options provides a concrete biological argument to select C.


**Missing item-specific fact**

> The specific substrate/product names (luteothin/aureothin) cannot be deduced from sequence alone, but this is not needed to distinguish among the four choices since only one represents a P450 reaction.


**Reason**

> The P450 heme-binding signature (FGGxHxCxG) is directly visible in the supplied sequence. General knowledge that P450s are O2-dependent monooxygenases requiring electron donors (ferredoxin in bacterial systems) allows elimination of the transporter (A), isomerase (B), and methyltransferase (D) options. The specific compound names are a lookup detail, but the reaction class is inferable from sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C is a P450 monooxygenase reaction; the other three represent entirely different enzyme classes (transporter, isomerase, methyltransferase) with no O2 or electron-transfer-chain involvement, making them incompatible with the P450 motif in the sequence.


### Important caveats

- The specific substrate names 'luteothin' and 'aureothin' are not derivable from sequence alone; a model without P450 motif recognition would need to memorize this annotation.
- The P450 motif identification is necessary but not sufficient to confirm the exact reaction; it only confirms the enzyme class. However, among the given choices, class-level identification is sufficient to select the answer.
- The annotation is experimentally supported (ECO:0000269) rather than purely computational, strengthening the expected answer's reliability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGGGPHFCLG' (residues ~370-379), identifying the protein as a P450 monooxygenase. Among the four choices, only C describes a P450-type reaction (consumes O2, uses reduced ferredoxin as electron donor, produces oxygenated product + water). Choice A is a membrane transporter reaction, B is an isomerase rearrangement, and D is a SAM-dependent methyltransferase reaction — none involve O2 or electron-transfer chains. Recognizing the P450 motif and matching it to the only O2-dependent, ferredoxin-coupled reaction among the options provides a concrete biological argument to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate/product names (luteothin/aureothin) cannot be deduced from sequence alone, but this is not needed to distinguish among the four choices since only one represents a P450 reaction.",
    "reason": "The P450 heme-binding signature (FGGxHxCxG) is directly visible in the supplied sequence. General knowledge that P450s are O2-dependent monooxygenases requiring electron donors (ferredoxin in bacterial systems) allows elimination of the transporter (A), isomerase (B), and methyltransferase (D) options. The specific compound names are a lookup detail, but the reaction class is inferable from sequence features."
  },
  "case_id": "catalytic_activity_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry Q70KH6 (AURH_STRTU, sequence SHA256 exact match) annotates the catalytic activity as 'luteothin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = aureothin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O' (EC 1.14.15.37), supported by experimental evidence codes (ECO:0000269) from PubMed:18855960 and PubMed:21280577, and confirmed by X-ray crystallography structures (3P3L, 3P3O, 3P3X, 3P3Z) showing heme B binding. The expected answer text matches the database annotation exactly."
  },
  "important_caveats": [
    "The specific substrate names 'luteothin' and 'aureothin' are not derivable from sequence alone; a model without P450 motif recognition would need to memorize this annotation.",
    "The P450 motif identification is necessary but not sufficient to confirm the exact reaction; it only confirms the enzyme class. However, among the given choices, class-level identification is sufficient to select the answer.",
    "The annotation is experimentally supported (ECO:0000269) rather than purely computational, strengthening the expected answer's reliability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C is a P450 monooxygenase reaction; the other three represent entirely different enzyme classes (transporter, isomerase, methyltransferase) with no O2 or electron-transfer-chain involvement, making them incompatible with the P450 motif in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry Q70KH6 (AURH_STRTU, sequence SHA256 exact match) annotates the catalytic activity as 'luteothin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = aureothin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O' (EC 1.14.15.37), supported by experimental evidence codes (ECO:0000269) from PubMed:18855960 and PubMed:21280577, and confirmed by X-ray crystallography structures (3P3L, 3P3O, 3P3X, 3P3Z) showing heme B binding. The expected answer text matches the database annotation exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif 'FGGGPHFCLG' (residues ~370-379), identifying the protein as a P450 monooxygenase. Among the four choices, only C describes a P450-type reaction (consumes O2, uses reduced ferredoxin as electron donor, produces oxygenated product + water). Choice A is a membrane transporter reaction, B is an isomerase rearrangement, and D is a SAM-dependent methyltransferase reaction — none involve O2 or electron-transfer chains. Recognizing the P450 motif and matching it to the only O2-dependent, ferredoxin-coupled reaction among the options provides a concrete biological argument to select C.",
    "missing_item_specific_fact": "The specific substrate/product names (luteothin/aureothin) cannot be deduced from sequence alone, but this is not needed to distinguish among the four choices since only one represents a P450 reaction.",
    "reason": "The P450 heme-binding signature (FGGxHxCxG) is directly visible in the supplied sequence. General knowledge that P450s are O2-dependent monooxygenases requiring electron donors (ferredoxin in bacterial systems) allows elimination of the transporter (A), isomerase (B), and methyltransferase (D) options. The specific compound names are a lookup detail, but the reaction class is inferable from sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C is a P450 monooxygenase reaction; the other three represent entirely different enzyme classes (transporter, isomerase, methyltransferase) with no O2 or electron-transfer-chain involvement, making them incompatible with the P450 motif in the sequence."
  },
  "important_caveats": [
    "The specific substrate names 'luteothin' and 'aureothin' are not derivable from sequence alone; a model without P450 motif recognition would need to memorize this annotation.",
    "The P450 motif identification is necessary but not sufficient to confirm the exact reaction; it only confirms the enzyme class. However, among the given choices, class-level identification is sufficient to select the answer.",
    "The annotation is experimentally supported (ECO:0000269) rather than purely computational, strengthening the expected answer's reliability."
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

**Accession:** `Q70KH6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 97. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:47.723607+00:00.  

```json
"Q70KH6"
```

Source SHA-256: `ba8377eaa9a48799a1eee53d5720940c7e354b7f3a661214941630d81d9902ff`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:47.723607+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"15612710","source":"PubMed"}],"value":"Bifunctional cytochrome P450 monooxygenase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18855960","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21280577","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"15612710","source":"PubMed"}],"value":"1.14.15.37"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Luteothin monooxygenase"}}}
```

Source SHA-256: `ba8377eaa9a48799a1eee53d5720940c7e354b7f3a661214941630d81d9902ff`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:47.723607+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"15612710","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"18855960","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"21280577","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:58825"}}],"reaction":{"ecNumber":"1.14.15.37","evidences":[{"evidenceCode":"ECO:0000269","id":"18855960","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21280577","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"15612710","source":"PubMed"}],"name":"luteothin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = aureothin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58824"},{"database":"Rhea","id":"RHEA-COMP:10000"},{"database":"Rhea","id":"RHEA-COMP:10001"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:33737"},{"database":"ChEBI","id":"CHEBI:33738"},{"database":"ChEBI","id":"CHEBI:80024"},{"database":"ChEBI","id":"CHEBI:142840"}]}}
```

Source SHA-256: `ba8377eaa9a48799a1eee53d5720940c7e354b7f3a661214941630d81d9902ff`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH6.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:47.723607+00:00.  

```json
{"citation":{"authors":["Richter M.E.","Traitcheva N.","Knuepfer U.","Hertweck C."],"citationCrossReferences":[{"database":"PubMed","id":"18855960"},{"database":"DOI","id":"10.1002/anie.200803714"}],"citationType":"journal article","firstPage":"8872","id":"18855960","journal":"Angew. Chem. Int. Ed.","lastPage":"8875","publicationDate":"2008","title":"Sequential asymmetric polyketide heterocyclization catalyzed by a single cytochrome P450 monooxygenase (AurH).","volume":"47"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","REACTION MECHANISM"]}
```

Source SHA-256: `ba8377eaa9a48799a1eee53d5720940c7e354b7f3a661214941630d81d9902ff`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH6?format=txt&versions=97)  
**Locator:** `lines 56-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 97 / 1.  
**Retrieved:** 2026-11-02T04:31:51.166275+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=luteothin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) =
CC         aureothin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O;
CC         Xref=Rhea:RHEA:58824, Rhea:RHEA-COMP:10000, Rhea:RHEA-COMP:10001,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:80024,
CC         ChEBI:CHEBI:142840; EC=1.14.15.37;
CC         Evidence={ECO:0000269|PubMed:18855960, ECO:0000269|PubMed:21280577,
CC         ECO:0000305|PubMed:15612710};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58825;
CC         Evidence={ECO:0000305|PubMed:15612710, ECO:0000305|PubMed:18855960,
CC         ECO:0000305|PubMed:21280577};
```

Source SHA-256: `2dcea6b60b452a9aa4815c42f9dc0d88db5c87719a5dec08b5f84b305e55f621`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
