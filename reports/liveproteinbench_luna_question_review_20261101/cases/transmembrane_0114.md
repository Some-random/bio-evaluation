# transmembrane_0114

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 1250..1269

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MKKISKCAFVAISALVLIQATQTVKSQEPLVQSQLVTTVALTQDNRLLVEEIGPYASQSAGKEYYKHIEKIIVDNDVYEKSLEGERTFDINYQGIKINADLIKDGKHELTIVNKKDGDILITFIKKGDKVTFISAQKLGTTDHQDSLKKDVLSDKTVPQNQGTQKVVKSGKNTANLSLITKLSQEDGAILFPEIDRYSDNKQIKALTQQITKVTVNGTVYKDLISDSVKDTNGWVSNMTGLHLGTKAFKDGENTIVISSKGFEDVTITVTKKDGQIHFVSAKQKQHVTAEDRQSTKLDVTTLEKAIKEADAIIAKESNKDAVKDLAEKLQVIKDSYKEIKDSKLLADTHRLLKDTIESYQAGEVSINNLTEGTYTLNFKANKENSEESSMLQGAFDKRAKLVVKADGTMEISMLNTALGQFLIDFSIESKGTYPAAVRKQVGQKDINGSYIRSEFTMPIDDLDKLHKGAVLVSAMGGQESDLNHYDKYTKLDMTFSKTVTKGWSGYQVETDDKEKGVGTERLEKVLVKLGKDLDGDGKLSKTELEQIRGELRLDHYELTDISLLKHAKNITELHLDGNQITEIPKELFSQMKQLRFLNLRSNHLTYLDKDTFKSNAQLRELYLSSNFIHSLEGGLFQSLHHLEQLDLSKNRIGRLCDNPFEGLSRLTSLGFAENSLEEIPEKALEPLTSLNFIDLSQNNLALLPKTIEKLRALSTIVASRNHITRIDNISFKNLPKLSVLDLSTNEISNLPNGIFKQNNQLTKLDFFNNLLTQVEESVFPDVETLNLDVKFNQIKSVSPKVRALIGQHKLTPQKHIAKLEASLDGEKIKYHQAFSLLDLYYWEQKTNSAIDKELVSVEEYQQLLQEKGSDTVSLLNDMQVDWSIVIQLQKKASNGQYVTVDEKLLSNDPKDDLTGEFSLKDPGTYRIRKALITKKFATQKEHIYLTSNDILVAKGPHSHQKDLVENGLRALNQKQLRDGIYYLNASMLKTDLASESMSNKAINHRVTLVVKKGVSYLEVEFRGIKVGKMLGYLGELSYFVDGYQRDLAGKPVGRTKKAEVVSYFTDVTGLPLADRYGKNYPKVLRMKLIEQAKKDGLVPLQVFVPIMDAISKGSGLQTVFMRLDWASLTTEKAKVVKETNNPQENSHLTSTDQLKGPQNRQQEKTPTSPPSAATGIANLTDLLAKKATGQSTQETSKTDDTDKAEKLKQLVRDHQTSIEGKTAKDTKTKKSDKKHRSNQQSNGEESSSRYHLIAGLSSFMIVALGFIIGRKTLFK

[Multiple Choices]
A. 223..243; 6520..6540; 6552..6572; 6578..6598; 6627..6647; 6770..6790; 6831..6851; 6888..6908; 6912..6932; 7017..7037
B. 1250..1269
C. 1253..1267
D. 1250..1269; 742..763
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence matches the UniProt entry, whose transmembrane annotation is exactly 1250–1269. The annotation is computational (ECO:0000255), not evidence of direct experimental measurement.

Cited evidence: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal hydrophobic stretch supports a membrane-spanning helix and distinguishes this region from the other proposed locations. Sequence composition alone does not establish the precise helix boundaries.

**Missing item-specific fact**

> The specific annotated or predicted boundaries at residues 1250–1269, needed to distinguish B from the narrower overlapping interval in C.

**Reason**

> General sequence reasoning identifies the likely C-terminal membrane helix, but selecting its exact endpoints depends on a protein-specific boundary annotation or prediction.

### Question ambiguity

**Multiple defensible options named by Luna:** B, C.

> B matches the annotated full interval, while C is a shorter interval within the same hydrophobic region and could be read as identifying its membrane-spanning core. The wording does not specify whether the complete annotated helix or any crossing segment is required.

### Important caveats

- The cited annotation applies to the exact supplied sequence, but it is computational rather than demonstrated here by experimental evidence.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose transmembrane annotation is exactly 1250–1269. The annotation is computational (ECO:0000255), not evidence of direct experimental measurement.",
    "evidence_ids": [
      "C5",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal hydrophobic stretch supports a membrane-spanning helix and distinguishes this region from the other proposed locations. Sequence composition alone does not establish the precise helix boundaries.",
    "missing_item_specific_fact": "The specific annotated or predicted boundaries at residues 1250–1269, needed to distinguish B from the narrower overlapping interval in C.",
    "reason": "General sequence reasoning identifies the likely C-terminal membrane helix, but selecting its exact endpoints depends on a protein-specific boundary annotation or prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B matches the annotated full interval, while C is a shorter interval within the same hydrophobic region and could be read as identifying its membrane-spanning core. The wording does not specify whether the complete annotated helix or any crossing segment is required."
  },
  "important_caveats": [
    "The cited annotation applies to the exact supplied sequence, but it is computational rather than demonstrated here by experimental evidence.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q99YA0`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 156. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q99YA0.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.368907+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1269},"start":{"modifier":"EXACT","value":1250}},"type":"Transmembrane"}
```

Source SHA-256: `13d192b72925d5c393cc3105671c42e63812538c0c7b0b4492aea8192c61a8b1`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q99YA0?format=txt&versions=156)  
**Locator:** `lines 268-270`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-01T06:28:45.568124+00:00.  

```text
FT   TRANSMEM        1250..1269
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `19d54403bf689f1c46885d29ac65062d1747c6a8f0492de30c3b76138294fd49`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 114). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
