# pathway_0128

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPILQRISKTFIKPSSPTPESLRCYNLSSSDQMITSVYISLAFFYGSPGCESSRIRQQLDNSLSRTLVYYYPFAGRLVDNDHIDCNDQGVQFVEVRIHCPISAILKQTTSYAEDLVFPRGTSACHEDSLVVVQLNRFECGGVAIAVCISHKVADGSGAIAFINDWAATARVSSHIPSPLLVADSIFPHLDNSLPVPYNLSKNCVTRRFVFPAAEIEKLKSKAVESGLQQPTRVEVVTALLYQCALLASRSTNSGLSRPSVLIQAVNLRPFLVPPLPRNSVGNIFSINFSIIEVDSLEFPELAGRLRKAKLKFQNLSQEKLYYDSQMQELGECLKQLNTGNFDVYYCSSWCRFPVYDVDFGWGKPTWVCTVKSQIKDMIVLMDSPGDEIAAFVTLEEEKMSAFQHNELLLSFASLYSAK

[Multiple Choices]
A. tetrahydrofolate biosynthesis
B. coenzyme A biosynthesis
C. ajmaline biosynthesis. .
D. Alkaloid biosynthesis. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry naming the protein akuammiline synthase 1 and annotating its pathway as alkaloid biosynthesis, with the pathway annotation linked to a publication and ECO:0000269 evidence. This supports D; it is not merely an inferred sequence annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone may suggest a plant enzyme, but it does not meaningfully establish which specialized-metabolite pathway it serves or distinguish alkaloid biosynthesis from the other options.


**Missing item-specific fact**

> The protein-specific functional identification as akuammiline synthase 1 and its experimentally supported pathway annotation.


**Reason**

> Choosing among these pathways requires knowing the characterized function of this particular sequence. Recognizing the sequence or consulting its annotation would supply that missing fact; neither is provided in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence directly supports the broad alkaloid-biosynthesis option. Ajmaline biosynthesis is a distinct, more specific pathway and is not established for this protein by the supplied evidence.


### Important caveats

- The UniProt record and its source evidence are reviewer-only and were not available to the evaluated model.
- The historical record also matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone may suggest a plant enzyme, but it does not meaningfully establish which specialized-metabolite pathway it serves or distinguish alkaloid biosynthesis from the other options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification as akuammiline synthase 1 and its experimentally supported pathway annotation.",
    "reason": "Choosing among these pathways requires knowing the characterized function of this particular sequence. Recognizing the sequence or consulting its annotation would supply that missing fact; neither is provided in the question."
  },
  "case_id": "pathway_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry naming the protein akuammiline synthase 1 and annotating its pathway as alkaloid biosynthesis, with the pathway annotation linked to a publication and ECO:0000269 evidence. This supports D; it is not merely an inferred sequence annotation."
  },
  "important_caveats": [
    "The UniProt record and its source evidence are reviewer-only and were not available to the evaluated model.",
    "The historical record also matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence directly supports the broad alkaloid-biosynthesis option. Ajmaline biosynthesis is a distinct, more specific pathway and is not established for this protein by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry naming the protein akuammiline synthase 1 and annotating its pathway as alkaloid biosynthesis, with the pathway annotation linked to a publication and ECO:0000269 evidence. This supports D; it is not merely an inferred sequence annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone may suggest a plant enzyme, but it does not meaningfully establish which specialized-metabolite pathway it serves or distinguish alkaloid biosynthesis from the other options.",
    "missing_item_specific_fact": "The protein-specific functional identification as akuammiline synthase 1 and its experimentally supported pathway annotation.",
    "reason": "Choosing among these pathways requires knowing the characterized function of this particular sequence. Recognizing the sequence or consulting its annotation would supply that missing fact; neither is provided in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence directly supports the broad alkaloid-biosynthesis option. Ajmaline biosynthesis is a distinct, more specific pathway and is not established for this protein by the supplied evidence."
  },
  "important_caveats": [
    "The UniProt record and its source evidence are reviewer-only and were not available to the evaluated model.",
    "The historical record also matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7S5E3 (Akuammiline synthase 1, EC 2.3.1.322, from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:36349266). The protein catalyzes a cyclization step in indole alkaloid biosynthesis, as confirmed by the cited paper. Option C ('ajmaline biosynthesis') is a distractor: while ajmaline is an alkaloid from the same plant, this specific enzyme is named for akuammiline synthesis, and the UniProt pathway annotation uses the general category 'Alkaloid biosynthesis,' not a specific alkaloid name. Options A and B are unrelated primary-metabolism pathways.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model might weakly infer plant secondary metabolism (ruling out A and B) from sequence composition and length, and note that 'alkaloid biosynthesis' is the standard UniProt pathway category name versus the non-standard 'ajmaline biosynthesis.' However, the critical distinction between C (ajmaline biosynthesis) and D (alkaloid biosynthesis) cannot be resolved from the sequence: both refer to indole alkaloid pathways in the same plant. Knowing that this enzyme is akuammiline synthase (not ajmaline synthase) and that the UniProt pathway annotation uses the general category 'Alkaloid biosynthesis' requires item-specific database knowledge.


**Missing item-specific fact**

> The specific identity of the enzyme as Akuammiline synthase 1 (AsAKS1, EC 2.3.1.322) and the UniProt convention of annotating the pathway under the general heading 'Alkaloid biosynthesis' rather than a specific alkaloid name. Distinguishing C from D requires knowing this enzyme's specific substrate (akuammiline vs. ajmaline) and the database annotation convention.


**Reason**

> The sequence provides no clear motif or domain signature that uniquely identifies this as involved in 'alkaloid biosynthesis' as opposed to 'ajmaline biosynthesis' (both are indole alkaloid pathways in Alstonia). The correct answer depends on the specific UniProt pathway annotation and the enzyme's experimentally determined substrate specificity, neither of which is derivable from the sequence alone through general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Ajmaline is an indole alkaloid produced by Alstonia scholaris, and 'ajmaline biosynthesis' could be argued as a valid pathway description for an enzyme in that plant's alkaloid metabolism. The distinction from 'alkaloid biosynthesis' (D) rests on the UniProt annotation convention and the specific enzyme identity (akuammiline synthase, not ajmaline synthase), which are not derivable from the sequence. A knowledgeable model might select C if it associates Alstonia scholaris with ajmaline production.


### Important caveats

- The UniProt pathway annotation 'Alkaloid biosynthesis' is a broad category; the specific reaction is akuammiline synthesis via cyclization, not ajmaline synthesis.
- The evidence is experimental (ECO:0000269) from a 2022 paper, not merely computational inference.
- The entry was first publicly released 2025-06-18; the author's source snapshot is unknown, but the sequence has been unchanged since 2023-05-03.
- The double period in options C and D ('biosynthesis. .') appears to be a formatting artifact and does not affect answerability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model might weakly infer plant secondary metabolism (ruling out A and B) from sequence composition and length, and note that 'alkaloid biosynthesis' is the standard UniProt pathway category name versus the non-standard 'ajmaline biosynthesis.' However, the critical distinction between C (ajmaline biosynthesis) and D (alkaloid biosynthesis) cannot be resolved from the sequence: both refer to indole alkaloid pathways in the same plant. Knowing that this enzyme is akuammiline synthase (not ajmaline synthase) and that the UniProt pathway annotation uses the general category 'Alkaloid biosynthesis' requires item-specific database knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of the enzyme as Akuammiline synthase 1 (AsAKS1, EC 2.3.1.322) and the UniProt convention of annotating the pathway under the general heading 'Alkaloid biosynthesis' rather than a specific alkaloid name. Distinguishing C from D requires knowing this enzyme's specific substrate (akuammiline vs. ajmaline) and the database annotation convention.",
    "reason": "The sequence provides no clear motif or domain signature that uniquely identifies this as involved in 'alkaloid biosynthesis' as opposed to 'ajmaline biosynthesis' (both are indole alkaloid pathways in Alstonia). The correct answer depends on the specific UniProt pathway annotation and the enzyme's experimentally determined substrate specificity, neither of which is derivable from the sequence alone through general biological reasoning."
  },
  "case_id": "pathway_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S5E3 (Akuammiline synthase 1, EC 2.3.1.322, from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:36349266). The protein catalyzes a cyclization step in indole alkaloid biosynthesis, as confirmed by the cited paper. Option C ('ajmaline biosynthesis') is a distractor: while ajmaline is an alkaloid from the same plant, this specific enzyme is named for akuammiline synthesis, and the UniProt pathway annotation uses the general category 'Alkaloid biosynthesis,' not a specific alkaloid name. Options A and B are unrelated primary-metabolism pathways."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Alkaloid biosynthesis' is a broad category; the specific reaction is akuammiline synthesis via cyclization, not ajmaline synthesis.",
    "The evidence is experimental (ECO:0000269) from a 2022 paper, not merely computational inference.",
    "The entry was first publicly released 2025-06-18; the author's source snapshot is unknown, but the sequence has been unchanged since 2023-05-03.",
    "The double period in options C and D ('biosynthesis. .') appears to be a formatting artifact and does not affect answerability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Ajmaline is an indole alkaloid produced by Alstonia scholaris, and 'ajmaline biosynthesis' could be argued as a valid pathway description for an enzyme in that plant's alkaloid metabolism. The distinction from 'alkaloid biosynthesis' (D) rests on the UniProt annotation convention and the specific enzyme identity (akuammiline synthase, not ajmaline synthase), which are not derivable from the sequence. A knowledgeable model might select C if it associates Alstonia scholaris with ajmaline production."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7S5E3 (Akuammiline synthase 1, EC 2.3.1.322, from Alstonia scholaris) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:36349266). The protein catalyzes a cyclization step in indole alkaloid biosynthesis, as confirmed by the cited paper. Option C ('ajmaline biosynthesis') is a distractor: while ajmaline is an alkaloid from the same plant, this specific enzyme is named for akuammiline synthesis, and the UniProt pathway annotation uses the general category 'Alkaloid biosynthesis,' not a specific alkaloid name. Options A and B are unrelated primary-metabolism pathways.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model might weakly infer plant secondary metabolism (ruling out A and B) from sequence composition and length, and note that 'alkaloid biosynthesis' is the standard UniProt pathway category name versus the non-standard 'ajmaline biosynthesis.' However, the critical distinction between C (ajmaline biosynthesis) and D (alkaloid biosynthesis) cannot be resolved from the sequence: both refer to indole alkaloid pathways in the same plant. Knowing that this enzyme is akuammiline synthase (not ajmaline synthase) and that the UniProt pathway annotation uses the general category 'Alkaloid biosynthesis' requires item-specific database knowledge.",
    "missing_item_specific_fact": "The specific identity of the enzyme as Akuammiline synthase 1 (AsAKS1, EC 2.3.1.322) and the UniProt convention of annotating the pathway under the general heading 'Alkaloid biosynthesis' rather than a specific alkaloid name. Distinguishing C from D requires knowing this enzyme's specific substrate (akuammiline vs. ajmaline) and the database annotation convention.",
    "reason": "The sequence provides no clear motif or domain signature that uniquely identifies this as involved in 'alkaloid biosynthesis' as opposed to 'ajmaline biosynthesis' (both are indole alkaloid pathways in Alstonia). The correct answer depends on the specific UniProt pathway annotation and the enzyme's experimentally determined substrate specificity, neither of which is derivable from the sequence alone through general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Ajmaline is an indole alkaloid produced by Alstonia scholaris, and 'ajmaline biosynthesis' could be argued as a valid pathway description for an enzyme in that plant's alkaloid metabolism. The distinction from 'alkaloid biosynthesis' (D) rests on the UniProt annotation convention and the specific enzyme identity (akuammiline synthase, not ajmaline synthase), which are not derivable from the sequence. A knowledgeable model might select C if it associates Alstonia scholaris with ajmaline production."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Alkaloid biosynthesis' is a broad category; the specific reaction is akuammiline synthesis via cyclization, not ajmaline synthesis.",
    "The evidence is experimental (ECO:0000269) from a 2022 paper, not merely computational inference.",
    "The entry was first publicly released 2025-06-18; the author's source snapshot is unknown, but the sequence has been unchanged since 2023-05-03.",
    "The double period in options C and D ('biosynthesis. .') appears to be a formatting artifact and does not affect answerability."
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

**Accession:** `A0A9E7S5E3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.493793+00:00.  

```json
"A0A9E7S5E3"
```

Source SHA-256: `dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.493793+00:00.  

```json
{"commonName":"Dogbane","lineage":["Eukaryota","Viridiplantae","Streptophyta","Embryophyta","Tracheophyta","Spermatophyta","Magnoliopsida","eudicotyledons","Gunneridae","Pentapetalae","asterids","lamiids","Gentianales","Apocynaceae","Rauvolfioideae","Alstonieae","Alstonia"],"scientificName":"Alstonia scholaris","synonyms":["Echites scholaris"],"taxonId":52822}
```

Source SHA-256: `dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.493793+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"2.3.1.322"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Akuammiline synthase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsAKS1"}]}}
```

Source SHA-256: `dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.493793+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S5E3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:54.493793+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65387.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `dccc1e1f78f84ddf8a52309526ec78e3e0e822b2e5e5620c9b28bd1314fc2e3d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.651074+00:00.  

```text
ID   AKS1_ALSSC              Reviewed;         419 AA.
AC   A0A9E7S5E3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 13.
DE   RecName: Full=Akuammiline synthase 1 {ECO:0000303|PubMed:36349266};
DE            Short=AsAKS1 {ECO:0000303|PubMed:36349266};
DE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};
GN   Name=AKS1 {ECO:0000303|PubMed:36349266};
GN   Synonyms=BAHD3 {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)  
**Locator:** `lines 17-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.651074+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:URS65387.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=36349266; DOI=10.1039/d2sc03612f;
RA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;
RT   "Deciphering and reprogramming the cyclization regioselectivity in
RT   bifurcation of indole alkaloid biosynthesis.";
RL   Chem. Sci. 13:12389-12395(2022).
```

Source SHA-256: `1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S5E3?format=txt&versions=13)  
**Locator:** `lines 44-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-01T06:27:37.651074+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:36349266}.
```

Source SHA-256: `1462d014137043d064b721b692e151871424684911f566849eb4da04580f0a54`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
