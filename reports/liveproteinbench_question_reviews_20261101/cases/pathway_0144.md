# pathway_0144

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Cell wall degradation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGQFRFLALIVAVLCFSVALFLPTADEPDQDSYSVPLNQSVNTSQPPSSEMVPSDIRLTPLPQPKRIHYMVKVGDTLSGIFAQLGVPYSILQKILSVDLDHLQLDMIQPGEELELMMDDMGQLSRLIYHMSIVEKAIYTRENDGSFSYDFQEISGEWREILFSGEINGSFSVSARRVGLTSSQVANITQVMKDKIDFSRSLRAGDRFDILVKQQYLGEHNTGNSEIKAISFKLAKGDVSAFLAEDGRFYDRAGNSLERAFNRYPVDKAYRQITSGFNPKRKHPVTGRVVPHNGTDFATPIGAPVYSTGDGKVIVVRKHPYAGNYLVIEHNSVYKTRYLHLDKILVKKGQLVKRGQKIALAGATGRLTGPHLHFEVLVRNRPVDAMKADLPIAKSLSSNQKTSFLARVSEFDHLVQANQQEVALDET

[Multiple Choices]
A. Metabolic intermediate biosynthesis
B. ajmaline biosynthesis. .
C. Cell wall degradation
D. Protein biosynthesis
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

> The exact sequence matches the Vibrio cholerae ShyB entry, annotated as a peptidoglycan DD-endopeptidase with the pathway “Cell wall degradation; peptidoglycan degradation.” The pathway annotation is linked to a publication (ECO:0000269); this supports the key, though the excerpt alone does not independently verify the experiments.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus has a strong hydrophobic signal-peptide-like region, and the remaining sequence is consistent with a catalytic metallopeptidase, supporting an exported enzyme rather than a protein-biosynthesis component. Among the choices, cell-wall degradation is the biologically coherent pathway.


**Missing item-specific fact**

> The exact substrate specificity and ShyB pathway annotation are protein-specific facts not explicitly supplied; the sequence-based argument supports, but does not by itself experimentally establish, peptidoglycan degradation.


**Reason**

> The sequence and contrasting choices provide a meaningful biological basis for selecting C without requiring recognition of the exact database entry, although protein-specific annotation would strengthen the precise assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the exported-enzyme features and the listed alternatives, cell wall degradation is the clearly best-supported choice.


### Important caveats

- The reviewer-only evidence confirms an exact sequence match and a historical pathway annotation, but the author's exact source snapshot is unknown.
- The database annotation is linked to experimental-evidence coding and a cited study; the supplied excerpts do not include the study's full experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus has a strong hydrophobic signal-peptide-like region, and the remaining sequence is consistent with a catalytic metallopeptidase, supporting an exported enzyme rather than a protein-biosynthesis component. Among the choices, cell-wall degradation is the biologically coherent pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate specificity and ShyB pathway annotation are protein-specific facts not explicitly supplied; the sequence-based argument supports, but does not by itself experimentally establish, peptidoglycan degradation.",
    "reason": "The sequence and contrasting choices provide a meaningful biological basis for selecting C without requiring recognition of the exact database entry, although protein-specific annotation would strengthen the precise assignment."
  },
  "case_id": "pathway_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Vibrio cholerae ShyB entry, annotated as a peptidoglycan DD-endopeptidase with the pathway “Cell wall degradation; peptidoglycan degradation.” The pathway annotation is linked to a publication (ECO:0000269); this supports the key, though the excerpt alone does not independently verify the experiments."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms an exact sequence match and a historical pathway annotation, but the author's exact source snapshot is unknown.",
    "The database annotation is linked to experimental-evidence coding and a cited study; the supplied excerpts do not include the study's full experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the exported-enzyme features and the listed alternatives, cell wall degradation is the clearly best-supported choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Vibrio cholerae ShyB entry, annotated as a peptidoglycan DD-endopeptidase with the pathway “Cell wall degradation; peptidoglycan degradation.” The pathway annotation is linked to a publication (ECO:0000269); this supports the key, though the excerpt alone does not independently verify the experiments.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a strong hydrophobic signal-peptide-like region, and the remaining sequence is consistent with a catalytic metallopeptidase, supporting an exported enzyme rather than a protein-biosynthesis component. Among the choices, cell-wall degradation is the biologically coherent pathway.",
    "missing_item_specific_fact": "The exact substrate specificity and ShyB pathway annotation are protein-specific facts not explicitly supplied; the sequence-based argument supports, but does not by itself experimentally establish, peptidoglycan degradation.",
    "reason": "The sequence and contrasting choices provide a meaningful biological basis for selecting C without requiring recognition of the exact database entry, although protein-specific annotation would strengthen the precise assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the exported-enzyme features and the listed alternatives, cell wall degradation is the clearly best-supported choice."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms an exact sequence match and a historical pathway annotation, but the author's exact source snapshot is unknown.",
    "The database annotation is linked to experimental-evidence coding and a cited study; the supplied excerpts do not include the study's full experimental results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is UniProt Q9KUL5 (ShyB) from Vibrio cholerae, experimentally characterized as a Peptidoglycan DD-endopeptidase (EC 3.4.24.-). The UniProt PATHWAY annotation explicitly states 'Cell wall degradation; peptidoglycan degradation' with experimental evidence code ECO:0000269 from PubMed:30782657. Multiple independent publications (PubMed:23834664, 30782657, 18498110) and a crystal structure (PDB 2GU1) confirm its peptidoglycan-hydrolyzing activity. The sequence match is confirmed (SHA256 identical). The expected answer 'Cell wall degradation' directly corresponds to the database pathway annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could note the hydrophobic N-terminal signal peptide (MGQFRFLALIVAVLCFSVALFL...) suggesting a secreted protein, and detect zinc-binding HxH motifs (e.g., 'HPYAGNYLVIEHNSV') suggesting a metalloprotease. This weakly supports an extracellular proteolytic role. However, the specific assignment to 'cell wall degradation' (peptidoglycan hydrolysis) versus other extracellular proteolysis requires recognizing the M23/lysostaphin-type peptidase family, which is not reliably inferable from primary sequence alone without family-level annotation knowledge.


**Missing item-specific fact**

> Recognition that this specific sequence belongs to the M23 (lysostaphin-type) peptidase family, whose defining substrate is peptidoglycan cross-links, rather than being a general extracellular metalloprotease. This family assignment is the item-specific fact needed to positively identify 'cell wall degradation' as the pathway.


**Reason**

> While elimination of clearly wrong distractors (B: plant alkaloid pathway; D: ribosomal protein biosynthesis is intracellular and non-proteolytic; A: generic biosynthesis) is possible, the positive identification of peptidoglycan as the specific substrate of this zinc-metalloprotease requires knowledge of the M23 peptidase family or direct recognition of the protein. The sequence does not contain a unique, unambiguous signature that a general model could use to conclude 'cell wall degradation' rather than, say, general extracellular protein turnover (which is not an option but shows the reasoning gap).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated: B (ajmaline biosynthesis) is a plant pathway irrelevant to a bacterial protein; D (Protein biosynthesis) refers to ribosomal translation, incompatible with a secreted protease; A (Metabolic intermediate biosynthesis) is a generic biosynthetic category incompatible with a catabolic hydrolase. C is the only option involving extracellular hydrolytic activity. No genuine ambiguity among the choices.


### Important caveats

- The UniProt entry was first publicly released on 2025-04-09 (Swiss-Prot), meaning the full experimental annotation (including the PATHWAY line) was established in 2019 (PubMed:30782657). The author's data-construction date and exact source snapshot are unknown.
- The pathway annotation carries experimental evidence (ECO:0000269), not purely computational inference, strengthening the expected-answer key.
- The identity of the protein (Q9KUL5) was inferred by the reviewer from dataset metadata absent from the model input; the model only sees the raw sequence.
- Distractor B contains a formatting artifact ('ajmaline biosynthesis. .') suggesting possible data-quality issues in the question generation pipeline.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could note the hydrophobic N-terminal signal peptide (MGQFRFLALIVAVLCFSVALFL...) suggesting a secreted protein, and detect zinc-binding HxH motifs (e.g., 'HPYAGNYLVIEHNSV') suggesting a metalloprotease. This weakly supports an extracellular proteolytic role. However, the specific assignment to 'cell wall degradation' (peptidoglycan hydrolysis) versus other extracellular proteolysis requires recognizing the M23/lysostaphin-type peptidase family, which is not reliably inferable from primary sequence alone without family-level annotation knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this specific sequence belongs to the M23 (lysostaphin-type) peptidase family, whose defining substrate is peptidoglycan cross-links, rather than being a general extracellular metalloprotease. This family assignment is the item-specific fact needed to positively identify 'cell wall degradation' as the pathway.",
    "reason": "While elimination of clearly wrong distractors (B: plant alkaloid pathway; D: ribosomal protein biosynthesis is intracellular and non-proteolytic; A: generic biosynthesis) is possible, the positive identification of peptidoglycan as the specific substrate of this zinc-metalloprotease requires knowledge of the M23 peptidase family or direct recognition of the protein. The sequence does not contain a unique, unambiguous signature that a general model could use to conclude 'cell wall degradation' rather than, say, general extracellular protein turnover (which is not an option but shows the reasoning gap)."
  },
  "case_id": "pathway_0144",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The protein is UniProt Q9KUL5 (ShyB) from Vibrio cholerae, experimentally characterized as a Peptidoglycan DD-endopeptidase (EC 3.4.24.-). The UniProt PATHWAY annotation explicitly states 'Cell wall degradation; peptidoglycan degradation' with experimental evidence code ECO:0000269 from PubMed:30782657. Multiple independent publications (PubMed:23834664, 30782657, 18498110) and a crystal structure (PDB 2GU1) confirm its peptidoglycan-hydrolyzing activity. The sequence match is confirmed (SHA256 identical). The expected answer 'Cell wall degradation' directly corresponds to the database pathway annotation."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-04-09 (Swiss-Prot), meaning the full experimental annotation (including the PATHWAY line) was established in 2019 (PubMed:30782657). The author's data-construction date and exact source snapshot are unknown.",
    "The pathway annotation carries experimental evidence (ECO:0000269), not purely computational inference, strengthening the expected-answer key.",
    "The identity of the protein (Q9KUL5) was inferred by the reviewer from dataset metadata absent from the model input; the model only sees the raw sequence.",
    "Distractor B contains a formatting artifact ('ajmaline biosynthesis. .') suggesting possible data-quality issues in the question generation pipeline."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: B (ajmaline biosynthesis) is a plant pathway irrelevant to a bacterial protein; D (Protein biosynthesis) refers to ribosomal translation, incompatible with a secreted protease; A (Metabolic intermediate biosynthesis) is a generic biosynthetic category incompatible with a catabolic hydrolase. C is the only option involving extracellular hydrolytic activity. No genuine ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0144",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is UniProt Q9KUL5 (ShyB) from Vibrio cholerae, experimentally characterized as a Peptidoglycan DD-endopeptidase (EC 3.4.24.-). The UniProt PATHWAY annotation explicitly states 'Cell wall degradation; peptidoglycan degradation' with experimental evidence code ECO:0000269 from PubMed:30782657. Multiple independent publications (PubMed:23834664, 30782657, 18498110) and a crystal structure (PDB 2GU1) confirm its peptidoglycan-hydrolyzing activity. The sequence match is confirmed (SHA256 identical). The expected answer 'Cell wall degradation' directly corresponds to the database pathway annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could note the hydrophobic N-terminal signal peptide (MGQFRFLALIVAVLCFSVALFL...) suggesting a secreted protein, and detect zinc-binding HxH motifs (e.g., 'HPYAGNYLVIEHNSV') suggesting a metalloprotease. This weakly supports an extracellular proteolytic role. However, the specific assignment to 'cell wall degradation' (peptidoglycan hydrolysis) versus other extracellular proteolysis requires recognizing the M23/lysostaphin-type peptidase family, which is not reliably inferable from primary sequence alone without family-level annotation knowledge.",
    "missing_item_specific_fact": "Recognition that this specific sequence belongs to the M23 (lysostaphin-type) peptidase family, whose defining substrate is peptidoglycan cross-links, rather than being a general extracellular metalloprotease. This family assignment is the item-specific fact needed to positively identify 'cell wall degradation' as the pathway.",
    "reason": "While elimination of clearly wrong distractors (B: plant alkaloid pathway; D: ribosomal protein biosynthesis is intracellular and non-proteolytic; A: generic biosynthesis) is possible, the positive identification of peptidoglycan as the specific substrate of this zinc-metalloprotease requires knowledge of the M23 peptidase family or direct recognition of the protein. The sequence does not contain a unique, unambiguous signature that a general model could use to conclude 'cell wall degradation' rather than, say, general extracellular protein turnover (which is not an option but shows the reasoning gap)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: B (ajmaline biosynthesis) is a plant pathway irrelevant to a bacterial protein; D (Protein biosynthesis) refers to ribosomal translation, incompatible with a secreted protease; A (Metabolic intermediate biosynthesis) is a generic biosynthetic category incompatible with a catabolic hydrolase. C is the only option involving extracellular hydrolytic activity. No genuine ambiguity among the choices."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-04-09 (Swiss-Prot), meaning the full experimental annotation (including the PATHWAY line) was established in 2019 (PubMed:30782657). The author's data-construction date and exact source snapshot are unknown.",
    "The pathway annotation carries experimental evidence (ECO:0000269), not purely computational inference, strengthening the expected-answer key.",
    "The identity of the protein (Q9KUL5) was inferred by the reviewer from dataset metadata absent from the model input; the model only sees the raw sequence.",
    "Distractor B contains a formatting artifact ('ajmaline biosynthesis. .') suggesting possible data-quality issues in the question generation pipeline."
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

**Accession:** `Q9KUL5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:03.079631+00:00.  

```json
"Q9KUL5"
```

Source SHA-256: `1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:03.079631+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30782657","source":"PubMed"}],"value":"Autolysin ShyB"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18498110","source":"PubMed"}],"value":"Putative lysostaphin-type peptidase P01"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23834664","source":"PubMed"}],"value":"Sidewall hydrolase B"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30782657","source":"PubMed"}],"value":"3.4.24.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30782657","source":"PubMed"}],"value":"Peptidoglycan DD-endopeptidase ShyB"}}}
```

Source SHA-256: `1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:03.079631+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30782657","source":"PubMed"}],"value":"Cell wall degradation; peptidoglycan degradation"}]}
```

Source SHA-256: `1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:03.079631+00:00.  

```json
{"citation":{"authors":["Doerr T.","Cava F.","Lam H.","Davis B.M.","Waldor M.K."],"citationCrossReferences":[{"database":"PubMed","id":"23834664"},{"database":"DOI","id":"10.1111/mmi.12323"}],"citationType":"journal article","firstPage":"949","id":"23834664","journal":"Mol. Microbiol.","lastPage":"962","publicationDate":"2013","title":"Substrate specificity of an elongation-specific peptidoglycan endopeptidase and its implications for cell wall architecture and growth of Vibrio cholerae.","volume":"89"},"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"23834664","source":"PubMed"}],"type":"STRAIN","value":"ATCC 39315 / El Tor Inaba N16961"}],"referenceNumber":2,"referencePositions":["SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:03.079631+00:00.  

```json
{"citation":{"authors":["Murphy S.G.","Alvarez L.","Adams M.C.","Liu S.","Chappie J.S.","Cava F.","Doerr T."],"citationCrossReferences":[{"database":"PubMed","id":"30782657"},{"database":"DOI","id":"10.1128/mbio.02620-18"}],"citationType":"journal article","firstPage":"0","id":"30782657","journal":"MBio","lastPage":"0","publicationDate":"2019","title":"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc Starvation Response.","volume":"10"},"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30782657","source":"PubMed"}],"type":"STRAIN","value":"ATCC 39315 / El Tor Inaba N16961"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","PATHWAY","INDUCTION","DISRUPTION PHENOTYPE","MUTAGENESIS OF HIS-372"]}
```

Source SHA-256: `1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:03.079631+00:00.  

```json
{"citation":{"authors":["Ragumani S.","Kumaran D.","Burley S.K.","Swaminathan S."],"citationCrossReferences":[{"database":"PubMed","id":"18498110"},{"database":"DOI","id":"10.1002/prot.22095"}],"citationType":"journal article","firstPage":"1096","id":"18498110","journal":"Proteins","lastPage":"1103","publicationDate":"2008","title":"Crystal structure of a putative lysostaphin peptidase from Vibrio cholerae.","volume":"72"},"evidences":[{"evidenceCode":"ECO:0007744","id":"2GU1","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.90 ANGSTROMS) OF 63-412 IN COMPLEX WITH ZINC","COFACTOR","SUBUNIT","REACTION MECHANISM"]}
```

Source SHA-256: `1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:33:12.389220+00:00.  

```text
ID   SHYB_VIBCH              Reviewed;         426 AA.
AC   Q9KUL5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2000, sequence version 1.
DT   28-JAN-2026, entry version 122.
DE   RecName: Full=Peptidoglycan DD-endopeptidase ShyB {ECO:0000303|PubMed:30782657};
DE            EC=3.4.24.- {ECO:0000269|PubMed:30782657};
DE   AltName: Full=Autolysin ShyB {ECO:0000303|PubMed:30782657};
DE   AltName: Full=Putative lysostaphin-type peptidase P01 {ECO:0000303|PubMed:18498110};
DE   AltName: Full=Sidewall hydrolase B {ECO:0000303|PubMed:23834664};
DE   Flags: Precursor;
GN   Name=shyB {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};
GN   OrderedLocusNames=VC_0503 {ECO:0000303|PubMed:23834664,
GN   ECO:0000312|EMBL:AAF93673.1};
OS   Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Vibrionales;
OC   Vibrionaceae; Vibrio.
OX   NCBI_TaxID=243277 {ECO:0000312|EMBL:AAF93673.1, ECO:0000312|Proteomes:UP000000584};
```

Source SHA-256: `b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)  
**Locator:** `lines 33-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:33:12.389220+00:00.  

```text
RN   [2]
RP   SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.
RC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:23834664};
RX   PubMed=23834664; DOI=10.1111/mmi.12323;
RA   Doerr T., Cava F., Lam H., Davis B.M., Waldor M.K.;
RT   "Substrate specificity of an elongation-specific peptidoglycan
RT   endopeptidase and its implications for cell wall architecture and growth of
RT   Vibrio cholerae.";
RL   Mol. Microbiol. 89:949-962(2013).
```

Source SHA-256: `b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)  
**Locator:** `lines 42-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:33:12.389220+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, INDUCTION,
RP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF HIS-372.
RC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:30782657};
RX   PubMed=30782657; DOI=10.1128/mbio.02620-18;
RA   Murphy S.G., Alvarez L., Adams M.C., Liu S., Chappie J.S., Cava F.,
RA   Doerr T.;
RT   "Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc
RT   Starvation Response.";
RL   MBio 10:0-0(2019).
```

Source SHA-256: `b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)  
**Locator:** `lines 52-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:33:12.389220+00:00.  

```text
RN   [4] {ECO:0007744|PDB:2GU1}
RP   X-RAY CRYSTALLOGRAPHY (1.90 ANGSTROMS) OF 63-412 IN COMPLEX WITH ZINC,
RP   COFACTOR, SUBUNIT, AND REACTION MECHANISM.
RX   PubMed=18498110; DOI=10.1002/prot.22095;
RA   Ragumani S., Kumaran D., Burley S.K., Swaminathan S.;
RT   "Crystal structure of a putative lysostaphin peptidase from Vibrio
RT   cholerae.";
RL   Proteins 72:1096-1103(2008).
```

Source SHA-256: `b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)  
**Locator:** `lines 76-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:33:12.389220+00:00.  

```text
CC   -!- PATHWAY: Cell wall degradation; peptidoglycan degradation.
CC       {ECO:0000269|PubMed:30782657}.
```

Source SHA-256: `b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 144. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
