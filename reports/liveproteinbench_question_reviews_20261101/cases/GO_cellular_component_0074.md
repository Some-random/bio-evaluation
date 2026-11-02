# GO_cellular_component_0074

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — mitochondrion

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQPEEPLIRVTDLPAPNSGHIRVLELNRPKARNAISRALLASLREEVHSIARQYDAQTGEEIPTPSWNKRFGGIAGDSEKGPTRALVLASAVESSFCAGADLKERRGFTQEETNEFLANLRSTFAALDALPIPTISAISSRALGGGLELALCTHFRVLTSNAIVSLPETRLGIIPGAGGTHRLPRLIGLGRARDMIVTGRAVSGAEAYFLGLADRLVEVLPPDEQEAADTTDKDAALLSAAREAALTEAVRLASQICEGGPIGIRAALQAVQAPSQETENKMYERVIGTEDRNEALKAFAEKRKPVFKGR

[Multiple Choices]
A. heterotrimeric G-protein complex
B. neuronal cell body
C. host cell plasma membrane
D. mitochondrion
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

> The exact sequence matches the UniProt record, which reports mitochondrial localization with experimental evidence (ECO:0000269) and an experimental GO annotation. The cited primary study is the source of that annotation, although it was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus is strongly enriched in arginine and lacks acidic residues over an extended segment, a pattern compatible with a mitochondrial targeting presequence. That provides a concrete reason to favor mitochondrion over the listed neuronal, host-membrane, and G-protein-complex options.


**Missing item-specific fact**

> The experimentally established localization and the protein's identity are not supplied; those would require protein-specific lookup to confirm rather than infer.


**Reason**

> The sequence offers a biologically meaningful targeting-signal clue for the broad compartment choice, even though that clue is not itself experimental proof.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The N-terminal targeting-signal pattern supports mitochondrion among the listed choices; the other options do not have comparable sequence-based support.


### Important caveats

- The annotation evidence is reviewer-only and was not available to the evaluated model.
- The N-terminal sequence pattern supports a prediction but does not independently establish localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus is strongly enriched in arginine and lacks acidic residues over an extended segment, a pattern compatible with a mitochondrial targeting presequence. That provides a concrete reason to favor mitochondrion over the listed neuronal, host-membrane, and G-protein-complex options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The experimentally established localization and the protein's identity are not supplied; those would require protein-specific lookup to confirm rather than infer.",
    "reason": "The sequence offers a biologically meaningful targeting-signal clue for the broad compartment choice, even though that clue is not itself experimental proof."
  },
  "case_id": "GO_cellular_component_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, which reports mitochondrial localization with experimental evidence (ECO:0000269) and an experimental GO annotation. The cited primary study is the source of that annotation, although it was not independently reviewed here."
  },
  "important_caveats": [
    "The annotation evidence is reviewer-only and was not available to the evaluated model.",
    "The N-terminal sequence pattern supports a prediction but does not independently establish localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The N-terminal targeting-signal pattern supports mitochondrion among the listed choices; the other options do not have comparable sequence-based support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, which reports mitochondrial localization with experimental evidence (ECO:0000269) and an experimental GO annotation. The cited primary study is the source of that annotation, although it was not independently reviewed here.",
    "evidence_ids": ["C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus is strongly enriched in arginine and lacks acidic residues over an extended segment, a pattern compatible with a mitochondrial targeting presequence. That provides a concrete reason to favor mitochondrion over the listed neuronal, host-membrane, and G-protein-complex options.",
    "missing_item_specific_fact": "The experimentally established localization and the protein's identity are not supplied; those would require protein-specific lookup to confirm rather than infer.",
    "reason": "The sequence offers a biologically meaningful targeting-signal clue for the broad compartment choice, even though that clue is not itself experimental proof."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The N-terminal targeting-signal pattern supports mitochondrion among the listed choices; the other options do not have comparable sequence-based support."
  },
  "important_caveats": [
    "The annotation evidence is reviewer-only and was not available to the evaluated model.",
    "The N-terminal sequence pattern supports a prediction but does not independently establish localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G4N954 (AUH1_PYRO7) annotates this protein as 'Methylglutaconyl-CoA hydratase 1, mitochondrial' (EC 4.2.1.18) with experimental evidence (ECO:0000269, PubMed:32431008). The GO annotation GO:0005739 (mitochondrion) carries EXP:UniProtKB evidence. The sequence is flagged as a Precursor, consistent with a cleavable mitochondrial targeting signal. Both current (C4, C5, C6) and historical (H1, H3) records confirm mitochondrial localization. The sequence match is exact (349 aa, SHA256 match).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~30 residues (MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQ) display classic mitochondrial targeting signal (MTS) features: enrichment in basic residues (R, K) and hydroxylated residues (S, T, A) with a notable absence of acidic residues (D, E) in the initial stretch, forming an amphipathic helix pattern typical of cleavable matrix-targeting presequences. The protein is small (~349 aa), globular, and lacks transmembrane helices, lipid-anchor motifs, or GTPase signature motifs (GXXXXGK&#91;ST&#93;, DxxG, NKxD). These features collectively support a soluble mitochondrial matrix enzyme and allow elimination of the other options: (A) no G-protein GTPase motifs; (B) no neuronal-specific structural features; (C) no transmembrane domains or lipid modifications.


**Missing item-specific fact**

> Precise recognition of the crotonase-superfamily catalytic fold (GGGLELAL, GAGGTHRLPRLIG motifs) and its connection to leucine catabolism in mitochondria would strengthen the positive identification, but is not strictly necessary given the MTS pattern and elimination of all other options.


**Reason**

> The N-terminal MTS-like composition provides a concrete, generalizable biological argument for mitochondrial targeting. The three distractors are eliminable by general structural biology: G-protein complexes require GTPase motifs, neuronal cell body requires neuron-specific context/proteins, and host cell plasma membrane requires TM domains or lipid anchors. None of these features are present. The positive evidence (basic/hydroxyl-rich N-terminus, no TM, globular soluble architecture) meaningfully points to mitochondrion without requiring exact database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> All three distractors are clearly eliminable: (A) lacks GTPase motifs entirely; (B) is a neuron-specific term inapplicable to a fungal enzyme with no neuronal structural features; (C) requires membrane-anchoring features absent from this globular sequence. Only D (mitochondrion) is consistent with the N-terminal MTS pattern and soluble matrix-enzyme architecture.


### Important caveats

- The organism (Pyricularia oryzae, a fungus) is not provided to the evaluated model, making elimination of option B (neuronal cell body) rely on absence of neuronal features rather than taxonomic knowledge.
- The MTS pattern in the N-terminus is suggestive but not absolutely diagnostic; other organelles (peroxisome, chloroplast) can also use basic N-terminal signals, though the overall context (no peroxisomal PTS1/PTS2 motifs, no chloroplast transit peptide features) favors mitochondrion.
- The specific enzyme identity (methylglutaconyl-CoA hydratase) and its mitochondrial pathway role are more lookup-dependent, but the question is answerable via MTS recognition and distractor elimination.
- The experimental evidence (PubMed:32431008) for mitochondrial localization was published in 2021, well before the benchmark construction; the annotation is stable and experimentally grounded rather than purely computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~30 residues (MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQ) display classic mitochondrial targeting signal (MTS) features: enrichment in basic residues (R, K) and hydroxylated residues (S, T, A) with a notable absence of acidic residues (D, E) in the initial stretch, forming an amphipathic helix pattern typical of cleavable matrix-targeting presequences. The protein is small (~349 aa), globular, and lacks transmembrane helices, lipid-anchor motifs, or GTPase signature motifs (GXXXXGK[ST], DxxG, NKxD). These features collectively support a soluble mitochondrial matrix enzyme and allow elimination of the other options: (A) no G-protein GTPase motifs; (B) no neuronal-specific structural features; (C) no transmembrane domains or lipid modifications.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of the crotonase-superfamily catalytic fold (GGGLELAL, GAGGTHRLPRLIG motifs) and its connection to leucine catabolism in mitochondria would strengthen the positive identification, but is not strictly necessary given the MTS pattern and elimination of all other options.",
    "reason": "The N-terminal MTS-like composition provides a concrete, generalizable biological argument for mitochondrial targeting. The three distractors are eliminable by general structural biology: G-protein complexes require GTPase motifs, neuronal cell body requires neuron-specific context/proteins, and host cell plasma membrane requires TM domains or lipid anchors. None of these features are present. The positive evidence (basic/hydroxyl-rich N-terminus, no TM, globular soluble architecture) meaningfully points to mitochondrion without requiring exact database lookup."
  },
  "case_id": "GO_cellular_component_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G4N954 (AUH1_PYRO7) annotates this protein as 'Methylglutaconyl-CoA hydratase 1, mitochondrial' (EC 4.2.1.18) with experimental evidence (ECO:0000269, PubMed:32431008). The GO annotation GO:0005739 (mitochondrion) carries EXP:UniProtKB evidence. The sequence is flagged as a Precursor, consistent with a cleavable mitochondrial targeting signal. Both current (C4, C5, C6) and historical (H1, H3) records confirm mitochondrial localization. The sequence match is exact (349 aa, SHA256 match)."
  },
  "important_caveats": [
    "The organism (Pyricularia oryzae, a fungus) is not provided to the evaluated model, making elimination of option B (neuronal cell body) rely on absence of neuronal features rather than taxonomic knowledge.",
    "The MTS pattern in the N-terminus is suggestive but not absolutely diagnostic; other organelles (peroxisome, chloroplast) can also use basic N-terminal signals, though the overall context (no peroxisomal PTS1/PTS2 motifs, no chloroplast transit peptide features) favors mitochondrion.",
    "The specific enzyme identity (methylglutaconyl-CoA hydratase) and its mitochondrial pathway role are more lookup-dependent, but the question is answerable via MTS recognition and distractor elimination.",
    "The experimental evidence (PubMed:32431008) for mitochondrial localization was published in 2021, well before the benchmark construction; the annotation is stable and experimentally grounded rather than purely computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "All three distractors are clearly eliminable: (A) lacks GTPase motifs entirely; (B) is a neuron-specific term inapplicable to a fungal enzyme with no neuronal structural features; (C) requires membrane-anchoring features absent from this globular sequence. Only D (mitochondrion) is consistent with the N-terminal MTS pattern and soluble matrix-enzyme architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G4N954 (AUH1_PYRO7) annotates this protein as 'Methylglutaconyl-CoA hydratase 1, mitochondrial' (EC 4.2.1.18) with experimental evidence (ECO:0000269, PubMed:32431008). The GO annotation GO:0005739 (mitochondrion) carries EXP:UniProtKB evidence. The sequence is flagged as a Precursor, consistent with a cleavable mitochondrial targeting signal. Both current (C4, C5, C6) and historical (H1, H3) records confirm mitochondrial localization. The sequence match is exact (349 aa, SHA256 match).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~30 residues (MPPVSRILSYAPRVAIRPSSQLARPARAFAVGTVRYYSAEQ) display classic mitochondrial targeting signal (MTS) features: enrichment in basic residues (R, K) and hydroxylated residues (S, T, A) with a notable absence of acidic residues (D, E) in the initial stretch, forming an amphipathic helix pattern typical of cleavable matrix-targeting presequences. The protein is small (~349 aa), globular, and lacks transmembrane helices, lipid-anchor motifs, or GTPase signature motifs (GXXXXGK[ST], DxxG, NKxD). These features collectively support a soluble mitochondrial matrix enzyme and allow elimination of the other options: (A) no G-protein GTPase motifs; (B) no neuronal-specific structural features; (C) no transmembrane domains or lipid modifications.",
    "missing_item_specific_fact": "Precise recognition of the crotonase-superfamily catalytic fold (GGGLELAL, GAGGTHRLPRLIG motifs) and its connection to leucine catabolism in mitochondria would strengthen the positive identification, but is not strictly necessary given the MTS pattern and elimination of all other options.",
    "reason": "The N-terminal MTS-like composition provides a concrete, generalizable biological argument for mitochondrial targeting. The three distractors are eliminable by general structural biology: G-protein complexes require GTPase motifs, neuronal cell body requires neuron-specific context/proteins, and host cell plasma membrane requires TM domains or lipid anchors. None of these features are present. The positive evidence (basic/hydroxyl-rich N-terminus, no TM, globular soluble architecture) meaningfully points to mitochondrion without requiring exact database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "All three distractors are clearly eliminable: (A) lacks GTPase motifs entirely; (B) is a neuron-specific term inapplicable to a fungal enzyme with no neuronal structural features; (C) requires membrane-anchoring features absent from this globular sequence. Only D (mitochondrion) is consistent with the N-terminal MTS pattern and soluble matrix-enzyme architecture."
  },
  "important_caveats": [
    "The organism (Pyricularia oryzae, a fungus) is not provided to the evaluated model, making elimination of option B (neuronal cell body) rely on absence of neuronal features rather than taxonomic knowledge.",
    "The MTS pattern in the N-terminus is suggestive but not absolutely diagnostic; other organelles (peroxisome, chloroplast) can also use basic N-terminal signals, though the overall context (no peroxisomal PTS1/PTS2 motifs, no chloroplast transit peptide features) favors mitochondrion.",
    "The specific enzyme identity (methylglutaconyl-CoA hydratase) and its mitochondrial pathway role are more lookup-dependent, but the question is answerable via MTS recognition and distractor elimination.",
    "The experimental evidence (PubMed:32431008) for mitochondrial localization was published in 2021, well before the benchmark construction; the annotation is stable and experimentally grounded rather than purely computational."
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

**Accession:** `G4N954` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
"G4N954"
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"32431008","source":"PubMed"}],"value":"4.2.1.18"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32431008","source":"PubMed"}],"value":"Methylglutaconyl-CoA hydratase 1, mitochondrial"}}}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"32431008","source":"PubMed"}],"id":"SL-0173","value":"Mitochondrion"}}]}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4N954.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:45.109101+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"32431008","source":"PubMed"}],"id":"GO:0005739","properties":[{"key":"GoTerm","value":"C:mitochondrion"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `f1feb70a0aa6ce77a3f46c3887f39c0438ffbec8f1dda03d658acd878f87049c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
ID   AUH1_PYRO7              Reviewed;         349 AA.
AC   G4N954;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-DEC-2011, sequence version 1.
DT   28-JAN-2026, entry version 54.
DE   RecName: Full=Methylglutaconyl-CoA hydratase 1, mitochondrial {ECO:0000303|PubMed:32431008};
DE            EC=4.2.1.18 {ECO:0000305|PubMed:32431008};
DE   Flags: Precursor;
GN   Name=AUH1 {ECO:0000303|PubMed:32431008}; ORFNames=MGG_03335;
OS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast
OS   fungus) (Magnaporthe oryzae).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.
OX   NCBI_TaxID=242507;
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4N954?format=txt&versions=54)  
**Locator:** `lines 53-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:47.046190+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:32431008}.
```

Source SHA-256: `0442f2ae47a56feb93ddf2851830770bbc3cdc78cf17135612d99cf022c5c856`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 74. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
