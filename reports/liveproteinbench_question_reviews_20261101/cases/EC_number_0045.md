# EC_number_0045

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.2.1.70

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSKTDFSHDLLRFSDEVKEALHSGKPVVALESTVIAHGLPYPENVATARKIEAAVRAEGAIPATIGIENGRFLIGMSDADLERFGSTRGIPKASSRDIPVILAQGGMGATTVASSLVAADLAGIPFFASAGIGGVHRGAERSMDISADLIQFTRSRVAVVCAGAKSILDLGLTLEYLETQCVPIISYQSDDFPAFYCRSSGFHSPHRLDDATVIARSIDMHWKLGNQSSVLITHPIHEEDAIGTDEVESIIREAAVQAEHEGIRGPGATPYLMRAVAKATEGKTVKANMSVLISTAALAGKLACAHIDYLRQQNQA

[Multiple Choices]
A. 4.2.1.18
B. 3.1.1.29
C. 4.2.1.70
D. 4.1.1.129
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

> The exact sequence matches UniProt entry Q9L393, whose EC 4.2.1.70 annotation and catalytic reaction are assigned by the HAMAP computational rule MF_01876. This supports the key as a database-based functional inference, not as independently established experimental evidence in the supplied sources.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a bacterial protein, but its length and sequence alone provide no broadly recognizable, general biological argument that identifies the specific EC reaction over the alternatives.


**Missing item-specific fact**

> The protein's identity as a pseudouridine-5'-phosphate glycosidase, or equivalent family/function annotation linking it to EC 4.2.1.70.


**Reason**

> Choosing the specific EC number requires protein-specific functional knowledge or sequence-family identification. The reviewer-only annotation supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched database annotation supports one listed EC number; the limitation is that this annotation is not provided in the question, rather than evidence that multiple options fit equally well.


### Important caveats

- The sequence match is exact, including in the historical UniProt record checked.
- The cited EC assignment is based on a HAMAP computational rule; the supplied evidence does not independently establish experimental validation.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a bacterial protein, but its length and sequence alone provide no broadly recognizable, general biological argument that identifies the specific EC reaction over the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as a pseudouridine-5'-phosphate glycosidase, or equivalent family/function annotation linking it to EC 4.2.1.70.",
    "reason": "Choosing the specific EC number requires protein-specific functional knowledge or sequence-family identification. The reviewer-only annotation supports the key but was not supplied to the evaluated model."
  },
  "case_id": "EC_number_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q9L393, whose EC 4.2.1.70 annotation and catalytic reaction are assigned by the HAMAP computational rule MF_01876. This supports the key as a database-based functional inference, not as independently established experimental evidence in the supplied sources."
  },
  "important_caveats": [
    "The sequence match is exact, including in the historical UniProt record checked.",
    "The cited EC assignment is based on a HAMAP computational rule; the supplied evidence does not independently establish experimental validation.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports one listed EC number; the limitation is that this annotation is not provided in the question, rather than evidence that multiple options fit equally well."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q9L393, whose EC 4.2.1.70 annotation and catalytic reaction are assigned by the HAMAP computational rule MF_01876. This supports the key as a database-based functional inference, not as independently established experimental evidence in the supplied sources.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a bacterial protein, but its length and sequence alone provide no broadly recognizable, general biological argument that identifies the specific EC reaction over the alternatives.",
    "missing_item_specific_fact": "The protein's identity as a pseudouridine-5'-phosphate glycosidase, or equivalent family/function annotation linking it to EC 4.2.1.70.",
    "reason": "Choosing the specific EC number requires protein-specific functional knowledge or sequence-family identification. The reviewer-only annotation supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports one listed EC number; the limitation is that this annotation is not provided in the question, rather than evidence that multiple options fit equally well."
  },
  "important_caveats": [
    "The sequence match is exact, including in the historical UniProt record checked.",
    "The cited EC assignment is based on a HAMAP computational rule; the supplied evidence does not independently establish experimental validation.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9L393 (PSUG_DICD3, Dickeya dadantii strain 3937) assigns EC 4.2.1.70 (Pseudouridine-5'-phosphate glycosidase) to this exact 316-aa sequence (SHA256 match confirmed). The annotation is present in both the current entry (v68) and the historical archived entry (v67). However, the evidence code is ECO:0000255|HAMAP-Rule:MF_01876, indicating a computational/probabilistic annotation rather than direct experimental characterization of this enzyme's activity. The original publication (PubMed:11790734) characterized indigoidine biosynthetic genes (indA) but the EC assignment derives from HAMAP rule transfer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H1](#evidence-h1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains motifs (GIPATIG, GGMGATT, GIPFFASAGIGGVHRG) suggestive of a nucleotidyltransferase-like fold, which is consistent with glycosidases acting on nucleotide substrates. This fold-based reasoning could help eliminate B (3.1.1.29, an esterase with a distinct α/β-hydrolase fold), D (4.1.1.129, a decarboxylase), and potentially A (4.2.1.18, isochorismatase, which has an unrelated fold and acts on chorismate derivatives rather than nucleotides). However, within the 4.2.1.x lyase family, the precise assignment to pseudouridine-5'-phosphate glycosidase (4.2.1.70) versus other C-O lyases requires knowledge of the specific substrate-binding residues and HAMAP family membership (MF_01876), which is not derivable from general fold recognition alone.


**Missing item-specific fact**

> The specific substrate specificity of this protein family (pseudouridine-5'-phosphate as substrate) and the HAMAP rule MF_01876 assignment that distinguishes EC 4.2.1.70 from other 4.2.1.x glycosidases. The association of 'indA' gene naming with indigoidine biosynthesis (PubMed:11790734) and the subsequent reclassification as PsiMP glycosidase is an item-specific annotation fact.


**Reason**

> While the nucleotidyltransferase-like fold provides general grounds to favor a nucleotide-acting glycosidase over an esterase or decarboxylase, the precise 4-digit EC number (4.2.1.70 vs. 4.2.1.18 or other 4.2.1.x entries) depends on knowing this particular protein family's substrate specificity, which is established by HAMAP rule annotation rather than by general biological reasoning from sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three EC classes (3.1.1.x hydrolase, 4.1.1.x C-C lyase, 4.2.1.x C-O lyase). The nucleotidyltransferase-like fold and the absence of esterase or decarboxylase catalytic motifs make B and D clearly less plausible. Between A (4.2.1.18, isochorismatase) and C (4.2.1.70), the fold difference is substantial: isochorismatase belongs to a distinct structural family acting on chorismate, not a nucleotide. Thus C is the most defensible choice, though the distinction requires specific family-level knowledge.


### Important caveats

- The EC 4.2.1.70 annotation is based on HAMAP-Rule (ECO:0000255), a computational/probabilistic assignment, not direct experimental enzyme assay evidence.
- The original gene is named 'indA' and was characterized in the context of indigoidine biosynthesis (PubMed:11790734); the PsiMP glycosidase EC assignment was added later via HAMAP rule transfer.
- The protein was first integrated into Swiss-Prot on 2025-02-05 (sequence version 2), so the author's source snapshot and the annotation timeline should be considered.
- The reviewer-only evidence was absent from the evaluated model input; the model had only the 316-aa sequence and four EC number choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs (GIPATIG, GGMGATT, GIPFFASAGIGGVHRG) suggestive of a nucleotidyltransferase-like fold, which is consistent with glycosidases acting on nucleotide substrates. This fold-based reasoning could help eliminate B (3.1.1.29, an esterase with a distinct α/β-hydrolase fold), D (4.1.1.129, a decarboxylase), and potentially A (4.2.1.18, isochorismatase, which has an unrelated fold and acts on chorismate derivatives rather than nucleotides). However, within the 4.2.1.x lyase family, the precise assignment to pseudouridine-5'-phosphate glycosidase (4.2.1.70) versus other C-O lyases requires knowledge of the specific substrate-binding residues and HAMAP family membership (MF_01876), which is not derivable from general fold recognition alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity of this protein family (pseudouridine-5'-phosphate as substrate) and the HAMAP rule MF_01876 assignment that distinguishes EC 4.2.1.70 from other 4.2.1.x glycosidases. The association of 'indA' gene naming with indigoidine biosynthesis (PubMed:11790734) and the subsequent reclassification as PsiMP glycosidase is an item-specific annotation fact.",
    "reason": "While the nucleotidyltransferase-like fold provides general grounds to favor a nucleotide-acting glycosidase over an esterase or decarboxylase, the precise 4-digit EC number (4.2.1.70 vs. 4.2.1.18 or other 4.2.1.x entries) depends on knowing this particular protein family's substrate specificity, which is established by HAMAP rule annotation rather than by general biological reasoning from sequence."
  },
  "case_id": "EC_number_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9L393 (PSUG_DICD3, Dickeya dadantii strain 3937) assigns EC 4.2.1.70 (Pseudouridine-5'-phosphate glycosidase) to this exact 316-aa sequence (SHA256 match confirmed). The annotation is present in both the current entry (v68) and the historical archived entry (v67). However, the evidence code is ECO:0000255|HAMAP-Rule:MF_01876, indicating a computational/probabilistic annotation rather than direct experimental characterization of this enzyme's activity. The original publication (PubMed:11790734) characterized indigoidine biosynthetic genes (indA) but the EC assignment derives from HAMAP rule transfer."
  },
  "important_caveats": [
    "The EC 4.2.1.70 annotation is based on HAMAP-Rule (ECO:0000255), a computational/probabilistic assignment, not direct experimental enzyme assay evidence.",
    "The original gene is named 'indA' and was characterized in the context of indigoidine biosynthesis (PubMed:11790734); the PsiMP glycosidase EC assignment was added later via HAMAP rule transfer.",
    "The protein was first integrated into Swiss-Prot on 2025-02-05 (sequence version 2), so the author's source snapshot and the annotation timeline should be considered.",
    "The reviewer-only evidence was absent from the evaluated model input; the model had only the 316-aa sequence and four EC number choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three EC classes (3.1.1.x hydrolase, 4.1.1.x C-C lyase, 4.2.1.x C-O lyase). The nucleotidyltransferase-like fold and the absence of esterase or decarboxylase catalytic motifs make B and D clearly less plausible. Between A (4.2.1.18, isochorismatase) and C (4.2.1.70), the fold difference is substantial: isochorismatase belongs to a distinct structural family acting on chorismate, not a nucleotide. Thus C is the most defensible choice, though the distinction requires specific family-level knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9L393 (PSUG_DICD3, Dickeya dadantii strain 3937) assigns EC 4.2.1.70 (Pseudouridine-5'-phosphate glycosidase) to this exact 316-aa sequence (SHA256 match confirmed). The annotation is present in both the current entry (v68) and the historical archived entry (v67). However, the evidence code is ECO:0000255|HAMAP-Rule:MF_01876, indicating a computational/probabilistic annotation rather than direct experimental characterization of this enzyme's activity. The original publication (PubMed:11790734) characterized indigoidine biosynthetic genes (indA) but the EC assignment derives from HAMAP rule transfer.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains motifs (GIPATIG, GGMGATT, GIPFFASAGIGGVHRG) suggestive of a nucleotidyltransferase-like fold, which is consistent with glycosidases acting on nucleotide substrates. This fold-based reasoning could help eliminate B (3.1.1.29, an esterase with a distinct α/β-hydrolase fold), D (4.1.1.129, a decarboxylase), and potentially A (4.2.1.18, isochorismatase, which has an unrelated fold and acts on chorismate derivatives rather than nucleotides). However, within the 4.2.1.x lyase family, the precise assignment to pseudouridine-5'-phosphate glycosidase (4.2.1.70) versus other C-O lyases requires knowledge of the specific substrate-binding residues and HAMAP family membership (MF_01876), which is not derivable from general fold recognition alone.",
    "missing_item_specific_fact": "The specific substrate specificity of this protein family (pseudouridine-5'-phosphate as substrate) and the HAMAP rule MF_01876 assignment that distinguishes EC 4.2.1.70 from other 4.2.1.x glycosidases. The association of 'indA' gene naming with indigoidine biosynthesis (PubMed:11790734) and the subsequent reclassification as PsiMP glycosidase is an item-specific annotation fact.",
    "reason": "While the nucleotidyltransferase-like fold provides general grounds to favor a nucleotide-acting glycosidase over an esterase or decarboxylase, the precise 4-digit EC number (4.2.1.70 vs. 4.2.1.18 or other 4.2.1.x entries) depends on knowing this particular protein family's substrate specificity, which is established by HAMAP rule annotation rather than by general biological reasoning from sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three EC classes (3.1.1.x hydrolase, 4.1.1.x C-C lyase, 4.2.1.x C-O lyase). The nucleotidyltransferase-like fold and the absence of esterase or decarboxylase catalytic motifs make B and D clearly less plausible. Between A (4.2.1.18, isochorismatase) and C (4.2.1.70), the fold difference is substantial: isochorismatase belongs to a distinct structural family acting on chorismate, not a nucleotide. Thus C is the most defensible choice, though the distinction requires specific family-level knowledge."
  },
  "important_caveats": [
    "The EC 4.2.1.70 annotation is based on HAMAP-Rule (ECO:0000255), a computational/probabilistic assignment, not direct experimental enzyme assay evidence.",
    "The original gene is named 'indA' and was characterized in the context of indigoidine biosynthesis (PubMed:11790734); the PsiMP glycosidase EC assignment was added later via HAMAP rule transfer.",
    "The protein was first integrated into Swiss-Prot on 2025-02-05 (sequence version 2), so the author's source snapshot and the annotation timeline should be considered.",
    "The reviewer-only evidence was absent from the evaluated model input; the model had only the 316-aa sequence and four EC number choices."
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

**Accession:** `Q9L393` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 67. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:05.918269+00:00.  

```json
"Q9L393"
```

Source SHA-256: `e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:05.918269+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01876","source":"HAMAP-Rule"}],"value":"4.2.1.70"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01876","source":"HAMAP-Rule"}],"value":"Pseudouridine-5'-phosphate glycosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01876","source":"HAMAP-Rule"}],"value":"PsiMP glycosidase"}]}}
```

Source SHA-256: `e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9L393.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:05.918269+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"4.2.1.70","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01876","source":"HAMAP-Rule"}],"name":"D-ribose 5-phosphate + uracil = psi-UMP + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:18337"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:17568"},{"database":"ChEBI","id":"CHEBI:58380"},{"database":"ChEBI","id":"CHEBI:78346"}]}}
```

Source SHA-256: `e759032be015a488064afb4002812a0cd7d67c7a33fdd30fb39167eddef3cb9d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 2.  
**Retrieved:** 2026-11-02T04:33:13.935581+00:00.  

```text
ID   PSUG_DICD3              Reviewed;         316 AA.
AC   Q9L393; E0SMH8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 2.
DT   28-JAN-2026, entry version 67.
DE   RecName: Full=Pseudouridine-5'-phosphate glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};
DE            Short=PsiMP glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};
DE            EC=4.2.1.70 {ECO:0000255|HAMAP-Rule:MF_01876};
GN   Name=indA {ECO:0000303|PubMed:11790734};
GN   Synonyms=psuG {ECO:0000255|HAMAP-Rule:MF_01876};
GN   OrderedLocusNames=Dda3937_00974 {ECO:0000312|EMBL:ADN00617.1};
OS   Dickeya dadantii (strain 3937) (Erwinia chrysanthemi (strain 3937)).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Pectobacteriaceae; Dickeya.
OX   NCBI_TaxID=198628;
```

Source SHA-256: `b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 2.  
**Retrieved:** 2026-11-02T04:33:13.935581+00:00.  

```text
DE   RecName: Full=Pseudouridine-5'-phosphate glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};
DE            Short=PsiMP glycosidase {ECO:0000255|HAMAP-Rule:MF_01876};
DE            EC=4.2.1.70 {ECO:0000255|HAMAP-Rule:MF_01876};
```

Source SHA-256: `b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9L393?format=txt&versions=67)  
**Locator:** `lines 48-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 2.  
**Retrieved:** 2026-11-02T04:33:13.935581+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-ribose 5-phosphate + uracil = psi-UMP + H2O;
CC         Xref=Rhea:RHEA:18337, ChEBI:CHEBI:15377, ChEBI:CHEBI:17568,
CC         ChEBI:CHEBI:58380, ChEBI:CHEBI:78346; EC=4.2.1.70;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_01876};
```

Source SHA-256: `b4ef33743dbb4e6ea7562dc04819ab1d2a209831d0e36c41a3dbb21a465472ea`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
