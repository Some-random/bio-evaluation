# GO_molecular_function_0056

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — toxin activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHALRSSVLALWLCLHVSVRAWMTYRSANGLDEYEPEDRIIFLGTKWCGNGNVAEGPEDLGPLKETDACCREHDMCPDLIAAGQSKHGLTNTASYTRLNCGCDEKFYNCLKNSAETGSGAVRFTYFTVLGTKCYRNEHPLICVKKGWFSCSKYELDKSQPKRYQWFDVSSNFAFPRMLT

[Multiple Choices]
A. phosphatidylcholine transfer activity
B. alpha-1,2-mannosyltransferase activity
C. acyltransferase activity, transferring groups other than amino-acyl groups
D. toxin activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches a bee venom phospholipase A2 annotated with toxin activity. The record also links it to venom and reports a possible role potentiating another venom toxin’s effects. However, the toxin-activity annotation is inferred from a keyword, and the reported potentiation is qualified and partly based on an ortholog; this is not unambiguous direct evidence that this protein itself causes toxicity.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3), [H7](#evidence-h7), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The signal peptide and cysteine-rich sequence are consistent with a secreted protein, and the options make several transferase functions implausible. Those features do not establish the protein’s evolved toxin role, which is what distinguishes D.


**Missing item-specific fact**

> The protein-specific fact that this sequence is a venom phospholipase A2 associated with toxin activity and venom effects.


**Reason**

> Identifying the precise venom protein or establishing its toxin role requires item-specific annotation or experimental/contextual information absent from the question. Sequence-level secretion clues alone do not distinguish toxin activity from other secreted proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, toxin activity is supported by the protein-specific evidence; the reported phospholipase reaction is hydrolysis, not the acyl-group transfer described by C.


### Important caveats

- The exact sequence match and toxin annotation are reviewer-only evidence, not information supplied to the evaluated model.
- The protein’s phospholipase A2 catalytic activity is distinct from toxin activity and is not offered as an option.
- The toxin-activity annotation is computationally inferred; the cited functional statement is qualified and includes inference from an ortholog.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The signal peptide and cysteine-rich sequence are consistent with a secreted protein, and the options make several transferase functions implausible. Those features do not establish the protein’s evolved toxin role, which is what distinguishes D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is a venom phospholipase A2 associated with toxin activity and venom effects.",
    "reason": "Identifying the precise venom protein or establishing its toxin role requires item-specific annotation or experimental/contextual information absent from the question. Sequence-level secretion clues alone do not distinguish toxin activity from other secreted proteins."
  },
  "case_id": "GO_molecular_function_0056",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3",
      "H7",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a bee venom phospholipase A2 annotated with toxin activity. The record also links it to venom and reports a possible role potentiating another venom toxin’s effects. However, the toxin-activity annotation is inferred from a keyword, and the reported potentiation is qualified and partly based on an ortholog; this is not unambiguous direct evidence that this protein itself causes toxicity."
  },
  "important_caveats": [
    "The exact sequence match and toxin annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The protein’s phospholipase A2 catalytic activity is distinct from toxin activity and is not offered as an option.",
    "The toxin-activity annotation is computationally inferred; the cited functional statement is qualified and includes inference from an ortholog."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, toxin activity is supported by the protein-specific evidence; the reported phospholipase reaction is hydrolysis, not the acyl-group transfer described by C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a bee venom phospholipase A2 annotated with toxin activity. The record also links it to venom and reports a possible role potentiating another venom toxin’s effects. However, the toxin-activity annotation is inferred from a keyword, and the reported potentiation is qualified and partly based on an ortholog; this is not unambiguous direct evidence that this protein itself causes toxicity.",
    "evidence_ids": ["H2", "H3", "H7", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The signal peptide and cysteine-rich sequence are consistent with a secreted protein, and the options make several transferase functions implausible. Those features do not establish the protein’s evolved toxin role, which is what distinguishes D.",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is a venom phospholipase A2 associated with toxin activity and venom effects.",
    "reason": "Identifying the precise venom protein or establishing its toxin role requires item-specific annotation or experimental/contextual information absent from the question. Sequence-level secretion clues alone do not distinguish toxin activity from other secreted proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, toxin activity is supported by the protein-specific evidence; the reported phospholipase reaction is hydrolysis, not the acyl-group transfer described by C."
  },
  "important_caveats": [
    "The exact sequence match and toxin annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The protein’s phospholipase A2 catalytic activity is distinct from toxin activity and is not offered as an option.",
    "The toxin-activity annotation is computationally inferred; the cited functional statement is qualified and includes inference from an ortholog."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (UniProt P0DXZ6, PA2_XYLAR from Xylocopa aruana) carries GO:0090729 (toxin activity) as an annotation (evidence H7, IEA:UniProtKB-KW). The FUNCTION comment (C5/H3) describes potentiation of DRG activation, cell lysis, and pain behaviors, consistent with the GO:0090729 definition of 'interacting selectively with biological molecules in another organism, initiating pathogenesis.' The protein is a venom PLA2 from a venom gland. Among the four options, D is the only one matching any UniProt annotation for this protein. Options A (phosphatidylcholine transfer, GO:0120019) and B (alpha-1,2-mannosyltransferase, GO:0000026) are unrelated enzyme classes. Option C (acyltransferase, EC 2.3.1.-) is incorrect because PLA2 is classified as a hydrolase (EC 3.1.1.4), not a transferase. The annotation is keyword-based (IEA) rather than experimentally determined, but it is present and consistent with the protein's venom origin and pain-potentiating activity.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H7](#evidence-h7), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could theoretically recognize PLA2 sequence features (the GTKWCGNG calcium-binding loop motif, catalytic His in the CREHDM region, characteristic cysteine spacing in a ~179 AA secreted protein) and then reason that PLA2 is a well-known venom toxin, eliminating options A (lipid transfer protein), B (glycosyltransferase, much larger), and C (acyltransferase, wrong EC class—PLA2 is a hydrolase). However, recognizing the PLA2 fold from raw sequence without database lookup is a specialized pattern-matching task that effectively requires memorized motif knowledge or a trained predictor.


**Missing item-specific fact**

> Identification of this specific 179-residue sequence as a phospholipase A2 (EC 3.1.1.4) requires recognizing the PLA2 calcium-binding loop motif (GTKWCGNG) and catalytic architecture, which is a protein-family-specific annotation fact. Additionally, the answer 'toxin activity' is a keyword-based GO annotation (IEA:UniProtKB-KW) applied because the protein is from a venom gland, not a precise mechanistic molecular function. Without knowing the protein is PLA2, one cannot confidently eliminate option C (acyltransferase), since PLA2 does transfer an acyl group (to water), and the hydrolase-vs-transferase distinction requires knowing the EC classification.


**Reason**

> The correct answer depends on identifying the protein as a PLA2 from sequence motifs (a lookup/family-recognition step) and then mapping that to 'toxin activity' via the venom context. The distinction between C (acyltransferase) and D (toxin activity) requires knowing PLA2 is a hydrolase (EC 3.1.1.4) rather than a transferase (EC 2.3.1.-), which is an item-specific classification fact. Without PLA2 identification, the four options cannot be meaningfully discriminated by general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> A model that identifies the protein as a phospholipase but does not know the EC hydrolase-vs-transferase distinction might select C (acyltransferase activity, transferring groups other than amino-acyl groups), since PLA2 does catalyze transfer of an acyl group from a phospholipid to water. The GO:0090729 'toxin activity' term is also somewhat unusual as a 'molecular function' (it describes an ecological/evolutionary role rather than a catalytic mechanism), and the older GO:0015070 'toxin activity' was made obsolete precisely because 'it represents a classification of molecules and not a molecular function.' This creates conceptual ambiguity about whether 'toxin activity' is the best answer for a molecular-function question.


### Important caveats

- The GO:0090729 toxin activity annotation is keyword-based (IEA:UniProtKB-KW), not experimentally validated as a molecular function.
- The GO:0015070 'toxin activity' term was made obsolete because it 'represents a classification of molecules and not a molecular function,' yet GO:0090729 (its replacement) is still used here, raising conceptual tension with the question's framing of 'fundamental activity at the molecular level.'
- The protein's actual catalytic activity (phospholipase A2, GO:0004623) is not offered as an option, forcing the model to choose a broader ecological annotation over a precise mechanistic one.
- The UniProt entry was first released 2025-02-05; the benchmark's author snapshot date is unknown, though the historical version (entry v4, 2026-01) matches the sequence.
- The PLA2 activity annotation itself is IEA:UniProtKB-EC (transferred by similarity from P00630, bee PLA2), not independently experimentally confirmed for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could theoretically recognize PLA2 sequence features (the GTKWCGNG calcium-binding loop motif, catalytic His in the CREHDM region, characteristic cysteine spacing in a ~179 AA secreted protein) and then reason that PLA2 is a well-known venom toxin, eliminating options A (lipid transfer protein), B (glycosyltransferase, much larger), and C (acyltransferase, wrong EC class—PLA2 is a hydrolase). However, recognizing the PLA2 fold from raw sequence without database lookup is a specialized pattern-matching task that effectively requires memorized motif knowledge or a trained predictor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identification of this specific 179-residue sequence as a phospholipase A2 (EC 3.1.1.4) requires recognizing the PLA2 calcium-binding loop motif (GTKWCGNG) and catalytic architecture, which is a protein-family-specific annotation fact. Additionally, the answer 'toxin activity' is a keyword-based GO annotation (IEA:UniProtKB-KW) applied because the protein is from a venom gland, not a precise mechanistic molecular function. Without knowing the protein is PLA2, one cannot confidently eliminate option C (acyltransferase), since PLA2 does transfer an acyl group (to water), and the hydrolase-vs-transferase distinction requires knowing the EC classification.",
    "reason": "The correct answer depends on identifying the protein as a PLA2 from sequence motifs (a lookup/family-recognition step) and then mapping that to 'toxin activity' via the venom context. The distinction between C (acyltransferase) and D (toxin activity) requires knowing PLA2 is a hydrolase (EC 3.1.1.4) rather than a transferase (EC 2.3.1.-), which is an item-specific classification fact. Without PLA2 identification, the four options cannot be meaningfully discriminated by general biological reasoning alone."
  },
  "case_id": "GO_molecular_function_0056",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C7",
      "H3",
      "H7",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein (UniProt P0DXZ6, PA2_XYLAR from Xylocopa aruana) carries GO:0090729 (toxin activity) as an annotation (evidence H7, IEA:UniProtKB-KW). The FUNCTION comment (C5/H3) describes potentiation of DRG activation, cell lysis, and pain behaviors, consistent with the GO:0090729 definition of 'interacting selectively with biological molecules in another organism, initiating pathogenesis.' The protein is a venom PLA2 from a venom gland. Among the four options, D is the only one matching any UniProt annotation for this protein. Options A (phosphatidylcholine transfer, GO:0120019) and B (alpha-1,2-mannosyltransferase, GO:0000026) are unrelated enzyme classes. Option C (acyltransferase, EC 2.3.1.-) is incorrect because PLA2 is classified as a hydrolase (EC 3.1.1.4), not a transferase. The annotation is keyword-based (IEA) rather than experimentally determined, but it is present and consistent with the protein's venom origin and pain-potentiating activity."
  },
  "important_caveats": [
    "The GO:0090729 toxin activity annotation is keyword-based (IEA:UniProtKB-KW), not experimentally validated as a molecular function.",
    "The GO:0015070 'toxin activity' term was made obsolete because it 'represents a classification of molecules and not a molecular function,' yet GO:0090729 (its replacement) is still used here, raising conceptual tension with the question's framing of 'fundamental activity at the molecular level.'",
    "The protein's actual catalytic activity (phospholipase A2, GO:0004623) is not offered as an option, forcing the model to choose a broader ecological annotation over a precise mechanistic one.",
    "The UniProt entry was first released 2025-02-05; the benchmark's author snapshot date is unknown, though the historical version (entry v4, 2026-01) matches the sequence.",
    "The PLA2 activity annotation itself is IEA:UniProtKB-EC (transferred by similarity from P00630, bee PLA2), not independently experimentally confirmed for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "A model that identifies the protein as a phospholipase but does not know the EC hydrolase-vs-transferase distinction might select C (acyltransferase activity, transferring groups other than amino-acyl groups), since PLA2 does catalyze transfer of an acyl group from a phospholipid to water. The GO:0090729 'toxin activity' term is also somewhat unusual as a 'molecular function' (it describes an ecological/evolutionary role rather than a catalytic mechanism), and the older GO:0015070 'toxin activity' was made obsolete precisely because 'it represents a classification of molecules and not a molecular function.' This creates conceptual ambiguity about whether 'toxin activity' is the best answer for a molecular-function question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0056",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (UniProt P0DXZ6, PA2_XYLAR from Xylocopa aruana) carries GO:0090729 (toxin activity) as an annotation (evidence H7, IEA:UniProtKB-KW). The FUNCTION comment (C5/H3) describes potentiation of DRG activation, cell lysis, and pain behaviors, consistent with the GO:0090729 definition of 'interacting selectively with biological molecules in another organism, initiating pathogenesis.' The protein is a venom PLA2 from a venom gland. Among the four options, D is the only one matching any UniProt annotation for this protein. Options A (phosphatidylcholine transfer, GO:0120019) and B (alpha-1,2-mannosyltransferase, GO:0000026) are unrelated enzyme classes. Option C (acyltransferase, EC 2.3.1.-) is incorrect because PLA2 is classified as a hydrolase (EC 3.1.1.4), not a transferase. The annotation is keyword-based (IEA) rather than experimentally determined, but it is present and consistent with the protein's venom origin and pain-potentiating activity.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C7", "H3", "H7", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could theoretically recognize PLA2 sequence features (the GTKWCGNG calcium-binding loop motif, catalytic His in the CREHDM region, characteristic cysteine spacing in a ~179 AA secreted protein) and then reason that PLA2 is a well-known venom toxin, eliminating options A (lipid transfer protein), B (glycosyltransferase, much larger), and C (acyltransferase, wrong EC class—PLA2 is a hydrolase). However, recognizing the PLA2 fold from raw sequence without database lookup is a specialized pattern-matching task that effectively requires memorized motif knowledge or a trained predictor.",
    "missing_item_specific_fact": "Identification of this specific 179-residue sequence as a phospholipase A2 (EC 3.1.1.4) requires recognizing the PLA2 calcium-binding loop motif (GTKWCGNG) and catalytic architecture, which is a protein-family-specific annotation fact. Additionally, the answer 'toxin activity' is a keyword-based GO annotation (IEA:UniProtKB-KW) applied because the protein is from a venom gland, not a precise mechanistic molecular function. Without knowing the protein is PLA2, one cannot confidently eliminate option C (acyltransferase), since PLA2 does transfer an acyl group (to water), and the hydrolase-vs-transferase distinction requires knowing the EC classification.",
    "reason": "The correct answer depends on identifying the protein as a PLA2 from sequence motifs (a lookup/family-recognition step) and then mapping that to 'toxin activity' via the venom context. The distinction between C (acyltransferase) and D (toxin activity) requires knowing PLA2 is a hydrolase (EC 3.1.1.4) rather than a transferase (EC 2.3.1.-), which is an item-specific classification fact. Without PLA2 identification, the four options cannot be meaningfully discriminated by general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "A model that identifies the protein as a phospholipase but does not know the EC hydrolase-vs-transferase distinction might select C (acyltransferase activity, transferring groups other than amino-acyl groups), since PLA2 does catalyze transfer of an acyl group from a phospholipid to water. The GO:0090729 'toxin activity' term is also somewhat unusual as a 'molecular function' (it describes an ecological/evolutionary role rather than a catalytic mechanism), and the older GO:0015070 'toxin activity' was made obsolete precisely because 'it represents a classification of molecules and not a molecular function.' This creates conceptual ambiguity about whether 'toxin activity' is the best answer for a molecular-function question."
  },
  "important_caveats": [
    "The GO:0090729 toxin activity annotation is keyword-based (IEA:UniProtKB-KW), not experimentally validated as a molecular function.",
    "The GO:0015070 'toxin activity' term was made obsolete because it 'represents a classification of molecules and not a molecular function,' yet GO:0090729 (its replacement) is still used here, raising conceptual tension with the question's framing of 'fundamental activity at the molecular level.'",
    "The protein's actual catalytic activity (phospholipase A2, GO:0004623) is not offered as an option, forcing the model to choose a broader ecological annotation over a precise mechanistic one.",
    "The UniProt entry was first released 2025-02-05; the benchmark's author snapshot date is unknown, though the historical version (entry v4, 2026-01) matches the sequence.",
    "The PLA2 activity annotation itself is IEA:UniProtKB-EC (transferred by similarity from P00630, bee PLA2), not independently experimentally confirmed for this specific protein."
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

**Accession:** `P0DXZ6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
"P0DXZ6"
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
{"commonName":"Great carpenter bee","lineage":["Eukaryota","Metazoa","Ecdysozoa","Arthropoda","Altocrustacea","Allotriocarida","Hexapoda","Insecta","Pterygota","Neoptera","Eumetabola","Endopterygota","Hymenoptera","Apocrita","Aculeata","Apoidea","Anthophila","Apidae","Xylocopa","Koptortosoma"],"scientificName":"Xylocopa aruana","taxonId":135674}
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Phosphatidylcholine 2-acylhydrolase"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P00630","source":"UniProtKB"}],"value":"3.1.1.4"}],"fullName":{"value":"Phospholipase A2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PA2"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"36550366","source":"PubMed"}],"value":"PLA2"}]}}
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36550366","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"May potentiate Xylotoxin(1)-Xa1a DRG activation and cell lysis, since the orthologous A.mellifera PA2 potentiates Xylotoxin(1)-Xa1a DRG activation and cell lysis. In vivo, intraplantar injection in mice may potentiate spontaneous pain behaviors and paw swelling caused by Xylotoxin(1)-Xa1a, since the orthologous A.mellifera PA2 shows this effect (PubMed:36550366). PLA2 catalyzes the calcium-dependent hydrolysis of the 2-acyl groups in 3-sn-phosphoglycerides (Probable)"}]}
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ6.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:59.679483+00:00.  

```json
{"database":"GO","id":"GO:0004623","properties":[{"key":"GoTerm","value":"F:A2-type glycerophospholipase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
```

Source SHA-256: `a4a3642c25c1c2414c3d78cd3e1fc44c8a083a58364446defb8748c41e68c974`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)  
**Locator:** `lines 17-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:30:01.445083+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [MRNA], IDENTIFICATION BY MASS SPECTROMETRY, AND
RP   SUBCELLULAR LOCATION.
RC   TISSUE=Venom, and Venom gland;
RX   PubMed=36550366; DOI=10.1038/s41598-022-26867-8;
RA   Shi N., Szanto T.G., He J., Schroeder C.I., Walker A.A., Deuis J.R.,
RA   Vetter I., Panyi G., King G.F., Robinson S.D.;
RT   "Venom composition and pain-causing toxins of the Australian great
RT   carpenter bee Xylocopa aruana.";
RL   Sci. Rep. 12:22168-22168(2022).
```

Source SHA-256: `ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)  
**Locator:** `lines 27-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:30:01.445083+00:00.  

```text
CC   -!- FUNCTION: May potentiate Xylotoxin(1)-Xa1a DRG activation and cell
CC       lysis, since the orthologous A.mellifera PA2 potentiates Xylotoxin(1)-
CC       Xa1a DRG activation and cell lysis. In vivo, intraplantar injection in
CC       mice may potentiate spontaneous pain behaviors and paw swelling caused
CC       by Xylotoxin(1)-Xa1a, since the orthologous A.mellifera PA2 shows this
CC       effect (PubMed:36550366). PLA2 catalyzes the calcium-dependent
CC       hydrolysis of the 2-acyl groups in 3-sn-phosphoglycerides (Probable).
CC       {ECO:0000269|PubMed:36550366, ECO:0000305}.
```

Source SHA-256: `ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ6?format=txt&versions=4)  
**Locator:** `lines 59-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:30:01.445083+00:00.  

```text
DR   GO; GO:0090729; F:toxin activity; IEA:UniProtKB-KW.
```

Source SHA-256: `ce685ee2cfb313cb4868e922c2f9afc26dee98c65065d4d9d113b9c37eab4c1a`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 401379-401391`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0090729
name: toxin activity
namespace: molecular_function
alt_id: GO:0050827
def: "Interacting selectively with one or more biological molecules in another (target) organism, initiating pathogenesis (leading to an abnormal, generally detrimental state) in the target organism. The activity should refer to an evolved function of the active gene product, i.e. one that was selected for. Examples include the activity of botulinum toxin, and snake venom." [GOC:pt]
subset: goslim_generic
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
synonym: "toxin receptor binding" EXACT []
xref: Wikipedia:Toxin
is_a: GO:0003674 ! molecular_function

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 56. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
