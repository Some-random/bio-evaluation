# catalytic_activity_0035

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDKKEVQHHRSQQAMTKSLYAIGMGLLGKSATNMDCANTNLESAGKSSSTNYNRNRFYNERFVPMASGTMPSVSGTNHHSRHQQLLLQQAPKCTADLNEKLVKINRQNANKELSTIQAKDMQSVDKNEEALKELQESIPEINKIFDVHCRIGSGTFSTVLLGTLQRERGLVETQRRRFAIKHHNPTNHPERILRELECMYRIGGVENVIGINCCIRYNDNVAFIMPYMTHDRFHDIYRSLNFPEIRDYLRNLLIALRHVHKFNVIHRDVKPSNILYNRRTGKFLLCDFGLAQRIADDGSVVQSSDLSSREVFSILRDLENGRSVTLTDGNSAQAEAEDYMARRRMRALGGGGSVERAVTGPPSIQKLREQAGGHLTKKDVANQRADTMRLLNRLRLVSPNADPNNYVVSTNTSKKEMHASRAGTPGYRPPEVLLRYPKQSTAVDVWAAGVIMLSLLSGLHPFFKAPHDCGALAEIINLFGDMPVRKTAFLLDRLILLAQKVNTLDLRRVCMRFRHADFFLAPEIQRKYQRPDGTTEMCRSCEQPTFNCLCSNSGHNLERYDGLDIFPAVAYDLLSRLLEVNPQKRITAEEALKHPFFSDQHRITPGIPLHQQQLIMHQQQHIMQHQQHLQRSRETLPSSAARTLKAFVCYPMEITSTASQAAGNI

[Multiple Choices]
A. D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+)
B. dUMP + ATP = dUDP + ADP
C. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
D. (19E)-geissoschizine + NADPH + H(+) = (16R,19Z)-isositsirikine + NADP(+)
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

> The supplied sequence exactly matches the UniProt entry annotated as a non-specific serine/threonine protein kinase (EC 2.7.11.1), with the listed serine-phosphorylation reaction. The cited evidence is a PROSITE-ProRule computational annotation, not direct experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the characteristic eukaryotic protein kinase catalytic-domain motifs, including the HRD and DFG motifs. That supports a protein-phosphorylation reaction and distinguishes option C from the acetyltransferase, nucleotide kinase, and alkaloid-reduction alternatives.


**Missing item-specific fact**

> No item-specific database identity is necessary to distinguish these choices at the enzyme-class level. The sequence alone does not establish experimentally which residue or protein substrate is modified.


**Reason**

> A recognizable kinase-domain pattern provides a concrete biological basis for selecting the only protein-phosphorylation option. The inference supports the broad choice, though it does not independently prove this particular enzyme's substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed reactions, only C corresponds to a protein kinase. The sequence does not establish serine-versus-threonine specificity, but the options do not offer a competing threonine-phosphorylation reaction.


### Important caveats

- The sequence match and catalytic-activity annotation are from reviewer-only sources, not information supplied to the evaluated model.
- The cited UniProt reaction annotation is supported by a PROSITE-ProRule computational inference; direct experimental validation was not established by the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the characteristic eukaryotic protein kinase catalytic-domain motifs, including the HRD and DFG motifs. That supports a protein-phosphorylation reaction and distinguishes option C from the acetyltransferase, nucleotide kinase, and alkaloid-reduction alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific database identity is necessary to distinguish these choices at the enzyme-class level. The sequence alone does not establish experimentally which residue or protein substrate is modified.",
    "reason": "A recognizable kinase-domain pattern provides a concrete biological basis for selecting the only protein-phosphorylation option. The inference supports the broad choice, though it does not independently prove this particular enzyme's substrate specificity."
  },
  "case_id": "catalytic_activity_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a non-specific serine/threonine protein kinase (EC 2.7.11.1), with the listed serine-phosphorylation reaction. The cited evidence is a PROSITE-ProRule computational annotation, not direct experimental evidence."
  },
  "important_caveats": [
    "The sequence match and catalytic-activity annotation are from reviewer-only sources, not information supplied to the evaluated model.",
    "The cited UniProt reaction annotation is supported by a PROSITE-ProRule computational inference; direct experimental validation was not established by the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, only C corresponds to a protein kinase. The sequence does not establish serine-versus-threonine specificity, but the options do not offer a competing threonine-phosphorylation reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as a non-specific serine/threonine protein kinase (EC 2.7.11.1), with the listed serine-phosphorylation reaction. The cited evidence is a PROSITE-ProRule computational annotation, not direct experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the characteristic eukaryotic protein kinase catalytic-domain motifs, including the HRD and DFG motifs. That supports a protein-phosphorylation reaction and distinguishes option C from the acetyltransferase, nucleotide kinase, and alkaloid-reduction alternatives.",
    "missing_item_specific_fact": "No item-specific database identity is necessary to distinguish these choices at the enzyme-class level. The sequence alone does not establish experimentally which residue or protein substrate is modified.",
    "reason": "A recognizable kinase-domain pattern provides a concrete biological basis for selecting the only protein-phosphorylation option. The inference supports the broad choice, though it does not independently prove this particular enzyme's substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, only C corresponds to a protein kinase. The sequence does not establish serine-versus-threonine specificity, but the options do not offer a competing threonine-phosphorylation reaction."
  },
  "important_caveats": [
    "The sequence match and catalytic-activity annotation are from reviewer-only sources, not information supplied to the evaluated model.",
    "The cited UniProt reaction annotation is supported by a PROSITE-ProRule computational inference; direct experimental validation was not established by the supplied evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VJ90 (CDC7B_DROME) for this exact 665-aa sequence annotates EC 2.7.11.1 (non-specific serine/threonine protein kinase) and explicitly lists the catalytic reaction 'L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)' (evidence C5/H3). The sequence matches the UniProt record exactly. The annotation evidence code is ECO:0000255 (PROSITE-ProRule), i.e., computational inference from the protein kinase domain rather than direct experimental measurement, but the kinase domain motifs (HRD, DFG, GxGxxG) are clearly present in the sequence, lending structural support to the annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark protein kinase domain motifs: a glycine-rich loop region ('GSGTFSTVLLG'), the catalytic HRD motif ('IHRDVKPSNILYNRRTGKFLLCDFGLAQRIADDGS' containing HRD and DFG), and the activation-segment architecture. These motifs are diagnostic of a protein kinase (transferase acting on a protein substrate with ATP). Among the four choices, only C describes a protein-kinase reaction (phosphorylation of a seryl residue on a protein by ATP). Choice A is an amino-acid acetyltransferase, B is a nucleotide kinase (dUMP→dUDP), and D is a NADPH-dependent reductase. Recognizing the kinase fold and its ATP-dependent protein-substrate phosphorylation chemistry is sufficient to select C without memorizing the specific UniProt entry.


**Missing item-specific fact**

> None critical. Distinguishing a protein kinase from an amino-acid acetyltransferase, a nucleotide kinase, or a reductase is achievable from the conserved kinase-domain motifs visible in the sequence.


**Reason**

> The protein kinase motifs (HRD, DFG, GxGxxG) are directly observable in the supplied sequence and are general biological knowledge. Only one of the four choices corresponds to a protein kinase reaction, so motif recognition plus knowledge of enzyme-class chemistry meaningfully discriminates the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry annotates both serine and threonine kinase activity (EC 2.7.11.1), only the serine-phosphorylation reaction (C) is offered among the choices. The remaining three options belong to entirely different enzyme classes (acetyltransferase, nucleotide kinase, reductase), so no alternative choice is defensible.


### Important caveats

- The catalytic-activity annotation carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a computational inference from the protein kinase domain profile rather than direct experimental assay of this specific Drosophila protein.
- The protein is a non-specific serine/threonine kinase; the question tests only the serine arm of its dual activity. This does not affect answerability since no threonine-specific option is presented.
- The UniProt accession Q9VJ90 was inferred by the reviewer from dataset metadata; it was not supplied to the evaluated model. The model must rely on sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark protein kinase domain motifs: a glycine-rich loop region ('GSGTFSTVLLG'), the catalytic HRD motif ('IHRDVKPSNILYNRRTGKFLLCDFGLAQRIADDGS' containing HRD and DFG), and the activation-segment architecture. These motifs are diagnostic of a protein kinase (transferase acting on a protein substrate with ATP). Among the four choices, only C describes a protein-kinase reaction (phosphorylation of a seryl residue on a protein by ATP). Choice A is an amino-acid acetyltransferase, B is a nucleotide kinase (dUMP→dUDP), and D is a NADPH-dependent reductase. Recognizing the kinase fold and its ATP-dependent protein-substrate phosphorylation chemistry is sufficient to select C without memorizing the specific UniProt entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Distinguishing a protein kinase from an amino-acid acetyltransferase, a nucleotide kinase, or a reductase is achievable from the conserved kinase-domain motifs visible in the sequence.",
    "reason": "The protein kinase motifs (HRD, DFG, GxGxxG) are directly observable in the supplied sequence and are general biological knowledge. Only one of the four choices corresponds to a protein kinase reaction, so motif recognition plus knowledge of enzyme-class chemistry meaningfully discriminates the answer."
  },
  "case_id": "catalytic_activity_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VJ90 (CDC7B_DROME) for this exact 665-aa sequence annotates EC 2.7.11.1 (non-specific serine/threonine protein kinase) and explicitly lists the catalytic reaction 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' (evidence C5/H3). The sequence matches the UniProt record exactly. The annotation evidence code is ECO:0000255 (PROSITE-ProRule), i.e., computational inference from the protein kinase domain rather than direct experimental measurement, but the kinase domain motifs (HRD, DFG, GxGxxG) are clearly present in the sequence, lending structural support to the annotation."
  },
  "important_caveats": [
    "The catalytic-activity annotation carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a computational inference from the protein kinase domain profile rather than direct experimental assay of this specific Drosophila protein.",
    "The protein is a non-specific serine/threonine kinase; the question tests only the serine arm of its dual activity. This does not affect answerability since no threonine-specific option is presented.",
    "The UniProt accession Q9VJ90 was inferred by the reviewer from dataset metadata; it was not supplied to the evaluated model. The model must rely on sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates both serine and threonine kinase activity (EC 2.7.11.1), only the serine-phosphorylation reaction (C) is offered among the choices. The remaining three options belong to entirely different enzyme classes (acetyltransferase, nucleotide kinase, reductase), so no alternative choice is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VJ90 (CDC7B_DROME) for this exact 665-aa sequence annotates EC 2.7.11.1 (non-specific serine/threonine protein kinase) and explicitly lists the catalytic reaction 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' (evidence C5/H3). The sequence matches the UniProt record exactly. The annotation evidence code is ECO:0000255 (PROSITE-ProRule), i.e., computational inference from the protein kinase domain rather than direct experimental measurement, but the kinase domain motifs (HRD, DFG, GxGxxG) are clearly present in the sequence, lending structural support to the annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark protein kinase domain motifs: a glycine-rich loop region ('GSGTFSTVLLG'), the catalytic HRD motif ('IHRDVKPSNILYNRRTGKFLLCDFGLAQRIADDGS' containing HRD and DFG), and the activation-segment architecture. These motifs are diagnostic of a protein kinase (transferase acting on a protein substrate with ATP). Among the four choices, only C describes a protein-kinase reaction (phosphorylation of a seryl residue on a protein by ATP). Choice A is an amino-acid acetyltransferase, B is a nucleotide kinase (dUMP→dUDP), and D is a NADPH-dependent reductase. Recognizing the kinase fold and its ATP-dependent protein-substrate phosphorylation chemistry is sufficient to select C without memorizing the specific UniProt entry.",
    "missing_item_specific_fact": "None critical. Distinguishing a protein kinase from an amino-acid acetyltransferase, a nucleotide kinase, or a reductase is achievable from the conserved kinase-domain motifs visible in the sequence.",
    "reason": "The protein kinase motifs (HRD, DFG, GxGxxG) are directly observable in the supplied sequence and are general biological knowledge. Only one of the four choices corresponds to a protein kinase reaction, so motif recognition plus knowledge of enzyme-class chemistry meaningfully discriminates the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates both serine and threonine kinase activity (EC 2.7.11.1), only the serine-phosphorylation reaction (C) is offered among the choices. The remaining three options belong to entirely different enzyme classes (acetyltransferase, nucleotide kinase, reductase), so no alternative choice is defensible."
  },
  "important_caveats": [
    "The catalytic-activity annotation carries evidence code ECO:0000255 (PROSITE-ProRule), meaning it is a computational inference from the protein kinase domain profile rather than direct experimental assay of this specific Drosophila protein.",
    "The protein is a non-specific serine/threonine kinase; the question tests only the serine arm of its dual activity. This does not affect answerability since no threonine-specific option is presented.",
    "The UniProt accession Q9VJ90 was inferred by the reviewer from dataset metadata; it was not supplied to the evaluated model. The model must rely on sequence features alone."
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

**Accession:** `Q9VJ90` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 211. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
"Q9VJ90"
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0032677","source":"FlyBase"}],"value":"non-specific serine/threonine protein kinase"}}}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
ID   CDC7B_DROME             Reviewed;         665 AA.
AC   Q9VJ90; Q8T0Q5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 211.
DE   RecName: Full=non-specific serine/threonine protein kinase {ECO:0000312|FlyBase:FBgn0032677};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
GN   ORFNames=CG5790 {ECO:0000312|FlyBase:FBgn0032677};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
DE   RecName: Full=non-specific serine/threonine protein kinase {ECO:0000312|FlyBase:FBgn0032677};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 92-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
