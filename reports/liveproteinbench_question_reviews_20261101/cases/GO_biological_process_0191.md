# GO_biological_process_0191

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — steroid metabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTRKSILVTGASSGLGYAAVQKLAENGFYVFAAVREIRGMFSNIKNIKELKLDLANEQSIEELFIYIEATQKDYPLWGLVNNAGICVPSPLELLREFDLRQQLDTNVIGQLLVTQFALPFIRKSKGRIINITSGLGSIAVPYLGAYSIAQFAKMAFTDVLRRELKHSGVTVSVVQPGAIYTPIWDKFLVTGQEILDNSLDEKRKIYERSFIEFLKASQIGVNSVKTTRNDFAKVILDIFKAEIPETHYYVGDDAKNFSNKSKILTVTEIDEWFDLQSPTESEFKKI

[Multiple Choices]
A. appressorium formation
B. oocyte localization involved in germarium-derived egg chamber formation
C. lipid metabolic process
D. steroid metabolic process
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

### Expected-answer support: contradicted

> The matched protein has an experimentally supported function in pyrrolizwilline alkaloid biosynthesis: it reduces a pyrrolizinone intermediate. That does not support steroid metabolism. The steroid-process annotation is present, but its evidence is computational (IEA:TreeGrafter), not experimental, and appears inconsistent with the reported substrate and pathway.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence offers no clear basis for identifying a steroid-metabolizing enzyme rather than an enzyme in another small-molecule pathway; the choices do not disclose its substrate or pathway.


**Missing item-specific fact**

> The protein-specific substrate and pathway, or a GO annotation for this sequence, would be needed to choose among the metabolic options.


**Reason**

> Choosing D depends on an item-specific annotation or functional fact absent from the input. The sequence alone does not meaningfully distinguish steroid metabolism from other metabolism, and the available specific functional evidence does not support D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The supplied GO annotation assigns D, and the ontology places steroid metabolic process under lipid metabolic process, so C is also a broader term entailed by that annotation. However, the experimentally reported pathway supports neither option as a description of this enzyme's demonstrated function.


### Important caveats

- The sequence matches the protein in the reviewer-only UniProt evidence, including the historical record.
- The D annotation is computational; the cited function is supported by experimental evidence, though the primary paper was not independently reviewed here.
- Pyrrolizwilline is described as an alkaloid, not a steroid.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence offers no clear basis for identifying a steroid-metabolizing enzyme rather than an enzyme in another small-molecule pathway; the choices do not disclose its substrate or pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate and pathway, or a GO annotation for this sequence, would be needed to choose among the metabolic options.",
    "reason": "Choosing D depends on an item-specific annotation or functional fact absent from the input. The sequence alone does not meaningfully distinguish steroid metabolism from other metabolism, and the available specific functional evidence does not support D."
  },
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "contradicted",
    "reason": "The matched protein has an experimentally supported function in pyrrolizwilline alkaloid biosynthesis: it reduces a pyrrolizinone intermediate. That does not support steroid metabolism. The steroid-process annotation is present, but its evidence is computational (IEA:TreeGrafter), not experimental, and appears inconsistent with the reported substrate and pathway."
  },
  "important_caveats": [
    "The sequence matches the protein in the reviewer-only UniProt evidence, including the historical record.",
    "The D annotation is computational; the cited function is supported by experimental evidence, though the primary paper was not independently reviewed here.",
    "Pyrrolizwilline is described as an alkaloid, not a steroid."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The supplied GO annotation assigns D, and the ontology places steroid metabolic process under lipid metabolic process, so C is also a broader term entailed by that annotation. However, the experimentally reported pathway supports neither option as a description of this enzyme's demonstrated function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The matched protein has an experimentally supported function in pyrrolizwilline alkaloid biosynthesis: it reduces a pyrrolizinone intermediate. That does not support steroid metabolism. The steroid-process annotation is present, but its evidence is computational (IEA:TreeGrafter), not experimental, and appears inconsistent with the reported substrate and pathway.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence offers no clear basis for identifying a steroid-metabolizing enzyme rather than an enzyme in another small-molecule pathway; the choices do not disclose its substrate or pathway.",
    "missing_item_specific_fact": "The protein-specific substrate and pathway, or a GO annotation for this sequence, would be needed to choose among the metabolic options.",
    "reason": "Choosing D depends on an item-specific annotation or functional fact absent from the input. The sequence alone does not meaningfully distinguish steroid metabolism from other metabolism, and the available specific functional evidence does not support D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The supplied GO annotation assigns D, and the ontology places steroid metabolic process under lipid metabolic process, so C is also a broader term entailed by that annotation. However, the experimentally reported pathway supports neither option as a description of this enzyme's demonstrated function."
  },
  "important_caveats": [
    "The sequence matches the protein in the reviewer-only UniProt evidence, including the historical record.",
    "The D annotation is computational; the cited function is supported by experimental evidence, though the primary paper was not independently reviewed here.",
    "Pyrrolizwilline is described as an alkaloid, not a steroid."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The GO:0008202 'steroid metabolic process' annotation (C6, H4) carries only evidence code IEA:TreeGrafter — a purely computational sequence-similarity transfer, not experimental evidence. The experimental characterization (ECO:0000269, PubMed:39428351; C5, H3) explicitly states the protein 'catalyzes the reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol' as part of 'the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid.' Pyrrolizidine alkaloids contain a fused pyrrolizidine ring system (two five-membered N-containing rings), not the cyclopentanoperhydrophenanthrene nucleus required by the GO:0008202 definition (GO2). The TreeGrafter annotation appears to be a false positive from oxidoreductase-family similarity and is contradicted by the primary experimental data.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence (286 aa, N-terminal Rossmann-like motif 'TGASSGLGY') suggests an NAD(P)-dependent oxidoreductase, which is broadly consistent with metabolic processes. Options A (appressorium formation) and B (oocyte localization) are eukaryotic/fungal processes irrelevant to a bacterial protein, so they can be eliminated by general knowledge. However, distinguishing C (lipid metabolic process, GO:0006629) from D (steroid metabolic process, GO:0008202) requires knowing the specific substrate class. No sequence motif in the provided 286-aa sequence identifies a steroid nucleus or a lipid substrate. The actual substrate (3-amino-tetrahydro-pyrrolizinone, a pyrrolizidine alkaloid) fits neither C nor D, so no sequence-based argument can favor D over C.


**Missing item-specific fact**

> The specific UniProt GO annotation GO:0008202 (IEA:TreeGrafter) for this exact accession, or equivalently knowledge that TreeGrafter assigned this protein to the steroid-metabolism branch — an item-specific database lookup with no sequence-level justification.


**Reason**

> Eliminating A and B uses general biology (bacterial protein cannot form appressoria or localize oocytes). Choosing between C and D requires the specific database annotation, which is itself a computational inference likely incorrect. No motif, domain architecture, or catalytic-residue pattern in the supplied sequence distinguishes steroid from lipid metabolism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> GO:0008202 (steroid metabolic process) is_a GO:0006629 (lipid metabolic process) per GO2. If D were accepted as the annotation, C is automatically true as the parent term, making both defensible under standard GO semantics. More fundamentally, the experimentally verified function (pyrrolizidine alkaloid biosynthesis) matches neither C nor D, so the 'correct' answer rests entirely on a likely-erroneous IEA annotation.


### Important caveats

- The only GO:0008202 annotation is IEA:TreeGrafter (automated, not curated or experimental); the experimental evidence (ECO:0000269) describes pyrrolizidine alkaloid biosynthesis, not steroid metabolism.
- Pyrrolizidine alkaloids are not steroids (no cyclopentanoperhydrophenanthrene nucleus) and are not lipids; neither C nor D accurately describes the protein's verified biological role.
- The identity of the protein (UniProt A0A2G0QDN4) was inferred reviewer-only from dataset metadata; the evaluated model received only the raw 286-aa sequence.
- The benchmark ontology snapshot may differ from the current GO release, though the steroid/lipid is_a relationship is long-standing.
- The question's expected answer relies on a database annotation that the primary literature contradicts, raising concerns about benchmark key validity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (286 aa, N-terminal Rossmann-like motif 'TGASSGLGY') suggests an NAD(P)-dependent oxidoreductase, which is broadly consistent with metabolic processes. Options A (appressorium formation) and B (oocyte localization) are eukaryotic/fungal processes irrelevant to a bacterial protein, so they can be eliminated by general knowledge. However, distinguishing C (lipid metabolic process, GO:0006629) from D (steroid metabolic process, GO:0008202) requires knowing the specific substrate class. No sequence motif in the provided 286-aa sequence identifies a steroid nucleus or a lipid substrate. The actual substrate (3-amino-tetrahydro-pyrrolizinone, a pyrrolizidine alkaloid) fits neither C nor D, so no sequence-based argument can favor D over C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt GO annotation GO:0008202 (IEA:TreeGrafter) for this exact accession, or equivalently knowledge that TreeGrafter assigned this protein to the steroid-metabolism branch — an item-specific database lookup with no sequence-level justification.",
    "reason": "Eliminating A and B uses general biology (bacterial protein cannot form appressoria or localize oocytes). Choosing between C and D requires the specific database annotation, which is itself a computational inference likely incorrect. No motif, domain architecture, or catalytic-residue pattern in the supplied sequence distinguishes steroid from lipid metabolism."
  },
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The GO:0008202 'steroid metabolic process' annotation (C6, H4) carries only evidence code IEA:TreeGrafter — a purely computational sequence-similarity transfer, not experimental evidence. The experimental characterization (ECO:0000269, PubMed:39428351; C5, H3) explicitly states the protein 'catalyzes the reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol' as part of 'the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid.' Pyrrolizidine alkaloids contain a fused pyrrolizidine ring system (two five-membered N-containing rings), not the cyclopentanoperhydrophenanthrene nucleus required by the GO:0008202 definition (GO2). The TreeGrafter annotation appears to be a false positive from oxidoreductase-family similarity and is contradicted by the primary experimental data."
  },
  "important_caveats": [
    "The only GO:0008202 annotation is IEA:TreeGrafter (automated, not curated or experimental); the experimental evidence (ECO:0000269) describes pyrrolizidine alkaloid biosynthesis, not steroid metabolism.",
    "Pyrrolizidine alkaloids are not steroids (no cyclopentanoperhydrophenanthrene nucleus) and are not lipids; neither C nor D accurately describes the protein's verified biological role.",
    "The identity of the protein (UniProt A0A2G0QDN4) was inferred reviewer-only from dataset metadata; the evaluated model received only the raw 286-aa sequence.",
    "The benchmark ontology snapshot may differ from the current GO release, though the steroid/lipid is_a relationship is long-standing.",
    "The question's expected answer relies on a database annotation that the primary literature contradicts, raising concerns about benchmark key validity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "GO:0008202 (steroid metabolic process) is_a GO:0006629 (lipid metabolic process) per GO2. If D were accepted as the annotation, C is automatically true as the parent term, making both defensible under standard GO semantics. More fundamentally, the experimentally verified function (pyrrolizidine alkaloid biosynthesis) matches neither C nor D, so the 'correct' answer rests entirely on a likely-erroneous IEA annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The GO:0008202 'steroid metabolic process' annotation (C6, H4) carries only evidence code IEA:TreeGrafter — a purely computational sequence-similarity transfer, not experimental evidence. The experimental characterization (ECO:0000269, PubMed:39428351; C5, H3) explicitly states the protein 'catalyzes the reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol' as part of 'the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid.' Pyrrolizidine alkaloids contain a fused pyrrolizidine ring system (two five-membered N-containing rings), not the cyclopentanoperhydrophenanthrene nucleus required by the GO:0008202 definition (GO2). The TreeGrafter annotation appears to be a false positive from oxidoreductase-family similarity and is contradicted by the primary experimental data.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence (286 aa, N-terminal Rossmann-like motif 'TGASSGLGY') suggests an NAD(P)-dependent oxidoreductase, which is broadly consistent with metabolic processes. Options A (appressorium formation) and B (oocyte localization) are eukaryotic/fungal processes irrelevant to a bacterial protein, so they can be eliminated by general knowledge. However, distinguishing C (lipid metabolic process, GO:0006629) from D (steroid metabolic process, GO:0008202) requires knowing the specific substrate class. No sequence motif in the provided 286-aa sequence identifies a steroid nucleus or a lipid substrate. The actual substrate (3-amino-tetrahydro-pyrrolizinone, a pyrrolizidine alkaloid) fits neither C nor D, so no sequence-based argument can favor D over C.",
    "missing_item_specific_fact": "The specific UniProt GO annotation GO:0008202 (IEA:TreeGrafter) for this exact accession, or equivalently knowledge that TreeGrafter assigned this protein to the steroid-metabolism branch — an item-specific database lookup with no sequence-level justification.",
    "reason": "Eliminating A and B uses general biology (bacterial protein cannot form appressoria or localize oocytes). Choosing between C and D requires the specific database annotation, which is itself a computational inference likely incorrect. No motif, domain architecture, or catalytic-residue pattern in the supplied sequence distinguishes steroid from lipid metabolism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "GO:0008202 (steroid metabolic process) is_a GO:0006629 (lipid metabolic process) per GO2. If D were accepted as the annotation, C is automatically true as the parent term, making both defensible under standard GO semantics. More fundamentally, the experimentally verified function (pyrrolizidine alkaloid biosynthesis) matches neither C nor D, so the 'correct' answer rests entirely on a likely-erroneous IEA annotation."
  },
  "important_caveats": [
    "The only GO:0008202 annotation is IEA:TreeGrafter (automated, not curated or experimental); the experimental evidence (ECO:0000269) describes pyrrolizidine alkaloid biosynthesis, not steroid metabolism.",
    "Pyrrolizidine alkaloids are not steroids (no cyclopentanoperhydrophenanthrene nucleus) and are not lipids; neither C nor D accurately describes the protein's verified biological role.",
    "The identity of the protein (UniProt A0A2G0QDN4) was inferred reviewer-only from dataset metadata; the evaluated model received only the raw 286-aa sequence.",
    "The benchmark ontology snapshot may differ from the current GO release, though the steroid/lipid is_a relationship is long-standing.",
    "The question's expected answer relies on a database annotation that the primary literature contradicts, raising concerns about benchmark key validity."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `mixed_annotations_require_qualification`.

> C5/H3 describe pyrrolizwilline alkaloid biosynthesis and pyrrolizinone reduction with ECO:0000269; C6/H4 separately carry the keyed steroid-metabolism term as IEA:TreeGrafter.

**Remaining uncertainty:** The mismatch is real at the annotation-description level; possible additional substrate/pathway roles remain untested in these excerpts.

Evidence checked: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A2G0QDN4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 28. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.620054+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39428351","source":"PubMed"}],"value":"Involved in the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid. Catalyzes the reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol"}]}
```

Source SHA-256: `5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:47.620054+00:00.  

```json
{"database":"GO","id":"GO:0008202","properties":[{"key":"GoTerm","value":"P:steroid metabolic process"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)  
**Locator:** `lines 32-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959850+00:00.  

```text
CC   -!- FUNCTION: Involved in the biosynthetic pathway of pyrrolizwilline, a
CC       pyrrolizidine alkaloid. Catalyzes the reduction of 3-amino-tetrahydro-
CC       pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol.
CC       {ECO:0000269|PubMed:39428351}.
```

Source SHA-256: `e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)  
**Locator:** `lines 58-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 28 / 1.  
**Retrieved:** 2026-11-02T04:24:49.959850+00:00.  

```text
DR   GO; GO:0008202; P:steroid metabolic process; IEA:TreeGrafter.
```

Source SHA-256: `e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 80627-80636`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008202
name: steroid metabolic process
namespace: biological_process
def: "The chemical reactions and pathways involving steroids, compounds with a 1,2,cyclopentanoperhydrophenanthrene nucleus." [ISBN:0198547684]
synonym: "steroid metabolism" EXACT []
xref: Reactome:R-HSA-8957322 "Metabolism of steroids"
xref: Wikipedia:Steroid_metabolism
is_a: GO:0006629 ! lipid metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 191. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
