# GO_cellular_component_0137

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — extracellular space

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNFTKLFAIVLLAALVLLGQTEAGGLKKLGKKLEGAGKRVFKASEKALPVVVGIKAIGK

[Multiple Choices]
A. nuclear periphery
B. mitochondrial outer membrane
C. extracellular space
D. mitochondrial matrix
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

> The exact-matching UniProt record annotates the protein as secreted, and its GO annotations include extracellular localization. These support choice C, though the cited annotations do not by themselves establish direct experimental localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a long hydrophobic stretch characteristic of a secretory signal peptide. That favors entry into the secretory pathway and extracellular release over mitochondrial targeting, whose transit peptides generally lack such a continuous hydrophobic core.


**Missing item-specific fact**

> No protein-specific fact is necessary to distinguish these choices from the supplied sequence, although the exact annotation is external corroboration.


**Reason**

> The N-terminal sequence provides a concrete biological signal favoring secretion, rather than merely relying on recognition of the protein or a database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The strong N-terminal hydrophobic segment supports secretion; none of the other listed compartments is comparably supported by the sequence.


### Important caveats

- The UniProt subcellular-location annotation is evidence-coded as ECO:0000305; the supplied excerpts do not establish direct experimental localization.
- The GO annotations include computational evidence, and the exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a long hydrophobic stretch characteristic of a secretory signal peptide. That favors entry into the secretory pathway and extracellular release over mitochondrial targeting, whose transit peptides generally lack such a continuous hydrophobic core.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific fact is necessary to distinguish these choices from the supplied sequence, although the exact annotation is external corroboration.",
    "reason": "The N-terminal sequence provides a concrete biological signal favoring secretion, rather than merely relying on recognition of the protein or a database lookup."
  },
  "case_id": "GO_cellular_component_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates the protein as secreted, and its GO annotations include extracellular localization. These support choice C, though the cited annotations do not by themselves establish direct experimental localization."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation is evidence-coded as ECO:0000305; the supplied excerpts do not establish direct experimental localization.",
    "The GO annotations include computational evidence, and the exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The strong N-terminal hydrophobic segment supports secretion; none of the other listed compartments is comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates the protein as secreted, and its GO annotations include extracellular localization. These support choice C, though the cited annotations do not by themselves establish direct experimental localization.",
    "evidence_ids": ["C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a long hydrophobic stretch characteristic of a secretory signal peptide. That favors entry into the secretory pathway and extracellular release over mitochondrial targeting, whose transit peptides generally lack such a continuous hydrophobic core.",
    "missing_item_specific_fact": "No protein-specific fact is necessary to distinguish these choices from the supplied sequence, although the exact annotation is external corroboration.",
    "reason": "The N-terminal sequence provides a concrete biological signal favoring secretion, rather than merely relying on recognition of the protein or a database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The strong N-terminal hydrophobic segment supports secretion; none of the other listed compartments is comparably supported by the sequence."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation is evidence-coded as ECO:0000305; the supplied excerpts do not establish direct experimental localization.",
    "The GO annotations include computational evidence, and the exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q17NR1 (CECL_AEDAE, Aedesin, a cecropin-like antimicrobial peptide from Aedes aegypti). The UniProt entry explicitly annotates SUBCELLULAR LOCATION: Secreted (ECO:0000305, evidence from mass spectrometry identification in salivary gland). GO annotations include GO:0005576 (extracellular region, IEA:UniProtKB-SubCell) and GO:0005615 (extracellular space, IEA:TreeGrafter). The protein is a small secreted antimicrobial peptide identified by mass spectrometry in the salivary gland, with published function as an inducible antimicrobial/anti-inflammatory peptide. 'Extracellular space' is the appropriate GO cellular component for a secreted peptide.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~19 residues (MNFTKLFAIVLLAALVLLG) form a strongly hydrophobic segment with a single K and no R residues, characteristic of a classical ER-targeting signal peptide rather than a mitochondrial targeting sequence (MTS), which is typically enriched in arginines and serines/threonines in an amphipathic helix. The mature peptide (residues ~20-59) is only ~40 residues, highly cationic (K/R-rich), and amphipathic — hallmarks of a secreted antimicrobial peptide (cecropin family), not a mitochondrial or nuclear protein. Mitochondrial and nuclear proteins are generally much larger and lack this extreme cationicity in a short mature domain. The absence of a nuclear localization signal (a defined stretch of basic residues in a larger context) and the hydrophobic signal peptide pattern together argue against nuclear periphery (A), mitochondrial outer membrane (B), and mitochondrial matrix (D), leaving extracellular space (C) as the biologically consistent compartment.


**Missing item-specific fact**

> None strictly required; the sequence features (signal peptide composition, mature peptide size and cationicity) provide sufficient general biological grounds to distinguish the answer without knowing this specific protein's database annotation.


**Reason**

> A biologist familiar with signal peptide vs. MTS discrimination and antimicrobial peptide characteristics can reason from the sequence alone: the hydrophobic N-terminus lacks the arginine enrichment of an MTS, the mature peptide is too small and too cationic for a mitochondrial or nuclear protein, and its amphipathic cationic character is diagnostic of a secreted antimicrobial peptide. This constitutes a concrete biological argument grounded in the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated biologically. Nuclear periphery, mitochondrial outer membrane, and mitochondrial matrix are all intracellular compartments incompatible with a small secreted cationic peptide. Extracellular space is the only option consistent with a signal-peptide-bearing, secreted antimicrobial peptide. No ambiguity among the choices.


### Important caveats

- The GO term 'extracellular space' (GO:0005615) has empty term_ids in the supplied ontology_option_term_candidates, but the UniProt entry annotates both GO:0005576 (extracellular region) and GO:0005615 (extracellular space). The GO evidence code for the extracellular region annotation is IEA (inferred from electronic annotation via UniProtKB-SubCell), while the 'Secreted' subcellular location itself carries ECO:0000305 (curator inference from literature, specifically mass spectrometry identification in the salivary gland).
- The identity of the protein (Aedesin/cecropin-like peptide) and its secretion status were not provided in the model input; only the raw sequence was given. The reasoning argument relies on general sequence-feature interpretation rather than database lookup.
- The ontology snapshot used by the benchmark authors is unknown; the supplied GO definitions are from the current ontology.
- The sequence is a precursor (signal peptide + mature peptide); the functional mature peptide is residues ~20-59.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~19 residues (MNFTKLFAIVLLAALVLLG) form a strongly hydrophobic segment with a single K and no R residues, characteristic of a classical ER-targeting signal peptide rather than a mitochondrial targeting sequence (MTS), which is typically enriched in arginines and serines/threonines in an amphipathic helix. The mature peptide (residues ~20-59) is only ~40 residues, highly cationic (K/R-rich), and amphipathic — hallmarks of a secreted antimicrobial peptide (cecropin family), not a mitochondrial or nuclear protein. Mitochondrial and nuclear proteins are generally much larger and lack this extreme cationicity in a short mature domain. The absence of a nuclear localization signal (a defined stretch of basic residues in a larger context) and the hydrophobic signal peptide pattern together argue against nuclear periphery (A), mitochondrial outer membrane (B), and mitochondrial matrix (D), leaving extracellular space (C) as the biologically consistent compartment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; the sequence features (signal peptide composition, mature peptide size and cationicity) provide sufficient general biological grounds to distinguish the answer without knowing this specific protein's database annotation.",
    "reason": "A biologist familiar with signal peptide vs. MTS discrimination and antimicrobial peptide characteristics can reason from the sequence alone: the hydrophobic N-terminus lacks the arginine enrichment of an MTS, the mature peptide is too small and too cationic for a mitochondrial or nuclear protein, and its amphipathic cationic character is diagnostic of a secreted antimicrobial peptide. This constitutes a concrete biological argument grounded in the supplied sequence."
  },
  "case_id": "GO_cellular_component_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q17NR1 (CECL_AEDAE, Aedesin, a cecropin-like antimicrobial peptide from Aedes aegypti). The UniProt entry explicitly annotates SUBCELLULAR LOCATION: Secreted (ECO:0000305, evidence from mass spectrometry identification in salivary gland). GO annotations include GO:0005576 (extracellular region, IEA:UniProtKB-SubCell) and GO:0005615 (extracellular space, IEA:TreeGrafter). The protein is a small secreted antimicrobial peptide identified by mass spectrometry in the salivary gland, with published function as an inducible antimicrobial/anti-inflammatory peptide. 'Extracellular space' is the appropriate GO cellular component for a secreted peptide."
  },
  "important_caveats": [
    "The GO term 'extracellular space' (GO:0005615) has empty term_ids in the supplied ontology_option_term_candidates, but the UniProt entry annotates both GO:0005576 (extracellular region) and GO:0005615 (extracellular space). The GO evidence code for the extracellular region annotation is IEA (inferred from electronic annotation via UniProtKB-SubCell), while the 'Secreted' subcellular location itself carries ECO:0000305 (curator inference from literature, specifically mass spectrometry identification in the salivary gland).",
    "The identity of the protein (Aedesin/cecropin-like peptide) and its secretion status were not provided in the model input; only the raw sequence was given. The reasoning argument relies on general sequence-feature interpretation rather than database lookup.",
    "The ontology snapshot used by the benchmark authors is unknown; the supplied GO definitions are from the current ontology.",
    "The sequence is a precursor (signal peptide + mature peptide); the functional mature peptide is residues ~20-59."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated biologically. Nuclear periphery, mitochondrial outer membrane, and mitochondrial matrix are all intracellular compartments incompatible with a small secreted cationic peptide. Extracellular space is the only option consistent with a signal-peptide-bearing, secreted antimicrobial peptide. No ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q17NR1 (CECL_AEDAE, Aedesin, a cecropin-like antimicrobial peptide from Aedes aegypti). The UniProt entry explicitly annotates SUBCELLULAR LOCATION: Secreted (ECO:0000305, evidence from mass spectrometry identification in salivary gland). GO annotations include GO:0005576 (extracellular region, IEA:UniProtKB-SubCell) and GO:0005615 (extracellular space, IEA:TreeGrafter). The protein is a small secreted antimicrobial peptide identified by mass spectrometry in the salivary gland, with published function as an inducible antimicrobial/anti-inflammatory peptide. 'Extracellular space' is the appropriate GO cellular component for a secreted peptide.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "C9", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~19 residues (MNFTKLFAIVLLAALVLLG) form a strongly hydrophobic segment with a single K and no R residues, characteristic of a classical ER-targeting signal peptide rather than a mitochondrial targeting sequence (MTS), which is typically enriched in arginines and serines/threonines in an amphipathic helix. The mature peptide (residues ~20-59) is only ~40 residues, highly cationic (K/R-rich), and amphipathic — hallmarks of a secreted antimicrobial peptide (cecropin family), not a mitochondrial or nuclear protein. Mitochondrial and nuclear proteins are generally much larger and lack this extreme cationicity in a short mature domain. The absence of a nuclear localization signal (a defined stretch of basic residues in a larger context) and the hydrophobic signal peptide pattern together argue against nuclear periphery (A), mitochondrial outer membrane (B), and mitochondrial matrix (D), leaving extracellular space (C) as the biologically consistent compartment.",
    "missing_item_specific_fact": "None strictly required; the sequence features (signal peptide composition, mature peptide size and cationicity) provide sufficient general biological grounds to distinguish the answer without knowing this specific protein's database annotation.",
    "reason": "A biologist familiar with signal peptide vs. MTS discrimination and antimicrobial peptide characteristics can reason from the sequence alone: the hydrophobic N-terminus lacks the arginine enrichment of an MTS, the mature peptide is too small and too cationic for a mitochondrial or nuclear protein, and its amphipathic cationic character is diagnostic of a secreted antimicrobial peptide. This constitutes a concrete biological argument grounded in the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated biologically. Nuclear periphery, mitochondrial outer membrane, and mitochondrial matrix are all intracellular compartments incompatible with a small secreted cationic peptide. Extracellular space is the only option consistent with a signal-peptide-bearing, secreted antimicrobial peptide. No ambiguity among the choices."
  },
  "important_caveats": [
    "The GO term 'extracellular space' (GO:0005615) has empty term_ids in the supplied ontology_option_term_candidates, but the UniProt entry annotates both GO:0005576 (extracellular region) and GO:0005615 (extracellular space). The GO evidence code for the extracellular region annotation is IEA (inferred from electronic annotation via UniProtKB-SubCell), while the 'Secreted' subcellular location itself carries ECO:0000305 (curator inference from literature, specifically mass spectrometry identification in the salivary gland).",
    "The identity of the protein (Aedesin/cecropin-like peptide) and its secretion status were not provided in the model input; only the raw sequence was given. The reasoning argument relies on general sequence-feature interpretation rather than database lookup.",
    "The ontology snapshot used by the benchmark authors is unknown; the supplied GO definitions are from the current ontology.",
    "The sequence is a precursor (signal peptide + mature peptide); the functional mature peptide is residues ~20-59."
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

**Accession:** `Q17NR1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 109. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:31.121229+00:00.  

```json
"Q17NR1"
```

Source SHA-256: `3fd0a35482453f147acddf9e86c2492ad175da8533df1aa3631a5791fbf01886`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:31.121229+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30107813","source":"PubMed"}],"value":"AeaeCec4"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21249175","source":"PubMed"}],"value":"Cecropin-like peptide"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25162372","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"30107813","source":"PubMed"}],"value":"Aedesin"}}}
```

Source SHA-256: `3fd0a35482453f147acddf9e86c2492ad175da8533df1aa3631a5791fbf01886`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:31.121229+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0243","value":"Secreted"}}]}
```

Source SHA-256: `3fd0a35482453f147acddf9e86c2492ad175da8533df1aa3631a5791fbf01886`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR1.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:31.121229+00:00.  

```json
{"database":"GO","id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `3fd0a35482453f147acddf9e86c2492ad175da8533df1aa3631a5791fbf01886`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:31.121229+00:00.  

```json
{"citation":{"authors":["Luplertlop N.","Surasombatpattana P.","Patramool S.","Dumas E.","Wasinpiyamongkol L.","Saune L.","Hamel R.","Bernard E.","Sereno D.","Thomas F.","Piquemal D.","Yssel H.","Briant L.","Misse D."],"citationCrossReferences":[{"database":"PubMed","id":"21249175"},{"database":"DOI","id":"10.1371/journal.ppat.1001252"}],"citationType":"journal article","firstPage":"e1001252","id":"21249175","journal":"PLoS Pathog.","lastPage":"e1001252","publicationDate":"2011","title":"Induction of a peptide with activity against a broad spectrum of pathogens in the Aedes aegypti salivary gland, following Infection with Dengue Virus.","volume":"7"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["IDENTIFICATION BY MASS SPECTROMETRY","FUNCTION","TISSUE SPECIFICITY","INDUCTION"]}
```

Source SHA-256: `3fd0a35482453f147acddf9e86c2492ad175da8533df1aa3631a5791fbf01886`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:31.121229+00:00.  

```json
{"citation":{"authors":["Wei L.","Yang Y.","Zhou Y.","Li M.","Yang H.","Mu L.","Qian Q.","Wu J.","Xu W."],"citationCrossReferences":[{"database":"PubMed","id":"30107813"},{"database":"DOI","id":"10.1186/s13071-018-3000-8"}],"citationType":"journal article","firstPage":"470","id":"30107813","journal":"Parasit. Vectors","lastPage":"470","publicationDate":"2018","title":"Anti-inflammatory activities of Aedes aegypti cecropins and their protection against murine endotoxin shock.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `3fd0a35482453f147acddf9e86c2492ad175da8533df1aa3631a5791fbf01886`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q17NR1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:31.121229+00:00.  

```json
{"citation":{"authors":["Godreuil S.","Leban N.","Padilla A.","Hamel R.","Luplertlop N.","Chauffour A.","Vittecoq M.","Hoh F.","Thomas F.","Sougakoff W.","Lionne C.","Yssel H.","Misse D."],"citationCrossReferences":[{"database":"PubMed","id":"25162372"},{"database":"DOI","id":"10.1371/journal.pone.0105441"}],"citationType":"journal article","firstPage":"e105441","id":"25162372","journal":"PLoS ONE","lastPage":"e105441","publicationDate":"2014","title":"Aedesin: structure and antimicrobial activity against multidrug resistant bacterial strains.","volume":"9"},"evidences":[{"evidenceCode":"ECO:0007744","id":"2MMM","source":"PDB"}],"referenceNumber":4,"referencePositions":["STRUCTURE BY NMR OF 24-59","FUNCTION"]}
```

Source SHA-256: `3fd0a35482453f147acddf9e86c2492ad175da8533df1aa3631a5791fbf01886`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q17NR1?format=txt&versions=109)  
**Locator:** `lines 83-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 109 / 2.  
**Retrieved:** 2026-11-02T04:30:35.225208+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305}.
```

Source SHA-256: `5cbc7b36b1b44ebdf40c8028a2a74d007c4e4608d3cec15b73e9d39b35e6e931`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q17NR1?format=txt&versions=109)  
**Locator:** `lines 106-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 109 / 2.  
**Retrieved:** 2026-11-02T04:30:35.225208+00:00.  

```text
DR   GO; GO:0005615; C:extracellular space; IEA:TreeGrafter.
```

Source SHA-256: `5cbc7b36b1b44ebdf40c8028a2a74d007c4e4608d3cec15b73e9d39b35e6e931`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 137. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
