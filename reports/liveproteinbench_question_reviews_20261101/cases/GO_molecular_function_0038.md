# GO_molecular_function_0038

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — host cell surface receptor binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches the mumps-virus hemagglutinin-neuraminidase protein. UniProt reports attachment to sialic-acid-containing cell receptors, supported by cited experimental studies; the specific GO annotation for host cell surface receptor binding is computationally assigned by InterPro.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C9](#evidence-c9), [C12](#evidence-c12).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic membrane-anchor region followed by a large extracellular domain, consistent with a viral surface glycoprotein that can engage host-cell receptors. It lacks the recognizable kinase and nucleotide-binding features expected for choices A, B, and D, so C is meaningfully favored among these options.


**Missing item-specific fact**

> The exact receptor specificity and experimentally established receptor-binding activity are not supplied; those would require protein-specific evidence, but are not necessary to favor C over these choices.


**Reason**

> The sequence architecture and contrast with the proposed intracellular catalytic or cofactor-binding functions provide a concrete basis for selecting C. This supports relative choice discrimination, not deduction of the precise ligand or all functions of the protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, receptor binding is the defensible choice. The protein also has neuraminidase activity, but that function is not offered as an option.


### Important caveats

- The receptor-binding GO annotation itself is IEA:InterPro, while the functional description cites experimental studies.
- The protein is a hemagglutinin-neuraminidase, so calling receptor binding its singular primary molecular function omits its enzymatic sialidase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic membrane-anchor region followed by a large extracellular domain, consistent with a viral surface glycoprotein that can engage host-cell receptors. It lacks the recognizable kinase and nucleotide-binding features expected for choices A, B, and D, so C is meaningfully favored among these options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact receptor specificity and experimentally established receptor-binding activity are not supplied; those would require protein-specific evidence, but are not necessary to favor C over these choices.",
    "reason": "The sequence architecture and contrast with the proposed intracellular catalytic or cofactor-binding functions provide a concrete basis for selecting C. This supports relative choice discrimination, not deduction of the precise ligand or all functions of the protein."
  },
  "case_id": "GO_molecular_function_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C9",
      "C12"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the mumps-virus hemagglutinin-neuraminidase protein. UniProt reports attachment to sialic-acid-containing cell receptors, supported by cited experimental studies; the specific GO annotation for host cell surface receptor binding is computationally assigned by InterPro."
  },
  "important_caveats": [
    "The receptor-binding GO annotation itself is IEA:InterPro, while the functional description cites experimental studies.",
    "The protein is a hemagglutinin-neuraminidase, so calling receptor binding its singular primary molecular function omits its enzymatic sialidase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, receptor binding is the defensible choice. The protein also has neuraminidase activity, but that function is not offered as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the mumps-virus hemagglutinin-neuraminidase protein. UniProt reports attachment to sialic-acid-containing cell receptors, supported by cited experimental studies; the specific GO annotation for host cell surface receptor binding is computationally assigned by InterPro.",
    "evidence_ids": ["C1", "C5", "C9", "C12"]
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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q9WAF5 (Mumps orthorubulavirus Hemagglutinin-neuraminidase, HN). GO:0046789 'host cell surface receptor binding' is annotated (IEA:InterPro, evidence C9/H9). The FUNCTION comment (C5/H5) describes experimental evidence (PubMed:27671656, PubMed:31118251) that the protein 'Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection' and 'Binds to the glycan motifs sialyl Lewis (SLe) and GM2 ganglioside.' Among the four options, only C applies to this protein; the neuraminidase/sialidase catalytic activity (GO:0004308) is not offered as a distractor, and options A, B, D have no supporting annotation.

Citations as saved: [C5](#evidence-c5), [C9](#evidence-c9), [H5](#evidence-h5), [H9](#evidence-h9), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could partially eliminate D (no kinase catalytic motifs such as HRD, DFG, or glycine-rich loop), B (no Rossmann-fold NAD-binding pattern), and A (no phosphatase motifs) by noting the absence of characteristic enzymatic sequence signatures. The N-terminal hydrophobic stretch suggests a transmembrane anchor, and multiple N-X-S/T glycosylation sequons plus cysteine-rich regions are consistent with a viral surface glycoprotein. However, these features are generic to many membrane glycoproteins and do not positively identify 'host cell surface receptor binding' as opposed to, e.g., a receptor or channel.


**Missing item-specific fact**

> Recognition that this 582-aa sequence is the paramyxovirus (Mumps) Hemagglutinin-neuraminidase (HN) attachment protein, whose primary receptor-binding role is to attach virions to sialic acid-containing host cell surface receptors. This identification is essentially a sequence-to-database lookup; no purely sequence-intrinsic motif uniquely encodes 'host cell surface receptor binding' versus other membrane-protein functions.


**Reason**

> Positive confirmation of option C requires identifying the protein as a viral attachment glycoprotein. While absence of kinase/NAD/phosphatase motifs helps eliminate D, B, A, the remaining inference that a TM-domain glycoprotein must be a 'host cell surface receptor binding' protein is too weak to constitute genuine reasoning without knowing the specific viral protein family.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is bifunctional (hemagglutinin + neuraminidase), but the neuraminidase/sialidase activity (GO:0004308, EC 3.2.1.18) is not among the four choices. Options A, B, and D have no annotation or mechanistic support for this protein. Only C is applicable, so no ambiguity among the offered options.


### Important caveats

- The GO:0046789 annotation carries evidence code IEA:InterPro (inferred from electronic annotation), not direct experimental evidence, though the FUNCTION comment itself cites experimental studies (PubMed:27671656, 31118251).
- The protein's catalytic neuraminidase activity (EC 3.2.1.18, GO:0004308 with EXP evidence) is arguably equally 'primary' but is absent from the option set, making the question effectively about the hemagglutinin (binding) half of the bifunctional enzyme.
- Identity of the protein (Q9WAF5) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.
- The benchmark sequence matches the UniProt canonical sequence exactly (582 aa, SHA-256 confirmed).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could partially eliminate D (no kinase catalytic motifs such as HRD, DFG, or glycine-rich loop), B (no Rossmann-fold NAD-binding pattern), and A (no phosphatase motifs) by noting the absence of characteristic enzymatic sequence signatures. The N-terminal hydrophobic stretch suggests a transmembrane anchor, and multiple N-X-S/T glycosylation sequons plus cysteine-rich regions are consistent with a viral surface glycoprotein. However, these features are generic to many membrane glycoproteins and do not positively identify 'host cell surface receptor binding' as opposed to, e.g., a receptor or channel.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this 582-aa sequence is the paramyxovirus (Mumps) Hemagglutinin-neuraminidase (HN) attachment protein, whose primary receptor-binding role is to attach virions to sialic acid-containing host cell surface receptors. This identification is essentially a sequence-to-database lookup; no purely sequence-intrinsic motif uniquely encodes 'host cell surface receptor binding' versus other membrane-protein functions.",
    "reason": "Positive confirmation of option C requires identifying the protein as a viral attachment glycoprotein. While absence of kinase/NAD/phosphatase motifs helps eliminate D, B, A, the remaining inference that a TM-domain glycoprotein must be a 'host cell surface receptor binding' protein is too weak to constitute genuine reasoning without knowing the specific viral protein family."
  },
  "case_id": "GO_molecular_function_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C9",
      "H5",
      "H9",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9WAF5 (Mumps orthorubulavirus Hemagglutinin-neuraminidase, HN). GO:0046789 'host cell surface receptor binding' is annotated (IEA:InterPro, evidence C9/H9). The FUNCTION comment (C5/H5) describes experimental evidence (PubMed:27671656, PubMed:31118251) that the protein 'Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection' and 'Binds to the glycan motifs sialyl Lewis (SLe) and GM2 ganglioside.' Among the four options, only C applies to this protein; the neuraminidase/sialidase catalytic activity (GO:0004308) is not offered as a distractor, and options A, B, D have no supporting annotation."
  },
  "important_caveats": [
    "The GO:0046789 annotation carries evidence code IEA:InterPro (inferred from electronic annotation), not direct experimental evidence, though the FUNCTION comment itself cites experimental studies (PubMed:27671656, 31118251).",
    "The protein's catalytic neuraminidase activity (EC 3.2.1.18, GO:0004308 with EXP evidence) is arguably equally 'primary' but is absent from the option set, making the question effectively about the hemagglutinin (binding) half of the bifunctional enzyme.",
    "Identity of the protein (Q9WAF5) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.",
    "The benchmark sequence matches the UniProt canonical sequence exactly (582 aa, SHA-256 confirmed)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (hemagglutinin + neuraminidase), but the neuraminidase/sialidase activity (GO:0004308, EC 3.2.1.18) is not among the four choices. Options A, B, and D have no annotation or mechanistic support for this protein. Only C is applicable, so no ambiguity among the offered options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q9WAF5 (Mumps orthorubulavirus Hemagglutinin-neuraminidase, HN). GO:0046789 'host cell surface receptor binding' is annotated (IEA:InterPro, evidence C9/H9). The FUNCTION comment (C5/H5) describes experimental evidence (PubMed:27671656, PubMed:31118251) that the protein 'Attaches the virus to alpha-2,3-linked sialic acid-containing cell receptors and thereby initiating infection' and 'Binds to the glycan motifs sialyl Lewis (SLe) and GM2 ganglioside.' Among the four options, only C applies to this protein; the neuraminidase/sialidase catalytic activity (GO:0004308) is not offered as a distractor, and options A, B, D have no supporting annotation.",
    "evidence_ids": ["C5", "C9", "H5", "H9", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could partially eliminate D (no kinase catalytic motifs such as HRD, DFG, or glycine-rich loop), B (no Rossmann-fold NAD-binding pattern), and A (no phosphatase motifs) by noting the absence of characteristic enzymatic sequence signatures. The N-terminal hydrophobic stretch suggests a transmembrane anchor, and multiple N-X-S/T glycosylation sequons plus cysteine-rich regions are consistent with a viral surface glycoprotein. However, these features are generic to many membrane glycoproteins and do not positively identify 'host cell surface receptor binding' as opposed to, e.g., a receptor or channel.",
    "missing_item_specific_fact": "Recognition that this 582-aa sequence is the paramyxovirus (Mumps) Hemagglutinin-neuraminidase (HN) attachment protein, whose primary receptor-binding role is to attach virions to sialic acid-containing host cell surface receptors. This identification is essentially a sequence-to-database lookup; no purely sequence-intrinsic motif uniquely encodes 'host cell surface receptor binding' versus other membrane-protein functions.",
    "reason": "Positive confirmation of option C requires identifying the protein as a viral attachment glycoprotein. While absence of kinase/NAD/phosphatase motifs helps eliminate D, B, A, the remaining inference that a TM-domain glycoprotein must be a 'host cell surface receptor binding' protein is too weak to constitute genuine reasoning without knowing the specific viral protein family."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is bifunctional (hemagglutinin + neuraminidase), but the neuraminidase/sialidase activity (GO:0004308, EC 3.2.1.18) is not among the four choices. Options A, B, and D have no annotation or mechanistic support for this protein. Only C is applicable, so no ambiguity among the offered options."
  },
  "important_caveats": [
    "The GO:0046789 annotation carries evidence code IEA:InterPro (inferred from electronic annotation), not direct experimental evidence, though the FUNCTION comment itself cites experimental studies (PubMed:27671656, 31118251).",
    "The protein's catalytic neuraminidase activity (EC 3.2.1.18, GO:0004308 with EXP evidence) is arguably equally 'primary' but is absent from the option set, making the question effectively about the hemagglutinin (binding) half of the bifunctional enzyme.",
    "Identity of the protein (Q9WAF5) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.",
    "The benchmark sequence matches the UniProt canonical sequence exactly (582 aa, SHA-256 confirmed)."
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

**Accession:** `Q9WAF5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 130. Exact author snapshot unknown.

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

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)  
**Locator:** `lines 82-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-02T04:33:57.899829+00:00.  

```text
CC   -!- FUNCTION: Attaches the virus to alpha-2,3-linked sialic acid-containing
CC       cell receptors and thereby initiating infection (PubMed:27671656).
CC       Binding of HN protein to the receptor induces a conformational change
CC       that allows the F protein to trigger virion/cell membranes fusion (By
CC       similarity). Binds to the glycan motifs sialyl Lewis (SLe) and GM2
CC       ganglioside (GM2-glycan) (PubMed:31118251).
CC       {ECO:0000250|UniProtKB:Q786F2, ECO:0000269|PubMed:27671656,
CC       ECO:0000269|PubMed:31118251}.
```

Source SHA-256: `eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)  
**Locator:** `lines 132-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-02T04:33:57.899829+00:00.  

```text
DR   GO; GO:0046789; F:host cell surface receptor binding; IEA:InterPro.
```

Source SHA-256: `eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 280483-280492`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0046789
name: host cell surface receptor binding
namespace: molecular_function
def: "Binding to a receptor on the host cell surface." [GOC:ai, PMID:11511370]
subset: goslim_chembl
synonym: "cell surface antigen activity, host-interacting" RELATED []
synonym: "cell surface receptor ligand" RELATED []
is_a: GO:0046812 ! host cell surface binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
