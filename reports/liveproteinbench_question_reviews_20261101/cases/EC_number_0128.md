# EC_number_0128

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.3.1.193

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIPGSNPGGRIHNVIEMFENYFMDAVKGYYRHLAIIESQDPLEKINSLIDDYLKVNKKPRVIYGFHPWLDNSKDRMKELKKRFENFLDIDYSNSEKYLGQSADLVILDAMDDFRPNYIARFVDMTKGGGIAIIYSDNILEGKLYKKSLTRYGVVKDLFEARFIELAKRYRGIIFFQGNDRITFTPYSSNETHKPYKKIPKSPKVSMELHELCLSSDQNKVLEESLFIMNLGKRVLVITAARGRGKSASIGLFLSYLMSEGNFGSIIVTSPTYYSSQEIFKFIIRGLEALNVKYKVITSRDGKIMKISTRDSRVKWVSPDLAKNEEGDLIVIDEAAAMGIEFLDYIVRSWDKVILVTTIHGYEGSGKAFLKYVDKLKGKVLLKNIKMDYPIRYAKGDPIEKFLFDVFLLDAEPHEVEYNGKLKIVEVPQEELFRDDDLLKSVYGILVTAHYRNSPDDLMLLGDMAFQKVIVGYSSENPVAVCQVVYEGGLTDKQIWDISNGLKNEGHLIPHRLIKYMRALDFGKLKGWRIMRIAVSPENQGKGIGSRVIEEVIKMAKGVDWIGSSFVADYSVLRFWIKNGFLPVYLSSIKNEELNGYSVIVIKALSERTKEFVVKLSSLLKDKLLRTSHQVYYNLNPQLIVLLLRNTYSERIEGEVPDLYVDKIKAYTEGKVPYNVIAEAAHFLVTKHFLELKADLSIEAEASLVARVLQGKSWYHAGLMLGLSSREVEDNVKQSLGVLLETYT

[Multiple Choices]
A. 2.3.1.312
B. 1.14.19.80
C. 5.3.1.16
D. 2.3.1.193
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

> The exact supplied sequence matches the 743-aa UniProt entry annotated as TmcA1 with EC 2.3.1.193. The entry associates this EC with acetylation of cytidine in elongator tRNA(Met), citing both a HAMAP rule and a PubMed reference. This supports choice D, though the excerpts do not independently establish the experimental basis of the annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices alone provide no sufficiently specific, general biological argument to identify the protein's particular RNA-acetylation function and exact EC number.


**Missing item-specific fact**

> The protein-specific identity/function as TmcA1, including its RNA substrate and acetylation reaction, or equivalent reliable homology/annotation evidence.


**Reason**

> Choosing the complete EC number requires recognizing or looking up the sequence-specific enzyme function. Broad sequence-based enzyme-family inference would not by itself distinguish this precise EC assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched entry assigns the sequence to EC 2.3.1.193, and the supplied evidence does not support another listed option for this protein.


### Important caveats

- UniProt’s EC assignment cites both a computational HAMAP rule and a PubMed reference; the cited paper was not independently reviewed here.
- The reviewer-only evidence identifies an exact sequence match, but the author's precise database snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices alone provide no sufficiently specific, general biological argument to identify the protein's particular RNA-acetylation function and exact EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity/function as TmcA1, including its RNA substrate and acetylation reaction, or equivalent reliable homology/annotation evidence.",
    "reason": "Choosing the complete EC number requires recognizing or looking up the sequence-specific enzyme function. Broad sequence-based enzyme-family inference would not by itself distinguish this precise EC assignment."
  },
  "case_id": "EC_number_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the 743-aa UniProt entry annotated as TmcA1 with EC 2.3.1.193. The entry associates this EC with acetylation of cytidine in elongator tRNA(Met), citing both a HAMAP rule and a PubMed reference. This supports choice D, though the excerpts do not independently establish the experimental basis of the annotation."
  },
  "important_caveats": [
    "UniProt’s EC assignment cites both a computational HAMAP rule and a PubMed reference; the cited paper was not independently reviewed here.",
    "The reviewer-only evidence identifies an exact sequence match, but the author's precise database snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry assigns the sequence to EC 2.3.1.193, and the supplied evidence does not support another listed option for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the 743-aa UniProt entry annotated as TmcA1 with EC 2.3.1.193. The entry associates this EC with acetylation of cytidine in elongator tRNA(Met), citing both a HAMAP rule and a PubMed reference. This supports choice D, though the excerpts do not independently establish the experimental basis of the annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices alone provide no sufficiently specific, general biological argument to identify the protein's particular RNA-acetylation function and exact EC number.",
    "missing_item_specific_fact": "The protein-specific identity/function as TmcA1, including its RNA substrate and acetylation reaction, or equivalent reliable homology/annotation evidence.",
    "reason": "Choosing the complete EC number requires recognizing or looking up the sequence-specific enzyme function. Broad sequence-based enzyme-family inference would not by itself distinguish this precise EC assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry assigns the sequence to EC 2.3.1.193, and the supplied evidence does not support another listed option for this protein."
  },
  "important_caveats": [
    "UniProt’s EC assignment cites both a computational HAMAP rule and a PubMed reference; the cited paper was not independently reviewed here.",
    "The reviewer-only evidence identifies an exact sequence match, but the author's precise database snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 743-residue sequence matches UniProt Q980C5 (TMCA1_SACS2) exactly (SHA256 confirmed). UniProt annotates this entry as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA 1) with evidence from HAMAP-Rule MF_01886 and experimental data in PubMed:32555463 (Sas-Chen et al., Nature 2020). The catalytic reaction (cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP → N(4)-acetylcytidine(34) + ADP + Pi + CoA) is consistent with EC 2.3.1.193. The expected answer D is directly supported by both computational (HAMAP) and experimental (PubMed) evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could note a P-loop-like motif (GRGKS) suggesting ATP binding, consistent with EC 2.3.1.193's requirement for ATP alongside acetyl-CoA, and the large size (743 AA) is compatible with an RNA-modification enzyme. However, both option A (EC 2.3.1.312) and option D (EC 2.3.1.193) belong to the same EC 2.3.1.x sub-subclass (transferases transferring acetyl groups to nitrogenous groups). Distinguishing between them requires knowing the exact substrate: tRNA(Met) cytidine-34 for 2.3.1.193 versus whatever substrate EC 2.3.1.312 acts upon. No general sequence heuristic reliably separates these two specific four-digit EC numbers.


**Missing item-specific fact**

> The specific substrate identity of the enzyme (acetylation of cytidine at position 34 of elongator tRNA(Met)) and the corresponding four-digit EC assignment, which is a database annotation derived from experimental characterization (Sas-Chen et al., Nature 2020) and HAMAP rule matching. Without prior knowledge that this sequence is TmcA, one cannot determine from the sequence alone whether the acetyltransferase acts on tRNA-Met cytidine-34 (EC 2.3.1.193) or on another nitrogenous substrate (EC 2.3.1.312).


**Reason**

> While the broad EC class (transferase, EC 2) and sub-subclass (acetyltransferase to nitrogenous groups, EC 2.3.1) might be inferable from recognizable acetyltransferase motifs, the critical distinction between the two EC 2.3.1.x options (A vs D) depends entirely on knowing the precise substrate specificity, which is an item-specific experimental annotation not derivable from general biological reasoning about the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (EC 2.3.1.312) and D (EC 2.3.1.193) are acetyltransferases acting on nitrogenous substrates. From sequence alone, without prior knowledge of the specific substrate (tRNA-Met cytidine-34), a model recognizing acetyltransferase features could plausibly select either. The distinction requires the specific experimental annotation that this is TmcA acting on tRNA(Met) cytidine-34.


### Important caveats

- The EC annotation carries both HAMAP-Rule (computational) and PubMed:32555463 (experimental) evidence codes, so the functional assignment is well-supported.
- The sequence match to Q980C5 is exact (SHA256 confirmed) across both current and historical (entry version 120) UniProt snapshots.
- EC 2.3.1.193 was only formally established in the EC numbering system relatively recently (2020 Nature paper); older database snapshots may not have contained this entry.
- The reviewer-only evidence was absent from the evaluated model's input; the model had only the raw sequence and four EC number choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could note a P-loop-like motif (GRGKS) suggesting ATP binding, consistent with EC 2.3.1.193's requirement for ATP alongside acetyl-CoA, and the large size (743 AA) is compatible with an RNA-modification enzyme. However, both option A (EC 2.3.1.312) and option D (EC 2.3.1.193) belong to the same EC 2.3.1.x sub-subclass (transferases transferring acetyl groups to nitrogenous groups). Distinguishing between them requires knowing the exact substrate: tRNA(Met) cytidine-34 for 2.3.1.193 versus whatever substrate EC 2.3.1.312 acts upon. No general sequence heuristic reliably separates these two specific four-digit EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of the enzyme (acetylation of cytidine at position 34 of elongator tRNA(Met)) and the corresponding four-digit EC assignment, which is a database annotation derived from experimental characterization (Sas-Chen et al., Nature 2020) and HAMAP rule matching. Without prior knowledge that this sequence is TmcA, one cannot determine from the sequence alone whether the acetyltransferase acts on tRNA-Met cytidine-34 (EC 2.3.1.193) or on another nitrogenous substrate (EC 2.3.1.312).",
    "reason": "While the broad EC class (transferase, EC 2) and sub-subclass (acetyltransferase to nitrogenous groups, EC 2.3.1) might be inferable from recognizable acetyltransferase motifs, the critical distinction between the two EC 2.3.1.x options (A vs D) depends entirely on knowing the precise substrate specificity, which is an item-specific experimental annotation not derivable from general biological reasoning about the sequence."
  },
  "case_id": "EC_number_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C9",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 743-residue sequence matches UniProt Q980C5 (TMCA1_SACS2) exactly (SHA256 confirmed). UniProt annotates this entry as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA 1) with evidence from HAMAP-Rule MF_01886 and experimental data in PubMed:32555463 (Sas-Chen et al., Nature 2020). The catalytic reaction (cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP → N(4)-acetylcytidine(34) + ADP + Pi + CoA) is consistent with EC 2.3.1.193. The expected answer D is directly supported by both computational (HAMAP) and experimental (PubMed) evidence."
  },
  "important_caveats": [
    "The EC annotation carries both HAMAP-Rule (computational) and PubMed:32555463 (experimental) evidence codes, so the functional assignment is well-supported.",
    "The sequence match to Q980C5 is exact (SHA256 confirmed) across both current and historical (entry version 120) UniProt snapshots.",
    "EC 2.3.1.193 was only formally established in the EC numbering system relatively recently (2020 Nature paper); older database snapshots may not have contained this entry.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model had only the raw sequence and four EC number choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (EC 2.3.1.312) and D (EC 2.3.1.193) are acetyltransferases acting on nitrogenous substrates. From sequence alone, without prior knowledge of the specific substrate (tRNA-Met cytidine-34), a model recognizing acetyltransferase features could plausibly select either. The distinction requires the specific experimental annotation that this is TmcA acting on tRNA(Met) cytidine-34."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 743-residue sequence matches UniProt Q980C5 (TMCA1_SACS2) exactly (SHA256 confirmed). UniProt annotates this entry as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA 1) with evidence from HAMAP-Rule MF_01886 and experimental data in PubMed:32555463 (Sas-Chen et al., Nature 2020). The catalytic reaction (cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP → N(4)-acetylcytidine(34) + ADP + Pi + CoA) is consistent with EC 2.3.1.193. The expected answer D is directly supported by both computational (HAMAP) and experimental (PubMed) evidence.",
    "evidence_ids": ["C4", "C5", "C9", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could note a P-loop-like motif (GRGKS) suggesting ATP binding, consistent with EC 2.3.1.193's requirement for ATP alongside acetyl-CoA, and the large size (743 AA) is compatible with an RNA-modification enzyme. However, both option A (EC 2.3.1.312) and option D (EC 2.3.1.193) belong to the same EC 2.3.1.x sub-subclass (transferases transferring acetyl groups to nitrogenous groups). Distinguishing between them requires knowing the exact substrate: tRNA(Met) cytidine-34 for 2.3.1.193 versus whatever substrate EC 2.3.1.312 acts upon. No general sequence heuristic reliably separates these two specific four-digit EC numbers.",
    "missing_item_specific_fact": "The specific substrate identity of the enzyme (acetylation of cytidine at position 34 of elongator tRNA(Met)) and the corresponding four-digit EC assignment, which is a database annotation derived from experimental characterization (Sas-Chen et al., Nature 2020) and HAMAP rule matching. Without prior knowledge that this sequence is TmcA, one cannot determine from the sequence alone whether the acetyltransferase acts on tRNA-Met cytidine-34 (EC 2.3.1.193) or on another nitrogenous substrate (EC 2.3.1.312).",
    "reason": "While the broad EC class (transferase, EC 2) and sub-subclass (acetyltransferase to nitrogenous groups, EC 2.3.1) might be inferable from recognizable acetyltransferase motifs, the critical distinction between the two EC 2.3.1.x options (A vs D) depends entirely on knowing the precise substrate specificity, which is an item-specific experimental annotation not derivable from general biological reasoning about the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (EC 2.3.1.312) and D (EC 2.3.1.193) are acetyltransferases acting on nitrogenous substrates. From sequence alone, without prior knowledge of the specific substrate (tRNA-Met cytidine-34), a model recognizing acetyltransferase features could plausibly select either. The distinction requires the specific experimental annotation that this is TmcA acting on tRNA(Met) cytidine-34."
  },
  "important_caveats": [
    "The EC annotation carries both HAMAP-Rule (computational) and PubMed:32555463 (experimental) evidence codes, so the functional assignment is well-supported.",
    "The sequence match to Q980C5 is exact (SHA256 confirmed) across both current and historical (entry version 120) UniProt snapshots.",
    "EC 2.3.1.193 was only formally established in the EC numbering system relatively recently (2020 Nature paper); older database snapshots may not have contained this entry.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model had only the raw sequence and four EC number choices."
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

**Accession:** `Q980C5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 120. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q980C5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.389296+00:00.  

```json
"Q980C5"
```

Source SHA-256: `53795b1b01dab170f20a1b80c136e90b3970c268b7973d524bbec4ff7916a2de`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q980C5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.389296+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"value":"2.3.1.193"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"}],"value":"tRNA(Met) cytidine acetyltransferase TmcA 1"}}}
```

Source SHA-256: `53795b1b01dab170f20a1b80c136e90b3970c268b7973d524bbec4ff7916a2de`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q980C5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.389296+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.193","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01886","source":"HAMAP-Rule"},{"evidenceCode":"ECO:0000305","id":"32555463","source":"PubMed"}],"name":"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:43788"},{"database":"Rhea","id":"RHEA-COMP:10693"},{"database":"Rhea","id":"RHEA-COMP:10694"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:74900"},{"database":"ChEBI","id":"CHEBI:82748"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `53795b1b01dab170f20a1b80c136e90b3970c268b7973d524bbec4ff7916a2de`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q980C5.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.389296+00:00.  

```json
{"citation":{"authors":["Sas-Chen A.","Thomas J.M.","Matzov D.","Taoka M.","Nance K.D.","Nir R.","Bryson K.M.","Shachar R.","Liman G.L.S.","Burkhart B.W.","Gamage S.T.","Nobe Y.","Briney C.A.","Levy M.J.","Fuchs R.T.","Robb G.B.","Hartmann J.","Sharma S.","Lin Q.","Florens L.","Washburn M.P.","Isobe T.","Santangelo T.J.","Shalev-Benami M.","Meier J.L.","Schwartz S."],"citationCrossReferences":[{"database":"PubMed","id":"32555463"},{"database":"DOI","id":"10.1038/s41586-020-2418-2"}],"citationType":"journal article","firstPage":"638","id":"32555463","journal":"Nature","lastPage":"643","publicationDate":"2020","title":"Dynamic RNA acetylation revealed by quantitative cross-evolutionary mapping.","volume":"583"},"referenceComments":[{"type":"STRAIN","value":"ATCC 35092 / DSM 1617 / JCM 11322 / P2"}],"referenceNumber":2,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `53795b1b01dab170f20a1b80c136e90b3970c268b7973d524bbec4ff7916a2de`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q980C5?format=txt&versions=120)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-02T04:32:39.667309+00:00.  

```text
DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA 1 {ECO:0000255|HAMAP-Rule:MF_01886};
DE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000305|PubMed:32555463};
```

Source SHA-256: `54dca461df7edf27cb19d88d371e28a2b2ee2df6f64027617005e98dd382c089`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q980C5?format=txt&versions=120)  
**Locator:** `lines 27-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-02T04:32:39.667309+00:00.  

```text
RN   [2]
RP   FUNCTION.
RC   STRAIN=ATCC 35092 / DSM 1617 / JCM 11322 / P2;
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

Source SHA-256: `54dca461df7edf27cb19d88d371e28a2b2ee2df6f64027617005e98dd382c089`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q980C5?format=txt&versions=120)  
**Locator:** `lines 59-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-02T04:32:39.667309+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =
CC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +
CC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-
CC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;
CC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886,
CC         ECO:0000305|PubMed:32555463};
```

Source SHA-256: `54dca461df7edf27cb19d88d371e28a2b2ee2df6f64027617005e98dd382c089`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
