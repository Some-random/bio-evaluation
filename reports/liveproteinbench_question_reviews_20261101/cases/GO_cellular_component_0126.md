# GO_cellular_component_0126

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — mitochondrial outer membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRAGRVRPLRASDMKKDVRILLVGEPRVGKTSLIMSLVSEEFPEEVPPRAEEITIPADVTPERVPTHIVDYSEAEQSDEQLHQEISQANVICIVYAVNNKHSIDKVTSRWIPLINERTDKDSRLPLILVGNKSDLVEYSSMETILPIMNQYTEIETCVECSAKNLKNISELFYYAQKAVLHPTGPLYCPEEKEMKPACIKALTRIFKISDQDNDGTLNDAELNFFQRICFNTPLAPQALEDVKNVVRKHLSDGVADSGLTLRGFLFLHTLFIQRGRHETTWTVLRRFGYDDDLDLTPEYLFPLLKIPPDCTTELNHHAYLFLQSTFDKHDLDRDCALSPDELKDLFQVFPYIPWGPDVNNTVCTNESGWITYQGFLSQWTLTTYLDVQRCLEYLGYLGYSILTEQESQASAITVTRDKKIDLQKKQTQRNVFRCNVIGVKGCGKTGVLQSLLGRNLMRQKKIRDDHKSYYAINTVYVYGQEKYLLLHDISESEFLTEAEIVCDVVCLVYDVTNPKSFEYCARIFKQHFMDSRIPCLIVAAKSDLHEVKQEHSVSPTDFCRKHKMPPPQAFTCNTADAPSKDIFVKLTTMAMYPHVTQADLKSSTFWLRASFGATVFAVVGFAMYRALLKQR

[Multiple Choices]
A. nuclear envelope
B. vitelline envelope
C. mitochondrial outer membrane
D. nematocyst
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

> The sequence matches rat MIRO-1/Rhot1. UniProt annotates it at the mitochondrial outer membrane, and the matching historical entry carries the same localization annotation. The support is chiefly transferred or computationally inferred rather than direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The GTPase-rich sequence and C-terminal hydrophobic membrane anchor support a membrane-associated protein, but those features alone do not distinguish the mitochondrial outer membrane from the nuclear envelope.


**Missing item-specific fact**

> The protein-specific association of MIRO-1/Rhot1 with the mitochondrial outer membrane is needed to select C; that localization is not supplied in the question.


**Reason**

> The sequence offers clues to protein architecture and membrane association, but identifying the correct organelle requires protein-specific localization knowledge or an external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence has no general targeting feature that makes the nuclear envelope a comparably supported choice; the external sequence-matched annotation supports C.


### Important caveats

- The reviewed localization annotation is transferred from UniProtKB:Q8IXI2 (ECO:0000250), while the GO mitochondrial outer membrane annotation is marked ISS; neither excerpt establishes direct experimental localization of this rat sequence.
- The source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The GTPase-rich sequence and C-terminal hydrophobic membrane anchor support a membrane-associated protein, but those features alone do not distinguish the mitochondrial outer membrane from the nuclear envelope.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific association of MIRO-1/Rhot1 with the mitochondrial outer membrane is needed to select C; that localization is not supplied in the question.",
    "reason": "The sequence offers clues to protein architecture and membrane association, but identifying the correct organelle requires protein-specific localization knowledge or an external annotation."
  },
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches rat MIRO-1/Rhot1. UniProt annotates it at the mitochondrial outer membrane, and the matching historical entry carries the same localization annotation. The support is chiefly transferred or computationally inferred rather than direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewed localization annotation is transferred from UniProtKB:Q8IXI2 (ECO:0000250), while the GO mitochondrial outer membrane annotation is marked ISS; neither excerpt establishes direct experimental localization of this rat sequence.",
    "The source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence has no general targeting feature that makes the nuclear envelope a comparably supported choice; the external sequence-matched annotation supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches rat MIRO-1/Rhot1. UniProt annotates it at the mitochondrial outer membrane, and the matching historical entry carries the same localization annotation. The support is chiefly transferred or computationally inferred rather than direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The GTPase-rich sequence and C-terminal hydrophobic membrane anchor support a membrane-associated protein, but those features alone do not distinguish the mitochondrial outer membrane from the nuclear envelope.",
    "missing_item_specific_fact": "The protein-specific association of MIRO-1/Rhot1 with the mitochondrial outer membrane is needed to select C; that localization is not supplied in the question.",
    "reason": "The sequence offers clues to protein architecture and membrane association, but identifying the correct organelle requires protein-specific localization knowledge or an external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence has no general targeting feature that makes the nuclear envelope a comparably supported choice; the external sequence-matched annotation supports C."
  },
  "important_caveats": [
    "The reviewed localization annotation is transferred from UniProtKB:Q8IXI2 (ECO:0000250), while the GO mitochondrial outer membrane annotation is marked ISS; neither excerpt establishes direct experimental localization of this rat sequence.",
    "The source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A1L1L6 (MIRO1_RAT) annotates the subcellular location as 'Mitochondrion outer membrane' with topology 'Single-pass type IV membrane protein' (C5, H2). GO annotation GO:0005741 (mitochondrial outer membrane) is present (C8, H5). The protein is named 'Mitochondrial Rho GTPase' (C4, H1). The evidence code is ECO:0000250 / ISS:UniProtKB, indicating inference by similarity to human MIRO1 (Q8IXI2) rather than direct experimental evidence for this specific rat sequence. However, MIRO1 localization to the mitochondrial outer membrane is well-established experimentally in the human ortholog and broadly in the literature. The annotation is computational in this specific entry but rests on a well-characterized protein family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains three recognizable functional modules: (1) an N-terminal Ras-superfamily GTPase domain (GKT, NKxD, SAK, NxxD motifs), (2) two EF-hand calcium-binding domains in the middle region (DxDxDGxDG patterns), and (3) a C-terminal hydrophobic single-pass transmembrane anchor. This tripartite architecture (GTPase + EF-hands + C-terminal TM) is the hallmark of MIRO proteins, which are textbook examples of mitochondrial outer membrane proteins regulating mitochondrial transport along microtubules. The C-terminal type-IV topology (N-terminus cytoplasmic) is consistent with outer-membrane anchoring rather than inner-membrane insertion. Distractors are eliminable by domain logic: nematocyst (D) is a cnidarian stinging organelle with no GTPase/EF-hand architecture; vitelline envelope (B) is an egg-coat glycoprotein structure, not a GTPase; nuclear envelope (A) proteins carry NLS motifs, nucleoporin FG-repeats, or lamina-binding domains, none of which are present.


**Missing item-specific fact**

> None strictly required. The final step—MIRO family → mitochondrial outer membrane—is well-established cell biology, though a model unfamiliar with MIRO proteins might hesitate between 'mitochondrial membrane' options. No experimental measurement or obscure annotation beyond standard domain-to-localization inference is needed.


**Reason**

> A knowledgeable model can reason from the GTPase + EF-hand + C-terminal TM architecture to the MIRO protein family and then to mitochondrial outer membrane localization using general cell biology. The three distractors are eliminated by incompatible domain architectures and organismal context (a vertebrate GTPase cannot reside in a cnidarian nematocyst or an egg coat).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (nuclear envelope, vitelline envelope, nematocyst) are clearly incompatible with the observed GTPase/EF-hand/TM architecture. No other supplied option is defensible.


### Important caveats

- The UniProt annotation for this rat entry (A1L1L6) uses evidence code ECO:0000250 (inferred by similarity to human Q8IXI2), not direct experimental evidence for the rat protein. The human ortholog MIRO1 is experimentally well-characterized as an outer-membrane protein.
- The organism (Rattus norvegicus) is not stated in the question; the model must infer vertebrate origin from the sequence itself. This does not affect answerability because the domain architecture is diagnostic regardless.
- The reviewer-only accession and metadata were absent from the evaluated model input; the model must work from the raw sequence and choices alone.
- The GO annotation evidence type in the current snapshot is ISS (sequence similarity) while the historical snapshot (entry v147) lists ISO:RGD; both are computational inferences, not direct experiments on this rat protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains three recognizable functional modules: (1) an N-terminal Ras-superfamily GTPase domain (GKT, NKxD, SAK, NxxD motifs), (2) two EF-hand calcium-binding domains in the middle region (DxDxDGxDG patterns), and (3) a C-terminal hydrophobic single-pass transmembrane anchor. This tripartite architecture (GTPase + EF-hands + C-terminal TM) is the hallmark of MIRO proteins, which are textbook examples of mitochondrial outer membrane proteins regulating mitochondrial transport along microtubules. The C-terminal type-IV topology (N-terminus cytoplasmic) is consistent with outer-membrane anchoring rather than inner-membrane insertion. Distractors are eliminable by domain logic: nematocyst (D) is a cnidarian stinging organelle with no GTPase/EF-hand architecture; vitelline envelope (B) is an egg-coat glycoprotein structure, not a GTPase; nuclear envelope (A) proteins carry NLS motifs, nucleoporin FG-repeats, or lamina-binding domains, none of which are present.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The final step—MIRO family → mitochondrial outer membrane—is well-established cell biology, though a model unfamiliar with MIRO proteins might hesitate between 'mitochondrial membrane' options. No experimental measurement or obscure annotation beyond standard domain-to-localization inference is needed.",
    "reason": "A knowledgeable model can reason from the GTPase + EF-hand + C-terminal TM architecture to the MIRO protein family and then to mitochondrial outer membrane localization using general cell biology. The three distractors are eliminated by incompatible domain architectures and organismal context (a vertebrate GTPase cannot reside in a cnidarian nematocyst or an egg coat)."
  },
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A1L1L6 (MIRO1_RAT) annotates the subcellular location as 'Mitochondrion outer membrane' with topology 'Single-pass type IV membrane protein' (C5, H2). GO annotation GO:0005741 (mitochondrial outer membrane) is present (C8, H5). The protein is named 'Mitochondrial Rho GTPase' (C4, H1). The evidence code is ECO:0000250 / ISS:UniProtKB, indicating inference by similarity to human MIRO1 (Q8IXI2) rather than direct experimental evidence for this specific rat sequence. However, MIRO1 localization to the mitochondrial outer membrane is well-established experimentally in the human ortholog and broadly in the literature. The annotation is computational in this specific entry but rests on a well-characterized protein family."
  },
  "important_caveats": [
    "The UniProt annotation for this rat entry (A1L1L6) uses evidence code ECO:0000250 (inferred by similarity to human Q8IXI2), not direct experimental evidence for the rat protein. The human ortholog MIRO1 is experimentally well-characterized as an outer-membrane protein.",
    "The organism (Rattus norvegicus) is not stated in the question; the model must infer vertebrate origin from the sequence itself. This does not affect answerability because the domain architecture is diagnostic regardless.",
    "The reviewer-only accession and metadata were absent from the evaluated model input; the model must work from the raw sequence and choices alone.",
    "The GO annotation evidence type in the current snapshot is ISS (sequence similarity) while the historical snapshot (entry v147) lists ISO:RGD; both are computational inferences, not direct experiments on this rat protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (nuclear envelope, vitelline envelope, nematocyst) are clearly incompatible with the observed GTPase/EF-hand/TM architecture. No other supplied option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A1L1L6 (MIRO1_RAT) annotates the subcellular location as 'Mitochondrion outer membrane' with topology 'Single-pass type IV membrane protein' (C5, H2). GO annotation GO:0005741 (mitochondrial outer membrane) is present (C8, H5). The protein is named 'Mitochondrial Rho GTPase' (C4, H1). The evidence code is ECO:0000250 / ISS:UniProtKB, indicating inference by similarity to human MIRO1 (Q8IXI2) rather than direct experimental evidence for this specific rat sequence. However, MIRO1 localization to the mitochondrial outer membrane is well-established experimentally in the human ortholog and broadly in the literature. The annotation is computational in this specific entry but rests on a well-characterized protein family.",
    "evidence_ids": ["C4", "C5", "C8", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains three recognizable functional modules: (1) an N-terminal Ras-superfamily GTPase domain (GKT, NKxD, SAK, NxxD motifs), (2) two EF-hand calcium-binding domains in the middle region (DxDxDGxDG patterns), and (3) a C-terminal hydrophobic single-pass transmembrane anchor. This tripartite architecture (GTPase + EF-hands + C-terminal TM) is the hallmark of MIRO proteins, which are textbook examples of mitochondrial outer membrane proteins regulating mitochondrial transport along microtubules. The C-terminal type-IV topology (N-terminus cytoplasmic) is consistent with outer-membrane anchoring rather than inner-membrane insertion. Distractors are eliminable by domain logic: nematocyst (D) is a cnidarian stinging organelle with no GTPase/EF-hand architecture; vitelline envelope (B) is an egg-coat glycoprotein structure, not a GTPase; nuclear envelope (A) proteins carry NLS motifs, nucleoporin FG-repeats, or lamina-binding domains, none of which are present.",
    "missing_item_specific_fact": "None strictly required. The final step—MIRO family → mitochondrial outer membrane—is well-established cell biology, though a model unfamiliar with MIRO proteins might hesitate between 'mitochondrial membrane' options. No experimental measurement or obscure annotation beyond standard domain-to-localization inference is needed.",
    "reason": "A knowledgeable model can reason from the GTPase + EF-hand + C-terminal TM architecture to the MIRO protein family and then to mitochondrial outer membrane localization using general cell biology. The three distractors are eliminated by incompatible domain architectures and organismal context (a vertebrate GTPase cannot reside in a cnidarian nematocyst or an egg coat)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (nuclear envelope, vitelline envelope, nematocyst) are clearly incompatible with the observed GTPase/EF-hand/TM architecture. No other supplied option is defensible."
  },
  "important_caveats": [
    "The UniProt annotation for this rat entry (A1L1L6) uses evidence code ECO:0000250 (inferred by similarity to human Q8IXI2), not direct experimental evidence for the rat protein. The human ortholog MIRO1 is experimentally well-characterized as an outer-membrane protein.",
    "The organism (Rattus norvegicus) is not stated in the question; the model must infer vertebrate origin from the sequence itself. This does not affect answerability because the domain architecture is diagnostic regardless.",
    "The reviewer-only accession and metadata were absent from the evaluated model input; the model must work from the raw sequence and choices alone.",
    "The GO annotation evidence type in the current snapshot is ISS (sequence similarity) while the historical snapshot (entry v147) lists ISO:RGD; both are computational inferences, not direct experiments on this rat protein."
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

**Accession:** `A1L1L6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 147. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
"A1L1L6"
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"1307023","source":"RGD"}],"value":"Ras homolog gene family member T1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"value":"3.6.5.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"PIRNR037488","source":"PIRNR"}],"value":"Mitochondrial Rho GTPase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"MIRO-1"}]}}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"value":"Colocalizes with MGARP and RHOT2 at the mitochondria"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"id":"SL-0172","value":"Mitochondrion outer membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8IXI2","source":"UniProtKB"}],"id":"SL-9908","value":"Single-pass type IV membrane protein"}}]}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1L1L6.json)  
**Locator:** `/uniProtKBCrossReferences/24`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:46.803603+00:00.  

```json
{"database":"GO","id":"GO:0005741","properties":[{"key":"GoTerm","value":"C:mitochondrial outer membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `c125ef86885e5aa234ab5686ffd7e9cc9805cc651f4aa85b1cf455ff62ee7ca3`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
ID   MIRO1_RAT               Reviewed;         631 AA.
AC   A1L1L6;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   06-FEB-2007, sequence version 1.
DT   28-JAN-2026, entry version 147.
DE   RecName: Full=Mitochondrial Rho GTPase {ECO:0000255|PIRNR:PIRNR037488};
DE            Short=MIRO-1 {ECO:0000305};
DE            EC=3.6.5.- {ECO:0000250|UniProtKB:Q8IXI2};
DE   AltName: Full=Ras homolog gene family member T1 {ECO:0000312|RGD:1307023};
GN   Name=Rhot1 {ECO:0000312|RGD:1307023};
GN   Synonyms=Rnf135 {ECO:0000312|RGD:1307023};
OS   Rattus norvegicus (Rat).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Rattus.
OX   NCBI_TaxID=10116 {ECO:0000312|EMBL:AAI29124.1};
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 72-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion outer membrane
CC       {ECO:0000250|UniProtKB:Q8IXI2}; Single-pass type IV membrane protein
CC       {ECO:0000250|UniProtKB:Q8IXI2}. Note=Colocalizes with MGARP and RHOT2
CC       at the mitochondria. {ECO:0000250|UniProtKB:Q8IXI2}.
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1L1L6?format=txt&versions=147)  
**Locator:** `lines 115-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:26:49.663865+00:00.  

```text
DR   GO; GO:0005741; C:mitochondrial outer membrane; ISO:RGD.
```

Source SHA-256: `f2d4593a1952b2407eeaa23ae16f133c7086e78f4fa0cdc9464acd586d1a5a5e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 126. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
