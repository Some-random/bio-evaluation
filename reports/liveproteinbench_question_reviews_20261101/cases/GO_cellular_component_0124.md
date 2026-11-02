# GO_cellular_component_0124

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — peroxisomal membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | uncertain | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | uncertain | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MESMVNNLWSSWDTLSQATASTGGDMDAASVASKQSPQESKMAASSMIWSSFSEPQKTPPTKRASSSFFDDMFTSSKDHSTTLTDKMFERFLSMALPTTTTQDGEELQSILERIEMQKSRPQLSLNVMSKNAIQLLSRLSVPFVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAYMKRHPPDKHTILQNRNPIPAEGPSVSHVDVPRPVPELSREFVLNSTDLQNHMLLYVMSYDFVTSLIVKYLYFKDENITIFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKEVKETEIFELQHLDPETHNWQLICFSSDPYPANSHARLNNLPLLGTLHLSQVKPPEGWKFVDVETAVNTRSVDGWLLDLTPEGWIKENFLNETMDIDEDEKWCYDLVTKFSYQAGLTTNEKKTRGEVRRRRWIRYCVRDIWDEDDQMEETVAHRRNKSMESSNSLHPVKSIDSVDG

[Multiple Choices]
A. actin cytoskeleton
B. cytosol
C. peroxisomal membrane
D. virus tail, tube
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

### Expected-answer support: uncertain

> The matched sequence has a computational GO annotation for peroxisomal membrane, supporting the key as an annotation-based prediction. However, the matched entry reports experimental localization to the endoplasmic-reticulum membrane, not peroxisomal membrane. The evidence does not establish whether the protein also localizes to peroxisomes or which location is primary.

Citations as saved: [C7](#evidence-c7), [H5](#evidence-h5), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic regions, consistent with a multipass membrane protein; this makes the membrane-associated choice more plausible than the soluble or viral choices, but does not identify the membrane compartment.


**Missing item-specific fact**

> The protein-specific subcellular localization, including whether it localizes to peroxisomes and which compartment is primary.


**Reason**

> General sequence analysis can suggest membrane association, but cannot distinguish peroxisomal membrane from other cellular membranes. Selecting the precise compartment therefore depends on a protein-specific annotation or localization fact absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, peroxisomal membrane is the only membrane compartment, so it is the best-listed option. However, the evidence indicates ER membrane localization, which is not offered, and does not resolve whether peroxisomal localization is also present.


### Important caveats

- The peroxisomal-membrane GO annotation is computationally inferred, whereas the cited ER localization is experimentally supported.
- Reviewer-only database evidence establishes the annotation and localization conflict, but was not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic regions, consistent with a multipass membrane protein; this makes the membrane-associated choice more plausible than the soluble or viral choices, but does not identify the membrane compartment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific subcellular localization, including whether it localizes to peroxisomes and which compartment is primary.",
    "reason": "General sequence analysis can suggest membrane association, but cannot distinguish peroxisomal membrane from other cellular membranes. Selecting the precise compartment therefore depends on a protein-specific annotation or localization fact absent from the question."
  },
  "case_id": "GO_cellular_component_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H5",
      "C5",
      "H3"
    ],
    "judgment": "cannot_determine",
    "reason": "The matched sequence has a computational GO annotation for peroxisomal membrane, supporting the key as an annotation-based prediction. However, the matched entry reports experimental localization to the endoplasmic-reticulum membrane, not peroxisomal membrane. The evidence does not establish whether the protein also localizes to peroxisomes or which location is primary."
  },
  "important_caveats": [
    "The peroxisomal-membrane GO annotation is computationally inferred, whereas the cited ER localization is experimentally supported.",
    "Reviewer-only database evidence establishes the annotation and localization conflict, but was not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, peroxisomal membrane is the only membrane compartment, so it is the best-listed option. However, the evidence indicates ER membrane localization, which is not offered, and does not resolve whether peroxisomal localization is also present."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0124",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The matched sequence has a computational GO annotation for peroxisomal membrane, supporting the key as an annotation-based prediction. However, the matched entry reports experimental localization to the endoplasmic-reticulum membrane, not peroxisomal membrane. The evidence does not establish whether the protein also localizes to peroxisomes or which location is primary.",
    "evidence_ids": ["C7", "H5", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic regions, consistent with a multipass membrane protein; this makes the membrane-associated choice more plausible than the soluble or viral choices, but does not identify the membrane compartment.",
    "missing_item_specific_fact": "The protein-specific subcellular localization, including whether it localizes to peroxisomes and which compartment is primary.",
    "reason": "General sequence analysis can suggest membrane association, but cannot distinguish peroxisomal membrane from other cellular membranes. Selecting the precise compartment therefore depends on a protein-specific annotation or localization fact absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, peroxisomal membrane is the only membrane compartment, so it is the best-listed option. However, the evidence indicates ER membrane localization, which is not offered, and does not resolve whether peroxisomal localization is also present."
  },
  "important_caveats": [
    "The peroxisomal-membrane GO annotation is computationally inferred, whereas the cited ER localization is experimentally supported.",
    "Reviewer-only database evidence establishes the annotation and localization conflict, but was not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: uncertain

> The protein is named 'Peroxisomal membrane protein PEX29' (C4) and carries an IEA (computational) GO annotation for GO:0005778 peroxisomal membrane (C7, H5). However, the experimental evidence (ECO:0000269, PubMed:32665322) in the SUBCELLULAR LOCATION comment explicitly states 'Endoplasmic reticulum membrane' with the note 'Localizes to multiple regions of the ER' (C5, H3), and the EXP GO annotation is GO:0005789 ER membrane (C6). The peroxisomal membrane annotation is only IEA:EnsemblFungi/TreeGrafter (C7, H5), i.e., computational inference. The protein's name and peroxin function support peroxisomal membrane association, but the best experimental evidence contradicts it by placing the protein at the ER. Whether 'peroxisomal membrane' or 'ER membrane' is the 'primary' component for a peroxin that cycles between compartments cannot be resolved from the supplied evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 535-aa sequence contains multiple long hydrophobic stretches (e.g., 'FVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAY', 'IFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKE'), clearly indicating a multi-pass transmembrane protein. Option A (actin cytoskeleton) and B (cytosol) describe soluble/non-membrane compartments incompatible with a multi-pass membrane protein. Option D (virus tail, tube) applies to bacteriophage structural proteins, not eukaryotic proteins. Among the four choices, only C (peroxisomal membrane) is a membrane compartment, so general biological reasoning about membrane protein topology eliminates A, B, and D.


**Missing item-specific fact**

> None strictly required for elimination; however, distinguishing 'peroxisomal membrane' specifically from 'ER membrane' or 'mitochondrial membrane' would require PEX29-specific knowledge. Since those alternatives are absent from the choices, the elimination logic suffices.


**Reason**

> A model can reason that the sequence encodes a multi-pass membrane protein, then eliminate the three non-membrane/viral distractors by general cell-biology knowledge, arriving at the only membrane compartment option. This does not require memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are clearly incompatible with a multi-pass membrane eukaryotic protein. No other membrane compartment is offered, so C is the only viable choice by elimination. There is no ambiguity among the provided options.


### Important caveats

- The experimental evidence (EXP, ECO:0000269) places PEX29 at the ER membrane, not the peroxisomal membrane; the peroxisomal membrane GO annotation is purely computational (IEA). The author's key aligns with the protein name and IEA annotation but conflicts with the experimental localization data.
- The question's 'primary Cellular Component' framing is ambiguous for a peroxin known to traffic between ER and peroxisomal membranes.
- The reasoning support relies on the absence of competing membrane-compartment options (ER, mitochondria); had 'ER membrane' been an option, the question would have become lookup-dependent.
- All reviewer-only evidence was absent from the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 535-aa sequence contains multiple long hydrophobic stretches (e.g., 'FVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAY', 'IFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKE'), clearly indicating a multi-pass transmembrane protein. Option A (actin cytoskeleton) and B (cytosol) describe soluble/non-membrane compartments incompatible with a multi-pass membrane protein. Option D (virus tail, tube) applies to bacteriophage structural proteins, not eukaryotic proteins. Among the four choices, only C (peroxisomal membrane) is a membrane compartment, so general biological reasoning about membrane protein topology eliminates A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination; however, distinguishing 'peroxisomal membrane' specifically from 'ER membrane' or 'mitochondrial membrane' would require PEX29-specific knowledge. Since those alternatives are absent from the choices, the elimination logic suffices.",
    "reason": "A model can reason that the sequence encodes a multi-pass membrane protein, then eliminate the three non-membrane/viral distractors by general cell-biology knowledge, arriving at the only membrane compartment option. This does not require memorizing the specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "cannot_determine",
    "reason": "The protein is named 'Peroxisomal membrane protein PEX29' (C4) and carries an IEA (computational) GO annotation for GO:0005778 peroxisomal membrane (C7, H5). However, the experimental evidence (ECO:0000269, PubMed:32665322) in the SUBCELLULAR LOCATION comment explicitly states 'Endoplasmic reticulum membrane' with the note 'Localizes to multiple regions of the ER' (C5, H3), and the EXP GO annotation is GO:0005789 ER membrane (C6). The peroxisomal membrane annotation is only IEA:EnsemblFungi/TreeGrafter (C7, H5), i.e., computational inference. The protein's name and peroxin function support peroxisomal membrane association, but the best experimental evidence contradicts it by placing the protein at the ER. Whether 'peroxisomal membrane' or 'ER membrane' is the 'primary' component for a peroxin that cycles between compartments cannot be resolved from the supplied evidence."
  },
  "important_caveats": [
    "The experimental evidence (EXP, ECO:0000269) places PEX29 at the ER membrane, not the peroxisomal membrane; the peroxisomal membrane GO annotation is purely computational (IEA). The author's key aligns with the protein name and IEA annotation but conflicts with the experimental localization data.",
    "The question's 'primary Cellular Component' framing is ambiguous for a peroxin known to traffic between ER and peroxisomal membranes.",
    "The reasoning support relies on the absence of competing membrane-compartment options (ER, mitochondria); had 'ER membrane' been an option, the question would have become lookup-dependent.",
    "All reviewer-only evidence was absent from the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with a multi-pass membrane eukaryotic protein. No other membrane compartment is offered, so C is the only viable choice by elimination. There is no ambiguity among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0124",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The protein is named 'Peroxisomal membrane protein PEX29' (C4) and carries an IEA (computational) GO annotation for GO:0005778 peroxisomal membrane (C7, H5). However, the experimental evidence (ECO:0000269, PubMed:32665322) in the SUBCELLULAR LOCATION comment explicitly states 'Endoplasmic reticulum membrane' with the note 'Localizes to multiple regions of the ER' (C5, H3), and the EXP GO annotation is GO:0005789 ER membrane (C6). The peroxisomal membrane annotation is only IEA:EnsemblFungi/TreeGrafter (C7, H5), i.e., computational inference. The protein's name and peroxin function support peroxisomal membrane association, but the best experimental evidence contradicts it by placing the protein at the ER. Whether 'peroxisomal membrane' or 'ER membrane' is the 'primary' component for a peroxin that cycles between compartments cannot be resolved from the supplied evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 535-aa sequence contains multiple long hydrophobic stretches (e.g., 'FVLIDQVIIIFSWSKPLYTLTFLNVATLLILKPILLLSLPFFYTCFEIIVPAY', 'IFIFVALLTSGTLLTLFGAQVLSAMLPFIKVTLSVGLWAATIAMHPNYRSTLLDMLYSEDTRLRLLMMSNRLELWLNKELNLREQKE'), clearly indicating a multi-pass transmembrane protein. Option A (actin cytoskeleton) and B (cytosol) describe soluble/non-membrane compartments incompatible with a multi-pass membrane protein. Option D (virus tail, tube) applies to bacteriophage structural proteins, not eukaryotic proteins. Among the four choices, only C (peroxisomal membrane) is a membrane compartment, so general biological reasoning about membrane protein topology eliminates A, B, and D.",
    "missing_item_specific_fact": "None strictly required for elimination; however, distinguishing 'peroxisomal membrane' specifically from 'ER membrane' or 'mitochondrial membrane' would require PEX29-specific knowledge. Since those alternatives are absent from the choices, the elimination logic suffices.",
    "reason": "A model can reason that the sequence encodes a multi-pass membrane protein, then eliminate the three non-membrane/viral distractors by general cell-biology knowledge, arriving at the only membrane compartment option. This does not require memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly incompatible with a multi-pass membrane eukaryotic protein. No other membrane compartment is offered, so C is the only viable choice by elimination. There is no ambiguity among the provided options."
  },
  "important_caveats": [
    "The experimental evidence (EXP, ECO:0000269) places PEX29 at the ER membrane, not the peroxisomal membrane; the peroxisomal membrane GO annotation is purely computational (IEA). The author's key aligns with the protein name and IEA annotation but conflicts with the experimental localization data.",
    "The question's 'primary Cellular Component' framing is ambiguous for a peroxin known to traffic between ER and peroxisomal membranes.",
    "The reasoning support relies on the absence of competing membrane-compartment options (ER, mitochondria); had 'ER membrane' been an option, the question would have become lookup-dependent.",
    "All reviewer-only evidence was absent from the evaluated model input."
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

**Accession:** `W1QL91` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 41. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:09.919107+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Peroxin-29"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32665322","source":"PubMed"}],"value":"Peroxisomal membrane protein PEX29"}}}
```

Source SHA-256: `82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:09.919107+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32665322","source":"PubMed"}],"value":"Localizes to multiple regions of the ER"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"32665322","source":"PubMed"}],"id":"SL-0097","value":"Endoplasmic reticulum membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:09.919107+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"32665322","source":"PubMed"}],"id":"GO:0005789","properties":[{"key":"GoTerm","value":"C:endoplasmic reticulum membrane"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/W1QL91.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:09.919107+00:00.  

```json
{"database":"GO","id":"GO:0005778","properties":[{"key":"GoTerm","value":"C:peroxisomal membrane"},{"key":"GoEvidenceType","value":"IEA:EnsemblFungi"}]}
```

Source SHA-256: `82521092a67ef997abdc31799f3577764b26227f0c47f2c09c813128fc009f23`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)  
**Locator:** `lines 43-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:34:13.232116+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Endoplasmic reticulum membrane
CC       {ECO:0000269|PubMed:32665322}; Multi-pass membrane protein
CC       {ECO:0000255}. Note=Localizes to multiple regions of the ER.
CC       {ECO:0000269|PubMed:32665322}.
```

Source SHA-256: `2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)  
**Locator:** `lines 70-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:34:13.232116+00:00.  

```text
DR   GO; GO:0005789; C:endoplasmic reticulum membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/W1QL91?format=txt&versions=41)  
**Locator:** `lines 71-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-02T04:34:13.232116+00:00.  

```text
DR   GO; GO:0005778; C:peroxisomal membrane; IEA:TreeGrafter.
```

Source SHA-256: `2b59cad336a5f0f970c7aa6c93d04cd1ad5885189ae5de312c6383b733a569b7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
