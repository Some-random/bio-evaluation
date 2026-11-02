# EC_number_0157

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.1.1.80

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGFAARPFHIVFSLFVLAGATQALIICPFDSIYQFGDSISDTGNYIRILPNGPAAAAANFPYGITFPGIPTGRFSDGRLIVDFIARVLGLPLLNPYLQQNASFKNGVNFAVGGATALNSSVLAAAGVQIPDIYLIPLSTQLNWFQTYLRSNCSSPTECSKKVQNSLFLIGNIGNNDVNYALPYRTIQEIEAYVPSIAKAVANATREIIRLGGRRIIVPGTFPFGCLPRNLYLFPNGDKDDLGCLRRLNDLSIYFNNLFQQALNSLRIEFPQAVIIYADYYNAFRFLLRNARALGFTSTLQSCCGIGGPYNFDLNRLCGFPGVPVCRNPREYIQWDGFHYTEAAHRHIVQYLIPDILKELKCS

[Multiple Choices]
A. 3.1.3.16
B. 3.1.1.80
C. 1.1.1.12
D. 6.3.5.1
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

> The supplied sequence exactly matches the UniProtKB entry for acetylajmalan esterase 2, which assigns EC 3.1.1.80 and annotates its catalytic reaction with ECO:0000269 evidence linked to a publication. The historical entry also matches the sequence and records the same EC assignment. This supports choice B, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme with hydrolase-like properties, but the choices include distinct catalytic classes and the sequence alone does not establish the substrate-specific reaction needed to identify EC 3.1.1.80.


**Missing item-specific fact**

> The protein's identity and experimentally characterized activity as an acetylajmalan esterase, including its substrate-specific deacetylation reaction.


**Reason**

> The exact EC assignment depends on protein-specific functional annotation or experimental characterization absent from the prompt. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports choice B; no other listed EC number is supported for this sequence.


### Important caveats

- The reviewer-only UniProt records match the supplied sequence; those records were not available to the evaluated model.
- The curated annotation cites experimental evidence, but the cited primary paper was not independently retrieved or validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme with hydrolase-like properties, but the choices include distinct catalytic classes and the sequence alone does not establish the substrate-specific reaction needed to identify EC 3.1.1.80.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and experimentally characterized activity as an acetylajmalan esterase, including its substrate-specific deacetylation reaction.",
    "reason": "The exact EC assignment depends on protein-specific functional annotation or experimental characterization absent from the prompt. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from supplied context."
  },
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProtKB entry for acetylajmalan esterase 2, which assigns EC 3.1.1.80 and annotates its catalytic reaction with ECO:0000269 evidence linked to a publication. The historical entry also matches the sequence and records the same EC assignment. This supports choice B, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence; those records were not available to the evaluated model.",
    "The curated annotation cites experimental evidence, but the cited primary paper was not independently retrieved or validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports choice B; no other listed EC number is supported for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProtKB entry for acetylajmalan esterase 2, which assigns EC 3.1.1.80 and annotates its catalytic reaction with ECO:0000269 evidence linked to a publication. The historical entry also matches the sequence and records the same EC assignment. This supports choice B, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme with hydrolase-like properties, but the choices include distinct catalytic classes and the sequence alone does not establish the substrate-specific reaction needed to identify EC 3.1.1.80.",
    "missing_item_specific_fact": "The protein's identity and experimentally characterized activity as an acetylajmalan esterase, including its substrate-specific deacetylation reaction.",
    "reason": "The exact EC assignment depends on protein-specific functional annotation or experimental characterization absent from the prompt. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports choice B; no other listed EC number is supported for this sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence; those records were not available to the evaluated model.",
    "The curated annotation cites experimental evidence, but the cited primary paper was not independently retrieved or validated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ5 (sequence SHA256 matched) annotates this protein as Acetylajmalan esterase 2 (RsAAE2) with EC 3.1.1.80, supported by experimental evidence (ECO:0000269) from PubMed:38212296 (Guo et al., Nat. Commun. 2024). The catalytic reaction 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+) is experimentally confirmed. The sequence in the question matches the canonical entry exactly (362 aa, precursor).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can argue from general sequence features that the protein lacks Rossmann-fold characteristics (eliminating C, L-lactate dehydrogenase) and lacks glutamine synthetase motifs (eliminating D). The presence of a signal peptide and cysteine-rich C-terminal region is broadly consistent with a secreted hydrolase. However, distinguishing EC 3.1.1.80 (acetylajmalan esterase) from EC 3.1.3.16 (phosphoserine phosphatase) requires knowing the specific substrate (acetylated alkaloid vs. phosphoserine), which is not inferable from sequence architecture alone. No canonical GxSxG nucleophile-elbow motif is clearly identifiable, and the overall fold does not uniquely specify carboxylesterase over phosphatase activity.


**Missing item-specific fact**

> The specific identity of this protein as Acetylajmalan esterase 2 from Rauvolfia serpentina, and the experimental demonstration that it hydrolyzes 17-O-acetylnorajmaline (EC 3.1.1.80), are item-specific facts not derivable from the sequence alone. EC 3.1.1.80 is an extremely obscure, recently characterized EC number (first annotated 2025) that cannot be predicted by general enzymology reasoning.


**Reason**

> While options C and D can be eliminated by general biological reasoning (absence of dehydrogenase or ligase structural features), the critical discrimination between A (3.1.3.16, phosphoserine phosphatase) and B (3.1.1.80, acetylajmalan esterase) depends on knowing this protein's specific substrate specificity, which is an experimental finding from a 2024 paper. No sequence motif, domain architecture, or general biological principle uniquely identifies this as an acetylajmalan esterase rather than a phosphatase without database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although both A and B are esterases (EC 3.1.x.x), the question asks for the complete 4-digit EC number. Without organism context or substrate information, a model cannot definitively choose between a phosphoserine phosphatase and a carboxylesterase acting on an acetylated alkaloid. However, the expected answer B is the only one experimentally validated for this exact sequence, so no other option is actually correct.


### Important caveats

- EC 3.1.1.80 was first annotated in UniProt on 2025-06-18 based on a 2024 Nature Communications paper; this is an extremely recent and obscure EC number unlikely to be in most training data.
- The second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) from Q3MKY2, not directly demonstrated for P0DXJ5.
- The identity of the protein (P0DXJ5) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence with no accession or organism context.
- The sequence lacks a clearly identifiable canonical GxSxG serine hydrolase motif, making even broad esterase classification from sequence difficult.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can argue from general sequence features that the protein lacks Rossmann-fold characteristics (eliminating C, L-lactate dehydrogenase) and lacks glutamine synthetase motifs (eliminating D). The presence of a signal peptide and cysteine-rich C-terminal region is broadly consistent with a secreted hydrolase. However, distinguishing EC 3.1.1.80 (acetylajmalan esterase) from EC 3.1.3.16 (phosphoserine phosphatase) requires knowing the specific substrate (acetylated alkaloid vs. phosphoserine), which is not inferable from sequence architecture alone. No canonical GxSxG nucleophile-elbow motif is clearly identifiable, and the overall fold does not uniquely specify carboxylesterase over phosphatase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as Acetylajmalan esterase 2 from Rauvolfia serpentina, and the experimental demonstration that it hydrolyzes 17-O-acetylnorajmaline (EC 3.1.1.80), are item-specific facts not derivable from the sequence alone. EC 3.1.1.80 is an extremely obscure, recently characterized EC number (first annotated 2025) that cannot be predicted by general enzymology reasoning.",
    "reason": "While options C and D can be eliminated by general biological reasoning (absence of dehydrogenase or ligase structural features), the critical discrimination between A (3.1.3.16, phosphoserine phosphatase) and B (3.1.1.80, acetylajmalan esterase) depends on knowing this protein's specific substrate specificity, which is an experimental finding from a 2024 paper. No sequence motif, domain architecture, or general biological principle uniquely identifies this as an acetylajmalan esterase rather than a phosphatase without database lookup."
  },
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ5 (sequence SHA256 matched) annotates this protein as Acetylajmalan esterase 2 (RsAAE2) with EC 3.1.1.80, supported by experimental evidence (ECO:0000269) from PubMed:38212296 (Guo et al., Nat. Commun. 2024). The catalytic reaction 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+) is experimentally confirmed. The sequence in the question matches the canonical entry exactly (362 aa, precursor)."
  },
  "important_caveats": [
    "EC 3.1.1.80 was first annotated in UniProt on 2025-06-18 based on a 2024 Nature Communications paper; this is an extremely recent and obscure EC number unlikely to be in most training data.",
    "The second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) from Q3MKY2, not directly demonstrated for P0DXJ5.",
    "The identity of the protein (P0DXJ5) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence with no accession or organism context.",
    "The sequence lacks a clearly identifiable canonical GxSxG serine hydrolase motif, making even broad esterase classification from sequence difficult."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although both A and B are esterases (EC 3.1.x.x), the question asks for the complete 4-digit EC number. Without organism context or substrate information, a model cannot definitively choose between a phosphoserine phosphatase and a carboxylesterase acting on an acetylated alkaloid. However, the expected answer B is the only one experimentally validated for this exact sequence, so no other option is actually correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ5 (sequence SHA256 matched) annotates this protein as Acetylajmalan esterase 2 (RsAAE2) with EC 3.1.1.80, supported by experimental evidence (ECO:0000269) from PubMed:38212296 (Guo et al., Nat. Commun. 2024). The catalytic reaction 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+) is experimentally confirmed. The sequence in the question matches the canonical entry exactly (362 aa, precursor).",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can argue from general sequence features that the protein lacks Rossmann-fold characteristics (eliminating C, L-lactate dehydrogenase) and lacks glutamine synthetase motifs (eliminating D). The presence of a signal peptide and cysteine-rich C-terminal region is broadly consistent with a secreted hydrolase. However, distinguishing EC 3.1.1.80 (acetylajmalan esterase) from EC 3.1.3.16 (phosphoserine phosphatase) requires knowing the specific substrate (acetylated alkaloid vs. phosphoserine), which is not inferable from sequence architecture alone. No canonical GxSxG nucleophile-elbow motif is clearly identifiable, and the overall fold does not uniquely specify carboxylesterase over phosphatase activity.",
    "missing_item_specific_fact": "The specific identity of this protein as Acetylajmalan esterase 2 from Rauvolfia serpentina, and the experimental demonstration that it hydrolyzes 17-O-acetylnorajmaline (EC 3.1.1.80), are item-specific facts not derivable from the sequence alone. EC 3.1.1.80 is an extremely obscure, recently characterized EC number (first annotated 2025) that cannot be predicted by general enzymology reasoning.",
    "reason": "While options C and D can be eliminated by general biological reasoning (absence of dehydrogenase or ligase structural features), the critical discrimination between A (3.1.3.16, phosphoserine phosphatase) and B (3.1.1.80, acetylajmalan esterase) depends on knowing this protein's specific substrate specificity, which is an experimental finding from a 2024 paper. No sequence motif, domain architecture, or general biological principle uniquely identifies this as an acetylajmalan esterase rather than a phosphatase without database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although both A and B are esterases (EC 3.1.x.x), the question asks for the complete 4-digit EC number. Without organism context or substrate information, a model cannot definitively choose between a phosphoserine phosphatase and a carboxylesterase acting on an acetylated alkaloid. However, the expected answer B is the only one experimentally validated for this exact sequence, so no other option is actually correct."
  },
  "important_caveats": [
    "EC 3.1.1.80 was first annotated in UniProt on 2025-06-18 based on a 2024 Nature Communications paper; this is an extremely recent and obscure EC number unlikely to be in most training data.",
    "The second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) from Q3MKY2, not directly demonstrated for P0DXJ5.",
    "The identity of the protein (P0DXJ5) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence with no accession or organism context.",
    "The sequence lacks a clearly identifiable canonical GxSxG serine hydrolase motif, making even broad esterase classification from sequence difficult."
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

**Accession:** `P0DXJ5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:33.413705+00:00.  

```json
"P0DXJ5"
```

Source SHA-256: `e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:33.413705+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"3.1.1.80"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Acetylajmalan esterase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsAAE2"}]}}
```

Source SHA-256: `e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:33.413705+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23797"}}],"reaction":{"ecNumber":"3.1.1.80","evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"name":"17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23796"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30089"},{"database":"ChEBI","id":"CHEBI:77618"},{"database":"ChEBI","id":"CHEBI:77725"}]}}
```

Source SHA-256: `e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:33.413705+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:35.241829+00:00.  

```text
ID   AAE2_RAUSE              Reviewed;         362 AA.
AC   P0DXJ5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};
DE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};
DE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};
DE   Flags: Precursor;
GN   Name=AAE2 {ECO:0000303|PubMed:38212296};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:35.241829+00:00.  

```text
DE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};
DE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};
DE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};
DE   Flags: Precursor;
```

Source SHA-256: `fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:35.241829+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+);
CC         Xref=Rhea:RHEA:23796, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30089, ChEBI:CHEBI:77618, ChEBI:CHEBI:77725; EC=3.1.1.80;
CC         Evidence={ECO:0000269|PubMed:38212296};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23797;
CC         Evidence={ECO:0000269|PubMed:38212296};
```

Source SHA-256: `fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 157. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
