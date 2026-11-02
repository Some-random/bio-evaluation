# transmembrane_0028

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 1404..1424

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MGKTKIYSVGFTVHEAQTLVTEKGQPVDPLVVVRCCGREYRTEIKYAKSNVVSWDESHTWTDLCLTDEEWETAYITFEVQAANAFWRNTLLGLVSVQLRLIQLRKTHQIRKALPLQHPDDTDVHGSLRVTVFACAPGEAPPSPGEEEVLEEEDHNDYDDLRKAVIDTNQVVEREAGSRLYHVYVTAYRVEDLPRSSKGARDPFVTCEFAGCKLKSTQARGCCSHTFNECFRFPVVTPLPEDAILIKIWDWNFMKADELIAVGRISFSELRTRQMVPRWFNLYGFDDEEVAQATKVAGQGGRLVANCYLGRILLGARAERLTKEDDLMPAHTVAARPYETPPVIPLAVLADVYEVQGAPGEKVSVEIWCGPARARTKWVTGLETKAAQRAGVAPQAFNRAMEGALGVASYLRGDIPEGEDRFPFDNTEGRVEDLRLVVPEDTKQQWDIIISLYVRGTTKGFMGDTRIAFQRLKMSKIPGHVHNNPRAPIWVPLISTPPFESVKPAPAILMVIEKSKVEAFARSKRKHVTAVGYQLRAYVYAARNLLSPSGALPNPFVQVACAGTSRETEVFEQTSSPVFMDCLLLDITMMTDPVSRLPTVAPIVVTLFEQRSWGIQFLGRATCHYDRLRGRLKPGESPTVAEPRWIKLRGGKYANRHLGDVLLLLELIRKRDAEIIPAFPMRPVVNMCNLTFSCLGVRSLYMTQRAKRLDYVSIRKGQDKKTELRRIRGPLLRISVSSYASAGRGNNEAILRYERNLPEDPTTVNKLWTTVTKAANADIFKVVNMEIDVPVDPIYDPRLVVQVYDRKQKPKYFIGEYSMSLVPLIPWVLDQQSAIEAVSPVNDFTDTVDLKHLGGLLRGFHGNSKNRGTGQIGLEALSAADRETADAHKEKTLAQSRFATYDPDNKTFSDSWLLPSGLPKILVSSYAVPGFRCDVIYTNMFTLNVYIPAKFVLFAEGKRAADKKTKEQYARPSVDSTLEQFLDDVIFPSDSLKKSVMGDIDVTGFVKFFVNLTHHEEPNPHVDSSAAEWASSEDRMRRHLRGEDAYPKLLKIRVYVIRAISLYVGDDRILPNPYLLFNLGDKSDTLRAEAKPNTHNPEFFTVWEKDVMFPDDSQFELQVWSAHEGTSGGLDDIFIGSTCIDLEERWFSKEWQKSMSKNQVPMEYRPLKQMPSGSFKGTVEMWVELMDFQKAGEVPKFDLQSPAATEVEIRVIVWGARNLNFKALGKDFVDAMIRCNLDCTGYRGSQPIAQQTDVHYYSKTGAAIFNWRMVYSRVVMPVSTCVLQIAAYDNRNMGESPFIGEVNLELRRYLERVASTLNSIDVDAELKLINRSRESADVSSFGFVQVSLQFISQSEATSKPVGLGREPPNRDPRLTTPQEGRKWEDVLGSAGLRVDYRPLWYWVRVAAVVFLSIWIFVVAFLYPSLLG

[Multiple Choices]
A. 35..55
B. 1408..1428
C. 1404..1424
D. 1404..1424; 630..652
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

> The supplied sequence exactly matches a UniProt entry annotated with a helical transmembrane region at 1404..1424, supporting choice C. The annotation is computational (ECO:0000255), not experimental evidence.

Cited evidence: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal hydrophobic stretch is consistent with a membrane-spanning helix, so sequence reasoning can suggest the general location.

**Missing item-specific fact**

> The precise annotated boundaries 1404..1424 are needed to distinguish C from the overlapping, slightly shifted 1408..1428 in B; those exact coordinates are not supplied in the question.

**Reason**

> A hydrophobic C-terminal segment supports a broad prediction, but does not meaningfully establish the exact start and end residues among the close alternatives.

### Question ambiguity

**Multiple defensible options named by Luna:** C, D.

> Choice D includes the annotated 1404..1424 segment as well as 630..652. If an option need only identify a segment, D also contains the correct one; if it is meant to list all predicted transmembrane regions, the extra range makes D a different claim.

### Important caveats

- The reviewer-only sequence-matched database annotation supports the key but was not available to the evaluated model.
- The annotation establishes database support, not experimental confirmation of the membrane-spanning boundaries.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated with a helical transmembrane region at 1404..1424, supporting choice C. The annotation is computational (ECO:0000255), not experimental evidence.",
    "evidence_ids": [
      "C5",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal hydrophobic stretch is consistent with a membrane-spanning helix, so sequence reasoning can suggest the general location.",
    "missing_item_specific_fact": "The precise annotated boundaries 1404..1424 are needed to distinguish C from the overlapping, slightly shifted 1408..1428 in B; those exact coordinates are not supplied in the question.",
    "reason": "A hydrophobic C-terminal segment supports a broad prediction, but does not meaningfully establish the exact start and end residues among the close alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Choice D includes the annotated 1404..1424 segment as well as 630..652. If an option need only identify a segment, D also contains the correct one; if it is meant to list all predicted transmembrane regions, the extra range makes D a different claim."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched database annotation supports the key but was not available to the evaluated model.",
    "The annotation establishes database support, not experimental confirmation of the membrane-spanning boundaries."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A7J6K2G0`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 12. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.269882+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1424},"start":{"modifier":"EXACT","value":1404}},"type":"Transmembrane"}
```

Source SHA-256: `68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-01T06:27:33.007451+00:00.  

```text
FT   TRANSMEM        1404..1424
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 28). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
