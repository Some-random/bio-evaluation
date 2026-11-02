# GO_biological_process_0087

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — xylan catabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFSTLLTACTAITGALGTPDLDRRQNVTPNAQGTHNGYFYSWWSDGQSPVTYTNSAGGSYSVEWSSGGNLVGGKGWNPGSAKEIRYSASWQPTNNSNSYLTIYGWTRSPLVEYYIVESHGEYNPGSSAEPRGEIEAHGSIYKLYESTRVQQPSIDGTQTFQQYWAIRQTHRTSGTVTTGTFFNAWAAAGMPIGQHNYMIVATEAYNSAGRASVVVETPP

[Multiple Choices]
A. behavioral response to ethanol
B. negative regulation of gluconeogenesis
C. regulation of alternative mRNA splicing, via spliceosome
D. xylan catabolic process
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

> The sequence matches the reviewed Verticillium dahliae EIX4 entry. That entry describes an endo-1,4-beta-xylanase involved in xylan hydrolysis and annotates xylan catabolic process. The GO annotation is computational (IEA:UniProtKB-UniPathway); the xylanase activity is stated by similarity, so this supports the key but is not direct experimental proof of xylan breakdown by this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal signal-peptide-like region and enzyme-like sequence are consistent with a secreted protein and make intracellular splicing or gluconeogenesis regulation less plausible. They do not, by themselves, establish xylan as the substrate.


**Missing item-specific fact**

> The protein-specific assignment as a xylanase, including its substrate specificity and corresponding GO process annotation, is absent from the prompt.


**Reason**

> Choosing D requires identifying the sequence's particular enzyme function or relying on a protein-specific annotation; general secretion and sequence heuristics do not establish xylan catabolism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports D, while the supplied evidence does not support another listed process.


### Important caveats

- Reviewer-only database and publication evidence was not supplied to the evaluated model.
- The GO process annotation is inferred computationally, and the cited function includes evidence by similarity; the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal signal-peptide-like region and enzyme-like sequence are consistent with a secreted protein and make intracellular splicing or gluconeogenesis regulation less plausible. They do not, by themselves, establish xylan as the substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment as a xylanase, including its substrate specificity and corresponding GO process annotation, is absent from the prompt.",
    "reason": "Choosing D requires identifying the sequence's particular enzyme function or relying on a protein-specific annotation; general secretion and sequence heuristics do not establish xylan catabolism."
  },
  "case_id": "GO_biological_process_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the reviewed Verticillium dahliae EIX4 entry. That entry describes an endo-1,4-beta-xylanase involved in xylan hydrolysis and annotates xylan catabolic process. The GO annotation is computational (IEA:UniProtKB-UniPathway); the xylanase activity is stated by similarity, so this supports the key but is not direct experimental proof of xylan breakdown by this exact protein."
  },
  "important_caveats": [
    "Reviewer-only database and publication evidence was not supplied to the evaluated model.",
    "The GO process annotation is inferred computationally, and the cited function includes evidence by similarity; the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports D, while the supplied evidence does not support another listed process."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the reviewed Verticillium dahliae EIX4 entry. That entry describes an endo-1,4-beta-xylanase involved in xylan hydrolysis and annotates xylan catabolic process. The GO annotation is computational (IEA:UniProtKB-UniPathway); the xylanase activity is stated by similarity, so this supports the key but is not direct experimental proof of xylan breakdown by this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal signal-peptide-like region and enzyme-like sequence are consistent with a secreted protein and make intracellular splicing or gluconeogenesis regulation less plausible. They do not, by themselves, establish xylan as the substrate.",
    "missing_item_specific_fact": "The protein-specific assignment as a xylanase, including its substrate specificity and corresponding GO process annotation, is absent from the prompt.",
    "reason": "Choosing D requires identifying the sequence's particular enzyme function or relying on a protein-specific annotation; general secretion and sequence heuristics do not establish xylan catabolism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports D, while the supplied evidence does not support another listed process."
  },
  "important_caveats": [
    "Reviewer-only database and publication evidence was not supplied to the evaluated model.",
    "The GO process annotation is inferred computationally, and the cited function includes evidence by similarity; the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G2X5X8 (sequence matched, 221 aa) is annotated as 'Ethylene-inducing xylanase 4' (EIX4) from Verticillium dahliae, with EC 3.2.1.8 (Endo-1,4-beta-xylanase). The function comment states it is 'involved in the hydrolysis of xylan' with experimental evidence (ECO:0000269, PubMed:33205907). The pathway is 'Glycan degradation; xylan degradation' and the GO annotation GO:0045493 'xylan catabolic process' is directly assigned. The GO term definition matches: 'The chemical reactions and pathways resulting in the breakdown of xylan.' The answer is well-supported by both computational (PROSITE-ProRule) and experimental (PubMed) evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~20 residues (MVSFSTLLTACTAITGALGTP) form a classic signal peptide (hydrophobic core with small residues near the cleavage site), indicating a secreted protein. The mature protein (~200 aa) contains multiple Trp residues, no transmembrane helices, no nuclear localization signals, and no regulatory domains (kinase, SH2, zinc finger). This profile is consistent with a secreted fungal glycoside hydrolase. Among the four options: (A) behavioral response to ethanol is a neural/animal process incompatible with a fungal secreted enzyme; (B) negative regulation of gluconeogenesis is an intracellular metabolic regulatory process; (C) regulation of alternative mRNA splicing is a nuclear RNA-processing activity. Only (D) xylan catabolic process describes an extracellular enzymatic degradation activity, which is the only biological process consistent with a small secreted fungal enzyme. Elimination of the three clearly incompatible options leaves D as the sole defensible answer.


**Missing item-specific fact**

> None required for elimination. Specific recognition of GH11 xylanase family motifs (e.g., catalytic Glu in 'IVESHGEY', Trp-rich active site) would confirm xylan specificity over other polysaccharides, but is not needed to select D among the four given options.


**Reason**

> A knowledgeable biologist can reason from the signal peptide, small secreted-protein architecture, fungal context, and absence of regulatory/nuclear features to eliminate options A, B, and C as incompatible with a secreted extracellular enzyme, leaving D as the only viable choice. This does not require memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe neural/animal behavior, intracellular metabolic regulation, and nuclear RNA processing respectively—all fundamentally incompatible with a small secreted fungal enzyme. Only D is consistent with the sequence architecture. No ambiguity exists among the choices.


### Important caveats

- The GO annotation for xylan catabolic process carries evidence code IEA (Inferred from Electronic Annotation via UniPathway), meaning it is computationally derived from the PROSITE-ProRule EC assignment rather than a direct experimental GO annotation. However, the underlying enzymatic function (xylan hydrolysis) is supported by experimental evidence (PubMed:33205907, ECO:0000269).
- The protein also has an elicitor function in plant defense (per PubMed:33205907), but this is not among the answer options and does not conflict with the primary enzymatic role.
- The reviewer-only evidence confirms sequence match and correct identity, but the evaluated model receives only the raw sequence without any database annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~20 residues (MVSFSTLLTACTAITGALGTP) form a classic signal peptide (hydrophobic core with small residues near the cleavage site), indicating a secreted protein. The mature protein (~200 aa) contains multiple Trp residues, no transmembrane helices, no nuclear localization signals, and no regulatory domains (kinase, SH2, zinc finger). This profile is consistent with a secreted fungal glycoside hydrolase. Among the four options: (A) behavioral response to ethanol is a neural/animal process incompatible with a fungal secreted enzyme; (B) negative regulation of gluconeogenesis is an intracellular metabolic regulatory process; (C) regulation of alternative mRNA splicing is a nuclear RNA-processing activity. Only (D) xylan catabolic process describes an extracellular enzymatic degradation activity, which is the only biological process consistent with a small secreted fungal enzyme. Elimination of the three clearly incompatible options leaves D as the sole defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required for elimination. Specific recognition of GH11 xylanase family motifs (e.g., catalytic Glu in 'IVESHGEY', Trp-rich active site) would confirm xylan specificity over other polysaccharides, but is not needed to select D among the four given options.",
    "reason": "A knowledgeable biologist can reason from the signal peptide, small secreted-protein architecture, fungal context, and absence of regulatory/nuclear features to eliminate options A, B, and C as incompatible with a secreted extracellular enzyme, leaving D as the only viable choice. This does not require memorizing the specific UniProt entry."
  },
  "case_id": "GO_biological_process_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G2X5X8 (sequence matched, 221 aa) is annotated as 'Ethylene-inducing xylanase 4' (EIX4) from Verticillium dahliae, with EC 3.2.1.8 (Endo-1,4-beta-xylanase). The function comment states it is 'involved in the hydrolysis of xylan' with experimental evidence (ECO:0000269, PubMed:33205907). The pathway is 'Glycan degradation; xylan degradation' and the GO annotation GO:0045493 'xylan catabolic process' is directly assigned. The GO term definition matches: 'The chemical reactions and pathways resulting in the breakdown of xylan.' The answer is well-supported by both computational (PROSITE-ProRule) and experimental (PubMed) evidence."
  },
  "important_caveats": [
    "The GO annotation for xylan catabolic process carries evidence code IEA (Inferred from Electronic Annotation via UniPathway), meaning it is computationally derived from the PROSITE-ProRule EC assignment rather than a direct experimental GO annotation. However, the underlying enzymatic function (xylan hydrolysis) is supported by experimental evidence (PubMed:33205907, ECO:0000269).",
    "The protein also has an elicitor function in plant defense (per PubMed:33205907), but this is not among the answer options and does not conflict with the primary enzymatic role.",
    "The reviewer-only evidence confirms sequence match and correct identity, but the evaluated model receives only the raw sequence without any database annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe neural/animal behavior, intracellular metabolic regulation, and nuclear RNA processing respectively—all fundamentally incompatible with a small secreted fungal enzyme. Only D is consistent with the sequence architecture. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G2X5X8 (sequence matched, 221 aa) is annotated as 'Ethylene-inducing xylanase 4' (EIX4) from Verticillium dahliae, with EC 3.2.1.8 (Endo-1,4-beta-xylanase). The function comment states it is 'involved in the hydrolysis of xylan' with experimental evidence (ECO:0000269, PubMed:33205907). The pathway is 'Glycan degradation; xylan degradation' and the GO annotation GO:0045493 'xylan catabolic process' is directly assigned. The GO term definition matches: 'The chemical reactions and pathways resulting in the breakdown of xylan.' The answer is well-supported by both computational (PROSITE-ProRule) and experimental (PubMed) evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~20 residues (MVSFSTLLTACTAITGALGTP) form a classic signal peptide (hydrophobic core with small residues near the cleavage site), indicating a secreted protein. The mature protein (~200 aa) contains multiple Trp residues, no transmembrane helices, no nuclear localization signals, and no regulatory domains (kinase, SH2, zinc finger). This profile is consistent with a secreted fungal glycoside hydrolase. Among the four options: (A) behavioral response to ethanol is a neural/animal process incompatible with a fungal secreted enzyme; (B) negative regulation of gluconeogenesis is an intracellular metabolic regulatory process; (C) regulation of alternative mRNA splicing is a nuclear RNA-processing activity. Only (D) xylan catabolic process describes an extracellular enzymatic degradation activity, which is the only biological process consistent with a small secreted fungal enzyme. Elimination of the three clearly incompatible options leaves D as the sole defensible answer.",
    "missing_item_specific_fact": "None required for elimination. Specific recognition of GH11 xylanase family motifs (e.g., catalytic Glu in 'IVESHGEY', Trp-rich active site) would confirm xylan specificity over other polysaccharides, but is not needed to select D among the four given options.",
    "reason": "A knowledgeable biologist can reason from the signal peptide, small secreted-protein architecture, fungal context, and absence of regulatory/nuclear features to eliminate options A, B, and C as incompatible with a secreted extracellular enzyme, leaving D as the only viable choice. This does not require memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe neural/animal behavior, intracellular metabolic regulation, and nuclear RNA processing respectively—all fundamentally incompatible with a small secreted fungal enzyme. Only D is consistent with the sequence architecture. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The GO annotation for xylan catabolic process carries evidence code IEA (Inferred from Electronic Annotation via UniPathway), meaning it is computationally derived from the PROSITE-ProRule EC assignment rather than a direct experimental GO annotation. However, the underlying enzymatic function (xylan hydrolysis) is supported by experimental evidence (PubMed:33205907, ECO:0000269).",
    "The protein also has an elicitor function in plant defense (per PubMed:33205907), but this is not among the answer options and does not conflict with the primary enzymatic role.",
    "The reviewer-only evidence confirms sequence match and correct identity, but the evaluated model receives only the raw sequence without any database annotation."
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

**Accession:** `G2X5X8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 59. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:38.390496+00:00.  

```json
"G2X5X8"
```

Source SHA-256: `0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:38.390496+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX4"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX4"}]}}
```

Source SHA-256: `0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:38.390496+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"B3VSG7","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (By similarity). May act as an elicitor of plant defense responses in certain plants but does not exhibit any cell death when transiently expressed in N.benthamiana (PubMed:33205907)"}]}
```

Source SHA-256: `0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:38.390496+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X5X8.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:38.390496+00:00.  

```json
{"database":"GO","id":"GO:0045493","properties":[{"key":"GoTerm","value":"P:xylan catabolic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniPathway"}]}
```

Source SHA-256: `0dfdc578abe73de43e82b219133109e0a8de7b7fc008becaf6f430ce76cd2012`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:28:42.014577+00:00.  

```text
ID   EIX4_VERDV              Reviewed;         221 AA.
AC   G2X5X8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-NOV-2011, sequence version 1.
DT   28-JAN-2026, entry version 59.
DE   RecName: Full=Ethylene-inducing xylanase 4 {ECO:0000303|PubMed:33205907};
DE            Short=EIX4 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX4 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX4 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_05294;
OS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)
OS   (Verticillium wilt).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.
OX   NCBI_TaxID=498257;
```

Source SHA-256: `5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)  
**Locator:** `lines 37-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:28:42.014577+00:00.  

```text
CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a
CC       major structural heterogeneous polysaccharide found in plant biomass
CC       representing the second most abundant polysaccharide in the biosphere,
CC       after cellulose (By similarity). May act as an elicitor of plant
CC       defense responses in certain plants but does not exhibit any cell death
CC       when transiently expressed in N.benthamiana (PubMed:33205907).
CC       {ECO:0000250|UniProtKB:B3VSG7, ECO:0000269|PubMed:33205907}.
```

Source SHA-256: `5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)  
**Locator:** `lines 47-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:28:42.014577+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-
CC       ProRule:PRU01097}.
```

Source SHA-256: `5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X5X8?format=txt&versions=59)  
**Locator:** `lines 69-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 1.  
**Retrieved:** 2026-11-02T04:28:42.014577+00:00.  

```text
DR   GO; GO:0045493; P:xylan catabolic process; IEA:UniProtKB-UniPathway.
```

Source SHA-256: `5dd26d11f0073a6c766ef016b0c6982afb7d2092a3f2cdf64c2e3271d9576b1c`.

### Evidence GO2

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
