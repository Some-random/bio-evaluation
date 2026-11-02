# GO_biological_process_0025

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — xylan catabolic process

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
A. 'de novo' IMP biosynthetic process
B. xylan catabolic process
C. germ cell development
D. ribosomal small subunit assembly
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as an endo-1,4-beta-xylanase, with a xylan-degradation pathway annotation and the GO term xylan catabolic process. The functional description says xylan hydrolysis is supported by similarity, so this supports the key as an annotation-based claim, not as independently established experimental proof of that activity.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted protein, and the sequence is more consistent with an enzyme than with a ribosomal assembly factor or a purine-biosynthesis enzyme. These clues may favor a catabolic enzyme, but do not establish xylan as its substrate.


**Missing item-specific fact**

> The protein-specific identification as an endo-1,4-beta-xylanase, including its substrate specificity, is not provided in the question and is needed to distinguish xylan catabolism from other possible enzyme functions.


**Reason**

> The supplied sequence offers broad clues against several distractors, but selecting the specific xylan catabolic process depends on identifying this particular protein or its substrate activity; sequence resemblance or a trained predictor alone does not make that fact part of the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe substantially different processes, and the matched protein annotation supports option B. The limitation is that the sequence alone does not establish the specific xylan-related function.


### Important caveats

- The historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.
- The xylan-hydrolysis function is described as supported by similarity; a separate publication cited in the record concerns elicitor activity, not direct demonstration of xylan hydrolysis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and the sequence is more consistent with an enzyme than with a ribosomal assembly factor or a purine-biosynthesis enzyme. These clues may favor a catabolic enzyme, but do not establish xylan as its substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as an endo-1,4-beta-xylanase, including its substrate specificity, is not provided in the question and is needed to distinguish xylan catabolism from other possible enzyme functions.",
    "reason": "The supplied sequence offers broad clues against several distractors, but selecting the specific xylan catabolic process depends on identifying this particular protein or its substrate activity; sequence resemblance or a trained predictor alone does not make that fact part of the input."
  },
  "case_id": "GO_biological_process_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as an endo-1,4-beta-xylanase, with a xylan-degradation pathway annotation and the GO term xylan catabolic process. The functional description says xylan hydrolysis is supported by similarity, so this supports the key as an annotation-based claim, not as independently established experimental proof of that activity."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The xylan-hydrolysis function is described as supported by similarity; a separate publication cited in the record concerns elicitor activity, not direct demonstration of xylan hydrolysis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe substantially different processes, and the matched protein annotation supports option B. The limitation is that the sequence alone does not establish the specific xylan-related function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as an endo-1,4-beta-xylanase, with a xylan-degradation pathway annotation and the GO term xylan catabolic process. The functional description says xylan hydrolysis is supported by similarity, so this supports the key as an annotation-based claim, not as independently established experimental proof of that activity.",
    "evidence_ids": ["H3", "H4", "H5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and the sequence is more consistent with an enzyme than with a ribosomal assembly factor or a purine-biosynthesis enzyme. These clues may favor a catabolic enzyme, but do not establish xylan as its substrate.",
    "missing_item_specific_fact": "The protein-specific identification as an endo-1,4-beta-xylanase, including its substrate specificity, is not provided in the question and is needed to distinguish xylan catabolism from other possible enzyme functions.",
    "reason": "The supplied sequence offers broad clues against several distractors, but selecting the specific xylan catabolic process depends on identifying this particular protein or its substrate activity; sequence resemblance or a trained predictor alone does not make that fact part of the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe substantially different processes, and the matched protein annotation supports option B. The limitation is that the sequence alone does not establish the specific xylan-related function."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The xylan-hydrolysis function is described as supported by similarity; a separate publication cited in the record concerns elicitor activity, not direct demonstration of xylan hydrolysis."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is UniProt A0A384JXV5 (EIX1_BOTFB), annotated as Ethylene-inducing xylanase 1 with EC 3.2.1.8 (Endo-1,4-beta-xylanase). UniProt explicitly annotates GO:0045493 (xylan catabolic process) and the pathway 'Glycan degradation; xylan degradation.' The EC assignment is based on PROSITE-ProRule (PRU01097), and the FUNCTION comment cites both by-similarity evidence (ECO:0000250) and experimental evidence from PubMed:33205907 (ECO:0000269). The sequence matches exactly (281 AA, SHA256 confirmed). The GO annotation itself is IEA (Inferred from Electronic Annotation via UniPathway), but the underlying xylanase activity is supported by experimental data. The expected answer 'xylan catabolic process' is scientifically well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region (MVSYKAFLITLAAVTRVLTYPAN) exhibits a clear signal peptide (hydrophobic stretch followed by a cleavage-site-like region), indicating the protein is secreted. Its small size (~281 AA, ~260 mature) is consistent with a single-domain secreted enzyme rather than a multi-subunit biosynthetic complex or a large assembly factor. Three of the four options describe strictly intracellular or developmental processes: 'de novo' IMP biosynthetic process (cytoplasmic purine pathway enzymes), ribosomal small subunit assembly (nuclear/cytoplasmic ribosome biogenesis), and germ cell development (multicellular developmental program). A secreted, small, single-domain protein is incompatible with all three. The remaining option, xylan catabolic process, is the only one consistent with a secreted fungal glycoside-hydrolase-type enzyme. Additionally, the sequence contains motifs (e.g., WTDGG, WSGNG, WTTSPL patterns) reminiscent of glycoside hydrolase catalytic domains, further supporting a polysaccharide-degradation role. The elimination logic based on subcellular localization and protein architecture provides a concrete biological argument favoring B.


**Missing item-specific fact**

> None strictly required. Positive confirmation that the enzyme is specifically a xylanase (GH10 family) rather than another secreted glycoside hydrolase (e.g., cellulase, mannanase) would require recognizing family-specific catalytic motifs, but since xylan catabolic process is the only glycan-degradation option, the elimination argument suffices.


**Reason**

> The signal peptide and small secreted-enzyme architecture allow a model to eliminate the three intracellular/developmental distractors through general cell-biology reasoning, leaving xylan catabolic process as the only viable option. This constitutes a concrete biological argument derivable from the sequence and general knowledge, not a lookup of a specific database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different biological contexts (secreted enzyme vs. cytoplasmic biosynthesis vs. nuclear assembly vs. multicellular development). The signal peptide and small size of the protein create a clear incompatibility with options A, C, and D. No alternative option is defensible given the sequence features.


### Important caveats

- The GO annotation in UniProt is IEA (Inferred from Electronic Annotation) via UniPathway/PROSITE-ProRule, not a direct experimental GO assignment. However, the underlying xylanase function is supported by experimental evidence (PubMed:33205907).
- The protein is also described as an ethylene-inducing elicitor of plant defense responses, which could in principle relate to a different biological process, but its primary enzymatic activity (xylan hydrolysis) maps to xylan catabolism.
- The reasoning path relies on elimination via subcellular localization rather than positive recognition of GH10-specific catalytic motifs; a model lacking signal-peptide recognition might struggle.
- The reviewer-only evidence was not available to the evaluated model; the reasoning argument is assessed based solely on the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region (MVSYKAFLITLAAVTRVLTYPAN) exhibits a clear signal peptide (hydrophobic stretch followed by a cleavage-site-like region), indicating the protein is secreted. Its small size (~281 AA, ~260 mature) is consistent with a single-domain secreted enzyme rather than a multi-subunit biosynthetic complex or a large assembly factor. Three of the four options describe strictly intracellular or developmental processes: 'de novo' IMP biosynthetic process (cytoplasmic purine pathway enzymes), ribosomal small subunit assembly (nuclear/cytoplasmic ribosome biogenesis), and germ cell development (multicellular developmental program). A secreted, small, single-domain protein is incompatible with all three. The remaining option, xylan catabolic process, is the only one consistent with a secreted fungal glycoside-hydrolase-type enzyme. Additionally, the sequence contains motifs (e.g., WTDGG, WSGNG, WTTSPL patterns) reminiscent of glycoside hydrolase catalytic domains, further supporting a polysaccharide-degradation role. The elimination logic based on subcellular localization and protein architecture provides a concrete biological argument favoring B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Positive confirmation that the enzyme is specifically a xylanase (GH10 family) rather than another secreted glycoside hydrolase (e.g., cellulase, mannanase) would require recognizing family-specific catalytic motifs, but since xylan catabolic process is the only glycan-degradation option, the elimination argument suffices.",
    "reason": "The signal peptide and small secreted-enzyme architecture allow a model to eliminate the three intracellular/developmental distractors through general cell-biology reasoning, leaving xylan catabolic process as the only viable option. This constitutes a concrete biological argument derivable from the sequence and general knowledge, not a lookup of a specific database annotation."
  },
  "case_id": "GO_biological_process_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein is UniProt A0A384JXV5 (EIX1_BOTFB), annotated as Ethylene-inducing xylanase 1 with EC 3.2.1.8 (Endo-1,4-beta-xylanase). UniProt explicitly annotates GO:0045493 (xylan catabolic process) and the pathway 'Glycan degradation; xylan degradation.' The EC assignment is based on PROSITE-ProRule (PRU01097), and the FUNCTION comment cites both by-similarity evidence (ECO:0000250) and experimental evidence from PubMed:33205907 (ECO:0000269). The sequence matches exactly (281 AA, SHA256 confirmed). The GO annotation itself is IEA (Inferred from Electronic Annotation via UniPathway), but the underlying xylanase activity is supported by experimental data. The expected answer 'xylan catabolic process' is scientifically well-supported."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA (Inferred from Electronic Annotation) via UniPathway/PROSITE-ProRule, not a direct experimental GO assignment. However, the underlying xylanase function is supported by experimental evidence (PubMed:33205907).",
    "The protein is also described as an ethylene-inducing elicitor of plant defense responses, which could in principle relate to a different biological process, but its primary enzymatic activity (xylan hydrolysis) maps to xylan catabolism.",
    "The reasoning path relies on elimination via subcellular localization rather than positive recognition of GH10-specific catalytic motifs; a model lacking signal-peptide recognition might struggle.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning argument is assessed based solely on the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological contexts (secreted enzyme vs. cytoplasmic biosynthesis vs. nuclear assembly vs. multicellular development). The signal peptide and small size of the protein create a clear incompatibility with options A, C, and D. No alternative option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is UniProt A0A384JXV5 (EIX1_BOTFB), annotated as Ethylene-inducing xylanase 1 with EC 3.2.1.8 (Endo-1,4-beta-xylanase). UniProt explicitly annotates GO:0045493 (xylan catabolic process) and the pathway 'Glycan degradation; xylan degradation.' The EC assignment is based on PROSITE-ProRule (PRU01097), and the FUNCTION comment cites both by-similarity evidence (ECO:0000250) and experimental evidence from PubMed:33205907 (ECO:0000269). The sequence matches exactly (281 AA, SHA256 confirmed). The GO annotation itself is IEA (Inferred from Electronic Annotation via UniPathway), but the underlying xylanase activity is supported by experimental data. The expected answer 'xylan catabolic process' is scientifically well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region (MVSYKAFLITLAAVTRVLTYPAN) exhibits a clear signal peptide (hydrophobic stretch followed by a cleavage-site-like region), indicating the protein is secreted. Its small size (~281 AA, ~260 mature) is consistent with a single-domain secreted enzyme rather than a multi-subunit biosynthetic complex or a large assembly factor. Three of the four options describe strictly intracellular or developmental processes: 'de novo' IMP biosynthetic process (cytoplasmic purine pathway enzymes), ribosomal small subunit assembly (nuclear/cytoplasmic ribosome biogenesis), and germ cell development (multicellular developmental program). A secreted, small, single-domain protein is incompatible with all three. The remaining option, xylan catabolic process, is the only one consistent with a secreted fungal glycoside-hydrolase-type enzyme. Additionally, the sequence contains motifs (e.g., WTDGG, WSGNG, WTTSPL patterns) reminiscent of glycoside hydrolase catalytic domains, further supporting a polysaccharide-degradation role. The elimination logic based on subcellular localization and protein architecture provides a concrete biological argument favoring B.",
    "missing_item_specific_fact": "None strictly required. Positive confirmation that the enzyme is specifically a xylanase (GH10 family) rather than another secreted glycoside hydrolase (e.g., cellulase, mannanase) would require recognizing family-specific catalytic motifs, but since xylan catabolic process is the only glycan-degradation option, the elimination argument suffices.",
    "reason": "The signal peptide and small secreted-enzyme architecture allow a model to eliminate the three intracellular/developmental distractors through general cell-biology reasoning, leaving xylan catabolic process as the only viable option. This constitutes a concrete biological argument derivable from the sequence and general knowledge, not a lookup of a specific database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological contexts (secreted enzyme vs. cytoplasmic biosynthesis vs. nuclear assembly vs. multicellular development). The signal peptide and small size of the protein create a clear incompatibility with options A, C, and D. No alternative option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA (Inferred from Electronic Annotation) via UniPathway/PROSITE-ProRule, not a direct experimental GO assignment. However, the underlying xylanase function is supported by experimental evidence (PubMed:33205907).",
    "The protein is also described as an ethylene-inducing elicitor of plant defense responses, which could in principle relate to a different biological process, but its primary enzymatic activity (xylan hydrolysis) maps to xylan catabolism.",
    "The reasoning path relies on elimination via subcellular localization rather than positive recognition of GH10-specific catalytic motifs; a model lacking signal-peptide recognition might struggle.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning argument is assessed based solely on the sequence and general biological knowledge."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.123065+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"B3VSG7","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (By similarity). May act as an elicitor of plant defense responses in certain plants but does not exhibit any cell death when transiently expressed in N.benthamiana (PubMed:33205907)"}]}
```

Source SHA-256: `83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.123065+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JXV5.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.123065+00:00.  

```json
{"database":"GO","id":"GO:0045493","properties":[{"key":"GoTerm","value":"P:xylan catabolic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniPathway"}]}
```

Source SHA-256: `83f653c725cb3cb95996a5253b38afe4076857dad481a88855db79f7d973240a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)  
**Locator:** `lines 60-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:00.003931+00:00.  

```text
CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a
CC       major structural heterogeneous polysaccharide found in plant biomass
CC       representing the second most abundant polysaccharide in the biosphere,
CC       after cellulose (By similarity). May act as an elicitor of plant
CC       defense responses in certain plants but does not exhibit any cell death
CC       when transiently expressed in N.benthamiana (PubMed:33205907).
CC       {ECO:0000250|UniProtKB:B3VSG7, ECO:0000269|PubMed:33205907}.
```

Source SHA-256: `82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef`.

### Evidence H4

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

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JXV5?format=txt&versions=25)  
**Locator:** `lines 92-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 25 / 1.  
**Retrieved:** 2026-11-02T04:25:00.003931+00:00.  

```text
DR   GO; GO:0045493; P:xylan catabolic process; IEA:UniProtKB-UniPathway.
```

Source SHA-256: `82b4ecbdbcc3751e49d8363b6c40353beac4055c700b46e23d74ec116b1c11ef`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 265164-265174`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0045493
name: xylan catabolic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the breakdown of xylan, a polymer containing a beta-1,4-linked D-xylose backbone." [GOC:curators, PMID:11931668]
synonym: "xylan breakdown" EXACT []
synonym: "xylan catabolism" EXACT []
synonym: "xylan degradation" EXACT []
is_a: GO:0045491 ! xylan metabolic process
is_a: GO:2000895 ! hemicellulose catabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
