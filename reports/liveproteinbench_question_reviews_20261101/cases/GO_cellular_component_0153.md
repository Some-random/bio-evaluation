# GO_cellular_component_0153

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSIIGSFPPGGPRVEVQETRVQTDRVLTIPNILSMARLAGVPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD

[Multiple Choices]
A. actin cytoskeleton
B. microvillus membrane
C. plasma membrane
D. trans-Golgi network membrane
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

> The sequence matches the Streptomyces coelicolor cardiolipin synthase record, which annotates the protein to the cell membrane. In GO, “cell membrane” is an exact synonym of “plasma membrane,” including in the prokaryotic context. The annotation is a literature-based manual assertion, while the GO plasma-membrane cross-reference is computationally assigned; neither should be mistaken for a directly supplied measurement.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5), [H5](#evidence-h5), [C6](#evidence-c6), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments support that this is an integral membrane protein, but do not by themselves distinguish the plasma membrane from another membrane. Identifying a bacterial context could make the eukaryote-specific microvillus and trans-Golgi choices implausible, but does not establish this protein’s particular membrane localization from the supplied sequence alone.


**Missing item-specific fact**

> The protein-specific localization annotation or supporting literature that places this cardiolipin synthase at the cell membrane.


**Reason**

> The evidence supporting the key is reviewer-only and absent from the question. The sequence provides a membrane-protein clue, not sufficient grounds to select plasma membrane over all other membrane options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein-specific cell-membrane annotation maps to the offered plasma-membrane choice; no other option is supported by the supplied evidence.


### Important caveats

- The accession and organism identity were inferred from reviewer-only metadata, not provided to the evaluated model.
- The cited UniProt location is a manual literature-based assertion; the GO plasma-membrane annotation is IEA:UniProtKB-SubCell.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments support that this is an integral membrane protein, but do not by themselves distinguish the plasma membrane from another membrane. Identifying a bacterial context could make the eukaryote-specific microvillus and trans-Golgi choices implausible, but does not establish this protein’s particular membrane localization from the supplied sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or supporting literature that places this cardiolipin synthase at the cell membrane.",
    "reason": "The evidence supporting the key is reviewer-only and absent from the question. The sequence provides a membrane-protein clue, not sufficient grounds to select plasma membrane over all other membrane options."
  },
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5",
      "H5",
      "C6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the Streptomyces coelicolor cardiolipin synthase record, which annotates the protein to the cell membrane. In GO, “cell membrane” is an exact synonym of “plasma membrane,” including in the prokaryotic context. The annotation is a literature-based manual assertion, while the GO plasma-membrane cross-reference is computationally assigned; neither should be mistaken for a directly supplied measurement."
  },
  "important_caveats": [
    "The accession and organism identity were inferred from reviewer-only metadata, not provided to the evaluated model.",
    "The cited UniProt location is a manual literature-based assertion; the GO plasma-membrane annotation is IEA:UniProtKB-SubCell."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific cell-membrane annotation maps to the offered plasma-membrane choice; no other option is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Streptomyces coelicolor cardiolipin synthase record, which annotates the protein to the cell membrane. In GO, “cell membrane” is an exact synonym of “plasma membrane,” including in the prokaryotic context. The annotation is a literature-based manual assertion, while the GO plasma-membrane cross-reference is computationally assigned; neither should be mistaken for a directly supplied measurement.",
    "evidence_ids": ["H4", "C5", "H5", "C6", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments support that this is an integral membrane protein, but do not by themselves distinguish the plasma membrane from another membrane. Identifying a bacterial context could make the eukaryote-specific microvillus and trans-Golgi choices implausible, but does not establish this protein’s particular membrane localization from the supplied sequence alone.",
    "missing_item_specific_fact": "The protein-specific localization annotation or supporting literature that places this cardiolipin synthase at the cell membrane.",
    "reason": "The evidence supporting the key is reviewer-only and absent from the question. The sequence provides a membrane-protein clue, not sufficient grounds to select plasma membrane over all other membrane options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific cell-membrane annotation maps to the offered plasma-membrane choice; no other option is supported by the supplied evidence."
  },
  "important_caveats": [
    "The accession and organism identity were inferred from reviewer-only metadata, not provided to the evaluated model.",
    "The cited UniProt location is a manual literature-based assertion; the GO plasma-membrane annotation is IEA:UniProtKB-SubCell."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, Streptomyces coelicolor) annotates subcellular location as 'Cell membrane; Multi-pass membrane protein' (evidence: ECO:0000305 from PubMed:19439403, an experimental study). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). GO:0005886 lists 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms, confirming the mapping. The 2009 J. Biol. Chem. paper (Sandoval-Calderon et al.) experimentally determined subcellular location. The sequence matches exactly (215 aa, SHA256 match).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1), [C7](#evidence-c7), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches (e.g., MARLAGVPLFLWLILRPEFG, GWALLVLALSGVSDY, LSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRR, FNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRL) indicating a multi-pass transmembrane protein. The absence of eukaryotic signal peptides, no ER/Golgi targeting motifs, and the short length (215 aa) with amino acid composition consistent with a GC-rich actinobacterium point to a bacterial origin. Bacteria lack a Golgi apparatus (eliminating D: trans-Golgi network membrane), microvilli (eliminating B: microvillus membrane), and a true actin cytoskeleton (eliminating A: actin cytoskeleton). The only remaining viable compartment for a bacterial multi-pass membrane protein is the cell/plasma membrane (option C), which GO:0005886 explicitly includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms.


**Missing item-specific fact**

> None strictly required. The sequence features (multiple TM helices, bacterial-like composition, absence of eukaryotic targeting signals) combined with general knowledge that bacteria lack Golgi, microvilli, and actin cytoskeleton provide sufficient grounds to select C.


**Reason**

> A model can reason: (1) multiple TM domains → membrane protein; (2) no eukaryotic secretory-pathway targeting signals and bacterial-like sequence composition → bacterial origin; (3) bacteria lack Golgi, microvilli, and actin cytoskeleton → eliminate A, B, D; (4) bacterial cell membrane = plasma membrane in GO → select C. This is a concrete biological argument grounded in the sequence and general cell biology, not requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe structures exclusive to eukaryotic cells. Given the bacterial sequence features, only C (plasma membrane) is biologically viable. No other option is defensible for a bacterial multi-pass membrane protein.


### Important caveats

- The GO annotation evidence code for plasma membrane is IEA:UniProtKB-SubCell (electronic inference from UniProt), but the underlying UniProt annotation traces to experimental determination in PubMed:19439403 (Sandoval-Calderon et al. 2009, J. Biol. Chem.).
- The organism (Streptomyces coelicolor) is not explicitly stated in the question; the model must infer bacterial origin from sequence features. This inference, while reasonable, adds a step of difficulty.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model.
- GO:0005886 'plasma membrane' includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms per the ontology definition (GO1), making the mapping from bacterial 'cell membrane' annotation to 'plasma membrane' unambiguous.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (e.g., MARLAGVPLFLWLILRPEFG, GWALLVLALSGVSDY, LSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRR, FNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRL) indicating a multi-pass transmembrane protein. The absence of eukaryotic signal peptides, no ER/Golgi targeting motifs, and the short length (215 aa) with amino acid composition consistent with a GC-rich actinobacterium point to a bacterial origin. Bacteria lack a Golgi apparatus (eliminating D: trans-Golgi network membrane), microvilli (eliminating B: microvillus membrane), and a true actin cytoskeleton (eliminating A: actin cytoskeleton). The only remaining viable compartment for a bacterial multi-pass membrane protein is the cell/plasma membrane (option C), which GO:0005886 explicitly includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The sequence features (multiple TM helices, bacterial-like composition, absence of eukaryotic targeting signals) combined with general knowledge that bacteria lack Golgi, microvilli, and actin cytoskeleton provide sufficient grounds to select C.",
    "reason": "A model can reason: (1) multiple TM domains → membrane protein; (2) no eukaryotic secretory-pathway targeting signals and bacterial-like sequence composition → bacterial origin; (3) bacteria lack Golgi, microvilli, and actin cytoskeleton → eliminate A, B, D; (4) bacterial cell membrane = plasma membrane in GO → select C. This is a concrete biological argument grounded in the sequence and general cell biology, not requiring recall of this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO1",
      "C7",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, Streptomyces coelicolor) annotates subcellular location as 'Cell membrane; Multi-pass membrane protein' (evidence: ECO:0000305 from PubMed:19439403, an experimental study). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). GO:0005886 lists 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms, confirming the mapping. The 2009 J. Biol. Chem. paper (Sandoval-Calderon et al.) experimentally determined subcellular location. The sequence matches exactly (215 aa, SHA256 match)."
  },
  "important_caveats": [
    "The GO annotation evidence code for plasma membrane is IEA:UniProtKB-SubCell (electronic inference from UniProt), but the underlying UniProt annotation traces to experimental determination in PubMed:19439403 (Sandoval-Calderon et al. 2009, J. Biol. Chem.).",
    "The organism (Streptomyces coelicolor) is not explicitly stated in the question; the model must infer bacterial origin from sequence features. This inference, while reasonable, adds a step of difficulty.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model.",
    "GO:0005886 'plasma membrane' includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms per the ontology definition (GO1), making the mapping from bacterial 'cell membrane' annotation to 'plasma membrane' unambiguous."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe structures exclusive to eukaryotic cells. Given the bacterial sequence features, only C (plasma membrane) is biologically viable. No other option is defensible for a bacterial multi-pass membrane protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, Streptomyces coelicolor) annotates subcellular location as 'Cell membrane; Multi-pass membrane protein' (evidence: ECO:0000305 from PubMed:19439403, an experimental study). The GO cross-reference maps this to GO:0005886 'plasma membrane' (IEA:UniProtKB-SubCell). GO:0005886 lists 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms, confirming the mapping. The 2009 J. Biol. Chem. paper (Sandoval-Calderon et al.) experimentally determined subcellular location. The sequence matches exactly (215 aa, SHA256 match).",
    "evidence_ids": ["C5", "C6", "H4", "H5", "GO1", "C7", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches (e.g., MARLAGVPLFLWLILRPEFG, GWALLVLALSGVSDY, LSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRR, FNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRL) indicating a multi-pass transmembrane protein. The absence of eukaryotic signal peptides, no ER/Golgi targeting motifs, and the short length (215 aa) with amino acid composition consistent with a GC-rich actinobacterium point to a bacterial origin. Bacteria lack a Golgi apparatus (eliminating D: trans-Golgi network membrane), microvilli (eliminating B: microvillus membrane), and a true actin cytoskeleton (eliminating A: actin cytoskeleton). The only remaining viable compartment for a bacterial multi-pass membrane protein is the cell/plasma membrane (option C), which GO:0005886 explicitly includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms.",
    "missing_item_specific_fact": "None strictly required. The sequence features (multiple TM helices, bacterial-like composition, absence of eukaryotic targeting signals) combined with general knowledge that bacteria lack Golgi, microvilli, and actin cytoskeleton provide sufficient grounds to select C.",
    "reason": "A model can reason: (1) multiple TM domains → membrane protein; (2) no eukaryotic secretory-pathway targeting signals and bacterial-like sequence composition → bacterial origin; (3) bacteria lack Golgi, microvilli, and actin cytoskeleton → eliminate A, B, D; (4) bacterial cell membrane = plasma membrane in GO → select C. This is a concrete biological argument grounded in the sequence and general cell biology, not requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe structures exclusive to eukaryotic cells. Given the bacterial sequence features, only C (plasma membrane) is biologically viable. No other option is defensible for a bacterial multi-pass membrane protein."
  },
  "important_caveats": [
    "The GO annotation evidence code for plasma membrane is IEA:UniProtKB-SubCell (electronic inference from UniProt), but the underlying UniProt annotation traces to experimental determination in PubMed:19439403 (Sandoval-Calderon et al. 2009, J. Biol. Chem.).",
    "The organism (Streptomyces coelicolor) is not explicitly stated in the question; the model must infer bacterial origin from sequence features. This inference, while reasonable, adds a step of difficulty.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model.",
    "GO:0005886 'plasma membrane' includes 'cell membrane' and 'cytoplasmic membrane' as EXACT synonyms per the ontology definition (GO1), making the mapping from bacterial 'cell membrane' annotation to 'plasma membrane' unambiguous."
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

**Accession:** `Q9KZP3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 118. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"19439403","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"citation":{"authors":["Sandoval-Calderon M.","Geiger O.","Guan Z.","Barona-Gomez F.","Sohlenkamp C."],"citationCrossReferences":[{"database":"PubMed","id":"19439403"},{"database":"DOI","id":"10.1074/jbc.m109.006072"}],"citationType":"journal article","firstPage":"17383","id":"19439403","journal":"J. Biol. Chem.","lastPage":"17390","publicationDate":"2009","title":"A eukaryote-like cardiolipin synthase is present in Streptomyces coelicolor and in most actinobacteria.","volume":"284"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 31-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND
RP   SUBCELLULAR LOCATION.
RX   PubMed=19439403; DOI=10.1074/jbc.m109.006072;
RA   Sandoval-Calderon M., Geiger O., Guan Z., Barona-Gomez F., Sohlenkamp C.;
RT   "A eukaryote-like cardiolipin synthase is present in Streptomyces
RT   coelicolor and in most actinobacteria.";
RL   J. Biol. Chem. 284:17383-17390(2009).
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 66-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000305|PubMed:19439403};
CC       Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 93-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 153. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
