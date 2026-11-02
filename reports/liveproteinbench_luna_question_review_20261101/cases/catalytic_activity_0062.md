# catalytic_activity_0062

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — a D-glucoside + &#91;(1-&gt;2)-beta-D-glucosyl&#93;(n) = a beta-D-glucosyl-(1-&gt;2)-D-glucoside + &#91;(1-&gt;2)-beta-D-glucosyl&#93;(n-1)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MKPHNSEKYFVKNGQPHFLISGEVHYFRINPKLWRNHLQLLKQTGADTVSTYIPWDWHEIEEDDFDFEGKTHPARNLIRFIKLCKEENLDLIVKPGPYILAEYENQGLPSWLLKKLSKNAFALDENGNVISPDLVSYLSDEFLEYTFKWYDKVMPIISKHQKEHYGPITMMQLCNEIGVFQWLSGKSDYNPKVINLYKEFIIQRYKTIEKLNSVYSTNYNSFDDLKAPSGKIKLRSDYCAYFDFHLFFREYYNKYISILKNKIRSFGINIKLTHNIPGWIYGNASELPMLISTYSEIMKNHPDIIFGLDHIPEFVSFRNAHSDLACNKILEAMQPEAPVWAAEFQAGTREHHVKAYAKDLETFYIASLAHGIKGFNYYMFSQGINPEGKGFYGKTFYFQTALDAASNKLALYDSIKKVNRFIRKEQKDLLRTNVNSEICVGFYKPYFFTELISSQLLKEKKLNVEELGLYIDPRFLREEILFNGLLRGLQTLNYNYDVVDLENCDLKSLTAYKQLWITSAEFMDAETQNLLSEFVLNGGNLILYPAVPTLDNYLNRCEILKNNFGIEFITKDSSHKVSAFGIEDVFTAFSKKQIYNDTNSKPIAFTQENEICGIRKKIGKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQFVVRENNKSRYIFFLNYHNERKTFNYRKSSELKKKKSEEISIAPFSYKVIKENK

[Multiple Choices]
A. N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2
B. (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O
C. nicotinate beta-D-ribonucleotide + ATP + H(+) = deamido-NAD(+) + diphosphate
D. a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)
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

> The supplied sequence exactly matches the historical UniProt entry for this protein. That entry assigns EC 2.4.1.391 and records reaction D with ECO:0000269 evidence linked to a characterization paper, supporting the keyed activity.

Cited evidence: [H4](#evidence-h4), [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme reactions, but the sequence and choices alone provide no clear general biological argument that identifies this protein as the beta-1,2-glucosyltransferase in D.

**Missing item-specific fact**

> The protein-specific functional annotation or experimental characterization assigning this sequence to EC 2.4.1.391 and reaction D.

**Reason**

> Selecting D depends on knowing the function of this particular sequence; the supporting annotation and paper were reviewer-only, not supplied in the question.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The four choices describe distinct transformations; the supplied evidence supports D for the sequence-matched protein.

### Important caveats

- The annotation is linked to experimental evidence in a cited publication, but that primary paper was not independently retrieved or validated here.
- The exact author source snapshot is unknown; the historical entry and current entry both match the supplied sequence.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical UniProt entry for this protein. That entry assigns EC 2.4.1.391 and records reaction D with ECO:0000269 evidence linked to a characterization paper, supporting the keyed activity.",
    "evidence_ids": [
      "H4",
      "H3",
      "C5"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme reactions, but the sequence and choices alone provide no clear general biological argument that identifies this protein as the beta-1,2-glucosyltransferase in D.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization assigning this sequence to EC 2.4.1.391 and reaction D.",
    "reason": "Selecting D depends on knowing the function of this particular sequence; the supporting annotation and paper were reviewer-only, not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct transformations; the supplied evidence supports D for the sequence-matched protein."
  },
  "important_caveats": [
    "The annotation is linked to experimental evidence in a cited publication, but that primary paper was not independently retrieved or validated here.",
    "The exact author source snapshot is unknown; the historical entry and current entry both match the supplied sequence."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `I0AIT9`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 55. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.4.1.391","evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"name":"a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78691"},{"database":"Rhea","id":"RHEA-COMP:11881"},{"database":"Rhea","id":"RHEA-COMP:11882"},{"database":"ChEBI","id":"CHEBI:27517"},{"database":"ChEBI","id":"CHEBI:35436"},{"database":"ChEBI","id":"CHEBI:229541"}]}}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 25-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
RN   [2] {ECO:0007744|PDB:7VKW, ECO:0007744|PDB:7VKX, ECO:0007744|PDB:7VKY, ECO:0007744|PDB:7VKZ, ECO:0007744|PDB:7VL0, ECO:0007744|PDB:7VL1, ECO:0007744|PDB:7VL2, ECO:0007744|PDB:7VL3, ECO:0007744|PDB:7VL4, ECO:0007744|PDB:7VL5, ECO:0007744|PDB:7VL6}
RP   X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE;
RP   SOPHOROSE AND ALTERNATIVE SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF
RP   GLU-176 AND GLU-343.
RC   STRAIN=DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16;
RX   PubMed=35065074; DOI=10.1016/j.jbc.2022.101606;
RA   Kobayashi K., Shimizu H., Tanaka N., Kuramochi K., Nakai H., Nakajima M.,
RA   Taguchi H.;
RT   "Characterization and structural analyses of a novel glycosyltransferase
RT   acting on the beta-1,2-glucosidic linkages.";
RL   J. Biol. Chem. 298:101606-101606(2022).
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 46-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-
CC         glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1);
CC         Xref=Rhea:RHEA:78691, Rhea:RHEA-COMP:11881, Rhea:RHEA-COMP:11882,
CC         ChEBI:CHEBI:27517, ChEBI:CHEBI:35436, ChEBI:CHEBI:229541;
CC         EC=2.4.1.391; Evidence={ECO:0000269|PubMed:35065074};
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 62). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
