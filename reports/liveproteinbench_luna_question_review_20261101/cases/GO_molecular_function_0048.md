# GO_molecular_function_0048

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — chorismate synthase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MSTYGTLLKVTSFGESHGKAIGCVIDGFLPNVEINFDLIQRQLNRRRPNQSKLTSNRNEPDKLIVLSGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNLSGYPSNGSGNPPNGSDHPSNRSGNPPNRSDPRVDESTRETSPPSGEKLLVTTSNNCGGILAGITTGNNIVFRSAIKPVSSIQIEKETCNFFGEKCKLKVTGMHDCCILPRLPPIIEASTSIVIGDMILRQVAKYGHSKLPSVGSLSRSTRE

[Multiple Choices]
A. ATP hydrolysis activity
B. heme oxygenase (decyclizing) activity
C. chorismate synthase activity
D. single-stranded DNA binding
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

> The supplied sequence exactly matches the Plasmodium vivax protein annotated as chorismate synthase. UniProt records the EPSP-to-chorismate reaction with experimental evidence (ECO:0000269, citing PMID 31381947), supporting choice C. The entry also describes a second, flavin-reductase activity, which is not among the choices.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clear, general biological clue that identifies chorismate synthase activity over the other offered functions; distinguishing these choices requires recognizing the protein family or knowing a protein-specific functional annotation.

**Missing item-specific fact**

> That this particular 547-aa Plasmodium vivax protein is a bifunctional chorismate synthase/flavin reductase.

**Reason**

> Reviewer-only annotation and experimental evidence support the key, but those facts are not supplied to the evaluated model. Exact-sequence recognition or recalled database annotation would be lookup or memorization, not reasoning from the provided input.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The protein has an additional flavin-reductase activity, but that activity is not offered. Among the listed options, the evidence supports chorismate synthase activity.

### Important caveats

- The experimental support is represented by UniProt evidence citing PMID 31381947; the primary paper was not independently reviewed here.
- The GO annotation itself is electronically inferred from the EC number, so it should be distinguished from the cited experimental functional annotation.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Plasmodium vivax protein annotated as chorismate synthase. UniProt records the EPSP-to-chorismate reaction with experimental evidence (ECO:0000269, citing PMID 31381947), supporting choice C. The entry also describes a second, flavin-reductase activity, which is not among the choices.",
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clear, general biological clue that identifies chorismate synthase activity over the other offered functions; distinguishing these choices requires recognizing the protein family or knowing a protein-specific functional annotation.",
    "missing_item_specific_fact": "That this particular 547-aa Plasmodium vivax protein is a bifunctional chorismate synthase/flavin reductase.",
    "reason": "Reviewer-only annotation and experimental evidence support the key, but those facts are not supplied to the evaluated model. Exact-sequence recognition or recalled database annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has an additional flavin-reductase activity, but that activity is not offered. Among the listed options, the evidence supports chorismate synthase activity."
  },
  "important_caveats": [
    "The experimental support is represented by UniProt evidence citing PMID 31381947; the primary paper was not independently reviewed here.",
    "The GO annotation itself is electronically inferred from the EC number, so it should be distinguished from the cited experimental functional annotation."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A5K264`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 64. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
"A5K264"
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"value":"Bifunctional chorismate synthase and flavin reductase (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate 3-phosphate (EPSP) to form chorismate (PubMed:31381947). Acts also as a flavin reductase (FR) able to generate reduced flavin mononucleotide in the presence of NADPH (PubMed:31381947)"}]}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:01.460415+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:21021"}}],"reaction":{"ecNumber":"4.2.3.5","evidences":[{"evidenceCode":"ECO:0000269","id":"31381947","source":"PubMed"}],"name":"5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:21020"},{"database":"ChEBI","id":"CHEBI:29748"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57701"}]}}
```

Source SHA-256: `d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 35-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
CC   -!- FUNCTION: Bifunctional chorismate synthase and flavin reductase
CC       (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate
CC       3-phosphate (EPSP) to form chorismate (PubMed:31381947). Acts also as a
CC       flavin reductase (FR) able to generate reduced flavin mononucleotide in
CC       the presence of NADPH (PubMed:31381947). {ECO:0000269|PubMed:31381947}.
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:05.947967+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate +
CC         phosphate; Xref=Rhea:RHEA:21020, ChEBI:CHEBI:29748,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57701; EC=4.2.3.5;
CC         Evidence={ECO:0000269|PubMed:31381947};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:21021;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 48). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
