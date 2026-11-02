# GO_molecular_function_0109

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — delta(3)-delta(2)-enoyl-CoA isomerase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGVTTVEYRGRVAVITICNERKLNALDLHGYYELSERMREVATHDEVYVTLLTAKGRFFSAGADVSTIRDPPTTGEDDSGIADGGRRQWLQSFVAFNLNITQAFYSHPKILVVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGGASRALVQRLGVSKANEALLMSRRVPADELLQTGFVNKVFTELKGAKDDDVRFKELVLAEIDDKLGDHLVGDSLIGIKELIRRPEIDVLEGQNAREVFAGLGRFMSGVPQREFLKLASGEKRHKL

[Multiple Choices]
A. histone deacetylase binding
B. methyltransferase activity
C. peptide binding
D. delta(3)-delta(2)-enoyl-CoA isomerase activity
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

> The exact sequence matches a UniProt record annotated with option D (GO:0004165), but that annotation is computational (IEA:UniProtKB-ARBA). Experimental evidence cited for the protein instead establishes a related, more specific dienoyl-CoA isomerase reaction, not necessarily the exact activity named in D.

Citations as saved: [C1](#evidence-c1), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone offers no clear, general biological feature that distinguishes this specific CoA-isomerase function from the other choices; identifying the enzyme family would require protein-specific homology or annotation knowledge.


**Missing item-specific fact**

> The protein's identity and its GO/function annotation, or comparable protein-specific experimental characterization, are not supplied.


**Reason**

> The answer is supported by a sequence-matched database annotation, but that reviewer-only annotation was unavailable to the evaluated model. Recognizing the exact sequence or retrieving its annotation would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other option is supported by the supplied sequence. However, D's exact reaction wording is not independently established by the cited experimental evidence, which describes a related dienoyl-CoA isomerase activity.


### Important caveats

- The GO:0004165 assignment is computational, not experimental evidence.
- The experimentally described reaction is EC 5.3.3.21; it should not be conflated with the exact reaction definition of GO:0004165.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone offers no clear, general biological feature that distinguishes this specific CoA-isomerase function from the other choices; identifying the enzyme family would require protein-specific homology or annotation knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and its GO/function annotation, or comparable protein-specific experimental characterization, are not supplied.",
    "reason": "The answer is supported by a sequence-matched database annotation, but that reviewer-only annotation was unavailable to the evaluated model. Recognizing the exact sequence or retrieving its annotation would be lookup, not reasoning from the supplied input."
  },
  "case_id": "GO_molecular_function_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated with option D (GO:0004165), but that annotation is computational (IEA:UniProtKB-ARBA). Experimental evidence cited for the protein instead establishes a related, more specific dienoyl-CoA isomerase reaction, not necessarily the exact activity named in D."
  },
  "important_caveats": [
    "The GO:0004165 assignment is computational, not experimental evidence.",
    "The experimentally described reaction is EC 5.3.3.21; it should not be conflated with the exact reaction definition of GO:0004165."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other option is supported by the supplied sequence. However, D's exact reaction wording is not independently established by the cited experimental evidence, which describes a related dienoyl-CoA isomerase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated with option D (GO:0004165), but that annotation is computational (IEA:UniProtKB-ARBA). Experimental evidence cited for the protein instead establishes a related, more specific dienoyl-CoA isomerase reaction, not necessarily the exact activity named in D.",
    "evidence_ids": ["C1", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone offers no clear, general biological feature that distinguishes this specific CoA-isomerase function from the other choices; identifying the enzyme family would require protein-specific homology or annotation knowledge.",
    "missing_item_specific_fact": "The protein's identity and its GO/function annotation, or comparable protein-specific experimental characterization, are not supplied.",
    "reason": "The answer is supported by a sequence-matched database annotation, but that reviewer-only annotation was unavailable to the evaluated model. Recognizing the exact sequence or retrieving its annotation would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other option is supported by the supplied sequence. However, D's exact reaction wording is not independently established by the cited experimental evidence, which describes a related dienoyl-CoA isomerase activity."
  },
  "important_caveats": [
    "The GO:0004165 assignment is computational, not experimental evidence.",
    "The experimentally described reaction is EC 5.3.3.21; it should not be conflated with the exact reaction definition of GO:0004165."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (G4NCP4, DCI1_PYRO7) is annotated with GO:0004165 (delta(3)-delta(2)-enoyl-CoA isomerase activity) via IEA:UniProtKB-ARBA (C7/H5), and with GO:0051750 (delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity) via ISS (C8/H6). The experimentally validated function (PubMed:36774535, ECO:0000269) is conversion of 3,5-dienoyl-CoAs to 2,4-dienoyl-CoAs (EC 5.3.3.21), which is a closely related isomerase activity in the same fatty acid beta-oxidation pathway. Among the four choices, D is the only isomerase option and is in the correct functional family. The GO:0004165 annotation is computational (IEA), not experimental, but it correctly places the protein in the enoyl-CoA isomerase functional class. The more precise experimental annotation (GO:0051750) is not among the choices, making D the best available match.

Citations as saved: [C7](#evidence-c7), [C8](#evidence-c8), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal residues (…KRHKL) weakly resemble a non-canonical PTS1 signal, suggesting peroxisomal localization, which is consistent with fatty acid oxidation enzymes. The absence of recognizable Rossmann-fold/SET methyltransferase motifs argues against B, and the absence of MHC/SH3-like peptide-binding domains argues against C. However, being peroxisomal does not uniquely identify the activity as isomerase rather than dehydrogenase, hydratase, thioesterase, or other peroxisomal enzymes. Positively identifying this 280-residue sequence as an enoyl-CoA isomerase (crotonase superfamily) from sequence alone requires recognition of specific catalytic residues (e.g., the conserved His-Glu pair in the oxyanion hole) or database lookup.


**Missing item-specific fact**

> The specific catalytic residue arrangement or fold recognition that identifies this sequence as belonging to the enoyl-CoA/dienoyl-CoA isomerase family (EC 5.3.3.8/5.3.3.21) rather than another peroxisomal fatty acid oxidation enzyme. The non-canonical PTS1 signal (H-K-L) is not reliably recognizable from sequence alone.


**Reason**

> While the peroxisomal context (if the PTS1 is recognized) and absence of other domain signatures provide weak negative evidence against A, B, and C, the positive identification of isomerase activity specifically requires either recognizing crotonase-superfamily catalytic motifs in the sequence or knowing the database annotation. The 280-residue length is consistent with ECI proteins but not diagnostic. General biological knowledge narrows the space but does not uniquely resolve D without item-specific recognition.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only D is an isomerase activity in fatty acid metabolism. A (HDAC binding), B (methyltransferase), and C (peptide binding) are clearly inconsistent with a peroxisomal fatty acid oxidation enzyme. The slight mismatch between GO:0004165 (enoyl-CoA isomerase, EC 5.3.3.8) and the experimentally validated GO:0051750 (dienoyl-CoA isomerase, EC 5.3.3.21) does not create ambiguity among the provided choices since no dienoyl-CoA isomerase option is offered.


### Important caveats

- The GO:0004165 annotation supporting answer D is IEA (Inferred from Electronic Annotation via ARBA), not experimental. The experimentally validated activity (PubMed:36774535) is EC 5.3.3.21 / GO:0051750 (dienoyl-CoA isomerase), a related but distinct activity.
- The PTS1 signal in this sequence (H-K-L) is non-canonical, making peroxisomal targeting difficult to infer from sequence alone.
- The UniProt entry was first publicly released 2025-06-18; the historical entry version 50 (selected for comparison) was first released 2026-01-28. The benchmark creation date relative to this release is unknown.
- The sequence-to-accession mapping was inferred from dataset metadata (reviewer-only); the evaluated model saw only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal residues (…KRHKL) weakly resemble a non-canonical PTS1 signal, suggesting peroxisomal localization, which is consistent with fatty acid oxidation enzymes. The absence of recognizable Rossmann-fold/SET methyltransferase motifs argues against B, and the absence of MHC/SH3-like peptide-binding domains argues against C. However, being peroxisomal does not uniquely identify the activity as isomerase rather than dehydrogenase, hydratase, thioesterase, or other peroxisomal enzymes. Positively identifying this 280-residue sequence as an enoyl-CoA isomerase (crotonase superfamily) from sequence alone requires recognition of specific catalytic residues (e.g., the conserved His-Glu pair in the oxyanion hole) or database lookup.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific catalytic residue arrangement or fold recognition that identifies this sequence as belonging to the enoyl-CoA/dienoyl-CoA isomerase family (EC 5.3.3.8/5.3.3.21) rather than another peroxisomal fatty acid oxidation enzyme. The non-canonical PTS1 signal (H-K-L) is not reliably recognizable from sequence alone.",
    "reason": "While the peroxisomal context (if the PTS1 is recognized) and absence of other domain signatures provide weak negative evidence against A, B, and C, the positive identification of isomerase activity specifically requires either recognizing crotonase-superfamily catalytic motifs in the sequence or knowing the database annotation. The 280-residue length is consistent with ECI proteins but not diagnostic. General biological knowledge narrows the space but does not uniquely resolve D without item-specific recognition."
  },
  "case_id": "GO_molecular_function_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C8",
      "C4",
      "C5",
      "C6",
      "H5",
      "H6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein (G4NCP4, DCI1_PYRO7) is annotated with GO:0004165 (delta(3)-delta(2)-enoyl-CoA isomerase activity) via IEA:UniProtKB-ARBA (C7/H5), and with GO:0051750 (delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity) via ISS (C8/H6). The experimentally validated function (PubMed:36774535, ECO:0000269) is conversion of 3,5-dienoyl-CoAs to 2,4-dienoyl-CoAs (EC 5.3.3.21), which is a closely related isomerase activity in the same fatty acid beta-oxidation pathway. Among the four choices, D is the only isomerase option and is in the correct functional family. The GO:0004165 annotation is computational (IEA), not experimental, but it correctly places the protein in the enoyl-CoA isomerase functional class. The more precise experimental annotation (GO:0051750) is not among the choices, making D the best available match."
  },
  "important_caveats": [
    "The GO:0004165 annotation supporting answer D is IEA (Inferred from Electronic Annotation via ARBA), not experimental. The experimentally validated activity (PubMed:36774535) is EC 5.3.3.21 / GO:0051750 (dienoyl-CoA isomerase), a related but distinct activity.",
    "The PTS1 signal in this sequence (H-K-L) is non-canonical, making peroxisomal targeting difficult to infer from sequence alone.",
    "The UniProt entry was first publicly released 2025-06-18; the historical entry version 50 (selected for comparison) was first released 2026-01-28. The benchmark creation date relative to this release is unknown.",
    "The sequence-to-accession mapping was inferred from dataset metadata (reviewer-only); the evaluated model saw only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D is an isomerase activity in fatty acid metabolism. A (HDAC binding), B (methyltransferase), and C (peptide binding) are clearly inconsistent with a peroxisomal fatty acid oxidation enzyme. The slight mismatch between GO:0004165 (enoyl-CoA isomerase, EC 5.3.3.8) and the experimentally validated GO:0051750 (dienoyl-CoA isomerase, EC 5.3.3.21) does not create ambiguity among the provided choices since no dienoyl-CoA isomerase option is offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (G4NCP4, DCI1_PYRO7) is annotated with GO:0004165 (delta(3)-delta(2)-enoyl-CoA isomerase activity) via IEA:UniProtKB-ARBA (C7/H5), and with GO:0051750 (delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity) via ISS (C8/H6). The experimentally validated function (PubMed:36774535, ECO:0000269) is conversion of 3,5-dienoyl-CoAs to 2,4-dienoyl-CoAs (EC 5.3.3.21), which is a closely related isomerase activity in the same fatty acid beta-oxidation pathway. Among the four choices, D is the only isomerase option and is in the correct functional family. The GO:0004165 annotation is computational (IEA), not experimental, but it correctly places the protein in the enoyl-CoA isomerase functional class. The more precise experimental annotation (GO:0051750) is not among the choices, making D the best available match.",
    "evidence_ids": ["C7", "C8", "C4", "C5", "C6", "H5", "H6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal residues (…KRHKL) weakly resemble a non-canonical PTS1 signal, suggesting peroxisomal localization, which is consistent with fatty acid oxidation enzymes. The absence of recognizable Rossmann-fold/SET methyltransferase motifs argues against B, and the absence of MHC/SH3-like peptide-binding domains argues against C. However, being peroxisomal does not uniquely identify the activity as isomerase rather than dehydrogenase, hydratase, thioesterase, or other peroxisomal enzymes. Positively identifying this 280-residue sequence as an enoyl-CoA isomerase (crotonase superfamily) from sequence alone requires recognition of specific catalytic residues (e.g., the conserved His-Glu pair in the oxyanion hole) or database lookup.",
    "missing_item_specific_fact": "The specific catalytic residue arrangement or fold recognition that identifies this sequence as belonging to the enoyl-CoA/dienoyl-CoA isomerase family (EC 5.3.3.8/5.3.3.21) rather than another peroxisomal fatty acid oxidation enzyme. The non-canonical PTS1 signal (H-K-L) is not reliably recognizable from sequence alone.",
    "reason": "While the peroxisomal context (if the PTS1 is recognized) and absence of other domain signatures provide weak negative evidence against A, B, and C, the positive identification of isomerase activity specifically requires either recognizing crotonase-superfamily catalytic motifs in the sequence or knowing the database annotation. The 280-residue length is consistent with ECI proteins but not diagnostic. General biological knowledge narrows the space but does not uniquely resolve D without item-specific recognition."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D is an isomerase activity in fatty acid metabolism. A (HDAC binding), B (methyltransferase), and C (peptide binding) are clearly inconsistent with a peroxisomal fatty acid oxidation enzyme. The slight mismatch between GO:0004165 (enoyl-CoA isomerase, EC 5.3.3.8) and the experimentally validated GO:0051750 (dienoyl-CoA isomerase, EC 5.3.3.21) does not create ambiguity among the provided choices since no dienoyl-CoA isomerase option is offered."
  },
  "important_caveats": [
    "The GO:0004165 annotation supporting answer D is IEA (Inferred from Electronic Annotation via ARBA), not experimental. The experimentally validated activity (PubMed:36774535) is EC 5.3.3.21 / GO:0051750 (dienoyl-CoA isomerase), a related but distinct activity.",
    "The PTS1 signal in this sequence (H-K-L) is non-canonical, making peroxisomal targeting difficult to infer from sequence alone.",
    "The UniProt entry was first publicly released 2025-06-18; the historical entry version 50 (selected for comparison) was first released 2026-01-28. The benchmark creation date relative to this release is unknown.",
    "The sequence-to-accession mapping was inferred from dataset metadata (reviewer-only); the evaluated model saw only the raw sequence."
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

**Accession:** `G4NCP4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 50. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
"G4NCP4"
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"value":"Peroxisomal di-isomerase DCI1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"36774535","source":"PubMed"}],"value":"5.3.3.21"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36774535","source":"PubMed"}],"value":"Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase"}}}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36774535","source":"PubMed"}],"value":"Peroxisomal di-isomerase that is involved in fatty acid metabolism enzyme by converting 3,5-dienoyl-CoAs to the corresponding 2,4-dienoyl-CoAs (PubMed:36774535). Involved in fatty acid beta-oxidation, which is important for lipid droplets degradation and infectious growth (PubMed:36774535)"}]}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:45241"}}],"reaction":{"ecNumber":"5.3.3.21","evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"name":"a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:45240"},{"database":"ChEBI","id":"CHEBI:85110"},{"database":"ChEBI","id":"CHEBI:85111"}]}}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"database":"GO","id":"GO:0004165","properties":[{"key":"GoTerm","value":"F:delta(3)-delta(2)-enoyl-CoA isomerase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-ARBA"}]}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/uniProtKBCrossReferences/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"database":"GO","id":"GO:0051750","properties":[{"key":"GoTerm","value":"F:delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 36-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
CC   -!- FUNCTION: Peroxisomal di-isomerase that is involved in fatty acid
CC       metabolism enzyme by converting 3,5-dienoyl-CoAs to the corresponding
CC       2,4-dienoyl-CoAs (PubMed:36774535). Involved in fatty acid beta-
CC       oxidation, which is important for lipid droplets degradation and
CC       infectious growth (PubMed:36774535). {ECO:0000269|PubMed:36774535}.
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 41-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA;
CC         Xref=Rhea:RHEA:45240, ChEBI:CHEBI:85110, ChEBI:CHEBI:85111;
CC         EC=5.3.3.21; Evidence={ECO:0000250|UniProtKB:Q08558};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:45241;
CC         Evidence={ECO:0000250|UniProtKB:Q08558};
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 90-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
DR   GO; GO:0004165; F:delta(3)-delta(2)-enoyl-CoA isomerase activity; IEA:UniProtKB-ARBA.
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 91-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
DR   GO; GO:0051750; F:delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 36710-36795`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004165
name: delta(3)-delta(2)-enoyl-CoA isomerase activity
namespace: molecular_function
alt_id: GO:0008461
def: "Catalysis of the reactions: a (3Z)-enoyl-CoA = a 4-saturated (2E)-enoyl-CoA or a (3E)-enoyl-CoA = a 4-saturated (2E)-enoyl-CoA." [RHEA:45900]
synonym: "3,2-trans-enoyl-CoA isomerase activity" RELATED [EC:5.3.3.8]
synonym: "acetylene-allene isomerase activity" RELATED [EC:5.3.3.8]
synonym: "delta(3),delta(2)-enoyl-CoA isomerase activity" RELATED [EC:5.3.3.8]
synonym: "delta(3)-cis-delta(2)-trans-enoyl-CoA isomerase activity" RELATED [EC:5.3.3.8]
synonym: "delta3,delta2-enoyl-CoA isomerase activity" RELATED [EC:5.3.3.8]
synonym: "delta3-cis-delta2-trans-enoyl-CoA isomerase" EXACT [EC:5.3.3.8]
synonym: "delta3-delta2 enoyl-CoA isomerase activity" EXACT []
synonym: "dodecenoyl-CoA (3Z)-(2E)-isomerase activity" NARROW [EC:5.3.3.8]
synonym: "dodecenoyl-CoA D-isomerase activity" NARROW []
synonym: "dodecenoyl-CoA delta-isomerase activity" NARROW []
synonym: "dodecenoyl-CoA delta3-cis-delta2-trans-isomerase activity" NARROW [EC:5.3.3.8]
synonym: "dodecenoyl-CoA isomerase activity" RELATED [EC:5.3.3.8]
xref: EC:5.3.3.8
xref: MetaCyc:ENOYL-COA-DELTA-ISOM-RXN
xref: MetaCyc:RXN-7836
xref: MetaCyc:RXN-7931
xref: Reactome:R-HSA-109338 "Isomerization of cis,cis-3,6-Dodecadienoyl-CoA to form trans,cis-Lauro-2,6-dienoyl-CoA"
xref: Reactome:R-HSA-6809808 "ECI2 isomerizes 3Z-enoyl-CoA to 2E-enoyl-CoA"
xref: RHEA:23716
xref: RHEA:29847
xref: RHEA:45228
xref: RHEA:45736
xref: RHEA:45748
xref: RHEA:45752
xref: RHEA:45900
xref: RHEA:46044
xref: RHEA:46068
xref: RHEA:47464
xref: RHEA:47476
xref: RHEA:49852
xref: RHEA:49932
xref: RHEA:77195
xref: RHEA:83231
xref: RHEA:84219
xref: RHEA:84487
xref: RHEA:84491
xref: RHEA:84495
xref: RHEA:84503
xref: RHEA:84547
xref: RHEA:84555
xref: RHEA:84559
xref: RHEA:84563
xref: RHEA:84783
xref: RHEA:84843
xref: RHEA:84851
xref: RHEA:84855
is_a: GO:0016863 ! intramolecular oxidoreductase activity, transposing C=C bonds
property_value: skos:exactMatch EC:5.3.3.8
property_value: skos:exactMatch RHEA:45900
property_value: skos:narrowMatch MetaCyc:ENOYL-COA-DELTA-ISOM-RXN
property_value: skos:narrowMatch MetaCyc:RXN-7836
property_value: skos:narrowMatch MetaCyc:RXN-7931
property_value: skos:narrowMatch RHEA:23716
property_value: skos:narrowMatch RHEA:29847
property_value: skos:narrowMatch RHEA:45228
property_value: skos:narrowMatch RHEA:45736
property_value: skos:narrowMatch RHEA:45748
property_value: skos:narrowMatch RHEA:45752
property_value: skos:narrowMatch RHEA:46044
property_value: skos:narrowMatch RHEA:46068
property_value: skos:narrowMatch RHEA:47464
property_value: skos:narrowMatch RHEA:47476
property_value: skos:narrowMatch RHEA:49852
property_value: skos:narrowMatch RHEA:49932
property_value: skos:narrowMatch RHEA:77195
property_value: skos:narrowMatch RHEA:83231
property_value: skos:narrowMatch RHEA:84219
property_value: skos:narrowMatch RHEA:84487
property_value: skos:narrowMatch RHEA:84491
property_value: skos:narrowMatch RHEA:84495
property_value: skos:narrowMatch RHEA:84503
property_value: skos:narrowMatch RHEA:84547
property_value: skos:narrowMatch RHEA:84555
property_value: skos:narrowMatch RHEA:84559
property_value: skos:narrowMatch RHEA:84563
property_value: skos:narrowMatch RHEA:84783
property_value: skos:narrowMatch RHEA:84843
property_value: skos:narrowMatch RHEA:84851
property_value: skos:narrowMatch RHEA:84855

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
