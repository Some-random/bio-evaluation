# transmembrane_0103

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MGKEQKEKKDGNLSIKEEVEKELNKKSTAELFRKIKNEKISFFLPFKCLPAQHRKLLFISFVCAVLSGGTLPFFISVFGVILKNMNLGDDINPIILSLVSIGLVQFILSMISSYCMDVITSKILKTLKLEYLRSVFYQDGQFHDNNPGSKLRSDLDFYLEQVSSGIGTKFITIFTYASSFLGLYIWSLIKNARLTLCITCVFPLIYVCGVICNKKVKLNKKTSLLYNNNTMSIIEEALMGIRTVASYCGEKTILNKFNLSETFYSKYILKANFVEALHIGLINGLILVSYAFGFWYGTRIIINSATNQYPNNDFNGASVISILLGVLISMFMLTIILPNITEYMKALEATNSLYEIINRKPLVENNDDGETLPNIKKIEFKNVRFHYDTRKDVEIYKDLSFTLKEGKTYAFVGESGCGKSTILKLIERLYDPTEGDIIVNDSHNLKDINLKWWRSKIGVVSQDPLLFSNSIKNNIKYSLYSLKDLEAMENYYEENTNDTYENKNFSLISNSMTSNELLEMKKEYQTIKDSDVVDVSKKVLIHDFVSSLPDKYDTLVGSNASKLSGGQKQRISIARAIMRNPKILILDEATSSLDNKSEYLVQKTINNLKGNENRITIIIAHRLSTIRYANTIFVLSNRERSDNNNNNNNDDNNNNNNNNNNKINNEGSYIIEQGTHDSLMKNKNGIYHLMINNQKISSNKSSNNGNDNGSDNKSSAYKDSDTGNDADNMNSLSIHENENISNNRNCKNTAENEKEEKVPFFKRMFRRKKKAPNNLRIIYKEIFSYKKDVTIIFFSILVAGGLYPVFALLYARYVSTLFDFANLEYNSNKYSIYILLIAIAMFISETLKNYYNNKIGEKVEKTMKRRLFENILYQEMSFFDQDKNTPGVLSAHINRDVHLLKTGLVNNIVIFSHFIMLFLVSMVMSFYFCPIVAAVLTFIYFINMRVFAVRARLTKSKEIEKKENMSSGVFAFSSDDEMFKDPSFLIQEAFYNMHTVINYGLEDYFCNLIEKAIDYKNKGQKRRIIVNAALWGFSQSAQLFINSFAYWFGSFLIKRGTILVDDFMKSLFTFIFTGSYAGKLMSLKGDSENAKLSFEKYYPLMIRKSNIDVRDDGGIRINKNLIKGKVDIKDVNFRYISRPNVPIYKNLSFTCDSKKTTAIVGETGSGKSTFMNLLLRFYDLKNDHIILKNDMTNFQDYQNNNNNSLVLKNVNEFSNQSGSAEDYTVFNNNGEILLDDINICDYNLRDLRNLFSIVSQEPMLFNMSIYENIKFGREDATLEDVKRVSKFAAIDEFIESLPNKYDTNVGPYGKSLSGGQKQRIAIARALLREPKILLLDEATSSLDSNSEKLIEKTIVDIKDKADKTIITIAHRIASIKRSDKIVVFNNPDRNGTFVQSHGTHDELLSAQDGIYKKYVKLAK

[Multiple Choices]
A. 3..23
B. 61..81; 91..111; 169..189; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
C. 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
D. 61..81; 91..111; 169..189; 192..212; 276..296; 318..338; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
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

> The sequence-matched UniProt record annotates the transmembrane regions listed in C, including 192..212 and 317..337. These annotations are computational (PROSITE-ProRule), not independent experimental confirmation of every boundary.

Cited evidence: [C1](#evidence-c1), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general pattern of regions in the choices and argues against A. That pattern does not reliably distinguish the one-residue boundary shift in D from C.

**Missing item-specific fact**

> The protein-specific transmembrane annotations or equivalent structure/topology evidence specifying the segment boundaries, especially the 317..337 versus 318..338 choice.

**Reason**

> Sequence hydrophobicity supports broad helix locations, but the choices ask for precise boundaries and differ in ways that general biological reasoning cannot settle reliably.

### Question ambiguity

**Multiple defensible options named by Luna:** C, D.

> C and D differ only by shifting the 317..337 segment by one residue; the supplied sequence alone does not establish that exact boundary distinction.

### Important caveats

- The reviewer-only records match the supplied sequence, but their accession and annotations were not provided in the question.
- The cited UniProt transmembrane features are computationally supported annotations, not direct experimental evidence for each exact endpoint.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the transmembrane regions listed in C, including 192..212 and 317..337. These annotations are computational (PROSITE-ProRule), not independent experimental confirmation of every boundary.",
    "evidence_ids": [
      "C1",
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C23",
      "C25",
      "C27"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, which supports the general pattern of regions in the choices and argues against A. That pattern does not reliably distinguish the one-residue boundary shift in D from C.",
    "missing_item_specific_fact": "The protein-specific transmembrane annotations or equivalent structure/topology evidence specifying the segment boundaries, especially the 317..337 versus 318..338 choice.",
    "reason": "Sequence hydrophobicity supports broad helix locations, but the choices ask for precise boundaries and differ in ways that general biological reasoning cannot settle reliably."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "C and D differ only by shifting the 317..337 segment by one residue; the supplied sequence alone does not establish that exact boundary distinction."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but their accession and annotations were not provided in the question.",
    "The cited UniProt transmembrane features are computationally supported annotations, not direct experimental evidence for each exact endpoint."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `boundary_alternative_not_independently_validated`.

> Cited PROSITE-ProRule Transmembrane features match keyC including317..337; optionD shifts that one interval to318..338.

**Remaining uncertainty:** The specific shift is present in the options. The source supports the keyed predicted interval, not experimental equivalence of the alternative boundaries.

Evidence checked: [C1](#evidence-c1), [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C23](#evidence-c23), [C25](#evidence-c25), [C27](#evidence-c27).

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q7K6A5`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 159. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
"Q7K6A5"
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":81},"start":{"modifier":"EXACT","value":61}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":111},"start":{"modifier":"EXACT","value":91}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":189},"start":{"modifier":"EXACT","value":169}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":212},"start":{"modifier":"EXACT","value":192}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":296},"start":{"modifier":"EXACT","value":276}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":337},"start":{"modifier":"EXACT","value":317}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":809},"start":{"modifier":"EXACT","value":789}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":850},"start":{"modifier":"EXACT","value":830}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":928},"start":{"modifier":"EXACT","value":908}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":949},"start":{"modifier":"EXACT","value":929}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":1053},"start":{"modifier":"EXACT","value":1033}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/features/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00441","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":1078},"start":{"modifier":"EXACT","value":1058}},"type":"Transmembrane"}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 103). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
