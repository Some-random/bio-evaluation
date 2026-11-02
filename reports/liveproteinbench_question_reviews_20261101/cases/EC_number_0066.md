# EC_number_0066

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.7.4.9

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSAGKRGALIIFEGCDRSGKTTQSRLLVELLKSKGIPTLPMNFPERSSSIGQVINSYLTNSKDLPDEVIHLMFSANRWEHINQVKEKLLEGTTLVVDRYSFSGVAYSAAKGLDFDWCYAPERGLIKPDAVFYLRAPPNDLTHRGQYGKERYEKVEFQGRVAEVFNRICSKEGSYFHQFDARQSVEDLHAQIASITEELLPKVATRPLDTLS

[Multiple Choices]
A. 2.7.2.4
B. 2.4.1.391
C. 3.6.1.5
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

> The supplied sequence exactly matches the Drosophila melanogaster thymidylate kinase entry. That entry assigns EC 2.7.4.9 and reports dTMP + ATP → dTDP + ADP with experimental-evidence attribution (ECO:0000269), supporting choice D.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The short, soluble sequence and nucleotide-kinase-like P-loop motif are compatible with an ATP-dependent kinase and make the glycosyltransferase and hydrolase choices less plausible. But that general evidence does not establish the specific nucleotide substrate needed to distinguish D from another kinase option.


**Missing item-specific fact**

> The protein's thymidylate kinase identity or evidence that it phosphorylates dTMP to dTDP, rather than catalyzing the reaction represented by another kinase choice.


**Reason**

> The sequence may support a broad enzyme-family inference, but assigning the complete EC number requires substrate specificity not established by the supplied context. A protein-specific annotation or experimental characterization is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports D, and no other listed option is supported for this sequence by the supplied reviewer evidence.


### Important caveats

- The UniProt sequence match and EC assignment are reviewer-only evidence, not information supplied to the evaluated model.
- The experimental-evidence attribution is recorded in the annotation; the underlying primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short, soluble sequence and nucleotide-kinase-like P-loop motif are compatible with an ATP-dependent kinase and make the glycosyltransferase and hydrolase choices less plausible. But that general evidence does not establish the specific nucleotide substrate needed to distinguish D from another kinase option.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's thymidylate kinase identity or evidence that it phosphorylates dTMP to dTDP, rather than catalyzing the reaction represented by another kinase choice.",
    "reason": "The sequence may support a broad enzyme-family inference, but assigning the complete EC number requires substrate specificity not established by the supplied context. A protein-specific annotation or experimental characterization is needed."
  },
  "case_id": "EC_number_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Drosophila melanogaster thymidylate kinase entry. That entry assigns EC 2.7.4.9 and reports dTMP + ATP → dTDP + ADP with experimental-evidence attribution (ECO:0000269), supporting choice D."
  },
  "important_caveats": [
    "The UniProt sequence match and EC assignment are reviewer-only evidence, not information supplied to the evaluated model.",
    "The experimental-evidence attribution is recorded in the annotation; the underlying primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D, and no other listed option is supported for this sequence by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Drosophila melanogaster thymidylate kinase entry. That entry assigns EC 2.7.4.9 and reports dTMP + ATP → dTDP + ADP with experimental-evidence attribution (ECO:0000269), supporting choice D.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The short, soluble sequence and nucleotide-kinase-like P-loop motif are compatible with an ATP-dependent kinase and make the glycosyltransferase and hydrolase choices less plausible. But that general evidence does not establish the specific nucleotide substrate needed to distinguish D from another kinase option.",
    "missing_item_specific_fact": "The protein's thymidylate kinase identity or evidence that it phosphorylates dTMP to dTDP, rather than catalyzing the reaction represented by another kinase choice.",
    "reason": "The sequence may support a broad enzyme-family inference, but assigning the complete EC number requires substrate specificity not established by the supplied context. A protein-specific annotation or experimental characterization is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D, and no other listed option is supported for this sequence by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The UniProt sequence match and EC assignment are reviewer-only evidence, not information supplied to the evaluated model.",
    "The experimental-evidence attribution is recorded in the annotation; the underlying primary paper was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A1ZB29 (KTHY_DROME) is annotated as Thymidylate kinase with EC 2.7.4.9, supported by experimental evidence (ECO:0000269, PubMed:38518117, a 2024 biochemical characterization of D. melanogaster TMPK). The catalytic reaction dTMP + ATP = dTDP + ADP is confirmed experimentally. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match, 211 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical P-loop motif (GCDRSGKTT, with the GK&#91;T/S&#93; signature) indicating a nucleotide-binding phosphotransferase (EC 2.7.x). The protein length (~211 aa) is consistent with small nucleotide kinases rather than amino acid kinases (EC 2.7.2.x, typically >400 aa), eliminating option A. Options B (2.4.1.391, a glycosyltransferase) and C (3.6.1.5, a hydrolase) belong to entirely different EC top-level classes and lack P-loop/nucleotide-kinase architecture. Critically, the well-known DRY motif ('VVDRYSF') in the central region is a hallmark of thymidylate kinases (EC 2.7.4.9), distinguishing TMPK from other nucleotide kinases (adenylate, guanylate, uridylate kinases) that lack this motif. Together, P-loop + small size + DRY motif provide a concrete sequence-based argument for 2.7.4.9.


**Missing item-specific fact**

> None identified. The P-loop, DRY motif, and protein size are all directly observable in the supplied sequence and are well-established diagnostic features of thymidylate kinases in the biochemistry literature.


**Reason**

> A model with knowledge of nucleotide-kinase motifs can identify the P-loop (GKTT) to narrow to phosphotransferases, use the ~211 aa size to exclude amino acid kinases, and recognize the DRY motif as diagnostic of thymidylate kinases specifically. The two non-kinase distractors (B, C) are eliminated by EC-class reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (glycosyltransferase) and C (hydrolase) are in fundamentally different EC classes and lack any sequence features supporting them. Option A (glutamate 5-kinase) is a much larger protein acting on amino acids, inconsistent with the observed P-loop context and DRY motif. Only D (2.7.4.9) is consistent with all observable sequence features.


### Important caveats

- The EC annotation is based on experimental evidence (ECO:0000269) from a 2024 publication, not merely computational inference.
- The DRY motif is a well-known TMPK signature but is not absolutely exclusive; however, combined with P-loop and size, it is highly diagnostic in this context.
- The UniProt entry was first publicly released in April 2025; the historical archived version (entry v156, released Jan 2026) confirms the same annotation, but the exact author source snapshot is unknown.
- The reviewer-only accession A1ZB29 was inferred from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical P-loop motif (GCDRSGKTT, with the GK[T/S] signature) indicating a nucleotide-binding phosphotransferase (EC 2.7.x). The protein length (~211 aa) is consistent with small nucleotide kinases rather than amino acid kinases (EC 2.7.2.x, typically >400 aa), eliminating option A. Options B (2.4.1.391, a glycosyltransferase) and C (3.6.1.5, a hydrolase) belong to entirely different EC top-level classes and lack P-loop/nucleotide-kinase architecture. Critically, the well-known DRY motif ('VVDRYSF') in the central region is a hallmark of thymidylate kinases (EC 2.7.4.9), distinguishing TMPK from other nucleotide kinases (adenylate, guanylate, uridylate kinases) that lack this motif. Together, P-loop + small size + DRY motif provide a concrete sequence-based argument for 2.7.4.9.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None identified. The P-loop, DRY motif, and protein size are all directly observable in the supplied sequence and are well-established diagnostic features of thymidylate kinases in the biochemistry literature.",
    "reason": "A model with knowledge of nucleotide-kinase motifs can identify the P-loop (GKTT) to narrow to phosphotransferases, use the ~211 aa size to exclude amino acid kinases, and recognize the DRY motif as diagnostic of thymidylate kinases specifically. The two non-kinase distractors (B, C) are eliminated by EC-class reasoning alone."
  },
  "case_id": "EC_number_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A1ZB29 (KTHY_DROME) is annotated as Thymidylate kinase with EC 2.7.4.9, supported by experimental evidence (ECO:0000269, PubMed:38518117, a 2024 biochemical characterization of D. melanogaster TMPK). The catalytic reaction dTMP + ATP = dTDP + ADP is confirmed experimentally. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match, 211 aa)."
  },
  "important_caveats": [
    "The EC annotation is based on experimental evidence (ECO:0000269) from a 2024 publication, not merely computational inference.",
    "The DRY motif is a well-known TMPK signature but is not absolutely exclusive; however, combined with P-loop and size, it is highly diagnostic in this context.",
    "The UniProt entry was first publicly released in April 2025; the historical archived version (entry v156, released Jan 2026) confirms the same annotation, but the exact author source snapshot is unknown.",
    "The reviewer-only accession A1ZB29 was inferred from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (glycosyltransferase) and C (hydrolase) are in fundamentally different EC classes and lack any sequence features supporting them. Option A (glutamate 5-kinase) is a much larger protein acting on amino acids, inconsistent with the observed P-loop context and DRY motif. Only D (2.7.4.9) is consistent with all observable sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A1ZB29 (KTHY_DROME) is annotated as Thymidylate kinase with EC 2.7.4.9, supported by experimental evidence (ECO:0000269, PubMed:38518117, a 2024 biochemical characterization of D. melanogaster TMPK). The catalytic reaction dTMP + ATP = dTDP + ADP is confirmed experimentally. The benchmark sequence matches the UniProt sequence exactly (SHA-256 match, 211 aa).",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical P-loop motif (GCDRSGKTT, with the GK[T/S] signature) indicating a nucleotide-binding phosphotransferase (EC 2.7.x). The protein length (~211 aa) is consistent with small nucleotide kinases rather than amino acid kinases (EC 2.7.2.x, typically >400 aa), eliminating option A. Options B (2.4.1.391, a glycosyltransferase) and C (3.6.1.5, a hydrolase) belong to entirely different EC top-level classes and lack P-loop/nucleotide-kinase architecture. Critically, the well-known DRY motif ('VVDRYSF') in the central region is a hallmark of thymidylate kinases (EC 2.7.4.9), distinguishing TMPK from other nucleotide kinases (adenylate, guanylate, uridylate kinases) that lack this motif. Together, P-loop + small size + DRY motif provide a concrete sequence-based argument for 2.7.4.9.",
    "missing_item_specific_fact": "None identified. The P-loop, DRY motif, and protein size are all directly observable in the supplied sequence and are well-established diagnostic features of thymidylate kinases in the biochemistry literature.",
    "reason": "A model with knowledge of nucleotide-kinase motifs can identify the P-loop (GKTT) to narrow to phosphotransferases, use the ~211 aa size to exclude amino acid kinases, and recognize the DRY motif as diagnostic of thymidylate kinases specifically. The two non-kinase distractors (B, C) are eliminated by EC-class reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (glycosyltransferase) and C (hydrolase) are in fundamentally different EC classes and lack any sequence features supporting them. Option A (glutamate 5-kinase) is a much larger protein acting on amino acids, inconsistent with the observed P-loop context and DRY motif. Only D (2.7.4.9) is consistent with all observable sequence features."
  },
  "important_caveats": [
    "The EC annotation is based on experimental evidence (ECO:0000269) from a 2024 publication, not merely computational inference.",
    "The DRY motif is a well-known TMPK signature but is not absolutely exclusive; however, combined with P-loop and size, it is highly diagnostic in this context.",
    "The UniProt entry was first publicly released in April 2025; the historical archived version (entry v156, released Jan 2026) confirms the same annotation, but the exact author source snapshot is unknown.",
    "The reviewer-only accession A1ZB29 was inferred from dataset metadata and was not provided to the evaluated model."
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

**Accession:** `A1ZB29` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 156. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:47.024723+00:00.  

```json
"A1ZB29"
```

Source SHA-256: `8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:47.024723+00:00.  

```json
{"commonName":"Fruit fly","evidences":[{"evidenceCode":"ECO:0000312","id":"UP000000803","source":"Proteomes"}],"lineage":["Eukaryota","Metazoa","Ecdysozoa","Arthropoda","Altocrustacea","Allotriocarida","Hexapoda","Insecta","Pterygota","Neoptera","Eumetabola","Endopterygota","Aparaglossata","Panorpida","Diptera","Brachycera","Muscomorpha","Ephydroidea","Drosophilidae","Drosophila","Sophophora"],"scientificName":"Drosophila melanogaster","taxonId":7227}
```

Source SHA-256: `8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:47.024723+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0034299","source":"FlyBase"}],"value":"Deoxythymidylate kinase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38518117","source":"PubMed"}],"value":"2.7.4.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38518117","source":"PubMed"}],"value":"Thymidylate kinase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38518117","source":"PubMed"}],"value":"DmTMPK"}]}}
```

Source SHA-256: `8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:47.024723+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38518117","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13518"}}],"reaction":{"ecNumber":"2.7.4.9","evidences":[{"evidenceCode":"ECO:0000269","id":"38518117","source":"PubMed"}],"name":"dTMP + ATP = dTDP + ADP","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13517"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:58369"},{"database":"ChEBI","id":"CHEBI:63528"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:47.024723+00:00.  

```json
{"citation":{"authors":["Hu Frisk J.","Wang L."],"citationCrossReferences":[{"database":"PubMed","id":"38518117"},{"database":"DOI","id":"10.1080/15257770.2024.2332410"}],"citationType":"journal article","firstPage":"1","id":"38518117","journal":"Nucleosides Nucleotides Nucleic Acids","lastPage":"9","publicationDate":"2024","title":"Molecular characterization of Drosophila melanogaster thymidylate kinase.","volume":"43"},"referenceNumber":6,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:26:49.964915+00:00.  

```text
DE   RecName: Full=Thymidylate kinase {ECO:0000303|PubMed:38518117};
DE            Short=DmTMPK {ECO:0000303|PubMed:38518117};
DE            EC=2.7.4.9 {ECO:0000269|PubMed:38518117};
DE   AltName: Full=Deoxythymidylate kinase {ECO:0000312|FlyBase:FBgn0034299};
```

Source SHA-256: `bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)  
**Locator:** `lines 99-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:26:49.964915+00:00.  

```text
RN   [6]
RP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=38518117; DOI=10.1080/15257770.2024.2332410;
RA   Hu Frisk J., Wang L.;
RT   "Molecular characterization of Drosophila melanogaster thymidylate
RT   kinase.";
RL   Nucleosides Nucleotides Nucleic Acids 43:1-9(2024).
```

Source SHA-256: `bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)  
**Locator:** `lines 113-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:26:49.964915+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=dTMP + ATP = dTDP + ADP; Xref=Rhea:RHEA:13517,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:58369, ChEBI:CHEBI:63528,
CC         ChEBI:CHEBI:456216; EC=2.7.4.9;
CC         Evidence={ECO:0000269|PubMed:38518117};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13518;
CC         Evidence={ECO:0000269|PubMed:38518117};
```

Source SHA-256: `bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 66. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
