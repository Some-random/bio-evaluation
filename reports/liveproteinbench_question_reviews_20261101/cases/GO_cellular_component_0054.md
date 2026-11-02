# GO_cellular_component_0054

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTQLPYLLDRRGGALAAPATAWGDMMLNRALFSVALLSSVGSAWVVLSYACIKELRSYRHQLILGLAISDLLMSLNFMFSAGWNVAGGDLALEESRTACSVNGFLTQVFVVQTDWWILVIAIATYIILGNFKTQSQFIQTHVWIPWVGPWVLSIIIAAICHGVLGYGYIGGWCWLTSDLMRLLINFIPRWLIVIAIALIYIRLYMIVRKARKWDIEGVSPDPGDDMADTSVILMSVGKKDRERQGSGVLVSRDVSVSFGRKGSTAPTFVTMVTTSGAGDSREAISSCSAREEGSRARTVNVNSSRSLSLGMRQPLNAAQLKRIAKKMMVYPVAYAIIWACPTAIRIYQGTTGSRAPLWITIVDKSCIVIQGLVDAVVYGLNERAWQGWRDHIRRIIYKNEGGRIIG

[Multiple Choices]
A. cell leading edge
B. plasma membrane
C. endoplasmic reticulum
D. cell surface
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

> The sequence matches the cited UniProt entry, which annotates the protein to the cell membrane with PubMed-linked experimental evidence. GO treats “cell membrane” as an exact synonym of “plasma membrane.” The annotation also reports ligand-stimulated relocalization to the vacuole, so the plasma-membrane assignment is not necessarily exclusive or invariant.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple hydrophobic transmembrane segments, supporting that it is a membrane protein. That does not distinguish plasma membrane from endoplasmic reticulum or establish cell-surface localization.


**Missing item-specific fact**

> The protein-specific localization annotation or experimental evidence that this receptor resides at the cell membrane, and can relocalize to the vacuole after ligand stimulation.


**Reason**

> The supplied sequence supports membrane insertion but does not provide a reliable basis for selecting the plasma membrane over the other membrane-related choices. The localization evidence is item-specific and was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> B is the directly supported, more specific location. D is also potentially defensible at a broader GO level: the cell-surface term includes products integrated into or loosely bound to the plasma membrane. The supplied annotation does not itself assign the cell-surface term.


### Important caveats

- The reviewer-only UniProt record and archived entry match the supplied sequence; that identity information was not available in the question.
- The UniProt cell-membrane annotation cites PubMed evidence with an experimental evidence code, but the underlying paper was not independently assessed here.
- The current UniProt entry also records ligand-stimulated relocalization to the vacuole.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic transmembrane segments, supporting that it is a membrane protein. That does not distinguish plasma membrane from endoplasmic reticulum or establish cell-surface localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence that this receptor resides at the cell membrane, and can relocalize to the vacuole after ligand stimulation.",
    "reason": "The supplied sequence supports membrane insertion but does not provide a reliable basis for selecting the plasma membrane over the other membrane-related choices. The localization evidence is item-specific and was not supplied to the evaluated model."
  },
  "case_id": "GO_cellular_component_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which annotates the protein to the cell membrane with PubMed-linked experimental evidence. GO treats “cell membrane” as an exact synonym of “plasma membrane.” The annotation also reports ligand-stimulated relocalization to the vacuole, so the plasma-membrane assignment is not necessarily exclusive or invariant."
  },
  "important_caveats": [
    "The reviewer-only UniProt record and archived entry match the supplied sequence; that identity information was not available in the question.",
    "The UniProt cell-membrane annotation cites PubMed evidence with an experimental evidence code, but the underlying paper was not independently assessed here.",
    "The current UniProt entry also records ligand-stimulated relocalization to the vacuole."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B is the directly supported, more specific location. D is also potentially defensible at a broader GO level: the cell-surface term includes products integrated into or loosely bound to the plasma membrane. The supplied annotation does not itself assign the cell-surface term."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt entry, which annotates the protein to the cell membrane with PubMed-linked experimental evidence. GO treats “cell membrane” as an exact synonym of “plasma membrane.” The annotation also reports ligand-stimulated relocalization to the vacuole, so the plasma-membrane assignment is not necessarily exclusive or invariant.",
    "evidence_ids": ["H3", "C5", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic transmembrane segments, supporting that it is a membrane protein. That does not distinguish plasma membrane from endoplasmic reticulum or establish cell-surface localization.",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence that this receptor resides at the cell membrane, and can relocalize to the vacuole after ligand stimulation.",
    "reason": "The supplied sequence supports membrane insertion but does not provide a reliable basis for selecting the plasma membrane over the other membrane-related choices. The localization evidence is item-specific and was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "B is the directly supported, more specific location. D is also potentially defensible at a broader GO level: the cell-surface term includes products integrated into or loosely bound to the plasma membrane. The supplied annotation does not itself assign the cell-surface term."
  },
  "important_caveats": [
    "The reviewer-only UniProt record and archived entry match the supplied sequence; that identity information was not available in the question.",
    "The UniProt cell-membrane annotation cites PubMed evidence with an experimental evidence code, but the underlying paper was not independently assessed here.",
    "The current UniProt entry also records ligand-stimulated relocalization to the vacuole."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G1X9E2 (Ascaroside receptor GPR2, a 7-TM GPCR from Arthrobotrys oligospora) annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:38649409, Nat. Microbiol. 2024). The GO cross-reference assigns GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym. The sequence matches the benchmark input exactly. The expected answer B (plasma membrane) is directly supported by the annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays approximately seven hydrophobic stretches of ~20-25 residues separated by hydrophilic loops, with a longer N-terminal extracellular region and a hydrophilic C-terminal tail. This 7-TM topology with extracellular N-terminus and intracellular C-terminus is the canonical architecture of a G protein-coupled receptor, which is a well-known class of plasma membrane receptors. ER membrane proteins, while also multi-pass, typically lack this specific 7-TM GPCR topology and do not present a long extracellular N-terminal domain. The general biological knowledge that 7-TM receptors reside at the plasma membrane provides a concrete reasoning path from sequence to answer B.


**Missing item-specific fact**

> None critical. The distinction between plasma membrane and cell surface (option D) relies somewhat on GO annotation convention (cell surface refers to the external part of cell wall/plasma membrane, typically for cell-wall-associated proteins), but the multi-pass integral membrane topology more naturally maps to 'plasma membrane' than 'cell surface' under standard GO usage.


**Reason**

> A knowledgeable model can identify the 7-TM GPCR topology from the hydrophobicity pattern in the sequence and apply the general biological fact that GPCRs are plasma membrane proteins. This distinguishes B from C (ER) and A (leading edge). The B-vs-D distinction is somewhat convention-dependent but the integral multi-pass membrane topology favors 'plasma membrane' over 'cell surface' (which GO reserves for cell-wall-associated or peripherally attached proteins).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> GO:0009986 (cell surface) is defined as 'The external part of the cell wall and/or plasma membrane' and includes gene products 'attached (integrated or loosely bound) to the plasma membrane or cell wall.' A multi-pass membrane protein is integrated in the plasma membrane, which is part of the cell surface. However, standard GO annotation practice assigns multi-pass integral membrane proteins (especially GPCRs) to 'plasma membrane' (GO:0005886) rather than 'cell surface' (GO:0009986), which is more commonly used for cell-wall-associated proteins in fungi. The UniProt annotation explicitly uses GO:0005886. While D is not strictly wrong in a colloquial sense, B is the more precise and conventionally correct GO term.


### Important caveats

- The GO annotation for plasma membrane carries evidence code IEA:UniProtKB-SubCell (inferred from electronic annotation based on the UniProt subcellular location comment), while the underlying subcellular location comment has experimental evidence (ECO:0000269) from PubMed:38649409.
- The UniProt topology annotation 'Multi-pass membrane protein' uses evidence code ECO:0000255 (sequence analysis), not direct experimental determination of membrane topology.
- The protein is from a fungus (Arthrobotrys oligospora); the 'plasma membrane' vs 'cell surface' distinction is relevant in fungal biology where a cell wall lies outside the plasma membrane.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what could be inferred from the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays approximately seven hydrophobic stretches of ~20-25 residues separated by hydrophilic loops, with a longer N-terminal extracellular region and a hydrophilic C-terminal tail. This 7-TM topology with extracellular N-terminus and intracellular C-terminus is the canonical architecture of a G protein-coupled receptor, which is a well-known class of plasma membrane receptors. ER membrane proteins, while also multi-pass, typically lack this specific 7-TM GPCR topology and do not present a long extracellular N-terminal domain. The general biological knowledge that 7-TM receptors reside at the plasma membrane provides a concrete reasoning path from sequence to answer B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The distinction between plasma membrane and cell surface (option D) relies somewhat on GO annotation convention (cell surface refers to the external part of cell wall/plasma membrane, typically for cell-wall-associated proteins), but the multi-pass integral membrane topology more naturally maps to 'plasma membrane' than 'cell surface' under standard GO usage.",
    "reason": "A knowledgeable model can identify the 7-TM GPCR topology from the hydrophobicity pattern in the sequence and apply the general biological fact that GPCRs are plasma membrane proteins. This distinguishes B from C (ER) and A (leading edge). The B-vs-D distinction is somewhat convention-dependent but the integral multi-pass membrane topology favors 'plasma membrane' over 'cell surface' (which GO reserves for cell-wall-associated or peripherally attached proteins)."
  },
  "case_id": "GO_cellular_component_0054",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G1X9E2 (Ascaroside receptor GPR2, a 7-TM GPCR from Arthrobotrys oligospora) annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:38649409, Nat. Microbiol. 2024). The GO cross-reference assigns GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym. The sequence matches the benchmark input exactly. The expected answer B (plasma membrane) is directly supported by the annotation."
  },
  "important_caveats": [
    "The GO annotation for plasma membrane carries evidence code IEA:UniProtKB-SubCell (inferred from electronic annotation based on the UniProt subcellular location comment), while the underlying subcellular location comment has experimental evidence (ECO:0000269) from PubMed:38649409.",
    "The UniProt topology annotation 'Multi-pass membrane protein' uses evidence code ECO:0000255 (sequence analysis), not direct experimental determination of membrane topology.",
    "The protein is from a fungus (Arthrobotrys oligospora); the 'plasma membrane' vs 'cell surface' distinction is relevant in fungal biology where a cell wall lies outside the plasma membrane.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what could be inferred from the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "GO:0009986 (cell surface) is defined as 'The external part of the cell wall and/or plasma membrane' and includes gene products 'attached (integrated or loosely bound) to the plasma membrane or cell wall.' A multi-pass membrane protein is integrated in the plasma membrane, which is part of the cell surface. However, standard GO annotation practice assigns multi-pass integral membrane proteins (especially GPCRs) to 'plasma membrane' (GO:0005886) rather than 'cell surface' (GO:0009986), which is more commonly used for cell-wall-associated proteins in fungi. The UniProt annotation explicitly uses GO:0005886. While D is not strictly wrong in a colloquial sense, B is the more precise and conventionally correct GO term."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0054",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G1X9E2 (Ascaroside receptor GPR2, a 7-TM GPCR from Arthrobotrys oligospora) annotates the subcellular location as 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:38649409, Nat. Microbiol. 2024). The GO cross-reference assigns GO:0005886 (plasma membrane), which has 'cell membrane' as an EXACT synonym. The sequence matches the benchmark input exactly. The expected answer B (plasma membrane) is directly supported by the annotation.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays approximately seven hydrophobic stretches of ~20-25 residues separated by hydrophilic loops, with a longer N-terminal extracellular region and a hydrophilic C-terminal tail. This 7-TM topology with extracellular N-terminus and intracellular C-terminus is the canonical architecture of a G protein-coupled receptor, which is a well-known class of plasma membrane receptors. ER membrane proteins, while also multi-pass, typically lack this specific 7-TM GPCR topology and do not present a long extracellular N-terminal domain. The general biological knowledge that 7-TM receptors reside at the plasma membrane provides a concrete reasoning path from sequence to answer B.",
    "missing_item_specific_fact": "None critical. The distinction between plasma membrane and cell surface (option D) relies somewhat on GO annotation convention (cell surface refers to the external part of cell wall/plasma membrane, typically for cell-wall-associated proteins), but the multi-pass integral membrane topology more naturally maps to 'plasma membrane' than 'cell surface' under standard GO usage.",
    "reason": "A knowledgeable model can identify the 7-TM GPCR topology from the hydrophobicity pattern in the sequence and apply the general biological fact that GPCRs are plasma membrane proteins. This distinguishes B from C (ER) and A (leading edge). The B-vs-D distinction is somewhat convention-dependent but the integral multi-pass membrane topology favors 'plasma membrane' over 'cell surface' (which GO reserves for cell-wall-associated or peripherally attached proteins)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "GO:0009986 (cell surface) is defined as 'The external part of the cell wall and/or plasma membrane' and includes gene products 'attached (integrated or loosely bound) to the plasma membrane or cell wall.' A multi-pass membrane protein is integrated in the plasma membrane, which is part of the cell surface. However, standard GO annotation practice assigns multi-pass integral membrane proteins (especially GPCRs) to 'plasma membrane' (GO:0005886) rather than 'cell surface' (GO:0009986), which is more commonly used for cell-wall-associated proteins in fungi. The UniProt annotation explicitly uses GO:0005886. While D is not strictly wrong in a colloquial sense, B is the more precise and conventionally correct GO term."
  },
  "important_caveats": [
    "The GO annotation for plasma membrane carries evidence code IEA:UniProtKB-SubCell (inferred from electronic annotation based on the UniProt subcellular location comment), while the underlying subcellular location comment has experimental evidence (ECO:0000269) from PubMed:38649409.",
    "The UniProt topology annotation 'Multi-pass membrane protein' uses evidence code ECO:0000255 (sequence analysis), not direct experimental determination of membrane topology.",
    "The protein is from a fungus (Arthrobotrys oligospora); the 'plasma membrane' vs 'cell surface' distinction is relevant in fungal biology where a cell wall lies outside the plasma membrane.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what could be inferred from the sequence and general biological knowledge."
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

**Accession:** `G1X9E2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 45. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38649409","source":"PubMed"}],"value":"Relocalizes to the vacuole following stimulation by ligand"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38649409","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1X9E2.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:30.739464+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `d672d0bdd6e6d87681068eb4f338f9f4a6f7cf51e1400211480752ecd223995f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 43-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:38649409};
CC       Multi-pass membrane protein {ECO:0000255}. Note=Relocalizes to the
CC       vacuole following stimulation by ligand. {ECO:0000269|PubMed:38649409}.
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1X9E2?format=txt&versions=45)  
**Locator:** `lines 69-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:28:32.723564+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `e35d509b45ea64e3eac1fedae5691280c0fa8c7205a8651df542bc73ee054a3f`.

### Evidence GO2

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 54. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
