# transmembrane_0110

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **A** — 20..40; 84..104; 119..139; 180..200; 210..230; 273..293; 304..324; 381..401

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MKSMISGISSKIVESKKAKIFLLGTRILWIITTIIYIVLFYFITNKYVSLSEDDIDEYNIKGNEEELLKDDKIFNNYYKSYNKINAICGTFLILLCIVNIISSFYSKLNRGYMLYYKRMIGFVSLHLQLLFIAIMFLQNHENELFFCNINKYIYWFEDYDNKTDLFINSGENLCKVHNYSYIFPACFLFFSLIEFVVLYFKIEKHFRKKFLIFYIKMGTGIMYLALFYIFLKSKSFYNNILSEYNIFTLDDYSDPIKIIIFATQKQKMYYFQLLLVSTVSSAIVFCLLGYFDIYTIMKSCRFSLLVNIPISVFTMIVVFSQLLFSSYILETSAFFCAYEEFIEIHKRDQKASNKMIAPSNITETDWFCNLKSFDYIYFTNISTCLVIFGSDFIVSLYLVFSKKYAPKTS

[Multiple Choices]
A. 20..40; 84..104; 119..139; 180..200; 210..230; 273..293; 304..324; 381..401
B. 15..36; 84..104; 119..139; 180..200; 210..230; 273..293; 304..324; 381..401
C. 20..40; 84..104; 119..139; 210..230; 273..293; 304..324; 381..401
D. 9..45; 50..80; 86..121; 130..156; 173..211; 216..251; 268..296
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

> The supplied sequence matches the annotated 409-aa protein sequence. The annotation lists transmembrane helices at all eight ranges in choice A; these features carry computational evidence code ECO:0000255, so they support the key as annotation rather than establishing independent experimental validation.

Cited evidence: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated, roughly 20-residue hydrophobic stretches characteristic of membrane-spanning helices, with more polar or charged regions between them. In particular, residues 20–40 form a much more plausible hydrophobic span than 15–36, which includes charged residues near its start and omits hydrophobic residues at its end; the other choices omit a clear hydrophobic span or give substantially mismatched regions.

**Missing item-specific fact**

> No protein-specific external fact is necessary to distinguish these choices at the level of predicted spans, though exact boundaries are predictions rather than experimentally established from the sequence alone.

**Reason**

> The sequence itself supplies meaningful hydropathy and spacing evidence for the set in A. The reviewer-only annotation corroborates the answer but is not needed as input for this distinction.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The alternatives differ in ways the sequence can distinguish: B shifts the first interval into less hydrophobic residues, C omits a strongly hydrophobic candidate span, and D proposes broadly misplaced or excessive regions.

### Important caveats

- The annotation evidence for the transmembrane features is computational (ECO:0000255), not direct experimental evidence.
- Sequence-based hydropathy supports predicted membrane-spanning segments but does not by itself prove exact residue boundaries or topology.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated 409-aa protein sequence. The annotation lists transmembrane helices at all eight ranges in choice A; these features carry computational evidence code ECO:0000255, so they support the key as annotation rather than establishing independent experimental validation.",
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated, roughly 20-residue hydrophobic stretches characteristic of membrane-spanning helices, with more polar or charged regions between them. In particular, residues 20–40 form a much more plausible hydrophobic span than 15–36, which includes charged residues near its start and omits hydrophobic residues at its end; the other choices omit a clear hydrophobic span or give substantially mismatched regions.",
    "missing_item_specific_fact": "No protein-specific external fact is necessary to distinguish these choices at the level of predicted spans, though exact boundaries are predictions rather than experimentally established from the sequence alone.",
    "reason": "The sequence itself supplies meaningful hydropathy and spacing evidence for the set in A. The reviewer-only annotation corroborates the answer but is not needed as input for this distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives differ in ways the sequence can distinguish: B shifts the first interval into less hydrophobic residues, C omits a strongly hydrophobic candidate span, and D proposes broadly misplaced or excessive regions."
  },
  "important_caveats": [
    "The annotation evidence for the transmembrane features is computational (ECO:0000255), not direct experimental evidence.",
    "Sequence-based hydropathy supports predicted membrane-spanning segments but does not by itself prove exact residue boundaries or topology."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q8II12`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 86. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":40},"start":{"modifier":"EXACT","value":20}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":104},"start":{"modifier":"EXACT","value":84}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":139},"start":{"modifier":"EXACT","value":119}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":200},"start":{"modifier":"EXACT","value":180}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":230},"start":{"modifier":"EXACT","value":210}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":293},"start":{"modifier":"EXACT","value":273}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":324},"start":{"modifier":"EXACT","value":304}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8II12.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:11.920942+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":401},"start":{"modifier":"EXACT","value":381}},"type":"Transmembrane"}
```

Source SHA-256: `bb5a23789bd2691c2b0648f9210bb64a95740fd8f7e1e937e9d0d08c46ee6b1b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 83-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        20..40
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 89-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        84..104
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 95-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        119..139
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 101-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        180..200
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 107-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        210..230
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 113-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        273..293
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        304..324
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8II12?format=txt&versions=86)  
**Locator:** `lines 125-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-02T04:32:18.045484+00:00.  

```text
FT   TRANSMEM        381..401
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `f3b6997a1e5c1b67464918e100196c401cdbecca1c059e393e612b127411f297`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 110). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
