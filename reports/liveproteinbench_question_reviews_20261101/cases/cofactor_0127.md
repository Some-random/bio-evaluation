# cofactor_0127

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — heme

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGASTFSQSFAEGYAAWALMLPALVGCALLIYRAFFAIRYPANLPLAGEPDGKRTFSWRTRWRYYIDCEALYKETYDNYTKHGKTVLLPGLGFRHDIVLPQSAMRDIMARPEKELSHADAVLELVQLKYSLGHEKYKADPWPCMLVKSDINSKLEAVCDGMNEELKYAFDKYVGCDTESWKEVDLLETIRMIIMAAASRFTVGFPLCRSEAYLRACWKVNDGIMMNGGLTGATPRLLRPIVGPLVTMKLRQSIEQVKKHVEPIYRQRVQALSQQNSAEKPASDETQDLFQQMLRYAQRERPGELHDLPSMCRRLCFANFAAVHQTTLLVTNMVLNIVSSDPQHNTISVLRDEVKDVIGPDSNAKWTKYKVAQMIKSDSVARETMRLYSNTNRGVFRKVLVEGIKTEDGIELPKGAYVSFLGRPLQCDPETFEDPFEYNPFRFSRIREQAPRDTKGRSSASHLSFVSTSPEHLPFGHGGHSCPGRFLVDFEVKMIVAYLLMNYDVEFPAEYKGQRPANRWMAEALMPPSGARIRIKRRS

[Multiple Choices]
A. Mn(2+)
B. cob(II)alamin
C. heme b
D. heme
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

> The sequence-matched UniProt entry annotates the protein as cytochrome P450 monooxygenase astC and lists heme as its cofactor. The cofactor annotation is transferred from another UniProt entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a characteristic P450 heme-binding motif, and P450 enzymes are generally heme-dependent. This supports a heme cofactor but does not establish whether the intended answer label is the broad term “heme” or the more specific “heme b.”


**Missing item-specific fact**

> The protein-specific annotation uses the term “heme”; that label is not supplied in the question. The sequence-based P450 inference alone does not settle the benchmark’s distinction between the overlapping options.


**Reason**

> General biological reasoning supports heme dependence, but selecting the keyed wording over the more specific heme b option depends on the protein-specific annotation or an unstated convention about answer specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Heme b is a specific form of heme, and P450 enzymes commonly use heme b. Thus both “heme b” and the broader “heme” are defensible descriptions, although the cited database annotation says simply “heme.”


### Important caveats

- The sequence matches the reviewed UniProt record, but the cited cofactor annotation is transferred by similarity rather than shown here as a direct measurement.
- The historical annotation also lists heme; the exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a characteristic P450 heme-binding motif, and P450 enzymes are generally heme-dependent. This supports a heme cofactor but does not establish whether the intended answer label is the broad term “heme” or the more specific “heme b.”",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation uses the term “heme”; that label is not supplied in the question. The sequence-based P450 inference alone does not settle the benchmark’s distinction between the overlapping options.",
    "reason": "General biological reasoning supports heme dependence, but selecting the keyed wording over the more specific heme b option depends on the protein-specific annotation or an unstated convention about answer specificity."
  },
  "case_id": "cofactor_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the protein as cytochrome P450 monooxygenase astC and lists heme as its cofactor. The cofactor annotation is transferred from another UniProt entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The sequence matches the reviewed UniProt record, but the cited cofactor annotation is transferred by similarity rather than shown here as a direct measurement.",
    "The historical annotation also lists heme; the exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Heme b is a specific form of heme, and P450 enzymes commonly use heme b. Thus both “heme b” and the broader “heme” are defensible descriptions, although the cited database annotation says simply “heme.”"
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the protein as cytochrome P450 monooxygenase astC and lists heme as its cofactor. The cofactor annotation is transferred from another UniProt entry (ECO:0000250), so it supports the key but is not direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a characteristic P450 heme-binding motif, and P450 enzymes are generally heme-dependent. This supports a heme cofactor but does not establish whether the intended answer label is the broad term “heme” or the more specific “heme b.”",
    "missing_item_specific_fact": "The protein-specific annotation uses the term “heme”; that label is not supplied in the question. The sequence-based P450 inference alone does not settle the benchmark’s distinction between the overlapping options.",
    "reason": "General biological reasoning supports heme dependence, but selecting the keyed wording over the more specific heme b option depends on the protein-specific annotation or an unstated convention about answer specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Heme b is a specific form of heme, and P450 enzymes commonly use heme b. Thus both “heme b” and the broader “heme” are defensible descriptions, although the cited database annotation says simply “heme.”"
  },
  "important_caveats": [
    "The sequence matches the reviewed UniProt record, but the cited cofactor annotation is transferred by similarity rather than shown here as a direct measurement.",
    "The historical annotation also lists heme; the exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q0CPG6 (Cytochrome P450 monooxygenase astC from Aspergillus terreus) explicitly states COFACTOR: Name=heme (C5, H4). The protein is annotated as a cytochrome P450 monooxygenase with experimental functional characterization (PubMed:29995859). All cytochrome P450 enzymes require heme as their prosthetic group, which is consistent with the annotation. The evidence code is ECO:0000250 (inferred by similarity from P04798, another P450), which is a transferred annotation rather than direct experimental determination for this specific protein, but the P450 superfamily heme requirement is an established biochemical fact. However, the ChEBI cross-reference (CHEBI:30413) points specifically to 'heme b,' making choice C also technically accurate.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable cytochrome P450 signature motifs, including the conserved heme-ligating cysteine within an FxxGxxxCxG-like motif (visible in the 'FGHGGHSCP' region near the C-terminus) and the conserved I-helix region. Recognition of these P450 hallmarks allows a model to conclude the enzyme requires heme as its prosthetic group, eliminating Mn(2+) (A) and cob(II)alamin (B). In standard biochemical usage, the P450 prosthetic group is referred to as 'heme,' making D the conventional answer.


**Missing item-specific fact**

> The distinction between choices C (heme b) and D (heme) depends on the specific naming convention used in the UniProt annotation field rather than on a biological fact, since P450s use heme b specifically and 'heme' is the common shorthand. This is a nomenclature convention issue rather than a missing experimental fact.


**Reason**

> The core reasoning (P450 motif recognition → heme cofactor) is derivable from the sequence using general enzymology knowledge. The elimination of Mn(2+) and cob(II)alamin is straightforward. The remaining C vs D distinction is a nomenclature subtlety rather than a biological fact requiring lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The UniProt annotation uses 'heme' as the name field (supporting D) but cross-references to CHEBI:30413, which is 'heme b' specifically (supporting C). P450 enzymes use heme b (protoporphyrin IX with iron, non-covalently bound), not heme c or heme d. In precise biochemical terminology, 'heme b' is the correct specific designation, while 'heme' is the commonly used general term. Presenting both as mutually exclusive options creates genuine ambiguity, as both are correct at different levels of specificity.


### Important caveats

- The cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from P04798, a characterized P450), not direct experimental determination for astC itself.
- The distinction between 'heme' and 'heme b' in this MCQ is artificial: CHEBI:30413 (the cross-reference in the annotation) IS heme b, so the annotation simultaneously supports both C and D.
- The P450 identity is well-supported by the protein name annotation and the 2018 Nature paper characterizing astC function, but the heme cofactor assignment is by superfamily analogy rather than direct spectroscopic or crystallographic evidence for this specific enzyme.
- Sequence match is confirmed (SHA256 match between benchmark and UniProt entries C1/H1).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable cytochrome P450 signature motifs, including the conserved heme-ligating cysteine within an FxxGxxxCxG-like motif (visible in the 'FGHGGHSCP' region near the C-terminus) and the conserved I-helix region. Recognition of these P450 hallmarks allows a model to conclude the enzyme requires heme as its prosthetic group, eliminating Mn(2+) (A) and cob(II)alamin (B). In standard biochemical usage, the P450 prosthetic group is referred to as 'heme,' making D the conventional answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The distinction between choices C (heme b) and D (heme) depends on the specific naming convention used in the UniProt annotation field rather than on a biological fact, since P450s use heme b specifically and 'heme' is the common shorthand. This is a nomenclature convention issue rather than a missing experimental fact.",
    "reason": "The core reasoning (P450 motif recognition → heme cofactor) is derivable from the sequence using general enzymology knowledge. The elimination of Mn(2+) and cob(II)alamin is straightforward. The remaining C vs D distinction is a nomenclature subtlety rather than a biological fact requiring lookup."
  },
  "case_id": "cofactor_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q0CPG6 (Cytochrome P450 monooxygenase astC from Aspergillus terreus) explicitly states COFACTOR: Name=heme (C5, H4). The protein is annotated as a cytochrome P450 monooxygenase with experimental functional characterization (PubMed:29995859). All cytochrome P450 enzymes require heme as their prosthetic group, which is consistent with the annotation. The evidence code is ECO:0000250 (inferred by similarity from P04798, another P450), which is a transferred annotation rather than direct experimental determination for this specific protein, but the P450 superfamily heme requirement is an established biochemical fact. However, the ChEBI cross-reference (CHEBI:30413) points specifically to 'heme b,' making choice C also technically accurate."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from P04798, a characterized P450), not direct experimental determination for astC itself.",
    "The distinction between 'heme' and 'heme b' in this MCQ is artificial: CHEBI:30413 (the cross-reference in the annotation) IS heme b, so the annotation simultaneously supports both C and D.",
    "The P450 identity is well-supported by the protein name annotation and the 2018 Nature paper characterizing astC function, but the heme cofactor assignment is by superfamily analogy rather than direct spectroscopic or crystallographic evidence for this specific enzyme.",
    "Sequence match is confirmed (SHA256 match between benchmark and UniProt entries C1/H1)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The UniProt annotation uses 'heme' as the name field (supporting D) but cross-references to CHEBI:30413, which is 'heme b' specifically (supporting C). P450 enzymes use heme b (protoporphyrin IX with iron, non-covalently bound), not heme c or heme d. In precise biochemical terminology, 'heme b' is the correct specific designation, while 'heme' is the commonly used general term. Presenting both as mutually exclusive options creates genuine ambiguity, as both are correct at different levels of specificity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q0CPG6 (Cytochrome P450 monooxygenase astC from Aspergillus terreus) explicitly states COFACTOR: Name=heme (C5, H4). The protein is annotated as a cytochrome P450 monooxygenase with experimental functional characterization (PubMed:29995859). All cytochrome P450 enzymes require heme as their prosthetic group, which is consistent with the annotation. The evidence code is ECO:0000250 (inferred by similarity from P04798, another P450), which is a transferred annotation rather than direct experimental determination for this specific protein, but the P450 superfamily heme requirement is an established biochemical fact. However, the ChEBI cross-reference (CHEBI:30413) points specifically to 'heme b,' making choice C also technically accurate.",
    "evidence_ids": ["C4", "C5", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable cytochrome P450 signature motifs, including the conserved heme-ligating cysteine within an FxxGxxxCxG-like motif (visible in the 'FGHGGHSCP' region near the C-terminus) and the conserved I-helix region. Recognition of these P450 hallmarks allows a model to conclude the enzyme requires heme as its prosthetic group, eliminating Mn(2+) (A) and cob(II)alamin (B). In standard biochemical usage, the P450 prosthetic group is referred to as 'heme,' making D the conventional answer.",
    "missing_item_specific_fact": "The distinction between choices C (heme b) and D (heme) depends on the specific naming convention used in the UniProt annotation field rather than on a biological fact, since P450s use heme b specifically and 'heme' is the common shorthand. This is a nomenclature convention issue rather than a missing experimental fact.",
    "reason": "The core reasoning (P450 motif recognition → heme cofactor) is derivable from the sequence using general enzymology knowledge. The elimination of Mn(2+) and cob(II)alamin is straightforward. The remaining C vs D distinction is a nomenclature subtlety rather than a biological fact requiring lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The UniProt annotation uses 'heme' as the name field (supporting D) but cross-references to CHEBI:30413, which is 'heme b' specifically (supporting C). P450 enzymes use heme b (protoporphyrin IX with iron, non-covalently bound), not heme c or heme d. In precise biochemical terminology, 'heme b' is the correct specific designation, while 'heme' is the commonly used general term. Presenting both as mutually exclusive options creates genuine ambiguity, as both are correct at different levels of specificity."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000250 (inferred by similarity from P04798, a characterized P450), not direct experimental determination for astC itself.",
    "The distinction between 'heme' and 'heme b' in this MCQ is artificial: CHEBI:30413 (the cross-reference in the annotation) IS heme b, so the annotation simultaneously supports both C and D.",
    "The P450 identity is well-supported by the protein name annotation and the 2018 Nature paper characterizing astC function, but the heme cofactor assignment is by superfamily analogy rather than direct spectroscopic or crystallographic evidence for this specific enzyme.",
    "Sequence match is confirmed (SHA256 match between benchmark and UniProt entries C1/H1)."
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

**Accession:** `Q0CPG6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 96. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
"Q0CPG6"
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"1.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase astC"}}}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:30413"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P04798","source":"UniProtKB"}],"name":"heme"}],"commentType":"COFACTOR"}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:30:24.324806+00:00.  

```text
ID   ASTC_ASPTN              Reviewed;         538 AA.
AC   Q0CPG6;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   17-OCT-2006, sequence version 1.
DT   28-JAN-2026, entry version 96.
DE   RecName: Full=Cytochrome P450 monooxygenase astC {ECO:0000303|PubMed:29995859};
DE            EC=1.-.-.- {ECO:0000269|PubMed:29995859};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein C {ECO:0000303|PubMed:29995859};
GN   Name=astC {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04418;
OS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=341663;
```

Source SHA-256: `482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:30:24.324806+00:00.  

```text
DE   RecName: Full=Cytochrome P450 monooxygenase astC {ECO:0000303|PubMed:29995859};
DE            EC=1.-.-.- {ECO:0000269|PubMed:29995859};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein C {ECO:0000303|PubMed:29995859};
```

Source SHA-256: `482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)  
**Locator:** `lines 60-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:30:24.324806+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=heme; Xref=ChEBI:CHEBI:30413;
CC         Evidence={ECO:0000250|UniProtKB:P04798};
```

Source SHA-256: `482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
