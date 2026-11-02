# EC_number_0085

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.1.1.25

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGSLDIKQESSPLMTNPLDSEEFRRQGYMVIDFLAEYYKNIQKFPVRSQVEPGYLRKRLPESAPYEPESIETILKDVHDDIVPGLTHWQSPNYYAYFPSSGSTAGLLGETLAAGFNVVGFNWISSPASTELESIVMDWLAEMLNLPKSFTFSGDGGGVMMGTTCEAILTTITAARDRILDRIGREHINKLVVYGSDQTHCSFFKSAKIAGISPNNFRQVKTSRVNAFSMRPDALRAAIQADVDAGLVPFFLCTTVGTTSTAAVDPVALLCEVAKDYGMWVHIDAAYAGNACICPEFRHMINGVENADSFSFNAHKWFLTTLDCCCLWVKDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQITLSRRFRSLKMWLVLRSYGVDYLRNFLRSHVDMAAYFEQLVRMDGRFEVVVPRSFALVCFRLSASAVIQRLYDSCHRHGHGQKFLEEETLNDVNAELLESVNSAGQIYMTHSLVDGVYMLRFAVGATLTQTHHVTYAWKQVQDHASAVLARRINSICNC

[Multiple Choices]
A. 4.1.1.36
B. 3.1.3.2
C. 4.1.1.25
D. 2.7.4.9
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

> The exact sequence matches a UniProt entry annotated with EC 4.1.1.25 for L-tyrosine decarboxylation, with experimental-evidence codes cited. The entry also assigns EC 4.1.1.28 for L-DOPA decarboxylation, which is not among the choices.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a PLP-dependent decarboxylase, but that broad inference does not establish its specific substrate activity or distinguish among decarboxylase EC subclasses.


**Missing item-specific fact**

> The protein-specific evidence that this enzyme decarboxylates L-tyrosine (EC 4.1.1.25); the annotation also reports L-DOPA decarboxylation (EC 4.1.1.28).


**Reason**

> Selecting the exact EC number requires substrate-specific functional knowledge not supplied by the sequence prompt. The matched-sequence annotation supports the key but was reviewer-only information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, C is supported. However, the protein is also annotated with EC 4.1.1.28, an additional catalytic activity not offered as a choice, so the singular wording does not represent all reported activities.


### Important caveats

- The UniProt annotations cite experimental evidence, but the primary studies were not independently reviewed here.
- The matched historical and current records support sequence applicability; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a PLP-dependent decarboxylase, but that broad inference does not establish its specific substrate activity or distinguish among decarboxylase EC subclasses.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that this enzyme decarboxylates L-tyrosine (EC 4.1.1.25); the annotation also reports L-DOPA decarboxylation (EC 4.1.1.28).",
    "reason": "Selecting the exact EC number requires substrate-specific functional knowledge not supplied by the sequence prompt. The matched-sequence annotation supports the key but was reviewer-only information."
  },
  "case_id": "EC_number_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with EC 4.1.1.25 for L-tyrosine decarboxylation, with experimental-evidence codes cited. The entry also assigns EC 4.1.1.28 for L-DOPA decarboxylation, which is not among the choices."
  },
  "important_caveats": [
    "The UniProt annotations cite experimental evidence, but the primary studies were not independently reviewed here.",
    "The matched historical and current records support sequence applicability; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, C is supported. However, the protein is also annotated with EC 4.1.1.28, an additional catalytic activity not offered as a choice, so the singular wording does not represent all reported activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with EC 4.1.1.25 for L-tyrosine decarboxylation, with experimental-evidence codes cited. The entry also assigns EC 4.1.1.28 for L-DOPA decarboxylation, which is not among the choices.",
    "evidence_ids": ["C1", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a PLP-dependent decarboxylase, but that broad inference does not establish its specific substrate activity or distinguish among decarboxylase EC subclasses.",
    "missing_item_specific_fact": "The protein-specific evidence that this enzyme decarboxylates L-tyrosine (EC 4.1.1.25); the annotation also reports L-DOPA decarboxylation (EC 4.1.1.28).",
    "reason": "Selecting the exact EC number requires substrate-specific functional knowledge not supplied by the sequence prompt. The matched-sequence annotation supports the key but was reviewer-only information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, C is supported. However, the protein is also annotated with EC 4.1.1.28, an additional catalytic activity not offered as a choice, so the singular wording does not represent all reported activities."
  },
  "important_caveats": [
    "The UniProt annotations cite experimental evidence, but the primary studies were not independently reviewed here.",
    "The matched historical and current records support sequence applicability; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AA51Z3J4 (sequence matched, 522 aa) is experimentally annotated (ECO:0000269, PubMed:37675639 and PubMed:38835170) with EC 4.1.1.25 (L-tyrosine decarboxylase: L-tyrosine + H(+) = tyramine + CO2). The protein also carries EC 4.1.1.28 (L-DOPA decarboxylase) with the same experimental evidence, but 4.1.1.25 is one of the two validated EC numbers and is the only AADC-family option among the four choices. The author's key is scientifically supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The ~522-aa sequence contains hallmark motifs of PLP-dependent aromatic amino acid decarboxylases (AADC family), including the conserved 'GG' motif in the PLP-binding region (visible in 'GGGVMMGTTCEAILTTITAARDR') and the overall domain architecture (~500 aa, α/β fold). This immediately eliminates EC 3.1.3.2 (acid phosphatase, a small hydrolase with a different fold) and EC 2.7.4.9 (UMP kinase, a nucleotide-binding transferase). Among the remaining lyase options, EC 4.1.1.36 (isochorismate synthase) belongs to the chorismate-mutase-like superfamily (~200-300 aa, no PLP cofactor), which is structurally and sequence-wise incompatible with a 522-aa PLP-dependent enzyme. EC 4.1.1.25 (L-tyrosine decarboxylase) is the sole AADC-family member among the choices, making it the uniquely defensible answer.


**Missing item-specific fact**

> None critical. The protein's dual activity (also EC 4.1.1.28) is an annotation detail, but since 4.1.1.28 is not among the four options, it does not introduce ambiguity in selecting from the given choices.


**Reason**

> A knowledgeable reader can use general enzyme-family sequence signatures (PLP-binding motifs, family length, cofactor requirement) to eliminate the phosphatase, kinase, and isochorismate synthase options, leaving only the AADC-family EC number. This is a concrete biological argument from the sequence itself rather than a database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein experimentally catalyzes both EC 4.1.1.25 and EC 4.1.1.28 reactions, only 4.1.1.25 appears among the four choices. The other three options belong to entirely different enzyme classes or unrelated lyase subfamilies, so no other option is defensible.


### Important caveats

- The protein is a dual-function enzyme (EC 4.1.1.25 and EC 4.1.1.28) per experimental evidence; the question's single-answer format masks this but does not create ambiguity among the provided choices.
- The UniProt annotation is recent (first public date 2025-06-18); the author's source snapshot is unknown, though the sequence matches the current and historical entries.
- The reviewer-only evidence confirms experimental validation (ECO:0000269) from two independent studies, strengthening the annotation beyond computational transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The ~522-aa sequence contains hallmark motifs of PLP-dependent aromatic amino acid decarboxylases (AADC family), including the conserved 'GG' motif in the PLP-binding region (visible in 'GGGVMMGTTCEAILTTITAARDR') and the overall domain architecture (~500 aa, α/β fold). This immediately eliminates EC 3.1.3.2 (acid phosphatase, a small hydrolase with a different fold) and EC 2.7.4.9 (UMP kinase, a nucleotide-binding transferase). Among the remaining lyase options, EC 4.1.1.36 (isochorismate synthase) belongs to the chorismate-mutase-like superfamily (~200-300 aa, no PLP cofactor), which is structurally and sequence-wise incompatible with a 522-aa PLP-dependent enzyme. EC 4.1.1.25 (L-tyrosine decarboxylase) is the sole AADC-family member among the choices, making it the uniquely defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The protein's dual activity (also EC 4.1.1.28) is an annotation detail, but since 4.1.1.28 is not among the four options, it does not introduce ambiguity in selecting from the given choices.",
    "reason": "A knowledgeable reader can use general enzyme-family sequence signatures (PLP-binding motifs, family length, cofactor requirement) to eliminate the phosphatase, kinase, and isochorismate synthase options, leaving only the AADC-family EC number. This is a concrete biological argument from the sequence itself rather than a database lookup."
  },
  "case_id": "EC_number_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AA51Z3J4 (sequence matched, 522 aa) is experimentally annotated (ECO:0000269, PubMed:37675639 and PubMed:38835170) with EC 4.1.1.25 (L-tyrosine decarboxylase: L-tyrosine + H(+) = tyramine + CO2). The protein also carries EC 4.1.1.28 (L-DOPA decarboxylase) with the same experimental evidence, but 4.1.1.25 is one of the two validated EC numbers and is the only AADC-family option among the four choices. The author's key is scientifically supported."
  },
  "important_caveats": [
    "The protein is a dual-function enzyme (EC 4.1.1.25 and EC 4.1.1.28) per experimental evidence; the question's single-answer format masks this but does not create ambiguity among the provided choices.",
    "The UniProt annotation is recent (first public date 2025-06-18); the author's source snapshot is unknown, though the sequence matches the current and historical entries.",
    "The reviewer-only evidence confirms experimental validation (ECO:0000269) from two independent studies, strengthening the annotation beyond computational transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein experimentally catalyzes both EC 4.1.1.25 and EC 4.1.1.28 reactions, only 4.1.1.25 appears among the four choices. The other three options belong to entirely different enzyme classes or unrelated lyase subfamilies, so no other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AA51Z3J4 (sequence matched, 522 aa) is experimentally annotated (ECO:0000269, PubMed:37675639 and PubMed:38835170) with EC 4.1.1.25 (L-tyrosine decarboxylase: L-tyrosine + H(+) = tyramine + CO2). The protein also carries EC 4.1.1.28 (L-DOPA decarboxylase) with the same experimental evidence, but 4.1.1.25 is one of the two validated EC numbers and is the only AADC-family option among the four choices. The author's key is scientifically supported.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The ~522-aa sequence contains hallmark motifs of PLP-dependent aromatic amino acid decarboxylases (AADC family), including the conserved 'GG' motif in the PLP-binding region (visible in 'GGGVMMGTTCEAILTTITAARDR') and the overall domain architecture (~500 aa, α/β fold). This immediately eliminates EC 3.1.3.2 (acid phosphatase, a small hydrolase with a different fold) and EC 2.7.4.9 (UMP kinase, a nucleotide-binding transferase). Among the remaining lyase options, EC 4.1.1.36 (isochorismate synthase) belongs to the chorismate-mutase-like superfamily (~200-300 aa, no PLP cofactor), which is structurally and sequence-wise incompatible with a 522-aa PLP-dependent enzyme. EC 4.1.1.25 (L-tyrosine decarboxylase) is the sole AADC-family member among the choices, making it the uniquely defensible answer.",
    "missing_item_specific_fact": "None critical. The protein's dual activity (also EC 4.1.1.28) is an annotation detail, but since 4.1.1.28 is not among the four options, it does not introduce ambiguity in selecting from the given choices.",
    "reason": "A knowledgeable reader can use general enzyme-family sequence signatures (PLP-binding motifs, family length, cofactor requirement) to eliminate the phosphatase, kinase, and isochorismate synthase options, leaving only the AADC-family EC number. This is a concrete biological argument from the sequence itself rather than a database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein experimentally catalyzes both EC 4.1.1.25 and EC 4.1.1.28 reactions, only 4.1.1.25 appears among the four choices. The other three options belong to entirely different enzyme classes or unrelated lyase subfamilies, so no other option is defensible."
  },
  "important_caveats": [
    "The protein is a dual-function enzyme (EC 4.1.1.25 and EC 4.1.1.28) per experimental evidence; the question's single-answer format masks this but does not create ambiguity among the provided choices.",
    "The UniProt annotation is recent (first public date 2025-06-18); the author's source snapshot is unknown, though the sequence matches the current and historical entries.",
    "The reviewer-only evidence confirms experimental validation (ECO:0000269) from two independent studies, strengthening the annotation beyond computational transfer."
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

**Accession:** `A0AA51Z3J4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 9. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
"A0AA51Z3J4"
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37675639","source":"PubMed"}],"value":"Aromatic amino acid decarboxylase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"37675639","source":"PubMed"}],"value":"LwTyDC1"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"value":"4.1.1.25"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"value":"4.1.1.28"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38835170","source":"PubMed"}],"value":"L-tyrosine/L-DOPA decarboxylase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38835170","source":"PubMed"}],"value":"LwTyDC2"}]}}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:14346"}}],"reaction":{"ecNumber":"4.1.1.25","evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"name":"L-tyrosine + H(+) = tyramine + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14345"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:58315"},{"database":"ChEBI","id":"CHEBI:327995"}]}}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:12273"}}],"reaction":{"ecNumber":"4.1.1.28","evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"name":"L-dopa + H(+) = dopamine + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:12272"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:57504"},{"database":"ChEBI","id":"CHEBI:59905"}]}}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"citation":{"authors":["Watkins J.L.","Li Q.","Yeaman S.","Facchini P.J."],"citationCrossReferences":[{"database":"PubMed","id":"37675639"},{"database":"DOI","id":"10.1111/tpj.16447"}],"citationType":"journal article","firstPage":"635","id":"37675639","journal":"Plant J.","lastPage":"649","publicationDate":"2023","title":"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora williamsii).","volume":"116"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WMX25288.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"cv. Jourdaniana"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"citation":{"authors":["Berman P.","de Haro L.A.","Cavaco A.-R.","Panda S.","Dong Y.","Kuzmich N.","Lichtenstein G.","Peleg Y.","Harat H.","Jozwiak A.","Cai J.","Heinig U.","Meir S.","Rogachev I.","Aharoni A."],"citationCrossReferences":[{"database":"PubMed","id":"38835170"},{"database":"DOI","id":"10.1016/j.molp.2024.05.012"}],"citationType":"journal article","firstPage":"1129","id":"38835170","journal":"Mol. Plant","lastPage":"1150","publicationDate":"2024","title":"The biosynthetic pathway of the hallucinogen mescaline and its heterologous reconstruction.","volume":"17"},"referenceComments":[{"type":"STRAIN","value":"cv. Rehovot 7"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOTECHNOLOGY","BIOPHYSICOCHEMICAL PROPERTIES","TISSUE SPECIFICITY"]}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
ID   TYDC2_LOPWI             Reviewed;         522 AA.
AC   A0AA51Z3J4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 2.
DT   28-JAN-2026, entry version 9.
DE   RecName: Full=L-tyrosine/L-DOPA decarboxylase 2 {ECO:0000303|PubMed:38835170};
DE            Short=LwTyDC2 {ECO:0000303|PubMed:38835170};
DE            EC=4.1.1.25 {ECO:0000269|PubMed:38835170};
DE            EC=4.1.1.28 {ECO:0000269|PubMed:38835170};
DE   AltName: Full=Aromatic amino acid decarboxylase 1 {ECO:0000303|PubMed:37675639};
DE            Short=LwTyDC1 {ECO:0000303|PubMed:37675639};
GN   Name=TyDC2 {ECO:0000303|PubMed:38835170};
GN   Synonyms=TyDC1 {ECO:0000303|PubMed:37675639};
OS   Lophophora williamsii (Peyote) (Echinocactus williamsii).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Cactineae; Cactaceae; Cactoideae; Cacteae; Lophophora.
OX   NCBI_TaxID=130138;
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
DE   RecName: Full=L-tyrosine/L-DOPA decarboxylase 2 {ECO:0000303|PubMed:38835170};
DE            Short=LwTyDC2 {ECO:0000303|PubMed:38835170};
DE            EC=4.1.1.25 {ECO:0000269|PubMed:38835170};
DE            EC=4.1.1.28 {ECO:0000269|PubMed:38835170};
DE   AltName: Full=Aromatic amino acid decarboxylase 1 {ECO:0000303|PubMed:37675639};
DE            Short=LwTyDC1 {ECO:0000303|PubMed:37675639};
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 46-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-tyrosine + H(+) = tyramine + CO2; Xref=Rhea:RHEA:14345,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:58315,
CC         ChEBI:CHEBI:327995; EC=4.1.1.25;
CC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14346;
CC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 53-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-dopa + H(+) = dopamine + CO2; Xref=Rhea:RHEA:12272,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57504,
CC         ChEBI:CHEBI:59905; EC=4.1.1.28;
CC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:12273;
CC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
