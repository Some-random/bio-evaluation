# pathway_0141

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSYKAFLITLAAVTRVLTYPANSSFELVDRSGTPSSTGTSGGYYYSFWTDGGADVTYTNGAGGEYKLQWSGNGNLVGGKGWNPGSAKAVTYSGTYSPNGNSYLSLYGWTTSPLIEYYVVENFGTYDPSTGATLKGTVVSDGATYKIYQTQRVNQPSIIGTATFYQYWSVRQTKRTGGTVTTGNHFNAWKALGMNMGTFDYMIVATEGYFSSGSSDITVGSSTGGGDSGSPTSAPTTSPTTSPGGTCGALYSQCGGTGFTGSQCCASGTCKYANSYYSQCL

[Multiple Choices]
A. Glycan degradation
B. LPS O-antigen biosynthesis. .
C. Pyrimidine metabolism
D. NAD(+) from nicotinamide D-ribonucleotide: step 1/1. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches UniProt EIX1, annotated as an endo-1,4-beta-xylanase (EC 3.2.1.8) in glycan degradation/xylan degradation. The pathway assignment is supported as a database annotation, but its cited basis is a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secretion signal, which makes an extracellular enzyme plausible; however, secretion alone does not establish that this protein degrades glycans rather than performing another extracellular function.


**Missing item-specific fact**

> The protein-specific functional or domain assignment identifying this sequence as a xylanase is not provided in the question.


**Reason**

> Choosing glycan degradation requires identifying the sequence as a xylanase or otherwise knowing its specific enzymatic function. That fact is available in the reviewer-only annotation, but is not stated in the input; generic secretion-based inference does not by itself distinguish the pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports choice A, and no other listed pathway is comparably supported by the available evidence.


### Important caveats

- The current and archived records match the supplied sequence; the archived annotation supports that the pathway assignment was present by the historical cutoff.
- The pathway evidence is computationally assigned by PROSITE-ProRule. The cited evidence does not independently establish the annotation through an experiment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, which makes an extracellular enzyme plausible; however, secretion alone does not establish that this protein degrades glycans rather than performing another extracellular function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional or domain assignment identifying this sequence as a xylanase is not provided in the question.",
    "reason": "Choosing glycan degradation requires identifying the sequence as a xylanase or otherwise knowing its specific enzymatic function. That fact is available in the reviewer-only annotation, but is not stated in the input; generic secretion-based inference does not by itself distinguish the pathway."
  },
  "case_id": "pathway_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches UniProt EIX1, annotated as an endo-1,4-beta-xylanase (EC 3.2.1.8) in glycan degradation/xylan degradation. The pathway assignment is supported as a database annotation, but its cited basis is a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The current and archived records match the supplied sequence; the archived annotation supports that the pathway assignment was present by the historical cutoff.",
    "The pathway evidence is computationally assigned by PROSITE-ProRule. The cited evidence does not independently establish the annotation through an experiment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports choice A, and no other listed pathway is comparably supported by the available evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches UniProt EIX1, annotated as an endo-1,4-beta-xylanase (EC 3.2.1.8) in glycan degradation/xylan degradation. The pathway assignment is supported as a database annotation, but its cited basis is a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretion signal, which makes an extracellular enzyme plausible; however, secretion alone does not establish that this protein degrades glycans rather than performing another extracellular function.",
    "missing_item_specific_fact": "The protein-specific functional or domain assignment identifying this sequence as a xylanase is not provided in the question.",
    "reason": "Choosing glycan degradation requires identifying the sequence as a xylanase or otherwise knowing its specific enzymatic function. That fact is available in the reviewer-only annotation, but is not stated in the input; generic secretion-based inference does not by itself distinguish the pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports choice A, and no other listed pathway is comparably supported by the available evidence."
  },
  "important_caveats": [
    "The current and archived records match the supplied sequence; the archived annotation supports that the pathway assignment was present by the historical cutoff.",
    "The pathway evidence is computationally assigned by PROSITE-ProRule. The cited evidence does not independently establish the annotation through an experiment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A384JXV5 (EIX1_BOTFB), annotated as Ethylene-inducing xylanase 1 / Endo-1,4-beta-xylanase EIX1 (EC 3.2.1.8) from Botrytis cinerea. The UniProt PATHWAY comment explicitly states 'Glycan degradation; xylan degradation' (ECO:0000255|PROSITE-ProRule:PRU01097). EC 3.2.1.8 is a glycoside hydrolase (xylanase) that hydrolyzes xylan, a glycan. The expected answer 'Glycan degradation' is directly supported by the database annotation. The evidence code is PROSITE-ProRule (similarity-based), but the EC assignment and protein identity are well-established for GH11 xylanases.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal signal peptide (MVSYKAFLITLAAVTRVLT), indicating a secreted protein. The sequence displays hallmark motifs of glycoside hydrolase family 11 (GH11) xylanases: the 'WSGNG' motif (in 'YKLQWSGNG'), the 'WTDGG' motif (in 'YYYSFWTDGG'), and multiple Trp residues spaced in the characteristic pattern of the GH11 β-jellyroll fold. The protein length (~281 aa) is consistent with GH11 xylanases. Among the four choices, only 'Glycan degradation' is compatible with a secreted fungal glycoside hydrolase. LPS O-antigen biosynthesis is a bacterial pathway; pyrimidine metabolism and NAD+ biosynthesis are intracellular metabolic pathways incompatible with a secreted extracellular enzyme bearing these hydrolase motifs.


**Missing item-specific fact**

> None critical. Recognition of the WSGNG and WTDGG motifs as GH11 xylanase signatures requires specialized enzymology knowledge, but the broader reasoning (secreted protein + glycoside hydrolase architecture → glycan degradation, eliminating bacterial/intracellular pathways) provides defensible grounds without memorizing this specific entry.


**Reason**

> A model with general knowledge of glycoside hydrolase families and secreted fungal enzymes can identify the GH11 motifs and the secreted nature of the protein, then eliminate the three clearly incompatible distractors (bacterial LPS pathway, intracellular pyrimidine/NAD+ pathways). The WSGNG motif is a widely recognized signature in the enzymology literature, making this accessible to trained reasoning rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated: Glycan degradation (glycoside hydrolase), LPS O-antigen biosynthesis (bacterial glycosyltransferases), Pyrimidine metabolism (nucleotide biosynthesis), and NAD+ biosynthesis (nicotinamide metabolism). A secreted fungal enzyme with GH11 xylanase motifs unambiguously fits only option A.


### Important caveats

- The UniProt pathway annotation carries evidence code ECO:0000255 (PROSITE-ProRule), indicating computational/similarity-based assignment rather than direct experimental pathway reconstitution.
- The protein is also an ethylene-inducing elicitor (EIX) with a signaling role in plant-pathogen interactions, but its enzymatic activity (xylan hydrolysis) places it in the glycan degradation pathway, which is what the question asks.
- The WSGNG/WTDGG motif recognition is specialized knowledge; a model without glycoside hydrolase family training might struggle, though the elimination of clearly wrong distractors still provides a reasoning path.
- Reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence features and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MVSYKAFLITLAAVTRVLT), indicating a secreted protein. The sequence displays hallmark motifs of glycoside hydrolase family 11 (GH11) xylanases: the 'WSGNG' motif (in 'YKLQWSGNG'), the 'WTDGG' motif (in 'YYYSFWTDGG'), and multiple Trp residues spaced in the characteristic pattern of the GH11 β-jellyroll fold. The protein length (~281 aa) is consistent with GH11 xylanases. Among the four choices, only 'Glycan degradation' is compatible with a secreted fungal glycoside hydrolase. LPS O-antigen biosynthesis is a bacterial pathway; pyrimidine metabolism and NAD+ biosynthesis are intracellular metabolic pathways incompatible with a secreted extracellular enzyme bearing these hydrolase motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the WSGNG and WTDGG motifs as GH11 xylanase signatures requires specialized enzymology knowledge, but the broader reasoning (secreted protein + glycoside hydrolase architecture → glycan degradation, eliminating bacterial/intracellular pathways) provides defensible grounds without memorizing this specific entry.",
    "reason": "A model with general knowledge of glycoside hydrolase families and secreted fungal enzymes can identify the GH11 motifs and the secreted nature of the protein, then eliminate the three clearly incompatible distractors (bacterial LPS pathway, intracellular pyrimidine/NAD+ pathways). The WSGNG motif is a widely recognized signature in the enzymology literature, making this accessible to trained reasoning rather than pure lookup."
  },
  "case_id": "pathway_0141",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A384JXV5 (EIX1_BOTFB), annotated as Ethylene-inducing xylanase 1 / Endo-1,4-beta-xylanase EIX1 (EC 3.2.1.8) from Botrytis cinerea. The UniProt PATHWAY comment explicitly states 'Glycan degradation; xylan degradation' (ECO:0000255|PROSITE-ProRule:PRU01097). EC 3.2.1.8 is a glycoside hydrolase (xylanase) that hydrolyzes xylan, a glycan. The expected answer 'Glycan degradation' is directly supported by the database annotation. The evidence code is PROSITE-ProRule (similarity-based), but the EC assignment and protein identity are well-established for GH11 xylanases."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000255 (PROSITE-ProRule), indicating computational/similarity-based assignment rather than direct experimental pathway reconstitution.",
    "The protein is also an ethylene-inducing elicitor (EIX) with a signaling role in plant-pathogen interactions, but its enzymatic activity (xylan hydrolysis) places it in the glycan degradation pathway, which is what the question asks.",
    "The WSGNG/WTDGG motif recognition is specialized knowledge; a model without glycoside hydrolase family training might struggle, though the elimination of clearly wrong distractors still provides a reasoning path.",
    "Reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence features and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: Glycan degradation (glycoside hydrolase), LPS O-antigen biosynthesis (bacterial glycosyltransferases), Pyrimidine metabolism (nucleotide biosynthesis), and NAD+ biosynthesis (nicotinamide metabolism). A secreted fungal enzyme with GH11 xylanase motifs unambiguously fits only option A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0141",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A384JXV5 (EIX1_BOTFB), annotated as Ethylene-inducing xylanase 1 / Endo-1,4-beta-xylanase EIX1 (EC 3.2.1.8) from Botrytis cinerea. The UniProt PATHWAY comment explicitly states 'Glycan degradation; xylan degradation' (ECO:0000255|PROSITE-ProRule:PRU01097). EC 3.2.1.8 is a glycoside hydrolase (xylanase) that hydrolyzes xylan, a glycan. The expected answer 'Glycan degradation' is directly supported by the database annotation. The evidence code is PROSITE-ProRule (similarity-based), but the EC assignment and protein identity are well-established for GH11 xylanases.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MVSYKAFLITLAAVTRVLT), indicating a secreted protein. The sequence displays hallmark motifs of glycoside hydrolase family 11 (GH11) xylanases: the 'WSGNG' motif (in 'YKLQWSGNG'), the 'WTDGG' motif (in 'YYYSFWTDGG'), and multiple Trp residues spaced in the characteristic pattern of the GH11 β-jellyroll fold. The protein length (~281 aa) is consistent with GH11 xylanases. Among the four choices, only 'Glycan degradation' is compatible with a secreted fungal glycoside hydrolase. LPS O-antigen biosynthesis is a bacterial pathway; pyrimidine metabolism and NAD+ biosynthesis are intracellular metabolic pathways incompatible with a secreted extracellular enzyme bearing these hydrolase motifs.",
    "missing_item_specific_fact": "None critical. Recognition of the WSGNG and WTDGG motifs as GH11 xylanase signatures requires specialized enzymology knowledge, but the broader reasoning (secreted protein + glycoside hydrolase architecture → glycan degradation, eliminating bacterial/intracellular pathways) provides defensible grounds without memorizing this specific entry.",
    "reason": "A model with general knowledge of glycoside hydrolase families and secreted fungal enzymes can identify the GH11 motifs and the secreted nature of the protein, then eliminate the three clearly incompatible distractors (bacterial LPS pathway, intracellular pyrimidine/NAD+ pathways). The WSGNG motif is a widely recognized signature in the enzymology literature, making this accessible to trained reasoning rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: Glycan degradation (glycoside hydrolase), LPS O-antigen biosynthesis (bacterial glycosyltransferases), Pyrimidine metabolism (nucleotide biosynthesis), and NAD+ biosynthesis (nicotinamide metabolism). A secreted fungal enzyme with GH11 xylanase motifs unambiguously fits only option A."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000255 (PROSITE-ProRule), indicating computational/similarity-based assignment rather than direct experimental pathway reconstitution.",
    "The protein is also an ethylene-inducing elicitor (EIX) with a signaling role in plant-pathogen interactions, but its enzymatic activity (xylan hydrolysis) places it in the glycan degradation pathway, which is what the question asks.",
    "The WSGNG/WTDGG motif recognition is specialized knowledge; a model without glycoside hydrolase family training might struggle, though the elimination of clearly wrong distractors still provides a reasoning path.",
    "Reviewer-only evidence was absent from the evaluated model input; the model must rely on sequence features and general biological knowledge."
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

**Accession:** `A0A384JXV5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 25. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.123065+00:00.  

```json
"A0A384JXV5"
```

Source SHA-256: `83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.123065+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX1"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX1"}]}}
```

Source SHA-256: `83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.123065+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:00.003931+00:00.  

```text
ID   EIX1_BOTFB              Reviewed;         281 AA.
AC   A0A384JXV5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-NOV-2018, sequence version 1.
DT   28-JAN-2026, entry version 25.
DE   RecName: Full=Ethylene-inducing xylanase 1 {ECO:0000303|PubMed:33205907};
DE            Short=EIX1 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX1 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX1 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_12g00090;
OS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis
OS   cinerea).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;
OC   Helotiales; Sclerotiniaceae; Botrytis.
OX   NCBI_TaxID=332648;
```

Source SHA-256: `82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)  
**Locator:** `lines 70-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:00.003931+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-
CC       ProRule:PRU01097}.
```

Source SHA-256: `82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 141. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
