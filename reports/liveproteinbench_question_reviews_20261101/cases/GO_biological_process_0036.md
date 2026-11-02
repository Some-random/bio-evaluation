# GO_biological_process_0036

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — saponin biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDQNDKKVEIIVFPYHGQGHMNTMLQFAKRIAWKNAKVTIATTLSTTNKMKSKVENAWGTSITLDSIYDDSDESQIKFMDRMARFEAAAASSLSKLLVQKKEEADNKVLLVYDGNLPWALDIAHEHGVRGAAFFPQSCATVATYYSLYQETQGKELETELPAVFPPLELIQRNVPNVFGLKFPEAVVAKNGKEYSPFVLFVLRQCINLEKADLLLFNQFDKLVEPGEVLQWMSKIFNVKTIGPTLPSSYIDKRIKDDVDYGFHAFNLDNNSCINWLNSKPARSVIYIAFGSSVHYSVEQMTEIAEALKSQPNNFLWAVRETEQKKLPEDFVQQTSEKGLMLSWCPQLDVLVHESISCFVTHCGWNSITEALSFGVPMLSVPQFLDQPVDAHFVEQVWGAGITVKRSEDGLVTRDEIVRCLEVLNNGEKAEEIKANVARWKVLAKEALDEGGSSDKHIDEIIEWVSSF

[Multiple Choices]
A. polysaccharide catabolic process
B. saponin biosynthetic process
C. positive regulation of calcium-mediated signaling
D. mitochondrial outer membrane permeabilization
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as a UDP-glucosyl transferase involved in oleanane-type triterpene saponin biosynthesis. The entry includes an experimentally supported function annotation and an IDA annotation for saponin biosynthesis, supporting choice B.

Citations as saved: [H3](#evidence-h3), [H5](#evidence-h5), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with an enzyme, and possibly a glycosyltransferase, but that broad inference does not establish its substrate or specific pathway.


**Missing item-specific fact**

> Identifying saponin biosynthesis requires the protein-specific substrate and pathway annotation or experimental characterization; these are not supplied in the sequence and choices.


**Reason**

> The choices do not provide enough context to distinguish this enzyme’s specific role from other possible glycosyltransferase functions by general biological reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched functional evidence specifically supports saponin biosynthesis; none of the other choices is comparably supported.


### Important caveats

- The reviewer evidence supports the key but was not available to the evaluated model.
- The exact source snapshot used by the author is unknown, although the matching historical entry already contained the saponin-biosynthesis annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, and possibly a glycosyltransferase, but that broad inference does not establish its substrate or specific pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying saponin biosynthesis requires the protein-specific substrate and pathway annotation or experimental characterization; these are not supplied in the sequence and choices.",
    "reason": "The choices do not provide enough context to distinguish this enzyme’s specific role from other possible glycosyltransferase functions by general biological reasoning alone."
  },
  "case_id": "GO_biological_process_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H5",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a UDP-glucosyl transferase involved in oleanane-type triterpene saponin biosynthesis. The entry includes an experimentally supported function annotation and an IDA annotation for saponin biosynthesis, supporting choice B."
  },
  "important_caveats": [
    "The reviewer evidence supports the key but was not available to the evaluated model.",
    "The exact source snapshot used by the author is unknown, although the matching historical entry already contained the saponin-biosynthesis annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched functional evidence specifically supports saponin biosynthesis; none of the other choices is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as a UDP-glucosyl transferase involved in oleanane-type triterpene saponin biosynthesis. The entry includes an experimentally supported function annotation and an IDA annotation for saponin biosynthesis, supporting choice B.",
    "evidence_ids": ["H3", "H5", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with an enzyme, and possibly a glycosyltransferase, but that broad inference does not establish its substrate or specific pathway.",
    "missing_item_specific_fact": "Identifying saponin biosynthesis requires the protein-specific substrate and pathway annotation or experimental characterization; these are not supplied in the sequence and choices.",
    "reason": "The choices do not provide enough context to distinguish this enzyme’s specific role from other possible glycosyltransferase functions by general biological reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched functional evidence specifically supports saponin biosynthesis; none of the other choices is comparably supported."
  },
  "important_caveats": [
    "The reviewer evidence supports the key but was not available to the evaluated model.",
    "The exact source snapshot used by the author is unknown, although the matching historical entry already contained the saponin-biosynthesis annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1M2U7 (SoUGT74CD1 from Saponaria officinalis) is explicitly annotated with GO:0016135 'saponin biosynthetic process' via IDA:UniProtKB evidence based on experimental data from PubMed:39043959. The FUNCTION comment confirms it is a 'Component of the oleanane-type triterpene saponins biosynthetic pathway.' The GO term is also annotated with GO:0016104 'triterpenoid biosynthetic process.' The sequence matches exactly (SHA-256 verified). The expected answer B is directly supported by experimental annotation.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options C (positive regulation of calcium-mediated signaling) and D (mitochondrial outer membrane permeabilization) are animal-specific processes involving BCL-2 family proteins and calcium signaling cascades, respectively. The supplied sequence lacks mitochondrial targeting signals, BH3/BH4 domains, or any features of animal signaling proteins, and its composition is consistent with a plant protein. Option A (polysaccharide catabolic process) describes hydrolytic breakdown of polysaccharides, which requires glycosidases/hydrolases, not transferases. The C-terminal region of the sequence contains motifs consistent with the plant secondary product glycosyltransferase (PSPG) box of UDP-glycosyltransferases (UGTs), which catalyze glycosyl transfer (biosynthetic direction), not hydrolysis. By elimination of A (wrong enzyme class/direction), C and D (animal-specific processes), option B (a plant secondary metabolite biosynthetic process involving glycosylation) is the only remaining option consistent with a plant UGT.


**Missing item-specific fact**

> The specific identification of 'saponin' biosynthesis (as opposed to flavonoid, phenylpropanoid, or other glycosyltransferase-mediated pathways) is not derivable from the sequence alone. The substrate specificity (QA-tri acceptor for 4-keto-6-deoxy-glucose transfer) was determined experimentally in PubMed:39043959. However, this specificity is not needed to answer the question since the other three options are eliminable.


**Reason**

> While the positive identification of 'saponin' specifically requires experimental substrate data, the question is answerable by elimination: C and D are animal-specific processes clearly inconsistent with a plant protein sequence, and A describes catabolic hydrolysis inconsistent with a transferase. B is the only option consistent with a plant glycosyltransferase in a biosynthetic pathway. The elimination reasoning is grounded in general biological knowledge about enzyme classes, organism-specific processes, and protein domain architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (B) is consistent with a plant glycosyltransferase involved in secondary metabolite biosynthesis. The other three options describe processes (animal calcium signaling, animal apoptosis, polysaccharide hydrolysis) that are mechanistically incompatible with the sequence features. No ambiguity exists among the choices.


### Important caveats

- The positive identification of 'saponin' specifically (vs. other UGT pathways) is not derivable from sequence alone; it relies on experimental substrate data. The answer is reached primarily by elimination of clearly incompatible distractors.
- Recognition of the PSPG box motif from a 468-aa sequence without prior knowledge of UGT domain architecture is non-trivial and may not be reliable for all models.
- The UniProt annotation is IDA (Inferred from Direct Assay) based on PubMed:39043959 (2025, Nat. Chem. Biol.), indicating experimental validation of saponin biosynthesis involvement.
- The organism (Saponaria officinalis, 'soapwort') is not provided in the question input; if it were, the name 'Saponaria' itself would strongly hint at saponin biosynthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options C (positive regulation of calcium-mediated signaling) and D (mitochondrial outer membrane permeabilization) are animal-specific processes involving BCL-2 family proteins and calcium signaling cascades, respectively. The supplied sequence lacks mitochondrial targeting signals, BH3/BH4 domains, or any features of animal signaling proteins, and its composition is consistent with a plant protein. Option A (polysaccharide catabolic process) describes hydrolytic breakdown of polysaccharides, which requires glycosidases/hydrolases, not transferases. The C-terminal region of the sequence contains motifs consistent with the plant secondary product glycosyltransferase (PSPG) box of UDP-glycosyltransferases (UGTs), which catalyze glycosyl transfer (biosynthetic direction), not hydrolysis. By elimination of A (wrong enzyme class/direction), C and D (animal-specific processes), option B (a plant secondary metabolite biosynthetic process involving glycosylation) is the only remaining option consistent with a plant UGT.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identification of 'saponin' biosynthesis (as opposed to flavonoid, phenylpropanoid, or other glycosyltransferase-mediated pathways) is not derivable from the sequence alone. The substrate specificity (QA-tri acceptor for 4-keto-6-deoxy-glucose transfer) was determined experimentally in PubMed:39043959. However, this specificity is not needed to answer the question since the other three options are eliminable.",
    "reason": "While the positive identification of 'saponin' specifically requires experimental substrate data, the question is answerable by elimination: C and D are animal-specific processes clearly inconsistent with a plant protein sequence, and A describes catabolic hydrolysis inconsistent with a transferase. B is the only option consistent with a plant glycosyltransferase in a biosynthetic pathway. The elimination reasoning is grounded in general biological knowledge about enzyme classes, organism-specific processes, and protein domain architecture."
  },
  "case_id": "GO_biological_process_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1M2U7 (SoUGT74CD1 from Saponaria officinalis) is explicitly annotated with GO:0016135 'saponin biosynthetic process' via IDA:UniProtKB evidence based on experimental data from PubMed:39043959. The FUNCTION comment confirms it is a 'Component of the oleanane-type triterpene saponins biosynthetic pathway.' The GO term is also annotated with GO:0016104 'triterpenoid biosynthetic process.' The sequence matches exactly (SHA-256 verified). The expected answer B is directly supported by experimental annotation."
  },
  "important_caveats": [
    "The positive identification of 'saponin' specifically (vs. other UGT pathways) is not derivable from sequence alone; it relies on experimental substrate data. The answer is reached primarily by elimination of clearly incompatible distractors.",
    "Recognition of the PSPG box motif from a 468-aa sequence without prior knowledge of UGT domain architecture is non-trivial and may not be reliable for all models.",
    "The UniProt annotation is IDA (Inferred from Direct Assay) based on PubMed:39043959 (2025, Nat. Chem. Biol.), indicating experimental validation of saponin biosynthesis involvement.",
    "The organism (Saponaria officinalis, 'soapwort') is not provided in the question input; if it were, the name 'Saponaria' itself would strongly hint at saponin biosynthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (B) is consistent with a plant glycosyltransferase involved in secondary metabolite biosynthesis. The other three options describe processes (animal calcium signaling, animal apoptosis, polysaccharide hydrolysis) that are mechanistically incompatible with the sequence features. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1M2U7 (SoUGT74CD1 from Saponaria officinalis) is explicitly annotated with GO:0016135 'saponin biosynthetic process' via IDA:UniProtKB evidence based on experimental data from PubMed:39043959. The FUNCTION comment confirms it is a 'Component of the oleanane-type triterpene saponins biosynthetic pathway.' The GO term is also annotated with GO:0016104 'triterpenoid biosynthetic process.' The sequence matches exactly (SHA-256 verified). The expected answer B is directly supported by experimental annotation.",
    "evidence_ids": ["C5", "C7", "H3", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options C (positive regulation of calcium-mediated signaling) and D (mitochondrial outer membrane permeabilization) are animal-specific processes involving BCL-2 family proteins and calcium signaling cascades, respectively. The supplied sequence lacks mitochondrial targeting signals, BH3/BH4 domains, or any features of animal signaling proteins, and its composition is consistent with a plant protein. Option A (polysaccharide catabolic process) describes hydrolytic breakdown of polysaccharides, which requires glycosidases/hydrolases, not transferases. The C-terminal region of the sequence contains motifs consistent with the plant secondary product glycosyltransferase (PSPG) box of UDP-glycosyltransferases (UGTs), which catalyze glycosyl transfer (biosynthetic direction), not hydrolysis. By elimination of A (wrong enzyme class/direction), C and D (animal-specific processes), option B (a plant secondary metabolite biosynthetic process involving glycosylation) is the only remaining option consistent with a plant UGT.",
    "missing_item_specific_fact": "The specific identification of 'saponin' biosynthesis (as opposed to flavonoid, phenylpropanoid, or other glycosyltransferase-mediated pathways) is not derivable from the sequence alone. The substrate specificity (QA-tri acceptor for 4-keto-6-deoxy-glucose transfer) was determined experimentally in PubMed:39043959. However, this specificity is not needed to answer the question since the other three options are eliminable.",
    "reason": "While the positive identification of 'saponin' specifically requires experimental substrate data, the question is answerable by elimination: C and D are animal-specific processes clearly inconsistent with a plant protein sequence, and A describes catabolic hydrolysis inconsistent with a transferase. B is the only option consistent with a plant glycosyltransferase in a biosynthetic pathway. The elimination reasoning is grounded in general biological knowledge about enzyme classes, organism-specific processes, and protein domain architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (B) is consistent with a plant glycosyltransferase involved in secondary metabolite biosynthesis. The other three options describe processes (animal calcium signaling, animal apoptosis, polysaccharide hydrolysis) that are mechanistically incompatible with the sequence features. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The positive identification of 'saponin' specifically (vs. other UGT pathways) is not derivable from sequence alone; it relies on experimental substrate data. The answer is reached primarily by elimination of clearly incompatible distractors.",
    "Recognition of the PSPG box motif from a 468-aa sequence without prior knowledge of UGT domain architecture is non-trivial and may not be reliable for all models.",
    "The UniProt annotation is IDA (Inferred from Direct Assay) based on PubMed:39043959 (2025, Nat. Chem. Biol.), indicating experimental validation of saponin biosynthesis involvement.",
    "The organism (Saponaria officinalis, 'soapwort') is not provided in the question input; if it were, the name 'Saponaria' itself would strongly hint at saponin biosynthesis."
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

**Accession:** `A0AAW1M2U7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1M2U7.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:41.867838+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). A glycosyltransferase that, together with SDR1, mediates the conversion of QA-tri to QA-triF; UGT74CD1 may transfer 4-keto-6-deoxy-glucose to QA-tri, which is in turn reduced to D-fucose by SDR1, thus leading to QA-triF formation via the initiation of the C-28 sugar chain (PubMed:39043959)"}]}
```

Source SHA-256: `9e83ecfae642612e0a9d04119aef39a3020c2e00cb00661e9ca5632043218b90`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1M2U7.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:41.867838+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0016135","properties":[{"key":"GoTerm","value":"P:saponin biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `9e83ecfae642612e0a9d04119aef39a3020c2e00cb00661e9ca5632043218b90`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1M2U7?format=txt&versions=5)  
**Locator:** `lines 34-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:45.433800+00:00.  

```text
CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.
CC       saponarioside A and saponarioside B) biosynthetic pathway, leading to
CC       the production of natural products with detergent properties used as
CC       traditional sources of soap (PubMed:39043959). A glycosyltransferase
CC       that, together with SDR1, mediates the conversion of QA-tri to QA-triF;
CC       UGT74CD1 may transfer 4-keto-6-deoxy-glucose to QA-tri, which is in
CC       turn reduced to D-fucose by SDR1, thus leading to QA-triF formation via
CC       the initiation of the C-28 sugar chain (PubMed:39043959).
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `6fb7981b56d64ad94695deca153a07b58aaf5f39453d0b61b923eef58aac0a67`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1M2U7?format=txt&versions=5)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:45.433800+00:00.  

```text
DR   GO; GO:0016135; P:saponin biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `6fb7981b56d64ad94695deca153a07b58aaf5f39453d0b61b923eef58aac0a67`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 123836-123847`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016135
name: saponin biosynthetic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the formation of saponins, glycosides of plants in which the aglycan (sapogenin) group is a terpene or steroid and the sugar group is a glucose, a galactose, a pentose, a methylpentose or an oligosaccharide. Saponins are powerful surfactant agents and membrane active; they are, hence, toxic to animals on injection." [GOC:curators]
synonym: "saponin anabolism" EXACT []
synonym: "saponin biosynthesis" EXACT []
synonym: "saponin formation" EXACT []
synonym: "saponin synthesis" EXACT []
is_a: GO:0016134 ! saponin metabolic process
is_a: GO:0016138 ! glycoside biosynthetic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 36. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
