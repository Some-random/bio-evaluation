# GO_molecular_function_0169

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — transaminase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MANSWRISALRERHLALGSQLEDWNGMGTAWTYASDLADHHEAIRTRAGLMDVSGLKKVHYVGPHAESLLDYATTRDIGKLYPGKSVYACLLDEDGKFIDDCIVYRTGPNAFMVVHGAGTGHEMLIRSAQGRQVAVLFDDDLHDLSLQGPRAVDFLAEHVPGIRDLPYFHHLQTKLFDRPVMISRTGYTGERGYEIFCKAADAPAIWDAILEQGKGYGIIPCAFTALDWLRVESYLLFFPYDNSQMYPFADQKAGDTLWELGLDFTVSPGKQDFRGAGEHYRLKGQERFKIFGVLLDGHQAAQGGDTLWHDGRQVGVITCSMYSRLTERSMAIARVEPQIAEQGVPLQVRGSLDCAAIAHSLPFDDPEKKKRTAKG

[Multiple Choices]
A. methylated histone binding
B. transaminase activity
C. ribonuclease III activity
D. DNA-binding transcription factor activity
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

> The exact sequence is annotated with GO:0008483 (transaminase activity) in the archived UniProt record, but the assignment is IEA:UniProtKB-KW, so it is computational annotation rather than direct experimental proof. The cited functional description identifies the protein as the gamma subunit of a heme-dependent oxidative N-demethylase and says it may act as an aminomethyltransferase; that does not independently establish transaminase activity in the narrower GO sense.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The bacterial sequence is a globular protein without an obvious DNA-binding or RNA-processing signature, which makes the transcription-factor and RNase III choices less plausible. But that broad reasoning does not identify transaminase activity specifically.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental characterization linking this sequence to amino-group transfer is not supplied in the question.


**Reason**

> Choosing B depends on a protein-specific annotation or functional fact absent from the input; general sequence heuristics do not establish this precise molecular function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the only choice supported by the matched-sequence GO annotation. The evidence does, however, leave a caveat about whether the IEA transaminase label accurately captures the described possible aminomethyltransferase role.


### Important caveats

- The sequence matches the cited UniProt record exactly.
- The transaminase GO assignment is inferred (IEA), whereas the functional description cites experimental evidence for the protein's role in the HODM complex and describes its aminomethyltransferase role as possible.
- The supplied evidence does not independently validate transaminase activity as distinct from aminomethyltransferase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The bacterial sequence is a globular protein without an obvious DNA-binding or RNA-processing signature, which makes the transcription-factor and RNase III choices less plausible. But that broad reasoning does not identify transaminase activity specifically.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization linking this sequence to amino-group transfer is not supplied in the question.",
    "reason": "Choosing B depends on a protein-specific annotation or functional fact absent from the input; general sequence heuristics do not establish this precise molecular function."
  },
  "case_id": "GO_molecular_function_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence is annotated with GO:0008483 (transaminase activity) in the archived UniProt record, but the assignment is IEA:UniProtKB-KW, so it is computational annotation rather than direct experimental proof. The cited functional description identifies the protein as the gamma subunit of a heme-dependent oxidative N-demethylase and says it may act as an aminomethyltransferase; that does not independently establish transaminase activity in the narrower GO sense."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record exactly.",
    "The transaminase GO assignment is inferred (IEA), whereas the functional description cites experimental evidence for the protein's role in the HODM complex and describes its aminomethyltransferase role as possible.",
    "The supplied evidence does not independently validate transaminase activity as distinct from aminomethyltransferase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only choice supported by the matched-sequence GO annotation. The evidence does, however, leave a caveat about whether the IEA transaminase label accurately captures the described possible aminomethyltransferase role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence is annotated with GO:0008483 (transaminase activity) in the archived UniProt record, but the assignment is IEA:UniProtKB-KW, so it is computational annotation rather than direct experimental proof. The cited functional description identifies the protein as the gamma subunit of a heme-dependent oxidative N-demethylase and says it may act as an aminomethyltransferase; that does not independently establish transaminase activity in the narrower GO sense.",
    "evidence_ids": ["H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The bacterial sequence is a globular protein without an obvious DNA-binding or RNA-processing signature, which makes the transcription-factor and RNase III choices less plausible. But that broad reasoning does not identify transaminase activity specifically.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization linking this sequence to amino-group transfer is not supplied in the question.",
    "reason": "Choosing B depends on a protein-specific annotation or functional fact absent from the input; general sequence heuristics do not establish this precise molecular function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the only choice supported by the matched-sequence GO annotation. The evidence does, however, leave a caveat about whether the IEA transaminase label accurately captures the described possible aminomethyltransferase role."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record exactly.",
    "The transaminase GO assignment is inferred (IEA), whereas the functional description cites experimental evidence for the protein's role in the HODM complex and describes its aminomethyltransferase role as possible.",
    "The supplied evidence does not independently validate transaminase activity as distinct from aminomethyltransferase activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A4XXZ0 (HODMG_ECTM1) carries a direct GO annotation: 'DR GO; GO:0008483; F:transaminase activity; IEA:UniProtKB-KW' (evidence H4). The protein's function comment describes it as an aminomethyltransferase (EC 2.1.2.-) involved in transferring an aminomethyl group to THF. While EC 2.1.2.- (aminomethyltransferases) and EC 2.6.1.- (transaminases) are distinct EC subclasses, the UniProt keyword-based annotation explicitly assigns GO:0008483 (transaminase activity) to this protein. The evidence code is IEA (Inferred from Electronic Annotation via UniProtKB keyword), meaning this is a computational/keyword-based assignment rather than direct experimental proof of classical transaminase activity. Nevertheless, the annotation exists in the database and the author's expected answer matches it.

Citations as saved: [H4](#evidence-h4), [H3](#evidence-h3), [C5](#evidence-c5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs consistent with a PLP-dependent class III aminotransferase/transferase fold (e.g., the 'HGAGTGHE' region resembling a PLP-binding segment, and the C-terminal 'GYGIIPCAFTALDWLRVESYLLFFPY' region resembling the dimerization domain of class III aminotransferases). Among the four options, B (transaminase activity) is the only transferase-class activity. Options A (methylated histone binding), C (ribonuclease III activity), and D (DNA-binding transcription factor activity) require entirely different structural motifs (chromo/Tudor/PHD domains, RNase III fold, helix-turn-helix/zinc-finger DNA-binding domains) that are absent from this sequence. Recognizing transferase-like fold features and eliminating the three non-transferase options provides a biological reasoning path to B.


**Missing item-specific fact**

> The precise distinction between aminomethyltransferase (EC 2.1.2.-) and transaminase (EC 2.6.1.-) activity, and the knowledge that UniProt's keyword system maps this protein to GO:0008483, would require database lookup. However, this level of EC-subclass precision is not needed to select B among the four given options.


**Reason**

> A model with general knowledge of enzyme folds can recognize transferase-like features in the sequence and eliminate the three non-transferase distractors (histone binding, RNase III, DNA-binding TF), arriving at B as the only transferase option. The specific GO term 'transaminase activity' is imprecise for this protein's actual aminomethyltransferase function, but among the provided choices it is the best fit.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D describe activities (histone binding, RNase III cleavage, sequence-specific DNA binding) that require structural motifs clearly absent from this sequence. B is the only transferase-class option and the only one consistent with the observed fold features. No other option is defensible.


### Important caveats

- The GO:0008483 annotation is IEA:UniProtKB-KW (keyword-based inference), not direct experimental evidence of transaminase activity. The protein's experimentally characterized function (PubMed:27851736, Nature 2016) is aminomethyltransferase (EC 2.1.2.-), transferring an aminomethyl group to THF, which is mechanistically distinct from classical transamination (EC 2.6.1.-).
- The protein is the gamma subunit of a multi-component HODM enzyme; its isolated catalytic role as aminomethyltransferase is stated with 'may act as' language in UniProt, indicating some uncertainty.
- The sequence features suggestive of a class III aminotransferase fold are consistent with the protein's PAS-to-enzyme evolutionary transition described in the primary literature, meaning the fold is related to but not identical to canonical aminotransferases.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs consistent with a PLP-dependent class III aminotransferase/transferase fold (e.g., the 'HGAGTGHE' region resembling a PLP-binding segment, and the C-terminal 'GYGIIPCAFTALDWLRVESYLLFFPY' region resembling the dimerization domain of class III aminotransferases). Among the four options, B (transaminase activity) is the only transferase-class activity. Options A (methylated histone binding), C (ribonuclease III activity), and D (DNA-binding transcription factor activity) require entirely different structural motifs (chromo/Tudor/PHD domains, RNase III fold, helix-turn-helix/zinc-finger DNA-binding domains) that are absent from this sequence. Recognizing transferase-like fold features and eliminating the three non-transferase options provides a biological reasoning path to B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise distinction between aminomethyltransferase (EC 2.1.2.-) and transaminase (EC 2.6.1.-) activity, and the knowledge that UniProt's keyword system maps this protein to GO:0008483, would require database lookup. However, this level of EC-subclass precision is not needed to select B among the four given options.",
    "reason": "A model with general knowledge of enzyme folds can recognize transferase-like features in the sequence and eliminate the three non-transferase distractors (histone binding, RNase III, DNA-binding TF), arriving at B as the only transferase option. The specific GO term 'transaminase activity' is imprecise for this protein's actual aminomethyltransferase function, but among the provided choices it is the best fit."
  },
  "case_id": "GO_molecular_function_0169",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H3",
      "C5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A4XXZ0 (HODMG_ECTM1) carries a direct GO annotation: 'DR GO; GO:0008483; F:transaminase activity; IEA:UniProtKB-KW' (evidence H4). The protein's function comment describes it as an aminomethyltransferase (EC 2.1.2.-) involved in transferring an aminomethyl group to THF. While EC 2.1.2.- (aminomethyltransferases) and EC 2.6.1.- (transaminases) are distinct EC subclasses, the UniProt keyword-based annotation explicitly assigns GO:0008483 (transaminase activity) to this protein. The evidence code is IEA (Inferred from Electronic Annotation via UniProtKB keyword), meaning this is a computational/keyword-based assignment rather than direct experimental proof of classical transaminase activity. Nevertheless, the annotation exists in the database and the author's expected answer matches it."
  },
  "important_caveats": [
    "The GO:0008483 annotation is IEA:UniProtKB-KW (keyword-based inference), not direct experimental evidence of transaminase activity. The protein's experimentally characterized function (PubMed:27851736, Nature 2016) is aminomethyltransferase (EC 2.1.2.-), transferring an aminomethyl group to THF, which is mechanistically distinct from classical transamination (EC 2.6.1.-).",
    "The protein is the gamma subunit of a multi-component HODM enzyme; its isolated catalytic role as aminomethyltransferase is stated with 'may act as' language in UniProt, indicating some uncertainty.",
    "The sequence features suggestive of a class III aminotransferase fold are consistent with the protein's PAS-to-enzyme evolutionary transition described in the primary literature, meaning the fold is related to but not identical to canonical aminotransferases."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D describe activities (histone binding, RNase III cleavage, sequence-specific DNA binding) that require structural motifs clearly absent from this sequence. B is the only transferase-class option and the only one consistent with the observed fold features. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0169",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A4XXZ0 (HODMG_ECTM1) carries a direct GO annotation: 'DR GO; GO:0008483; F:transaminase activity; IEA:UniProtKB-KW' (evidence H4). The protein's function comment describes it as an aminomethyltransferase (EC 2.1.2.-) involved in transferring an aminomethyl group to THF. While EC 2.1.2.- (aminomethyltransferases) and EC 2.6.1.- (transaminases) are distinct EC subclasses, the UniProt keyword-based annotation explicitly assigns GO:0008483 (transaminase activity) to this protein. The evidence code is IEA (Inferred from Electronic Annotation via UniProtKB keyword), meaning this is a computational/keyword-based assignment rather than direct experimental proof of classical transaminase activity. Nevertheless, the annotation exists in the database and the author's expected answer matches it.",
    "evidence_ids": ["H4", "H3", "C5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs consistent with a PLP-dependent class III aminotransferase/transferase fold (e.g., the 'HGAGTGHE' region resembling a PLP-binding segment, and the C-terminal 'GYGIIPCAFTALDWLRVESYLLFFPY' region resembling the dimerization domain of class III aminotransferases). Among the four options, B (transaminase activity) is the only transferase-class activity. Options A (methylated histone binding), C (ribonuclease III activity), and D (DNA-binding transcription factor activity) require entirely different structural motifs (chromo/Tudor/PHD domains, RNase III fold, helix-turn-helix/zinc-finger DNA-binding domains) that are absent from this sequence. Recognizing transferase-like fold features and eliminating the three non-transferase options provides a biological reasoning path to B.",
    "missing_item_specific_fact": "The precise distinction between aminomethyltransferase (EC 2.1.2.-) and transaminase (EC 2.6.1.-) activity, and the knowledge that UniProt's keyword system maps this protein to GO:0008483, would require database lookup. However, this level of EC-subclass precision is not needed to select B among the four given options.",
    "reason": "A model with general knowledge of enzyme folds can recognize transferase-like features in the sequence and eliminate the three non-transferase distractors (histone binding, RNase III, DNA-binding TF), arriving at B as the only transferase option. The specific GO term 'transaminase activity' is imprecise for this protein's actual aminomethyltransferase function, but among the provided choices it is the best fit."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D describe activities (histone binding, RNase III cleavage, sequence-specific DNA binding) that require structural motifs clearly absent from this sequence. B is the only transferase-class option and the only one consistent with the observed fold features. No other option is defensible."
  },
  "important_caveats": [
    "The GO:0008483 annotation is IEA:UniProtKB-KW (keyword-based inference), not direct experimental evidence of transaminase activity. The protein's experimentally characterized function (PubMed:27851736, Nature 2016) is aminomethyltransferase (EC 2.1.2.-), transferring an aminomethyl group to THF, which is mechanistically distinct from classical transamination (EC 2.6.1.-).",
    "The protein is the gamma subunit of a multi-component HODM enzyme; its isolated catalytic role as aminomethyltransferase is stated with 'may act as' language in UniProt, indicating some uncertainty.",
    "The sequence features suggestive of a class III aminotransferase fold are consistent with the protein's PAS-to-enzyme evolutionary transition described in the primary literature, meaning the fold is related to but not identical to canonical aminotransferases."
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

**Accession:** `A4XXZ0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 100. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXZ0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.222940+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27851736","source":"PubMed"}],"value":"Component of the heme-dependent oxidative N-demethylase (HODM) enzyme, that catalyzes the NADPH-dependent oxidation of dimethylamine (DMA) to methylamine (MA) and formaldehyde. Functions in bacterial methylated amine catabolism, linking alkylamine oxidation to the tetrahydrofolate C1 pool. The gamma subunit of HODM may act as an aminomethyltransferase involved in the detoxification of formaldehyde released by the alpha subunit; this process requires tetrahydrofolate (THF)"}]}
```

Source SHA-256: `6f0eed2868cd9a6e6f3e2b1f2663c95fada28bf957433c33cd393818d18e5334`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXZ0?format=txt&versions=100)  
**Locator:** `lines 32-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:27:04.659432+00:00.  

```text
CC   -!- FUNCTION: Component of the heme-dependent oxidative N-demethylase
CC       (HODM) enzyme, that catalyzes the NADPH-dependent oxidation of
CC       dimethylamine (DMA) to methylamine (MA) and formaldehyde. Functions in
CC       bacterial methylated amine catabolism, linking alkylamine oxidation to
CC       the tetrahydrofolate C1 pool. The gamma subunit of HODM may act as an
CC       aminomethyltransferase involved in the detoxification of formaldehyde
CC       released by the alpha subunit; this process requires tetrahydrofolate
CC       (THF). {ECO:0000269|PubMed:27851736}.
```

Source SHA-256: `1c758d997424eaebb18659e5383cd3333a76a5ee74453dcecd72062942392ca5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXZ0?format=txt&versions=100)  
**Locator:** `lines 58-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:27:04.659432+00:00.  

```text
DR   GO; GO:0008483; F:transaminase activity; IEA:UniProtKB-KW.
```

Source SHA-256: `1c758d997424eaebb18659e5383cd3333a76a5ee74453dcecd72062942392ca5`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 84102-84112`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008483
name: transaminase activity
namespace: molecular_function
def: "Catalysis of the transfer of an amino group to an acceptor, usually a 2-oxo acid." [EC:2.6.1.-]
synonym: "aminotransferase activity" EXACT []
xref: EC:2.6.1.-
xref: Reactome:R-HSA-1237102 "Transamination of MOB to methionine"
is_a: GO:0016769 ! transferase activity, transferring nitrogenous groups
property_value: skos:exactMatch EC:2.6.1.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 169. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
