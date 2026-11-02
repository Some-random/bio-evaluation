# GO_molecular_function_0012

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — ADP-ribosylarginine hydrolase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MRSFLYMLSQRPKLACLCGKSIIIWPGKRTNLPENAFTQRMLQECGQMAKPDASVDLDNFKAISEQSPAEFGIDSCRVKAQPEDRSDRIREQIASAYPVIHERTLLLFISFLEHKLTFGSEQEKAIYKDMTVVDLVQRLLAKRCVWFFGANDYYRTMQGNIGNEGFEAVGTPAEKEPLTLTSVLSYDEIKLSALLYVSCHSEFINNGSRVNGGEVLQNKDTIEREGVVIGLIGARFERPDVMEYQDIMITKTQNTEANGYGFDLEQISSETVTPASDLRRIWREFYEEPRDFIYADTPYDTTRFEEVSQGIFDHQVMRKRYAISFDTLLLEAQDRAFKAGKPAYIHVVGIGLGVWKAARQQERTFLESFEGRLRALGERLSHIGVVHFSWFHLACVGSLHDGAIIPVDKHPQGGIRIRNSVRNPGDKLTEDMLPVVTYAWDGNALPGNEFWANMLISTGDPAAACSTLISELQNPHINVHYMNGANLHIASVEHGLLHVGDYARRLIV

[Multiple Choices]
A. RNA polymerase II core promoter sequence-specific DNA binding
B. ADP-ribosylarginine hydrolase activity
C. peptidase inhibitor activity
D. zinc ion binding
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

> The supplied sequence exactly matches the 508-aa Drosophila melanogaster protein annotated as an ADP-ribosylarginine hydrolase. Its catalytic activity and corresponding GO molecular-function term are supported by experimental evidence cited in the record, including an IDA annotation. The matching historical record also supports the key, although the author's exact source snapshot is unknown.

Cited evidence: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a folded soluble enzyme, and the choices make DNA binding and peptidase inhibition less immediately plausible. But those broad features do not identify this enzyme's specific ADP-ribosylarginine-hydrolysis activity or reliably distinguish it from the remaining molecular-function options.

**Missing item-specific fact**

> The protein-specific identification as Drosophila CG3568/ADP-ribosylarginine hydrolase, or equivalent family/domain evidence connecting this sequence to that precise catalytic activity.

**Reason**

> The input supplies only an amino-acid sequence and choices. Selecting B requires recognizing or retrieving a protein-specific functional assignment; generic sequence reasoning alone does not establish the precise substrate and reaction.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The evidence supports B for the sequence-matched protein, and no other listed choice is comparably supported.

### Important caveats

- Reviewer-only database evidence establishes support for the key but was not available to the evaluated model.
- The current and retrieved historical UniProt records match the supplied sequence; the author's exact source snapshot remains unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 508-aa Drosophila melanogaster protein annotated as an ADP-ribosylarginine hydrolase. Its catalytic activity and corresponding GO molecular-function term are supported by experimental evidence cited in the record, including an IDA annotation. The matching historical record also supports the key, although the author's exact source snapshot is unknown.",
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a folded soluble enzyme, and the choices make DNA binding and peptidase inhibition less immediately plausible. But those broad features do not identify this enzyme's specific ADP-ribosylarginine-hydrolysis activity or reliably distinguish it from the remaining molecular-function options.",
    "missing_item_specific_fact": "The protein-specific identification as Drosophila CG3568/ADP-ribosylarginine hydrolase, or equivalent family/domain evidence connecting this sequence to that precise catalytic activity.",
    "reason": "The input supplies only an amino-acid sequence and choices. Selecting B requires recognizing or retrieving a protein-specific functional assignment; generic sequence reasoning alone does not establish the precise substrate and reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports B for the sequence-matched protein, and no other listed choice is comparably supported."
  },
  "important_caveats": [
    "Reviewer-only database evidence establishes support for the key but was not available to the evaluated model.",
    "The current and retrieved historical UniProt records match the supplied sequence; the author's exact source snapshot remains unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9W4J9`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 153. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"value":"3.2.2.19"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"ADP-ribosylarginine hydrolase CG3568"}}}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"value":"Protein ADP-ribosyl hydrolase that specifically removes mono-ADP-ribosyl modifications from protein arginine residues"}]}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.2.19","evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"name":"N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14885"},{"database":"Rhea","id":"RHEA-COMP:10532"},{"database":"Rhea","id":"RHEA-COMP:15087"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29965"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142554"}]}}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/uniProtKBCrossReferences/27`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"38503748","source":"PubMed"}],"id":"GO:0003875","properties":[{"key":"GoTerm","value":"F:ADP-ribosylarginine-[protein] hydrolase activity"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 86-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
CC   -!- FUNCTION: Protein ADP-ribosyl hydrolase that specifically removes mono-
CC       ADP-ribosyl modifications from protein arginine residues.
CC       {ECO:0000269|PubMed:38503748}.
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 89-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-
CC         ribose + L-arginyl-[protein]; Xref=Rhea:RHEA:14885, Rhea:RHEA-
CC         COMP:10532, Rhea:RHEA-COMP:15087, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:29965, ChEBI:CHEBI:57967, ChEBI:CHEBI:142554;
CC         EC=3.2.2.19; Evidence={ECO:0000269|PubMed:38503748};
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 130-130`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
DR   GO; GO:0003875; F:ADP-ribosylarginine hydrolase activity; IDA:FlyBase.
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 12). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
