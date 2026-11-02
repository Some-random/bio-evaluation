# GO_biological_process_0158

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **B** — methylation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTTSASTTDHLIDQQVIDGQAGYTKSFLNIYDLAVFKGTAPLAWHCSPAVSRQMYDTCLGANHVEIGVGTGYLLDNATFPVADPKITLVDLNPNSLAHTAQRLNRYDVTTVRANVLEPLPLEERAYDSVGMSYLLHCVPGSIKEKGIALKHAAAVVRPGGVVFGATVLSSGVPVSARGRWTMNYLNKRGDFHNQEDNYDDLRDQLAQYFPRFQLTSRGCVGIWRAWTTD

[Multiple Choices]
A. negative regulation of chondrocyte differentiation
B. methylation
C. surfactant secretion
D. D-xylose metabolic process
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

> The sequence matches the UniProt record, which reports that the protein catalyzes methylation of demethylluteothin; the archived record also annotates GO:0032259 methylation. The cited functional annotation is experimental, although the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices make methylation plausible for an enzyme, but the supplied sequence provides no clear, decisive evidence identifying its reaction or substrate; generic enzyme-sequence heuristics do not establish this specific process.


**Missing item-specific fact**

> The protein-specific functional fact that this enzyme methylates demethylluteothin, or an equivalent identification as a methyltransferase, is absent from the input.


**Reason**

> Distinguishing B requires the protein's specific activity or annotation, not merely general biological reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Methylation is the only listed option supported by the reported catalytic activity. Antibiotic biosynthesis is the broader pathway context, but it is not an option.


### Important caveats

- The reviewer-only UniProt record matches the sequence, but the author's exact source snapshot is unknown.
- The experimental evidence is cited in the database annotation; the cited primary study was not independently examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices make methylation plausible for an enzyme, but the supplied sequence provides no clear, decisive evidence identifying its reaction or substrate; generic enzyme-sequence heuristics do not establish this specific process.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional fact that this enzyme methylates demethylluteothin, or an equivalent identification as a methyltransferase, is absent from the input.",
    "reason": "Distinguishing B requires the protein's specific activity or annotation, not merely general biological reasoning from the sequence."
  },
  "case_id": "GO_biological_process_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, which reports that the protein catalyzes methylation of demethylluteothin; the archived record also annotates GO:0032259 methylation. The cited functional annotation is experimental, although the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence is cited in the database annotation; the cited primary study was not independently examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Methylation is the only listed option supported by the reported catalytic activity. Antibiotic biosynthesis is the broader pathway context, but it is not an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt record, which reports that the protein catalyzes methylation of demethylluteothin; the archived record also annotates GO:0032259 methylation. The cited functional annotation is experimental, although the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H4", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices make methylation plausible for an enzyme, but the supplied sequence provides no clear, decisive evidence identifying its reaction or substrate; generic enzyme-sequence heuristics do not establish this specific process.",
    "missing_item_specific_fact": "The protein-specific functional fact that this enzyme methylates demethylluteothin, or an equivalent identification as a methyltransferase, is absent from the input.",
    "reason": "Distinguishing B requires the protein's specific activity or annotation, not merely general biological reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Methylation is the only listed option supported by the reported catalytic activity. Antibiotic biosynthesis is the broader pathway context, but it is not an option."
  },
  "important_caveats": [
    "The reviewer-only UniProt record matches the sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence is cited in the database annotation; the cited primary study was not independently examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q70KH3, AurI from Streptomyces thioluteus) is experimentally confirmed (ECO:0000269, PubMed:16292785) as a SAM-dependent O-methyltransferase catalyzing methylation of demethylluteothin to luteothin (EC 2.1.1.353). The GO term GO:0032259 'methylation' is annotated to this entry (IEA:UniProtKB-KW), and the underlying enzymatic activity is experimentally verified. Among the four choices, methylation is the only process this protein participates in. The other options (chondrocyte differentiation, surfactant secretion, D-xylose metabolism) are entirely unrelated to this bacterial methyltransferase.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H8](#evidence-h8), [GO1](#evidence-go1), [C3](#evidence-c3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 230 aa from a bacterial organism (Streptomyces), which eliminates options A (negative regulation of chondrocyte differentiation, a eukaryotic developmental process) and C (surfactant secretion, a mammalian lung-specific process) by organism-type reasoning. The sequence contains recognizable SAM-binding methyltransferase motifs: 'GVGTGYLLDN' resembles the classic VGTGY/VIGFG motif and 'GATVLSSGVP' contains the GxGxG glycine-rich loop characteristic of Rossmann-fold methyltransferases. These structural motifs, combined with the small protein size typical of SAM-dependent methyltransferases, support option B. Option D (D-xylose metabolic process) requires TIM-barrel or kinase-fold enzymes with entirely different sequence signatures absent here.


**Missing item-specific fact**

> None critical. The SAM-binding motif recognition and organism-based elimination provide a valid reasoning path, though precise motif identification requires moderate protein-structure knowledge.


**Reason**

> A model with general protein biochemistry knowledge can: (1) eliminate eukaryotic/mammalian-specific processes (A, C) based on the bacterial context inferable from sequence composition and codon-like patterns; (2) recognize the VGTGY and GxGxG motifs as hallmarks of SAM-dependent methyltransferases; (3) exclude D-xylose metabolism by absence of xylose-isomerase or xylulose-kinase fold signatures. This provides a multi-step reasoning path rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D are clearly incompatible with a bacterial methyltransferase. Only B (methylation) is consistent with the protein's identity. No ambiguity exists among the choices.


### Important caveats

- The GO annotation for methylation (GO:0032259) is IEA (Inferred from Electronic Annotation via UniProt keyword), not a direct experimental GO annotation. However, the underlying methylation reaction is experimentally confirmed (ECO:0000269).
- GO:0032259 is flagged as 'gocheck_obsoletion_candidate' in the current ontology, raising a question about its long-term stability, though it remains valid at the time of annotation.
- The 'primary biological process' could arguably be 'antibiotic biosynthetic process' (GO:0017000) or 'polyketide biosynthesis' rather than the general 'methylation' term, but these are not among the answer choices.
- The SAM-binding motif recognition (VGTGY, GxGxG) provides reasonable but not absolute sequence-level evidence; it is a well-established biochemistry heuristic rather than a definitive proof from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 230 aa from a bacterial organism (Streptomyces), which eliminates options A (negative regulation of chondrocyte differentiation, a eukaryotic developmental process) and C (surfactant secretion, a mammalian lung-specific process) by organism-type reasoning. The sequence contains recognizable SAM-binding methyltransferase motifs: 'GVGTGYLLDN' resembles the classic VGTGY/VIGFG motif and 'GATVLSSGVP' contains the GxGxG glycine-rich loop characteristic of Rossmann-fold methyltransferases. These structural motifs, combined with the small protein size typical of SAM-dependent methyltransferases, support option B. Option D (D-xylose metabolic process) requires TIM-barrel or kinase-fold enzymes with entirely different sequence signatures absent here.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The SAM-binding motif recognition and organism-based elimination provide a valid reasoning path, though precise motif identification requires moderate protein-structure knowledge.",
    "reason": "A model with general protein biochemistry knowledge can: (1) eliminate eukaryotic/mammalian-specific processes (A, C) based on the bacterial context inferable from sequence composition and codon-like patterns; (2) recognize the VGTGY and GxGxG motifs as hallmarks of SAM-dependent methyltransferases; (3) exclude D-xylose metabolism by absence of xylose-isomerase or xylulose-kinase fold signatures. This provides a multi-step reasoning path rather than pure lookup."
  },
  "case_id": "GO_biological_process_0158",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H8",
      "GO1",
      "C3"
    ],
    "judgment": "supported",
    "reason": "The protein (Q70KH3, AurI from Streptomyces thioluteus) is experimentally confirmed (ECO:0000269, PubMed:16292785) as a SAM-dependent O-methyltransferase catalyzing methylation of demethylluteothin to luteothin (EC 2.1.1.353). The GO term GO:0032259 'methylation' is annotated to this entry (IEA:UniProtKB-KW), and the underlying enzymatic activity is experimentally verified. Among the four choices, methylation is the only process this protein participates in. The other options (chondrocyte differentiation, surfactant secretion, D-xylose metabolism) are entirely unrelated to this bacterial methyltransferase."
  },
  "important_caveats": [
    "The GO annotation for methylation (GO:0032259) is IEA (Inferred from Electronic Annotation via UniProt keyword), not a direct experimental GO annotation. However, the underlying methylation reaction is experimentally confirmed (ECO:0000269).",
    "GO:0032259 is flagged as 'gocheck_obsoletion_candidate' in the current ontology, raising a question about its long-term stability, though it remains valid at the time of annotation.",
    "The 'primary biological process' could arguably be 'antibiotic biosynthetic process' (GO:0017000) or 'polyketide biosynthesis' rather than the general 'methylation' term, but these are not among the answer choices.",
    "The SAM-binding motif recognition (VGTGY, GxGxG) provides reasonable but not absolute sequence-level evidence; it is a well-established biochemistry heuristic rather than a definitive proof from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with a bacterial methyltransferase. Only B (methylation) is consistent with the protein's identity. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0158",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q70KH3, AurI from Streptomyces thioluteus) is experimentally confirmed (ECO:0000269, PubMed:16292785) as a SAM-dependent O-methyltransferase catalyzing methylation of demethylluteothin to luteothin (EC 2.1.1.353). The GO term GO:0032259 'methylation' is annotated to this entry (IEA:UniProtKB-KW), and the underlying enzymatic activity is experimentally verified. Among the four choices, methylation is the only process this protein participates in. The other options (chondrocyte differentiation, surfactant secretion, D-xylose metabolism) are entirely unrelated to this bacterial methyltransferase.",
    "evidence_ids": ["C4", "C5", "H4", "H8", "GO1", "C3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 230 aa from a bacterial organism (Streptomyces), which eliminates options A (negative regulation of chondrocyte differentiation, a eukaryotic developmental process) and C (surfactant secretion, a mammalian lung-specific process) by organism-type reasoning. The sequence contains recognizable SAM-binding methyltransferase motifs: 'GVGTGYLLDN' resembles the classic VGTGY/VIGFG motif and 'GATVLSSGVP' contains the GxGxG glycine-rich loop characteristic of Rossmann-fold methyltransferases. These structural motifs, combined with the small protein size typical of SAM-dependent methyltransferases, support option B. Option D (D-xylose metabolic process) requires TIM-barrel or kinase-fold enzymes with entirely different sequence signatures absent here.",
    "missing_item_specific_fact": "None critical. The SAM-binding motif recognition and organism-based elimination provide a valid reasoning path, though precise motif identification requires moderate protein-structure knowledge.",
    "reason": "A model with general protein biochemistry knowledge can: (1) eliminate eukaryotic/mammalian-specific processes (A, C) based on the bacterial context inferable from sequence composition and codon-like patterns; (2) recognize the VGTGY and GxGxG motifs as hallmarks of SAM-dependent methyltransferases; (3) exclude D-xylose metabolism by absence of xylose-isomerase or xylulose-kinase fold signatures. This provides a multi-step reasoning path rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D are clearly incompatible with a bacterial methyltransferase. Only B (methylation) is consistent with the protein's identity. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The GO annotation for methylation (GO:0032259) is IEA (Inferred from Electronic Annotation via UniProt keyword), not a direct experimental GO annotation. However, the underlying methylation reaction is experimentally confirmed (ECO:0000269).",
    "GO:0032259 is flagged as 'gocheck_obsoletion_candidate' in the current ontology, raising a question about its long-term stability, though it remains valid at the time of annotation.",
    "The 'primary biological process' could arguably be 'antibiotic biosynthetic process' (GO:0017000) or 'polyketide biosynthesis' rather than the general 'methylation' term, but these are not among the answer choices.",
    "The SAM-binding motif recognition (VGTGY, GxGxG) provides reasonable but not absolute sequence-level evidence; it is a well-established biochemistry heuristic rather than a definitive proof from sequence alone."
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

**Accession:** `Q70KH3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 58. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
"Q70KH3"
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"lineage":["Bacteria","Bacillati","Actinomycetota","Actinomycetes","Kitasatosporales","Streptomycetaceae","Streptomyces"],"scientificName":"Streptomyces thioluteus","taxonId":66431}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16292785","source":"PubMed"}],"value":"Gamma-pyrone methyltransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16292785","source":"PubMed"}],"value":"SAM-dependent pyrone methyltransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16292785","source":"PubMed"}],"value":"2.1.1.353"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Demethylluteothin O-methyltransferase"}}}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16292785","source":"PubMed"}],"value":"Methyltransferase involved in the biosynthesis of the antibiotic aureothin, a nitroaryl polyketide metabolite with antifungal, cytotoxic and insecticidal activities (PubMed:16292785). Catalyzes the methylation of demethylluteothin to luteothin (also called deoxyaureothin) (PubMed:16292785). Is specific for its gamma-pyrone substrate, and does not act on the alpha-pyrone isomer (PubMed:16292785)"}]}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH3?format=txt&versions=58)  
**Locator:** `lines 36-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 1.  
**Retrieved:** 2026-11-02T04:31:49.122851+00:00.  

```text
CC   -!- FUNCTION: Methyltransferase involved in the biosynthesis of the
CC       antibiotic aureothin, a nitroaryl polyketide metabolite with
CC       antifungal, cytotoxic and insecticidal activities (PubMed:16292785).
CC       Catalyzes the methylation of demethylluteothin to luteothin (also
CC       called deoxyaureothin) (PubMed:16292785). Is specific for its gamma-
CC       pyrone substrate, and does not act on the alpha-pyrone isomer
CC       (PubMed:16292785). {ECO:0000269|PubMed:16292785}.
```

Source SHA-256: `ecdac3ea83c9b526b46a0656f9bc8ad6168658ba01edaa0f5f3f90bf6b40cc09`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH3?format=txt&versions=58)  
**Locator:** `lines 72-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 1.  
**Retrieved:** 2026-11-02T04:31:49.122851+00:00.  

```text
DR   GO; GO:0032259; P:methylation; IEA:UniProtKB-KW.
```

Source SHA-256: `ecdac3ea83c9b526b46a0656f9bc8ad6168658ba01edaa0f5f3f90bf6b40cc09`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 184428-184438`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0032259
name: methylation
namespace: biological_process
def: "The process in which a methyl group is covalently attached to a molecule." [GOC:mah]
subset: gocheck_obsoletion_candidate
subset: goslim_chembl
xref: Reactome:R-HSA-156581 "Methylation"
xref: Wikipedia:Methylation
is_a: GO:0008152 ! metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 158. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
