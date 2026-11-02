# GO_cellular_component_0152

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAAFPPGGTFFDTLKRSFTDVPVESGKIATTQFLEACESLTTLFDVLGSTAFKPVKSDMTGNIKKIRDRQLAAPVDSETLQDLVRNELATKKHTATEGLVWLNRALDFTAQALRQNLTNSGEEVSVSFRSAYGNTLSKHHSFMIKPIFSAAMSATPYRKDFYAKLGDDQARVEKELGVWLSSLENIVKILNDFLASKEAKW

[Multiple Choices]
A. membrane
B. chromosome
C. ciliary basal body
D. peroxisomal matrix
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

> The exact-sequence-matched UniProt entry annotates membrane (GO:0016020), supporting choice A at the annotation level. This is an electronic TreeGrafter inference, not experimental localization evidence; the same entry also annotates cytosol, so it does not establish membrane as the protein’s exclusive or primary location.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is not visibly dominated by a long hydrophobic transmembrane segment or an obvious organelle-targeting signal. That may argue against an integral membrane protein, but it cannot distinguish a peripheral membrane-associated protein from other soluble localizations.


**Missing item-specific fact**

> The protein-specific localization annotation or experimental evidence is needed; identifying this sequence as a glycolipid transfer protein may also suggest membrane association, but that identity and its localization are not supplied in the question.


**Reason**

> The sequence and options provide no reliable basis for inferring the specific membrane association. The available membrane assignment comes from item-specific annotation, and it is computational rather than experimental.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option has comparable supporting evidence. However, the matched entry also annotates cytosol, which is not offered, and the question gives no basis for treating membrane as the primary rather than an additional location.


### Important caveats

- The matched UniProt membrane and cytosol annotations use IEA:TreeGrafter evidence; they should not be described as experimental findings.
- The historical sequence match is established, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is not visibly dominated by a long hydrophobic transmembrane segment or an obvious organelle-targeting signal. That may argue against an integral membrane protein, but it cannot distinguish a peripheral membrane-associated protein from other soluble localizations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence is needed; identifying this sequence as a glycolipid transfer protein may also suggest membrane association, but that identity and its localization are not supplied in the question.",
    "reason": "The sequence and options provide no reliable basis for inferring the specific membrane association. The available membrane assignment comes from item-specific annotation, and it is computational rather than experimental."
  },
  "case_id": "GO_cellular_component_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt entry annotates membrane (GO:0016020), supporting choice A at the annotation level. This is an electronic TreeGrafter inference, not experimental localization evidence; the same entry also annotates cytosol, so it does not establish membrane as the protein’s exclusive or primary location."
  },
  "important_caveats": [
    "The matched UniProt membrane and cytosol annotations use IEA:TreeGrafter evidence; they should not be described as experimental findings.",
    "The historical sequence match is established, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option has comparable supporting evidence. However, the matched entry also annotates cytosol, which is not offered, and the question gives no basis for treating membrane as the primary rather than an additional location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt entry annotates membrane (GO:0016020), supporting choice A at the annotation level. This is an electronic TreeGrafter inference, not experimental localization evidence; the same entry also annotates cytosol, so it does not establish membrane as the protein’s exclusive or primary location.",
    "evidence_ids": ["C6", "H4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is not visibly dominated by a long hydrophobic transmembrane segment or an obvious organelle-targeting signal. That may argue against an integral membrane protein, but it cannot distinguish a peripheral membrane-associated protein from other soluble localizations.",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence is needed; identifying this sequence as a glycolipid transfer protein may also suggest membrane association, but that identity and its localization are not supplied in the question.",
    "reason": "The sequence and options provide no reliable basis for inferring the specific membrane association. The available membrane assignment comes from item-specific annotation, and it is computational rather than experimental."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option has comparable supporting evidence. However, the matched entry also annotates cytosol, which is not offered, and the question gives no basis for treating membrane as the primary rather than an additional location."
  },
  "important_caveats": [
    "The matched UniProt membrane and cytosol annotations use IEA:TreeGrafter evidence; they should not be described as experimental findings.",
    "The historical sequence match is established, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A223HDI2 (GLTP_AURME, a 201-aa Glycolipid transfer protein from Aureobasidium melanogenum) carries the GO annotation GO:0016020 C:membrane (evidence C6/H4), which directly matches option A. However, the evidence code is IEA:TreeGrafter (computational phylogenetic grafting, not experimental), and the same entry also annotates GO:0005829 C:cytosol with the identical evidence code (C5/H3). GLTPs are classically soluble cytosolic proteins that transiently interact with membrane surfaces. The 'membrane' annotation is present and consistent with the protein's known membrane-interacting function, so the key is supported by the annotation, but it rests on computational inference rather than direct experimental localization data.

Citations as saved: [C6](#evidence-c6), [H4](#evidence-h4), [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three of the four options can be eliminated by general biological reasoning applied to the sequence and organism context. (1) Option C (ciliary basal body): the organism is Aureobasidium melanogenum, an Ascomycete fungus. Fungi lost cilia/flagella early in eukaryotic evolution; Ascomycota do not possess cilia or basal bodies, making this compartment biologically implausible. (2) Option D (peroxisomal matrix): peroxisomal matrix proteins require a C-terminal PTS1 signal (typically SKL or variants) or an N-terminal PTS2 signal. The C-terminus ends in '…LASKEAKW' with no PTS1 motif, and the N-terminus lacks a PTS2 tripeptide. (3) Option B (chromosome): the sequence shows no DNA-binding domain, no histone-fold motif, no HMG-box, and no other chromatin-associated structural feature. By elimination, option A (membrane) is the only remaining plausible compartment. Additionally, the sequence contains several amphipathic and moderately hydrophobic stretches (e.g., 'TTLFDVLGSTAFKP', 'SAAMSATPYRKDFYAKL') consistent with peripheral membrane association rather than a soluble-only protein, and glycolipid transfer proteins are well known to interact with membrane surfaces during lipid transfer.


**Missing item-specific fact**

> None that is essential. The positive identification of 'membrane' for a GLTP benefits from knowing that GLTPs are membrane-interacting proteins, but the elimination of B, C, and D is achievable through general cell biology (fungi lack cilia, peroxisomal targeting signals, DNA-binding motifs).


**Reason**

> The question is answerable through structured elimination using general biological knowledge: fungal biology rules out cilia, absence of PTS signals rules out peroxisomal matrix, absence of DNA-binding features rules out chromosome. The remaining option (membrane) is consistent with the protein's glycolipid-transfer function and its amphipathic sequence character. This constitutes meaningful reasoning grounds rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four provided options, only 'membrane' survives elimination. 'Cytosol' would arguably be the more precise primary localization for a GLTP (and is annotated in UniProt), but it is not offered as a choice. The GO term GO:0016020 'membrane' is extremely broad (any protein attached to or embedded in a lipid bilayer), so a peripheral membrane-interacting GLTP can legitimately be tagged 'membrane.' No other option is defensible given the organism (fungus, no cilia), the absence of targeting signals for peroxisomes or chromosomes, and the protein's known membrane-interacting biochemistry.


### Important caveats

- Both GO cellular-component annotations (membrane and cytosol) carry IEA:TreeGrafter evidence, i.e., computational phylogenetic inference, not experimental localization.
- GLTPs are canonically classified as soluble/cytosolic proteins that transiently engage membranes; calling 'membrane' the primary location is a simplification, though it is defensible under the broad GO:0016020 definition and given that 'cytosol' is not an option.
- The protein name 'Glycolipid transfer protein' is sourced from a literature reference (PubMed:32003433) on liamocin biosynthesis/transport, not from direct experimental subcellular fractionation of this specific protein.
- The identity of the protein (GLTP) is not provided in the question input; a model must infer function from sequence features or pattern recognition, which adds a layer of difficulty beyond pure compartment reasoning.
- The UniProt entry was first publicly released in February 2025; the benchmark author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three of the four options can be eliminated by general biological reasoning applied to the sequence and organism context. (1) Option C (ciliary basal body): the organism is Aureobasidium melanogenum, an Ascomycete fungus. Fungi lost cilia/flagella early in eukaryotic evolution; Ascomycota do not possess cilia or basal bodies, making this compartment biologically implausible. (2) Option D (peroxisomal matrix): peroxisomal matrix proteins require a C-terminal PTS1 signal (typically SKL or variants) or an N-terminal PTS2 signal. The C-terminus ends in '…LASKEAKW' with no PTS1 motif, and the N-terminus lacks a PTS2 tripeptide. (3) Option B (chromosome): the sequence shows no DNA-binding domain, no histone-fold motif, no HMG-box, and no other chromatin-associated structural feature. By elimination, option A (membrane) is the only remaining plausible compartment. Additionally, the sequence contains several amphipathic and moderately hydrophobic stretches (e.g., 'TTLFDVLGSTAFKP', 'SAAMSATPYRKDFYAKL') consistent with peripheral membrane association rather than a soluble-only protein, and glycolipid transfer proteins are well known to interact with membrane surfaces during lipid transfer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is essential. The positive identification of 'membrane' for a GLTP benefits from knowing that GLTPs are membrane-interacting proteins, but the elimination of B, C, and D is achievable through general cell biology (fungi lack cilia, peroxisomal targeting signals, DNA-binding motifs).",
    "reason": "The question is answerable through structured elimination using general biological knowledge: fungal biology rules out cilia, absence of PTS signals rules out peroxisomal matrix, absence of DNA-binding features rules out chromosome. The remaining option (membrane) is consistent with the protein's glycolipid-transfer function and its amphipathic sequence character. This constitutes meaningful reasoning grounds rather than pure lookup."
  },
  "case_id": "GO_cellular_component_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H4",
      "C5",
      "H3",
      "C4",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A223HDI2 (GLTP_AURME, a 201-aa Glycolipid transfer protein from Aureobasidium melanogenum) carries the GO annotation GO:0016020 C:membrane (evidence C6/H4), which directly matches option A. However, the evidence code is IEA:TreeGrafter (computational phylogenetic grafting, not experimental), and the same entry also annotates GO:0005829 C:cytosol with the identical evidence code (C5/H3). GLTPs are classically soluble cytosolic proteins that transiently interact with membrane surfaces. The 'membrane' annotation is present and consistent with the protein's known membrane-interacting function, so the key is supported by the annotation, but it rests on computational inference rather than direct experimental localization data."
  },
  "important_caveats": [
    "Both GO cellular-component annotations (membrane and cytosol) carry IEA:TreeGrafter evidence, i.e., computational phylogenetic inference, not experimental localization.",
    "GLTPs are canonically classified as soluble/cytosolic proteins that transiently engage membranes; calling 'membrane' the primary location is a simplification, though it is defensible under the broad GO:0016020 definition and given that 'cytosol' is not an option.",
    "The protein name 'Glycolipid transfer protein' is sourced from a literature reference (PubMed:32003433) on liamocin biosynthesis/transport, not from direct experimental subcellular fractionation of this specific protein.",
    "The identity of the protein (GLTP) is not provided in the question input; a model must infer function from sequence features or pattern recognition, which adds a layer of difficulty beyond pure compartment reasoning.",
    "The UniProt entry was first publicly released in February 2025; the benchmark author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided options, only 'membrane' survives elimination. 'Cytosol' would arguably be the more precise primary localization for a GLTP (and is annotated in UniProt), but it is not offered as a choice. The GO term GO:0016020 'membrane' is extremely broad (any protein attached to or embedded in a lipid bilayer), so a peripheral membrane-interacting GLTP can legitimately be tagged 'membrane.' No other option is defensible given the organism (fungus, no cilia), the absence of targeting signals for peroxisomes or chromosomes, and the protein's known membrane-interacting biochemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A223HDI2 (GLTP_AURME, a 201-aa Glycolipid transfer protein from Aureobasidium melanogenum) carries the GO annotation GO:0016020 C:membrane (evidence C6/H4), which directly matches option A. However, the evidence code is IEA:TreeGrafter (computational phylogenetic grafting, not experimental), and the same entry also annotates GO:0005829 C:cytosol with the identical evidence code (C5/H3). GLTPs are classically soluble cytosolic proteins that transiently interact with membrane surfaces. The 'membrane' annotation is present and consistent with the protein's known membrane-interacting function, so the key is supported by the annotation, but it rests on computational inference rather than direct experimental localization data.",
    "evidence_ids": ["C6", "H4", "C5", "H3", "C4", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three of the four options can be eliminated by general biological reasoning applied to the sequence and organism context. (1) Option C (ciliary basal body): the organism is Aureobasidium melanogenum, an Ascomycete fungus. Fungi lost cilia/flagella early in eukaryotic evolution; Ascomycota do not possess cilia or basal bodies, making this compartment biologically implausible. (2) Option D (peroxisomal matrix): peroxisomal matrix proteins require a C-terminal PTS1 signal (typically SKL or variants) or an N-terminal PTS2 signal. The C-terminus ends in '…LASKEAKW' with no PTS1 motif, and the N-terminus lacks a PTS2 tripeptide. (3) Option B (chromosome): the sequence shows no DNA-binding domain, no histone-fold motif, no HMG-box, and no other chromatin-associated structural feature. By elimination, option A (membrane) is the only remaining plausible compartment. Additionally, the sequence contains several amphipathic and moderately hydrophobic stretches (e.g., 'TTLFDVLGSTAFKP', 'SAAMSATPYRKDFYAKL') consistent with peripheral membrane association rather than a soluble-only protein, and glycolipid transfer proteins are well known to interact with membrane surfaces during lipid transfer.",
    "missing_item_specific_fact": "None that is essential. The positive identification of 'membrane' for a GLTP benefits from knowing that GLTPs are membrane-interacting proteins, but the elimination of B, C, and D is achievable through general cell biology (fungi lack cilia, peroxisomal targeting signals, DNA-binding motifs).",
    "reason": "The question is answerable through structured elimination using general biological knowledge: fungal biology rules out cilia, absence of PTS signals rules out peroxisomal matrix, absence of DNA-binding features rules out chromosome. The remaining option (membrane) is consistent with the protein's glycolipid-transfer function and its amphipathic sequence character. This constitutes meaningful reasoning grounds rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided options, only 'membrane' survives elimination. 'Cytosol' would arguably be the more precise primary localization for a GLTP (and is annotated in UniProt), but it is not offered as a choice. The GO term GO:0016020 'membrane' is extremely broad (any protein attached to or embedded in a lipid bilayer), so a peripheral membrane-interacting GLTP can legitimately be tagged 'membrane.' No other option is defensible given the organism (fungus, no cilia), the absence of targeting signals for peroxisomes or chromosomes, and the protein's known membrane-interacting biochemistry."
  },
  "important_caveats": [
    "Both GO cellular-component annotations (membrane and cytosol) carry IEA:TreeGrafter evidence, i.e., computational phylogenetic inference, not experimental localization.",
    "GLTPs are canonically classified as soluble/cytosolic proteins that transiently engage membranes; calling 'membrane' the primary location is a simplification, though it is defensible under the broad GO:0016020 definition and given that 'cytosol' is not an option.",
    "The protein name 'Glycolipid transfer protein' is sourced from a literature reference (PubMed:32003433) on liamocin biosynthesis/transport, not from direct experimental subcellular fractionation of this specific protein.",
    "The identity of the protein (GLTP) is not provided in the question input; a model must infer function from sequence features or pattern recognition, which adds a layer of difficulty beyond pure compartment reasoning.",
    "The UniProt entry was first publicly released in February 2025; the benchmark author's exact source snapshot is unknown."
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

**Accession:** `A0A223HDI2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 16. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.060643+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Glycolipid transfer protein"}}}
```

Source SHA-256: `cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)  
**Locator:** `/uniProtKBCrossReferences/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.060643+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDI2.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:44.060643+00:00.  

```json
{"database":"GO","id":"GO:0016020","properties":[{"key":"GoTerm","value":"C:membrane"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `cd27114264ad6d95907c9d0ca40d7087fc933a811ae632a7d10b4a29dd9c86d4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16)  
**Locator:** `lines 69-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:24:46.537205+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; IEA:TreeGrafter.
```

Source SHA-256: `5250846a5879910a1cb487027efe195ee80b515fd2492b5e68903453b74cc6bb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDI2?format=txt&versions=16)  
**Locator:** `lines 70-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:24:46.537205+00:00.  

```text
DR   GO; GO:0016020; C:membrane; IEA:TreeGrafter.
```

Source SHA-256: `5250846a5879910a1cb487027efe195ee80b515fd2492b5e68903453b74cc6bb`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 122626-122650`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016020
name: membrane
namespace: cellular_component
alt_id: GO:0016021
alt_id: GO:0098589
alt_id: GO:0098805
def: "A lipid bilayer along with all the proteins and protein complexes embedded in it and attached to it." [GOC:dos, GOC:mah, ISBN:0815316194]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_flybase_ribbon
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_plant
subset: goslim_yeast
synonym: "integral component of membrane" NARROW []
synonym: "integral to membrane" NARROW []
synonym: "membrane region" NARROW []
synonym: "region of membrane" NARROW []
synonym: "transmembrane" RELATED [GOC:mah]
synonym: "whole membrane" NARROW []
xref: Wikipedia:Biological_membrane
xref: Wikipedia:Transmembrane_protein
is_a: GO:0110165 ! cellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 152. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
