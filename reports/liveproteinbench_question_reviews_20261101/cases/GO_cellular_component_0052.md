# GO_cellular_component_0052

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQLRKALLVIFVAYLLVTDEAEAFWGFLGKLAMKAVPSLIGGNKSSSKRKREIEDLFDPYQKDLDLQRLDRFFSQFQ

[Multiple Choices]
A. membrane
B. lipid droplet
C. host cytoskeleton
D. apicoplast
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

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the peptide as secreted and as acting at the target cell membrane, supporting membrane among the listed choices. This is a curated annotation, not direct experimental localization evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is compatible with secretion, and the short, basic peptide sequence is compatible with an antimicrobial peptide; these features make membrane interaction plausible and the organelle distractors less likely.


**Missing item-specific fact**

> The sequence alone does not establish that this particular peptide has antimicrobial activity or that its relevant cellular component is the target cell membrane; that protein-specific functional annotation is needed to select membrane as the requested location.


**Reason**

> Sequence features offer a plausible hypothesis but do not establish membrane localization. The decisive target-membrane annotation is item-specific and absent from the question input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, membrane is supported by the target-cell-membrane annotation. The record also describes the peptide as secreted, a location not offered as an option, so membrane should be understood as its annotated target rather than necessarily its primary residence.


### Important caveats

- The matched database annotation includes both secreted and target-cell-membrane locations; it does not establish that membrane is the peptide's sole or primary residence.
- The excerpts identify curated annotations and a cited antimicrobial-peptide paper, but do not independently demonstrate experimental localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is compatible with secretion, and the short, basic peptide sequence is compatible with an antimicrobial peptide; these features make membrane interaction plausible and the organelle distractors less likely.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence alone does not establish that this particular peptide has antimicrobial activity or that its relevant cellular component is the target cell membrane; that protein-specific functional annotation is needed to select membrane as the requested location.",
    "reason": "Sequence features offer a plausible hypothesis but do not establish membrane localization. The decisive target-membrane annotation is item-specific and absent from the question input."
  },
  "case_id": "GO_cellular_component_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the peptide as secreted and as acting at the target cell membrane, supporting membrane among the listed choices. This is a curated annotation, not direct experimental localization evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The matched database annotation includes both secreted and target-cell-membrane locations; it does not establish that membrane is the peptide's sole or primary residence.",
    "The excerpts identify curated annotations and a cited antimicrobial-peptide paper, but do not independently demonstrate experimental localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, membrane is supported by the target-cell-membrane annotation. The record also describes the peptide as secreted, a location not offered as an option, so membrane should be understood as its annotated target rather than necessarily its primary residence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the peptide as secreted and as acting at the target cell membrane, supporting membrane among the listed choices. This is a curated annotation, not direct experimental localization evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is compatible with secretion, and the short, basic peptide sequence is compatible with an antimicrobial peptide; these features make membrane interaction plausible and the organelle distractors less likely.",
    "missing_item_specific_fact": "The sequence alone does not establish that this particular peptide has antimicrobial activity or that its relevant cellular component is the target cell membrane; that protein-specific functional annotation is needed to select membrane as the requested location.",
    "reason": "Sequence features offer a plausible hypothesis but do not establish membrane localization. The decisive target-membrane annotation is item-specific and absent from the question input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, membrane is supported by the target-cell-membrane annotation. The record also describes the peptide as secreted, a location not offered as an option, so membrane should be understood as its annotated target rather than necessarily its primary residence."
  },
  "important_caveats": [
    "The matched database annotation includes both secreted and target-cell-membrane locations; it does not establish that membrane is the peptide's sole or primary residence.",
    "The excerpts identify curated annotations and a cited antimicrobial-peptide paper, but do not independently demonstrate experimental localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5, H3) lists 'Target cell membrane' with evidence ECO:0000305 from PubMed 26352292, and the GO cross-reference (H5) assigns GO:0044218 'other organism cell membrane,' which is a child of GO:0016020 'membrane' (option A). The protein is VpAmp2.0, an antimicrobial peptide from scorpion venom gland that functions by disrupting target (microbial) membranes. Among the four options, 'membrane' is the only one consistent with the annotation. The annotation is computational/experimental (ECO:0000305 is 'curator inference based on publication'), not purely sequence-based, but it is a legitimate database annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H5](#evidence-h5), [C7](#evidence-c7), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 77-aa sequence shows a hydrophobic N-terminal signal peptide (MQLRKALLVIFVAYLLVT) followed by a small, highly cationic (multiple K/R), amphipathic mature peptide with aromatic residues (W, F, Y). These are canonical hallmarks of secreted antimicrobial peptides, which function by binding and disrupting microbial membranes. This general biological knowledge allows one to select 'membrane' over the distractors: (1) 'apicoplast' is restricted to apicomplexan parasites and is irrelevant to a scorpion peptide; (2) 'host cytoskeleton' applies to intracellular pathogen interactions, not secreted venom peptides; (3) 'lipid droplet' is an intracellular organelle and its associated proteins do not display the cationic amphipathic membrane-perturbing signature seen here. Thus, recognizing the peptide class (small cationic amphipathic secreted peptide → antimicrobial → membrane-targeting) provides a concrete biological argument to distinguish the answer.


**Missing item-specific fact**

> None strictly required. One could argue that knowing the specific peptide is VpAmp2.0 and its experimental characterization as a membrane-disrupting antimicrobial peptide would strengthen confidence, but the sequence features and general antimicrobial peptide biology are sufficient to reach 'membrane' over the other three options.


**Reason**

> The sequence contains recognizable features of a secreted antimicrobial peptide (signal peptide, cationic amphipathic mature region). General knowledge of antimicrobial peptide mechanism (membrane disruption) combined with elimination of biologically implausible distractors (apicoplast for a scorpion, host cytoskeleton for a secreted peptide, lipid droplet for a cationic membrane-perturbing peptide) provides a defensible reasoning path to 'membrane.'


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only 'membrane' is consistent with a secreted antimicrobial peptide. 'Apicoplast' is taxonomically impossible for a scorpion protein. 'Host cytoskeleton' pertains to intracellular pathogen biology, not secreted venom peptides. 'Lipid droplet' is an intracellular organelle inconsistent with a secreted cationic peptide. No other option is defensible.


### Important caveats

- The UniProt annotation 'Target cell membrane' (ECO:0000305) is curator inference from a publication, not direct experimental localization. The GO annotation GO:0044218 is IEA (inferred from electronic annotation), a lower-confidence evidence code.
- The option 'membrane' (GO:0016020) is a very broad term; the specific annotation is 'other organism cell membrane' (GO:0044218). The question does not distinguish between the protein's own cell membrane and a target organism's membrane, but 'membrane' is still the best fit among the given options.
- The primary GO annotation is GO:0005576 'extracellular region' (IEA), which is not offered as an option. The question forces a choice among four terms, and 'membrane' is the closest to the functional annotation.
- Reviewer-only evidence was used to verify the expected answer; the evaluated model had access only to the 77-aa sequence and the four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 77-aa sequence shows a hydrophobic N-terminal signal peptide (MQLRKALLVIFVAYLLVT) followed by a small, highly cationic (multiple K/R), amphipathic mature peptide with aromatic residues (W, F, Y). These are canonical hallmarks of secreted antimicrobial peptides, which function by binding and disrupting microbial membranes. This general biological knowledge allows one to select 'membrane' over the distractors: (1) 'apicoplast' is restricted to apicomplexan parasites and is irrelevant to a scorpion peptide; (2) 'host cytoskeleton' applies to intracellular pathogen interactions, not secreted venom peptides; (3) 'lipid droplet' is an intracellular organelle and its associated proteins do not display the cationic amphipathic membrane-perturbing signature seen here. Thus, recognizing the peptide class (small cationic amphipathic secreted peptide → antimicrobial → membrane-targeting) provides a concrete biological argument to distinguish the answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. One could argue that knowing the specific peptide is VpAmp2.0 and its experimental characterization as a membrane-disrupting antimicrobial peptide would strengthen confidence, but the sequence features and general antimicrobial peptide biology are sufficient to reach 'membrane' over the other three options.",
    "reason": "The sequence contains recognizable features of a secreted antimicrobial peptide (signal peptide, cationic amphipathic mature region). General knowledge of antimicrobial peptide mechanism (membrane disruption) combined with elimination of biologically implausible distractors (apicoplast for a scorpion, host cytoskeleton for a secreted peptide, lipid droplet for a cationic membrane-perturbing peptide) provides a defensible reasoning path to 'membrane.'"
  },
  "case_id": "GO_cellular_component_0052",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H5",
      "C7",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) lists 'Target cell membrane' with evidence ECO:0000305 from PubMed 26352292, and the GO cross-reference (H5) assigns GO:0044218 'other organism cell membrane,' which is a child of GO:0016020 'membrane' (option A). The protein is VpAmp2.0, an antimicrobial peptide from scorpion venom gland that functions by disrupting target (microbial) membranes. Among the four options, 'membrane' is the only one consistent with the annotation. The annotation is computational/experimental (ECO:0000305 is 'curator inference based on publication'), not purely sequence-based, but it is a legitimate database annotation."
  },
  "important_caveats": [
    "The UniProt annotation 'Target cell membrane' (ECO:0000305) is curator inference from a publication, not direct experimental localization. The GO annotation GO:0044218 is IEA (inferred from electronic annotation), a lower-confidence evidence code.",
    "The option 'membrane' (GO:0016020) is a very broad term; the specific annotation is 'other organism cell membrane' (GO:0044218). The question does not distinguish between the protein's own cell membrane and a target organism's membrane, but 'membrane' is still the best fit among the given options.",
    "The primary GO annotation is GO:0005576 'extracellular region' (IEA), which is not offered as an option. The question forces a choice among four terms, and 'membrane' is the closest to the functional annotation.",
    "Reviewer-only evidence was used to verify the expected answer; the evaluated model had access only to the 77-aa sequence and the four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'membrane' is consistent with a secreted antimicrobial peptide. 'Apicoplast' is taxonomically impossible for a scorpion protein. 'Host cytoskeleton' pertains to intracellular pathogen biology, not secreted venom peptides. 'Lipid droplet' is an intracellular organelle inconsistent with a secreted cationic peptide. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0052",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) lists 'Target cell membrane' with evidence ECO:0000305 from PubMed 26352292, and the GO cross-reference (H5) assigns GO:0044218 'other organism cell membrane,' which is a child of GO:0016020 'membrane' (option A). The protein is VpAmp2.0, an antimicrobial peptide from scorpion venom gland that functions by disrupting target (microbial) membranes. Among the four options, 'membrane' is the only one consistent with the annotation. The annotation is computational/experimental (ECO:0000305 is 'curator inference based on publication'), not purely sequence-based, but it is a legitimate database annotation.",
    "evidence_ids": ["C5", "H3", "H5", "C7", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 77-aa sequence shows a hydrophobic N-terminal signal peptide (MQLRKALLVIFVAYLLVT) followed by a small, highly cationic (multiple K/R), amphipathic mature peptide with aromatic residues (W, F, Y). These are canonical hallmarks of secreted antimicrobial peptides, which function by binding and disrupting microbial membranes. This general biological knowledge allows one to select 'membrane' over the distractors: (1) 'apicoplast' is restricted to apicomplexan parasites and is irrelevant to a scorpion peptide; (2) 'host cytoskeleton' applies to intracellular pathogen interactions, not secreted venom peptides; (3) 'lipid droplet' is an intracellular organelle and its associated proteins do not display the cationic amphipathic membrane-perturbing signature seen here. Thus, recognizing the peptide class (small cationic amphipathic secreted peptide → antimicrobial → membrane-targeting) provides a concrete biological argument to distinguish the answer.",
    "missing_item_specific_fact": "None strictly required. One could argue that knowing the specific peptide is VpAmp2.0 and its experimental characterization as a membrane-disrupting antimicrobial peptide would strengthen confidence, but the sequence features and general antimicrobial peptide biology are sufficient to reach 'membrane' over the other three options.",
    "reason": "The sequence contains recognizable features of a secreted antimicrobial peptide (signal peptide, cationic amphipathic mature region). General knowledge of antimicrobial peptide mechanism (membrane disruption) combined with elimination of biologically implausible distractors (apicoplast for a scorpion, host cytoskeleton for a secreted peptide, lipid droplet for a cationic membrane-perturbing peptide) provides a defensible reasoning path to 'membrane.'"
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'membrane' is consistent with a secreted antimicrobial peptide. 'Apicoplast' is taxonomically impossible for a scorpion protein. 'Host cytoskeleton' pertains to intracellular pathogen biology, not secreted venom peptides. 'Lipid droplet' is an intracellular organelle inconsistent with a secreted cationic peptide. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt annotation 'Target cell membrane' (ECO:0000305) is curator inference from a publication, not direct experimental localization. The GO annotation GO:0044218 is IEA (inferred from electronic annotation), a lower-confidence evidence code.",
    "The option 'membrane' (GO:0016020) is a very broad term; the specific annotation is 'other organism cell membrane' (GO:0044218). The question does not distinguish between the protein's own cell membrane and a target organism's membrane, but 'membrane' is still the best fit among the given options.",
    "The primary GO annotation is GO:0005576 'extracellular region' (IEA), which is not offered as an option. The question forces a choice among four terms, and 'membrane' is the closest to the functional annotation.",
    "Reviewer-only evidence was used to verify the expected answer; the evaluated model had access only to the 77-aa sequence and the four choices."
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

**Accession:** `A0A0N7FMT9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 7. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:17.678372+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"26352292","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0451","value":"Target cell membrane"}}]}
```

Source SHA-256: `c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7FMT9.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:17.678372+00:00.  

```json
{"citation":{"authors":["Ramirez-Carreto S.","Jimenez-Vargas J.M.","Rivas-Santiago B.","Corzo G.","Possani L.D.","Becerril B.","Ortiz E."],"citationCrossReferences":[{"database":"PubMed","id":"26352292"},{"database":"DOI","id":"10.1016/j.peptides.2015.08.014"}],"citationType":"journal article","firstPage":"51","id":"26352292","journal":"Peptides","lastPage":"59","publicationDate":"2015","title":"Peptides from the scorpion Vaejovis punctatus with broad antimicrobial activity.","volume":"73"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ALG64975.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Venom gland"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","SYNTHESIS OF 24-48","MUTAGENESIS OF 45-SER--SER-47"]}
```

Source SHA-256: `c9a8d5b7e9c0099fb47d97df473e04b963da7f9c984a18fd3f64abccc0181ec9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7)  
**Locator:** `lines 12-21`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 7 / 1.  
**Retrieved:** 2026-11-02T04:24:20.060714+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:ALG64975.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], SYNTHESIS OF 24-48, AND MUTAGENESIS OF
RP   45-SER--SER-47.
RC   TISSUE=Venom gland;
RX   PubMed=26352292; DOI=10.1016/j.peptides.2015.08.014;
RA   Ramirez-Carreto S., Jimenez-Vargas J.M., Rivas-Santiago B., Corzo G.,
RA   Possani L.D., Becerril B., Ortiz E.;
RT   "Peptides from the scorpion Vaejovis punctatus with broad antimicrobial
RT   activity.";
RL   Peptides 73:51-59(2015).
```

Source SHA-256: `45530fb73901a1d169a816a490448b47f0336a2dcdddaa6707cc7913b9a6181c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7)  
**Locator:** `lines 28-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 7 / 1.  
**Retrieved:** 2026-11-02T04:24:20.060714+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:26352292}. Target
CC       cell membrane {ECO:0000305}.
```

Source SHA-256: `45530fb73901a1d169a816a490448b47f0336a2dcdddaa6707cc7913b9a6181c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7FMT9?format=txt&versions=7)  
**Locator:** `lines 42-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 7 / 1.  
**Retrieved:** 2026-11-02T04:24:20.060714+00:00.  

```text
DR   GO; GO:0044218; C:other organism cell membrane; IEA:UniProtKB-KW.
```

Source SHA-256: `45530fb73901a1d169a816a490448b47f0336a2dcdddaa6707cc7913b9a6181c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 52. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
