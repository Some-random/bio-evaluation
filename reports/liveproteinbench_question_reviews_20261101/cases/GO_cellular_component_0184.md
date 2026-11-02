# GO_cellular_component_0184

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — cell outer membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIALTERTERVRPQRVEQNLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGGAREVQFFTDEDGERNLVALEKKGGIWRRSASEADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLIYDSLYFHGQQVAAGDILAAEVVKGGTRHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. protein-DNA complex
B. nuclear pore nuclear basket
C. cell outer membrane
D. chromosome
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

> The exact sequence matches the UniProt entry for a Neisseria meningitidis protein annotated to the cell outer membrane. The entry reports a GO annotation with IDA evidence and describes the mature protein as probably associated with the outer membrane, citing PubMed:22046377. The location is therefore supported, though the prose retains a qualification of probability.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region is consistent with a bacterial export signal, which makes nuclear options implausible. But that general sequence feature does not establish that the mature protein resides at the outer membrane rather than another non-cytoplasmic location.


**Missing item-specific fact**

> The protein-specific localization annotation or experimental evidence linking this particular protein to the cell outer membrane.


**Reason**

> Selecting C over the other options depends on the specific localization of this protein, a fact not supplied in the question. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are distinguishable, and the matched protein-specific evidence supports C. The remaining options are not comparably supported by the sequence or supplied context.


### Important caveats

- The UniProt subcellular-location text says the mature protein is probably associated with the outer membrane; this should not be overstated as unqualified certainty.
- The database entry and sequence match are reviewer-only evidence and were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with a bacterial export signal, which makes nuclear options implausible. But that general sequence feature does not establish that the mature protein resides at the outer membrane rather than another non-cytoplasmic location.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence linking this particular protein to the cell outer membrane.",
    "reason": "Selecting C over the other options depends on the specific localization of this protein, a fact not supplied in the question. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "GO_cellular_component_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for a Neisseria meningitidis protein annotated to the cell outer membrane. The entry reports a GO annotation with IDA evidence and describes the mature protein as probably associated with the outer membrane, citing PubMed:22046377. The location is therefore supported, though the prose retains a qualification of probability."
  },
  "important_caveats": [
    "The UniProt subcellular-location text says the mature protein is probably associated with the outer membrane; this should not be overstated as unqualified certainty.",
    "The database entry and sequence match are reviewer-only evidence and were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are distinguishable, and the matched protein-specific evidence supports C. The remaining options are not comparably supported by the sequence or supplied context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for a Neisseria meningitidis protein annotated to the cell outer membrane. The entry reports a GO annotation with IDA evidence and describes the mature protein as probably associated with the outer membrane, citing PubMed:22046377. The location is therefore supported, though the prose retains a qualification of probability.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with a bacterial export signal, which makes nuclear options implausible. But that general sequence feature does not establish that the mature protein resides at the outer membrane rather than another non-cytoplasmic location.",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence linking this particular protein to the cell outer membrane.",
    "reason": "Selecting C over the other options depends on the specific localization of this protein, a fact not supplied in the question. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are distinguishable, and the matched protein-specific evidence supports C. The remaining options are not comparably supported by the sequence or supplied context."
  },
  "important_caveats": [
    "The UniProt subcellular-location text says the mature protein is probably associated with the outer membrane; this should not be overstated as unqualified certainty.",
    "The database entry and sequence match are reviewer-only evidence and were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E0N688 (MPG_NEIM3, Neisseria meningitidis) annotates this DD-carboxypeptidase/endopeptidase Mpg as located at the cell outer membrane (GO:0009279). Evidence C5 states: 'Mature protein is probably associated with the cell outer membrane (PubMed:22046377)' with evidence code ECO:0000305. The current entry carries a GO IDA annotation (C6). The protein is explicitly named 'Outer membrane protein' (OMP) in its alternative names (C4). The N-terminal hydrophobic region in the supplied sequence is consistent with a signal/transmembrane anchor for outer membrane association. The crystal structure (PDB 3SLU, residues 54-420) supports the mature protein's association. The 'probably' qualifier introduces mild uncertainty, but the IDA GO annotation and explicit 'Outer membrane protein' naming provide adequate support for the expected answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region of the sequence contains a hydrophobic stretch (~residues 11-27: ALRALAVSIILVSAAYIAL) characteristic of a signal peptide or transmembrane anchor, strongly indicating membrane association. Among the four options, only C (cell outer membrane) represents a membrane compartment. Options A (protein-DNA complex), B (nuclear pore nuclear basket), and D (chromosome) are all eukaryotic nuclear structures requiring DNA-binding motifs or nuclear localization signals, none of which are present. The zinc-binding motifs (HxxH patterns) are catalytic (metalloprotease), not DNA-binding. The absence of any eukaryotic nuclear targeting features and the presence of a prokaryotic-type signal peptide provide a concrete biological argument to select C.


**Missing item-specific fact**

> The organism identity (Neisseria meningitidis, a Gram-negative bacterium) is not stated in the question. However, the sequence features (prokaryotic-type signal peptide architecture, zinc metalloprotease domain common in bacterial surface proteins, absence of eukaryotic motifs) allow inference of bacterial origin and membrane targeting without exact species identification.


**Reason**

> A model can reason from the N-terminal hydrophobic signal peptide (indicating membrane targeting) and the complete absence of DNA-binding motifs, nuclear localization signals, or eukaryotic structural features to eliminate options A, B, and D. The only membrane-associated option is C. This is a valid biological inference chain, not dependent on memorizing a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are all eukaryotic nuclear compartments incompatible with a protein bearing a prokaryotic-type signal peptide and lacking any DNA-binding or nuclear-targeting features. Only C is a membrane compartment consistent with the N-terminal hydrophobic anchor. No other option is defensible given the sequence features.


### Important caveats

- The UniProt annotation uses 'probably associated with the cell outer membrane' (ECO:0000305), indicating some uncertainty; the current entry upgrades to IDA but the historical entry used IEA.
- The organism (Neisseria meningitidis) is not provided in the question; the model must infer bacterial origin from sequence features.
- The protein is a zinc metalloprotease with a signal/transmembrane region, not a classic β-barrel outer membrane protein, making its exact membrane topology (integral vs. peripherally associated) less obvious from sequence alone.
- The crystal structure covers residues 54-420, confirming the mature domain but not directly proving membrane anchoring.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region of the sequence contains a hydrophobic stretch (~residues 11-27: ALRALAVSIILVSAAYIAL) characteristic of a signal peptide or transmembrane anchor, strongly indicating membrane association. Among the four options, only C (cell outer membrane) represents a membrane compartment. Options A (protein-DNA complex), B (nuclear pore nuclear basket), and D (chromosome) are all eukaryotic nuclear structures requiring DNA-binding motifs or nuclear localization signals, none of which are present. The zinc-binding motifs (HxxH patterns) are catalytic (metalloprotease), not DNA-binding. The absence of any eukaryotic nuclear targeting features and the presence of a prokaryotic-type signal peptide provide a concrete biological argument to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The organism identity (Neisseria meningitidis, a Gram-negative bacterium) is not stated in the question. However, the sequence features (prokaryotic-type signal peptide architecture, zinc metalloprotease domain common in bacterial surface proteins, absence of eukaryotic motifs) allow inference of bacterial origin and membrane targeting without exact species identification.",
    "reason": "A model can reason from the N-terminal hydrophobic signal peptide (indicating membrane targeting) and the complete absence of DNA-binding motifs, nuclear localization signals, or eukaryotic structural features to eliminate options A, B, and D. The only membrane-associated option is C. This is a valid biological inference chain, not dependent on memorizing a specific database entry."
  },
  "case_id": "GO_cellular_component_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E0N688 (MPG_NEIM3, Neisseria meningitidis) annotates this DD-carboxypeptidase/endopeptidase Mpg as located at the cell outer membrane (GO:0009279). Evidence C5 states: 'Mature protein is probably associated with the cell outer membrane (PubMed:22046377)' with evidence code ECO:0000305. The current entry carries a GO IDA annotation (C6). The protein is explicitly named 'Outer membrane protein' (OMP) in its alternative names (C4). The N-terminal hydrophobic region in the supplied sequence is consistent with a signal/transmembrane anchor for outer membrane association. The crystal structure (PDB 3SLU, residues 54-420) supports the mature protein's association. The 'probably' qualifier introduces mild uncertainty, but the IDA GO annotation and explicit 'Outer membrane protein' naming provide adequate support for the expected answer."
  },
  "important_caveats": [
    "The UniProt annotation uses 'probably associated with the cell outer membrane' (ECO:0000305), indicating some uncertainty; the current entry upgrades to IDA but the historical entry used IEA.",
    "The organism (Neisseria meningitidis) is not provided in the question; the model must infer bacterial origin from sequence features.",
    "The protein is a zinc metalloprotease with a signal/transmembrane region, not a classic β-barrel outer membrane protein, making its exact membrane topology (integral vs. peripherally associated) less obvious from sequence alone.",
    "The crystal structure covers residues 54-420, confirming the mature domain but not directly proving membrane anchoring."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are all eukaryotic nuclear compartments incompatible with a protein bearing a prokaryotic-type signal peptide and lacking any DNA-binding or nuclear-targeting features. Only C is a membrane compartment consistent with the N-terminal hydrophobic anchor. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E0N688 (MPG_NEIM3, Neisseria meningitidis) annotates this DD-carboxypeptidase/endopeptidase Mpg as located at the cell outer membrane (GO:0009279). Evidence C5 states: 'Mature protein is probably associated with the cell outer membrane (PubMed:22046377)' with evidence code ECO:0000305. The current entry carries a GO IDA annotation (C6). The protein is explicitly named 'Outer membrane protein' (OMP) in its alternative names (C4). The N-terminal hydrophobic region in the supplied sequence is consistent with a signal/transmembrane anchor for outer membrane association. The crystal structure (PDB 3SLU, residues 54-420) supports the mature protein's association. The 'probably' qualifier introduces mild uncertainty, but the IDA GO annotation and explicit 'Outer membrane protein' naming provide adequate support for the expected answer.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region of the sequence contains a hydrophobic stretch (~residues 11-27: ALRALAVSIILVSAAYIAL) characteristic of a signal peptide or transmembrane anchor, strongly indicating membrane association. Among the four options, only C (cell outer membrane) represents a membrane compartment. Options A (protein-DNA complex), B (nuclear pore nuclear basket), and D (chromosome) are all eukaryotic nuclear structures requiring DNA-binding motifs or nuclear localization signals, none of which are present. The zinc-binding motifs (HxxH patterns) are catalytic (metalloprotease), not DNA-binding. The absence of any eukaryotic nuclear targeting features and the presence of a prokaryotic-type signal peptide provide a concrete biological argument to select C.",
    "missing_item_specific_fact": "The organism identity (Neisseria meningitidis, a Gram-negative bacterium) is not stated in the question. However, the sequence features (prokaryotic-type signal peptide architecture, zinc metalloprotease domain common in bacterial surface proteins, absence of eukaryotic motifs) allow inference of bacterial origin and membrane targeting without exact species identification.",
    "reason": "A model can reason from the N-terminal hydrophobic signal peptide (indicating membrane targeting) and the complete absence of DNA-binding motifs, nuclear localization signals, or eukaryotic structural features to eliminate options A, B, and D. The only membrane-associated option is C. This is a valid biological inference chain, not dependent on memorizing a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are all eukaryotic nuclear compartments incompatible with a protein bearing a prokaryotic-type signal peptide and lacking any DNA-binding or nuclear-targeting features. Only C is a membrane compartment consistent with the N-terminal hydrophobic anchor. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt annotation uses 'probably associated with the cell outer membrane' (ECO:0000305), indicating some uncertainty; the current entry upgrades to IDA but the historical entry used IEA.",
    "The organism (Neisseria meningitidis) is not provided in the question; the model must infer bacterial origin from sequence features.",
    "The protein is a zinc metalloprotease with a signal/transmembrane region, not a classic β-barrel outer membrane protein, making its exact membrane topology (integral vs. peripherally associated) less obvious from sequence alone.",
    "The crystal structure covers residues 54-420, confirming the mature domain but not directly proving membrane anchoring."
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

**Accession:** `E0N688` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5F676","source":"UniProtKB"}],"value":"Metalloprotease active against peptidoglycan"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"value":"Outer membrane protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"value":"OMP"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Zinc metallopeptidase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Zinc metalloprotease"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"value":"Zinc-dependent metallopeptidase"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5F676","source":"UniProtKB"}],"value":"3.4.17.-"},{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5F676","source":"UniProtKB"}],"value":"3.4.24.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"DD-carboxypeptidase/endopeptidase Mpg"}}}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"22046377","source":"PubMed"}],"value":"There is a signal or a transmembrane region in the N-terminus of the pre-protein (Probable). Mature protein is probably associated with the cell outer membrane (PubMed:22046377)"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"22046377","source":"PubMed"}],"id":"SL-0040","value":"Cell outer membrane"}}]}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"22046377","source":"PubMed"}],"id":"GO:0009279","properties":[{"key":"GoTerm","value":"C:cell outer membrane"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0N688.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:57.637304+00:00.  

```json
{"citation":{"authors":["Wang X.","Yang X.","Yang C.","Wu Z.","Xu H.","Shen Y."],"citationCrossReferences":[{"database":"PubMed","id":"22046377"},{"database":"DOI","id":"10.1371/journal.pone.0026845"}],"citationType":"journal article","firstPage":"e26845","id":"22046377","journal":"PLoS ONE","lastPage":"e26845","publicationDate":"2011","title":"Crystal structure of outer membrane protein NMB0315 from Neisseria meningitidis.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0007744","id":"3SLU","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22046377","source":"PubMed"}],"type":"STRAIN","value":"ATCC 13091 / M2091"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL","COFACTOR","SUBUNIT","SUBCELLULAR LOCATION","PTM"]}
```

Source SHA-256: `15b7733cc2a0e4ab39ce1f757e23e6eca2f74da5098179381b3861594fe30e7a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)  
**Locator:** `lines 1-20`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:01.531640+00:00.  

```text
ID   MPG_NEIM3               Reviewed;         430 AA.
AC   E0N688;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-NOV-2010, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=DD-carboxypeptidase/endopeptidase Mpg {ECO:0000305};
DE            EC=3.4.17.- {ECO:0000250|UniProtKB:Q5F676};
DE            EC=3.4.24.- {ECO:0000250|UniProtKB:Q5F676};
DE   AltName: Full=Metalloprotease active against peptidoglycan {ECO:0000250|UniProtKB:Q5F676};
DE   AltName: Full=Outer membrane protein {ECO:0000303|PubMed:22046377};
DE            Short=OMP {ECO:0000303|PubMed:22046377};
DE   AltName: Full=Zinc metallopeptidase {ECO:0000305};
DE   AltName: Full=Zinc metalloprotease {ECO:0000305};
DE   AltName: Full=Zinc-dependent metallopeptidase {ECO:0000303|PubMed:22046377};
DE   Flags: Precursor;
GN   ORFNames=HMPREF0602_0018 {ECO:0000312|EMBL:EFM05396.1};
OS   Neisseria meningitidis serogroup B (strain ATCC 13091 / M2091).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;
OC   Neisseriaceae; Neisseria.
OX   NCBI_TaxID=862513;
```

Source SHA-256: `6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)  
**Locator:** `lines 37-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:01.531640+00:00.  

```text
RN   [2] {ECO:0007744|PDB:3SLU}
RP   X-RAY CRYSTALLOGRAPHY (2.41 ANGSTROMS) OF 54-420 IN COMPLEX WITH NICKEL,
RP   COFACTOR, SUBUNIT, SUBCELLULAR LOCATION, AND PTM.
RC   STRAIN=ATCC 13091 / M2091 {ECO:0000303|PubMed:22046377};
RX   PubMed=22046377; DOI=10.1371/journal.pone.0026845;
RA   Wang X., Yang X., Yang C., Wu Z., Xu H., Shen Y.;
RT   "Crystal structure of outer membrane protein NMB0315 from Neisseria
RT   meningitidis.";
RL   PLoS ONE 6:e26845-e26845(2011).
```

Source SHA-256: `6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)  
**Locator:** `lines 56-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:01.531640+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell outer membrane
CC       {ECO:0000305|PubMed:22046377}. Note=There is a signal or a
CC       transmembrane region in the N-terminus of the pre-protein (Probable).
CC       Mature protein is probably associated with the cell outer membrane
CC       (PubMed:22046377). {ECO:0000305|PubMed:22046377}.
```

Source SHA-256: `6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0N688?format=txt&versions=51)  
**Locator:** `lines 79-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:01.531640+00:00.  

```text
DR   GO; GO:0009279; C:cell outer membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `6bc19bde1a2b73ea5937ac1c69862e82fb2baf2bbd761f0a7ea56227dc234bf1`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 94785-94797`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009279
name: cell outer membrane
namespace: cellular_component
def: "A lipid bilayer that forms the outermost membrane of the cell envelope; enriched in polysaccharide and protein; the outer leaflet of the membrane contains specific lipopolysaccharide structures." [GOC:md, GOC:mtg_sensu, ISBN:0135712254]
comment: To annotate the plasma (cytoplasmic) membrane, see instead GO:0005886.
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
synonym: "outer membrane of cell" EXACT []
is_a: GO:0019867 ! outer membrane
is_a: GO:0030312 ! external encapsulating structure
relationship: part_of GO:0030313 ! cell envelope

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
