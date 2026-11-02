# GO_cellular_component_0081

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — mitochondrion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLRYRQVVGLLQRRNFSAGATSNGSGSSGGDKSGEDLHPIRRTLRLLGNDMRKVKEFFVPKEPETEKVPIPTQSQFHFSGERDKSKEATVPDDFQTHCDVLIIGGGGVGSSIAYWLKEKARDGLNVVVVEKDDTYAQSATRVSVGGLCQQFSLPENIQMSLFAADFLRSARKHFGEEVPLQFTPHGHLMLAGEEHAESLKRSSQLQNELGARNELLTADRLTARFPWLNTKGIALGCLGLEKEGWFNPLALLSNFRRSASGYGAHFISGQVVDFEFKSQTDISVVTDLGSNEGAYTGLEKAVIQLPDGTRRTCKFALCVISAGASSEQIARLARIGVGPGILRVPLPINARKRYMYAINSQAQSAPGMNMPMTIDPSGIFIRRDGLGGNYICVQDSTEEYNSAMIDPQYFAQHIRPHLYNRIPVLGEAQVVDSWAGCYDHNVYDENGILGAHPYYNNLYLATGFSGHGVQQSLAVGRAISELIMDGQFRTIDLSRLSFDRLIVDQPMFELNNVLS

[Multiple Choices]
A. T=4 icosahedral viral capsid
B. H3 histone acetyltransferase complex
C. mitochondrion
D. perikaryon
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

> The exact sequence matches Drosophila dFOXRED1. Its UniProt record carries a mitochondrion annotation with IDA:FlyBase evidence, supporting choice C; the inner-membrane annotation is separately transferred by similarity and should not be mistaken for direct evidence.

Citations as saved: [C4](#evidence-c4), [C8](#evidence-c8), [H6](#evidence-h6), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus is rich in arginine and lacks acidic residues across the initial stretch, a plausible mitochondrial targeting presequence. That provides a sequence-based reason to favor mitochondrion over the viral capsid, histone acetyltransferase complex, or neuron-specific perikaryon choices.


**Missing item-specific fact**

> The prompt does not supply experimental localization or the protein's database annotation; those would establish this particular protein's location more directly, but are not required to distinguish the options by the targeting-signal inference.


**Reason**

> A recognizable general targeting-signal pattern gives meaningful grounds for choice C. This is an inference rather than proof of localization, and the reviewer-only protein-specific annotation supports the key but is not information supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options ask for a primary compartment and the mitochondrial-targeting inference favors mitochondrion. The broader cytoplasmic context of mitochondria does not make the specialized alternatives equally defensible.


### Important caveats

- The historical record's mitochondrion annotation is labeled IDA:FlyBase, but the cited primary study was not independently reviewed here.
- The inner mitochondrial membrane annotation is supported by similarity transfer, not the same direct-evidence annotation as mitochondrion.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus is rich in arginine and lacks acidic residues across the initial stretch, a plausible mitochondrial targeting presequence. That provides a sequence-based reason to favor mitochondrion over the viral capsid, histone acetyltransferase complex, or neuron-specific perikaryon choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The prompt does not supply experimental localization or the protein's database annotation; those would establish this particular protein's location more directly, but are not required to distinguish the options by the targeting-signal inference.",
    "reason": "A recognizable general targeting-signal pattern gives meaningful grounds for choice C. This is an inference rather than proof of localization, and the reviewer-only protein-specific annotation supports the key but is not information supplied to the evaluated model."
  },
  "case_id": "GO_cellular_component_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C8",
      "H6",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches Drosophila dFOXRED1. Its UniProt record carries a mitochondrion annotation with IDA:FlyBase evidence, supporting choice C; the inner-membrane annotation is separately transferred by similarity and should not be mistaken for direct evidence."
  },
  "important_caveats": [
    "The historical record's mitochondrion annotation is labeled IDA:FlyBase, but the cited primary study was not independently reviewed here.",
    "The inner mitochondrial membrane annotation is supported by similarity transfer, not the same direct-evidence annotation as mitochondrion."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options ask for a primary compartment and the mitochondrial-targeting inference favors mitochondrion. The broader cytoplasmic context of mitochondria does not make the specialized alternatives equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches Drosophila dFOXRED1. Its UniProt record carries a mitochondrion annotation with IDA:FlyBase evidence, supporting choice C; the inner-membrane annotation is separately transferred by similarity and should not be mistaken for direct evidence.",
    "evidence_ids": ["C4", "C8", "H6", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus is rich in arginine and lacks acidic residues across the initial stretch, a plausible mitochondrial targeting presequence. That provides a sequence-based reason to favor mitochondrion over the viral capsid, histone acetyltransferase complex, or neuron-specific perikaryon choices.",
    "missing_item_specific_fact": "The prompt does not supply experimental localization or the protein's database annotation; those would establish this particular protein's location more directly, but are not required to distinguish the options by the targeting-signal inference.",
    "reason": "A recognizable general targeting-signal pattern gives meaningful grounds for choice C. This is an inference rather than proof of localization, and the reviewer-only protein-specific annotation supports the key but is not information supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options ask for a primary compartment and the mitochondrial-targeting inference favors mitochondrion. The broader cytoplasmic context of mitochondria does not make the specialized alternatives equally defensible."
  },
  "important_caveats": [
    "The historical record's mitochondrion annotation is labeled IDA:FlyBase, but the cited primary study was not independently reviewed here.",
    "The inner mitochondrial membrane annotation is supported by similarity transfer, not the same direct-evidence annotation as mitochondrion."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9VJ10 (FXRD1_DROME, dFOXRED1) is annotated with GO:0005739 (mitochondrion) with IDA:FlyBase evidence (direct assay, PMID:34386730), and the subcellular location comment specifies 'Mitochondrion inner membrane' (ECO:0000250, inferred from human FOXRED1 Q96CU9). The GO:0005743 (mitochondrial inner membrane) annotation is part_of GO:0005739 (mitochondrion) via the ontology path. The 2021 reference paper confirms interaction with mitochondrial complex I. The expected answer 'mitochondrion' is the correct parent term encompassing the specific inner-membrane localization.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H5](#evidence-h5), [H6](#evidence-h6), [GO1](#evidence-go1), [GO3](#evidence-go3), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear FAD-binding Rossmann fold motif ('GGGGVGSS' at approximately residues 130-137), identifying the protein as an FAD-dependent oxidoreductase. FAD-dependent oxidoreductases (complex I flavoproteins, succinate dehydrogenase, etc.) are predominantly mitochondrial enzymes. The three distractors are incompatible with this domain architecture: (A) a viral capsid would not contain a Rossmann-fold FAD-binding domain; (B) a histone acetyltransferase complex component would not be an FAD-dependent oxidoreductase; (D) perikaryon is a neuronal cell-body term irrelevant to a flavoprotein. Additionally, the N-terminal region contains clusters of basic residues (R, K) consistent with a mitochondrial targeting signal, and the overall ~515 AA length with a hydrophobic segment is consistent with a single-pass mitochondrial membrane protein. General knowledge that FAD-dependent oxidoreductases are commonly mitochondrial allows meaningful elimination of the other options.


**Missing item-specific fact**

> None strictly required. Precise identification as FOXRED1 and confirmation of inner-membrane topology would require database lookup, but the question asks for the primary compartment among four options, and the FAD-binding domain plus elimination of incompatible distractors provides sufficient reasoning grounds.


**Reason**

> The visible Rossmann-fold FAD-binding motif and the biological association of flavoprotein oxidoreductases with mitochondria, combined with the clear incompatibility of the other three options (viral capsid, HAT complex, perikaryon) with an FAD-dependent oxidoreductase, provide concrete reasoning to select 'mitochondrion' without memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein's FAD-binding oxidoreductase domain, membrane-protein characteristics, and ~515 AA length are incompatible with a viral capsid (A), a histone acetyltransferase complex (B), or a perikaryon (D). Only 'mitochondrion' (C) is consistent with the domain architecture. The broader 'cytoplasm' GO annotation (IBA) does not appear as an option and is a parent term of mitochondrion in any case.


### Important caveats

- The UniProt subcellular location annotation (mitochondrial inner membrane) is ECO:0000250 (inferred by similarity from human FOXRED1), not direct experimental evidence for the Drosophila protein itself. However, the GO:0005739 mitochondrion annotation carries IDA:FlyBase (direct assay) evidence.
- The FAD-binding Rossmann fold is visible in the sequence, but flavoproteins are not exclusively mitochondrial; the reasoning relies on probabilistic association plus elimination of clearly incompatible distractors.
- The identity of the protein as Q9VJ10/dFOXRED1 was inferred by the reviewer from dataset metadata; the evaluated model receives only the raw sequence and four options.
- The ontology snapshot used by the benchmark authors may differ from the current GO release, but the mitochondrion term (GO:0005739) and its hierarchy are stable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear FAD-binding Rossmann fold motif ('GGGGVGSS' at approximately residues 130-137), identifying the protein as an FAD-dependent oxidoreductase. FAD-dependent oxidoreductases (complex I flavoproteins, succinate dehydrogenase, etc.) are predominantly mitochondrial enzymes. The three distractors are incompatible with this domain architecture: (A) a viral capsid would not contain a Rossmann-fold FAD-binding domain; (B) a histone acetyltransferase complex component would not be an FAD-dependent oxidoreductase; (D) perikaryon is a neuronal cell-body term irrelevant to a flavoprotein. Additionally, the N-terminal region contains clusters of basic residues (R, K) consistent with a mitochondrial targeting signal, and the overall ~515 AA length with a hydrophobic segment is consistent with a single-pass mitochondrial membrane protein. General knowledge that FAD-dependent oxidoreductases are commonly mitochondrial allows meaningful elimination of the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Precise identification as FOXRED1 and confirmation of inner-membrane topology would require database lookup, but the question asks for the primary compartment among four options, and the FAD-binding domain plus elimination of incompatible distractors provides sufficient reasoning grounds.",
    "reason": "The visible Rossmann-fold FAD-binding motif and the biological association of flavoprotein oxidoreductases with mitochondria, combined with the clear incompatibility of the other three options (viral capsid, HAT complex, perikaryon) with an FAD-dependent oxidoreductase, provide concrete reasoning to select 'mitochondrion' without memorizing the specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C8",
      "C9",
      "H3",
      "H5",
      "H6",
      "GO1",
      "GO3",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9VJ10 (FXRD1_DROME, dFOXRED1) is annotated with GO:0005739 (mitochondrion) with IDA:FlyBase evidence (direct assay, PMID:34386730), and the subcellular location comment specifies 'Mitochondrion inner membrane' (ECO:0000250, inferred from human FOXRED1 Q96CU9). The GO:0005743 (mitochondrial inner membrane) annotation is part_of GO:0005739 (mitochondrion) via the ontology path. The 2021 reference paper confirms interaction with mitochondrial complex I. The expected answer 'mitochondrion' is the correct parent term encompassing the specific inner-membrane localization."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation (mitochondrial inner membrane) is ECO:0000250 (inferred by similarity from human FOXRED1), not direct experimental evidence for the Drosophila protein itself. However, the GO:0005739 mitochondrion annotation carries IDA:FlyBase (direct assay) evidence.",
    "The FAD-binding Rossmann fold is visible in the sequence, but flavoproteins are not exclusively mitochondrial; the reasoning relies on probabilistic association plus elimination of clearly incompatible distractors.",
    "The identity of the protein as Q9VJ10/dFOXRED1 was inferred by the reviewer from dataset metadata; the evaluated model receives only the raw sequence and four options.",
    "The ontology snapshot used by the benchmark authors may differ from the current GO release, but the mitochondrion term (GO:0005739) and its hierarchy are stable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein's FAD-binding oxidoreductase domain, membrane-protein characteristics, and ~515 AA length are incompatible with a viral capsid (A), a histone acetyltransferase complex (B), or a perikaryon (D). Only 'mitochondrion' (C) is consistent with the domain architecture. The broader 'cytoplasm' GO annotation (IBA) does not appear as an option and is a parent term of mitochondrion in any case."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9VJ10 (FXRD1_DROME, dFOXRED1) is annotated with GO:0005739 (mitochondrion) with IDA:FlyBase evidence (direct assay, PMID:34386730), and the subcellular location comment specifies 'Mitochondrion inner membrane' (ECO:0000250, inferred from human FOXRED1 Q96CU9). The GO:0005743 (mitochondrial inner membrane) annotation is part_of GO:0005739 (mitochondrion) via the ontology path. The 2021 reference paper confirms interaction with mitochondrial complex I. The expected answer 'mitochondrion' is the correct parent term encompassing the specific inner-membrane localization.",
    "evidence_ids": ["C5", "C7", "C8", "C9", "H3", "H5", "H6", "GO1", "GO3", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear FAD-binding Rossmann fold motif ('GGGGVGSS' at approximately residues 130-137), identifying the protein as an FAD-dependent oxidoreductase. FAD-dependent oxidoreductases (complex I flavoproteins, succinate dehydrogenase, etc.) are predominantly mitochondrial enzymes. The three distractors are incompatible with this domain architecture: (A) a viral capsid would not contain a Rossmann-fold FAD-binding domain; (B) a histone acetyltransferase complex component would not be an FAD-dependent oxidoreductase; (D) perikaryon is a neuronal cell-body term irrelevant to a flavoprotein. Additionally, the N-terminal region contains clusters of basic residues (R, K) consistent with a mitochondrial targeting signal, and the overall ~515 AA length with a hydrophobic segment is consistent with a single-pass mitochondrial membrane protein. General knowledge that FAD-dependent oxidoreductases are commonly mitochondrial allows meaningful elimination of the other options.",
    "missing_item_specific_fact": "None strictly required. Precise identification as FOXRED1 and confirmation of inner-membrane topology would require database lookup, but the question asks for the primary compartment among four options, and the FAD-binding domain plus elimination of incompatible distractors provides sufficient reasoning grounds.",
    "reason": "The visible Rossmann-fold FAD-binding motif and the biological association of flavoprotein oxidoreductases with mitochondria, combined with the clear incompatibility of the other three options (viral capsid, HAT complex, perikaryon) with an FAD-dependent oxidoreductase, provide concrete reasoning to select 'mitochondrion' without memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein's FAD-binding oxidoreductase domain, membrane-protein characteristics, and ~515 AA length are incompatible with a viral capsid (A), a histone acetyltransferase complex (B), or a perikaryon (D). Only 'mitochondrion' (C) is consistent with the domain architecture. The broader 'cytoplasm' GO annotation (IBA) does not appear as an option and is a parent term of mitochondrion in any case."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation (mitochondrial inner membrane) is ECO:0000250 (inferred by similarity from human FOXRED1), not direct experimental evidence for the Drosophila protein itself. However, the GO:0005739 mitochondrion annotation carries IDA:FlyBase (direct assay) evidence.",
    "The FAD-binding Rossmann fold is visible in the sequence, but flavoproteins are not exclusively mitochondrial; the reasoning relies on probabilistic association plus elimination of clearly incompatible distractors.",
    "The identity of the protein as Q9VJ10/dFOXRED1 was inferred by the reviewer from dataset metadata; the evaluated model receives only the raw sequence and four options.",
    "The ontology snapshot used by the benchmark authors may differ from the current GO release, but the mitochondrion term (GO:0005739) and its hierarchy are stable."
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

**Accession:** `Q9VJ10` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 178. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0002021","source":"FlyBase"}],"value":"Protein lethal (2) 37Bb"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34386730","source":"PubMed"}],"value":"FAD-dependent oxidoreductase domain-containing protein 1 homolog"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34386730","source":"PubMed"}],"value":"dFOXRED1"}]}}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q96CU9","source":"UniProtKB"}],"id":"SL-0168","value":"Mitochondrion inner membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9904","value":"Single-pass membrane protein"}}]}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/uniProtKBCrossReferences/27`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"database":"GO","id":"GO:0005743","properties":[{"key":"GoTerm","value":"C:mitochondrial inner membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/uniProtKBCrossReferences/28`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"34386730","source":"PubMed"}],"id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"citation":{"authors":["Murari A.","Rhooms S.K.","Garcia C.","Liu T.","Li H.","Mishra B.","Deshong C.","Owusu-Ansah E."],"citationCrossReferences":[{"database":"PubMed","id":"34386730"},{"database":"DOI","id":"10.1016/j.isci.2021.102869"}],"citationType":"journal article","firstPage":"102869","id":"34386730","journal":"IScience","lastPage":"102869","publicationDate":"2021","title":"Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in mitochondrial complex I biogenesis.","volume":"24"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","INTERACTION WITH COMPLEX 1"]}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)  
**Locator:** `lines 96-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:33:26.250109+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion inner membrane
CC       {ECO:0000250|UniProtKB:Q96CU9}; Single-pass membrane protein
CC       {ECO:0000255}.
CC   ---------------------------------------------------------------------------
CC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms
CC   Distributed under the Creative Commons Attribution (CC BY 4.0) License
CC   ---------------------------------------------------------------------------
```

Source SHA-256: `4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)  
**Locator:** `lines 129-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:33:26.250109+00:00.  

```text
DR   GO; GO:0005743; C:mitochondrial inner membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)  
**Locator:** `lines 130-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:33:26.250109+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IDA:FlyBase.
```

Source SHA-256: `4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58975-58998`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005739
name: mitochondrion
namespace: cellular_component
def: "A semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration." [GOC:giardia, ISBN:0198506732]
comment: Some anaerobic or microaerophilic organisms (e.g. Entamoeba histolytica, Giardia intestinalis and several Microsporidia species) do not have mitochondria, and contain mitochondrion-related organelles (MROs) instead, called mitosomes or hydrogenosomes, very likely derived from mitochondria. To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "mitochondria" EXACT []
xref: NIF_Subcellular:sao1860313010
xref: Wikipedia:Mitochondrion
is_a: GO:0043231 ! intracellular membrane-bounded organelle
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59031-59043`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005743
name: mitochondrial inner membrane
namespace: cellular_component
def: "The inner, i.e. lumen-facing, lipid bilayer of the mitochondrial envelope. It is highly folded to form cristae." [GOC:ai]
synonym: "inner mitochondrial membrane" EXACT []
synonym: "inner mitochondrion membrane" EXACT []
synonym: "mitochondrion inner membrane" EXACT []
xref: NIF_Subcellular:sao1371347282
xref: Wikipedia:Inner_mitochondrial_membrane
is_a: GO:0019866 ! organelle inner membrane
is_a: GO:0031966 ! mitochondrial membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 181484-181492`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031966
name: mitochondrial membrane
namespace: cellular_component
def: "Either of the lipid bilayers that surround the mitochondrion and form the mitochondrial envelope." [GOC:mah, NIF_Subcellular:sao1045389829]
xref: NIF_Subcellular:sao1045389829
is_a: GO:0031090 ! organelle membrane
relationship: part_of GO:0005740 ! mitochondrial envelope

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
