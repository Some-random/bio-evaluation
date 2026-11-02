# EC_number_0065

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 1.3.1.36

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGESTQVDLSVKAIGWGAKDASGILHPIKFSRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVVEVGSKVQKFKVGDKVAVGCMVGSCGKCYNCENGMENYCPEPNMADGSVYREQGERSYGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGVVVYSPMKYMGLDKPGKHIGVFGLGGLGSVAVKFIKAFGGKATVISTSRRKEKEAIEEHGADAFVVNSDTEQLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGSLILVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQEMLDFAAKHNILCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYEE

[Multiple Choices]
A. 1.3.1.73
B. 3.6.1.5
C. 2.1.1.393
D. 1.3.1.36
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

> The exact sequence matches the UniProt entry annotated as EC 1.3.1.36, with catalytic activity assigned that EC number and linked to ECO:0000269 experimental evidence. This supports the author's key, while the underlying publication was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a dehydrogenase, but that broad inference does not establish its substrate-specific reaction or distinguish EC 1.3.1.36 from the other listed EC numbers.


**Missing item-specific fact**

> The protein's specific catalytic activity on geissoschizine, and its associated EC classification, is not supplied in the question.


**Reason**

> Selecting the exact EC number requires protein-specific functional annotation or experimental knowledge absent from the sequence-and-choices input; recognizing the sequence from a database would be lookup, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence has experimental-evidence-linked annotation for 1.3.1.36; the reviewer evidence does not support another listed option.


### Important caveats

- The UniProt record is a current and archived database annotation, not an independent review of the cited primary experiment.
- The exact author source snapshot is unknown, although the sequence matches the historical and current records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a dehydrogenase, but that broad inference does not establish its substrate-specific reaction or distinguish EC 1.3.1.36 from the other listed EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific catalytic activity on geissoschizine, and its associated EC classification, is not supplied in the question.",
    "reason": "Selecting the exact EC number requires protein-specific functional annotation or experimental knowledge absent from the sequence-and-choices input; recognizing the sequence from a database would be lookup, not reasoning from supplied context."
  },
  "case_id": "EC_number_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 1.3.1.36, with catalytic activity assigned that EC number and linked to ECO:0000269 experimental evidence. This supports the author's key, while the underlying publication was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt record is a current and archived database annotation, not an independent review of the cited primary experiment.",
    "The exact author source snapshot is unknown, although the sequence matches the historical and current records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has experimental-evidence-linked annotation for 1.3.1.36; the reviewer evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 1.3.1.36, with catalytic activity assigned that EC number and linked to ECO:0000269 experimental evidence. This supports the author's key, while the underlying publication was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a dehydrogenase, but that broad inference does not establish its substrate-specific reaction or distinguish EC 1.3.1.36 from the other listed EC numbers.",
    "missing_item_specific_fact": "The protein's specific catalytic activity on geissoschizine, and its associated EC classification, is not supplied in the question.",
    "reason": "Selecting the exact EC number requires protein-specific functional annotation or experimental knowledge absent from the sequence-and-choices input; recognizing the sequence from a database would be lookup, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has experimental-evidence-linked annotation for 1.3.1.36; the reviewer evidence does not support another listed option."
  },
  "important_caveats": [
    "The UniProt record is a current and archived database annotation, not an independent review of the cited primary experiment.",
    "The exact author source snapshot is unknown, although the sequence matches the historical and current records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> UniProt entry A0A9E7LUR3 (sequence SHA256 match confirmed) annotates this protein as Geissoschizine synthase (AsGS) with EC 1.3.1.36, supported by in vitro experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH is explicitly assigned EC=1.3.1.36. The alternative name 'Alcohol dehydrogenase GS' is consistent with the observed ADH-fold sequence features.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence clearly displays an alcohol dehydrogenase (ADH) architecture: a Rossmann-fold NAD(P)-binding motif (GGLGSVAVKFIK), a second NAD-binding region (CAGVVVYSPMKY), and zinc-binding cysteine clusters (CGVCNFDMEM, GCMVGSCGKCYNCENGMENYCPEPN). These features confidently identify the enzyme as an oxidoreductase of the ADH superfamily, eliminating B (3.6.1.5, ATP diphosphohydrolase, a hydrolase) and C (2.1.1.393, a methyltransferase). However, both A (1.3.1.73) and D (1.3.1.36) belong to the same EC subclass (1.3.1.x, oxidoreductases acting on CH-CH group with NAD+/NADP+ as acceptor) and share the same overall fold. Distinguishing the specific 4-digit code requires knowing the exact substrate (geissoschizine for 1.3.1.36), which is not derivable from the sequence alone without organism context or substrate knowledge.


**Missing item-specific fact**

> The specific substrate identity (geissoschizine, a monoterpenoid indole alkaloid) and the organism source (Alstonia scholaris, a Gentianales plant specialized in indole alkaloid biosynthesis) are absent from the question input. Without these, the model cannot reason from sequence to the precise 4-digit EC code distinguishing 1.3.1.36 from 1.3.1.73.


**Reason**

> General ADH-fold recognition eliminates the hydrolase and transferase distractors, but the remaining two choices share the same EC subclass and fold architecture. Selecting 1.3.1.36 over 1.3.1.73 depends on knowing the specific enzymatic reaction and substrate, which is an item-specific annotation fact not inferable from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (1.3.1.73)",
  "D (1.3.1.36)"
]
```

> Both A and D are oxidoreductases acting on CH-CH group donors with NAD(P)+ as acceptor, consistent with the ADH-fold sequence. Without organism context or substrate information in the question, the sequence features cannot definitively distinguish the specific 4-digit code. B and C are clearly eliminable by fold analysis.


### Important caveats

- The organism (Alstonia scholaris, a plant known for indole alkaloid biosynthesis) is not provided in the question input; its absence removes a strong contextual clue for reasoning toward alkaloid-specific EC numbers.
- The UniProt annotation for EC 1.3.1.36 is based on in vitro experimental evidence (ECO:0000269), making the key well-supported as a factual claim.
- The sequence-match between the benchmark input and UniProt A0A9E7LUR3 is exact (SHA256 confirmed), so the annotation applies directly to the supplied sequence.
- EC 1.3.1.73 as a distractor is in the same EC subclass as the correct answer, making it a non-trivial distractor that cannot be eliminated by broad fold analysis alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence clearly displays an alcohol dehydrogenase (ADH) architecture: a Rossmann-fold NAD(P)-binding motif (GGLGSVAVKFIK), a second NAD-binding region (CAGVVVYSPMKY), and zinc-binding cysteine clusters (CGVCNFDMEM, GCMVGSCGKCYNCENGMENYCPEPN). These features confidently identify the enzyme as an oxidoreductase of the ADH superfamily, eliminating B (3.6.1.5, ATP diphosphohydrolase, a hydrolase) and C (2.1.1.393, a methyltransferase). However, both A (1.3.1.73) and D (1.3.1.36) belong to the same EC subclass (1.3.1.x, oxidoreductases acting on CH-CH group with NAD+/NADP+ as acceptor) and share the same overall fold. Distinguishing the specific 4-digit code requires knowing the exact substrate (geissoschizine for 1.3.1.36), which is not derivable from the sequence alone without organism context or substrate knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (geissoschizine, a monoterpenoid indole alkaloid) and the organism source (Alstonia scholaris, a Gentianales plant specialized in indole alkaloid biosynthesis) are absent from the question input. Without these, the model cannot reason from sequence to the precise 4-digit EC code distinguishing 1.3.1.36 from 1.3.1.73.",
    "reason": "General ADH-fold recognition eliminates the hydrolase and transferase distractors, but the remaining two choices share the same EC subclass and fold architecture. Selecting 1.3.1.36 over 1.3.1.73 depends on knowing the specific enzymatic reaction and substrate, which is an item-specific annotation fact not inferable from sequence alone."
  },
  "case_id": "EC_number_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A9E7LUR3 (sequence SHA256 match confirmed) annotates this protein as Geissoschizine synthase (AsGS) with EC 1.3.1.36, supported by in vitro experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH is explicitly assigned EC=1.3.1.36. The alternative name 'Alcohol dehydrogenase GS' is consistent with the observed ADH-fold sequence features."
  },
  "important_caveats": [
    "The organism (Alstonia scholaris, a plant known for indole alkaloid biosynthesis) is not provided in the question input; its absence removes a strong contextual clue for reasoning toward alkaloid-specific EC numbers.",
    "The UniProt annotation for EC 1.3.1.36 is based on in vitro experimental evidence (ECO:0000269), making the key well-supported as a factual claim.",
    "The sequence-match between the benchmark input and UniProt A0A9E7LUR3 is exact (SHA256 confirmed), so the annotation applies directly to the supplied sequence.",
    "EC 1.3.1.73 as a distractor is in the same EC subclass as the correct answer, making it a non-trivial distractor that cannot be eliminated by broad fold analysis alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (1.3.1.73)",
      "D (1.3.1.36)"
    ],
    "reason": "Both A and D are oxidoreductases acting on CH-CH group donors with NAD(P)+ as acceptor, consistent with the ADH-fold sequence. Without organism context or substrate information in the question, the sequence features cannot definitively distinguish the specific 4-digit code. B and C are clearly eliminable by fold analysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A9E7LUR3 (sequence SHA256 match confirmed) annotates this protein as Geissoschizine synthase (AsGS) with EC 1.3.1.36, supported by in vitro experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction (19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH is explicitly assigned EC=1.3.1.36. The alternative name 'Alcohol dehydrogenase GS' is consistent with the observed ADH-fold sequence features.",
    "evidence_ids": ["C4", "C5", "C8", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence clearly displays an alcohol dehydrogenase (ADH) architecture: a Rossmann-fold NAD(P)-binding motif (GGLGSVAVKFIK), a second NAD-binding region (CAGVVVYSPMKY), and zinc-binding cysteine clusters (CGVCNFDMEM, GCMVGSCGKCYNCENGMENYCPEPN). These features confidently identify the enzyme as an oxidoreductase of the ADH superfamily, eliminating B (3.6.1.5, ATP diphosphohydrolase, a hydrolase) and C (2.1.1.393, a methyltransferase). However, both A (1.3.1.73) and D (1.3.1.36) belong to the same EC subclass (1.3.1.x, oxidoreductases acting on CH-CH group with NAD+/NADP+ as acceptor) and share the same overall fold. Distinguishing the specific 4-digit code requires knowing the exact substrate (geissoschizine for 1.3.1.36), which is not derivable from the sequence alone without organism context or substrate knowledge.",
    "missing_item_specific_fact": "The specific substrate identity (geissoschizine, a monoterpenoid indole alkaloid) and the organism source (Alstonia scholaris, a Gentianales plant specialized in indole alkaloid biosynthesis) are absent from the question input. Without these, the model cannot reason from sequence to the precise 4-digit EC code distinguishing 1.3.1.36 from 1.3.1.73.",
    "reason": "General ADH-fold recognition eliminates the hydrolase and transferase distractors, but the remaining two choices share the same EC subclass and fold architecture. Selecting 1.3.1.36 over 1.3.1.73 depends on knowing the specific enzymatic reaction and substrate, which is an item-specific annotation fact not inferable from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (1.3.1.73)", "D (1.3.1.36)"],
    "reason": "Both A and D are oxidoreductases acting on CH-CH group donors with NAD(P)+ as acceptor, consistent with the ADH-fold sequence. Without organism context or substrate information in the question, the sequence features cannot definitively distinguish the specific 4-digit code. B and C are clearly eliminable by fold analysis."
  },
  "important_caveats": [
    "The organism (Alstonia scholaris, a plant known for indole alkaloid biosynthesis) is not provided in the question input; its absence removes a strong contextual clue for reasoning toward alkaloid-specific EC numbers.",
    "The UniProt annotation for EC 1.3.1.36 is based on in vitro experimental evidence (ECO:0000269), making the key well-supported as a factual claim.",
    "The sequence-match between the benchmark input and UniProt A0A9E7LUR3 is exact (SHA256 confirmed), so the annotation applies directly to the supplied sequence.",
    "EC 1.3.1.73 as a distractor is in the same EC subclass as the correct answer, making it a non-trivial distractor that cannot be eliminated by broad fold analysis alone."
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

**Accession:** `A0A9E7LUR3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:11.087134+00:00.  

```json
"A0A9E7LUR3"
```

Source SHA-256: `a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:11.087134+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Alcohol dehydrogenase GS"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"1.3.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Geissoschizine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsGS"}]}}
```

Source SHA-256: `a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:11.087134+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:11378"}}],"reaction":{"ecNumber":"1.3.1.36","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"name":"(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine + NADPH","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:11376"},{"database":"ChEBI","id":"CHEBI:17037"},{"database":"ChEBI","id":"CHEBI:17294"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"}]}}
```

Source SHA-256: `a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUR3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:11.087134+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65381.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `a882b68fd7c14ca824ffd0394e9d4ac0db53220bba86949cf217c54345aecd05`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:15.563182+00:00.  

```text
ID   GS_ALSSC                Reviewed;         364 AA.
AC   A0A9E7LUR3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 12.
DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:36349266};
DE            Short=AsGS {ECO:0000303|PubMed:36349266};
DE            EC=1.3.1.36 {ECO:0000269|PubMed:36349266};
DE   AltName: Full=Alcohol dehydrogenase GS {ECO:0000305};
GN   Name=GS {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:15.563182+00:00.  

```text
DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:36349266};
DE            Short=AsGS {ECO:0000303|PubMed:36349266};
DE            EC=1.3.1.36 {ECO:0000269|PubMed:36349266};
DE   AltName: Full=Alcohol dehydrogenase GS {ECO:0000305};
```

Source SHA-256: `77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUR3?format=txt&versions=12)  
**Locator:** `lines 29-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:26:15.563182+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(19E)-geissoschizine + NADP(+) = 4,21-dehydrogeissoschizine +
CC         NADPH; Xref=Rhea:RHEA:11376, ChEBI:CHEBI:17037, ChEBI:CHEBI:17294,
CC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349; EC=1.3.1.36;
CC         Evidence={ECO:0000269|PubMed:36349266};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:11378;
CC         Evidence={ECO:0000269|PubMed:36349266};
```

Source SHA-256: `77ff10b42c5078be81b8aafcc4ef858dbdc2d041d1fd54a8a90b0dd20ac0ec4e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 65. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
