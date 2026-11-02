# GO_cellular_component_0038

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — transcription regulator complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGHLQAARPYGSPTSMHASLHMPEPNMGPSGMAFPSMAPELYAPPQPLRAPDATSQPAPKAYACSTCGKGFARRSDLARHERIHTGVRPHVCEYPNCGKQFIQRSALTVHQRVHTGEKPHMCERCGKPFSDSSSLARHRRIHSGKRPYKCPYADCQKTFTRRTTLTRHQNHHTGTVEDAARATAEVLARNSVARSASARPTRSEGDQISNHGSPLSTPSPAQRTMSMSPSAELAAANGMQHQYNGNSSLPAHMRTDLHSSSPAATTSSGFSSNVRPTSHPNAYGAAPPPTTLEPSIEGSQGPGSAVGSPHMSSVGWASPSHVASPAHSNSGGNSSYVYPDPDSSYPTNAAAQGQMFYSAAMGLQRPGSAEPGAQSAYKPRQNELWAA

[Multiple Choices]
A. RNA polymerase II transcription regulator complex
B. transcription regulator complex
C. axon
D. protein-DNA complex
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

> The exact matched sequence has a UniProt GO annotation for transcription regulator complex (GO:0005667), but that annotation is computationally inferred (IEA:TreeGrafter), not experimental evidence of membership in a particular complex. Experimental evidence supports nuclear localization, not the complex annotation itself.

Citations as saved: [C8](#evidence-c8), [H6](#evidence-h6), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's C2H2 zinc-finger motifs and basic regions are consistent with a DNA-binding transcription factor, favoring transcription-related choices over axon. They do not establish which transcription-regulator complex it occupies or whether it specifically acts in an RNA polymerase II regulator complex.


**Missing item-specific fact**

> The protein-specific complex annotation or evidence of its complex membership and RNA polymerase II regulatory specificity is absent from the supplied input.


**Reason**

> Sequence-based reasoning supports a broad transcription-factor role but does not distinguish the nested choices A and B. Selecting B as the assigned GO term depends on the protein-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A is a narrower subtype of B. The sequence does not resolve whether this transcription factor acts specifically in an RNA polymerase II transcription regulator complex; the supplied choices and wording do not provide that distinction.


### Important caveats

- The sequence matches the cited UniProt record, including the historical entry; the author’s exact source snapshot is unknown.
- The experimental nuclear localization annotation does not itself establish localization in either listed transcription-regulator complex.
- The GO annotation supports B as the database-assigned term, but its computational evidence should not be mistaken for an experimental complex-membership measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's C2H2 zinc-finger motifs and basic regions are consistent with a DNA-binding transcription factor, favoring transcription-related choices over axon. They do not establish which transcription-regulator complex it occupies or whether it specifically acts in an RNA polymerase II regulator complex.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific complex annotation or evidence of its complex membership and RNA polymerase II regulatory specificity is absent from the supplied input.",
    "reason": "Sequence-based reasoning supports a broad transcription-factor role but does not distinguish the nested choices A and B. Selecting B as the assigned GO term depends on the protein-specific annotation."
  },
  "case_id": "GO_cellular_component_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H6",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact matched sequence has a UniProt GO annotation for transcription regulator complex (GO:0005667), but that annotation is computationally inferred (IEA:TreeGrafter), not experimental evidence of membership in a particular complex. Experimental evidence supports nuclear localization, not the complex annotation itself."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, including the historical entry; the author’s exact source snapshot is unknown.",
    "The experimental nuclear localization annotation does not itself establish localization in either listed transcription-regulator complex.",
    "The GO annotation supports B as the database-assigned term, but its computational evidence should not be mistaken for an experimental complex-membership measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A is a narrower subtype of B. The sequence does not resolve whether this transcription factor acts specifically in an RNA polymerase II transcription regulator complex; the supplied choices and wording do not provide that distinction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact matched sequence has a UniProt GO annotation for transcription regulator complex (GO:0005667), but that annotation is computationally inferred (IEA:TreeGrafter), not experimental evidence of membership in a particular complex. Experimental evidence supports nuclear localization, not the complex annotation itself.",
    "evidence_ids": ["C8", "H6", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's C2H2 zinc-finger motifs and basic regions are consistent with a DNA-binding transcription factor, favoring transcription-related choices over axon. They do not establish which transcription-regulator complex it occupies or whether it specifically acts in an RNA polymerase II regulator complex.",
    "missing_item_specific_fact": "The protein-specific complex annotation or evidence of its complex membership and RNA polymerase II regulatory specificity is absent from the supplied input.",
    "reason": "Sequence-based reasoning supports a broad transcription-factor role but does not distinguish the nested choices A and B. Selecting B as the assigned GO term depends on the protein-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A is a narrower subtype of B. The sequence does not resolve whether this transcription factor acts specifically in an RNA polymerase II transcription regulator complex; the supplied choices and wording do not provide that distinction."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, including the historical entry; the author’s exact source snapshot is unknown.",
    "The experimental nuclear localization annotation does not itself establish localization in either listed transcription-regulator complex.",
    "The GO annotation supports B as the database-assigned term, but its computational evidence should not be mistaken for an experimental complex-membership measurement."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A9P4XV22) annotates GO:0005667 'transcription regulator complex' (C8/H6) for this protein. The protein is identified as a C2H2-type transcription factor ZAP1 (C4), and the sequence contains multiple canonical C2H2 zinc finger motifs (e.g., 'CGKGFARRSDLARHERIHTGVRPHVCEYPNCGKQFIQRSALTVHQRVHTGEKPHMCERCGKPFSDSSSLARHRRIHSGKRPYKCPYADCQKTFTRRTTLTRHQNHHTG'). The annotation evidence is IEA:TreeGrafter (computational inference), while the experimental evidence (ECO:0000269, PubMed:39611846) supports 'Nucleus' (GO:0005634, C7/H5), which is not among the choices. Among the four options, B is the only term actually annotated for this protein and is biologically appropriate for a zinc finger transcription factor.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H6](#evidence-h6), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple canonical C2H2 zinc finger motifs (C-x2-4-C-x12-H-x3-5-H patterns), identifying this as a DNA-binding transcription factor. This eliminates C (axon: a neuronal structure absent in fungi, and irrelevant to a nuclear TF) and D (protein-DNA complex: the GO definition explicitly states 'Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here'). Between A and B, B ('transcription regulator complex') is the parent GO term and the broader, more conservative classification for a general zinc finger TF without demonstrated specific Pol II complex membership. Choosing the parent term over the child term (A, 'RNA polymerase II transcription regulator complex') is defensible without specific experimental evidence of Pol II-specific complex assembly.


**Missing item-specific fact**

> The specific experimental demonstration that this ZAP1 protein is part of a Pol II-specific regulatory complex (which would justify A over B) is absent. However, the absence of such evidence supports the broader term B.


**Reason**

> The C2H2 zinc finger motif recognition from the raw sequence provides a concrete biological argument to identify this as a transcription factor. The GO term definitions (GO1, GO3) provide explicit criteria to eliminate D. The fungal origin (inferable from sequence composition and the absence of neuronal context) eliminates C. The A-vs-B distinction is resolved by the principle of choosing the broader annotated term absent specific Pol II complex evidence. This constitutes a multi-step biological reasoning chain, though the A-vs-B margin is narrower than the C/D eliminations.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> In fungi, all protein-coding genes are transcribed by RNA Pol II, so a fungal zinc finger TF could arguably be classified under the more specific term A ('RNA polymerase II transcription regulator complex'). However, the UniProt annotation assigns only the broader term B (GO:0005667, IEA:TreeGrafter), and A (GO:0090575) is not annotated. The distinction between A and B depends on whether one requires explicit evidence of Pol II-specific complex membership or accepts the broader functional classification. This is a genuine but non-fatal ambiguity; B remains the annotated and more conservative choice.


### Important caveats

- The GO:0005667 annotation is IEA:TreeGrafter (computational phylogenetic grafting), not experimental. The only experimental subcellular localization evidence is for 'Nucleus' (GO:0005634), which is not offered as a choice.
- The sequence is 388 aa from Cryphonectria parasitica (a fungus); the organism context is not provided in the question input but is inferable from sequence composition.
- The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot is unknown but the historical entry version 11 (released 2026-01-28) contains the same annotation.
- The identity of the accession (A0A9P4XV22) was inferred by the reviewer from dataset metadata; this was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple canonical C2H2 zinc finger motifs (C-x2-4-C-x12-H-x3-5-H patterns), identifying this as a DNA-binding transcription factor. This eliminates C (axon: a neuronal structure absent in fungi, and irrelevant to a nuclear TF) and D (protein-DNA complex: the GO definition explicitly states 'Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here'). Between A and B, B ('transcription regulator complex') is the parent GO term and the broader, more conservative classification for a general zinc finger TF without demonstrated specific Pol II complex membership. Choosing the parent term over the child term (A, 'RNA polymerase II transcription regulator complex') is defensible without specific experimental evidence of Pol II-specific complex assembly.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific experimental demonstration that this ZAP1 protein is part of a Pol II-specific regulatory complex (which would justify A over B) is absent. However, the absence of such evidence supports the broader term B.",
    "reason": "The C2H2 zinc finger motif recognition from the raw sequence provides a concrete biological argument to identify this as a transcription factor. The GO term definitions (GO1, GO3) provide explicit criteria to eliminate D. The fungal origin (inferable from sequence composition and the absence of neuronal context) eliminates C. The A-vs-B distinction is resolved by the principle of choosing the broader annotated term absent specific Pol II complex evidence. This constitutes a multi-step biological reasoning chain, though the A-vs-B margin is narrower than the C/D eliminations."
  },
  "case_id": "GO_cellular_component_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9P4XV22) annotates GO:0005667 'transcription regulator complex' (C8/H6) for this protein. The protein is identified as a C2H2-type transcription factor ZAP1 (C4), and the sequence contains multiple canonical C2H2 zinc finger motifs (e.g., 'CGKGFARRSDLARHERIHTGVRPHVCEYPNCGKQFIQRSALTVHQRVHTGEKPHMCERCGKPFSDSSSLARHRRIHSGKRPYKCPYADCQKTFTRRTTLTRHQNHHTG'). The annotation evidence is IEA:TreeGrafter (computational inference), while the experimental evidence (ECO:0000269, PubMed:39611846) supports 'Nucleus' (GO:0005634, C7/H5), which is not among the choices. Among the four options, B is the only term actually annotated for this protein and is biologically appropriate for a zinc finger transcription factor."
  },
  "important_caveats": [
    "The GO:0005667 annotation is IEA:TreeGrafter (computational phylogenetic grafting), not experimental. The only experimental subcellular localization evidence is for 'Nucleus' (GO:0005634), which is not offered as a choice.",
    "The sequence is 388 aa from Cryphonectria parasitica (a fungus); the organism context is not provided in the question input but is inferable from sequence composition.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot is unknown but the historical entry version 11 (released 2026-01-28) contains the same annotation.",
    "The identity of the accession (A0A9P4XV22) was inferred by the reviewer from dataset metadata; this was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "In fungi, all protein-coding genes are transcribed by RNA Pol II, so a fungal zinc finger TF could arguably be classified under the more specific term A ('RNA polymerase II transcription regulator complex'). However, the UniProt annotation assigns only the broader term B (GO:0005667, IEA:TreeGrafter), and A (GO:0090575) is not annotated. The distinction between A and B depends on whether one requires explicit evidence of Pol II-specific complex membership or accepts the broader functional classification. This is a genuine but non-fatal ambiguity; B remains the annotated and more conservative choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9P4XV22) annotates GO:0005667 'transcription regulator complex' (C8/H6) for this protein. The protein is identified as a C2H2-type transcription factor ZAP1 (C4), and the sequence contains multiple canonical C2H2 zinc finger motifs (e.g., 'CGKGFARRSDLARHERIHTGVRPHVCEYPNCGKQFIQRSALTVHQRVHTGEKPHMCERCGKPFSDSSSLARHRRIHSGKRPYKCPYADCQKTFTRRTTLTRHQNHHTG'). The annotation evidence is IEA:TreeGrafter (computational inference), while the experimental evidence (ECO:0000269, PubMed:39611846) supports 'Nucleus' (GO:0005634, C7/H5), which is not among the choices. Among the four options, B is the only term actually annotated for this protein and is biologically appropriate for a zinc finger transcription factor.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H6", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple canonical C2H2 zinc finger motifs (C-x2-4-C-x12-H-x3-5-H patterns), identifying this as a DNA-binding transcription factor. This eliminates C (axon: a neuronal structure absent in fungi, and irrelevant to a nuclear TF) and D (protein-DNA complex: the GO definition explicitly states 'Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here'). Between A and B, B ('transcription regulator complex') is the parent GO term and the broader, more conservative classification for a general zinc finger TF without demonstrated specific Pol II complex membership. Choosing the parent term over the child term (A, 'RNA polymerase II transcription regulator complex') is defensible without specific experimental evidence of Pol II-specific complex assembly.",
    "missing_item_specific_fact": "The specific experimental demonstration that this ZAP1 protein is part of a Pol II-specific regulatory complex (which would justify A over B) is absent. However, the absence of such evidence supports the broader term B.",
    "reason": "The C2H2 zinc finger motif recognition from the raw sequence provides a concrete biological argument to identify this as a transcription factor. The GO term definitions (GO1, GO3) provide explicit criteria to eliminate D. The fungal origin (inferable from sequence composition and the absence of neuronal context) eliminates C. The A-vs-B distinction is resolved by the principle of choosing the broader annotated term absent specific Pol II complex evidence. This constitutes a multi-step biological reasoning chain, though the A-vs-B margin is narrower than the C/D eliminations."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "In fungi, all protein-coding genes are transcribed by RNA Pol II, so a fungal zinc finger TF could arguably be classified under the more specific term A ('RNA polymerase II transcription regulator complex'). However, the UniProt annotation assigns only the broader term B (GO:0005667, IEA:TreeGrafter), and A (GO:0090575) is not annotated. The distinction between A and B depends on whether one requires explicit evidence of Pol II-specific complex membership or accepts the broader functional classification. This is a genuine but non-fatal ambiguity; B remains the annotated and more conservative choice."
  },
  "important_caveats": [
    "The GO:0005667 annotation is IEA:TreeGrafter (computational phylogenetic grafting), not experimental. The only experimental subcellular localization evidence is for 'Nucleus' (GO:0005634), which is not offered as a choice.",
    "The sequence is 388 aa from Cryphonectria parasitica (a fungus); the organism context is not provided in the question input but is inferable from sequence composition.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark author's source snapshot is unknown but the historical entry version 11 (released 2026-01-28) contains the same annotation.",
    "The identity of the accession (A0A9P4XV22) was inferred by the reviewer from dataset metadata; this was not available to the evaluated model."
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

**Accession:** `A0A9P4XV22` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 11. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.008633+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39611846","source":"PubMed"}],"value":"C2H2-type transcription factor ZAP1"}}}
```

Source SHA-256: `eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.008633+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"id":"SL-0191","value":"Nucleus"}}]}
```

Source SHA-256: `eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.008633+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"39611846","source":"PubMed"}],"id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9P4XV22.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:16.008633+00:00.  

```json
{"database":"GO","id":"GO:0005667","properties":[{"key":"GoTerm","value":"C:transcription regulator complex"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `eb112fe54186da42ef70d1d66ed09d8890bc8ad2e336ba13391e7372aaac0732`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)  
**Locator:** `lines 53-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:26:18.672095+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; IEA:UniProtKB-SubCell.
```

Source SHA-256: `ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9P4XV22?format=txt&versions=11)  
**Locator:** `lines 54-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:26:18.672095+00:00.  

```text
DR   GO; GO:0005667; C:transcription regulator complex; IEA:TreeGrafter.
```

Source SHA-256: `ca54309309117c1baaf6e783eddf9a63f645605d769672bf9109d1945016d803`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58346-58358`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005667
name: transcription regulator complex
namespace: cellular_component
alt_id: GO:0044797
alt_id: GO:0044798
def: "A protein complex that is capable of associating with DNA by direct binding, or via other DNA-binding proteins or complexes, and regulating transcription." [GOC:jl]
subset: goslim_pir
synonym: "cytoplasmic transcription factor complex" RELATED []
synonym: "nuclear transcription factor complex" RELATED []
synonym: "transcription factor complex" RELATED []
is_a: GO:0032991 ! protein-containing complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 192695-192704`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0032993
name: protein-DNA complex
namespace: cellular_component
def: "A macromolecular complex containing both protein and DNA molecules." [GOC:mah]
comment: Note that this term is intended to classify complexes that have DNA as one of the members of the complex, that is, the complex does not exist if DNA is not present. Protein complexes that interact with DNA e.g. transcription factor complexes should not be classified here.
subset: goslim_pir
synonym: "DNA-protein complex" EXACT [GOC:mah]
is_a: GO:0032991 ! protein-containing complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
