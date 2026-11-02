# GO_cellular_component_0096

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — replisome

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTNRLELSGIICRTPLRKVSPSGIPHCQFVLEHRSVQEEAGFHRQAWCQMPVIISGHENQAITHSITVGSAVTVRGFISCHKAKNGLSKMVLHAEQIELIDSGD

[Multiple Choices]
A. mannosyltransferase complex
B. replisome
C. chromosome
D. apical plasma membrane
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

> The exact sequence matches UniProt entry A6THB2, annotated as replication restart protein PriB. The record assigns it to the primosome complex by computational UniRule evidence; the ontology places the primosome as part of the replisome. This supports B, though it is not experimental localization evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [GO4](#evidence-go4), [GO6](#evidence-go6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence gives no clear targeting signal or other reliable feature that identifies a replisome-associated protein rather than a chromosome-associated protein. Its short length and lack of an obvious membrane-targeting segment may make D less likely, but do not distinguish B from C.


**Missing item-specific fact**

> Identifying this sequence as PriB, or equivalent protein-specific knowledge that it associates with the primosome/replisome, is needed to select B.


**Reason**

> The decisive function and cellular-component association are not established by the supplied context or readily distinguishable from the sequence alone; they depend on protein-specific annotation or prior knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The annotation supports the primosome, which is part of the replisome; the ontology also places the replisome at a replication fork that is part of a chromosome. B is the more specific listed choice, but the question does not say to choose the most specific component, so C is also defensible as a broader location.


### Important caveats

- The sequence match is exact, but the cited PriB name is assigned by a computational HAMAP rule and the GO component annotation is IEA, not experimental evidence.
- The actual author source snapshot is unknown; the reviewer evidence includes a historical entry with a matching sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence gives no clear targeting signal or other reliable feature that identifies a replisome-associated protein rather than a chromosome-associated protein. Its short length and lack of an obvious membrane-targeting segment may make D less likely, but do not distinguish B from C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this sequence as PriB, or equivalent protein-specific knowledge that it associates with the primosome/replisome, is needed to select B.",
    "reason": "The decisive function and cellular-component association are not established by the supplied context or readily distinguishable from the sequence alone; they depend on protein-specific annotation or prior knowledge."
  },
  "case_id": "GO_cellular_component_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "GO4",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A6THB2, annotated as replication restart protein PriB. The record assigns it to the primosome complex by computational UniRule evidence; the ontology places the primosome as part of the replisome. This supports B, though it is not experimental localization evidence."
  },
  "important_caveats": [
    "The sequence match is exact, but the cited PriB name is assigned by a computational HAMAP rule and the GO component annotation is IEA, not experimental evidence.",
    "The actual author source snapshot is unknown; the reviewer evidence includes a historical entry with a matching sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The annotation supports the primosome, which is part of the replisome; the ontology also places the replisome at a replication fork that is part of a chromosome. B is the more specific listed choice, but the question does not say to choose the most specific component, so C is also defensible as a broader location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A6THB2, annotated as replication restart protein PriB. The record assigns it to the primosome complex by computational UniRule evidence; the ontology places the primosome as part of the replisome. This supports B, though it is not experimental localization evidence.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "GO4", "GO6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence gives no clear targeting signal or other reliable feature that identifies a replisome-associated protein rather than a chromosome-associated protein. Its short length and lack of an obvious membrane-targeting segment may make D less likely, but do not distinguish B from C.",
    "missing_item_specific_fact": "Identifying this sequence as PriB, or equivalent protein-specific knowledge that it associates with the primosome/replisome, is needed to select B.",
    "reason": "The decisive function and cellular-component association are not established by the supplied context or readily distinguishable from the sequence alone; they depend on protein-specific annotation or prior knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The annotation supports the primosome, which is part of the replisome; the ontology also places the replisome at a replication fork that is part of a chromosome. B is the more specific listed choice, but the question does not say to choose the most specific component, so C is also defensible as a broader location."
  },
  "important_caveats": [
    "The sequence match is exact, but the cited PriB name is assigned by a computational HAMAP rule and the GO component annotation is IEA, not experimental evidence.",
    "The actual author source snapshot is unknown; the reviewer evidence includes a historical entry with a matching sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A6THB2 (PriB, replication restart protein, Klebsiella pneumoniae). The direct GO annotation is GO:1990077 (primosome complex, evidence IEA:UniProtKB-UniRule). Per the GO ontology, primosome complex is part_of GO:0030894 (replisome). Thus 'replisome' is a valid parent-term annotation. The evidence code is computational (IEA/HAMAP rule), not experimental, but PriB's role in replication restart and primosome assembly is well established. The annotation applies to the exact 104-aa sequence supplied.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [GO4](#evidence-go4), [GO6](#evidence-go6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could note the absence of eukaryotic-specific features (no signal peptide, no transmembrane segments) to argue against 'apical plasma membrane' (D), and the lack of glycosyltransferase motifs to argue against 'mannosyltransferase complex' (A). However, distinguishing 'replisome' (B) from 'chromosome' (C) requires knowing that PriB is a replication-restart/primosome protein rather than a general chromosomal protein. The 104-aa sequence lacks obvious helicase, polymerase, or primase catalytic motifs; its OB-fold nucleic-acid-binding character would be consistent with any DNA-associated complex.


**Missing item-specific fact**

> Recognition that this specific 104-aa sequence is PriB (replication restart protein) and its association with the primosome/replisome machinery, rather than a generic chromosomal protein. The UniProt annotation (IEA:UniProtKB-UniRule) provides this, but it is not derivable from general sequence features alone.


**Reason**

> Eliminating D and A uses general biological knowledge (bacterial proteins lack apical membrane; no glycosyltransferase motifs). But choosing B over C requires knowing the protein is specifically a replication-restart/primosome component rather than a generic DNA-binding chromosomal protein. This is an item-specific annotation fact, not a generalizable sequence-structure inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The direct GO annotation is 'primosome complex' (not listed). Primosome is part_of replisome, and replisome is part_of replication fork, which is part_of chromosome. Both 'replisome' and 'chromosome' are valid ancestor terms. The question asks for the 'primary' component, which conventionally means the most specific term, favoring B. However, without the primosome option, a model reasoning from general knowledge might select 'chromosome' as a defensible broader annotation. The distinction between B and C is not resolvable from the sequence alone.


### Important caveats

- The GO annotation evidence code is IEA (Inferred from Electronic Annotation via HAMAP rule), not experimental. PriB's replisome association is well-established in the literature but the UniProt entry itself relies on computational inference.
- The direct annotation is 'primosome complex' (GO:1990077), not 'replisome' (GO:0030894). The author's key uses a parent term via the part_of relationship.
- The organism (Klebsiella pneumoniae) is not stated in the question, yet it is critical for ruling out 'apical plasma membrane' (a eukaryotic epithelial term). A model would need to infer prokaryotic origin from sequence features or general knowledge.
- Sequence match is exact (SHA256 confirmed) across both current and historical (v62) UniProt snapshots.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could note the absence of eukaryotic-specific features (no signal peptide, no transmembrane segments) to argue against 'apical plasma membrane' (D), and the lack of glycosyltransferase motifs to argue against 'mannosyltransferase complex' (A). However, distinguishing 'replisome' (B) from 'chromosome' (C) requires knowing that PriB is a replication-restart/primosome protein rather than a general chromosomal protein. The 104-aa sequence lacks obvious helicase, polymerase, or primase catalytic motifs; its OB-fold nucleic-acid-binding character would be consistent with any DNA-associated complex.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this specific 104-aa sequence is PriB (replication restart protein) and its association with the primosome/replisome machinery, rather than a generic chromosomal protein. The UniProt annotation (IEA:UniProtKB-UniRule) provides this, but it is not derivable from general sequence features alone.",
    "reason": "Eliminating D and A uses general biological knowledge (bacterial proteins lack apical membrane; no glycosyltransferase motifs). But choosing B over C requires knowing the protein is specifically a replication-restart/primosome component rather than a generic DNA-binding chromosomal protein. This is an item-specific annotation fact, not a generalizable sequence-structure inference."
  },
  "case_id": "GO_cellular_component_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "GO4",
      "GO6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A6THB2 (PriB, replication restart protein, Klebsiella pneumoniae). The direct GO annotation is GO:1990077 (primosome complex, evidence IEA:UniProtKB-UniRule). Per the GO ontology, primosome complex is part_of GO:0030894 (replisome). Thus 'replisome' is a valid parent-term annotation. The evidence code is computational (IEA/HAMAP rule), not experimental, but PriB's role in replication restart and primosome assembly is well established. The annotation applies to the exact 104-aa sequence supplied."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA (Inferred from Electronic Annotation via HAMAP rule), not experimental. PriB's replisome association is well-established in the literature but the UniProt entry itself relies on computational inference.",
    "The direct annotation is 'primosome complex' (GO:1990077), not 'replisome' (GO:0030894). The author's key uses a parent term via the part_of relationship.",
    "The organism (Klebsiella pneumoniae) is not stated in the question, yet it is critical for ruling out 'apical plasma membrane' (a eukaryotic epithelial term). A model would need to infer prokaryotic origin from sequence features or general knowledge.",
    "Sequence match is exact (SHA256 confirmed) across both current and historical (v62) UniProt snapshots."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The direct GO annotation is 'primosome complex' (not listed). Primosome is part_of replisome, and replisome is part_of replication fork, which is part_of chromosome. Both 'replisome' and 'chromosome' are valid ancestor terms. The question asks for the 'primary' component, which conventionally means the most specific term, favoring B. However, without the primosome option, a model reasoning from general knowledge might select 'chromosome' as a defensible broader annotation. The distinction between B and C is not resolvable from the sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A6THB2 (PriB, replication restart protein, Klebsiella pneumoniae). The direct GO annotation is GO:1990077 (primosome complex, evidence IEA:UniProtKB-UniRule). Per the GO ontology, primosome complex is part_of GO:0030894 (replisome). Thus 'replisome' is a valid parent-term annotation. The evidence code is computational (IEA/HAMAP rule), not experimental, but PriB's role in replication restart and primosome assembly is well established. The annotation applies to the exact 104-aa sequence supplied.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "GO4", "GO6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could note the absence of eukaryotic-specific features (no signal peptide, no transmembrane segments) to argue against 'apical plasma membrane' (D), and the lack of glycosyltransferase motifs to argue against 'mannosyltransferase complex' (A). However, distinguishing 'replisome' (B) from 'chromosome' (C) requires knowing that PriB is a replication-restart/primosome protein rather than a general chromosomal protein. The 104-aa sequence lacks obvious helicase, polymerase, or primase catalytic motifs; its OB-fold nucleic-acid-binding character would be consistent with any DNA-associated complex.",
    "missing_item_specific_fact": "Recognition that this specific 104-aa sequence is PriB (replication restart protein) and its association with the primosome/replisome machinery, rather than a generic chromosomal protein. The UniProt annotation (IEA:UniProtKB-UniRule) provides this, but it is not derivable from general sequence features alone.",
    "reason": "Eliminating D and A uses general biological knowledge (bacterial proteins lack apical membrane; no glycosyltransferase motifs). But choosing B over C requires knowing the protein is specifically a replication-restart/primosome component rather than a generic DNA-binding chromosomal protein. This is an item-specific annotation fact, not a generalizable sequence-structure inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The direct GO annotation is 'primosome complex' (not listed). Primosome is part_of replisome, and replisome is part_of replication fork, which is part_of chromosome. Both 'replisome' and 'chromosome' are valid ancestor terms. The question asks for the 'primary' component, which conventionally means the most specific term, favoring B. However, without the primosome option, a model reasoning from general knowledge might select 'chromosome' as a defensible broader annotation. The distinction between B and C is not resolvable from the sequence alone."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA (Inferred from Electronic Annotation via HAMAP rule), not experimental. PriB's replisome association is well-established in the literature but the UniProt entry itself relies on computational inference.",
    "The direct annotation is 'primosome complex' (GO:1990077), not 'replisome' (GO:0030894). The author's key uses a parent term via the part_of relationship.",
    "The organism (Klebsiella pneumoniae) is not stated in the question, yet it is critical for ruling out 'apical plasma membrane' (a eukaryotic epithelial term). A model would need to infer prokaryotic origin from sequence features or general knowledge.",
    "Sequence match is exact (SHA256 confirmed) across both current and historical (v62) UniProt snapshots."
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

**Accession:** `A6THB2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 62. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6THB2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.676093+00:00.  

```json
"A6THB2"
```

Source SHA-256: `112d26e808dc1fd38595dddb8c79bc1f7daa2f798cbd64dd9e82faff5c780e1c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6THB2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.676093+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00720","source":"HAMAP-Rule"}],"value":"Replication restart protein PriB"}}}
```

Source SHA-256: `112d26e808dc1fd38595dddb8c79bc1f7daa2f798cbd64dd9e82faff5c780e1c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6THB2.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.676093+00:00.  

```json
{"database":"GO","id":"GO:1990077","properties":[{"key":"GoTerm","value":"C:primosome complex"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniRule"}]}
```

Source SHA-256: `112d26e808dc1fd38595dddb8c79bc1f7daa2f798cbd64dd9e82faff5c780e1c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6THB2?format=txt&versions=62)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 2.  
**Retrieved:** 2026-11-01T06:27:50.187758+00:00.  

```text
ID   PRIB_KLEP7              Reviewed;         104 AA.
AC   A6THB2;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 2.
DT   28-JAN-2026, entry version 62.
DE   RecName: Full=Replication restart protein PriB {ECO:0000255|HAMAP-Rule:MF_00720};
GN   Name=priB {ECO:0000255|HAMAP-Rule:MF_00720};
GN   ORFNames=KPN_04595 {ECO:0000312|EMBL:ABR79946.1};
OS   Klebsiella pneumoniae subsp. pneumoniae (strain ATCC 700721 / MGH 78578).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Enterobacteriaceae; Klebsiella/Raoultella group;
OC   Klebsiella; Klebsiella pneumoniae complex.
OX   NCBI_TaxID=272620;
```

Source SHA-256: `dab4e075ff062d16bde88f88b9273b736fe7b9722b7009b1ba54f0a04e92086c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6THB2?format=txt&versions=62)  
**Locator:** `lines 87-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 2.  
**Retrieved:** 2026-11-01T06:27:50.187758+00:00.  

```text
DR   GO; GO:1990077; C:primosome complex; IEA:UniProtKB-UniRule.
```

Source SHA-256: `dab4e075ff062d16bde88f88b9273b736fe7b9722b7009b1ba54f0a04e92086c`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 171246-171258`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0030894
name: replisome
namespace: cellular_component
def: "A multi-component enzymatic machine at the replication fork which mediates DNA replication. Includes DNA primase, one or more DNA polymerases, DNA helicases, and other proteins." [GOC:mah, GOC:vw]
subset: goslim_pir
synonym: "DNA synthesome complex" RELATED [CORUM:1001]
synonym: "RC complex" RELATED [CORUM:309, PMID:12006500]
synonym: "replication-competent complex" RELATED [CORUM:309, PMID:12006500]
xref: Wikipedia:Replisome
is_a: GO:0032993 ! protein-DNA complex
relationship: part_of GO:0005657 ! replication fork

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 549032-549040`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990077
name: primosome complex
namespace: cellular_component
def: "Any of a family of protein complexes that form at the origin of replication or stalled replication forks and function in replication primer synthesis in all organisms. Early complexes initiate double-stranded DNA unwinding. The core unit consists of a replicative helicase and a primase. The helicase further unwinds the DNA and recruits the polymerase machinery. The primase synthesizes RNA primers that act as templates for complementary stand replication by the polymerase machinery. The primosome contains a number of associated proteins and protein complexes and contributes to the processes of replication initiation, lagging strand elongation, and replication restart." [GOC:bhm, GOC:mah, PMID:21856207]
synonym: "primosome" EXACT []
is_a: GO:0032993 ! protein-DNA complex
relationship: part_of GO:0030894 ! replisome

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
