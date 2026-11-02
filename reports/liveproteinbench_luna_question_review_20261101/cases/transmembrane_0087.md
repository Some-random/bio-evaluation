# transmembrane_0087

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 1599..1619; 1662..1682; 1704..1724; 1763..1783; 1796..1816

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MKFKKELINILALIFVLKKNIFAQSICPTGYQMTQGSCTAIQCPNGQYYDSNLGLCANCDQACSACNYYPTYCTQCQNGFYLYQNQCLTQCPQAQTYVSCSGSSCICQACDSSCTQCFGNKNTQCLACSVGFYYNQINSSCLKQCEDGYTQQIVNIGASQQLLCIPCDNNCRTCSQTNAQQCLTCKDNMYLNTATNQCVSTCPQLQYKINGICKICPTGCQTCYNTNPSNPSTVESCLSCVSGYFLDIENQLCVKNCVSGYVVDAATQRCLPCNATCKNCSDQTNQGCLQCQNGYSLTSGSPSSCQNNCPNGNYQNSSLCLSCNTACSECFGADNQQCTACKTGYYLYKTQCLVICPVGFYTFARQYADPLKQPICDYCPNEMEQCEQDKSNFDLIKPILCKRGYYLYNGTCVKTCPDQTYYQDEATRSCLPCVFPCQTCLSASVCLTCATYTPNGQVQGQTYIFAQITYNGPQGTVFQQNCVPACPKGFYQNSKNNSCQVCNQQCQTCQGPAQTDCITCQIYDSNNMLFKYNNQCYYTCPSSQNNPMYGDKTTQACLPCSQECSSCFNGNNKSCYSCMNGYFLEYLKPECKSFCASDGTYMNSSTNQCSLCGFGCSSCTNGTFNSCISCLNGYYLQQNYNVCYPCPQQCASCTDMNTCQSCNQGYFLYSQTNSCVQQCPLIGFYVDTTQQACIPCDASCLECYGGANNQCISCPKGSYLKTDGTCQQCSQCSSNNECLGPNITDCLNQPICKPGQYLYDGQCLTCFPYCSTCSGTTYDSCISCQTTTDYTLLFDVCKKKVSQTDTQCDIGFYYDSVNKQCYSCHQNCIQCFGKSSSQCTKCSSGYLLHLDITTCSSTCLDGYYQQDPSIPQCSPCLYNCINGCSSGYQFLLGLCFTQCPFGTTAQKENCSFNSKPSIQFAQNLGNSVNNNSQTISLQLLVYSKNLFSIKWRLFTGNTDISNGPIQSYIQNRFDYIVFPPKSLQSNTQYTIQASILDLANNCQNENDCMVQQTFQTMNAITKGNFNIEINSAYLQLTLIISGWLFNSVPDNISFDLYVKLTGNDYFFFDKGQNYQDGRFTYLIPNLSYDLQDNKAQFFLVIYNDFDVQIQQLLIALNLNLQQTTISIDEFLDSVYSKITTLQQIQSLSYQFYSQMQNLMSSQTTSQTIFNRHLFYQVYSSLKGVQIPCDSNINCSGNGKCLWSQDNYNEILCICNINYAGRYCEFQSYQLDIARQHLIALTDLISNIPLNKSSDLFFTIEVLLELTYFYSIFDEFTLNTLINVYFQVFNQLQRVQSNISDEKILFKISKLTSQLINLINEDQTLSYNDQQSLLMKTMNDFDSQINLYLQNFAKSFDDLKSQEQVQTSFQTDISNINLNLIYQNDLLDAFMSNNGASDGQQQTPIVFYGDQISYTFDITQFSPKSSLSTAVIKWNSNPFLSQSQYQAPFISCITELVIYSQQTEIQISTVSQIVEIAIPKILPTPILSVIRPFYQPYTCIYFDSVSQVYKQDGVQYLRENSTHVICGSEQISGNYGVIVNQEYIDPNLSLTVIWNATQQIYANDQQFINFINQLINSNNNNGTNENPQVSQSSFNPNLSLLYALLIYIIFITIFIVISIIRDRKDQETYIKESDSYWLVHPIYSLIFGPYSSFFPRLQRSINYAQLIINLFLYNAIFVLVYSLPSEQELQQNVGKRQIISIQISSTSVACSIVTYYLTICMVNLFKMKWYIKQKWLDFKQDKITTEIVEQVTKSLKIFHLMNYGLVFMLQAGMGIPIIILILSFNSQQNQFFFTSVFASFVIDNILDIIILISFCFIKIFSQSEKSKIILLFTLRGFYYPVYEFLDIEDKIKEYQQKGEVLPAEEANNQSDDEDIFEINDHMNTPKRIFKKNEEKIDKAQEEIQLNEFVNNLKTNQ

[Multiple Choices]
A. 1599..1619; 1704..1724; 1763..1783; 1796..1816
B. 1599..1619; 1662..1682; 1704..1724; 1758..1784; 1796..1816
C. 25..45; 55..75; 80..100; 116..136; 175..195; 211..231
D. 1599..1619; 1662..1682; 1704..1724; 1763..1783; 1796..1816
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

> The sequence-matched historical UniProt record annotates all five intervals in D as transmembrane helices. These annotations carry evidence code ECO:0000255, so they support the key as database computational annotations, not as independent experimental confirmation.

Cited evidence: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, distinguishing that region from the cysteine-rich N-terminal region. This supports the general location and likely number of spans, but not the exact boundaries in the choices.

**Missing item-specific fact**

> The precise annotated endpoints, especially whether the last interval is 1763..1783 or the broader 1758..1784, and the exact set of annotated spans.

**Reason**

> Choosing the precise interval set requires protein-specific boundary information not reliably determined from general sequence heuristics. The matching database annotation supports D, but reviewer-only evidence does not make the original input alone sufficient to resolve exact endpoints.

### Question ambiguity

**Multiple defensible options named by Luna:** B, D.

> B and D include the same hydrophobic core at the final span, with B giving a broader interval. Because membrane-span boundaries can be uncertain and the wording does not specify a boundary convention, both could identify a segment crossing the membrane; D matches the database annotation more exactly.

### Important caveats

- The historical and current UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.
- The cited transmembrane features are computational annotations, not evidence of experimental measurement of the exact boundaries.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates all five intervals in D as transmembrane helices. These annotations carry evidence code ECO:0000255, so they support the key as database computational annotations, not as independent experimental confirmation.",
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, distinguishing that region from the cysteine-rich N-terminal region. This supports the general location and likely number of spans, but not the exact boundaries in the choices.",
    "missing_item_specific_fact": "The precise annotated endpoints, especially whether the last interval is 1763..1783 or the broader 1758..1784, and the exact set of annotated spans.",
    "reason": "Choosing the precise interval set requires protein-specific boundary information not reliably determined from general sequence heuristics. The matching database annotation supports D, but reviewer-only evidence does not make the original input alone sufficient to resolve exact endpoints."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B and D include the same hydrophobic core at the final span, with B giving a broader interval. Because membrane-span boundaries can be uncertain and the wording does not specify a boundary convention, both could identify a segment crossing the membrane; D matches the database annotation more exactly."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The cited transmembrane features are computational annotations, not evidence of experimental measurement of the exact boundaries."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q22HI5`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 82. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 88-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1599..1619
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 91-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1662..1682
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 94-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1704..1724
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 97-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1763..1783
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q22HI5?format=txt&versions=82)  
**Locator:** `lines 100-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 2.  
**Retrieved:** 2026-11-01T06:28:29.712799+00:00.  

```text
FT   TRANSMEM        1796..1816
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `5b8287201ed2b14e65eebd69b4f7c01951e7aaf9c65caf0968e3ae2c42261ab5`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 87). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
