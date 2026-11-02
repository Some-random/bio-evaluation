# GO_molecular_function_0001

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — endo-1,4-beta-xylanase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVCFSSLFVAASAIAGVFASPVDHEQLAKRQSTPSSQGTHDGYFYSWWTDGGAAATYTNLAGGEYSVSWSNGGNLVGGKGWNPGSARTITYSGTYNPNGNSYLAVYGWTRNPQPWLTPLVVEYYVVENFGTYNPSSGATARGQVTHDGALYRLFESTRTNQPSIDGTATFQQYWAVRDVKRTGGTVNMATFFNAWTAAGMRLGTHNYQVVATEGYFSSGSARINVAGGGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL

[Multiple Choices]
A. lyase activity
B. tau protein binding
C. endo-1,4-beta-xylanase activity
D. D-lactate dehydrogenase activity
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

> The exact sequence matches the UniProt EIX3 entry, which annotates endo-1,4-beta-xylanase activity. The annotation is supported by a catalytic-activity assignment and a function-by-similarity statement; the cited experimental study supports immune-inducing activity, not by itself direct xylan hydrolysis.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment suggests secretion, making tau binding and a typical intracellular D-lactate dehydrogenase less plausible. That does not establish the substrate or catalytic mechanism needed to choose xylanase over lyase activity.


**Missing item-specific fact**

> The protein-specific functional assignment that this secreted protein hydrolyzes xylan; establishing it requires family/homology annotation or biochemical evidence absent from the input.


**Reason**

> Sequence features offer broad contextual clues but do not, without protein-specific functional knowledge, meaningfully resolve the precise activity among the relevant catalytic choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Endo-1,4-beta-xylanase is the best-supported choice; xylan hydrolysis is not lyase activity, and the other options are not supported by the sequence context.


### Important caveats

- The sequence match and historical UniProt record support applicability, but the xylanase catalytic assignment is computationally supported/by similarity rather than directly demonstrated by the cited experimental evidence.
- The exact author annotation snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment suggests secretion, making tau binding and a typical intracellular D-lactate dehydrogenase less plausible. That does not establish the substrate or catalytic mechanism needed to choose xylanase over lyase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that this secreted protein hydrolyzes xylan; establishing it requires family/homology annotation or biochemical evidence absent from the input.",
    "reason": "Sequence features offer broad contextual clues but do not, without protein-specific functional knowledge, meaningfully resolve the precise activity among the relevant catalytic choices."
  },
  "case_id": "GO_molecular_function_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt EIX3 entry, which annotates endo-1,4-beta-xylanase activity. The annotation is supported by a catalytic-activity assignment and a function-by-similarity statement; the cited experimental study supports immune-inducing activity, not by itself direct xylan hydrolysis."
  },
  "important_caveats": [
    "The sequence match and historical UniProt record support applicability, but the xylanase catalytic assignment is computationally supported/by similarity rather than directly demonstrated by the cited experimental evidence.",
    "The exact author annotation snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Endo-1,4-beta-xylanase is the best-supported choice; xylan hydrolysis is not lyase activity, and the other options are not supported by the sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt EIX3 entry, which annotates endo-1,4-beta-xylanase activity. The annotation is supported by a catalytic-activity assignment and a function-by-similarity statement; the cited experimental study supports immune-inducing activity, not by itself direct xylan hydrolysis.",
    "evidence_ids": ["C1", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment suggests secretion, making tau binding and a typical intracellular D-lactate dehydrogenase less plausible. That does not establish the substrate or catalytic mechanism needed to choose xylanase over lyase activity.",
    "missing_item_specific_fact": "The protein-specific functional assignment that this secreted protein hydrolyzes xylan; establishing it requires family/homology annotation or biochemical evidence absent from the input.",
    "reason": "Sequence features offer broad contextual clues but do not, without protein-specific functional knowledge, meaningfully resolve the precise activity among the relevant catalytic choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Endo-1,4-beta-xylanase is the best-supported choice; xylan hydrolysis is not lyase activity, and the other options are not supported by the sequence context."
  },
  "important_caveats": [
    "The sequence match and historical UniProt record support applicability, but the xylanase catalytic assignment is computationally supported/by similarity rather than directly demonstrated by the cited experimental evidence.",
    "The exact author annotation snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry G2X8M4 (Swiss-Prot, reviewed) annotates this protein as Ethylene-inducing xylanase 3 (EIX3) from Verticillium dahliae with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The sequence matches exactly (SHA256 confirmed). The EC assignment derives from PROSITE-ProRule (ECO:0000255, computational motif-based inference) and the GO term is IEA:UniProtKB-EC. The FUNCTION comment also notes 'By similarity' evidence plus experimental data (PubMed:33205907) for immunity-inducing activity. While the catalytic annotation is primarily computational/curated rather than directly experimentally measured for xylanase activity in this specific protein, the Swiss-Prot curation and consistent annotation across name, EC, catalytic activity, and GO term robustly support choice C.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an N-terminal signal peptide (MVCFSSLFVAASAIAGVFA...), indicating a secreted protein. The mature domain (~270 AA) displays an aromatic-residue-rich, compact architecture with motifs (e.g., 'GYFYSWWTDGG', 'YTNLAGGEYSVSWSNGGN') characteristic of a β-jelly roll fold found in glycosyl hydrolase family 11 (GH11) enzymes. Among the four options, only C (endo-1,4-beta-xylanase, EC 3.2.1.8) is a glycosyl hydrolase consistent with this fold. Option B (tau protein binding) is implausible for a secreted fungal protein with no mammalian cytoskeletal context. Option D (D-lactate dehydrogenase, EC 1.1.99.6) requires a Rossmann-fold oxidoreductase signature absent here. Option A (lyase, EC 4) involves non-hydrolytic bond cleavage and does not match the β-jelly roll glycosyl hydrolase architecture. Thus, fold recognition and elimination of clearly mismatched options provide a reasoning path to C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question can be answered by recognizing the signal peptide, identifying the β-jelly roll fold features consistent with GH11 glycosyl hydrolases, and eliminating options B (mammalian-specific binding), D (oxidoreductase fold absent), and A (wrong enzyme class for the observed fold). This requires specialized structural biology knowledge but does not require memorizing the specific UniProt entry or protein name. The distractors are sufficiently distinct (different enzyme classes, different biological contexts) to allow reasoning-based discrimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct functional categories: a hydrolase (C), a lyase (A), an oxidoreductase (D), and a non-enzymatic protein-protein interaction (B). The sequence features clearly favor a secreted glycosyl hydrolase, making C the only defensible choice. No other option is biologically plausible for this sequence.


### Important caveats

- The EC 3.2.1.8 assignment is via PROSITE-ProRule (ECO:0000255), a computational motif-based inference, not direct experimental kinetics on this specific protein.
- The GO annotation is IEA (Inferred from Electronic Annotation), derived from the EC number.
- The 'By similarity' evidence (ECO:0000250, from B3VSG7) means some functional aspects are transferred from a homolog rather than demonstrated de novo for EIX3.
- The protein is in Swiss-Prot (reviewed), which provides curator-level confidence, but the underlying catalytic evidence remains computational.
- The immunity-inducing activity (the actual experimental finding in PubMed:33205907) is distinct from the xylanase catalytic activity asked about in this question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an N-terminal signal peptide (MVCFSSLFVAASAIAGVFA...), indicating a secreted protein. The mature domain (~270 AA) displays an aromatic-residue-rich, compact architecture with motifs (e.g., 'GYFYSWWTDGG', 'YTNLAGGEYSVSWSNGGN') characteristic of a β-jelly roll fold found in glycosyl hydrolase family 11 (GH11) enzymes. Among the four options, only C (endo-1,4-beta-xylanase, EC 3.2.1.8) is a glycosyl hydrolase consistent with this fold. Option B (tau protein binding) is implausible for a secreted fungal protein with no mammalian cytoskeletal context. Option D (D-lactate dehydrogenase, EC 1.1.99.6) requires a Rossmann-fold oxidoreductase signature absent here. Option A (lyase, EC 4) involves non-hydrolytic bond cleavage and does not match the β-jelly roll glycosyl hydrolase architecture. Thus, fold recognition and elimination of clearly mismatched options provide a reasoning path to C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question can be answered by recognizing the signal peptide, identifying the β-jelly roll fold features consistent with GH11 glycosyl hydrolases, and eliminating options B (mammalian-specific binding), D (oxidoreductase fold absent), and A (wrong enzyme class for the observed fold). This requires specialized structural biology knowledge but does not require memorizing the specific UniProt entry or protein name. The distractors are sufficiently distinct (different enzyme classes, different biological contexts) to allow reasoning-based discrimination."
  },
  "case_id": "GO_molecular_function_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C8",
      "H1",
      "H3",
      "H4",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry G2X8M4 (Swiss-Prot, reviewed) annotates this protein as Ethylene-inducing xylanase 3 (EIX3) from Verticillium dahliae with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The sequence matches exactly (SHA256 confirmed). The EC assignment derives from PROSITE-ProRule (ECO:0000255, computational motif-based inference) and the GO term is IEA:UniProtKB-EC. The FUNCTION comment also notes 'By similarity' evidence plus experimental data (PubMed:33205907) for immunity-inducing activity. While the catalytic annotation is primarily computational/curated rather than directly experimentally measured for xylanase activity in this specific protein, the Swiss-Prot curation and consistent annotation across name, EC, catalytic activity, and GO term robustly support choice C."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment is via PROSITE-ProRule (ECO:0000255), a computational motif-based inference, not direct experimental kinetics on this specific protein.",
    "The GO annotation is IEA (Inferred from Electronic Annotation), derived from the EC number.",
    "The 'By similarity' evidence (ECO:0000250, from B3VSG7) means some functional aspects are transferred from a homolog rather than demonstrated de novo for EIX3.",
    "The protein is in Swiss-Prot (reviewed), which provides curator-level confidence, but the underlying catalytic evidence remains computational.",
    "The immunity-inducing activity (the actual experimental finding in PubMed:33205907) is distinct from the xylanase catalytic activity asked about in this question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct functional categories: a hydrolase (C), a lyase (A), an oxidoreductase (D), and a non-enzymatic protein-protein interaction (B). The sequence features clearly favor a secreted glycosyl hydrolase, making C the only defensible choice. No other option is biologically plausible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"GO_molecular_function_0001","expected_answer_check":{"judgment":"supported","reason":"UniProtKB entry G2X8M4 (Swiss-Prot, reviewed) annotates this protein as Ethylene-inducing xylanase 3 (EIX3) from Verticillium dahliae with EC 3.2.1.8 and GO:0031176 (endo-1,4-beta-xylanase activity). The sequence matches exactly (SHA256 confirmed). The EC assignment derives from PROSITE-ProRule (ECO:0000255, computational motif-based inference) and the GO term is IEA:UniProtKB-EC. The FUNCTION comment also notes 'By similarity' evidence plus experimental data (PubMed:33205907) for immunity-inducing activity. While the catalytic annotation is primarily computational/curated rather than directly experimentally measured for xylanase activity in this specific protein, the Swiss-Prot curation and consistent annotation across name, EC, catalytic activity, and GO term robustly support choice C.","evidence_ids":["C1","C4","C5","C6","C8","H1","H3","H4","H6","GO2"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The sequence contains an N-terminal signal peptide (MVCFSSLFVAASAIAGVFA...), indicating a secreted protein. The mature domain (~270 AA) displays an aromatic-residue-rich, compact architecture with motifs (e.g., 'GYFYSWWTDGG', 'YTNLAGGEYSVSWSNGGN') characteristic of a β-jelly roll fold found in glycosyl hydrolase family 11 (GH11) enzymes. Among the four options, only C (endo-1,4-beta-xylanase, EC 3.2.1.8) is a glycosyl hydrolase consistent with this fold. Option B (tau protein binding) is implausible for a secreted fungal protein with no mammalian cytoskeletal context. Option D (D-lactate dehydrogenase, EC 1.1.99.6) requires a Rossmann-fold oxidoreductase signature absent here. Option A (lyase, EC 4) involves non-hydrolytic bond cleavage and does not match the β-jelly roll glycosyl hydrolase architecture. Thus, fold recognition and elimination of clearly mismatched options provide a reasoning path to C.","missing_item_specific_fact":"","reason":"The question can be answered by recognizing the signal peptide, identifying the β-jelly roll fold features consistent with GH11 glycosyl hydrolases, and eliminating options B (mammalian-specific binding), D (oxidoreductase fold absent), and A (wrong enzyme class for the observed fold). This requires specialized structural biology knowledge but does not require memorizing the specific UniProt entry or protein name. The distractors are sufficiently distinct (different enzyme classes, different biological contexts) to allow reasoning-based discrimination."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"The four options span distinct functional categories: a hydrolase (C), a lyase (A), an oxidoreductase (D), and a non-enzymatic protein-protein interaction (B). The sequence features clearly favor a secreted glycosyl hydrolase, making C the only defensible choice. No other option is biologically plausible for this sequence."},"important_caveats":["The EC 3.2.1.8 assignment is via PROSITE-ProRule (ECO:0000255), a computational motif-based inference, not direct experimental kinetics on this specific protein.","The GO annotation is IEA (Inferred from Electronic Annotation), derived from the EC number.","The 'By similarity' evidence (ECO:0000250, from B3VSG7) means some functional aspects are transferred from a homolog rather than demonstrated de novo for EIX3.","The protein is in Swiss-Prot (reviewed), which provides curator-level confidence, but the underlying catalytic evidence remains computational.","The immunity-inducing activity (the actual experimental finding in PubMed:33205907) is distinct from the xylanase catalytic activity asked about in this question."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `G2X8M4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 61. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:39.111291+00:00.  

```json
"G2X8M4"
```

Source SHA-256: `0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:39.111291+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX3"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"Ethylene-inducing xylanase 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33205907","source":"PubMed"}],"value":"EIX3"}]}}
```

Source SHA-256: `0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:39.111291+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"B3VSG7","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"33205907","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (By similarity). Exhibits immunity-inducing activity in Nicotiana benthamiana (PubMed:33205907). Can induce strong oxidative burst, activate the expression of defense-related genes, and increase resistance against oomycete and fungal pathogens in N.benthamiana (PubMed:33205907)"}]}
```

Source SHA-256: `0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:39.111291+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X8M4.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:39.111291+00:00.  

```json
{"database":"GO","id":"GO:0031176","properties":[{"key":"GoTerm","value":"F:endo-1,4-beta-xylanase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
```

Source SHA-256: `0d3245ba74b9e0c578d36f87f7508c596ceb2d25929e23083625cf29ccee1e4b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-02T04:28:41.833412+00:00.  

```text
ID   EIX3_VERDV              Reviewed;         294 AA.
AC   G2X8M4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-NOV-2011, sequence version 1.
DT   28-JAN-2026, entry version 61.
DE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};
DE            Short=EIX3 {ECO:0000303|PubMed:33205907};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};
DE   Flags: Precursor;
GN   Name=EIX3 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_06165;
OS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)
OS   (Verticillium wilt).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.
OX   NCBI_TaxID=498257;
```

Source SHA-256: `dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)  
**Locator:** `lines 37-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-02T04:28:41.833412+00:00.  

```text
CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a
CC       major structural heterogeneous polysaccharide found in plant biomass
CC       representing the second most abundant polysaccharide in the biosphere,
CC       after cellulose (By similarity). Exhibits immunity-inducing activity in
CC       Nicotiana benthamiana (PubMed:33205907). Can induce strong oxidative
CC       burst, activate the expression of defense-related genes, and increase
CC       resistance against oomycete and fungal pathogens in N.benthamiana
CC       (PubMed:33205907). {ECO:0000250|UniProtKB:B3VSG7,
CC       ECO:0000269|PubMed:33205907}.
```

Source SHA-256: `dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)  
**Locator:** `lines 46-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-02T04:28:41.833412+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};
```

Source SHA-256: `dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X8M4?format=txt&versions=61)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-02T04:28:41.833412+00:00.  

```text
DR   GO; GO:0031176; F:endo-1,4-beta-xylanase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `dbdf6ed8a8e0617cac295b004204625338e46a980bf24a819e409ad502cf70e7`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 173997-174018`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031176
name: endo-1,4-beta-xylanase activity
namespace: molecular_function
def: "Catalysis of the endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans." [EC:3.2.1.8]
synonym: "1,4-beta-D-xylan xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "1,4-beta-xylan xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "beta-1,4-xylan xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "beta-1,4-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "beta-D-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "beta-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "endo-(1,4)-beta-xylanase(1,4)-beta-xylan 4-xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "endo-(1->4)-beta-xylanase(1->4)-beta-xylan 4-xylanohydrolase activity" RELATED [EC:3.2.1.8]
synonym: "endo-1,4-beta-D-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "endo-1,4-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "endo-beta-1,4-xylanase activity" RELATED [EC:3.2.1.8]
synonym: "xylanase" BROAD [EC:3.2.1.8]
xref: EC:3.2.1.8
xref: MetaCyc:3.2.1.8-RXN
is_a: GO:0097599 ! xylanase activity
property_value: skos:exactMatch EC:3.2.1.8

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
