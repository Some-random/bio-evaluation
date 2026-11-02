# GO_biological_process_0081

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — adenylate cyclase-activating G protein-coupled receptor signaling pathway

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGGCMSREASEEMEQRKKSQAIDREIMDDSRRLRRECKILLLGSGESGKSTIVKQMKIIHQNGYTVDELQHYRLTVYKNLVDCAKALIDAMRQFDIVPEHEANKEHMEFLYTFQVDPDPNVPLDLHVSKAVAALWDDPAVPSVLEHQSEFYIMDSAPYFFAEAARIGSPEYIPSEADVLRARTKTTGIYETRFTMGQLNIHMFDVGGQRSERKKWIHCFESVTSIIFCVALSEYDQVLLEEQNQNRMLESLVLFDSVVNSRWFVRTSIILFLNKVDLFRQKLPRTPLSNYFPDYSGGPDVNRAAKYLLWRFNQVNRAHLNLYPHLTQATDTSNIRLVFAAVKETILQNALKDSGIL

[Multiple Choices]
A. response to abscisic acid
B. homoserine biosynthetic process
C. DNA topological change
D. adenylate cyclase-activating G protein-coupled receptor signaling pathway
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

> The supplied sequence exactly matches the annotated fungal G-protein alpha-2 subunit. Its annotation links it to adenylate cyclase-activating GPCR signaling, with experimental evidence cited for the function; the sequence match makes that evidence relevant to this protein. The cited work includes strain-specific qualifications, but does not undermine the pathway assignment.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a nucleotide-binding motif consistent with a GTPase, and recognizing a heterotrimeric G-protein alpha subunit would make GPCR signaling plausible. That general inference does not establish this protein’s specific coupling to adenylate cyclase.


**Missing item-specific fact**

> The protein-specific functional link between this fungal G-protein alpha-2 subunit and adenylate cyclase-activating GPCR signaling, established by annotation and cited experimental work.


**Reason**

> The input provides sequence alone, without organism, protein identity, or functional data. General G-protein knowledge narrows the possibilities but does not establish the specific pathway needed to choose D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, D matches the supported pathway annotation; the other choices describe distinct processes not supported for this protein.


### Important caveats

- The functional annotation and supporting literature are reviewer-only evidence, not information supplied to the evaluated model.
- The exact author source snapshot is unknown; historical and current records match the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a nucleotide-binding motif consistent with a GTPase, and recognizing a heterotrimeric G-protein alpha subunit would make GPCR signaling plausible. That general inference does not establish this protein’s specific coupling to adenylate cyclase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional link between this fungal G-protein alpha-2 subunit and adenylate cyclase-activating GPCR signaling, established by annotation and cited experimental work.",
    "reason": "The input provides sequence alone, without organism, protein identity, or functional data. General G-protein knowledge narrows the possibilities but does not establish the specific pathway needed to choose D."
  },
  "case_id": "GO_biological_process_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated fungal G-protein alpha-2 subunit. Its annotation links it to adenylate cyclase-activating GPCR signaling, with experimental evidence cited for the function; the sequence match makes that evidence relevant to this protein. The cited work includes strain-specific qualifications, but does not undermine the pathway assignment."
  },
  "important_caveats": [
    "The functional annotation and supporting literature are reviewer-only evidence, not information supplied to the evaluated model.",
    "The exact author source snapshot is unknown; historical and current records match the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D matches the supported pathway annotation; the other choices describe distinct processes not supported for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated fungal G-protein alpha-2 subunit. Its annotation links it to adenylate cyclase-activating GPCR signaling, with experimental evidence cited for the function; the sequence match makes that evidence relevant to this protein. The cited work includes strain-specific qualifications, but does not undermine the pathway assignment.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a nucleotide-binding motif consistent with a GTPase, and recognizing a heterotrimeric G-protein alpha subunit would make GPCR signaling plausible. That general inference does not establish this protein’s specific coupling to adenylate cyclase.",
    "missing_item_specific_fact": "The protein-specific functional link between this fungal G-protein alpha-2 subunit and adenylate cyclase-activating GPCR signaling, established by annotation and cited experimental work.",
    "reason": "The input provides sequence alone, without organism, protein identity, or functional data. General G-protein knowledge narrows the possibilities but does not establish the specific pathway needed to choose D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D matches the supported pathway annotation; the other choices describe distinct processes not supported for this protein."
  },
  "important_caveats": [
    "The functional annotation and supporting literature are reviewer-only evidence, not information supplied to the evaluated model.",
    "The exact author source snapshot is unknown; historical and current records match the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G1XJZ0 (GPA2 from Arthrobotrys oligospora) explicitly annotates the protein as an alpha subunit of a heterotrimeric G protein involved in adenylate cyclase-activating GPCR signaling (GO:0007189). The FUNCTION comment (C5/H4) is backed by experimental evidence (ECO:0000269, PubMed:35993904 and PubMed:38649409). The GO cross-reference C6 confirms GO:0007189 directly. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical G-alpha subunit motifs identifiable by general biological knowledge: the Walker A/P-loop 'GSGESGKSTIVKQ' (GTP-binding glycine-rich loop), the 'NKVD' motif (NKxD), and the 'DVGGQ' switch II motif. These motifs are diagnostic of heterotrimeric G-protein alpha subunits. A model recognizing these motifs can conclude the protein participates in GPCR signaling. Among the four options, only D (adenylate cyclase-activating GPCR signaling pathway) is a G-protein/GPCR-related biological process. Options A (abscisic acid response – a plant hormone pathway), B (homoserine biosynthesis – amino acid metabolism), and C (DNA topological change – DNA metabolism) are categorically unrelated to G-protein function and can be eliminated by general biological reasoning.


**Missing item-specific fact**

> The specific determination that this particular G-alpha subunit ACTIVATES (rather than inhibits) adenylate cyclase in this organism is an experimentally derived fact from 2022/2024 papers not derivable from sequence motifs alone. However, since no other option relates to GPCR signaling at all, the elimination pathway still leads to D without needing this specific qualifier.


**Reason**

> A model with general knowledge of G-protein structural motifs can identify this as a G-alpha subunit and select D as the only GPCR-related option by elimination. The reasoning does not require memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe processes (plant hormone response, amino acid biosynthesis, DNA topology) that have no mechanistic connection to a G-protein alpha subunit. GO:0010619 (glucose-activated variant) is a child of GO:0007189 and is not offered as a separate option. D is uniquely defensible.


### Important caveats

- The GO:0007189 annotation carries IEA:TreeGrafter evidence (computational transfer), but the underlying FUNCTION statement is supported by experimental evidence (ECO:0000269) from two independent studies.
- The specific 'adenylate cyclase-activating' role of GPA2 in A. oligospora is organism-specific and counterintuitive relative to fungal GPA2 nomenclature (often Gi-like/inhibitory in other fungi); this was established experimentally in 2022-2024.
- The sequence-based identification of G-alpha subunits relies on conserved motifs; the precise subtype (Gs vs Gi vs Gq) is not trivially determined from sequence alone, but the elimination of clearly unrelated distractors compensates.
- Entry was first released 2025-04-09; the benchmark construction date is unknown, so the annotation may not have existed at question-authoring time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical G-alpha subunit motifs identifiable by general biological knowledge: the Walker A/P-loop 'GSGESGKSTIVKQ' (GTP-binding glycine-rich loop), the 'NKVD' motif (NKxD), and the 'DVGGQ' switch II motif. These motifs are diagnostic of heterotrimeric G-protein alpha subunits. A model recognizing these motifs can conclude the protein participates in GPCR signaling. Among the four options, only D (adenylate cyclase-activating GPCR signaling pathway) is a G-protein/GPCR-related biological process. Options A (abscisic acid response – a plant hormone pathway), B (homoserine biosynthesis – amino acid metabolism), and C (DNA topological change – DNA metabolism) are categorically unrelated to G-protein function and can be eliminated by general biological reasoning.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific determination that this particular G-alpha subunit ACTIVATES (rather than inhibits) adenylate cyclase in this organism is an experimentally derived fact from 2022/2024 papers not derivable from sequence motifs alone. However, since no other option relates to GPCR signaling at all, the elimination pathway still leads to D without needing this specific qualifier.",
    "reason": "A model with general knowledge of G-protein structural motifs can identify this as a G-alpha subunit and select D as the only GPCR-related option by elimination. The reasoning does not require memorizing this specific UniProt entry."
  },
  "case_id": "GO_biological_process_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G1XJZ0 (GPA2 from Arthrobotrys oligospora) explicitly annotates the protein as an alpha subunit of a heterotrimeric G protein involved in adenylate cyclase-activating GPCR signaling (GO:0007189). The FUNCTION comment (C5/H4) is backed by experimental evidence (ECO:0000269, PubMed:35993904 and PubMed:38649409). The GO cross-reference C6 confirms GO:0007189 directly. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The GO:0007189 annotation carries IEA:TreeGrafter evidence (computational transfer), but the underlying FUNCTION statement is supported by experimental evidence (ECO:0000269) from two independent studies.",
    "The specific 'adenylate cyclase-activating' role of GPA2 in A. oligospora is organism-specific and counterintuitive relative to fungal GPA2 nomenclature (often Gi-like/inhibitory in other fungi); this was established experimentally in 2022-2024.",
    "The sequence-based identification of G-alpha subunits relies on conserved motifs; the precise subtype (Gs vs Gi vs Gq) is not trivially determined from sequence alone, but the elimination of clearly unrelated distractors compensates.",
    "Entry was first released 2025-04-09; the benchmark construction date is unknown, so the annotation may not have existed at question-authoring time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe processes (plant hormone response, amino acid biosynthesis, DNA topology) that have no mechanistic connection to a G-protein alpha subunit. GO:0010619 (glucose-activated variant) is a child of GO:0007189 and is not offered as a separate option. D is uniquely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"GO_biological_process_0081","expected_answer_check":{"judgment":"supported","reason":"The UniProt entry G1XJZ0 (GPA2 from Arthrobotrys oligospora) explicitly annotates the protein as an alpha subunit of a heterotrimeric G protein involved in adenylate cyclase-activating GPCR signaling (GO:0007189). The FUNCTION comment (C5/H4) is backed by experimental evidence (ECO:0000269, PubMed:35993904 and PubMed:38649409). The GO cross-reference C6 confirms GO:0007189 directly. The sequence matches the benchmark input exactly.","evidence_ids":["C4","C5","C6","H4","H5","GO2"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The sequence contains canonical G-alpha subunit motifs identifiable by general biological knowledge: the Walker A/P-loop 'GSGESGKSTIVKQ' (GTP-binding glycine-rich loop), the 'NKVD' motif (NKxD), and the 'DVGGQ' switch II motif. These motifs are diagnostic of heterotrimeric G-protein alpha subunits. A model recognizing these motifs can conclude the protein participates in GPCR signaling. Among the four options, only D (adenylate cyclase-activating GPCR signaling pathway) is a G-protein/GPCR-related biological process. Options A (abscisic acid response – a plant hormone pathway), B (homoserine biosynthesis – amino acid metabolism), and C (DNA topological change – DNA metabolism) are categorically unrelated to G-protein function and can be eliminated by general biological reasoning.","missing_item_specific_fact":"The specific determination that this particular G-alpha subunit ACTIVATES (rather than inhibits) adenylate cyclase in this organism is an experimentally derived fact from 2022/2024 papers not derivable from sequence motifs alone. However, since no other option relates to GPCR signaling at all, the elimination pathway still leads to D without needing this specific qualifier.","reason":"A model with general knowledge of G-protein structural motifs can identify this as a G-alpha subunit and select D as the only GPCR-related option by elimination. The reasoning does not require memorizing this specific UniProt entry."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"Options A, B, and C describe processes (plant hormone response, amino acid biosynthesis, DNA topology) that have no mechanistic connection to a G-protein alpha subunit. GO:0010619 (glucose-activated variant) is a child of GO:0007189 and is not offered as a separate option. D is uniquely defensible."},"important_caveats":["The GO:0007189 annotation carries IEA:TreeGrafter evidence (computational transfer), but the underlying FUNCTION statement is supported by experimental evidence (ECO:0000269) from two independent studies.","The specific 'adenylate cyclase-activating' role of GPA2 in A. oligospora is organism-specific and counterintuitive relative to fungal GPA2 nomenclature (often Gi-like/inhibitory in other fungi); this was established experimentally in 2022-2024.","The sequence-based identification of G-alpha subunits relies on conserved motifs; the precise subtype (Gs vs Gi vs Gq) is not trivially determined from sequence alone, but the elimination of clearly unrelated distractors compensates.","Entry was first released 2025-04-09; the benchmark construction date is unknown, so the annotation may not have existed at question-authoring time."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `G1XJZ0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 67. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:34.414621+00:00.  

```json
"G1XJZ0"
```

Source SHA-256: `2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:34.414621+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Guanine nucleotide-binding protein alpha-2 subunit"}}}
```

Source SHA-256: `2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:34.414621+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35993904","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38649409","source":"PubMed"}],"value":"Alpha subunit of the heterotrimeric guanine nucleotide-binding protein (G protein) involved in adenylate cyclase-activating ascaroside pheromone-activated G protein-coupled receptor signaling pathway (PubMed:35993904, PubMed:38649409). Binding of prey ascaroside pheromones to transmembrane receptors GPR2 and GPR3 leads to activation of the pathway and positive regulation of trap formation for nematode capture (PubMed:35993904, PubMed:38649409)"}]}
```

Source SHA-256: `2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJZ0.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:34.414621+00:00.  

```json
{"database":"GO","id":"GO:0007189","properties":[{"key":"GoTerm","value":"P:adenylate cyclase-activating G protein-coupled receptor signaling pathway"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `2c5be4b49110e21226557cd97f2bd996a289b746c5daf1c644e85e8dc7d30e50`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)  
**Locator:** `lines 41-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:28:42.163763+00:00.  

```text
CC   -!- FUNCTION: Alpha subunit of the heterotrimeric guanine nucleotide-
CC       binding protein (G protein) involved in adenylate cyclase-activating
CC       ascaroside pheromone-activated G protein-coupled receptor signaling
CC       pathway (PubMed:35993904, PubMed:38649409). Binding of prey ascaroside
CC       pheromones to transmembrane receptors GPR2 and GPR3 leads to activation
CC       of the pathway and positive regulation of trap formation for nematode
CC       capture (PubMed:35993904, PubMed:38649409).
CC       {ECO:0000269|PubMed:35993904, ECO:0000269|PubMed:38649409}.
```

Source SHA-256: `0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJZ0?format=txt&versions=67)  
**Locator:** `lines 89-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:28:42.163763+00:00.  

```text
DR   GO; GO:0010619; P:adenylate cyclase-activating glucose-activated G protein-coupled receptor signaling pathway; IEA:EnsemblFungi.
```

Source SHA-256: `0b149b7c1c207fc18548ffb4888f1e75ed8d10e370f7367e39946316c6c4ef8f`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 74186-74212`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0007189
name: adenylate cyclase-activating G protein-coupled receptor signaling pathway
namespace: biological_process
alt_id: GO:0010579
alt_id: GO:0010580
def: "A G protein-coupled receptor signaling pathway in which the signal is transmitted via the activation of adenylyl cyclase activity which results in an increase in the intracellular concentration of cyclic AMP (cAMP). This pathway is negatively regulated by phosphodiesterase, which cleaves cAMP and terminates the signaling." [GOC:dph, GOC:mah, GOC:signaling, GOC:tb, ISBN:0815316194]
comment: This term can be used to annotate ligands, receptors and G-proteins that lead to activation of adenylate cyclase activity within a signaling pathway.
synonym: "activation of adenylate cyclase activity by G-protein signaling pathway" RELATED [GOC:bf]
synonym: "activation of adenylate cyclase activity involved in G-protein signaling" RELATED [GOC:signaling]
synonym: "adenylate cyclase-activating GPCR signaling pathway" EXACT [GOC:signaling]
synonym: "G protein signaling, adenylate cyclase activating pathway" EXACT []
synonym: "G protein signaling, adenylyl cyclase activating pathway" EXACT []
synonym: "G protein signalling, adenylate cyclase activating pathway" EXACT []
synonym: "G protein signalling, adenylyl cyclase activating pathway" EXACT []
synonym: "G-protein signaling, adenylate cyclase activating pathway" EXACT [GOC:dph, GOC:tb]
synonym: "G-protein signaling, adenylyl cyclase activating pathway" EXACT []
synonym: "G-protein signalling, adenylate cyclase activating pathway" EXACT []
synonym: "G-protein signalling, adenylyl cyclase activating pathway" EXACT []
synonym: "GPCR signaling pathway via activation of adenylate cyclase" EXACT [GOC:bf]
synonym: "GPCR signaling pathway via activation of adenylate cyclase activity" EXACT [GOC:signaling]
synonym: "positive regulation of adenylate cyclase activity by G-protein signaling pathway" RELATED [GOC:signaling]
synonym: "positive regulation of adenylate cyclase activity by G-protein signalling pathway" RELATED [GOC:mah]
synonym: "positive regulation of adenylate cyclase activity involved in G-protein coupled receptor signaling pathway" EXACT []
xref: Reactome:R-HSA-170660 "Adenylate cyclase activating pathway"
is_a: GO:0007188 ! adenylate cyclase-modulating G protein-coupled receptor signaling pathway

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
