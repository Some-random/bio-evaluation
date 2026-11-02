# catalytic_activity_0028

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — N(omega)-(ADP-D-ribosyl)-L-arginyl-&#91;protein&#93; + H2O = ADP-D-ribose + L-arginyl-&#91;protein&#93;

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MSTFGAEVDQVWPAVTGDSPHLTNFGRKLLKDCRQVQKPIGGYENLGNVIKLSAEFPLEFGVNSVKVYRQSPSRLARINEEVASAYPLIHERTLGLYLQYLEHKCRWGNAVEKPIYRNLSLCGFVQRLLVKRCASFFARNDKYLLVSGESGASGFEAVGTREEKAPLVLANVLSYDDIKLSALLSVSSRTEFVNEGERTNCGHVDLNTKTLERHGVIVGMIGARLSRRNLMEFQDIVIARQQNTRERGYGMALDEPATTRDEDYRRLWREFYATRDLIHGQAVIDNQRFGPSKNKMDVFDNLVMKRRYAISFDMLLLEAEARAKRVKKLAYIHVVGFGLGVWKAAEQQERIFMETFEQRMRTLGNRLNNVGLVHFSWFSITHCGGLSNGSLIEIPGHPKDGIRVLISKRNPARKLSDPEHAGMLLVVSYAWDGNALPGNEFWMKMLQSTGDSSTACSTLVAELHNPYINTKFCNGGNLHIASPEHGVLHIAEYAKRVIRSESDAL

[Multiple Choices]
A. N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]
B. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
C. a quinone + NADPH + H(+) = a quinol + NADP(+)
D. a 5'-end (5'-triphosphoguanosine)-adenylyl-adenylyl-cytidylyl-adenosine in mRNA + S-adenosyl-L-methionine = a 5'-end (5'-triphosphoguanosine)-(2'-O-methyladenylyl)-adenylyl-cytidylyl-adenosine in mRNA + S-adenosyl-L-homocysteine + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence exactly matches the UniProt entry for Drosophila ADP-ribosylarginine hydrolase CG2909, whose annotated catalytic reaction is choice A. The reaction annotation cites experimental evidence (ECO:0000269); the primary paper was not independently reviewed here.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe different enzyme activities, but the input provides no biological context or explicit substrate evidence that establishes this protein's particular activity.

**Missing item-specific fact**

> The protein-specific identification or experimental annotation that this sequence encodes an ADP-ribosylarginine hydrolase.

**Reason**

> Choosing A depends on knowing the identity or functional annotation of this particular sequence. The reviewer-only database match supports the key but was not supplied to the evaluated model; exact-sequence recognition or a predictor's output would not itself make the question reasoning-supported.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The matched sequence's cited catalytic-activity annotation specifies choice A; no competing reaction is supported by the supplied reviewer evidence.

### Important caveats

- The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.
- The cited experimental evidence is represented through UniProt annotation; the primary paper was not independently validated.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for Drosophila ADP-ribosylarginine hydrolase CG2909, whose annotated catalytic reaction is choice A. The reaction annotation cites experimental evidence (ECO:0000269); the primary paper was not independently reviewed here.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe different enzyme activities, but the input provides no biological context or explicit substrate evidence that establishes this protein's particular activity.",
    "missing_item_specific_fact": "The protein-specific identification or experimental annotation that this sequence encodes an ADP-ribosylarginine hydrolase.",
    "reason": "Choosing A depends on knowing the identity or functional annotation of this particular sequence. The reviewer-only database match supports the key but was not supplied to the evaluated model; exact-sequence recognition or a predictor's output would not itself make the question reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's cited catalytic-activity annotation specifies choice A; no competing reaction is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.",
    "The cited experimental evidence is represented through UniProt annotation; the primary paper was not independently validated."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9W2W5`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 173. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
"Q9W2W5"
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"value":"3.2.2.19"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"ADP-ribosylarginine hydrolase CG2909"}}}
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.2.19","evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"name":"N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14885"},{"database":"Rhea","id":"RHEA-COMP:10532"},{"database":"Rhea","id":"RHEA-COMP:15087"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29965"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142554"}]}}
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)  
**Locator:** `lines 89-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 173 / 1.  
**Retrieved:** 2026-11-02T04:33:51.554411+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-
CC         ribose + L-arginyl-[protein]; Xref=Rhea:RHEA:14885, Rhea:RHEA-
CC         COMP:10532, Rhea:RHEA-COMP:15087, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:29965, ChEBI:CHEBI:57967, ChEBI:CHEBI:142554;
CC         EC=3.2.2.19; Evidence={ECO:0000269|PubMed:38503748};
```

Source SHA-256: `d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 28). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
