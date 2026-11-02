# GO_molecular_function_0087

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — isomerase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MIRLLYLLVKPAGMSDETFRAECLRHYEMSHDVPGLHKYEVRLVAEQPTDTHVPFFDIGHVDAIGECWFKDDAAYATYMASDIRKAWFEHGKTFIGQLKPFRTAPVAGDEPAS

[Multiple Choices]
A. S-adenosyl-L-methionine binding
B. isomerase activity
C. carbohydrate binding
D. rRNA binding
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

## Luna’s full visible review

### Expected-answer support: supported

> The exact sequence matches the UniProt entry for a 4-carboxymethyl-4-methylbutenolide mutase. The entry reports experimentally supported isomerization activity, and the specific mutase activity is a subtype of isomerase activity, matching choice B.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [GO2](#evidence-go2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No clear sequence feature or supplied biological context distinguishes this specific isomerase from the listed binding functions. Recognizing the exact protein or relying on its annotated function would require protein-specific knowledge.

**Missing item-specific fact**

> The protein-specific identity and evidence that this sequence catalyzes an isomerization reaction.

**Reason**

> The key is supported by external, sequence-matched annotation and cited experimental evidence, but those facts are absent from the question input. The short sequence and choices alone do not provide a defensible distinguishing argument.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The supplied evidence supports isomerase activity; none of the other choices is indicated as a function of this protein.

### Important caveats

- The matched database entry and literature citations support the answer, but reviewer-only sources were not available to the evaluated model.
- The exact author source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for a 4-carboxymethyl-4-methylbutenolide mutase. The entry reports experimentally supported isomerization activity, and the specific mutase activity is a subtype of isomerase activity, matching choice B.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "GO2",
      "H4",
      "H5"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No clear sequence feature or supplied biological context distinguishes this specific isomerase from the listed binding functions. Recognizing the exact protein or relying on its annotated function would require protein-specific knowledge.",
    "missing_item_specific_fact": "The protein-specific identity and evidence that this sequence catalyzes an isomerization reaction.",
    "reason": "The key is supported by external, sequence-matched annotation and cited experimental evidence, but those facts are absent from the question input. The short sequence and choices alone do not provide a defensible distinguishing argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports isomerase activity; none of the other choices is indicated as a function of this protein."
  },
  "important_caveats": [
    "The matched database entry and literature citations support the answer, but reviewer-only sources were not available to the evaluated model.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `O51799`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 65. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
"O51799"
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"2241929","source":"PubMed"}],"value":"4-carboxymethyl-4-methylbut-2-en-4-olide isomerase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"2241929","source":"PubMed"}],"value":"4-methyl-2-enelactone isomerase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9461415","source":"PubMed"}],"value":"4-methylmuconolactone methylisomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"9461415","source":"PubMed"}],"value":"MLMI"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"value":"5.4.99.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4-carboxymethyl-4-methylbutenolide mutase"}}}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"value":"Isomerase involved in the degradation of 4-methylcatechol (PubMed:2241929). Catalyzes the isomerization of the dead-end metabolite 4-methylmuconolactone (4-ML) to 3-methylmuconolactone (3-ML), which can then be further degraded through a modified 3-oxoadipate pathway (PubMed:2241929, PubMed:9461415). Can also use 1-methylbislactone, but not the isomeric methyl-substituted 4-carboxymethylbut-2-en-4-olides (PubMed:2241929)"}]}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19238"}}],"reaction":{"ecNumber":"5.4.99.14","evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"name":"4-methylmuconolactone = 3-methylmuconolactone","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19237"},{"database":"ChEBI","id":"CHEBI:57883"},{"database":"ChEBI","id":"CHEBI:57888"}]}}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"id":"GO:0047469","properties":[{"key":"GoTerm","value":"F:4-carboxymethyl-4-methylbutenolide mutase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)  
**Locator:** `lines 56-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-01T06:28:15.847605+00:00.  

```text
CC   -!- FUNCTION: Isomerase involved in the degradation of 4-methylcatechol
CC       (PubMed:2241929). Catalyzes the isomerization of the dead-end
CC       metabolite 4-methylmuconolactone (4-ML) to 3-methylmuconolactone (3-
CC       ML), which can then be further degraded through a modified 3-oxoadipate
CC       pathway (PubMed:2241929, PubMed:9461415). Can also use 1-
CC       methylbislactone, but not the isomeric methyl-substituted 4-
CC       carboxymethylbut-2-en-4-olides (PubMed:2241929).
CC       {ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415}.
```

Source SHA-256: `1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)  
**Locator:** `lines 64-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-01T06:28:15.847605+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-methylmuconolactone = 3-methylmuconolactone;
CC         Xref=Rhea:RHEA:19237, ChEBI:CHEBI:57883, ChEBI:CHEBI:57888;
CC         EC=5.4.99.14; Evidence={ECO:0000269|PubMed:2241929,
CC         ECO:0000269|PubMed:9461415};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19238;
CC         Evidence={ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};
```

Source SHA-256: `1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 130892-130912`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016853
name: isomerase activity
namespace: molecular_function
def: "Catalysis of the geometric or structural changes within one molecule. Isomerase is the systematic name for any enzyme of EC class 5." [ISBN:0198506732]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_prokaryote
subset: goslim_yeast
synonym: "other isomerase activity" NARROW []
xref: EC:5.-.-.-
xref: Reactome:R-HSA-2161666 "PGA2 is isomerised to PGC2"
xref: Reactome:R-HSA-2161735 "PGC2 is isomerised to PGB2"
xref: Reactome:R-HSA-6787623 "GFUS dimer epimerises GDP-DHDMan to GDP-KDGal"
is_a: GO:0003824 ! catalytic activity
property_value: skos:exactMatch EC:5.-.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 131035-131045`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016866
name: intramolecular transferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a functional group from one position to another within a single molecule." [GOC:mah]
synonym: "intramolecular transferase activity, transferring other groups" NARROW []
synonym: "mutase activity" EXACT []
xref: EC:5.4.-.-
is_a: GO:0016853 ! isomerase activity
property_value: skos:exactMatch EC:5.4.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 87). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
