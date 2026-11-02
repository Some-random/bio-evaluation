# GO_molecular_function_0137

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — poly(A) binding

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MDTGGHGCSLSSLYVGDLHPDVTESMLYEMFSPIGNILSIRVCRDVATRRSLGYAYINFQQPADAERALDTMNFEVIKGQPIRIMWSHRDPGLRKSGMGNIFIKNLENSIDNKALYDTFSTFGSILSSKVVYNEHGSRGFGFVHFETHEAAQKAINTMNGMLLNDRKVFVGHFKSRQKREAELGARALGFTNIYVKNLHANVDEQRLQDLFSQFGNMQSVKVMRDSNGQSRGFGFVNFEKHEEAQKAVDHMNGKEVSGQLLYVGRAQKRAERQSELKRRFEQMKQERQNRYQGVNLYVKNLDDSINDERLKEVFSTYGVITSAKVMTESSHSKGFGFVCFSSPEEATKAVTEMNGRIVGTKPLYVALAQRKEERKAILTNQYRRRPSHPVLSSFQQPTSYLLPAVPQSTAQAVYYSSGSITPMQPDPRWTAQPHGPPSTCPPAASVVQPLSTTQHPCIHLRGASQVSSQVPHTQRVVNIGTQTTGPGGEGSSIPGQLLVPHRGTSAVHSAHGVQESAVYVPGHQPLTVSMLAAAPLHEQKQMIGERLYSLIHDACAPLTGKITGMLLELDNLELLLLLESPESLHAKIEEAVAVLQVHREMESTDRN

[Multiple Choices]
A. translation regulator activity
B. enoyl-[acyl-carrier-protein] reductase (NADPH) activity
C. beta-catenin binding
D. poly(A) binding
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

> The supplied sequence exactly matches the mouse UniProt entry for polyadenylate-binding protein 1-like. Its annotation identifies poly(A) binding, and its function description cites experimental evidence for a poly(A)-binding role.

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a characteristic PABP-like architecture: multiple N-terminal RNA-recognition motifs with conserved aromatic RNP-region patterns, followed by a C-terminal PABC-like region. This supports poly(A)-binding protein function over the enzyme and beta-catenin-binding choices.

**Missing item-specific fact**

> No external fact is strictly needed to favor D; recognizing the protein family from its sequence architecture provides a biological basis for the choice.

**Reason**

> The sequence contains recognizable family-level structural motifs that distinguish a PABP-like RNA-binding protein from the alternatives. This is a sequence-based inference, not reliance on remembering an accession or database annotation.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Translation regulation is a role associated with this protein, but poly(A) binding is the more direct molecular activity asked for and best distinguishes its primary function among the options.

### Important caveats

- The reviewer-only annotation supports the key but was not supplied to the evaluated model.
- The sequence match and cited experimental support establish the expected answer; they do not imply that every listed biological role is the protein's only function.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the mouse UniProt entry for polyadenylate-binding protein 1-like. Its annotation identifies poly(A) binding, and its function description cites experimental evidence for a poly(A)-binding role.",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H5",
      "H7"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a characteristic PABP-like architecture: multiple N-terminal RNA-recognition motifs with conserved aromatic RNP-region patterns, followed by a C-terminal PABC-like region. This supports poly(A)-binding protein function over the enzyme and beta-catenin-binding choices.",
    "missing_item_specific_fact": "No external fact is strictly needed to favor D; recognizing the protein family from its sequence architecture provides a biological basis for the choice.",
    "reason": "The sequence contains recognizable family-level structural motifs that distinguish a PABP-like RNA-binding protein from the alternatives. This is a sequence-based inference, not reliance on remembering an accession or database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Translation regulation is a role associated with this protein, but poly(A) binding is the more direct molecular activity asked for and best distinguishes its primary function among the options."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not supplied to the evaluated model.",
    "The sequence match and cited experimental support establish the expected answer; they do not imply that every listed biological role is the protein's only function."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A2A5N3`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2A5N3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:57.258604+00:00.  

```json
"A2A5N3"
```

Source SHA-256: `d566950f6c160c21b495a831c49fe21f6381c9ebe24477f0310c86b9267f4c1f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2A5N3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:57.258604+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"15630085","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"22621333","source":"PubMed"}],"value":"Embryonic poly(A)-binding protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"MGI:1922908","source":"MGI"}],"value":"Poly(A) binding protein, cytoplasmic 1-like"}}],"recommendedName":{"fullName":{"value":"Polyadenylate-binding protein 1-like"}}}
```

Source SHA-256: `d566950f6c160c21b495a831c49fe21f6381c9ebe24477f0310c86b9267f4c1f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2A5N3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:57.258604+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22621333","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"37052235","source":"PubMed"}],"value":"Poly(A)-binding protein involved in oocyte maturation and early embryo development (PubMed:22621333, PubMed:37052235). It is required for cytosolic mRNA polyadenylation and translational activation of maternally stored mRNA in oocytes (PubMed:22621333)"}]}
```

Source SHA-256: `d566950f6c160c21b495a831c49fe21f6381c9ebe24477f0310c86b9267f4c1f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2A5N3.json)  
**Locator:** `/uniProtKBCrossReferences/38`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:57.258604+00:00.  

```json
{"database":"GO","id":"GO:0008143","properties":[{"key":"GoTerm","value":"F:poly(A) binding"},{"key":"GoEvidenceType","value":"ISO:GO_Central"}]}
```

Source SHA-256: `d566950f6c160c21b495a831c49fe21f6381c9ebe24477f0310c86b9267f4c1f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2A5N3?format=txt&versions=130)  
**Locator:** `lines 55-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-01T06:27:44.941566+00:00.  

```text
CC   -!- FUNCTION: Poly(A)-binding protein involved in oocyte maturation and
CC       early embryo development (PubMed:22621333, PubMed:37052235). It is
CC       required for cytosolic mRNA polyadenylation and translational
CC       activation of maternally stored mRNA in oocytes (PubMed:22621333).
CC       {ECO:0000269|PubMed:22621333, ECO:0000269|PubMed:37052235}.
```

Source SHA-256: `6505f2784a667dbf4f83cdfc24a7d90e7b706c1f1af2f8d90f99f79cb282e5ea`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2A5N3?format=txt&versions=130)  
**Locator:** `lines 112-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-01T06:27:44.941566+00:00.  

```text
DR   GO; GO:0008143; F:poly(A) binding; ISO:GO_Central.
```

Source SHA-256: `6505f2784a667dbf4f83cdfc24a7d90e7b706c1f1af2f8d90f99f79cb282e5ea`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 137). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
