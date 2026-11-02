# cofactor_0003

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — &#91;2Fe-2S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. Co(2+)
B. [2Fe-2S] cluster
C. tungstopterin
D. Mo-bis(molybdopterin guanine dinucleotide)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact-sequence-matched UniProt entry annotates one &#91;2Fe-2S&#93; cluster per subunit, supporting choice B. This is a homology-transferred annotation, not direct experimental evidence for this particular protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A cysteine-containing enzyme sequence may suggest metal or iron-sulfur binding, but the supplied sequence and choices do not establish the protein's identity or distinguish this specific cluster from other cofactors.


**Missing item-specific fact**

> The protein-specific identification as dihydroxy-acid dehydratase and its annotated &#91;2Fe-2S&#93; cofactor are needed to select B; that annotation is absent from the input.


**Reason**

> The key is supported by reviewer-only database evidence, but that evidence was not supplied to the evaluated model. A generic sequence heuristic does not reliably establish the precise cofactor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the sequence-matched annotation supports B. The entry also annotates Mg(2+), but magnesium is not an option.


### Important caveats

- The cofactor annotation is based on similarity evidence from other UniProt entries, rather than cited direct measurement on this exact protein.
- The matching entry identifies the protein as mitochondrial dihydroxy-acid dehydratase; that identity is reviewer-only evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A cysteine-containing enzyme sequence may suggest metal or iron-sulfur binding, but the supplied sequence and choices do not establish the protein's identity or distinguish this specific cluster from other cofactors.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as dihydroxy-acid dehydratase and its annotated [2Fe-2S] cofactor are needed to select B; that annotation is absent from the input.",
    "reason": "The key is supported by reviewer-only database evidence, but that evidence was not supplied to the evaluated model. A generic sequence heuristic does not reliably establish the precise cofactor."
  },
  "case_id": "cofactor_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt entry annotates one [2Fe-2S] cluster per subunit, supporting choice B. This is a homology-transferred annotation, not direct experimental evidence for this particular protein."
  },
  "important_caveats": [
    "The cofactor annotation is based on similarity evidence from other UniProt entries, rather than cited direct measurement on this exact protein.",
    "The matching entry identifies the protein as mitochondrial dihydroxy-acid dehydratase; that identity is reviewer-only evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched annotation supports B. The entry also annotates Mg(2+), but magnesium is not an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched UniProt entry annotates one [2Fe-2S] cluster per subunit, supporting choice B. This is a homology-transferred annotation, not direct experimental evidence for this particular protein.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A cysteine-containing enzyme sequence may suggest metal or iron-sulfur binding, but the supplied sequence and choices do not establish the protein's identity or distinguish this specific cluster from other cofactors.",
    "missing_item_specific_fact": "The protein-specific identification as dihydroxy-acid dehydratase and its annotated [2Fe-2S] cofactor are needed to select B; that annotation is absent from the input.",
    "reason": "The key is supported by reviewer-only database evidence, but that evidence was not supplied to the evaluated model. A generic sequence heuristic does not reliably establish the precise cofactor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched annotation supports B. The entry also annotates Mg(2+), but magnesium is not an option."
  },
  "important_caveats": [
    "The cofactor annotation is based on similarity evidence from other UniProt entries, rather than cited direct measurement on this exact protein.",
    "The matching entry identifies the protein as mitochondrial dihydroxy-acid dehydratase; that identity is reviewer-only evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0F7TWW9 (Dihydroxy-acid dehydratase pbrD, EC 4.2.1.9, mitochondrial) annotates a &#91;2Fe-2S&#93; cluster as a cofactor (C5, H4), with evidence code ECO:0000250 (similarity-based transfer from Q0CPG9 and P39522, both characterized DHAD proteins). Mitochondrial DHAD (ILV3-type) is a well-established &#91;2Fe-2S&#93;-containing enzyme in branched-chain amino acid biosynthesis; the Fe-S cluster is a hallmark of this enzyme family. While the annotation for this specific protein is transferred by homology rather than directly measured, the family-level biochemistry is firmly established. The expected answer B is consistent with the annotation and with general DHAD biochemistry.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an N-terminal mitochondrial targeting sequence (Arg/Ser/Thr-rich), dehydratase-like catalytic architecture, and multiple cysteine residues in conserved positions (e.g., CPGKGACGGMYTANTL, SCPADDPKKL, YCALVSDASHGCVTDGPI) consistent with &#91;2Fe-2S&#93; coordination. Recognizing the protein as a mitochondrial dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) from these features, combined with the well-established biochemical fact that the mitochondrial/ILV3-type DHAD requires a &#91;2Fe-2S&#93; cluster for catalysis, allows elimination of the distractors: Co(2+) is exclusive to B12-dependent enzymes, tungstopterin to tungsten oxidoreductases (primarily in anaerobes), and Mo-bis(MGD) to molybdenum oxidoreductases. None of these cofactor classes are associated with dehydratases or with fungal mitochondrial enzymes.


**Missing item-specific fact**

> None critical. The reasoning relies on general DHAD family biochemistry (mitochondrial DHAD = &#91;2Fe-2S&#93;) and sequence-level features (targeting peptide, cysteine motifs, dehydratase fold), not on an obscure protein-specific annotation.


**Reason**

> A model with general protein biochemistry knowledge can identify the mitochondrial targeting sequence, recognize dehydratase architecture, note cysteine residues suggestive of Fe-S coordination, and use the well-known fact that mitochondrial DHAD is a &#91;2Fe-2S&#93; enzyme to select B over the three mechanistically unrelated distractors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although UniProt also lists Mg(2+) as a cofactor for this enzyme, Mg(2+) is not among the four choices. The four options represent four mechanistically distinct cofactor classes, only one of which (&#91;2Fe-2S&#93;) is compatible with DHAD biochemistry. No ambiguity exists among the provided choices.


### Important caveats

- The &#91;2Fe-2S&#93; annotation for this specific protein (A0A0F7TWW9) carries evidence code ECO:0000250 (similarity), i.e., it is transferred by homology from characterized DHAD proteins (Q0CPG9, P39522) rather than directly experimentally verified for this pbrD protein.
- The UniProt entry was first public in April 2025 and reviewed in January 2026; the benchmark author's source snapshot is unknown but the sequence matches the current and historical (v30) records.
- The protein is a precursor (mitochondrial targeting sequence included); the mature catalytic domain retains the &#91;2Fe-2S&#93; cluster.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an N-terminal mitochondrial targeting sequence (Arg/Ser/Thr-rich), dehydratase-like catalytic architecture, and multiple cysteine residues in conserved positions (e.g., CPGKGACGGMYTANTL, SCPADDPKKL, YCALVSDASHGCVTDGPI) consistent with [2Fe-2S] coordination. Recognizing the protein as a mitochondrial dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) from these features, combined with the well-established biochemical fact that the mitochondrial/ILV3-type DHAD requires a [2Fe-2S] cluster for catalysis, allows elimination of the distractors: Co(2+) is exclusive to B12-dependent enzymes, tungstopterin to tungsten oxidoreductases (primarily in anaerobes), and Mo-bis(MGD) to molybdenum oxidoreductases. None of these cofactor classes are associated with dehydratases or with fungal mitochondrial enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The reasoning relies on general DHAD family biochemistry (mitochondrial DHAD = [2Fe-2S]) and sequence-level features (targeting peptide, cysteine motifs, dehydratase fold), not on an obscure protein-specific annotation.",
    "reason": "A model with general protein biochemistry knowledge can identify the mitochondrial targeting sequence, recognize dehydratase architecture, note cysteine residues suggestive of Fe-S coordination, and use the well-known fact that mitochondrial DHAD is a [2Fe-2S] enzyme to select B over the three mechanistically unrelated distractors."
  },
  "case_id": "cofactor_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWW9 (Dihydroxy-acid dehydratase pbrD, EC 4.2.1.9, mitochondrial) annotates a [2Fe-2S] cluster as a cofactor (C5, H4), with evidence code ECO:0000250 (similarity-based transfer from Q0CPG9 and P39522, both characterized DHAD proteins). Mitochondrial DHAD (ILV3-type) is a well-established [2Fe-2S]-containing enzyme in branched-chain amino acid biosynthesis; the Fe-S cluster is a hallmark of this enzyme family. While the annotation for this specific protein is transferred by homology rather than directly measured, the family-level biochemistry is firmly established. The expected answer B is consistent with the annotation and with general DHAD biochemistry."
  },
  "important_caveats": [
    "The [2Fe-2S] annotation for this specific protein (A0A0F7TWW9) carries evidence code ECO:0000250 (similarity), i.e., it is transferred by homology from characterized DHAD proteins (Q0CPG9, P39522) rather than directly experimentally verified for this pbrD protein.",
    "The UniProt entry was first public in April 2025 and reviewed in January 2026; the benchmark author's source snapshot is unknown but the sequence matches the current and historical (v30) records.",
    "The protein is a precursor (mitochondrial targeting sequence included); the mature catalytic domain retains the [2Fe-2S] cluster."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although UniProt also lists Mg(2+) as a cofactor for this enzyme, Mg(2+) is not among the four choices. The four options represent four mechanistically distinct cofactor classes, only one of which ([2Fe-2S]) is compatible with DHAD biochemistry. No ambiguity exists among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWW9 (Dihydroxy-acid dehydratase pbrD, EC 4.2.1.9, mitochondrial) annotates a [2Fe-2S] cluster as a cofactor (C5, H4), with evidence code ECO:0000250 (similarity-based transfer from Q0CPG9 and P39522, both characterized DHAD proteins). Mitochondrial DHAD (ILV3-type) is a well-established [2Fe-2S]-containing enzyme in branched-chain amino acid biosynthesis; the Fe-S cluster is a hallmark of this enzyme family. While the annotation for this specific protein is transferred by homology rather than directly measured, the family-level biochemistry is firmly established. The expected answer B is consistent with the annotation and with general DHAD biochemistry.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an N-terminal mitochondrial targeting sequence (Arg/Ser/Thr-rich), dehydratase-like catalytic architecture, and multiple cysteine residues in conserved positions (e.g., CPGKGACGGMYTANTL, SCPADDPKKL, YCALVSDASHGCVTDGPI) consistent with [2Fe-2S] coordination. Recognizing the protein as a mitochondrial dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) from these features, combined with the well-established biochemical fact that the mitochondrial/ILV3-type DHAD requires a [2Fe-2S] cluster for catalysis, allows elimination of the distractors: Co(2+) is exclusive to B12-dependent enzymes, tungstopterin to tungsten oxidoreductases (primarily in anaerobes), and Mo-bis(MGD) to molybdenum oxidoreductases. None of these cofactor classes are associated with dehydratases or with fungal mitochondrial enzymes.",
    "missing_item_specific_fact": "None critical. The reasoning relies on general DHAD family biochemistry (mitochondrial DHAD = [2Fe-2S]) and sequence-level features (targeting peptide, cysteine motifs, dehydratase fold), not on an obscure protein-specific annotation.",
    "reason": "A model with general protein biochemistry knowledge can identify the mitochondrial targeting sequence, recognize dehydratase architecture, note cysteine residues suggestive of Fe-S coordination, and use the well-known fact that mitochondrial DHAD is a [2Fe-2S] enzyme to select B over the three mechanistically unrelated distractors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although UniProt also lists Mg(2+) as a cofactor for this enzyme, Mg(2+) is not among the four choices. The four options represent four mechanistically distinct cofactor classes, only one of which ([2Fe-2S]) is compatible with DHAD biochemistry. No ambiguity exists among the provided choices."
  },
  "important_caveats": [
    "The [2Fe-2S] annotation for this specific protein (A0A0F7TWW9) carries evidence code ECO:0000250 (similarity), i.e., it is transferred by homology from characterized DHAD proteins (Q0CPG9, P39522) rather than directly experimentally verified for this pbrD protein.",
    "The UniProt entry was first public in April 2025 and reviewed in January 2026; the benchmark author's source snapshot is unknown but the sequence matches the current and historical (v30) records.",
    "The protein is a precursor (mitochondrial targeting sequence included); the mature catalytic domain retains the [2Fe-2S] cluster."
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

**Accession:** `A0A0F7TWW9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
"A0A0F7TWW9"
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39511739","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase pbrD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.826200+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:190135"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q0CPG9","source":"UniProtKB"}],"name":"[2Fe-2S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39522","source":"UniProtKB"}],"value":"Binds 1 [2Fe-2S] cluster per subunit."}]}}
```

Source SHA-256: `9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
ID   PBRD_PENBI              Reviewed;         596 AA.
AC   A0A0F7TWW9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 2.
DT   28-JAN-2026, entry version 30.
DE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};
DE            Short=DHAD astD {ECO:0000303|PubMed:39511739};
DE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};
DE   Flags: Precursor;
GN   Name=pbrD {ECO:0000303|PubMed:39511739}; ORFNames=PMG11_09713;
OS   Penicillium brasilianum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=104259;
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
DE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};
DE            Short=DHAD astD {ECO:0000303|PubMed:39511739};
DE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};
DE   Flags: Precursor;
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)  
**Locator:** `lines 58-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 2.  
**Retrieved:** 2026-11-02T04:24:04.510512+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;
CC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};
CC       Note=Binds 1 [2Fe-2S] cluster per subunit.
CC       {ECO:0000250|UniProtKB:P39522};
```

Source SHA-256: `5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
