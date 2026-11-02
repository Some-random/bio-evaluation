# EC_number_0093

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 2.1.1.394

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVPAARSGRKVYFIGLNAVPFLPLVAGLLRTYAEQDPRVAAGYDFQEPVFLVDGVQEMAAGITDPDVLALSCYVWNFRRQMKVARLVKERHPGMLVVAGGPHVPDRPGDFFARHPYVDVLVHGEGETAFRELLIERLADHPDYTRVPGVSVRHGTEAVPGRPAERLPRRIETPSPYLLGVMDGAVATCRQRDLRFYALWETNRGCPYSCAFCDWGSATMSALRLFDAERLQEEIEWFAEHDVEDLFVCDANFGILPRDLEIARALADARAATGAPKLIRVNFAKNSNDRVFEISKTWHDADLLMGTTLSMQSTDLDVLEAIDRKNIGLENYRKLQQRYATENIHTYTELILGLPLESPRSFRDGIGSLLEAGNHEDIRVYEFGILPNAPINTPEKIAGYGLRTVPKRLYVEEPGTPDDEAETVDMVMETNAMSRDEWVDCFGFVQAVQFLHNGCYTRYLSMYLRQRHDIGYTAFYERLQQYFGARPDTVLGSIYLRMRKLYHDYIDIPELPLANLVASQPDMAADLARYGKRRGWTIDNWGWLRIANDFERTYTELRDFVAALGVDDTSDPDLAEVFRFQQDVMLRPDYDPAAGRTTEYTADWPGYFTTGELRRRPVRMRLADQRFGANGRYTPVPGDLKAFARAAIGPSYPVSRIGHYRHRFEAAEVTSPAEPVLTEQR

[Multiple Choices]
A. 2.1.1.394
B. 2.1.1.393
C. 3.2.1.8
D. 3.1.1.4
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches UniProt entry Q83XP3. That entry assigns EC 2.1.1.394 to the protein and cites experimental evidence codes (ECO:0000269) for the catalytic activity; the reported reactions are methylations consistent with that EC number. The primary studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may be suggestive of a large radical-SAM methylation enzyme, but that broad inference does not identify the exact substrate specificity or distinguish EC 2.1.1.394 from the closely related 2.1.1.393.


**Missing item-specific fact**

> The protein-specific catalytic assignment, including its substrate and reaction products, established by biochemical characterization or a reliable annotation.


**Reason**

> The exact EC number is not derivable from the supplied sequence and choices through general biological reasoning alone. The reviewer-only database evidence supports the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Reviewer-only evidence supports A for the sequence-matched protein. Although the input itself does not resolve the exact EC assignment, that is an information-dependence issue rather than evidence that another listed option is also correct.


### Important caveats

- Sequence identity and the supporting annotation are established for the reviewer-identified UniProt entry; the author's exact source snapshot is unknown.
- The cited experimental evidence is represented in the database annotation, but the underlying primary studies were not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may be suggestive of a large radical-SAM methylation enzyme, but that broad inference does not identify the exact substrate specificity or distinguish EC 2.1.1.394 from the closely related 2.1.1.393.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic assignment, including its substrate and reaction products, established by biochemical characterization or a reliable annotation.",
    "reason": "The exact EC number is not derivable from the supplied sequence and choices through general biological reasoning alone. The reviewer-only database evidence supports the key but was not available to the evaluated model."
  },
  "case_id": "EC_number_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches UniProt entry Q83XP3. That entry assigns EC 2.1.1.394 to the protein and cites experimental evidence codes (ECO:0000269) for the catalytic activity; the reported reactions are methylations consistent with that EC number. The primary studies were not independently reviewed here."
  },
  "important_caveats": [
    "Sequence identity and the supporting annotation are established for the reviewer-identified UniProt entry; the author's exact source snapshot is unknown.",
    "The cited experimental evidence is represented in the database annotation, but the underlying primary studies were not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports A for the sequence-matched protein. Although the input itself does not resolve the exact EC assignment, that is an information-dependence issue rather than evidence that another listed option is also correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches UniProt entry Q83XP3. That entry assigns EC 2.1.1.394 to the protein and cites experimental evidence codes (ECO:0000269) for the catalytic activity; the reported reactions are methylations consistent with that EC number. The primary studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may be suggestive of a large radical-SAM methylation enzyme, but that broad inference does not identify the exact substrate specificity or distinguish EC 2.1.1.394 from the closely related 2.1.1.393.",
    "missing_item_specific_fact": "The protein-specific catalytic assignment, including its substrate and reaction products, established by biochemical characterization or a reliable annotation.",
    "reason": "The exact EC number is not derivable from the supplied sequence and choices through general biological reasoning alone. The reviewer-only database evidence supports the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only evidence supports A for the sequence-matched protein. Although the input itself does not resolve the exact EC assignment, that is an information-dependence issue rather than evidence that another listed option is also correct."
  },
  "important_caveats": [
    "Sequence identity and the supporting annotation are established for the reviewer-identified UniProt entry; the author's exact source snapshot is unknown.",
    "The cited experimental evidence is represented in the database annotation, but the underlying primary studies were not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q83XP3 (THNK_STREN, ThnK from Streptomyces cattleya) is annotated with EC 2.1.1.394 based on experimental evidence (ECO:0000269) from three independent PubMed publications (26240322, 31774078, 36042702). The benchmark sequence matches the UniProt entry exactly (681 AA, SHA256 match). The catalytic activity is documented with Rhea IDs (RHEA:79659, RHEA:79663) for carbapenam methyltransferase reactions using SAM as methyl donor.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable radical SAM motif (CxxxCxxC region, e.g., 'VDCFGFV' and 'CDANFGIL'), which identifies this as a radical SAM enzyme. Since radical SAM methyltransferases fall under EC 2.1.1.x (transferases, one-carbon transfer, methyltransferases), this reasoning eliminates options C (3.2.1.8, glycosidase) and D (3.1.1.4, phospholipase), both of which are hydrolases with entirely different catalytic mechanisms and no radical SAM domain.


**Missing item-specific fact**

> Distinguishing EC 2.1.1.394 from EC 2.1.1.393 requires knowing the exact substrate specificity of the enzyme. Both are methyltransferases potentially associated with radical SAM chemistry. The specific assignment of 2.1.1.394 (2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase, ThnK) versus 2.1.1.393 depends on knowing the precise carbapenam substrate and the cobalamin-dependent consecutive methylation mechanism, which is an item-specific experimental fact not derivable from general sequence analysis.


**Reason**

> While the radical SAM motif provides a valid biological argument to eliminate hydrolase options (C, D), the final choice between A (2.1.1.394) and B (2.1.1.393) cannot be resolved through general biological reasoning from the sequence alone. Both are EC 2.1.1.x methyltransferases, and the distinction between these two specific four-digit numbers requires memorization or lookup of the exact EC assignment for this particular enzyme.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (2.1.1.394) and B (2.1.1.393) are methyltransferase EC numbers within the same EC 2.1.1.x class. Without specific knowledge of the substrate (carbapenam-3-carboxylate vs. whatever 2.1.1.393 targets), a model relying only on the radical SAM motif and general methyltransferase knowledge cannot definitively choose between them. Options C and D are clearly eliminable.


### Important caveats

- The EC number 2.1.1.394 was assigned relatively recently (entry first public date 2025-02-05), meaning this is a newly characterized enzyme; the distinction from 2.1.1.393 is particularly difficult for any model without up-to-date database access.
- The radical SAM domain identification is a genuine reasoning step that eliminates two of four options, but the remaining A-vs-B distinction is essentially a database lookup.
- All evidence is from UniProt annotation supported by experimental publications (ECO:0000269), not purely computational inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable radical SAM motif (CxxxCxxC region, e.g., 'VDCFGFV' and 'CDANFGIL'), which identifies this as a radical SAM enzyme. Since radical SAM methyltransferases fall under EC 2.1.1.x (transferases, one-carbon transfer, methyltransferases), this reasoning eliminates options C (3.2.1.8, glycosidase) and D (3.1.1.4, phospholipase), both of which are hydrolases with entirely different catalytic mechanisms and no radical SAM domain.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing EC 2.1.1.394 from EC 2.1.1.393 requires knowing the exact substrate specificity of the enzyme. Both are methyltransferases potentially associated with radical SAM chemistry. The specific assignment of 2.1.1.394 (2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase, ThnK) versus 2.1.1.393 depends on knowing the precise carbapenam substrate and the cobalamin-dependent consecutive methylation mechanism, which is an item-specific experimental fact not derivable from general sequence analysis.",
    "reason": "While the radical SAM motif provides a valid biological argument to eliminate hydrolase options (C, D), the final choice between A (2.1.1.394) and B (2.1.1.393) cannot be resolved through general biological reasoning from the sequence alone. Both are EC 2.1.1.x methyltransferases, and the distinction between these two specific four-digit numbers requires memorization or lookup of the exact EC assignment for this particular enzyme."
  },
  "case_id": "EC_number_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt Q83XP3 (THNK_STREN, ThnK from Streptomyces cattleya) is annotated with EC 2.1.1.394 based on experimental evidence (ECO:0000269) from three independent PubMed publications (26240322, 31774078, 36042702). The benchmark sequence matches the UniProt entry exactly (681 AA, SHA256 match). The catalytic activity is documented with Rhea IDs (RHEA:79659, RHEA:79663) for carbapenam methyltransferase reactions using SAM as methyl donor."
  },
  "important_caveats": [
    "The EC number 2.1.1.394 was assigned relatively recently (entry first public date 2025-02-05), meaning this is a newly characterized enzyme; the distinction from 2.1.1.393 is particularly difficult for any model without up-to-date database access.",
    "The radical SAM domain identification is a genuine reasoning step that eliminates two of four options, but the remaining A-vs-B distinction is essentially a database lookup.",
    "All evidence is from UniProt annotation supported by experimental publications (ECO:0000269), not purely computational inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (2.1.1.394) and B (2.1.1.393) are methyltransferase EC numbers within the same EC 2.1.1.x class. Without specific knowledge of the substrate (carbapenam-3-carboxylate vs. whatever 2.1.1.393 targets), a model relying only on the radical SAM motif and general methyltransferase knowledge cannot definitively choose between them. Options C and D are clearly eliminable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q83XP3 (THNK_STREN, ThnK from Streptomyces cattleya) is annotated with EC 2.1.1.394 based on experimental evidence (ECO:0000269) from three independent PubMed publications (26240322, 31774078, 36042702). The benchmark sequence matches the UniProt entry exactly (681 AA, SHA256 match). The catalytic activity is documented with Rhea IDs (RHEA:79659, RHEA:79663) for carbapenam methyltransferase reactions using SAM as methyl donor.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable radical SAM motif (CxxxCxxC region, e.g., 'VDCFGFV' and 'CDANFGIL'), which identifies this as a radical SAM enzyme. Since radical SAM methyltransferases fall under EC 2.1.1.x (transferases, one-carbon transfer, methyltransferases), this reasoning eliminates options C (3.2.1.8, glycosidase) and D (3.1.1.4, phospholipase), both of which are hydrolases with entirely different catalytic mechanisms and no radical SAM domain.",
    "missing_item_specific_fact": "Distinguishing EC 2.1.1.394 from EC 2.1.1.393 requires knowing the exact substrate specificity of the enzyme. Both are methyltransferases potentially associated with radical SAM chemistry. The specific assignment of 2.1.1.394 (2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase, ThnK) versus 2.1.1.393 depends on knowing the precise carbapenam substrate and the cobalamin-dependent consecutive methylation mechanism, which is an item-specific experimental fact not derivable from general sequence analysis.",
    "reason": "While the radical SAM motif provides a valid biological argument to eliminate hydrolase options (C, D), the final choice between A (2.1.1.394) and B (2.1.1.393) cannot be resolved through general biological reasoning from the sequence alone. Both are EC 2.1.1.x methyltransferases, and the distinction between these two specific four-digit numbers requires memorization or lookup of the exact EC assignment for this particular enzyme."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (2.1.1.394) and B (2.1.1.393) are methyltransferase EC numbers within the same EC 2.1.1.x class. Without specific knowledge of the substrate (carbapenam-3-carboxylate vs. whatever 2.1.1.393 targets), a model relying only on the radical SAM motif and general methyltransferase knowledge cannot definitively choose between them. Options C and D are clearly eliminable."
  },
  "important_caveats": [
    "The EC number 2.1.1.394 was assigned relatively recently (entry first public date 2025-02-05), meaning this is a newly characterized enzyme; the distinction from 2.1.1.393 is particularly difficult for any model without up-to-date database access.",
    "The radical SAM domain identification is a genuine reasoning step that eliminates two of four options, but the remaining A-vs-B distinction is essentially a database lookup.",
    "All evidence is from UniProt annotation supported by experimental publications (ECO:0000269), not purely computational inference."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q83XP3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
"Q83XP3"
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26240322","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31774078","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36042702","source":"PubMed"}],"value":"2.1.1.394"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase"}}}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"26240322","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79660"}}],"reaction":{"ecNumber":"2.1.1.394","evidences":[{"evidenceCode":"ECO:0000269","id":"26240322","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31774078","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36042702","source":"PubMed"}],"name":"(2R,3R,5R)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79659"},{"database":"ChEBI","id":"CHEBI:13193"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17319"},{"database":"ChEBI","id":"CHEBI:17499"},{"database":"ChEBI","id":"CHEBI:57844"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:230520"},{"database":"ChEBI","id":"CHEBI:230521"}]}}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"26240322","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79664"}}],"reaction":{"ecNumber":"2.1.1.394","evidences":[{"evidenceCode":"ECO:0000269","id":"26240322","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31774078","source":"PubMed"}],"name":"(2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(ethyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79663"},{"database":"ChEBI","id":"CHEBI:13193"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17319"},{"database":"ChEBI","id":"CHEBI:17499"},{"database":"ChEBI","id":"CHEBI:57844"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:230521"},{"database":"ChEBI","id":"CHEBI:230522"}]}}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:31:56.526994+00:00.  

```text
ID   THNK_STREN              Reviewed;         681 AA.
AC   Q83XP3; F8JND9; G8XDF2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2003, sequence version 1.
DT   28-JAN-2026, entry version 74.
DE   RecName: Full=2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase {ECO:0000305};
DE            EC=2.1.1.394 {ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078, ECO:0000269|PubMed:36042702};
GN   Name=thnK {ECO:0000303|PubMed:12725858};
GN   OrderedLocusNames=SCATT_p09050 {ECO:0000312|EMBL:AEW99098.1};
OS   Streptantibioticus cattleyicolor (strain ATCC 35852 / DSM 46488 / JCM 4925
OS   / NBRC 14057 / NRRL 8057) (Streptomyces cattleya).
OG   Plasmid pSCATT {ECO:0000312|EMBL:AEW99098.1}.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptantibioticus.
OX   NCBI_TaxID=1003195;
```

Source SHA-256: `c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:31:56.526994+00:00.  

```text
DE   RecName: Full=2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase {ECO:0000305};
DE            EC=2.1.1.394 {ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078, ECO:0000269|PubMed:36042702};
```

Source SHA-256: `c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)  
**Locator:** `lines 76-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:31:56.526994+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R,3R,5R)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 +
CC         2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(methyl)-2-(S-
CC         pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-
CC         methionine + A + S-adenosyl-L-homocysteine + 2 H(+);
CC         Xref=Rhea:RHEA:79659, ChEBI:CHEBI:13193, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:17319, ChEBI:CHEBI:17499, ChEBI:CHEBI:57844,
CC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:230520,
CC         ChEBI:CHEBI:230521; EC=2.1.1.394;
CC         Evidence={ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078,
CC         ECO:0000269|PubMed:36042702};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79660;
CC         Evidence={ECO:0000269|PubMed:26240322};
```

Source SHA-256: `c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)  
**Locator:** `lines 89-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:31:56.526994+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-
CC         carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-
CC         (ethyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-
CC         deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2
CC         H(+); Xref=Rhea:RHEA:79663, ChEBI:CHEBI:13193, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:17319, ChEBI:CHEBI:17499, ChEBI:CHEBI:57844,
CC         ChEBI:CHEBI:57856, ChEBI:CHEBI:59789, ChEBI:CHEBI:230521,
CC         ChEBI:CHEBI:230522; EC=2.1.1.394;
CC         Evidence={ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79664;
CC         Evidence={ECO:0000269|PubMed:26240322};
```

Source SHA-256: `c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
