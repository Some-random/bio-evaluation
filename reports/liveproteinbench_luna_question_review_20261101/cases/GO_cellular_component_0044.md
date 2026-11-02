# GO_cellular_component_0044

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MLSLFNRLPWLHRVLITAFSAIIVFAIFFLPNSEDLRKPDAQREVGRHYPVTLDNQLVSTPEEEVIAPPSVMLRWETYQVANGESAALLFQRAGLSSRVLYELTSSNSDINNQLSKLMPKDELKFGFDKDNQLVQLKRTISPYETFVVTRSDSGFTSEFDKKEVTFQLNYAEAKITSNFWNAGVTAGLSANQIIELANMFGWDIDFALDIREGDQFKLLYQEKIVEGSVIGRGNIIAATFINQGSTFTAILDDNTGNYYDQNGRAMKKAFLRSPLDFRRVSSNFNPRRLHPVTGQIKAHRGTDYVAPVGTPIWAAGDGVVEKSSYNQFNGNYVYIRHSNTYITKYLHLQRRLVKTGERVKQGQTIGTLGGTGRVTGPHLHYEFLVNGIHKNPRTVELPQAQSLTGKAKETFIANAKQRMEKLERYSQLLYANQ

[Multiple Choices]
A. protein-containing complex
B. endoplasmic reticulum membrane
C. plasma membrane
D. extracellular region
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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence matches the protein annotated as localized to the bacterial inner membrane, on its periplasmic side. The source reports experimental localization, and the periplasmic side of the plasma membrane is part of the plasma membrane; thus C is supported.

Cited evidence: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO3](#evidence-go3), [GO6](#evidence-go6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment supports membrane association, but that alone does not distinguish a plasma membrane protein from an ER membrane protein. The large downstream domain could also be consistent with an exported or membrane-tethered protein.

**Missing item-specific fact**

> The protein-specific identity and localization: it is Vibrio cholerae ShyC, experimentally localized to the cell periphery and midcell, with a single-pass inner-membrane topology and periplasmic orientation.

**Reason**

> The sequence offers a useful membrane-association clue, but selecting C over another membrane location requires item-specific organism/function or localization information not supplied in the question.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The source evidence supports C as the annotated location; the periplasmic-side annotation is compatible with, and more specific than, the plasma membrane option.

### Important caveats

- Reviewer-only database and literature-derived evidence supports the key but was not available to the evaluated model.
- The UniProt sequence match is exact; its localization note cites experimental evidence, whereas the single-pass topology annotation is computational.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_cellular_component_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the protein annotated as localized to the bacterial inner membrane, on its periplasmic side. The source reports experimental localization, and the periplasmic side of the plasma membrane is part of the plasma membrane; thus C is supported.",
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "GO3",
      "GO6"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment supports membrane association, but that alone does not distinguish a plasma membrane protein from an ER membrane protein. The large downstream domain could also be consistent with an exported or membrane-tethered protein.",
    "missing_item_specific_fact": "The protein-specific identity and localization: it is Vibrio cholerae ShyC, experimentally localized to the cell periphery and midcell, with a single-pass inner-membrane topology and periplasmic orientation.",
    "reason": "The sequence offers a useful membrane-association clue, but selecting C over another membrane location requires item-specific organism/function or localization information not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports C as the annotated location; the periplasmic-side annotation is compatible with, and more specific than, the plasma membrane option."
  },
  "important_caveats": [
    "Reviewer-only database and literature-derived evidence supports the key but was not available to the evaluated model.",
    "The UniProt sequence match is exact; its localization note cites experimental evidence, whereas the single-pass topology annotation is computational."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9KU93`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 105. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.755646+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23834664","source":"PubMed"}],"value":"Localizes to the periphery of the cell and at the midcell in a subset of cells"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"23834664","source":"PubMed"}],"id":"SL-0037","value":"Cell inner membrane"},"orientation":{"evidences":[{"evidenceCode":"ECO:0000305","id":"23834664","source":"PubMed"}],"id":"SL-9916","value":"Periplasmic side"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9904","value":"Single-pass membrane protein"}}]}
```

Source SHA-256: `4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.755646+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"23834664","source":"PubMed"}],"id":"GO:0098567","properties":[{"key":"GoTerm","value":"C:periplasmic side of plasma membrane"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)  
**Locator:** `lines 64-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-01T06:28:46.934559+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell inner membrane
CC       {ECO:0000305|PubMed:23834664}; Single-pass membrane protein
CC       {ECO:0000255}; Periplasmic side {ECO:0000305|PubMed:23834664}.
CC       Note=Localizes to the periphery of the cell and at the midcell in a
CC       subset of cells. {ECO:0000269|PubMed:23834664}.
```

Source SHA-256: `69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)  
**Locator:** `lines 93-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-01T06:28:46.934559+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c`.

### Evidence GO3

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

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 409072-409078`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0098567
name: periplasmic side of plasma membrane
namespace: cellular_component
def: "The leaflet of the plasma membrane that faces the periplasm, including any protein embedded in, attached to, or peripherally associated with it." [GOC:dos]
is_a: GO:0009897 ! external side of plasma membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json) (zero-based source row 44). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
