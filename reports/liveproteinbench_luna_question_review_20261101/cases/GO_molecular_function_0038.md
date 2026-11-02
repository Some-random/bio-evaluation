# GO_molecular_function_0038

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — host cell surface receptor binding

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQLSSIADKIRESATMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATIRTGKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYISMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPTGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGNQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. polynucleotide 5'-phosphatase activity
B. NAD+ binding
C. host cell surface receptor binding
D. protein serine/threonine kinase activity
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

> The sequence matches the mumps-virus hemagglutinin-neuraminidase protein. UniProt reports attachment to sialic-acid-containing cell receptors, supported by cited experimental studies; the specific GO annotation for host cell surface receptor binding is computationally assigned by InterPro.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [C9](#evidence-c9), [C12](#evidence-c12).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic membrane-anchor region followed by a large extracellular domain, consistent with a viral surface glycoprotein that can engage host-cell receptors. It lacks the recognizable kinase and nucleotide-binding features expected for choices A, B, and D, so C is meaningfully favored among these options.

**Missing item-specific fact**

> The exact receptor specificity and experimentally established receptor-binding activity are not supplied; those would require protein-specific evidence, but are not necessary to favor C over these choices.

**Reason**

> The sequence architecture and contrast with the proposed intracellular catalytic or cofactor-binding functions provide a concrete basis for selecting C. This supports relative choice discrimination, not deduction of the precise ligand or all functions of the protein.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed options, receptor binding is the defensible choice. The protein also has neuraminidase activity, but that function is not offered as an option.

### Important caveats

- The receptor-binding GO annotation itself is IEA:InterPro, while the functional description cites experimental studies.
- The protein is a hemagglutinin-neuraminidase, so calling receptor binding its singular primary molecular function omits its enzymatic sialidase activity.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the mumps-virus hemagglutinin-neuraminidase protein. UniProt reports attachment to sialic-acid-containing cell receptors, supported by cited experimental studies; the specific GO annotation for host cell surface receptor binding is computationally assigned by InterPro.",
    "evidence_ids": [
      "C1",
      "C5",
      "C9",
      "C12"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic membrane-anchor region followed by a large extracellular domain, consistent with a viral surface glycoprotein that can engage host-cell receptors. It lacks the recognizable kinase and nucleotide-binding features expected for choices A, B, and D, so C is meaningfully favored among these options.",
    "missing_item_specific_fact": "The exact receptor specificity and experimentally established receptor-binding activity are not supplied; those would require protein-specific evidence, but are not necessary to favor C over these choices.",
    "reason": "The sequence architecture and contrast with the proposed intracellular catalytic or cofactor-binding functions provide a concrete basis for selecting C. This supports relative choice discrimination, not deduction of the precise ligand or all functions of the protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, receptor binding is the defensible choice. The protein also has neuraminidase activity, but that function is not offered as an option."
  },
  "important_caveats": [
    "The receptor-binding GO annotation itself is IEA:InterPro, while the functional description cites experimental studies.",
    "The protein is a hemagglutinin-neuraminidase, so calling receptor binding its singular primary molecular function omits its enzymatic sialidase activity."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9WAF5`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 130. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
"Q9WAF5"
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q786F2","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"27671656","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31118251","source":"PubMed"}],"value":"Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection (PubMed:27671656). Binding of HN protein to the receptor induces a conformational change that allows the F protein to trigger virion/cell membranes fusion (By similarity). Binds to the glycan motifs sialyl Lewis (SLe) and GM2 ganglioside (GM2-glycan) (PubMed:31118251)"}]}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"database":"GO","id":"GO:0046789","properties":[{"key":"GoTerm","value":"F:host cell surface receptor binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"citation":{"authors":["Kubota M.","Takeuchi K.","Watanabe S.","Ohno S.","Matsuoka R.","Kohda D.","Nakakita S.I.","Hiramatsu H.","Suzuki Y.","Nakayama T.","Terada T.","Shimizu K.","Shimizu N.","Shiroishi M.","Yanagi Y.","Hashiguchi T."],"citationCrossReferences":[{"database":"PubMed","id":"27671656"},{"database":"DOI","id":"10.1073/pnas.1608383113"}],"citationType":"journal article","firstPage":"11579","id":"27671656","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"11584","publicationDate":"2016","title":"Trisaccharide containing alpha2,3-linked sialic acid is a receptor for mumps virus.","volume":"113"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5B2C","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"5B2D","source":"PDB"}],"referenceNumber":7,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.18 ANGSTROMS) OF 106-582","GLYCOSYLATION AT ASN-284; ASN-329; ASN-400; ASN-448 AND ASN-507","DISULFIDE BONDS","FUNCTION","SUBUNIT","MUTAGENESIS OF TYR-369"]}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 38). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
