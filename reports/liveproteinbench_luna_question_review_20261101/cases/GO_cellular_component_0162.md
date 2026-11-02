# GO_cellular_component_0162

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MQVTSLLILVCFIAAFQVFSRASSPVNCKWDSYGPWSECNGCTKTQTRRRSVAVYGQYGGYPCEGSAFETQSCKPERGCPTEEGCGDRFRCFSGQCISKSLVCNGDPDCEEDGADEDKCENVANPSCNIDKPPPNIELTGYGYNVVTGQGKKRVINTKSFGGQCRKVFSGDGKDFYRLSGNILSYTFQVKVDNDFNYEFYNSSWSYIKHTSTEQNTFYSWKGLFSHSRNTYGHGSAKEEIDTKMKSYKLLVVQNTVEVAQFTNNNPEFLQVAEPFWKELSHLPTLYDYSAYRRLIDQYGTHYLQSGSLGGEYRVLFYVDSGSAKETGFQSDQDNACSSADFQFLFTSSADQRCMKQLETEKSTSGNKGRLLRGKPLVRGGDSGFVADLSFLDLDNPAGNKQRYSSWAGSVTRLPQVIKEKLAPLYELVKEVPCASVKRLYLKRAIEEYFDEFDPCHCRPCQNGGLAIVVETQCQCLCKPYTFGSACEQGVLVGDQAGGVDGGWNCWSSWSPCVQGKRTRSRECNNPPPRDDGKSCLGETTESKQCEDQDLEKLRLLEPHCFHSSLAPKEFCLSPPALKDGFVQGEGTMVPVGQSVVYACDEGYSLIGDPVARCGEDLQWLVGEMHCQKLACVLPGEMNGMQSHPQKPFYMVGEKVTLSCVGGMSLEGPSTLLCGSSLKWSPELKDAKCVQKATSTPPPAAPACQPWEKLQNSKCICKMPYECGSSLDVCARDESRNKILSLTICKMHVVHCHKRNYTLVGKESCTLPSPAEKVCGACPIWSKCDAQNGKCICREASECQTAGYRICVEVNGKEETMSECEAGILRCRGQSISITAIKPCAEEAAQ

[Multiple Choices]
A. host cell nucleus
B. P-body
C. plasma membrane
D. perinuclear region of cytoplasm
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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence matches mouse complement component C7. Its annotation says it is secreted as a soluble protein and inserts into the target-cell membrane; a GO annotation also places it at the plasma membrane. This supports C among the listed choices, with the qualification that membrane insertion occurs in the complement context.

Cited evidence: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal peptide supports entry into the secretory pathway, making a cytosolic P-body or nuclear location unlikely. But secretion alone does not distinguish plasma-membrane insertion from other extracellular fates.

**Missing item-specific fact**

> The fact that this particular protein is complement C7, a soluble secreted protein that inserts into target-cell membranes as part of complement activity.

**Reason**

> The sequence offers broad clues about secretion, but selecting plasma membrane over the other options requires protein-specific functional or localization knowledge not supplied in the question.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> C is supported by the target-cell membrane annotation. However, the protein is also described as secreted and soluble, so plasma membrane should not be read as evidence that it is a constitutive plasma-membrane resident.

### Important caveats

- The subcellular-location annotation is transferred from human C7 (ECO:0000250); the plasma-membrane GO annotation is NAS:ComplexPortal.
- The sequence match and annotation support the key, but the question's use of “primary” location is imprecise for a protein secreted in soluble form that inserts into target-cell membranes.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_cellular_component_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches mouse complement component C7. Its annotation says it is secreted as a soluble protein and inserts into the target-cell membrane; a GO annotation also places it at the plasma membrane. This supports C among the listed choices, with the qualification that membrane insertion occurs in the complement context.",
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H2",
      "H6"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal peptide supports entry into the secretory pathway, making a cytosolic P-body or nuclear location unlikely. But secretion alone does not distinguish plasma-membrane insertion from other extracellular fates.",
    "missing_item_specific_fact": "The fact that this particular protein is complement C7, a soluble secreted protein that inserts into target-cell membranes as part of complement activity.",
    "reason": "The sequence offers broad clues about secretion, but selecting plasma membrane over the other options requires protein-specific functional or localization knowledge not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is supported by the target-cell membrane annotation. However, the protein is also described as secreted and soluble, so plasma membrane should not be read as evidence that it is a constitutive plasma-membrane resident."
  },
  "important_caveats": [
    "The subcellular-location annotation is transferred from human C7 (ECO:0000250); the plasma-membrane GO annotation is NAS:ComplexPortal.",
    "The sequence match and annotation support the key, but the question's use of “primary” location is imprecise for a protein secreted in soluble form that inserts into target-cell membranes."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `D3YXF5`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 111. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Complement component C7"}}}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10643","source":"UniProtKB"}],"value":"Secreted as soluble protein. Inserts into the cell membrane of target cells"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10643","source":"UniProtKB"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P10643","source":"UniProtKB"}],"id":"SL-0451","value":"Target cell membrane"}}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/uniProtKBCrossReferences/39`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"database":"GO","id":"GO:0005579","properties":[{"key":"GoTerm","value":"C:membrane attack complex"},{"key":"GoEvidenceType","value":"ISO:GO_Central"}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3YXF5.json)  
**Locator:** `/uniProtKBCrossReferences/41`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:45.100729+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000303","id":"30552328","source":"PubMed"}],"id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"NAS:ComplexPortal"}]}
```

Source SHA-256: `55824c468bad99d86484b91307c62a1409deecde122a11e3c5d814db122530d2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)  
**Locator:** `lines 49-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 2.  
**Retrieved:** 2026-11-02T04:27:47.074801+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000250|UniProtKB:P10643}. Target
CC       cell membrane {ECO:0000250|UniProtKB:P10643}. Note=Secreted as soluble
CC       protein. Inserts into the cell membrane of target cells.
CC       {ECO:0000250|UniProtKB:P10643}.
```

Source SHA-256: `94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3YXF5?format=txt&versions=111)  
**Locator:** `lines 100-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 2.  
**Retrieved:** 2026-11-02T04:27:47.074801+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; NAS:ComplexPortal.
```

Source SHA-256: `94d86c30e47a04ba17ec6abd0559bb6d1063264d0988b8e0cf5f89515164b588`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json) (zero-based source row 162). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
