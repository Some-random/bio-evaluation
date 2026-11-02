# cofactor_0159

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — pyridoxal 5&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKFLQIIKHLKLQNKKNALDNFVNCRTYEHISNINKLFLNNFSSTKEHSEHGQVKHENFLNSTLKYEENSQNGSTNNLKNGKYNMYVSEGNVNINEEKYKDNNISSNNTQYNNNSSNSGSLNDEGPLWKEHIDDVVNENKKKKMNRFYLDSQATTMIDPRVLDKMLPYMTYIYGNAHSRNHFFGWESEKAVEDARTNLLNLINGKNNKEIIFTSGATESNNLALIGICTYYNKLNKQKNHIITSQIEHKCILQTCRFLQTKGFEVTYLKPDTNGLVKLDDIKNSIKDNTIMASFIFVNNEIGVIQDIENIGNLCKEKNILFHTDASQAAGKVPIDVQKMNIDLMSMSGHKLYGPKGIGALYIKRKKPNIRLNALIHGGGQERGLRSGTLPTHLIVGFGEAAKVCSLEMNRDEKKVRYFFNYVKDYLTKHLDYIVFNGCQINRYYGNMNISFLFVEGESLLMSLNEIALSSGSACTSSTLEPSYVLRSIGISEDIAHTSIRIGFNRFTTFFEVQQLCINLVKSVERLRSISPLYEMELEKKNPSNDDIPKFIWT

[Multiple Choices]
A. FMN
B. Mn(2+)
C. pyridoxal 5'-phosphate
D. Fe cation
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

> The sequence exactly matches the annotated Plasmodium falciparum IscS cysteine desulfurase. Its UniProt cofactor annotation names pyridoxal 5'-phosphate, supporting choice C. The cited annotation is curated evidence, not by itself an independently presented experimental measurement.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Once the protein is identified as an IscS cysteine desulfurase, its enzyme family is associated with PLP-dependent catalysis. But the prompt supplies no function, organism, or other explicit context establishing that identity.


**Missing item-specific fact**

> The sequence's assignment to the IscS cysteine-desulfurase family, or equivalent protein-specific functional annotation, is needed to select PLP over the listed alternatives.


**Reason**

> The key is supported by the matched protein annotation, but recognizing or establishing this protein family from the sequence requires item-specific sequence-family knowledge; the choices alone do not provide a reliable general biological discriminator.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> For the annotated IscS protein, PLP is the supported cofactor choice; its role in iron-sulfur biogenesis does not make iron the answer to the cofactor question.


### Important caveats

- The historical and current records both match the supplied sequence, but the author's exact source snapshot is unknown.
- The cited UniProt cofactor evidence is annotated with ECO:0000305 and refers to a publication; the provided excerpts do not independently establish the experimental details.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Once the protein is identified as an IscS cysteine desulfurase, its enzyme family is associated with PLP-dependent catalysis. But the prompt supplies no function, organism, or other explicit context establishing that identity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's assignment to the IscS cysteine-desulfurase family, or equivalent protein-specific functional annotation, is needed to select PLP over the listed alternatives.",
    "reason": "The key is supported by the matched protein annotation, but recognizing or establishing this protein family from the sequence requires item-specific sequence-family knowledge; the choices alone do not provide a reliable general biological discriminator."
  },
  "case_id": "cofactor_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the annotated Plasmodium falciparum IscS cysteine desulfurase. Its UniProt cofactor annotation names pyridoxal 5'-phosphate, supporting choice C. The cited annotation is curated evidence, not by itself an independently presented experimental measurement."
  },
  "important_caveats": [
    "The historical and current records both match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited UniProt cofactor evidence is annotated with ECO:0000305 and refers to a publication; the provided excerpts do not independently establish the experimental details."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For the annotated IscS protein, PLP is the supported cofactor choice; its role in iron-sulfur biogenesis does not make iron the answer to the cofactor question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the annotated Plasmodium falciparum IscS cysteine desulfurase. Its UniProt cofactor annotation names pyridoxal 5'-phosphate, supporting choice C. The cited annotation is curated evidence, not by itself an independently presented experimental measurement.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Once the protein is identified as an IscS cysteine desulfurase, its enzyme family is associated with PLP-dependent catalysis. But the prompt supplies no function, organism, or other explicit context establishing that identity.",
    "missing_item_specific_fact": "The sequence's assignment to the IscS cysteine-desulfurase family, or equivalent protein-specific functional annotation, is needed to select PLP over the listed alternatives.",
    "reason": "The key is supported by the matched protein annotation, but recognizing or establishing this protein family from the sequence requires item-specific sequence-family knowledge; the choices alone do not provide a reliable general biological discriminator."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For the annotated IscS protein, PLP is the supported cofactor choice; its role in iron-sulfur biogenesis does not make iron the answer to the cofactor question."
  },
  "important_caveats": [
    "The historical and current records both match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited UniProt cofactor evidence is annotated with ECO:0000305 and refers to a publication; the provided excerpts do not independently establish the experimental details."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IBI5 (Cysteine desulfurase IscS, EC 2.8.1.7, Plasmodium falciparum) explicitly annotates pyridoxal 5'-phosphate as the cofactor (C5, H5), with evidence code ECO:0000305 (curator-inferred) linked to PubMed:34032321. This is also consistent with the universal biochemistry of the IscS/NFS cysteine desulfurase family (EC 2.8.1.7), which is defined as PLP-dependent: PLP forms a Schiff base with the catalytic cysteine and acts as an electron sink during β-replacement. The sequence match is exact (553 aa, SHA256 matched). The answer C is well-supported.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable catalytic cysteine motif region ('SGATESNNLALIGICTYYNK') consistent with the IscS/NFS cysteine desulfurase family, which universally requires PLP as its catalytic cofactor. A model with general biochemistry knowledge can: (1) identify the SGCT-like catalytic cysteine motif to assign the protein to the cysteine desulfurase family; (2) recall that EC 2.8.1.7 (cysteine desulfurase) is defined as PLP-dependent across all known members; (3) eliminate FMN (oxidoreductase cofactor), Mn²⁺ (not associated with this enzyme class), and Fe (the substrate/product component in Fe-S cluster assembly, not the catalytic cofactor of the desulfurase reaction itself). The distinction between Fe as a product component vs. PLP as the catalytic cofactor is a concrete biochemical argument.


**Missing item-specific fact**

> None critical. The identification of the SGCT-like motif in a Plasmodium sequence with unusual N/Q-rich composition adds difficulty, but the motif is present and the PLP dependence of IscS is a general, well-established biochemical fact, not a protein-specific lookup.


**Reason**

> The catalytic cysteine motif is identifiable in the sequence, and the PLP requirement of the IscS family is a fundamental biochemical property (not an obscure experimental finding). The distractors are eliminable through general enzyme-class knowledge. While recognizing the motif in a Plasmodium protein with atypical amino acid composition is non-trivial, it does not require a protein-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D (Fe cation) might superficially attract a model because the protein participates in Fe-S cluster biogenesis, but Fe is not the catalytic cofactor of the desulfurase reaction (L-cysteine → L-alanine + sulfide); PLP is. The question asks for the cofactor required for catalytic activity, which unambiguously points to PLP. No other option is defensible for EC 2.8.1.7.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000305 (curator-inferred), not direct experimental evidence code. However, the PLP dependence of IscS is a well-established family-wide biochemical property supported by the cited 2021 Sadik et al. study and decades of literature on bacterial IscS.
- The Plasmodium falciparum IscS entry was only integrated into Swiss-Prot on 2025-04-09. If the benchmark was constructed before this date, the author likely relied on computational annotation or homology transfer rather than a curated Swiss-Prot entry.
- The sequence has extensive N/Q/S-rich regions typical of Plasmodium proteins, which may obscure motif recognition and add practical difficulty despite the reasoning pathway being available in principle.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable catalytic cysteine motif region ('SGATESNNLALIGICTYYNK') consistent with the IscS/NFS cysteine desulfurase family, which universally requires PLP as its catalytic cofactor. A model with general biochemistry knowledge can: (1) identify the SGCT-like catalytic cysteine motif to assign the protein to the cysteine desulfurase family; (2) recall that EC 2.8.1.7 (cysteine desulfurase) is defined as PLP-dependent across all known members; (3) eliminate FMN (oxidoreductase cofactor), Mn²⁺ (not associated with this enzyme class), and Fe (the substrate/product component in Fe-S cluster assembly, not the catalytic cofactor of the desulfurase reaction itself). The distinction between Fe as a product component vs. PLP as the catalytic cofactor is a concrete biochemical argument.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The identification of the SGCT-like motif in a Plasmodium sequence with unusual N/Q-rich composition adds difficulty, but the motif is present and the PLP dependence of IscS is a general, well-established biochemical fact, not a protein-specific lookup.",
    "reason": "The catalytic cysteine motif is identifiable in the sequence, and the PLP requirement of the IscS family is a fundamental biochemical property (not an obscure experimental finding). The distractors are eliminable through general enzyme-class knowledge. While recognizing the motif in a Plasmodium protein with atypical amino acid composition is non-trivial, it does not require a protein-specific database lookup."
  },
  "case_id": "cofactor_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IBI5 (Cysteine desulfurase IscS, EC 2.8.1.7, Plasmodium falciparum) explicitly annotates pyridoxal 5'-phosphate as the cofactor (C5, H5), with evidence code ECO:0000305 (curator-inferred) linked to PubMed:34032321. This is also consistent with the universal biochemistry of the IscS/NFS cysteine desulfurase family (EC 2.8.1.7), which is defined as PLP-dependent: PLP forms a Schiff base with the catalytic cysteine and acts as an electron sink during β-replacement. The sequence match is exact (553 aa, SHA256 matched). The answer C is well-supported."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000305 (curator-inferred), not direct experimental evidence code. However, the PLP dependence of IscS is a well-established family-wide biochemical property supported by the cited 2021 Sadik et al. study and decades of literature on bacterial IscS.",
    "The Plasmodium falciparum IscS entry was only integrated into Swiss-Prot on 2025-04-09. If the benchmark was constructed before this date, the author likely relied on computational annotation or homology transfer rather than a curated Swiss-Prot entry.",
    "The sequence has extensive N/Q/S-rich regions typical of Plasmodium proteins, which may obscure motif recognition and add practical difficulty despite the reasoning pathway being available in principle."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (Fe cation) might superficially attract a model because the protein participates in Fe-S cluster biogenesis, but Fe is not the catalytic cofactor of the desulfurase reaction (L-cysteine → L-alanine + sulfide); PLP is. The question asks for the cofactor required for catalytic activity, which unambiguously points to PLP. No other option is defensible for EC 2.8.1.7."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IBI5 (Cysteine desulfurase IscS, EC 2.8.1.7, Plasmodium falciparum) explicitly annotates pyridoxal 5'-phosphate as the cofactor (C5, H5), with evidence code ECO:0000305 (curator-inferred) linked to PubMed:34032321. This is also consistent with the universal biochemistry of the IscS/NFS cysteine desulfurase family (EC 2.8.1.7), which is defined as PLP-dependent: PLP forms a Schiff base with the catalytic cysteine and acts as an electron sink during β-replacement. The sequence match is exact (553 aa, SHA256 matched). The answer C is well-supported.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable catalytic cysteine motif region ('SGATESNNLALIGICTYYNK') consistent with the IscS/NFS cysteine desulfurase family, which universally requires PLP as its catalytic cofactor. A model with general biochemistry knowledge can: (1) identify the SGCT-like catalytic cysteine motif to assign the protein to the cysteine desulfurase family; (2) recall that EC 2.8.1.7 (cysteine desulfurase) is defined as PLP-dependent across all known members; (3) eliminate FMN (oxidoreductase cofactor), Mn²⁺ (not associated with this enzyme class), and Fe (the substrate/product component in Fe-S cluster assembly, not the catalytic cofactor of the desulfurase reaction itself). The distinction between Fe as a product component vs. PLP as the catalytic cofactor is a concrete biochemical argument.",
    "missing_item_specific_fact": "None critical. The identification of the SGCT-like motif in a Plasmodium sequence with unusual N/Q-rich composition adds difficulty, but the motif is present and the PLP dependence of IscS is a general, well-established biochemical fact, not a protein-specific lookup.",
    "reason": "The catalytic cysteine motif is identifiable in the sequence, and the PLP requirement of the IscS family is a fundamental biochemical property (not an obscure experimental finding). The distractors are eliminable through general enzyme-class knowledge. While recognizing the motif in a Plasmodium protein with atypical amino acid composition is non-trivial, it does not require a protein-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (Fe cation) might superficially attract a model because the protein participates in Fe-S cluster biogenesis, but Fe is not the catalytic cofactor of the desulfurase reaction (L-cysteine → L-alanine + sulfide); PLP is. The question asks for the cofactor required for catalytic activity, which unambiguously points to PLP. No other option is defensible for EC 2.8.1.7."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000305 (curator-inferred), not direct experimental evidence code. However, the PLP dependence of IscS is a well-established family-wide biochemical property supported by the cited 2021 Sadik et al. study and decades of literature on bacterial IscS.",
    "The Plasmodium falciparum IscS entry was only integrated into Swiss-Prot on 2025-04-09. If the benchmark was constructed before this date, the author likely relied on computational annotation or homology transfer rather than a curated Swiss-Prot entry.",
    "The sequence has extensive N/Q/S-rich regions typical of Plasmodium proteins, which may obscure motif recognition and add practical difficulty despite the reasoning pathway being available in principle."
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

**Accession:** `Q8IBI5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 127. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.723158+00:00.  

```json
"Q8IBI5"
```

Source SHA-256: `dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.723158+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34032321","source":"PubMed"}],"value":"2.8.1.7"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cysteine desulfurase IscS"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34032321","source":"PubMed"}],"value":"PfIscS"}]}}
```

Source SHA-256: `dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.723158+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:597326"},"evidences":[{"evidenceCode":"ECO:0000305","id":"34032321","source":"PubMed"}],"name":"pyridoxal 5'-phosphate"}],"commentType":"COFACTOR"}
```

Source SHA-256: `dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:06.723158+00:00.  

```json
{"citation":{"authors":["Sadik M.","Afsar M.","Ramachandran R.","Habib S."],"citationCrossReferences":[{"database":"PubMed","id":"34032321"},{"database":"DOI","id":"10.1111/mmi.14735"}],"citationType":"journal article","firstPage":"606","id":"34032321","journal":"Mol. Microbiol.","lastPage":"623","publicationDate":"2021","title":"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.","volume":"116"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBUNIT","INTERACTION WITH ISD11 AND ISCU"]}
```

Source SHA-256: `dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-02T04:32:12.658506+00:00.  

```text
ID   ISCS_PLAF7              Reviewed;         553 AA.
AC   Q8IBI5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAR-2003, sequence version 1.
DT   28-JAN-2026, entry version 127.
DE   RecName: Full=Cysteine desulfurase IscS {ECO:0000305};
DE            Short=PfIscS {ECO:0000303|PubMed:34032321};
DE            EC=2.8.1.7 {ECO:0000269|PubMed:34032321};
GN   Name=IscS {ECO:0000303|PubMed:24086138, ECO:0000303|PubMed:34032321};
GN   Synonyms=NFS1 {ECO:0000305};
GN   ORFNames=PF3D7_0727200 {ECO:0000312|EMBL:CAD51015.1};
OS   Plasmodium falciparum (isolate 3D7).
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).
OX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};
```

Source SHA-256: `1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-02T04:32:12.658506+00:00.  

```text
DE   RecName: Full=Cysteine desulfurase IscS {ECO:0000305};
DE            Short=PfIscS {ECO:0000303|PubMed:34032321};
DE            EC=2.8.1.7 {ECO:0000269|PubMed:34032321};
```

Source SHA-256: `1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)  
**Locator:** `lines 58-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-02T04:32:12.658506+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, AND INTERACTION WITH ISD11
RP   AND ISCU.
RX   PubMed=34032321; DOI=10.1111/mmi.14735;
RA   Sadik M., Afsar M., Ramachandran R., Habib S.;
RT   "[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the
RT   Plasmodium falciparum mitochondrion.";
RL   Mol. Microbiol. 116:606-623(2021).
```

Source SHA-256: `1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)  
**Locator:** `lines 78-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-02T04:32:12.658506+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;
CC         Evidence={ECO:0000305|PubMed:34032321};
```

Source SHA-256: `1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 159. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
