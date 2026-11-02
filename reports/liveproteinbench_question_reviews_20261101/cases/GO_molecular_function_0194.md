# GO_molecular_function_0194

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — hydrolase activity, acting on ester bonds

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTHWAFSPIQPGAARNMAAWQIAGKKDGPYQIDVSWPLTWSESGDASGKSANAVYLVDGNALFLTATETLRRRESHRPSETGTVVIAIGYPITDSVFSPRRSYDLTPPCDHYIPPEGPDGSPKPEAHGGADEFLTFIAEIVRPFVELKVFPRVSFGRTALFGHSYGGLFALHALFTKPSSFDVYLAASPSIWWNNRSILTEARRFISGAALFSSAHPVLRLSFGSREQYPVRQRVESDEMFKRRQRAAEQRRMNDNCEELYSELLASGRLCKLEVKEYLDEDHGSVIGPALSGGIMFLSNLSA

[Multiple Choices]
A. holo-[acyl-carrier-protein] synthase activity
B. U6 snRNA (guanine-N(2))-methyltransferase activity
C. peptidyl-arginine 3-dioxygenase activity
D. hydrolase activity, acting on ester bonds
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

> The sequence exactly matches the historical UniProt entry annotated as a siderophore enterobactin esterase. Its reported catalytic reaction hydrolyzes enterobactin, supporting the broader GO function of hydrolysis of ester bonds. The record attributes the functional and catalytic-activity evidence to an experimental publication.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a GHSYG segment matching the G-X-S-X-G pattern commonly associated with serine hydrolases. That offers a concrete clue for ester-bond hydrolase activity, while the other choices describe phosphopantetheinyl transfer, RNA methylation, or 2-oxoglutarate-dependent arginine hydroxylation, for which the sequence provides no similarly compelling signature.


**Missing item-specific fact**

> Identifying enterobactin as the particular substrate would require item-specific functional information not supplied in the question; that specificity is not needed to distinguish the broad ester-hydrolase choice.


**Reason**

> A sequence motif supports the broad catalytic class among these options. This does not independently establish the exact substrate or experimental characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options name distinct molecular functions, and the sequence's serine-hydrolase-like motif supports D at the broad level asked.


### Important caveats

- The sequence match is to a historical record; the author's exact data snapshot is unknown.
- The enterobactin substrate specificity comes from reviewer-only evidence and is not inferable with confidence from the supplied sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GHSYG segment matching the G-X-S-X-G pattern commonly associated with serine hydrolases. That offers a concrete clue for ester-bond hydrolase activity, while the other choices describe phosphopantetheinyl transfer, RNA methylation, or 2-oxoglutarate-dependent arginine hydroxylation, for which the sequence provides no similarly compelling signature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Identifying enterobactin as the particular substrate would require item-specific functional information not supplied in the question; that specificity is not needed to distinguish the broad ester-hydrolase choice.",
    "reason": "A sequence motif supports the broad catalytic class among these options. This does not independently establish the exact substrate or experimental characterization."
  },
  "case_id": "GO_molecular_function_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt entry annotated as a siderophore enterobactin esterase. Its reported catalytic reaction hydrolyzes enterobactin, supporting the broader GO function of hydrolysis of ester bonds. The record attributes the functional and catalytic-activity evidence to an experimental publication."
  },
  "important_caveats": [
    "The sequence match is to a historical record; the author's exact data snapshot is unknown.",
    "The enterobactin substrate specificity comes from reviewer-only evidence and is not inferable with confidence from the supplied sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options name distinct molecular functions, and the sequence's serine-hydrolase-like motif supports D at the broad level asked."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt entry annotated as a siderophore enterobactin esterase. Its reported catalytic reaction hydrolyzes enterobactin, supporting the broader GO function of hydrolysis of ester bonds. The record attributes the functional and catalytic-activity evidence to an experimental publication.",
    "evidence_ids": ["H1", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a GHSYG segment matching the G-X-S-X-G pattern commonly associated with serine hydrolases. That offers a concrete clue for ester-bond hydrolase activity, while the other choices describe phosphopantetheinyl transfer, RNA methylation, or 2-oxoglutarate-dependent arginine hydroxylation, for which the sequence provides no similarly compelling signature.",
    "missing_item_specific_fact": "Identifying enterobactin as the particular substrate would require item-specific functional information not supplied in the question; that specificity is not needed to distinguish the broad ester-hydrolase choice.",
    "reason": "A sequence motif supports the broad catalytic class among these options. This does not independently establish the exact substrate or experimental characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options name distinct molecular functions, and the sequence's serine-hydrolase-like motif supports D at the broad level asked."
  },
  "important_caveats": [
    "The sequence match is to a historical record; the author's exact data snapshot is unknown.",
    "The enterobactin substrate specificity comes from reviewer-only evidence and is not inferable with confidence from the supplied sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q5AV79, ESTA_EMENI) is experimentally characterized as a siderophore enterobactin esterase (EC 3.1.-.-) by X-ray crystallography at 1.75 Å and biochemical assays (PubMed:30070018, ECO:0000269). The GO annotation GO:0016788 (hydrolase activity, acting on ester bonds) is directly assigned. The catalytic reaction (enterobactin + 3 H2O → 3 N-(2,3-dihydroxybenzoyl)-L-serine + 2 H+) confirms ester-bond hydrolysis. Sequence match is exact (303 AA, identical SHA256).

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a GHS motif (in 'GRTALFGHSYGGLFALHALFTK') characteristic of the nucleophilic serine at the α/β-hydrolase fold elbow (GxSxG-like motif). A plausible catalytic triad can be identified: Ser (GHS), His (in 'EAHGGADEFLTF'), and Asp (in 'GAD'), consistent with a serine esterase architecture. In contrast, option A (phosphotransferase, EC 2.7.8.7) requires CoA-binding and phosphopantetheinyl-transfer motifs absent here; option B (methyltransferase) requires a Rossmann-fold with VIGXG/DXXG motifs not present; option C (2-oxoglutarate-dependent dioxygenase) requires the HxD/E…H iron-binding motifs of the 2-OG dioxygenase fold, also absent. The presence of the GHS nucleophile elbow and absence of motifs diagnostic of the other three enzyme classes provides a concrete structural-biology argument favoring D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GHS nucleophilic-elbow motif and the apparent Ser-His-Asp catalytic triad provide identifiable sequence-level hallmarks of an α/β-hydrolase-fold serine esterase. The absence of Rossmann-fold, 2-OG dioxygenase, and phosphotransferase motifs further discriminates against options B, C, and A. While pinpointing the exact substrate (enterobactin) would require lookup, the broad GO category 'hydrolase activity, acting on ester bonds' is inferable from these structural motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GHS nucleophile-elbow motif and potential catalytic triad uniquely point toward a serine esterase among the four choices. None of the other three options' diagnostic motifs (Rossmann-fold, 2-OG dioxygenase HxD/E…H, phosphopantetheinyl-transferase) are present in the sequence.


### Important caveats

- The GO annotation GO:0016788 is assigned via IBA:GO_Central (inference by biological aspect), but the underlying evidence is experimental (ECO:0000269, PubMed:30070018, X-ray crystallography + biochemical characterization).
- The GHS motif is a strong but not absolutely exclusive indicator of α/β-hydrolases; however, combined with the absence of motifs for the other three options, it provides a defensible discriminative argument.
- The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning argument relies on general enzyme-structure knowledge applied to the supplied sequence.
- The entry was first released in January 2026, which may postdate the benchmark construction; however, the sequence itself is unchanged (version 1 since 2005).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GHS motif (in 'GRTALFGHSYGGLFALHALFTK') characteristic of the nucleophilic serine at the α/β-hydrolase fold elbow (GxSxG-like motif). A plausible catalytic triad can be identified: Ser (GHS), His (in 'EAHGGADEFLTF'), and Asp (in 'GAD'), consistent with a serine esterase architecture. In contrast, option A (phosphotransferase, EC 2.7.8.7) requires CoA-binding and phosphopantetheinyl-transfer motifs absent here; option B (methyltransferase) requires a Rossmann-fold with VIGXG/DXXG motifs not present; option C (2-oxoglutarate-dependent dioxygenase) requires the HxD/E…H iron-binding motifs of the 2-OG dioxygenase fold, also absent. The presence of the GHS nucleophile elbow and absence of motifs diagnostic of the other three enzyme classes provides a concrete structural-biology argument favoring D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GHS nucleophilic-elbow motif and the apparent Ser-His-Asp catalytic triad provide identifiable sequence-level hallmarks of an α/β-hydrolase-fold serine esterase. The absence of Rossmann-fold, 2-OG dioxygenase, and phosphotransferase motifs further discriminates against options B, C, and A. While pinpointing the exact substrate (enterobactin) would require lookup, the broad GO category 'hydrolase activity, acting on ester bonds' is inferable from these structural motifs."
  },
  "case_id": "GO_molecular_function_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein (Q5AV79, ESTA_EMENI) is experimentally characterized as a siderophore enterobactin esterase (EC 3.1.-.-) by X-ray crystallography at 1.75 Å and biochemical assays (PubMed:30070018, ECO:0000269). The GO annotation GO:0016788 (hydrolase activity, acting on ester bonds) is directly assigned. The catalytic reaction (enterobactin + 3 H2O → 3 N-(2,3-dihydroxybenzoyl)-L-serine + 2 H+) confirms ester-bond hydrolysis. Sequence match is exact (303 AA, identical SHA256)."
  },
  "important_caveats": [
    "The GO annotation GO:0016788 is assigned via IBA:GO_Central (inference by biological aspect), but the underlying evidence is experimental (ECO:0000269, PubMed:30070018, X-ray crystallography + biochemical characterization).",
    "The GHS motif is a strong but not absolutely exclusive indicator of α/β-hydrolases; however, combined with the absence of motifs for the other three options, it provides a defensible discriminative argument.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning argument relies on general enzyme-structure knowledge applied to the supplied sequence.",
    "The entry was first released in January 2026, which may postdate the benchmark construction; however, the sequence itself is unchanged (version 1 since 2005)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GHS nucleophile-elbow motif and potential catalytic triad uniquely point toward a serine esterase among the four choices. None of the other three options' diagnostic motifs (Rossmann-fold, 2-OG dioxygenase HxD/E…H, phosphopantetheinyl-transferase) are present in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q5AV79, ESTA_EMENI) is experimentally characterized as a siderophore enterobactin esterase (EC 3.1.-.-) by X-ray crystallography at 1.75 Å and biochemical assays (PubMed:30070018, ECO:0000269). The GO annotation GO:0016788 (hydrolase activity, acting on ester bonds) is directly assigned. The catalytic reaction (enterobactin + 3 H2O → 3 N-(2,3-dihydroxybenzoyl)-L-serine + 2 H+) confirms ester-bond hydrolysis. Sequence match is exact (303 AA, identical SHA256).",
    "evidence_ids": ["H1", "H2", "H3", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a GHS motif (in 'GRTALFGHSYGGLFALHALFTK') characteristic of the nucleophilic serine at the α/β-hydrolase fold elbow (GxSxG-like motif). A plausible catalytic triad can be identified: Ser (GHS), His (in 'EAHGGADEFLTF'), and Asp (in 'GAD'), consistent with a serine esterase architecture. In contrast, option A (phosphotransferase, EC 2.7.8.7) requires CoA-binding and phosphopantetheinyl-transfer motifs absent here; option B (methyltransferase) requires a Rossmann-fold with VIGXG/DXXG motifs not present; option C (2-oxoglutarate-dependent dioxygenase) requires the HxD/E…H iron-binding motifs of the 2-OG dioxygenase fold, also absent. The presence of the GHS nucleophile elbow and absence of motifs diagnostic of the other three enzyme classes provides a concrete structural-biology argument favoring D.",
    "missing_item_specific_fact": "",
    "reason": "The GHS nucleophilic-elbow motif and the apparent Ser-His-Asp catalytic triad provide identifiable sequence-level hallmarks of an α/β-hydrolase-fold serine esterase. The absence of Rossmann-fold, 2-OG dioxygenase, and phosphotransferase motifs further discriminates against options B, C, and A. While pinpointing the exact substrate (enterobactin) would require lookup, the broad GO category 'hydrolase activity, acting on ester bonds' is inferable from these structural motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GHS nucleophile-elbow motif and potential catalytic triad uniquely point toward a serine esterase among the four choices. None of the other three options' diagnostic motifs (Rossmann-fold, 2-OG dioxygenase HxD/E…H, phosphopantetheinyl-transferase) are present in the sequence."
  },
  "important_caveats": [
    "The GO annotation GO:0016788 is assigned via IBA:GO_Central (inference by biological aspect), but the underlying evidence is experimental (ECO:0000269, PubMed:30070018, X-ray crystallography + biochemical characterization).",
    "The GHS motif is a strong but not absolutely exclusive indicator of α/β-hydrolases; however, combined with the absence of motifs for the other three options, it provides a defensible discriminative argument.",
    "The reviewer-only UniProt evidence was not available to the evaluated model; the reasoning argument relies on general enzyme-structure knowledge applied to the supplied sequence.",
    "The entry was first released in January 2026, which may postdate the benchmark construction; however, the sequence itself is unchanged (version 1 since 2005)."
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

**Accession:** `Q5AV79` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current unavailable.  
**Historical cutoff:** 2026-05-07; archived entry version 95. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Current UniProt source unavailable: HTTPError: HTTP Error 500: Internal Server Error
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5AV79?format=txt&versions=95)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:31:11.699496+00:00.  

```text
ID   ESTA_EMENI              Reviewed;         303 AA.
AC   Q5AV79; C8VDS2;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   26-APR-2005, sequence version 1.
DT   28-JAN-2026, entry version 95.
DE   RecName: Full=Siderophore enterobactin esterase {ECO:0000303|PubMed:30070018};
DE            EC=3.1.-.- {ECO:0000269|PubMed:30070018};
GN   Name=estA {ECO:0000303|PubMed:30070018}; ORFNames=ANIA_07801;
OS   Emericella nidulans (strain FGSC A4 / ATCC 38163 / CBS 112.46 / NRRL 194 /
OS   M139) (Aspergillus nidulans).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Nidulantes.
OX   NCBI_TaxID=227321;
```

Source SHA-256: `ee551bd56cb3410ba539075dc7f0e4ae8b31c5f6778ce8e49d921dc022521f4a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5AV79?format=txt&versions=95)  
**Locator:** `lines 54-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:31:11.699496+00:00.  

```text
RN   [3] {ECO:0007744|PDB:6GUO}
RP   X-RAY CRYSTALLOGRAPHY (1.75 ANGSTROMS) OF 2-303, SUBUNIT, FUNCTION,
RP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND DOMAIN.
RX   PubMed=30070018; DOI=10.1002/anie.201807093;
RA   Ecker F., Haas H., Groll M., Huber E.M.;
RT   "Iron Scavenging in Aspergillus Species: Structural and Biochemical
RT   Insights into Fungal Siderophore Esterases.";
RL   Angew. Chem. Int. Ed. 57:14624-14629(2018).
```

Source SHA-256: `ee551bd56cb3410ba539075dc7f0e4ae8b31c5f6778ce8e49d921dc022521f4a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5AV79?format=txt&versions=95)  
**Locator:** `lines 62-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:31:11.699496+00:00.  

```text
CC   -!- FUNCTION: Displays specific enterobactin (ENB) esterase activity
CC       required for intracellular release of iron. Enterobactin is a
CC       xenosiderophore that is selectively produced by Gram-negative
CC       Enterobacteriaceae (PubMed:30070018). The affinity for enterobactin is
CC       quite high, potentially due to the low natural abundance of this
CC       xenosiderophore in fungal habitats (PubMed:30070018). Does not
CC       hydrolyze triacetylfusarinine C (TAFC) (PubMed:30070018).
CC       {ECO:0000269|PubMed:30070018}.
```

Source SHA-256: `ee551bd56cb3410ba539075dc7f0e4ae8b31c5f6778ce8e49d921dc022521f4a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5AV79?format=txt&versions=95)  
**Locator:** `lines 70-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:31:11.699496+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=enterobactin + 3 H2O = 3 N-(2,3-dihydroxybenzoyl)-L-serine + 2
CC         H(+); Xref=Rhea:RHEA:28018, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:58154, ChEBI:CHEBI:77805;
CC         Evidence={ECO:0000269|PubMed:30070018};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:28019;
CC         Evidence={ECO:0000269|PubMed:30070018};
```

Source SHA-256: `ee551bd56cb3410ba539075dc7f0e4ae8b31c5f6778ce8e49d921dc022521f4a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5AV79?format=txt&versions=95)  
**Locator:** `lines 110-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:31:11.699496+00:00.  

```text
DR   GO; GO:0016788; F:hydrolase activity, acting on ester bonds; IBA:GO_Central.
```

Source SHA-256: `ee551bd56cb3410ba539075dc7f0e4ae8b31c5f6778ce8e49d921dc022521f4a`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 130194-130208`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016788
name: hydrolase activity, acting on ester bonds
namespace: molecular_function
def: "Catalysis of the hydrolysis of any ester bond." [GOC:jl]
subset: goslim_chembl
synonym: "esterase activity" EXACT []
xref: EC:3.1.-.-
xref: Reactome:R-HSA-162729 "uPAR-acyl-GPI + H2O -> uPAR + long-chain fatty acid"
xref: Reactome:R-HSA-9023617 "Butyrylcholinesterase hydrolyzes acyl Ghrelin"
xref: Reactome:R-HSA-9023619 "Platelet-activating factor acetylhydrolase (PLA2G7) hydrolyzes acyl Ghrelin"
xref: Reactome:R-HSA-9749609 "BCHE hydrolyzes ASA-"
is_a: GO:0016787 ! hydrolase activity
property_value: skos:exactMatch EC:3.1.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 194. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
