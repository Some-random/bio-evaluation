# EC_number_0070

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 2.3.1.193

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVKVRFDKEVREYAKGEKVKDSVLKITETALAQALEKFHRRMIVIEGDTLKKAELAGILAGASARVLSDIVGELIEKRLRDESEDKIEVLYATDALGEETFGRKRYEAFRKHFDVLAGSEVNVTAVTFKHTREILGRTYDLLILDMSYDYSPNDLGRIIETVRGGGLIFILAHPFEKWKDMWTGFHKSLVTPPYTIEDVKKRFNRRLIRKFTQHDGIYIITESGKAKKKPKKSKSQAKIRARKGVEIPEETLFPKELYEMALTRGQVEVLKAFEELVDKEGMLVLTADRGRGKSVSVGIAAIGLAVALKKRTRIVVTAPELENVQSLFRFAKRALEKLGFKPYVVEEKGLIKELYARKIGLRYYPPAEGYKKNADLYILDEAAGIHVPILHKYLNKPRVVYSSTIHGYEGAGRGFSVKFLKKAREKRSFKELHMEEPIRYAYGDPIEKWLFDVLLLDAEPVELTEEDYELIKRKEVYLEEPDLDDWFENDREDLRHFVGIYILAHYRNRPSDVALLADAPHHEARVLRLKNGKIVTAVQIAKEGGIPKNVIDKMAKGYKPRGNIIPDMMVKHHYLKEFARLKGYRIVRIATHPDAMDMGLGSKALELLEKEAREKGLDWIGSGFGASEELVRFWVRNGFAVVHLSPARNPVSGEFTAIVLKPISKKAKELIKKANDEFRIRFTEWLGDTHRELEPEIARWLFETPFGEAVDYPIHLTEIQKKRLDAFTGKVLTYDTVVDAVKPIVKLYFLDGWMKPYLDERQIKLLIYRVLQAHSWEETAKLIDRTEMFTMIEVRDIIRGLWYYYKRLLT

[Multiple Choices]
A. 2.3.1.193
B. 2.3.1.322
C. 3.2.1.8
D. 1.1.1.336
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

> The supplied 811-aa sequence exactly matches the UniProt sequence for this protein. The entry assigns EC 2.3.1.193 and describes tRNA cytidine acetyltransferase activity; the annotation cites both a computational HAMAP rule and a PubMed experimental source. The experimental annotation specifically reports cytidine acetylation in tRNA.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C7](#evidence-c7), [H1](#evidence-h1), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence characteristics might suggest a large ATP-dependent acetyltransferase, but they do not establish the specific RNA substrate and reaction needed to choose among the acetyltransferase EC options.


**Missing item-specific fact**

> The protein-specific assignment to TmcA and its experimentally characterized tRNA cytidine acetylation activity are absent from the question.


**Reason**

> The sequence and choices provide no sufficiently specific biological clue to distinguish EC 2.3.1.193 from the other candidate EC numbers without protein-specific annotation or functional evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports the keyed EC number; no other listed option is supported by the evidence.


### Important caveats

- The reviewer-only database evidence was not available to the evaluated model and supports the key, not reasoning-based answerability.
- The UniProt assignment includes computational HAMAP evidence as well as a cited experimental source; the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence characteristics might suggest a large ATP-dependent acetyltransferase, but they do not establish the specific RNA substrate and reaction needed to choose among the acetyltransferase EC options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment to TmcA and its experimentally characterized tRNA cytidine acetylation activity are absent from the question.",
    "reason": "The sequence and choices provide no sufficiently specific biological clue to distinguish EC 2.3.1.193 from the other candidate EC numbers without protein-specific annotation or functional evidence."
  },
  "case_id": "EC_number_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C7",
      "H1",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied 811-aa sequence exactly matches the UniProt sequence for this protein. The entry assigns EC 2.3.1.193 and describes tRNA cytidine acetyltransferase activity; the annotation cites both a computational HAMAP rule and a PubMed experimental source. The experimental annotation specifically reports cytidine acetylation in tRNA."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model and supports the key, not reasoning-based answerability.",
    "The UniProt assignment includes computational HAMAP evidence as well as a cited experimental source; the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed EC number; no other listed option is supported by the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 811-aa sequence exactly matches the UniProt sequence for this protein. The entry assigns EC 2.3.1.193 and describes tRNA cytidine acetyltransferase activity; the annotation cites both a computational HAMAP rule and a PubMed experimental source. The experimental annotation specifically reports cytidine acetylation in tRNA.",
    "evidence_ids": ["C1", "C4", "C7", "H1", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence characteristics might suggest a large ATP-dependent acetyltransferase, but they do not establish the specific RNA substrate and reaction needed to choose among the acetyltransferase EC options.",
    "missing_item_specific_fact": "The protein-specific assignment to TmcA and its experimentally characterized tRNA cytidine acetylation activity are absent from the question.",
    "reason": "The sequence and choices provide no sufficiently specific biological clue to distinguish EC 2.3.1.193 from the other candidate EC numbers without protein-specific annotation or functional evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed EC number; no other listed option is supported by the evidence."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the evaluated model and supports the key, not reasoning-based answerability.",
    "The UniProt assignment includes computational HAMAP evidence as well as a cited experimental source; the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5JHC6 (TMCA_THEKO) is annotated with EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA) with both computational (ECO:0000255, HAMAP-Rule MF_01886) and experimental (ECO:0000269, PubMed:32555463, Nature 2020) evidence. The catalytic reaction (acetylating cytidine(34) in elongator tRNA(Met) using acetyl-CoA and ATP) is confirmed experimentally. The benchmark sequence (811 AA, SHA256 matched) corresponds exactly to this entry.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General reasoning can eliminate EC 3.2.1.8 (glycosidase/hydrolase) and EC 1.1.1.336 (oxidoreductase) because the sequence lacks canonical glycosidase motifs or Rossmann-fold NAD(P)-binding patterns typical of oxidoreductases. The GNAT-like 'GSGFG' motif and apparent ATP-binding regions suggest an acyltransferase (EC 2.3.1.x). However, distinguishing EC 2.3.1.193 (tRNA cytidine acetyltransferase) from EC 2.3.1.322 (another acetyltransferase) requires knowing the exact substrate identity and modification position, which is not derivable from sequence motifs alone.


**Missing item-specific fact**

> The specific substrate specificity (cytidine at position 34 of elongator tRNA(Met) vs. the substrate of EC 2.3.1.322) and the precise 4-digit EC assignment for this particular protein, which requires recognizing the protein as TmcA/NAT10 and recalling its database annotation.


**Reason**

> While the EC class (2 = transferase) can be reasoned from the GNAT fold and absence of hydrolase/oxidoreductase motifs, the final distinction between two acetyltransferase EC numbers (2.3.1.193 vs 2.3.1.322) depends on item-specific substrate knowledge that cannot be inferred from general sequence features. The answer effectively requires identifying the protein as TmcA/NAT10 and recalling its specific EC annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors C (3.2.1.8, glycosidase) and D (1.1.1.336, oxidoreductase) are clearly wrong for this protein. The distinction between A and B, while difficult, is not genuinely ambiguous in the database annotation sense—only one EC number is assigned. The question is answerable with sufficient training knowledge but not through pure reasoning.


### Important caveats

- The EC 2.3.1.193 annotation carries both HAMAP computational evidence (ECO:0000255) and experimental evidence (ECO:0000269, Nature 2020), so the assignment is well-supported experimentally.
- The reviewer-only evidence was not available to the evaluated model; the model must rely on training knowledge of the TmcA/NAT10 family or sequence-based inference.
- EC 2.3.1.322 is a relatively obscure transferase; its exact identity and substrate may not be widely represented in training data, making the A-vs-B distinction heavily dependent on memorization of the specific annotation rather than comparative reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General reasoning can eliminate EC 3.2.1.8 (glycosidase/hydrolase) and EC 1.1.1.336 (oxidoreductase) because the sequence lacks canonical glycosidase motifs or Rossmann-fold NAD(P)-binding patterns typical of oxidoreductases. The GNAT-like 'GSGFG' motif and apparent ATP-binding regions suggest an acyltransferase (EC 2.3.1.x). However, distinguishing EC 2.3.1.193 (tRNA cytidine acetyltransferase) from EC 2.3.1.322 (another acetyltransferase) requires knowing the exact substrate identity and modification position, which is not derivable from sequence motifs alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate specificity (cytidine at position 34 of elongator tRNA(Met) vs. the substrate of EC 2.3.1.322) and the precise 4-digit EC assignment for this particular protein, which requires recognizing the protein as TmcA/NAT10 and recalling its database annotation.",
    "reason": "While the EC class (2 = transferase) can be reasoned from the GNAT fold and absence of hydrolase/oxidoreductase motifs, the final distinction between two acetyltransferase EC numbers (2.3.1.193 vs 2.3.1.322) depends on item-specific substrate knowledge that cannot be inferred from general sequence features. The answer effectively requires identifying the protein as TmcA/NAT10 and recalling its specific EC annotation."
  },
  "case_id": "EC_number_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C9",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5JHC6 (TMCA_THEKO) is annotated with EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA) with both computational (ECO:0000255, HAMAP-Rule MF_01886) and experimental (ECO:0000269, PubMed:32555463, Nature 2020) evidence. The catalytic reaction (acetylating cytidine(34) in elongator tRNA(Met) using acetyl-CoA and ATP) is confirmed experimentally. The benchmark sequence (811 AA, SHA256 matched) corresponds exactly to this entry."
  },
  "important_caveats": [
    "The EC 2.3.1.193 annotation carries both HAMAP computational evidence (ECO:0000255) and experimental evidence (ECO:0000269, Nature 2020), so the assignment is well-supported experimentally.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely on training knowledge of the TmcA/NAT10 family or sequence-based inference.",
    "EC 2.3.1.322 is a relatively obscure transferase; its exact identity and substrate may not be widely represented in training data, making the A-vs-B distinction heavily dependent on memorization of the specific annotation rather than comparative reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors C (3.2.1.8, glycosidase) and D (1.1.1.336, oxidoreductase) are clearly wrong for this protein. The distinction between A and B, while difficult, is not genuinely ambiguous in the database annotation sense—only one EC number is assigned. The question is answerable with sufficient training knowledge but not through pure reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5JHC6 (TMCA_THEKO) is annotated with EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA) with both computational (ECO:0000255, HAMAP-Rule MF_01886) and experimental (ECO:0000269, PubMed:32555463, Nature 2020) evidence. The catalytic reaction (acetylating cytidine(34) in elongator tRNA(Met) using acetyl-CoA and ATP) is confirmed experimentally. The benchmark sequence (811 AA, SHA256 matched) corresponds exactly to this entry.",
    "evidence_ids": ["C1", "C4", "C5", "C9", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General reasoning can eliminate EC 3.2.1.8 (glycosidase/hydrolase) and EC 1.1.1.336 (oxidoreductase) because the sequence lacks canonical glycosidase motifs or Rossmann-fold NAD(P)-binding patterns typical of oxidoreductases. The GNAT-like 'GSGFG' motif and apparent ATP-binding regions suggest an acyltransferase (EC 2.3.1.x). However, distinguishing EC 2.3.1.193 (tRNA cytidine acetyltransferase) from EC 2.3.1.322 (another acetyltransferase) requires knowing the exact substrate identity and modification position, which is not derivable from sequence motifs alone.",
    "missing_item_specific_fact": "The specific substrate specificity (cytidine at position 34 of elongator tRNA(Met) vs. the substrate of EC 2.3.1.322) and the precise 4-digit EC assignment for this particular protein, which requires recognizing the protein as TmcA/NAT10 and recalling its database annotation.",
    "reason": "While the EC class (2 = transferase) can be reasoned from the GNAT fold and absence of hydrolase/oxidoreductase motifs, the final distinction between two acetyltransferase EC numbers (2.3.1.193 vs 2.3.1.322) depends on item-specific substrate knowledge that cannot be inferred from general sequence features. The answer effectively requires identifying the protein as TmcA/NAT10 and recalling its specific EC annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors C (3.2.1.8, glycosidase) and D (1.1.1.336, oxidoreductase) are clearly wrong for this protein. The distinction between A and B, while difficult, is not genuinely ambiguous in the database annotation sense—only one EC number is assigned. The question is answerable with sufficient training knowledge but not through pure reasoning."
  },
  "important_caveats": [
    "The EC 2.3.1.193 annotation carries both HAMAP computational evidence (ECO:0000255) and experimental evidence (ECO:0000269, Nature 2020), so the assignment is well-supported experimentally.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely on training knowledge of the TmcA/NAT10 family or sequence-based inference.",
    "EC 2.3.1.322 is a relatively obscure transferase; its exact identity and substrate may not be widely represented in training data, making the A-vs-B distinction heavily dependent on memorization of the specific annotation rather than comparative reasoning."
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

**Accession:** `Q5JHC6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 116. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:20.774043+00:00.  

```json
"Q5JHC6"
```

Source SHA-256: `1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:20.774043+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32555463","source":"PubMed"}],"value":"TkNAT10"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000269","id":"32555463","source":"PubMed"}],"value":"2.3.1.193"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"value":"tRNA(Met) cytidine acetyltransferase TmcA"}}}
```

Source SHA-256: `1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:20.774043+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.193","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000269","id":"32555463","source":"PubMed"}],"name":"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43788"},{"database":"Rhea","id":"RHEA-COMP:10693"},{"database":"Rhea","id":"RHEA-COMP:10694"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:20.774043+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"32555463","source":"PubMed"}],"name":"a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:53876"},{"database":"Rhea","id":"RHEA-COMP:13670"},{"database":"Rhea","id":"RHEA-COMP:13671"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JHC6.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:20.774043+00:00.  

```json
{"citation":{"authors":["Sas-Chen A.","Thomas J.M.","Matzov D.","Taoka M.","Nance K.D.","Nir R.","Bryson K.M.","Shachar R.","Liman G.L.S.","Burkhart B.W.","Gamage S.T.","Nobe Y.","Briney C.A.","Levy M.J.","Fuchs R.T.","Robb G.B.","Hartmann J.","Sharma S.","Lin Q.","Florens L.","Washburn M.P.","Isobe T.","Santangelo T.J.","Shalev-Benami M.","Meier J.L.","Schwartz S."],"citationCrossReferences":[{"database":"PubMed","id":"32555463"},{"database":"DOI","id":"10.1038/s41586-020-2418-2"}],"citationType":"journal article","firstPage":"638","id":"32555463","journal":"Nature","lastPage":"643","publicationDate":"2020","title":"Dynamic RNA acetylation revealed by quantitative cross-evolutionary mapping.","volume":"583"},"referenceComments":[{"type":"STRAIN","value":"ATCC BAA-918 / TS559"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `1ea4a460cde5d00a398177cf74e38b13ad1b2d74b5375e6ba462564c31deb157`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:31:24.956546+00:00.  

```text
ID   TMCA_THEKO              Reviewed;         811 AA.
AC   Q5JHC6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-FEB-2005, sequence version 1.
DT   28-JAN-2026, entry version 116.
DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};
DE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000269|PubMed:32555463};
DE   AltName: Full=TkNAT10 {ECO:0000303|PubMed:32555463};
GN   Name=tmcA {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000303|PubMed:30605516};
GN   Synonyms=Nat10 {ECO:0000303|PubMed:32555463};
GN   OrderedLocusNames=TK0754 {ECO:0000312|EMBL:BAD84943.1};
OS   Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)
OS   (Pyrococcus kodakaraensis (strain KOD1)).
OC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;
OC   Thermococcaceae; Thermococcus.
OX   NCBI_TaxID=69014;
```

Source SHA-256: `c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:31:24.956546+00:00.  

```text
DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA {ECO:0000255|HAMAP-Rule:MF_01886};
DE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000269|PubMed:32555463};
DE   AltName: Full=TkNAT10 {ECO:0000303|PubMed:32555463};
```

Source SHA-256: `c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)  
**Locator:** `lines 34-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:31:24.956546+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, INDUCTION, AND DISRUPTION PHENOTYPE.
RC   STRAIN=ATCC BAA-918 / TS559;
RX   PubMed=32555463; DOI=10.1038/s41586-020-2418-2;
RA   Sas-Chen A., Thomas J.M., Matzov D., Taoka M., Nance K.D., Nir R.,
RA   Bryson K.M., Shachar R., Liman G.L.S., Burkhart B.W., Gamage S.T., Nobe Y.,
RA   Briney C.A., Levy M.J., Fuchs R.T., Robb G.B., Hartmann J., Sharma S.,
RA   Lin Q., Florens L., Washburn M.P., Isobe T., Santangelo T.J.,
RA   Shalev-Benami M., Meier J.L., Schwartz S.;
RT   "Dynamic RNA acetylation revealed by quantitative cross-evolutionary
RT   mapping.";
RL   Nature 583:638-643(2020).
```

Source SHA-256: `c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)  
**Locator:** `lines 56-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:31:24.956546+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =
CC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +
CC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-
CC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886,
CC         ECO:0000269|PubMed:32555463};
```

Source SHA-256: `c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JHC6?format=txt&versions=116)  
**Locator:** `lines 73-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:31:24.956546+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-
CC         acetylcytidine in tRNA + ADP + phosphate + CoA + H(+);
CC         Xref=Rhea:RHEA:53876, Rhea:RHEA-COMP:13670, Rhea:RHEA-COMP:13671,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000269|PubMed:32555463};
```

Source SHA-256: `c05dd90ac793c3b0b7a7e2c5ead01e559eb6146b501bb39db646e351ccdaa9a7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
