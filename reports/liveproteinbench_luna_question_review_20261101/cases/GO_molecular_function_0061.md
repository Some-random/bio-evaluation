# GO_molecular_function_0061

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — folic acid transmembrane transporter activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MIEKSNNPFLSIDPIVERTKSNGEGLPLLSEKTKKGFDFTQIVVYLVGLSDGLTHLASLAIYYLFKDYFRLTPYQVSLILMYPYIPFILKPVIALITDSFSIFGMRRKPYLFLFSLFQSLNFLALAFLNLSVIQASLILFFISLCASFCTTVAEALVVESSMGQTYSQGTNKVTEFIASKAIGSLSVAYFSGYFLEKMPREYIFIATSIFPLIISLSCLFLKEKEYSTNRNIFNQLSDLIKFINTPIFLGPFLYIFVYMSGPDYDDAFFFFCTNKLGFRPSFMGTLRLTYGIASLIGIIIYRVFLKNCSLRKTLIITTLVSFPIYISPIILTEHINKFLGISNELFVLSGGFLIEAITEIQLLPLFILTANICQPGLEASVFATILSVKNLGSLTKKGTSSFITYLMKIDSYNFDNLSLYILTCGFFLLFSLTLVPLLPNEEHIEKLKNKETSKG

[Multiple Choices]
A. glutaminase activity
B. mannitol-1-phosphate 5-dehydrogenase activity
C. aspartic-type endopeptidase activity
D. folic acid transmembrane transporter activity
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

> The sequence exactly matches the reviewed Plasmodium falciparum folate transporter 2 entry. That entry attributes folate transport to experimental evidence and includes the matching GO term for folic acid transmembrane transporter activity. This supports D, while recognizing the database evidence is attributed to a cited study rather than independently assessed here.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has numerous long hydrophobic stretches consistent with a multi-pass membrane protein. Of the options, D is the transporter activity; the other choices are enzyme activities, making the membrane-protein topology a meaningful discriminator among these choices.

**Missing item-specific fact**

> The sequence topology alone does not establish folate as the transported substrate; that specificity is protein-specific. However, the choices contrast a transporter with three enzyme activities, so the topology provides grounds to select D without knowing the protein's database identity.

**Reason**

> The supplied sequence provides a concrete, biologically relevant topology signal that distinguishes the sole transmembrane-transporter option from the enzyme options. It does not independently prove the substrate specificity.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed choices, the multi-pass membrane-protein topology supports the transporter option rather than the enzyme activities.

### Important caveats

- The substrate-specific folate function is supported by reviewer-only annotation evidence, which was not supplied to the evaluated model.
- Hydrophobic topology supports a membrane protein but is not, on its own, proof of folate transport.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the reviewed Plasmodium falciparum folate transporter 2 entry. That entry attributes folate transport to experimental evidence and includes the matching GO term for folic acid transmembrane transporter activity. This supports D, while recognizing the database evidence is attributed to a cited study rather than independently assessed here.",
    "evidence_ids": [
      "C1",
      "C5",
      "C8",
      "H3",
      "H6"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has numerous long hydrophobic stretches consistent with a multi-pass membrane protein. Of the options, D is the transporter activity; the other choices are enzyme activities, making the membrane-protein topology a meaningful discriminator among these choices.",
    "missing_item_specific_fact": "The sequence topology alone does not establish folate as the transported substrate; that specificity is protein-specific. However, the choices contrast a transporter with three enzyme activities, so the topology provides grounds to select D without knowing the protein's database identity.",
    "reason": "The supplied sequence provides a concrete, biologically relevant topology signal that distinguishes the sole transmembrane-transporter option from the enzyme options. It does not independently prove the substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the multi-pass membrane-protein topology supports the transporter option rather than the enzyme activities."
  },
  "important_caveats": [
    "The substrate-specific folate function is supported by reviewer-only annotation evidence, which was not supplied to the evaluated model.",
    "Hydrophobic topology supports a membrane protein but is not, on its own, proof of folate transport."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q8IIK1`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 107. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
"Q8IIK1"
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21998306","source":"PubMed"}],"value":"Folate transporter with broad substrate specificity (PubMed:21998306). Transports folic acid, folinic acid, pteroic acid, dihydropteroic acid, the folate precursor p-amino benzoic acid (pABA) and the human folate catabolite pABA monoglutamate (PubMed:21998306). Can transport 5-methyltetrahydrofolate with low efficiency (PubMed:21998306)"}]}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIK1.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:24.989052+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"21998306","source":"PubMed"}],"id":"GO:0008517","properties":[{"key":"GoTerm","value":"F:folic acid transmembrane transporter activity"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `8631bdcc6b7274da8651ba15077787a2ccc347d9d53951e8b63a7d9807d07940`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 36-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
CC   -!- FUNCTION: Folate transporter with broad substrate specificity
CC       (PubMed:21998306). Transports folic acid, folinic acid, pteroic acid,
CC       dihydropteroic acid, the folate precursor p-amino benzoic acid (pABA)
CC       and the human folate catabolite pABA monoglutamate (PubMed:21998306).
CC       Can transport 5-methyltetrahydrofolate with low efficiency
CC       (PubMed:21998306). {ECO:0000269|PubMed:21998306}.
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIK1?format=txt&versions=107)  
**Locator:** `lines 81-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-01T06:28:40.005689+00:00.  

```text
DR   GO; GO:0008517; F:folic acid transmembrane transporter activity; IDA:GeneDB.
```

Source SHA-256: `c315cecd25012a01e06e0aefb68dd205d1cf053c48966bc36b4c33d3c6385707`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 61). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
