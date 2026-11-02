# EC_number_0149

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.3.1.312

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIETPYLLFLGDAPDMLAAKVAIGIRDWRPDHAVGQISLPGCGANLGLTEMTLEEAKAAGAKTLVIGVANRGGKISQEWKKVLVQALEEGFDLASGLHNLLRDEPDLAAVAEATGRTLHDVRVPSVQYPIADGVKRRGKRCLAVGTDCSVGKMYTALAMDAEMQARGIKSTFRATGQTGILITGDGVPLDAVIADFMAGSIEYLTPDNDDDHWDLIEGQGSLFHVSYSGVTMALVHGGQPDALILCHEPTRTHMRGLPDYDVPSLEELRDVALPLAQRANKDCKIVGISVNTQHLGEEEAVAYLKEVEGRMGLPAVDPYRHGAGRLVDALAAV

[Multiple Choices]
A. 2.3.1.322
B. 2.7.7.43
C. 2.3.1.312
D. 5.4.99.14
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

> The supplied sequence exactly matches the UniProt entry annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312. The annotation links the catalytic activity to PubMed evidence code ECO:0000269; the cited reaction is D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+). This supports choice C, although the primary paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include different enzyme reaction classifications, but the sequence and options alone provide no sufficiently specific biological argument for identifying this protein's exact substrate and reaction. Broad sequence-based functional inference would not establish the complete EC number.


**Missing item-specific fact**

> The protein-specific functional assignment identifying the sequence as D-glutamate N-acetyltransferase, and its catalyzed reaction, is needed to select EC 2.3.1.312.


**Reason**

> The reviewer evidence supports the key, but that annotation and its cited experimental evidence were not provided to the evaluated model. Recognizing or retrieving the exact protein entry would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched annotation specifies EC 2.3.1.312; no supplied evidence supports another listed choice.


### Important caveats

- The UniProt evidence links the functional assignment to a cited publication, but that publication was not independently assessed.
- The exact source snapshot used by the benchmark author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include different enzyme reaction classifications, but the sequence and options alone provide no sufficiently specific biological argument for identifying this protein's exact substrate and reaction. Broad sequence-based functional inference would not establish the complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment identifying the sequence as D-glutamate N-acetyltransferase, and its catalyzed reaction, is needed to select EC 2.3.1.312.",
    "reason": "The reviewer evidence supports the key, but that annotation and its cited experimental evidence were not provided to the evaluated model. Recognizing or retrieving the exact protein entry would be lookup, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312. The annotation links the catalytic activity to PubMed evidence code ECO:0000269; the cited reaction is D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+). This supports choice C, although the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt evidence links the functional assignment to a cited publication, but that publication was not independently assessed.",
    "The exact source snapshot used by the benchmark author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation specifies EC 2.3.1.312; no supplied evidence supports another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312. The annotation links the catalytic activity to PubMed evidence code ECO:0000269; the cited reaction is D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+). This supports choice C, although the primary paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include different enzyme reaction classifications, but the sequence and options alone provide no sufficiently specific biological argument for identifying this protein's exact substrate and reaction. Broad sequence-based functional inference would not establish the complete EC number.",
    "missing_item_specific_fact": "The protein-specific functional assignment identifying the sequence as D-glutamate N-acetyltransferase, and its catalyzed reaction, is needed to select EC 2.3.1.312.",
    "reason": "The reviewer evidence supports the key, but that annotation and its cited experimental evidence were not provided to the evaluated model. Recognizing or retrieving the exact protein entry would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation specifies EC 2.3.1.312; no supplied evidence supports another listed choice."
  },
  "important_caveats": [
    "The UniProt evidence links the functional assignment to a cited publication, but that publication was not independently assessed.",
    "The exact source snapshot used by the benchmark author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A2T1AE85 (sequence match confirmed, 333 AA, same SHA256) is annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269 from PubMed:36690779). X-ray crystallography at 2.20 Å (PDB:7XRJ) confirmed catalytic activity and mutagenesis of key residues (HIS-119, ARG-122, SER-125, GLN-177, ASP-185, ASP-190). The reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally established. This is a Swiss-Prot reviewed entry.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) fold motifs (e.g., 'GKISQEWKK', 'GTDCSVGK', 'GDGVPLDA'), which supports classification as an acyltransferase (EC 2.3.1.x), thereby eliminating option B (2.7.7.43, nucleotidyltransferase) and D (5.4.99.14, isomerase). However, this fold-level argument cannot distinguish between EC 2.3.1.322 (option A) and EC 2.3.1.312 (option C), both of which are acetyltransferases in the same subclass.


**Missing item-specific fact**

> The specific substrate identity (D-glutamate for 2.3.1.312 vs. the substrate of 2.3.1.322) required to distinguish the two remaining acyltransferase options. This enzyme was characterized in a 2023 paper (Yu et al., ISME J.) describing a novel D-glutamate catabolic pathway, making it a recently discovered enzyme whose substrate specificity cannot be inferred from general biological knowledge of the GNAT fold alone.


**Reason**

> While the GNAT fold narrows the answer to the 2.3.1.x subclass, the final distinction between two closely related acetyltransferase EC numbers (2.3.1.322 vs. 2.3.1.312) requires knowledge of the specific substrate or a database lookup. No sequence motif in the provided 333-residue protein uniquely encodes 'D-glutamate' as the substrate without external annotation or memorization of this specific enzyme's characterization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both options A (2.3.1.322) and C (2.3.1.312) are acetyltransferases in the same EC subclass. Without specific substrate knowledge or database access, a model identifying the GNAT fold could reasonably select either option. The distractors B (nucleotidyltransferase) and D (isomerase) are eliminable by fold recognition, but A vs. C requires item-specific knowledge.


### Important caveats

- The expected answer is experimentally validated (X-ray crystallography, mutagenesis, PubMed:36690779), so the key is scientifically correct.
- This is a novel enzyme described in 2023, making it unlikely to appear in pre-2023 training data, further increasing reliance on database lookup.
- The GNAT fold identification provides partial reasoning support (eliminates B and D) but is insufficient for the final A-vs-C discrimination.
- The identity of the protein was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) fold motifs (e.g., 'GKISQEWKK', 'GTDCSVGK', 'GDGVPLDA'), which supports classification as an acyltransferase (EC 2.3.1.x), thereby eliminating option B (2.7.7.43, nucleotidyltransferase) and D (5.4.99.14, isomerase). However, this fold-level argument cannot distinguish between EC 2.3.1.322 (option A) and EC 2.3.1.312 (option C), both of which are acetyltransferases in the same subclass.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (D-glutamate for 2.3.1.312 vs. the substrate of 2.3.1.322) required to distinguish the two remaining acyltransferase options. This enzyme was characterized in a 2023 paper (Yu et al., ISME J.) describing a novel D-glutamate catabolic pathway, making it a recently discovered enzyme whose substrate specificity cannot be inferred from general biological knowledge of the GNAT fold alone.",
    "reason": "While the GNAT fold narrows the answer to the 2.3.1.x subclass, the final distinction between two closely related acetyltransferase EC numbers (2.3.1.322 vs. 2.3.1.312) requires knowledge of the specific substrate or a database lookup. No sequence motif in the provided 333-residue protein uniquely encodes 'D-glutamate' as the substrate without external annotation or memorization of this specific enzyme's characterization."
  },
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A2T1AE85 (sequence match confirmed, 333 AA, same SHA256) is annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269 from PubMed:36690779). X-ray crystallography at 2.20 Å (PDB:7XRJ) confirmed catalytic activity and mutagenesis of key residues (HIS-119, ARG-122, SER-125, GLN-177, ASP-185, ASP-190). The reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally established. This is a Swiss-Prot reviewed entry."
  },
  "important_caveats": [
    "The expected answer is experimentally validated (X-ray crystallography, mutagenesis, PubMed:36690779), so the key is scientifically correct.",
    "This is a novel enzyme described in 2023, making it unlikely to appear in pre-2023 training data, further increasing reliance on database lookup.",
    "The GNAT fold identification provides partial reasoning support (eliminates B and D) but is insufficient for the final A-vs-C discrimination.",
    "The identity of the protein was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both options A (2.3.1.322) and C (2.3.1.312) are acetyltransferases in the same EC subclass. Without specific substrate knowledge or database access, a model identifying the GNAT fold could reasonably select either option. The distractors B (nucleotidyltransferase) and D (isomerase) are eliminable by fold recognition, but A vs. C requires item-specific knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A2T1AE85 (sequence match confirmed, 333 AA, same SHA256) is annotated as D-glutamate N-acetyltransferase, EC 2.3.1.312, with experimental evidence (ECO:0000269 from PubMed:36690779). X-ray crystallography at 2.20 Å (PDB:7XRJ) confirmed catalytic activity and mutagenesis of key residues (HIS-119, ARG-122, SER-125, GLN-177, ASP-185, ASP-190). The reaction D-glutamate + acetyl-CoA → N-acetyl-D-glutamate + CoA + H(+) is experimentally established. This is a Swiss-Prot reviewed entry.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) fold motifs (e.g., 'GKISQEWKK', 'GTDCSVGK', 'GDGVPLDA'), which supports classification as an acyltransferase (EC 2.3.1.x), thereby eliminating option B (2.7.7.43, nucleotidyltransferase) and D (5.4.99.14, isomerase). However, this fold-level argument cannot distinguish between EC 2.3.1.322 (option A) and EC 2.3.1.312 (option C), both of which are acetyltransferases in the same subclass.",
    "missing_item_specific_fact": "The specific substrate identity (D-glutamate for 2.3.1.312 vs. the substrate of 2.3.1.322) required to distinguish the two remaining acyltransferase options. This enzyme was characterized in a 2023 paper (Yu et al., ISME J.) describing a novel D-glutamate catabolic pathway, making it a recently discovered enzyme whose substrate specificity cannot be inferred from general biological knowledge of the GNAT fold alone.",
    "reason": "While the GNAT fold narrows the answer to the 2.3.1.x subclass, the final distinction between two closely related acetyltransferase EC numbers (2.3.1.322 vs. 2.3.1.312) requires knowledge of the specific substrate or a database lookup. No sequence motif in the provided 333-residue protein uniquely encodes 'D-glutamate' as the substrate without external annotation or memorization of this specific enzyme's characterization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both options A (2.3.1.322) and C (2.3.1.312) are acetyltransferases in the same EC subclass. Without specific substrate knowledge or database access, a model identifying the GNAT fold could reasonably select either option. The distractors B (nucleotidyltransferase) and D (isomerase) are eliminable by fold recognition, but A vs. C requires item-specific knowledge."
  },
  "important_caveats": [
    "The expected answer is experimentally validated (X-ray crystallography, mutagenesis, PubMed:36690779), so the key is scientifically correct.",
    "This is a novel enzyme described in 2023, making it unlikely to appear in pre-2023 training data, further increasing reliance on database lookup.",
    "The GNAT fold identification provides partial reasoning support (eliminates B and D) but is insufficient for the final A-vs-C discrimination.",
    "The identity of the protein was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence."
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

**Accession:** `A0A2T1AE85` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 17. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"value":"2.3.1.312"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"D-glutamate N-acetyltransferase"}}}
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"36690779","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:76496"}}],"reaction":{"ecNumber":"2.3.1.312","evidences":[{"evidenceCode":"ECO:0000269","id":"36690779","source":"PubMed"}],"name":"D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:76495"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29986"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:195260"}]}}
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2T1AE85.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:51.195751+00:00.  

```json
{"citation":{"authors":["Yu Y.","Wang P.","Cao H.Y.","Teng Z.J.","Zhu Y.","Wang M.","McMinn A.","Chen Y.","Xiang H.","Zhang Y.Z.","Chen X.L.","Zhang Y.Q."],"citationCrossReferences":[{"database":"PubMed","id":"36690779"},{"database":"DOI","id":"10.1038/s41396-023-01364-6"}],"citationType":"journal article","firstPage":"537","id":"36690779","journal":"ISME J.","lastPage":"548","publicationDate":"2023","title":"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.","volume":"17"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7XRJ","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 25328 / CCUG 55858 / LMG 24367 / R-28751"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190"]}
```

Source SHA-256: `09121d8b0043538afc137588986b1d12862e9e65cc3c978945cfbf12b87fe159`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:54.258050+00:00.  

```text
ID   DGCN_TRISK              Reviewed;         333 AA.
AC   A0A2T1AE85;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUL-2018, sequence version 1.
DT   28-JAN-2026, entry version 17.
DE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};
DE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};
GN   Name=dgcN {ECO:0000303|PubMed:36690779};
GN   ORFNames=CLV89_10851 {ECO:0000312|EMBL:PRZ46905.1};
OS   Tritonibacter scottomollicae (Epibacterium scottomollicae).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;
OC   Rhodobacterales; Paracoccaceae; Tritonibacter.
OX   NCBI_TaxID=483013;
```

Source SHA-256: `4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:54.258050+00:00.  

```text
DE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};
DE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};
```

Source SHA-256: `4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)  
**Locator:** `lines 21-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:54.258050+00:00.  

```text
RN   [2] {ECO:0007744|PDB:7XRJ}
RP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY, AND
RP   MUTAGENESIS OF HIS-119; ARG-122; SER-125; GLN-177; ASP-185 AND ASP-190.
RC   STRAIN=DSM 25328 / CCUG 55858 / LMG 24367 / R-28751;
RX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;
RA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,
RA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;
RT   "Novel D-glutamate catabolic pathway in marine Proteobacteria and
RT   halophilic archaea.";
RL   ISME J. 17:537-548(2023).
```

Source SHA-256: `4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2T1AE85?format=txt&versions=17)  
**Locator:** `lines 36-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:24:54.258050+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+);
CC         Xref=Rhea:RHEA:76495, ChEBI:CHEBI:15378, ChEBI:CHEBI:29986,
CC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195260;
CC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76496;
CC         Evidence={ECO:0000305|PubMed:36690779};
```

Source SHA-256: `4926acbea4e1ee7863274bfaadb5d06ca988e0c858a7b746efe1a16dba9863d6`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
