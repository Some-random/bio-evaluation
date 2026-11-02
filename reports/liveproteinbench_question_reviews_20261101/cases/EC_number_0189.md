# EC_number_0189

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.7.8.7

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTDSNLLGLTCWLIDTRTLWPGQHIKDAASDILHLLSNDERNAVLRKIFIADARMSLASALLKRLYISRALNIPWRDVKIARKGDPTHGKPCAVLPDGSFAPIDFNVSHQAGLVSLVGWNPPPGQSQSALVGTDIVCVNERDDYRTIDQEGFDAWIDIYEDVFSEAERWDMKYNVDYITLLDGRIIQGNSLGRVDRCVRRNKDLSITLPTGETHSFNSDLLIDAKLRRFYSFFCYKEAYIKLAGEALLAPWLKELEFQNVKSPKPGTVARCSTHGTWGEKVSDVEVVLHGEKVEDVKMTLQAFEENFMLATAVQGLRDLEAPPFTKLNLENDVVAFAS

[Multiple Choices]
A. 2.7.8.41
B. 2.7.8.7
C. 3.2.1.183
D. 1.16.1.10
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

> The exact sequence match is annotated as a 4′-phosphopantetheinyl transferase with EC 2.7.8.7, and its annotated reaction is consistent with that assignment. The annotation is transferred by similarity, not direct experimental evidence for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone supplies no clear contextual clue that establishes the precise EC number; identifying this particular protein as a phosphopantetheinyl transferase requires protein-family or annotation knowledge.


**Missing item-specific fact**

> The protein-specific identification as a 4′-phosphopantetheinyl transferase and its associated EC 2.7.8.7 assignment.


**Reason**

> The choices span different enzyme activities, but the input provides no explicit functional context or experimentally established reaction. A sequence-based family inference may be possible, but the needed protein-specific assignment is not otherwise supplied.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports B; the evidence provided does not support another listed EC number.


### Important caveats

- The EC and catalytic-activity annotations are supported by similarity transfer from UniProtKB:Q4X1W0, rather than direct experimental evidence for this sequence.
- The reviewer-only database evidence was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone supplies no clear contextual clue that establishes the precise EC number; identifying this particular protein as a phosphopantetheinyl transferase requires protein-family or annotation knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as a 4′-phosphopantetheinyl transferase and its associated EC 2.7.8.7 assignment.",
    "reason": "The choices span different enzyme activities, but the input provides no explicit functional context or experimentally established reaction. A sequence-based family inference may be possible, but the needed protein-specific assignment is not otherwise supplied."
  },
  "case_id": "EC_number_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a 4′-phosphopantetheinyl transferase with EC 2.7.8.7, and its annotated reaction is consistent with that assignment. The annotation is transferred by similarity, not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The EC and catalytic-activity annotations are supported by similarity transfer from UniProtKB:Q4X1W0, rather than direct experimental evidence for this sequence.",
    "The reviewer-only database evidence was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B; the evidence provided does not support another listed EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a 4′-phosphopantetheinyl transferase with EC 2.7.8.7, and its annotated reaction is consistent with that assignment. The annotation is transferred by similarity, not direct experimental evidence for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone supplies no clear contextual clue that establishes the precise EC number; identifying this particular protein as a phosphopantetheinyl transferase requires protein-family or annotation knowledge.",
    "missing_item_specific_fact": "The protein-specific identification as a 4′-phosphopantetheinyl transferase and its associated EC 2.7.8.7 assignment.",
    "reason": "The choices span different enzyme activities, but the input provides no explicit functional context or experimentally established reaction. A sequence-based family inference may be possible, but the needed protein-specific assignment is not otherwise supplied."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports B; the evidence provided does not support another listed EC number."
  },
  "important_caveats": [
    "The EC and catalytic-activity annotations are supported by similarity transfer from UniProtKB:Q4X1W0, rather than direct experimental evidence for this sequence.",
    "The reviewer-only database evidence was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A223GB52 (Swiss-Prot, reviewed) matches the supplied 338-aa sequence exactly (SHA256 confirmed). The entry is annotated as 4'-phosphopantetheinyl transferase (PPTase) with EC 2.7.8.7. The catalytic reaction (apo-&#91;ACP&#93; + CoA → holo-&#91;ACP&#93; + adenosine 3',5'-bisphosphate + H⁺) is listed. However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity from Q4X1W0), so it is a computational transfer rather than direct experimental characterization of this specific protein. The annotation is nonetheless a reviewed Swiss-Prot assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence (~338 aa) contains motifs loosely consistent with phosphopantetheinyl transferases (e.g., 'STHGTWGEK' appearing twice, a 'GTDIVCV' region suggestive of a CoA-binding pocket, overall domain architecture resembling a type-I/AcpS-like PPTase). These features support membership in the 2.7.8.x transferase class and help eliminate C (3.2.1.183, a glycosidase hydrolase) and D (1.16.1.10, a ferroxidase oxidoreductase) as they belong to entirely different EC top-level classes. However, distinguishing EC 2.7.8.7 from EC 2.7.8.41—both transferases in the same 2.7.8.x sub-subclass—requires knowing which specific PPTase subtype or substrate specificity this sequence encodes, a fact not derivable from general sequence motifs alone.


**Missing item-specific fact**

> The specific substrate specificity and protein-family assignment that distinguishes EC 2.7.8.7 (4'-phosphopantetheinyl transferase acting on apo-ACP) from EC 2.7.8.41 (a related but distinct transferase reaction, if valid) cannot be determined from the sequence without reference to a database annotation or detailed structural comparison with characterized family members.


**Reason**

> While the sequence provides enough general information to place the protein in the PPTase/transferase family and exclude the clearly unrelated hydrolase and oxidoreductase options, the final choice between two closely numbered EC entries in the 2.7.8.x group depends on an item-specific annotation fact (which PPTase subtype this particular sequence represents) that is not encoded in generalizable biological reasoning from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (3.2.1.183, hydrolase) and D (1.16.1.10, oxidoreductase) are clearly incompatible with the PPTase-like sequence architecture and can be eliminated. The remaining A vs B distinction is narrow but, given the evidence, B (2.7.8.7) is the annotated answer. Option A (2.7.8.41) is either a non-standard or very obscure EC number; if it does not correspond to a well-characterized enzyme, it is a trivially eliminable distractor. No two options are genuinely co-defensible given the sequence features.


### Important caveats

- The EC 2.7.8.7 annotation on UniProt A0A223GB52 is by similarity (ECO:0000250 from Q4X1W0), not from direct experimental assay of this specific fungal protein.
- The reviewer identified the accession from dataset image-path metadata; this was not available to the evaluated model.
- EC 2.7.8.41 may not correspond to a well-established, actively maintained EC entry, which would make option A a fabricated or obsolete distractor rather than a genuine competing classification.
- The sequence is from Aureobasidium melanogenum (a fungus); PPTase function in fungal NRPS/ PKS systems is well-supported biologically, lending plausibility to the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~338 aa) contains motifs loosely consistent with phosphopantetheinyl transferases (e.g., 'STHGTWGEK' appearing twice, a 'GTDIVCV' region suggestive of a CoA-binding pocket, overall domain architecture resembling a type-I/AcpS-like PPTase). These features support membership in the 2.7.8.x transferase class and help eliminate C (3.2.1.183, a glycosidase hydrolase) and D (1.16.1.10, a ferroxidase oxidoreductase) as they belong to entirely different EC top-level classes. However, distinguishing EC 2.7.8.7 from EC 2.7.8.41—both transferases in the same 2.7.8.x sub-subclass—requires knowing which specific PPTase subtype or substrate specificity this sequence encodes, a fact not derivable from general sequence motifs alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity and protein-family assignment that distinguishes EC 2.7.8.7 (4'-phosphopantetheinyl transferase acting on apo-ACP) from EC 2.7.8.41 (a related but distinct transferase reaction, if valid) cannot be determined from the sequence without reference to a database annotation or detailed structural comparison with characterized family members.",
    "reason": "While the sequence provides enough general information to place the protein in the PPTase/transferase family and exclude the clearly unrelated hydrolase and oxidoreductase options, the final choice between two closely numbered EC entries in the 2.7.8.x group depends on an item-specific annotation fact (which PPTase subtype this particular sequence represents) that is not encoded in generalizable biological reasoning from the sequence alone."
  },
  "case_id": "EC_number_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A223GB52 (Swiss-Prot, reviewed) matches the supplied 338-aa sequence exactly (SHA256 confirmed). The entry is annotated as 4'-phosphopantetheinyl transferase (PPTase) with EC 2.7.8.7. The catalytic reaction (apo-[ACP] + CoA → holo-[ACP] + adenosine 3',5'-bisphosphate + H⁺) is listed. However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity from Q4X1W0), so it is a computational transfer rather than direct experimental characterization of this specific protein. The annotation is nonetheless a reviewed Swiss-Prot assignment."
  },
  "important_caveats": [
    "The EC 2.7.8.7 annotation on UniProt A0A223GB52 is by similarity (ECO:0000250 from Q4X1W0), not from direct experimental assay of this specific fungal protein.",
    "The reviewer identified the accession from dataset image-path metadata; this was not available to the evaluated model.",
    "EC 2.7.8.41 may not correspond to a well-established, actively maintained EC entry, which would make option A a fabricated or obsolete distractor rather than a genuine competing classification.",
    "The sequence is from Aureobasidium melanogenum (a fungus); PPTase function in fungal NRPS/ PKS systems is well-supported biologically, lending plausibility to the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (3.2.1.183, hydrolase) and D (1.16.1.10, oxidoreductase) are clearly incompatible with the PPTase-like sequence architecture and can be eliminated. The remaining A vs B distinction is narrow but, given the evidence, B (2.7.8.7) is the annotated answer. Option A (2.7.8.41) is either a non-standard or very obscure EC number; if it does not correspond to a well-characterized enzyme, it is a trivially eliminable distractor. No two options are genuinely co-defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A223GB52 (Swiss-Prot, reviewed) matches the supplied 338-aa sequence exactly (SHA256 confirmed). The entry is annotated as 4'-phosphopantetheinyl transferase (PPTase) with EC 2.7.8.7. The catalytic reaction (apo-[ACP] + CoA → holo-[ACP] + adenosine 3',5'-bisphosphate + H⁺) is listed. However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity from Q4X1W0), so it is a computational transfer rather than direct experimental characterization of this specific protein. The annotation is nonetheless a reviewed Swiss-Prot assignment.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence (~338 aa) contains motifs loosely consistent with phosphopantetheinyl transferases (e.g., 'STHGTWGEK' appearing twice, a 'GTDIVCV' region suggestive of a CoA-binding pocket, overall domain architecture resembling a type-I/AcpS-like PPTase). These features support membership in the 2.7.8.x transferase class and help eliminate C (3.2.1.183, a glycosidase hydrolase) and D (1.16.1.10, a ferroxidase oxidoreductase) as they belong to entirely different EC top-level classes. However, distinguishing EC 2.7.8.7 from EC 2.7.8.41—both transferases in the same 2.7.8.x sub-subclass—requires knowing which specific PPTase subtype or substrate specificity this sequence encodes, a fact not derivable from general sequence motifs alone.",
    "missing_item_specific_fact": "The specific substrate specificity and protein-family assignment that distinguishes EC 2.7.8.7 (4'-phosphopantetheinyl transferase acting on apo-ACP) from EC 2.7.8.41 (a related but distinct transferase reaction, if valid) cannot be determined from the sequence without reference to a database annotation or detailed structural comparison with characterized family members.",
    "reason": "While the sequence provides enough general information to place the protein in the PPTase/transferase family and exclude the clearly unrelated hydrolase and oxidoreductase options, the final choice between two closely numbered EC entries in the 2.7.8.x group depends on an item-specific annotation fact (which PPTase subtype this particular sequence represents) that is not encoded in generalizable biological reasoning from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (3.2.1.183, hydrolase) and D (1.16.1.10, oxidoreductase) are clearly incompatible with the PPTase-like sequence architecture and can be eliminated. The remaining A vs B distinction is narrow but, given the evidence, B (2.7.8.7) is the annotated answer. Option A (2.7.8.41) is either a non-standard or very obscure EC number; if it does not correspond to a well-characterized enzyme, it is a trivially eliminable distractor. No two options are genuinely co-defensible given the sequence features."
  },
  "important_caveats": [
    "The EC 2.7.8.7 annotation on UniProt A0A223GB52 is by similarity (ECO:0000250 from Q4X1W0), not from direct experimental assay of this specific fungal protein.",
    "The reviewer identified the accession from dataset image-path metadata; this was not available to the evaluated model.",
    "EC 2.7.8.41 may not correspond to a well-established, actively maintained EC entry, which would make option A a fabricated or obsolete distractor rather than a genuine competing classification.",
    "The sequence is from Aureobasidium melanogenum (a fungus); PPTase function in fungal NRPS/ PKS systems is well-supported biologically, lending plausibility to the annotation."
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

**Accession:** `A0A223GB52` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:40.730186+00:00.  

```json
"A0A223GB52"
```

Source SHA-256: `1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:40.730186+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1W0","source":"UniProtKB"}],"value":"Acyl-carrier-protein synthase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1W0","source":"UniProtKB"}],"value":"Phosphopantetheine:protein transferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1W0","source":"UniProtKB"}],"value":"2.7.8.7"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.2","source":"Reference"}],"value":"4'-phosphopantetheinyl transferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"Ref.2","source":"Reference"}],"value":"PPTase"}]}}
```

Source SHA-256: `1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GB52.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:40.730186+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.8.7","evidences":[{"evidenceCode":"ECO:0000250","id":"Q4X1W0","source":"UniProtKB"}],"name":"apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:12068"},{"database":"Rhea","id":"RHEA-COMP:9685"},{"database":"Rhea","id":"RHEA-COMP:9690"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:58343"},{"database":"ChEBI","id":"CHEBI:64479"}]}}
```

Source SHA-256: `1f85238d8648a62503daea44a4355d8b9818bf0320c1e3b669761c3f74e77098`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:42.924113+00:00.  

```text
ID   PPTA_AURME              Reviewed;         338 AA.
AC   A0A223GB52;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   25-OCT-2017, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=4'-phosphopantetheinyl transferase {ECO:0000303|Ref.2};
DE            Short=PPTase {ECO:0000303|Ref.2};
DE            EC=2.7.8.7 {ECO:0000250|UniProtKB:Q4X1W0};
DE   AltName: Full=Acyl-carrier-protein synthase {ECO:0000250|UniProtKB:Q4X1W0};
DE   AltName: Full=Phosphopantetheine:protein transferase {ECO:0000250|UniProtKB:Q4X1W0};
OS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.
OX   NCBI_TaxID=46634;
```

Source SHA-256: `b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:42.924113+00:00.  

```text
DE   RecName: Full=4'-phosphopantetheinyl transferase {ECO:0000303|Ref.2};
DE            Short=PPTase {ECO:0000303|Ref.2};
DE            EC=2.7.8.7 {ECO:0000250|UniProtKB:Q4X1W0};
DE   AltName: Full=Acyl-carrier-protein synthase {ECO:0000250|UniProtKB:Q4X1W0};
DE   AltName: Full=Phosphopantetheine:protein transferase {ECO:0000250|UniProtKB:Q4X1W0};
```

Source SHA-256: `b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GB52?format=txt&versions=19)  
**Locator:** `lines 65-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:42.924113+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate +
CC         H(+); Xref=Rhea:RHEA:12068, Rhea:RHEA-COMP:9685, Rhea:RHEA-COMP:9690,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:57287,
CC         ChEBI:CHEBI:58343, ChEBI:CHEBI:64479; EC=2.7.8.7;
CC         Evidence={ECO:0000250|UniProtKB:Q4X1W0};
```

Source SHA-256: `b160e3bc52b04e40113462a98f748a49deb270020947dd63f379ab16fdcd21d0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 189. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
