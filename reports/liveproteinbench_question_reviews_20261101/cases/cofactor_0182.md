# cofactor_0182

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSEVERALDVLLQEAEELCIGSSVVELDRIPTALEFCREFYSKNQPVVIRKALNWPAIGKWTPKYLIEALGDRSVDVAITPNGYADGLATQNGQEYFVLPLETKMKLSEVVRRLDDPTGAVHYIQKQNSNLSVDLPELAADLRVSDLDFAQQSFNKPPDAVNFWLGDERAVTSMHKDPYENVYCVISGHKDFVLIPPHQLSCVPRGIYPTGVYKTSDSGQFYIEPLRDEEGSDQFTEWVSVDPLSPDLAKYPEYARAKPLKVRVHAGDILYLPNYWFHHVSQSHKCIAVNFWYDLDYDSRYCYYRMLEQMTSARSG

[Multiple Choices]
A. heme
B. Fe(2+)
C. [2Fe-2S] cluster
D. Mn(2+)
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

> The exact sequence matches the Drosophila JMJD7 UniProt record, which annotates Fe(2+) as a cofactor with experimental evidence (ECO:0000269; PubMed 35410347). The cited crystal structures include Mn(2+), but that alone does not establish Mn(2+) as the cofactor required for catalytic activity.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Histidine/aspartate-rich sequence regions may suggest a metal-binding enzyme, but they do not, by themselves, distinguish Fe(2+) from Mn(2+) or establish which metal supports this protein's catalytic activity.


**Missing item-specific fact**

> The JMJD7 identity and its experimentally supported Fe(2+) cofactor annotation are not supplied with the sequence.


**Reason**

> Selecting Fe(2+) over the other metal choices depends on identifying the protein or obtaining protein-specific functional evidence. General metal-binding sequence patterns do not resolve the choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reported Mn(2+) in crystal complexes is a caveat, but the question asks for the cofactor required for catalytic activity, and the matched entry supports Fe(2+).


### Important caveats

- The cofactor annotation is experimentally evidence-tagged in UniProt, but the cited primary study was not independently reviewed here.
- Mn(2+) occurs in the cited crystallographic complexes; its presence there should not be conflated with the physiological catalytic cofactor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Histidine/aspartate-rich sequence regions may suggest a metal-binding enzyme, but they do not, by themselves, distinguish Fe(2+) from Mn(2+) or establish which metal supports this protein's catalytic activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The JMJD7 identity and its experimentally supported Fe(2+) cofactor annotation are not supplied with the sequence.",
    "reason": "Selecting Fe(2+) over the other metal choices depends on identifying the protein or obtaining protein-specific functional evidence. General metal-binding sequence patterns do not resolve the choice."
  },
  "case_id": "cofactor_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila JMJD7 UniProt record, which annotates Fe(2+) as a cofactor with experimental evidence (ECO:0000269; PubMed 35410347). The cited crystal structures include Mn(2+), but that alone does not establish Mn(2+) as the cofactor required for catalytic activity."
  },
  "important_caveats": [
    "The cofactor annotation is experimentally evidence-tagged in UniProt, but the cited primary study was not independently reviewed here.",
    "Mn(2+) occurs in the cited crystallographic complexes; its presence there should not be conflated with the physiological catalytic cofactor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reported Mn(2+) in crystal complexes is a caveat, but the question asks for the cofactor required for catalytic activity, and the matched entry supports Fe(2+)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila JMJD7 UniProt record, which annotates Fe(2+) as a cofactor with experimental evidence (ECO:0000269; PubMed 35410347). The cited crystal structures include Mn(2+), but that alone does not establish Mn(2+) as the cofactor required for catalytic activity.",
    "evidence_ids": ["C1", "C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Histidine/aspartate-rich sequence regions may suggest a metal-binding enzyme, but they do not, by themselves, distinguish Fe(2+) from Mn(2+) or establish which metal supports this protein's catalytic activity.",
    "missing_item_specific_fact": "The JMJD7 identity and its experimentally supported Fe(2+) cofactor annotation are not supplied with the sequence.",
    "reason": "Selecting Fe(2+) over the other metal choices depends on identifying the protein or obtaining protein-specific functional evidence. General metal-binding sequence patterns do not resolve the choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reported Mn(2+) in crystal complexes is a caveat, but the question asks for the cofactor required for catalytic activity, and the matched entry supports Fe(2+)."
  },
  "important_caveats": [
    "The cofactor annotation is experimentally evidence-tagged in UniProt, but the cited primary study was not independently reviewed here.",
    "Mn(2+) occurs in the cited crystallographic complexes; its presence there should not be conflated with the physiological catalytic cofactor."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9VU77 (JMJD7_DROME) explicitly annotates the cofactor as Fe(2+) (ChEBI:29033) with experimental evidence code ECO:0000269 from PubMed:35410347 (C5, H4). The protein is a JmjC-domain-containing (3S)-lysyl hydroxylase (EC 1.14.11.63), a 2-oxoglutarate-dependent dioxygenase, a class universally dependent on Fe(II). Although the crystallographic reference (C6/H3) lists Mn(2+) in the co-crystallized complexes, this is a well-known crystallographic surrogate for Fe(2+) in Fe(II)/2OG dioxygenase studies; the functional cofactor annotation remains Fe(2+).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains HxD and H…H motifs (e.g., 'GHKDF', 'HHVSQSHK') characteristic of the JmjC-domain Fe(II) coordination site. JmjC-domain proteins constitute a well-established superfamily of Fe(II)/2-oxoglutarate-dependent dioxygenases; recognizing this fold and its canonical metal requirement is general biochemistry. The EC 1.14.11.x class (2-oxoglutarate-dependent dioxygenase) inherently requires Fe(II). Distinguishing Fe(2+) from Mn(2+) is supported by the field-standard knowledge that Mn(2+) is a common crystallographic substitute (non-oxidizable) while Fe(2+) is the catalytically required metal in 2OG-dependent oxygenases.


**Missing item-specific fact**

> None critical. The JmjC→Fe(II) association is textbook-level knowledge. A model would not need to know the specific PubMed paper or PDB entries; the domain family assignment and its cofactor requirement are general.


**Reason**

> A model with standard biochemistry training can identify JmjC-like motifs in the sequence and invoke the well-known Fe(II)/2OG dioxygenase biochemistry to select Fe(2+). The Mn(2+) option is a plausible distractor from crystallography but is not the catalytic cofactor for this enzyme class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the crystal structures contain Mn(2+) (C6/H3), this is a recognized crystallographic surrogate and not the functional cofactor. The COFACTOR annotation and the enzyme class (EC 1.14.11.63, 2OG-dependent dioxygenase) unambiguously designate Fe(2+) as the required cofactor. Heme and &#91;2Fe-2S&#93; are unrelated to JmjC-domain biochemistry.


### Important caveats

- The crystallographic reference explicitly lists Mn(2+) in the deposited structures (7YXG–7YXL), which could mislead a model that conflates crystallographic metal substitution with the catalytic cofactor.
- The ECO:0000269 evidence code indicates experimental determination of Fe(2+) requirement, likely from activity assays in the 2022 Sci. Rep. paper, distinguishing it from the crystallographic Mn(2+) substitution.
- The protein was only integrated into Swiss-Prot on 2025-04-09 (C2); before that date it was TrEMBL-only, limiting the annotation available at earlier benchmark construction times.
- Recognition of the JmjC fold from a raw 316-aa sequence without domain annotation is non-trivial; the reasoning is supported but requires the model to connect specific sequence motifs to a known domain family.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains HxD and H…H motifs (e.g., 'GHKDF', 'HHVSQSHK') characteristic of the JmjC-domain Fe(II) coordination site. JmjC-domain proteins constitute a well-established superfamily of Fe(II)/2-oxoglutarate-dependent dioxygenases; recognizing this fold and its canonical metal requirement is general biochemistry. The EC 1.14.11.x class (2-oxoglutarate-dependent dioxygenase) inherently requires Fe(II). Distinguishing Fe(2+) from Mn(2+) is supported by the field-standard knowledge that Mn(2+) is a common crystallographic substitute (non-oxidizable) while Fe(2+) is the catalytically required metal in 2OG-dependent oxygenases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The JmjC→Fe(II) association is textbook-level knowledge. A model would not need to know the specific PubMed paper or PDB entries; the domain family assignment and its cofactor requirement are general.",
    "reason": "A model with standard biochemistry training can identify JmjC-like motifs in the sequence and invoke the well-known Fe(II)/2OG dioxygenase biochemistry to select Fe(2+). The Mn(2+) option is a plausible distractor from crystallography but is not the catalytic cofactor for this enzyme class."
  },
  "case_id": "cofactor_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9VU77 (JMJD7_DROME) explicitly annotates the cofactor as Fe(2+) (ChEBI:29033) with experimental evidence code ECO:0000269 from PubMed:35410347 (C5, H4). The protein is a JmjC-domain-containing (3S)-lysyl hydroxylase (EC 1.14.11.63), a 2-oxoglutarate-dependent dioxygenase, a class universally dependent on Fe(II). Although the crystallographic reference (C6/H3) lists Mn(2+) in the co-crystallized complexes, this is a well-known crystallographic surrogate for Fe(2+) in Fe(II)/2OG dioxygenase studies; the functional cofactor annotation remains Fe(2+)."
  },
  "important_caveats": [
    "The crystallographic reference explicitly lists Mn(2+) in the deposited structures (7YXG–7YXL), which could mislead a model that conflates crystallographic metal substitution with the catalytic cofactor.",
    "The ECO:0000269 evidence code indicates experimental determination of Fe(2+) requirement, likely from activity assays in the 2022 Sci. Rep. paper, distinguishing it from the crystallographic Mn(2+) substitution.",
    "The protein was only integrated into Swiss-Prot on 2025-04-09 (C2); before that date it was TrEMBL-only, limiting the annotation available at earlier benchmark construction times.",
    "Recognition of the JmjC fold from a raw 316-aa sequence without domain annotation is non-trivial; the reasoning is supported but requires the model to connect specific sequence motifs to a known domain family."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the crystal structures contain Mn(2+) (C6/H3), this is a recognized crystallographic surrogate and not the functional cofactor. The COFACTOR annotation and the enzyme class (EC 1.14.11.63, 2OG-dependent dioxygenase) unambiguously designate Fe(2+) as the required cofactor. Heme and [2Fe-2S] are unrelated to JmjC-domain biochemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9VU77 (JMJD7_DROME) explicitly annotates the cofactor as Fe(2+) (ChEBI:29033) with experimental evidence code ECO:0000269 from PubMed:35410347 (C5, H4). The protein is a JmjC-domain-containing (3S)-lysyl hydroxylase (EC 1.14.11.63), a 2-oxoglutarate-dependent dioxygenase, a class universally dependent on Fe(II). Although the crystallographic reference (C6/H3) lists Mn(2+) in the co-crystallized complexes, this is a well-known crystallographic surrogate for Fe(2+) in Fe(II)/2OG dioxygenase studies; the functional cofactor annotation remains Fe(2+).",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains HxD and H…H motifs (e.g., 'GHKDF', 'HHVSQSHK') characteristic of the JmjC-domain Fe(II) coordination site. JmjC-domain proteins constitute a well-established superfamily of Fe(II)/2-oxoglutarate-dependent dioxygenases; recognizing this fold and its canonical metal requirement is general biochemistry. The EC 1.14.11.x class (2-oxoglutarate-dependent dioxygenase) inherently requires Fe(II). Distinguishing Fe(2+) from Mn(2+) is supported by the field-standard knowledge that Mn(2+) is a common crystallographic substitute (non-oxidizable) while Fe(2+) is the catalytically required metal in 2OG-dependent oxygenases.",
    "missing_item_specific_fact": "None critical. The JmjC→Fe(II) association is textbook-level knowledge. A model would not need to know the specific PubMed paper or PDB entries; the domain family assignment and its cofactor requirement are general.",
    "reason": "A model with standard biochemistry training can identify JmjC-like motifs in the sequence and invoke the well-known Fe(II)/2OG dioxygenase biochemistry to select Fe(2+). The Mn(2+) option is a plausible distractor from crystallography but is not the catalytic cofactor for this enzyme class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the crystal structures contain Mn(2+) (C6/H3), this is a recognized crystallographic surrogate and not the functional cofactor. The COFACTOR annotation and the enzyme class (EC 1.14.11.63, 2OG-dependent dioxygenase) unambiguously designate Fe(2+) as the required cofactor. Heme and [2Fe-2S] are unrelated to JmjC-domain biochemistry."
  },
  "important_caveats": [
    "The crystallographic reference explicitly lists Mn(2+) in the deposited structures (7YXG–7YXL), which could mislead a model that conflates crystallographic metal substitution with the catalytic cofactor.",
    "The ECO:0000269 evidence code indicates experimental determination of Fe(2+) requirement, likely from activity assays in the 2022 Sci. Rep. paper, distinguishing it from the crystallographic Mn(2+) substitution.",
    "The protein was only integrated into Swiss-Prot on 2025-04-09 (C2); before that date it was TrEMBL-only, limiting the annotation available at earlier benchmark construction times.",
    "Recognition of the JmjC fold from a raw 316-aa sequence without domain annotation is non-trivial; the reasoning is supported but requires the model to connect specific sequence motifs to a known domain family."
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

**Accession:** `Q9VU77` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 176. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:39.402140+00:00.  

```json
"Q9VU77"
```

Source SHA-256: `3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:39.402140+00:00.  

```json
{"entryVersion":178,"firstPublicDate":"2025-04-09","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2000-05-01","sequenceVersion":1}
```

Source SHA-256: `3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:39.402140+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29033"},"evidences":[{"evidenceCode":"ECO:0000269","id":"35410347","source":"PubMed"}],"name":"Fe(2+)"}],"commentType":"COFACTOR"}
```

Source SHA-256: `3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:39.402140+00:00.  

```json
{"citation":{"authors":["Chowdhury R.","Abboud M.I.","Wiley J.","Tumber A.","Markolovic S.","Schofield C.J."],"citationCrossReferences":[{"database":"PubMed","id":"35410347"},{"database":"DOI","id":"10.1038/s41598-022-10028-y"}],"citationType":"journal article","firstPage":"6065","id":"35410347","journal":"Sci. Rep.","lastPage":"6065","publicationDate":"2022","title":"Conservation of the unusual dimeric JmjC fold of JMJD7 from Drosophila melanogaster to humans.","volume":"12"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7YXG","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXH","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXI","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXJ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXK","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YXL","source":"PDB"}],"referenceNumber":7,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEX WITH 2-OXOGLUTARATE; MN(2+); SUCCINATE; N-OXALYLGLYCINE; N-OXALYL-D-ALANINE; N-OXALYL-D-PHENYLALANINE AND LUTIDINIC ACID","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBUNIT","DISULFIDE BOND","OXIDATION AT CYS-19"]}
```

Source SHA-256: `3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)  
**Locator:** `lines 104-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 176 / 1.  
**Retrieved:** 2026-11-02T04:33:41.782034+00:00.  

```text
RN   [7] {ECO:0007744|PDB:7YXG, ECO:0007744|PDB:7YXH, ECO:0007744|PDB:7YXI, ECO:0007744|PDB:7YXJ, ECO:0007744|PDB:7YXK, ECO:0007744|PDB:7YXL}
RP   X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEX WITH 2-OXOGLUTARATE;
RP   MN(2+); SUCCINATE; N-OXALYLGLYCINE; N-OXALYL-D-ALANINE;
RP   N-OXALYL-D-PHENYLALANINE AND LUTIDINIC ACID, FUNCTION, CATALYTIC ACTIVITY,
RP   COFACTOR, SUBUNIT, DISULFIDE BOND, AND OXIDATION AT CYS-19.
RX   PubMed=35410347; DOI=10.1038/s41598-022-10028-y;
RA   Chowdhury R., Abboud M.I., Wiley J., Tumber A., Markolovic S.,
RA   Schofield C.J.;
RT   "Conservation of the unusual dimeric JmjC fold of JMJD7 from Drosophila
RT   melanogaster to humans.";
RL   Sci. Rep. 12:6065-6065(2022).
```

Source SHA-256: `a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)  
**Locator:** `lines 133-135`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 176 / 1.  
**Retrieved:** 2026-11-02T04:33:41.782034+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;
CC         Evidence={ECO:0000269|PubMed:35410347};
```

Source SHA-256: `a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 182. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
