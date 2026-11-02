# GO_molecular_function_0189

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — beta-glucosidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGKNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAVNSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPQSYSDFFGVAYDTPPKAHALKASRLLVPTTVARPSKPARVFASTADPGTTTADQVYKVGHNLLLAHAAALKVYRDNFQDTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQSLGPRLREFTRDQKKLLIGSYDYVGVNYYTATYVSSARPPNDNKAIFHTDGNFYTTDCKDGVLIGPLAGPAWLNIVPEGIYRCLQEIKAKYNNPVIYITENGVYEVNDTTKTLSEARVDTTRVDYLQDHLSYVLKARQQGVRVQGYFVWSLMDNWELRAGYTSRFGLIHVDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKRPQEDDGAFDTPRKRLKK

[Multiple Choices]
A. ubiquitin-like protein transferase activity
B. 2-oxoglutarate-dependent dioxygenase activity
C. 2 iron, 2 sulfur cluster binding
D. beta-glucosidase activity
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

> The exact 540-aa sequence matches the UniProt record for Ipecac alkaloid beta-glucosidase 9. Its function and catalytic reactions are annotated with experimental evidence cited to PubMed 18927081, and its beta-glucosidase GO annotation is IDA. This supports choice D.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable glycoside hydrolase family 1 beta-glucosidase motifs, including NEP and TENG-like motifs. These support a glycoside-hydrolysis function and distinguish D from the ubiquitin-like transferase, 2-oxoglutarate-dependent dioxygenase, and Fe-S-cluster-binding alternatives.


**Missing item-specific fact**

> No item-specific annotation is needed to favor the broad beta-glucosidase activity; identifying the precise physiological substrates would require protein-specific information not supplied.


**Reason**

> The sequence motifs provide a concrete, biologically grounded basis for selecting D among these choices. The reviewer-only database evidence supports the key but is not needed as input to that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct functions, and the sequence motifs favor beta-glucosidase activity.


### Important caveats

- The experimental support is reported through UniProt annotations citing PubMed 18927081; the primary paper was not independently reviewed here.
- The annotation supports beta-glucosidase activity on specific ipecac alkaloid glycosides, not every possible beta-glucosidase substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable glycoside hydrolase family 1 beta-glucosidase motifs, including NEP and TENG-like motifs. These support a glycoside-hydrolysis function and distinguish D from the ubiquitin-like transferase, 2-oxoglutarate-dependent dioxygenase, and Fe-S-cluster-binding alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific annotation is needed to favor the broad beta-glucosidase activity; identifying the precise physiological substrates would require protein-specific information not supplied.",
    "reason": "The sequence motifs provide a concrete, biologically grounded basis for selecting D among these choices. The reviewer-only database evidence supports the key but is not needed as input to that inference."
  },
  "case_id": "GO_molecular_function_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact 540-aa sequence matches the UniProt record for Ipecac alkaloid beta-glucosidase 9. Its function and catalytic reactions are annotated with experimental evidence cited to PubMed 18927081, and its beta-glucosidase GO annotation is IDA. This supports choice D."
  },
  "important_caveats": [
    "The experimental support is reported through UniProt annotations citing PubMed 18927081; the primary paper was not independently reviewed here.",
    "The annotation supports beta-glucosidase activity on specific ipecac alkaloid glycosides, not every possible beta-glucosidase substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct functions, and the sequence motifs favor beta-glucosidase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 540-aa sequence matches the UniProt record for Ipecac alkaloid beta-glucosidase 9. Its function and catalytic reactions are annotated with experimental evidence cited to PubMed 18927081, and its beta-glucosidase GO annotation is IDA. This supports choice D.",
    "evidence_ids": ["C1", "C5", "C6", "C8", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable glycoside hydrolase family 1 beta-glucosidase motifs, including NEP and TENG-like motifs. These support a glycoside-hydrolysis function and distinguish D from the ubiquitin-like transferase, 2-oxoglutarate-dependent dioxygenase, and Fe-S-cluster-binding alternatives.",
    "missing_item_specific_fact": "No item-specific annotation is needed to favor the broad beta-glucosidase activity; identifying the precise physiological substrates would require protein-specific information not supplied.",
    "reason": "The sequence motifs provide a concrete, biologically grounded basis for selecting D among these choices. The reviewer-only database evidence supports the key but is not needed as input to that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct functions, and the sequence motifs favor beta-glucosidase activity."
  },
  "important_caveats": [
    "The experimental support is reported through UniProt annotations citing PubMed 18927081; the primary paper was not independently reviewed here.",
    "The annotation supports beta-glucosidase activity on specific ipecac alkaloid glycosides, not every possible beta-glucosidase substrate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B6ZKN1 (GLU9_CARIP, sequence matched exactly at 540 AA) is annotated with GO:0008422 (beta-glucosidase activity) with evidence code IDA (Inferred from Direct Assay, ECO:0000314). The function comment states 'Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside,' and two catalytic activity reactions confirm hydrolysis of glycosidic bonds releasing D-glucose. The EC number 3.2.1.- places it in the glycosidase class. All evidence is from direct experimental assay (PubMed:18927081).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Partial elimination is possible: the 540-residue sequence lacks obvious CxxC motifs (weakening option C, 2Fe-2S binding) and lacks the canonical HxD/E...H triad of 2-oxoglutarate-dependent dioxygenases (weakening option B). However, positively identifying beta-glucosidase activity requires recognizing GH1-family-specific sequence signatures (e.g., the 'NEP' and 'ITEN' catalytic motifs present in this sequence) or knowing that this particular plant protein belongs to glycoside hydrolase family 1. This is specialized family-level sequence knowledge, not general biology.


**Missing item-specific fact**

> Recognition that this sequence belongs to glycoside hydrolase family 1 (GH1) beta-glucosidases, identifiable by conserved catalytic motifs such as the 'NEP' box and 'ITEN' motif, or alternatively, database lookup of the specific protein's annotation.


**Reason**

> While general knowledge can eliminate options B and C (absence of dioxygenase and Fe-S cluster motifs), and somewhat weaken A (no obvious RING/HECT/U-box motifs), the positive identification of beta-glucosidase activity from sequence alone requires specialized knowledge of glycoside hydrolase family signatures or memorization of this protein's annotation. A general biologist without training on GH1 motifs would struggle to affirmatively assign 'beta-glucosidase activity' rather than another hydrolase class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are functionally very distinct (transferase, dioxygenase, metal-cluster binding, glycosidase). The experimental evidence unambiguously supports D. No other option is defensible given the annotation data.


### Important caveats

- The UniProt entry was first publicly released on 2025-06-18, which may postdate the benchmark construction; however, the underlying experimental data is from 2008 (PubMed:18927081).
- The sequence match is exact (540 AA, identical SHA256) between the benchmark input and the UniProt entry.
- The GO annotation uses IDA (direct assay) evidence, representing the highest-confidence annotation type.
- The reviewer-only evidence was not available to the evaluated model; the model must rely on sequence analysis and training knowledge alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Partial elimination is possible: the 540-residue sequence lacks obvious CxxC motifs (weakening option C, 2Fe-2S binding) and lacks the canonical HxD/E...H triad of 2-oxoglutarate-dependent dioxygenases (weakening option B). However, positively identifying beta-glucosidase activity requires recognizing GH1-family-specific sequence signatures (e.g., the 'NEP' and 'ITEN' catalytic motifs present in this sequence) or knowing that this particular plant protein belongs to glycoside hydrolase family 1. This is specialized family-level sequence knowledge, not general biology.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this sequence belongs to glycoside hydrolase family 1 (GH1) beta-glucosidases, identifiable by conserved catalytic motifs such as the 'NEP' box and 'ITEN' motif, or alternatively, database lookup of the specific protein's annotation.",
    "reason": "While general knowledge can eliminate options B and C (absence of dioxygenase and Fe-S cluster motifs), and somewhat weaken A (no obvious RING/HECT/U-box motifs), the positive identification of beta-glucosidase activity from sequence alone requires specialized knowledge of glycoside hydrolase family signatures or memorization of this protein's annotation. A general biologist without training on GH1 motifs would struggle to affirmatively assign 'beta-glucosidase activity' rather than another hydrolase class."
  },
  "case_id": "GO_molecular_function_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B6ZKN1 (GLU9_CARIP, sequence matched exactly at 540 AA) is annotated with GO:0008422 (beta-glucosidase activity) with evidence code IDA (Inferred from Direct Assay, ECO:0000314). The function comment states 'Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside,' and two catalytic activity reactions confirm hydrolysis of glycosidic bonds releasing D-glucose. The EC number 3.2.1.- places it in the glycosidase class. All evidence is from direct experimental assay (PubMed:18927081)."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-06-18, which may postdate the benchmark construction; however, the underlying experimental data is from 2008 (PubMed:18927081).",
    "The sequence match is exact (540 AA, identical SHA256) between the benchmark input and the UniProt entry.",
    "The GO annotation uses IDA (direct assay) evidence, representing the highest-confidence annotation type.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely on sequence analysis and training knowledge alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are functionally very distinct (transferase, dioxygenase, metal-cluster binding, glycosidase). The experimental evidence unambiguously supports D. No other option is defensible given the annotation data."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B6ZKN1 (GLU9_CARIP, sequence matched exactly at 540 AA) is annotated with GO:0008422 (beta-glucosidase activity) with evidence code IDA (Inferred from Direct Assay, ECO:0000314). The function comment states 'Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside,' and two catalytic activity reactions confirm hydrolysis of glycosidic bonds releasing D-glucose. The EC number 3.2.1.- places it in the glycosidase class. All evidence is from direct experimental assay (PubMed:18927081).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H3", "H4", "H5", "H6", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Partial elimination is possible: the 540-residue sequence lacks obvious CxxC motifs (weakening option C, 2Fe-2S binding) and lacks the canonical HxD/E...H triad of 2-oxoglutarate-dependent dioxygenases (weakening option B). However, positively identifying beta-glucosidase activity requires recognizing GH1-family-specific sequence signatures (e.g., the 'NEP' and 'ITEN' catalytic motifs present in this sequence) or knowing that this particular plant protein belongs to glycoside hydrolase family 1. This is specialized family-level sequence knowledge, not general biology.",
    "missing_item_specific_fact": "Recognition that this sequence belongs to glycoside hydrolase family 1 (GH1) beta-glucosidases, identifiable by conserved catalytic motifs such as the 'NEP' box and 'ITEN' motif, or alternatively, database lookup of the specific protein's annotation.",
    "reason": "While general knowledge can eliminate options B and C (absence of dioxygenase and Fe-S cluster motifs), and somewhat weaken A (no obvious RING/HECT/U-box motifs), the positive identification of beta-glucosidase activity from sequence alone requires specialized knowledge of glycoside hydrolase family signatures or memorization of this protein's annotation. A general biologist without training on GH1 motifs would struggle to affirmatively assign 'beta-glucosidase activity' rather than another hydrolase class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are functionally very distinct (transferase, dioxygenase, metal-cluster binding, glycosidase). The experimental evidence unambiguously supports D. No other option is defensible given the annotation data."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-06-18, which may postdate the benchmark construction; however, the underlying experimental data is from 2008 (PubMed:18927081).",
    "The sequence match is exact (540 AA, identical SHA256) between the benchmark input and the UniProt entry.",
    "The GO annotation uses IDA (direct assay) evidence, representing the highest-confidence annotation type.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely on sequence analysis and training knowledge alone."
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

**Accession:** `B6ZKN1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 44. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:22.416766+00:00.  

```json
"B6ZKN1"
```

Source SHA-256: `533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:22.416766+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"3.2.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Ipecac alkaloid beta-glucosidase 9"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"IpeGLU9"}]}}
```

Source SHA-256: `533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:22.416766+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside"}]}
```

Source SHA-256: `533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:22.416766+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:78764"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"name":"deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78763"},{"database":"ChEBI","id":"CHEBI:4167"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:58379"},{"database":"ChEBI","id":"CHEBI:229554"}]}}
```

Source SHA-256: `533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:22.416766+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:78888"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"name":"deacetylisoipecoside + H2O = deacetylisoipecoside aglycone + D-glucose","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78887"},{"database":"ChEBI","id":"CHEBI:4167"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:58091"},{"database":"ChEBI","id":"CHEBI:229557"}]}}
```

Source SHA-256: `533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:22.416766+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"18927081","source":"PubMed"}],"id":"GO:0008422","properties":[{"key":"GoTerm","value":"F:beta-glucosidase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)  
**Locator:** `lines 24-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-02T04:27:24.525722+00:00.  

```text
CC   -!- FUNCTION: Beta-glucosidase catalyzing deglucosylation on N-
CC       deacetylisoipecoside and N-deacetylipecoside.
CC       {ECO:0000269|PubMed:18927081}.
```

Source SHA-256: `e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)  
**Locator:** `lines 27-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-02T04:27:24.525722+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=deacetylipecoside + H2O = deacetylipecoside aglycone + D-
CC         glucose; Xref=Rhea:RHEA:78763, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:58379, ChEBI:CHEBI:229554;
CC         Evidence={ECO:0000269|PubMed:18927081};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78764;
CC         Evidence={ECO:0000269|PubMed:18927081};
```

Source SHA-256: `e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-02T04:27:24.525722+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=deacetylisoipecoside + H2O = deacetylisoipecoside aglycone +
CC         D-glucose; Xref=Rhea:RHEA:78887, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:58091, ChEBI:CHEBI:229557;
CC         Evidence={ECO:0000269|PubMed:18927081};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78888;
CC         Evidence={ECO:0000269|PubMed:18927081};
```

Source SHA-256: `e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)  
**Locator:** `lines 53-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-02T04:27:24.525722+00:00.  

```text
DR   GO; GO:0008422; F:beta-glucosidase activity; IDA:UniProtKB.
```

Source SHA-256: `e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 83077-83111`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008422
name: beta-glucosidase activity
namespace: molecular_function
alt_id: GO:0016983
def: "Catalysis of the hydrolysis of terminal, non-reducing beta-D-glucose residues with release of beta-D-glucose." [EC:3.2.1.21, PMID:12594539]
synonym: "amygdalase activity" NARROW [EC:3.2.1.21]
synonym: "amygdalinase" NARROW [EC:3.2.1.21]
synonym: "arbutinase activity" NARROW []
synonym: "aryl-beta-glucosidase activity" RELATED [EC:3.2.1.21]
synonym: "beta-1,6-glucosidase activity" RELATED [EC:3.2.1.21]
synonym: "beta-D-glucosidase activity" EXACT [EC:3.2.1.21]
synonym: "beta-D-glucoside glucohydrolase activity" RELATED [EC:3.2.1.21]
synonym: "beta-glucoside glucohydrolase activity" EXACT [EC:3.2.1.21]
synonym: "cellobiase activity" NARROW [EC:3.2.1.21]
synonym: "cytokine beta-glucosidase activity" NARROW []
synonym: "elaterase activity" NARROW []
synonym: "emulsin" RELATED [EC:3.2.1.21]
synonym: "gentiobiase activity" NARROW []
synonym: "gentobiase activity" NARROW [EC:3.2.1.21]
synonym: "limarase activity" NARROW []
synonym: "p-nitrophenyl beta-glucosidase activity" NARROW []
synonym: "primeverosidase activity" NARROW []
synonym: "quercetin 3'-O-beta-D-glucopyranoside hydrolase activity" NARROW []
synonym: "quercetin 4'-O-beta-D-glucopyranoside hydrolase activity" NARROW []
synonym: "salicilinase activity" NARROW []
xref: EC:3.2.1.21
xref: MetaCyc:3.2.1.21-RXN
xref: RHEA:69647
xref: RHEA:69655
is_a: GO:0015926 ! glucosidase activity
property_value: skos:exactMatch EC:3.2.1.21
property_value: skos:narrowMatch RHEA:69647
property_value: skos:narrowMatch RHEA:69655

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 189. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
