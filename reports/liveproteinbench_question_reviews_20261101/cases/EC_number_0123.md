# EC_number_0123

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.1.37

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPQVRNPILPGFNPDPSILRVGEDYYIATSTFEWYPGVQIHHSRDLANWELVARPLNRKSQLDMRGNPDSCGIWAPCLSHDGERFWLVYTDVKRKDGSFKDTPNYIVTAEKIEGPWSDPIYINSSGFDPSLFHDDDGRKWFVNMLWDHRRRPQLFEGIVLQEFDPKAGKLVGPRKNIFTGTDLALVEGPHLYKRNGWYYLLTAEGGTGYEHACTFARSRNIWGPYEVHPQKYILTSKDHPHAALQRAGHGDIVDTPDGRTYLVHLTGRPTTQFRRCVLGRETAIQEAYWGDDDWLYVKNGPVPSLWVDLPAARDDTKYWEEKRYTFESGLHKDFQWLRTPETDRIFRTREDGKLTLIGRESIGSWFEQALVARRQTHFSCDAETVIDFSPEDQRQFAGLTAYYCRYNFFYLAVSAHSDGQRELFIMASEASWPLGELRYPVPEGVRIPNEGKVRLALTIRGRELQFYYALEGEELKKIGPVLDASIVSDECGGHQKHGSFTGAFVGVAASDLNGTAAEATFDYFIYRPVQHPSDRYEI

[Multiple Choices]
A. 3.2.1.37
B. 3.2.1.18
C. 2.7.8.7
D. 1.5.1.38
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

> The supplied sequence exactly matches the 538-aa UniProt entry annotated with EC 3.2.1.37. The entry links that catalytic activity to ECO:0000269 evidence and PubMed 24262572, supporting the key beyond a purely computational prediction. The excerpts do not independently verify the primary study.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone provides no concrete basis in the prompt for distinguishing the specific xylosidase reaction from other possible enzyme activities or for selecting its precise EC number.


**Missing item-specific fact**

> The protein-specific catalytic activity—hydrolysis of beta-D-xylans to release terminal xylose residues—would be needed to identify EC 3.2.1.37.


**Reason**

> The key is supported by sequence-matched annotation and cited experimental evidence, but those facts are absent from the model input. Recognizing or retrieving this particular protein's annotation is lookup dependence, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only A is supported by the supplied evidence. However, the annotated protein is bifunctional and also has EC 3.2.1.55 activity, which is not offered; thus the singular wording does not represent all annotated activities.


### Important caveats

- The UniProt entry and its sequence match are reviewer-only evidence, not information supplied to the evaluated model.
- The annotation also assigns EC 3.2.1.55, supported by the same cited publication; this is an omitted activity, not another listed answer.
- The exact author data-source snapshot is unknown, though the sequence matches both current and historical records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone provides no concrete basis in the prompt for distinguishing the specific xylosidase reaction from other possible enzyme activities or for selecting its precise EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity—hydrolysis of beta-D-xylans to release terminal xylose residues—would be needed to identify EC 3.2.1.37.",
    "reason": "The key is supported by sequence-matched annotation and cited experimental evidence, but those facts are absent from the model input. Recognizing or retrieving this particular protein's annotation is lookup dependence, not sequence-based reasoning."
  },
  "case_id": "EC_number_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 538-aa UniProt entry annotated with EC 3.2.1.37. The entry links that catalytic activity to ECO:0000269 evidence and PubMed 24262572, supporting the key beyond a purely computational prediction. The excerpts do not independently verify the primary study."
  },
  "important_caveats": [
    "The UniProt entry and its sequence match are reviewer-only evidence, not information supplied to the evaluated model.",
    "The annotation also assigns EC 3.2.1.55, supported by the same cited publication; this is an omitted activity, not another listed answer.",
    "The exact author data-source snapshot is unknown, though the sequence matches both current and historical records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only A is supported by the supplied evidence. However, the annotated protein is bifunctional and also has EC 3.2.1.55 activity, which is not offered; thus the singular wording does not represent all annotated activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 538-aa UniProt entry annotated with EC 3.2.1.37. The entry links that catalytic activity to ECO:0000269 evidence and PubMed 24262572, supporting the key beyond a purely computational prediction. The excerpts do not independently verify the primary study.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone provides no concrete basis in the prompt for distinguishing the specific xylosidase reaction from other possible enzyme activities or for selecting its precise EC number.",
    "missing_item_specific_fact": "The protein-specific catalytic activity—hydrolysis of beta-D-xylans to release terminal xylose residues—would be needed to identify EC 3.2.1.37.",
    "reason": "The key is supported by sequence-matched annotation and cited experimental evidence, but those facts are absent from the model input. Recognizing or retrieving this particular protein's annotation is lookup dependence, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only A is supported by the supplied evidence. However, the annotated protein is bifunctional and also has EC 3.2.1.55 activity, which is not offered; thus the singular wording does not represent all annotated activities."
  },
  "important_caveats": [
    "The UniProt entry and its sequence match are reviewer-only evidence, not information supplied to the evaluated model.",
    "The annotation also assigns EC 3.2.1.55, supported by the same cited publication; this is an omitted activity, not another listed answer.",
    "The exact author data-source snapshot is unknown, though the sequence matches both current and historical records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry V9TT49 (XY43B_HUMIN, Humicola insolens) is annotated with EC 3.2.1.37 (Beta-xylosidase) with direct experimental evidence (ECO:0000269|PubMed:24262572). The catalytic activity is described as 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.' The sequence in the question matches the UniProt sequence exactly (SHA256 match confirmed). Although the protein is also annotated with EC 3.2.1.55 (alpha-L-arabinofuranosidase), that EC number is not among the answer choices, so 3.2.1.37 is the uniquely correct option.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could argue from general principles that the 538-residue fungal protein lacks Rossmann-fold or nucleotide-binding motifs (arguing against D: oxidoreductase and C: transferase), narrowing to glycoside hydrolases (A or B). However, distinguishing beta-xylosidase (3.2.1.37, GH43 family) from alpha-galactosidase (3.2.1.18, GH27/GH36 family) from sequence alone requires recognition of specific GH43 catalytic motifs (e.g., the conserved Asp-His-Asp triad in a beta-propeller fold) or memorization of the exact sequence's database annotation.


**Missing item-specific fact**

> The specific substrate specificity of this protein (beta-xylosidase vs. alpha-galactosidase) is an experimentally determined functional annotation (PubMed:24262572). Without recognizing the exact sequence or knowing GH43-specific catalytic motifs, a model cannot reliably distinguish 3.2.1.37 from 3.2.1.18 based on general biological reasoning alone.


**Reason**

> While the sequence class (hydrolase vs. transferase/oxidoreductase) might be partially inferable, the critical distinction between the two glycoside hydrolase options (A vs. B) depends on knowing this particular protein's substrate specificity, which is an item-specific experimental annotation not derivable from generic sequence features accessible to a general model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is bifunctional (EC 3.2.1.37 and 3.2.1.55), but only EC 3.2.1.37 appears among the choices. Options B (3.2.1.18, alpha-galactosidase), C (2.7.8.7, cytidylyltransferase), and D (1.5.1.38, dihydrofolate reductase) are all clearly different enzymes not matching this protein's annotation. No ambiguity exists among the provided choices.


### Important caveats

- The protein is annotated as bifunctional (GH43 beta-xylosidase AND alpha-L-arabinofuranosidase). The question selects only one EC number (3.2.1.37), which is the primary/recommended activity listed first in UniProt.
- The EC 3.2.1.37 annotation carries experimental evidence (ECO:0000269) from PubMed:24262572, not merely computational prediction.
- The UniProt entry was first released in Swiss-Prot in February 2025; the underlying experimental characterization dates to 2014.
- The accession V9TT49 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could argue from general principles that the 538-residue fungal protein lacks Rossmann-fold or nucleotide-binding motifs (arguing against D: oxidoreductase and C: transferase), narrowing to glycoside hydrolases (A or B). However, distinguishing beta-xylosidase (3.2.1.37, GH43 family) from alpha-galactosidase (3.2.1.18, GH27/GH36 family) from sequence alone requires recognition of specific GH43 catalytic motifs (e.g., the conserved Asp-His-Asp triad in a beta-propeller fold) or memorization of the exact sequence's database annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this protein (beta-xylosidase vs. alpha-galactosidase) is an experimentally determined functional annotation (PubMed:24262572). Without recognizing the exact sequence or knowing GH43-specific catalytic motifs, a model cannot reliably distinguish 3.2.1.37 from 3.2.1.18 based on general biological reasoning alone.",
    "reason": "While the sequence class (hydrolase vs. transferase/oxidoreductase) might be partially inferable, the critical distinction between the two glycoside hydrolase options (A vs. B) depends on knowing this particular protein's substrate specificity, which is an item-specific experimental annotation not derivable from generic sequence features accessible to a general model."
  },
  "case_id": "EC_number_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry V9TT49 (XY43B_HUMIN, Humicola insolens) is annotated with EC 3.2.1.37 (Beta-xylosidase) with direct experimental evidence (ECO:0000269|PubMed:24262572). The catalytic activity is described as 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.' The sequence in the question matches the UniProt sequence exactly (SHA256 match confirmed). Although the protein is also annotated with EC 3.2.1.55 (alpha-L-arabinofuranosidase), that EC number is not among the answer choices, so 3.2.1.37 is the uniquely correct option."
  },
  "important_caveats": [
    "The protein is annotated as bifunctional (GH43 beta-xylosidase AND alpha-L-arabinofuranosidase). The question selects only one EC number (3.2.1.37), which is the primary/recommended activity listed first in UniProt.",
    "The EC 3.2.1.37 annotation carries experimental evidence (ECO:0000269) from PubMed:24262572, not merely computational prediction.",
    "The UniProt entry was first released in Swiss-Prot in February 2025; the underlying experimental characterization dates to 2014.",
    "The accession V9TT49 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (EC 3.2.1.37 and 3.2.1.55), but only EC 3.2.1.37 appears among the choices. Options B (3.2.1.18, alpha-galactosidase), C (2.7.8.7, cytidylyltransferase), and D (1.5.1.38, dihydrofolate reductase) are all clearly different enzymes not matching this protein's annotation. No ambiguity exists among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry V9TT49 (XY43B_HUMIN, Humicola insolens) is annotated with EC 3.2.1.37 (Beta-xylosidase) with direct experimental evidence (ECO:0000269|PubMed:24262572). The catalytic activity is described as 'Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini.' The sequence in the question matches the UniProt sequence exactly (SHA256 match confirmed). Although the protein is also annotated with EC 3.2.1.55 (alpha-L-arabinofuranosidase), that EC number is not among the answer choices, so 3.2.1.37 is the uniquely correct option.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could argue from general principles that the 538-residue fungal protein lacks Rossmann-fold or nucleotide-binding motifs (arguing against D: oxidoreductase and C: transferase), narrowing to glycoside hydrolases (A or B). However, distinguishing beta-xylosidase (3.2.1.37, GH43 family) from alpha-galactosidase (3.2.1.18, GH27/GH36 family) from sequence alone requires recognition of specific GH43 catalytic motifs (e.g., the conserved Asp-His-Asp triad in a beta-propeller fold) or memorization of the exact sequence's database annotation.",
    "missing_item_specific_fact": "The specific substrate specificity of this protein (beta-xylosidase vs. alpha-galactosidase) is an experimentally determined functional annotation (PubMed:24262572). Without recognizing the exact sequence or knowing GH43-specific catalytic motifs, a model cannot reliably distinguish 3.2.1.37 from 3.2.1.18 based on general biological reasoning alone.",
    "reason": "While the sequence class (hydrolase vs. transferase/oxidoreductase) might be partially inferable, the critical distinction between the two glycoside hydrolase options (A vs. B) depends on knowing this particular protein's substrate specificity, which is an item-specific experimental annotation not derivable from generic sequence features accessible to a general model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (EC 3.2.1.37 and 3.2.1.55), but only EC 3.2.1.37 appears among the choices. Options B (3.2.1.18, alpha-galactosidase), C (2.7.8.7, cytidylyltransferase), and D (1.5.1.38, dihydrofolate reductase) are all clearly different enzymes not matching this protein's annotation. No ambiguity exists among the provided choices."
  },
  "important_caveats": [
    "The protein is annotated as bifunctional (GH43 beta-xylosidase AND alpha-L-arabinofuranosidase). The question selects only one EC number (3.2.1.37), which is the primary/recommended activity listed first in UniProt.",
    "The EC 3.2.1.37 annotation carries experimental evidence (ECO:0000269) from PubMed:24262572, not merely computational prediction.",
    "The UniProt entry was first released in Swiss-Prot in February 2025; the underlying experimental characterization dates to 2014.",
    "The accession V9TT49 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
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

**Accession:** `V9TT49` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
"V9TT49"
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
{"includes":[{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"1,4-beta-D-xylan xylohydrolase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Xylan 1,4-beta-xylosidase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"3.2.1.37"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Beta-xylosidase"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"3.2.1.55"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Alpha-L-arabinofuranosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Arabinosidase"}]}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Xylosidase/arabinosidase 43B"}}}
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TT49.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.461216+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.37","evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"name":"Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-xylose residues from the non-reducing termini."}}
```

Source SHA-256: `8d044aa2ece80e75b696bdeb84b0c6b83f2e8688f7e3e654cb8a18c760731a93`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)  
**Locator:** `lines 6-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:28:54.377134+00:00.  

```text
DE   RecName: Full=Xylosidase/arabinosidase 43B {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Beta-xylosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.37 {ECO:0000269|PubMed:24262572};
DE     AltName: Full=1,4-beta-D-xylan xylohydrolase {ECO:0000303|PubMed:24262572};
DE     AltName: Full=Xylan 1,4-beta-xylosidase {ECO:0000303|PubMed:24262572};
DE   Includes:
DE     RecName: Full=Alpha-L-arabinofuranosidase {ECO:0000303|PubMed:24262572};
DE              Short=Arabinosidase {ECO:0000303|PubMed:24262572};
DE              EC=3.2.1.55 {ECO:0000269|PubMed:24262572};
```

Source SHA-256: `7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TT49?format=txt&versions=19)  
**Locator:** `lines 46-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:28:54.377134+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of (1->4)-beta-D-xylans, to remove successive D-
CC         xylose residues from the non-reducing termini.; EC=3.2.1.37;
CC         Evidence={ECO:0000269|PubMed:24262572};
```

Source SHA-256: `7c94683d359fe3e29e3c6666c62dc5a8fefeee44cff7107932217aa0e610488c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
