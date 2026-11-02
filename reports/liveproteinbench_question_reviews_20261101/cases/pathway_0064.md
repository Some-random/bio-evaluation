# pathway_0064

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATPQFSCLLPAFFLLVVFLFLLIKELRRYKSPKTTQKLPPGPPMLPIIGNLHQMASSLPHQNLKKLADKYGPLMHLKLGEISAVAVSSPRLAKEVLQTRGLAFADRPQSVVAKLMLHNCLGVTFSRYGDYWRQLRQIFAMELLSSKSVQSFSTIMEDELFAMVKSIESEAGRPIILADKLISYLYATLSRATLGRVCKGKETLIEVTGETLALSGAQSLEDIFPSVKIFAYLNPLRPKVRKLFNRIDGVLEDIINQQEKKLLSARVDNDQLQPEENDMLSVLLKLRNGKDSKVQVTNNDIKAIIFELFLAGTVGSSTTVEWAMSEMMKNPKVMEKAQHEVREVLKGKKRICQSDIQKLSYLKLVVKETLRLHPPAPLLFPRECRGQCEVDGYTIPAKAMVMVNCWALGRDPEHWIEADKFEPERFKNSSIDFIGNHFEYIPFGAGRRICPGISFGATNVELLLAALLYHFDWELAGGMHPKDLDMLELFGPGCTRKNPLSVIPSICIPSHDDN

[Multiple Choices]
A. ergot alkaloid biosynthesis. .
B. Alkaloid biosynthesis. .
C. L-homoserine from L-aspartate: step 1/3. .
D. nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1. .
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

> The supplied sequence exactly matches the UniProt entry annotated as Alstonine synthase, with the pathway given as alkaloid biosynthesis. The pathway annotation cites experimental evidence and a publication reporting function and pathway; this supports B, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region and conserved features are consistent with a membrane-associated cytochrome P450, but that general class information does not identify its specific substrate or pathway.


**Missing item-specific fact**

> The protein-specific annotation or experimental finding that this sequence encodes Alstonine synthase, which functions in alkaloid biosynthesis.


**Reason**

> The sequence alone does not meaningfully distinguish alkaloid biosynthesis from other possible P450 functions, or establish the specific pathway. Choosing B depends on protein-specific functional information absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports broad alkaloid biosynthesis. Although ergot alkaloid biosynthesis is a narrower category of alkaloid biosynthesis in general, the evidence identifies this protein as an Alstonia alkaloid-pathway enzyme, not an ergot-pathway enzyme.


### Important caveats

- The UniProt record and its sequence match are reviewer-only evidence, not information provided to the evaluated model.
- The cited evidence supports the annotation, but the underlying primary study was not independently validated in the supplied materials.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region and conserved features are consistent with a membrane-associated cytochrome P450, but that general class information does not identify its specific substrate or pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or experimental finding that this sequence encodes Alstonine synthase, which functions in alkaloid biosynthesis.",
    "reason": "The sequence alone does not meaningfully distinguish alkaloid biosynthesis from other possible P450 functions, or establish the specific pathway. Choosing B depends on protein-specific functional information absent from the input."
  },
  "case_id": "pathway_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as Alstonine synthase, with the pathway given as alkaloid biosynthesis. The pathway annotation cites experimental evidence and a publication reporting function and pathway; this supports B, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt record and its sequence match are reviewer-only evidence, not information provided to the evaluated model.",
    "The cited evidence supports the annotation, but the underlying primary study was not independently validated in the supplied materials."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports broad alkaloid biosynthesis. Although ergot alkaloid biosynthesis is a narrower category of alkaloid biosynthesis in general, the evidence identifies this protein as an Alstonia alkaloid-pathway enzyme, not an ergot-pathway enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as Alstonine synthase, with the pathway given as alkaloid biosynthesis. The pathway annotation cites experimental evidence and a publication reporting function and pathway; this supports B, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region and conserved features are consistent with a membrane-associated cytochrome P450, but that general class information does not identify its specific substrate or pathway.",
    "missing_item_specific_fact": "The protein-specific annotation or experimental finding that this sequence encodes Alstonine synthase, which functions in alkaloid biosynthesis.",
    "reason": "The sequence alone does not meaningfully distinguish alkaloid biosynthesis from other possible P450 functions, or establish the specific pathway. Choosing B depends on protein-specific functional information absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports broad alkaloid biosynthesis. Although ergot alkaloid biosynthesis is a narrower category of alkaloid biosynthesis in general, the evidence identifies this protein as an Alstonia alkaloid-pathway enzyme, not an ergot-pathway enzyme."
  },
  "important_caveats": [
    "The UniProt record and its sequence match are reviewer-only evidence, not information provided to the evaluated model.",
    "The cited evidence supports the annotation, but the underlying primary study was not independently validated in the supplied materials."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7LUJ4 (Alstonine synthase, Cytochrome P450 AS, EC 1.14.19.-) from Alstonia scholaris is annotated with pathway 'Alkaloid biosynthesis' backed by experimental evidence (ECO:0000269, PubMed:36349266). The benchmark sequence matches the source sequence exactly (SHA256 match confirmed in both current and historical snapshots). Option B ('Alkaloid biosynthesis') matches the UniProt pathway annotation verbatim.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical Cytochrome P450 heme-binding motif 'FGAGRRICPG' (visible near the C-terminus: '...IPFGAGRRICPGISFGATNVELLLAALLYHFDWELAGGMHPKDLDMLELFGPGCTRKNPLSVIPSICIPSHDDN'), identifying the protein as a P450 monooxygenase. Plant P450s are well-known catalysts in secondary metabolite/alkaloid biosynthesis. Options C (L-aspartate → L-homoserine) and D (NAD biosynthesis) involve entirely different enzyme classes (aspartate kinase, nicotinamide phosphoribosyltransferase) and are incompatible with a P450. Between A ('ergot alkaloid biosynthesis') and B ('Alkaloid biosynthesis'): ergot alkaloids (e.g., ergotamine, ergometrine) are specifically produced by fungi of the genus Claviceps via a dedicated fungal gene cluster; they are not a plant pathway. A plant P450 from a member of Apocynaceae (a family rich in monoterpene indole alkaloids) would not participate in ergot alkaloid biosynthesis. General biological knowledge that ergot alkaloids are fungal-specific and that plant P450s participate in broader alkaloid pathways supports selecting B over A.


**Missing item-specific fact**

> None strictly required. The distinction between ergot alkaloid biosynthesis (fungal) and general alkaloid biosynthesis (plant) rests on well-established biological taxonomy of alkaloid classes. The exact UniProt pathway label 'Alkaloid biosynthesis' is a database term, but the biological reasoning (P450 + plant + not ergot) meaningfully narrows the answer.


**Reason**

> A model with general biological knowledge can (1) identify the P450 heme-binding motif from the sequence, (2) rule out aspartate and NAD pathways (C, D) because those do not involve P450s, and (3) distinguish ergot alkaloid biosynthesis (a specifically fungal pathway) from the broader plant alkaloid biosynthesis category. This constitutes a concrete biological argument grounded in the supplied sequence and general knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option A (ergot alkaloid biosynthesis) is distinguishable from B via the well-known fact that ergot alkaloids are fungal-specific. Options C and D involve non-P450 enzymes and are clearly incompatible. Only B remains defensible.


### Important caveats

- The UniProt pathway annotation 'Alkaloid biosynthesis' is a broad UniProt pathway term; a more specific name (e.g., 'monoterpene indole alkaloid biosynthesis') would also be biologically accurate but is not among the choices.
- The P450 identification relies on the FGAGRRICPG motif being recognizable; a model unfamiliar with this motif would struggle to rule out C and D from sequence alone.
- The distinction between A and B depends on knowing that ergot alkaloids are a fungal-specific class, which is standard biochemistry knowledge but still a factual recall point.
- All reviewer evidence is annotated with experimental evidence codes (ECO:0000269), confirming the pathway assignment is experimentally supported, not merely computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical Cytochrome P450 heme-binding motif 'FGAGRRICPG' (visible near the C-terminus: '...IPFGAGRRICPGISFGATNVELLLAALLYHFDWELAGGMHPKDLDMLELFGPGCTRKNPLSVIPSICIPSHDDN'), identifying the protein as a P450 monooxygenase. Plant P450s are well-known catalysts in secondary metabolite/alkaloid biosynthesis. Options C (L-aspartate → L-homoserine) and D (NAD biosynthesis) involve entirely different enzyme classes (aspartate kinase, nicotinamide phosphoribosyltransferase) and are incompatible with a P450. Between A ('ergot alkaloid biosynthesis') and B ('Alkaloid biosynthesis'): ergot alkaloids (e.g., ergotamine, ergometrine) are specifically produced by fungi of the genus Claviceps via a dedicated fungal gene cluster; they are not a plant pathway. A plant P450 from a member of Apocynaceae (a family rich in monoterpene indole alkaloids) would not participate in ergot alkaloid biosynthesis. General biological knowledge that ergot alkaloids are fungal-specific and that plant P450s participate in broader alkaloid pathways supports selecting B over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The distinction between ergot alkaloid biosynthesis (fungal) and general alkaloid biosynthesis (plant) rests on well-established biological taxonomy of alkaloid classes. The exact UniProt pathway label 'Alkaloid biosynthesis' is a database term, but the biological reasoning (P450 + plant + not ergot) meaningfully narrows the answer.",
    "reason": "A model with general biological knowledge can (1) identify the P450 heme-binding motif from the sequence, (2) rule out aspartate and NAD pathways (C, D) because those do not involve P450s, and (3) distinguish ergot alkaloid biosynthesis (a specifically fungal pathway) from the broader plant alkaloid biosynthesis category. This constitutes a concrete biological argument grounded in the supplied sequence and general knowledge."
  },
  "case_id": "pathway_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7LUJ4 (Alstonine synthase, Cytochrome P450 AS, EC 1.14.19.-) from Alstonia scholaris is annotated with pathway 'Alkaloid biosynthesis' backed by experimental evidence (ECO:0000269, PubMed:36349266). The benchmark sequence matches the source sequence exactly (SHA256 match confirmed in both current and historical snapshots). Option B ('Alkaloid biosynthesis') matches the UniProt pathway annotation verbatim."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Alkaloid biosynthesis' is a broad UniProt pathway term; a more specific name (e.g., 'monoterpene indole alkaloid biosynthesis') would also be biologically accurate but is not among the choices.",
    "The P450 identification relies on the FGAGRRICPG motif being recognizable; a model unfamiliar with this motif would struggle to rule out C and D from sequence alone.",
    "The distinction between A and B depends on knowing that ergot alkaloids are a fungal-specific class, which is standard biochemistry knowledge but still a factual recall point.",
    "All reviewer evidence is annotated with experimental evidence codes (ECO:0000269), confirming the pathway assignment is experimentally supported, not merely computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (ergot alkaloid biosynthesis) is distinguishable from B via the well-known fact that ergot alkaloids are fungal-specific. Options C and D involve non-P450 enzymes and are clearly incompatible. Only B remains defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7LUJ4 (Alstonine synthase, Cytochrome P450 AS, EC 1.14.19.-) from Alstonia scholaris is annotated with pathway 'Alkaloid biosynthesis' backed by experimental evidence (ECO:0000269, PubMed:36349266). The benchmark sequence matches the source sequence exactly (SHA256 match confirmed in both current and historical snapshots). Option B ('Alkaloid biosynthesis') matches the UniProt pathway annotation verbatim.",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical Cytochrome P450 heme-binding motif 'FGAGRRICPG' (visible near the C-terminus: '...IPFGAGRRICPGISFGATNVELLLAALLYHFDWELAGGMHPKDLDMLELFGPGCTRKNPLSVIPSICIPSHDDN'), identifying the protein as a P450 monooxygenase. Plant P450s are well-known catalysts in secondary metabolite/alkaloid biosynthesis. Options C (L-aspartate → L-homoserine) and D (NAD biosynthesis) involve entirely different enzyme classes (aspartate kinase, nicotinamide phosphoribosyltransferase) and are incompatible with a P450. Between A ('ergot alkaloid biosynthesis') and B ('Alkaloid biosynthesis'): ergot alkaloids (e.g., ergotamine, ergometrine) are specifically produced by fungi of the genus Claviceps via a dedicated fungal gene cluster; they are not a plant pathway. A plant P450 from a member of Apocynaceae (a family rich in monoterpene indole alkaloids) would not participate in ergot alkaloid biosynthesis. General biological knowledge that ergot alkaloids are fungal-specific and that plant P450s participate in broader alkaloid pathways supports selecting B over A.",
    "missing_item_specific_fact": "None strictly required. The distinction between ergot alkaloid biosynthesis (fungal) and general alkaloid biosynthesis (plant) rests on well-established biological taxonomy of alkaloid classes. The exact UniProt pathway label 'Alkaloid biosynthesis' is a database term, but the biological reasoning (P450 + plant + not ergot) meaningfully narrows the answer.",
    "reason": "A model with general biological knowledge can (1) identify the P450 heme-binding motif from the sequence, (2) rule out aspartate and NAD pathways (C, D) because those do not involve P450s, and (3) distinguish ergot alkaloid biosynthesis (a specifically fungal pathway) from the broader plant alkaloid biosynthesis category. This constitutes a concrete biological argument grounded in the supplied sequence and general knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option A (ergot alkaloid biosynthesis) is distinguishable from B via the well-known fact that ergot alkaloids are fungal-specific. Options C and D involve non-P450 enzymes and are clearly incompatible. Only B remains defensible."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Alkaloid biosynthesis' is a broad UniProt pathway term; a more specific name (e.g., 'monoterpene indole alkaloid biosynthesis') would also be biologically accurate but is not among the choices.",
    "The P450 identification relies on the FGAGRRICPG motif being recognizable; a model unfamiliar with this motif would struggle to rule out C and D from sequence alone.",
    "The distinction between A and B depends on knowing that ergot alkaloids are a fungal-specific class, which is standard biochemistry knowledge but still a factual recall point.",
    "All reviewer evidence is annotated with experimental evidence codes (ECO:0000269), confirming the pathway assignment is experimentally supported, not merely computational."
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

**Accession:** `A0A9E7LUJ4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
"A0A9E7LUJ4"
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Cytochrome P450 AS"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.14.19.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Alstonine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsAS"}]}}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUJ4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:52.163393+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65382.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `59fe739ed168944070cd38e29550519331b1495ba5653a150fa3d35624899435`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)  
**Locator:** `lines 17-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.040905+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:URS65382.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=36349266; DOI=10.1039/d2sc03612f;
RA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;
RT   "Deciphering and reprogramming the cyclization regioselectivity in
RT   bifurcation of indole alkaloid biosynthesis.";
RL   Chem. Sci. 13:12389-12395(2022).
```

Source SHA-256: `cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUJ4?format=txt&versions=13)  
**Locator:** `lines 44-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.040905+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:36349266}.
```

Source SHA-256: `cc693d1dbb0e42a4104ad818ad2836ecd8bdd9e71e50b40a970a3f13d0b5e109`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
