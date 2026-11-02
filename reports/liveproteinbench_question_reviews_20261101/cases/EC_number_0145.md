# EC_number_0145

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.1.1.395

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
METVQSSSSAELLRAQTHFSTQLFSFQNYASLKCALHLGIPDAIKQHGKPMNLSELTSALPIKPSKAPYIHRLMRMLVKAGYFAQENECFDLTPIGLLLLKDDPINIRALVLLELHPALLLPWIALSEWFQNDDATPFVTAHGKSFWDYTSRDPEFRKLFDEAMAGDSELISKVLVTEFKYVFEGLKSLVDVGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEGVVELEKNAGNEYAGLENLDMEMLVLYNSKERTKKEWAKLFSDAGFSDYKFIPALDSWCIIELTP

[Multiple Choices]
A. 2.1.1.353
B. 1.14.13.247
C. 2.1.1.395
D. 2.7.8.7
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

> The exact sequence matches the annotated Carapichea ipecacuanha CiOMT entry. The annotation assigns EC 2.1.1.395 to an experimentally evidenced methylation reaction, supporting choice C; the cited evidence is database annotation linked to PubMed, not independent review of the primary study here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may support a methyltransferase-like function and make the broad transferase class more plausible than the oxidoreductase or phosphotransferase options, but they do not establish the particular substrate and methylation site required for EC 2.1.1.395.


**Missing item-specific fact**

> The enzyme's specific catalytic activity on 7'-O-demethylcephaeline, as established by protein-specific functional evidence or an external annotation, is not supplied.


**Reason**

> Distinguishing this precise EC subnumber from other methyltransferase choices requires substrate-specific information absent from the sequence prompt; recognizing the sequence or recalling its annotation would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, the supplied reviewer evidence supports C. The entry also assigns this protein EC 2.1.1.396 for a distinct cephaeline methylation reaction, but that EC number is not offered.


### Important caveats

- The exact sequence match and functional annotation are reviewer-only evidence, not information provided to the evaluated model.
- The source annotates the protein with both EC 2.1.1.395 and EC 2.1.1.396, so the singular framing omits a second annotated catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may support a methyltransferase-like function and make the broad transferase class more plausible than the oxidoreductase or phosphotransferase options, but they do not establish the particular substrate and methylation site required for EC 2.1.1.395.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's specific catalytic activity on 7'-O-demethylcephaeline, as established by protein-specific functional evidence or an external annotation, is not supplied.",
    "reason": "Distinguishing this precise EC subnumber from other methyltransferase choices requires substrate-specific information absent from the sequence prompt; recognizing the sequence or recalling its annotation would be lookup or memorization."
  },
  "case_id": "EC_number_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Carapichea ipecacuanha CiOMT entry. The annotation assigns EC 2.1.1.395 to an experimentally evidenced methylation reaction, supporting choice C; the cited evidence is database annotation linked to PubMed, not independent review of the primary study here."
  },
  "important_caveats": [
    "The exact sequence match and functional annotation are reviewer-only evidence, not information provided to the evaluated model.",
    "The source annotates the protein with both EC 2.1.1.395 and EC 2.1.1.396, so the singular framing omits a second annotated catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the supplied reviewer evidence supports C. The entry also assigns this protein EC 2.1.1.396 for a distinct cephaeline methylation reaction, but that EC number is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Carapichea ipecacuanha CiOMT entry. The annotation assigns EC 2.1.1.395 to an experimentally evidenced methylation reaction, supporting choice C; the cited evidence is database annotation linked to PubMed, not independent review of the primary study here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may support a methyltransferase-like function and make the broad transferase class more plausible than the oxidoreductase or phosphotransferase options, but they do not establish the particular substrate and methylation site required for EC 2.1.1.395.",
    "missing_item_specific_fact": "The enzyme's specific catalytic activity on 7'-O-demethylcephaeline, as established by protein-specific functional evidence or an external annotation, is not supplied.",
    "reason": "Distinguishing this precise EC subnumber from other methyltransferase choices requires substrate-specific information absent from the sequence prompt; recognizing the sequence or recalling its annotation would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the supplied reviewer evidence supports C. The entry also assigns this protein EC 2.1.1.396 for a distinct cephaeline methylation reaction, but that EC number is not offered."
  },
  "important_caveats": [
    "The exact sequence match and functional annotation are reviewer-only evidence, not information provided to the evaluated model.",
    "The source annotates the protein with both EC 2.1.1.395 and EC 2.1.1.396, so the singular framing omits a second annotated catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E7FL15 (CIOMT_CARIP) from Carapichea ipecacuanha is experimentally annotated with EC 2.1.1.395 (7'-O-demethylcephaeline + SAM → cephaeline + SAH + H⁺; ECO:0000269|PubMed:21228475) as an alternative name, alongside EC 2.1.1.396 as the recommended name. EC 2.1.1.395 is a valid, experimentally supported EC number for this protein. Since EC 2.1.1.396 is not among the answer choices, option C is the only choice matching this protein's annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a plant-type SAM-binding motif (e.g., 'GDMFDRVPSADAILLKIVLHDWSD' region) and a Rossmann-like fold architecture consistent with a class 2.1.1 O-methyltransferase. This general reasoning can eliminate option B (EC 1.14.13.247, an oxidoreductase/monooxygenase) and option D (EC 2.7.8.7, a phosphorus-transferase). However, distinguishing between EC 2.1.1.353 (option A) and EC 2.1.1.395 (option C) requires knowledge of the exact substrate specificity (7'-O-demethylcephaeline as acceptor) and the specific reaction position of methylation, which is a protein-specific experimental fact not derivable from sequence motifs alone.


**Missing item-specific fact**

> The precise substrate identity (7'-O-demethylcephaeline) and methylation position (7'-O) that define EC 2.1.1.395 versus other EC 2.1.1.x methyltransferases. This requires knowing that this particular Carapichea ipecacuanha enzyme is the 'cephaeline synthase' acting at the 7'-hydroxyl, an experimental finding from Cheong et al. 2011 (PubMed:21228475).


**Reason**

> While general methyltransferase motifs allow narrowing to the 2.1.1.x class, the final distinction between two EC 2.1.1.xxx numbers depends on protein-specific substrate-reaction knowledge that cannot be deduced from sequence alone without database lookup or memorization of this enzyme's characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only EC 2.1.1.395 matches this protein. The enzyme also carries EC 2.1.1.396 (recommended name) but that number is not offered as an option, so no ambiguity arises within the given choices. Options A, B, and D correspond to unrelated enzyme classes or unrelated methyltransferase reactions.


### Important caveats

- The UniProt recommended name for E7FL15 is EC 2.1.1.396 (Cephaeline 6'-O-methyltransferase / Emetine synthase), while EC 2.1.1.395 is listed as an alternative name. Both are experimentally supported (ECO:0000269). The question's phrasing 'the most accurate EC number' could arguably favor 2.1.1.396, but since it is absent from the choices, C remains the only valid answer.
- The enzyme is bifunctional, catalyzing two sequential methylation steps in the emetine biosynthetic pathway. Assigning a single EC number is inherently incomplete.
- The sequence-match is confirmed (SHA-256 identical between benchmark input and UniProt entry E7FL15, 350 aa).
- EC 2.1.1.353 is a valid methyltransferase EC number but corresponds to a different substrate/reaction, making it a plausible but incorrect distractor for someone who identifies the enzyme class but not the specific substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a plant-type SAM-binding motif (e.g., 'GDMFDRVPSADAILLKIVLHDWSD' region) and a Rossmann-like fold architecture consistent with a class 2.1.1 O-methyltransferase. This general reasoning can eliminate option B (EC 1.14.13.247, an oxidoreductase/monooxygenase) and option D (EC 2.7.8.7, a phosphorus-transferase). However, distinguishing between EC 2.1.1.353 (option A) and EC 2.1.1.395 (option C) requires knowledge of the exact substrate specificity (7'-O-demethylcephaeline as acceptor) and the specific reaction position of methylation, which is a protein-specific experimental fact not derivable from sequence motifs alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise substrate identity (7'-O-demethylcephaeline) and methylation position (7'-O) that define EC 2.1.1.395 versus other EC 2.1.1.x methyltransferases. This requires knowing that this particular Carapichea ipecacuanha enzyme is the 'cephaeline synthase' acting at the 7'-hydroxyl, an experimental finding from Cheong et al. 2011 (PubMed:21228475).",
    "reason": "While general methyltransferase motifs allow narrowing to the 2.1.1.x class, the final distinction between two EC 2.1.1.xxx numbers depends on protein-specific substrate-reaction knowledge that cannot be deduced from sequence alone without database lookup or memorization of this enzyme's characterization."
  },
  "case_id": "EC_number_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E7FL15 (CIOMT_CARIP) from Carapichea ipecacuanha is experimentally annotated with EC 2.1.1.395 (7'-O-demethylcephaeline + SAM → cephaeline + SAH + H⁺; ECO:0000269|PubMed:21228475) as an alternative name, alongside EC 2.1.1.396 as the recommended name. EC 2.1.1.395 is a valid, experimentally supported EC number for this protein. Since EC 2.1.1.396 is not among the answer choices, option C is the only choice matching this protein's annotation."
  },
  "important_caveats": [
    "The UniProt recommended name for E7FL15 is EC 2.1.1.396 (Cephaeline 6'-O-methyltransferase / Emetine synthase), while EC 2.1.1.395 is listed as an alternative name. Both are experimentally supported (ECO:0000269). The question's phrasing 'the most accurate EC number' could arguably favor 2.1.1.396, but since it is absent from the choices, C remains the only valid answer.",
    "The enzyme is bifunctional, catalyzing two sequential methylation steps in the emetine biosynthetic pathway. Assigning a single EC number is inherently incomplete.",
    "The sequence-match is confirmed (SHA-256 identical between benchmark input and UniProt entry E7FL15, 350 aa).",
    "EC 2.1.1.353 is a valid methyltransferase EC number but corresponds to a different substrate/reaction, making it a plausible but incorrect distractor for someone who identifies the enzyme class but not the specific substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only EC 2.1.1.395 matches this protein. The enzyme also carries EC 2.1.1.396 (recommended name) but that number is not offered as an option, so no ambiguity arises within the given choices. Options A, B, and D correspond to unrelated enzyme classes or unrelated methyltransferase reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E7FL15 (CIOMT_CARIP) from Carapichea ipecacuanha is experimentally annotated with EC 2.1.1.395 (7'-O-demethylcephaeline + SAM → cephaeline + SAH + H⁺; ECO:0000269|PubMed:21228475) as an alternative name, alongside EC 2.1.1.396 as the recommended name. EC 2.1.1.395 is a valid, experimentally supported EC number for this protein. Since EC 2.1.1.396 is not among the answer choices, option C is the only choice matching this protein's annotation.",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a plant-type SAM-binding motif (e.g., 'GDMFDRVPSADAILLKIVLHDWSD' region) and a Rossmann-like fold architecture consistent with a class 2.1.1 O-methyltransferase. This general reasoning can eliminate option B (EC 1.14.13.247, an oxidoreductase/monooxygenase) and option D (EC 2.7.8.7, a phosphorus-transferase). However, distinguishing between EC 2.1.1.353 (option A) and EC 2.1.1.395 (option C) requires knowledge of the exact substrate specificity (7'-O-demethylcephaeline as acceptor) and the specific reaction position of methylation, which is a protein-specific experimental fact not derivable from sequence motifs alone.",
    "missing_item_specific_fact": "The precise substrate identity (7'-O-demethylcephaeline) and methylation position (7'-O) that define EC 2.1.1.395 versus other EC 2.1.1.x methyltransferases. This requires knowing that this particular Carapichea ipecacuanha enzyme is the 'cephaeline synthase' acting at the 7'-hydroxyl, an experimental finding from Cheong et al. 2011 (PubMed:21228475).",
    "reason": "While general methyltransferase motifs allow narrowing to the 2.1.1.x class, the final distinction between two EC 2.1.1.xxx numbers depends on protein-specific substrate-reaction knowledge that cannot be deduced from sequence alone without database lookup or memorization of this enzyme's characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only EC 2.1.1.395 matches this protein. The enzyme also carries EC 2.1.1.396 (recommended name) but that number is not offered as an option, so no ambiguity arises within the given choices. Options A, B, and D correspond to unrelated enzyme classes or unrelated methyltransferase reactions."
  },
  "important_caveats": [
    "The UniProt recommended name for E7FL15 is EC 2.1.1.396 (Cephaeline 6'-O-methyltransferase / Emetine synthase), while EC 2.1.1.395 is listed as an alternative name. Both are experimentally supported (ECO:0000269). The question's phrasing 'the most accurate EC number' could arguably favor 2.1.1.396, but since it is absent from the choices, C remains the only valid answer.",
    "The enzyme is bifunctional, catalyzing two sequential methylation steps in the emetine biosynthetic pathway. Assigning a single EC number is inherently incomplete.",
    "The sequence-match is confirmed (SHA-256 identical between benchmark input and UniProt entry E7FL15, 350 aa).",
    "EC 2.1.1.353 is a valid methyltransferase EC number but corresponds to a different substrate/reaction, making it a plausible but incorrect distractor for someone who identifies the enzyme class but not the specific substrate."
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

**Accession:** `E7FL15` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:03.494312+00:00.  

```json
"E7FL15"
```

Source SHA-256: `609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:03.494312+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21228475","source":"PubMed"}],"value":"2.1.1.395"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"7'-O-demethylcephaeline 7'-O-methyltransferase CiOMT"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"Cephaeline synthase CiOMT"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"},{"evidenceCode":"ECO:0000312","id":"BAJ72588.1","source":"EMBL"}],"value":"7'-O-demethylcephaeline/cephaeline O-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ72588.1","source":"EMBL"}],"value":"7'OMT"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"CiOMT"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21228475","source":"PubMed"}],"value":"2.1.1.396"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"Cephaeline 6'-O-methyltransferase CiOMT"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"Emetine synthase CiOMT"}]}}
```

Source SHA-256: `609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:03.494312+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"21228475","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:80556"}}],"reaction":{"ecNumber":"2.1.1.395","evidences":[{"evidenceCode":"ECO:0000269","id":"21228475","source":"PubMed"}],"name":"7'-O-demethylcephaeline + S-adenosyl-L-methionine = cephaeline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80555"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:231587"},{"database":"ChEBI","id":"CHEBI:231589"}]}}
```

Source SHA-256: `609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:03.494312+00:00.  

```json
{"citation":{"authors":["Cheong B.E.","Takemura T.","Yoshimatsu K.","Sato F."],"citationCrossReferences":[{"database":"PubMed","id":"21228475"},{"database":"DOI","id":"10.1271/bbb.100605"}],"citationType":"journal article","firstPage":"107","id":"21228475","journal":"Biosci. Biotechnol. Biochem.","lastPage":"113","publicationDate":"2011","title":"Molecular cloning of an O-methyltransferase from adventitious roots of Carapichea ipecacuanha.","volume":"75"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ72588.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Root"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION"]}
```

Source SHA-256: `609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)  
**Locator:** `lines 1-21`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:05.930954+00:00.  

```text
ID   CIOMT_CARIP             Reviewed;         350 AA.
AC   E7FL15;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-APR-2011, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Cephaeline 6'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};
DE            Short=Emetine synthase CiOMT {ECO:0000303|PubMed:21228475};
DE            EC=2.1.1.396 {ECO:0000269|PubMed:21228475};
DE   AltName: Full=7'-O-demethylcephaeline 7'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};
DE            Short=Cephaeline synthase CiOMT {ECO:0000303|PubMed:21228475};
DE            EC=2.1.1.395 {ECO:0000269|PubMed:21228475};
DE   AltName: Full=7'-O-demethylcephaeline/cephaeline O-methyltransferase {ECO:0000303|PubMed:21228475, ECO:0000312|EMBL:BAJ72588.1};
DE            Short=7'OMT {ECO:0000312|EMBL:BAJ72588.1};
DE            Short=CiOMT {ECO:0000303|PubMed:21228475};
GN   Name=OMT {ECO:0000303|PubMed:21228475};
OS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;
OC   Carapichea.
OX   NCBI_TaxID=77880;
```

Source SHA-256: `aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)  
**Locator:** `lines 6-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:05.930954+00:00.  

```text
DE   RecName: Full=Cephaeline 6'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};
DE            Short=Emetine synthase CiOMT {ECO:0000303|PubMed:21228475};
DE            EC=2.1.1.396 {ECO:0000269|PubMed:21228475};
DE   AltName: Full=7'-O-demethylcephaeline 7'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};
DE            Short=Cephaeline synthase CiOMT {ECO:0000303|PubMed:21228475};
DE            EC=2.1.1.395 {ECO:0000269|PubMed:21228475};
DE   AltName: Full=7'-O-demethylcephaeline/cephaeline O-methyltransferase {ECO:0000303|PubMed:21228475, ECO:0000312|EMBL:BAJ72588.1};
DE            Short=7'OMT {ECO:0000312|EMBL:BAJ72588.1};
DE            Short=CiOMT {ECO:0000303|PubMed:21228475};
```

Source SHA-256: `aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)  
**Locator:** `lines 39-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:05.930954+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=7'-O-demethylcephaeline + S-adenosyl-L-methionine = cephaeline
CC         + S-adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:80555,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:231587, ChEBI:CHEBI:231589; EC=2.1.1.395;
CC         Evidence={ECO:0000269|PubMed:21228475};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80556;
CC         Evidence={ECO:0000269|PubMed:21228475};
```

Source SHA-256: `aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 145. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
