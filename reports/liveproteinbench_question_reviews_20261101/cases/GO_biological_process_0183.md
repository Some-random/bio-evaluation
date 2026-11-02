# GO_biological_process_0183

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — xylan catabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFTTLLTAVATAVSAVTASPLEALKRGIQPGTGVHDGYFYSFWTDGRGYVDFNNGPRGSYRVSWSNVNNWVGGKGWNPGPPRRIAYNGTWNNWNVNSYLALYGWTTNPLVEYYIVEAYGSYNPSSGAARLGTIEDDGGVYDIYRTRRINQPSIIGTASFDQYWSVRRQKRVGGTIDTGKHFDEWRRQGNLQLGAWNYMIMATEGYQSSGSAEIEVRSLD

[Multiple Choices]
A. cell redox homeostasis
B. cellular response to oxidative stress
C. response to mannitol
D. xylan catabolic process
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

> The exact sequence matches a UniProt entry whose function annotation says the protein hydrolyzes xylan, with experimental evidence cited; its GO annotation is also xylan catabolic process. The GO annotation itself is computationally inferred, but the function annotation supports choice D.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5), [H5](#evidence-h5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted protein, and the compact enzyme-like sequence makes an extracellular catabolic enzyme more plausible than cellular redox or stress-response processes.


**Missing item-specific fact**

> The sequence does not state its substrate; identifying xylan breakdown requires recognizing or looking up this protein's family and substrate specificity, or having experimental characterization.


**Reason**

> The sequence offers broad clues favoring a secreted enzyme, but those clues alone do not establish xylan as its substrate rather than another possible substrate. The protein-specific substrate/function is needed to distinguish D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein's xylan-hydrolysis function supports D; the other options are not supported by the supplied sequence or the matched function evidence.


### Important caveats

- The cited UniProt function annotation assigns experimental evidence, but the underlying paper was not independently reviewed here.
- The GO annotation for xylan catabolic process is IEA; it is distinct from the experimentally supported function annotation.
- The reviewer-only accession and database evidence were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and the compact enzyme-like sequence makes an extracellular catabolic enzyme more plausible than cellular redox or stress-response processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence does not state its substrate; identifying xylan breakdown requires recognizing or looking up this protein's family and substrate specificity, or having experimental characterization.",
    "reason": "The sequence offers broad clues favoring a secreted enzyme, but those clues alone do not establish xylan as its substrate rather than another possible substrate. The protein-specific substrate/function is needed to distinguish D."
  },
  "case_id": "GO_biological_process_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5",
      "H5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry whose function annotation says the protein hydrolyzes xylan, with experimental evidence cited; its GO annotation is also xylan catabolic process. The GO annotation itself is computationally inferred, but the function annotation supports choice D."
  },
  "important_caveats": [
    "The cited UniProt function annotation assigns experimental evidence, but the underlying paper was not independently reviewed here.",
    "The GO annotation for xylan catabolic process is IEA; it is distinct from the experimentally supported function annotation.",
    "The reviewer-only accession and database evidence were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's xylan-hydrolysis function supports D; the other options are not supported by the supplied sequence or the matched function evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry whose function annotation says the protein hydrolyzes xylan, with experimental evidence cited; its GO annotation is also xylan catabolic process. The GO annotation itself is computationally inferred, but the function annotation supports choice D.",
    "evidence_ids": ["H3", "C5", "H5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted protein, and the compact enzyme-like sequence makes an extracellular catabolic enzyme more plausible than cellular redox or stress-response processes.",
    "missing_item_specific_fact": "The sequence does not state its substrate; identifying xylan breakdown requires recognizing or looking up this protein's family and substrate specificity, or having experimental characterization.",
    "reason": "The sequence offers broad clues favoring a secreted enzyme, but those clues alone do not establish xylan as its substrate rather than another possible substrate. The protein-specific substrate/function is needed to distinguish D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's xylan-hydrolysis function supports D; the other options are not supported by the supplied sequence or the matched function evidence."
  },
  "important_caveats": [
    "The cited UniProt function annotation assigns experimental evidence, but the underlying paper was not independently reviewed here.",
    "The GO annotation for xylan catabolic process is IEA; it is distinct from the experimentally supported function annotation.",
    "The reviewer-only accession and database evidence were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt V9TS54 (XY11A_HUMIN), an experimentally characterized Endo-1,4-beta-xylanase 11A (EC 3.2.1.8) from Humicola insolens. The FUNCTION comment (ECO:0000269, PubMed:24262572) states it hydrolyzes xylan. The PATHWAY comment assigns 'Glycan degradation; xylan degradation.' GO:0045493 (xylan catabolic process) is annotated via IEA:UniProtKB-UniPathway, with the underlying pathway assignment supported by experimental evidence. The protein's catalytic activity directly constitutes xylan breakdown, matching the GO term definition.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 221-residue sequence contains an N-terminal signal peptide (MVSFTTLLTAVATAVSAVTASPLEA), indicating a secreted protein. The mature domain contains ~8-9 tryptophan residues densely packed in a compact fold, along with characteristic 'GG' motifs (VGGKGW, VGGTID) and conserved Asp residues — hallmarks of the GH11 xylanase 'beta-jelly roll' family. Small (~200-250 AA) secreted enzymes with multiple Trp and GG motifs are diagnostic of GH11 endo-xylanases. The sequence lacks thioredoxin/glutaredoxin motifs (eliminating A), peroxidase/catalase/SOD motifs (eliminating B), and mannitol/sugar-sensing motifs (eliminating C). A knowledgeable biochemist can reason: small secreted protein + clustered Trp + GG motifs → GH11 → xylanase → xylan catabolic process.


**Missing item-specific fact**

> None critical. Recognition of GH11 family signatures (multiple Trp, GG motifs, small secreted size) is standard glycoside hydrolase biochemistry knowledge, not a single-database lookup.


**Reason**

> The sequence provides concrete structural/biochemical signatures (size, signal peptide, Trp density, GG motifs) that distinguish a GH11 xylanase from redox enzymes, oxidative stress proteins, and mannitol-related proteins. This constitutes a defensible biological reasoning chain using general knowledge of enzyme families, not reliance on a single database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (redox homeostasis, oxidative stress response, mannitol response) are readily eliminated by the absence of corresponding sequence motifs. The GH11 xylanase signature is distinctive enough to single out option D without ambiguity.


### Important caveats

- The GO annotation is IEA (Inferred from Electronic Annotation) via UniProtKB-UniPathway, not a direct experimental GO assignment, though the underlying pathway is experimentally supported.
- Recognition of GH11 family signatures requires specialized knowledge of glycoside hydrolase families; a model without this training would struggle to distinguish xylanase from other small secreted enzymes.
- The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot date is unknown, though the sequence version (1) has been stable since 2014.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 221-residue sequence contains an N-terminal signal peptide (MVSFTTLLTAVATAVSAVTASPLEA), indicating a secreted protein. The mature domain contains ~8-9 tryptophan residues densely packed in a compact fold, along with characteristic 'GG' motifs (VGGKGW, VGGTID) and conserved Asp residues — hallmarks of the GH11 xylanase 'beta-jelly roll' family. Small (~200-250 AA) secreted enzymes with multiple Trp and GG motifs are diagnostic of GH11 endo-xylanases. The sequence lacks thioredoxin/glutaredoxin motifs (eliminating A), peroxidase/catalase/SOD motifs (eliminating B), and mannitol/sugar-sensing motifs (eliminating C). A knowledgeable biochemist can reason: small secreted protein + clustered Trp + GG motifs → GH11 → xylanase → xylan catabolic process.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of GH11 family signatures (multiple Trp, GG motifs, small secreted size) is standard glycoside hydrolase biochemistry knowledge, not a single-database lookup.",
    "reason": "The sequence provides concrete structural/biochemical signatures (size, signal peptide, Trp density, GG motifs) that distinguish a GH11 xylanase from redox enzymes, oxidative stress proteins, and mannitol-related proteins. This constitutes a defensible biological reasoning chain using general knowledge of enzyme families, not reliance on a single database annotation."
  },
  "case_id": "GO_biological_process_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt V9TS54 (XY11A_HUMIN), an experimentally characterized Endo-1,4-beta-xylanase 11A (EC 3.2.1.8) from Humicola insolens. The FUNCTION comment (ECO:0000269, PubMed:24262572) states it hydrolyzes xylan. The PATHWAY comment assigns 'Glycan degradation; xylan degradation.' GO:0045493 (xylan catabolic process) is annotated via IEA:UniProtKB-UniPathway, with the underlying pathway assignment supported by experimental evidence. The protein's catalytic activity directly constitutes xylan breakdown, matching the GO term definition."
  },
  "important_caveats": [
    "The GO annotation is IEA (Inferred from Electronic Annotation) via UniProtKB-UniPathway, not a direct experimental GO assignment, though the underlying pathway is experimentally supported.",
    "Recognition of GH11 family signatures requires specialized knowledge of glycoside hydrolase families; a model without this training would struggle to distinguish xylanase from other small secreted enzymes.",
    "The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot date is unknown, though the sequence version (1) has been stable since 2014."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (redox homeostasis, oxidative stress response, mannitol response) are readily eliminated by the absence of corresponding sequence motifs. The GH11 xylanase signature is distinctive enough to single out option D without ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt V9TS54 (XY11A_HUMIN), an experimentally characterized Endo-1,4-beta-xylanase 11A (EC 3.2.1.8) from Humicola insolens. The FUNCTION comment (ECO:0000269, PubMed:24262572) states it hydrolyzes xylan. The PATHWAY comment assigns 'Glycan degradation; xylan degradation.' GO:0045493 (xylan catabolic process) is annotated via IEA:UniProtKB-UniPathway, with the underlying pathway assignment supported by experimental evidence. The protein's catalytic activity directly constitutes xylan breakdown, matching the GO term definition.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 221-residue sequence contains an N-terminal signal peptide (MVSFTTLLTAVATAVSAVTASPLEA), indicating a secreted protein. The mature domain contains ~8-9 tryptophan residues densely packed in a compact fold, along with characteristic 'GG' motifs (VGGKGW, VGGTID) and conserved Asp residues — hallmarks of the GH11 xylanase 'beta-jelly roll' family. Small (~200-250 AA) secreted enzymes with multiple Trp and GG motifs are diagnostic of GH11 endo-xylanases. The sequence lacks thioredoxin/glutaredoxin motifs (eliminating A), peroxidase/catalase/SOD motifs (eliminating B), and mannitol/sugar-sensing motifs (eliminating C). A knowledgeable biochemist can reason: small secreted protein + clustered Trp + GG motifs → GH11 → xylanase → xylan catabolic process.",
    "missing_item_specific_fact": "None critical. Recognition of GH11 family signatures (multiple Trp, GG motifs, small secreted size) is standard glycoside hydrolase biochemistry knowledge, not a single-database lookup.",
    "reason": "The sequence provides concrete structural/biochemical signatures (size, signal peptide, Trp density, GG motifs) that distinguish a GH11 xylanase from redox enzymes, oxidative stress proteins, and mannitol-related proteins. This constitutes a defensible biological reasoning chain using general knowledge of enzyme families, not reliance on a single database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (redox homeostasis, oxidative stress response, mannitol response) are readily eliminated by the absence of corresponding sequence motifs. The GH11 xylanase signature is distinctive enough to single out option D without ambiguity."
  },
  "important_caveats": [
    "The GO annotation is IEA (Inferred from Electronic Annotation) via UniProtKB-UniPathway, not a direct experimental GO assignment, though the underlying pathway is experimentally supported.",
    "Recognition of GH11 family signatures requires specialized knowledge of glycoside hydrolase families; a model without this training would struggle to distinguish xylanase from other small secreted enzymes.",
    "The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot date is unknown, though the sequence version (1) has been stable since 2014."
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

**Accession:** `V9TS54` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 39. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.137210+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1,4-beta-D-xylan xylanohydrolase 11A"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase 11A"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"24262572","source":"PubMed"}],"value":"Xylanase 11A"}]}}
```

Source SHA-256: `53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.137210+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a major structural heterogeneous polysaccharide found in plant biomass representing the second most abundant polysaccharide in the biosphere, after cellulose (PubMed:24262572). Is an alkali-tolerant enzyme, exhibiting 50.6% of activity at pH 9.0, and 26.9% even at pH 10.0 (PubMed:24262572)"}]}
```

Source SHA-256: `53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.137210+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU362015","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"24262572","source":"PubMed"}],"value":"Glycan degradation; xylan degradation"}]}
```

Source SHA-256: `53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V9TS54.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:30.137210+00:00.  

```json
{"database":"GO","id":"GO:0045493","properties":[{"key":"GoTerm","value":"P:xylan catabolic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniPathway"}]}
```

Source SHA-256: `53c73dbe7d403276bee2acc0f3aa08144adabd770e1e4b76b5d290b9edaa0a7e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)  
**Locator:** `lines 27-32`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-01T06:28:53.416982+00:00.  

```text
CC   -!- FUNCTION: Endo-1,4-beta-xylanase involved in the hydrolysis of xylan, a
CC       major structural heterogeneous polysaccharide found in plant biomass
CC       representing the second most abundant polysaccharide in the biosphere,
CC       after cellulose (PubMed:24262572). Is an alkali-tolerant enzyme,
CC       exhibiting 50.6% of activity at pH 9.0, and 26.9% even at pH 10.0
CC       (PubMed:24262572). {ECO:0000269|PubMed:24262572}.
```

Source SHA-256: `a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)  
**Locator:** `lines 48-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-01T06:28:53.416982+00:00.  

```text
CC   -!- PATHWAY: Glycan degradation; xylan degradation.
CC       {ECO:0000255|RuleBase:RU362015, ECO:0000269|PubMed:24262572}.
```

Source SHA-256: `a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V9TS54?format=txt&versions=39)  
**Locator:** `lines 73-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 39 / 1.  
**Retrieved:** 2026-11-01T06:28:53.416982+00:00.  

```text
DR   GO; GO:0045493; P:xylan catabolic process; IEA:UniProtKB-UniPathway.
```

Source SHA-256: `a074e123d2ec0589aa06f4931d85860d82aaf183072ecb88102fc2c6e967dd34`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 265164-265174`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0045493
name: xylan catabolic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the breakdown of xylan, a polymer containing a beta-1,4-linked D-xylose backbone." [GOC:curators, PMID:11931668]
synonym: "xylan breakdown" EXACT []
synonym: "xylan catabolism" EXACT []
synonym: "xylan degradation" EXACT []
is_a: GO:0045491 ! xylan metabolic process
is_a: GO:2000895 ! hemicellulose catabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 183. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
