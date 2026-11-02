# EC_number_0107

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.3.1.319

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATKRKVIITCAPTGAIHTPSMSPYLPVTPQQIGDAALAAAKEGAAIIHLHARDPDDGHPTQDPAVFQEFLPRIKAECDAVINLTTGGSPHMTVAERLKPAHHFQPEVASLNMGSMNFGLYPMLERFKELKYDWERKHLENSRDLVFKNTFADIEYILTSCGANGTRFEFECYDISHLYNLAHFVDRGLAKPPFFVQSVFGLLGGIGAHPEDLAHMRRTADRLFGKDYVWSILGAGRNQIPLASIGVAQGSNARVGLEDSLWIEPGKLAESSAAQVRKIRQVIEGLSLDIATPAEAREMLQLKGAANTNF

[Multiple Choices]
A. 2.3.1.322
B. 2.3.1.319
C. 3.6.1.5
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

> The sequence exactly matches the UniProt entry annotated with EC 2.3.1.319. Its catalytic-activity annotation assigns that EC to a specific reaction and cites experimental evidence (ECO:0000269; PubMed 24240508).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone provides no supplied reaction, substrate-specificity evidence, or other concrete basis to distinguish these precise EC assignments.


**Missing item-specific fact**

> The protein's experimentally characterized catalytic reaction—3,5-dioxohexanoate plus acetyl-CoA yielding acetoacetyl-CoA plus acetoacetate—is needed to identify EC 2.3.1.319.


**Reason**

> Choosing among these specific EC numbers depends on protein-specific catalytic annotation or functional characterization not included in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports B for the matched sequence; it does not support another listed option.


### Important caveats

- The UniProt record links the EC assignment to experimental evidence and a cited publication, but the primary paper was not independently retrieved or validated here.
- The historical and current UniProt records match the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone provides no supplied reaction, substrate-specificity evidence, or other concrete basis to distinguish these precise EC assignments.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally characterized catalytic reaction—3,5-dioxohexanoate plus acetyl-CoA yielding acetoacetyl-CoA plus acetoacetate—is needed to identify EC 2.3.1.319.",
    "reason": "Choosing among these specific EC numbers depends on protein-specific catalytic annotation or functional characterization not included in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry annotated with EC 2.3.1.319. Its catalytic-activity annotation assigns that EC to a specific reaction and cites experimental evidence (ECO:0000269; PubMed 24240508)."
  },
  "important_caveats": [
    "The UniProt record links the EC assignment to experimental evidence and a cited publication, but the primary paper was not independently retrieved or validated here.",
    "The historical and current UniProt records match the supplied sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports B for the matched sequence; it does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry annotated with EC 2.3.1.319. Its catalytic-activity annotation assigns that EC to a specific reaction and cites experimental evidence (ECO:0000269; PubMed 24240508).",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone provides no supplied reaction, substrate-specificity evidence, or other concrete basis to distinguish these precise EC assignments.",
    "missing_item_specific_fact": "The protein's experimentally characterized catalytic reaction—3,5-dioxohexanoate plus acetyl-CoA yielding acetoacetyl-CoA plus acetoacetate—is needed to identify EC 2.3.1.319.",
    "reason": "Choosing among these specific EC numbers depends on protein-specific catalytic annotation or functional characterization not included in the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports B for the matched sequence; it does not support another listed option."
  },
  "important_caveats": [
    "The UniProt record links the EC assignment to experimental evidence and a cited publication, but the primary paper was not independently retrieved or validated here.",
    "The historical and current UniProt records match the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B1G5Y9 (DOHCE_PARG4) is annotated with EC 2.3.1.319 (3,5-dioxohexanoate:acetyl-CoA acetone transferase), supported by experimental evidence (ECO:0000269, in vitro experiment, PubMed:24240508, Nat. Chem. Biol. 2014). The benchmark sequence (310 AA, SHA256 669119f3...) matches the UniProt sequence exactly. The catalytic reaction is 3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains crotonase-superfamily motifs (e.g., 'GAGRNQ', 'GGIGAHP', 'GGSPHMT'), which could help a knowledgeable model eliminate EC 3.6.1.5 (ATP diphosphohydrolase, a hydrolase with a distinct fold) and EC 6.3.5.1 (glutamine synthase, a ligase with a completely different fold). However, this only narrows the answer to transferases (A or B). Distinguishing EC 2.3.1.322 from EC 2.3.1.319 requires knowing the precise catalytic residues, substrate specificity, and reaction mechanism of this particular enzyme—information not derivable from the raw sequence by general biological reasoning.


**Missing item-specific fact**

> The exact identity of EC 2.3.1.319 as '3,5-dioxohexanoate:acetyl-CoA acetone transferase' and the specific catalytic mechanism that distinguishes it from EC 2.3.1.322 (2,3-dioxo-5-methylsulfonylpentanoate acetyl-CoA transferase). Both are extremely obscure, recently characterized crotonase-superfamily transferases with no obvious sequence-level distinction visible in the provided input.


**Reason**

> EC 2.3.1.319 was only experimentally characterized in 2014 (PubMed:24240508) and the UniProt entry was created in 2025. Both choices A and B belong to the same EC sub-subclass (2.3.1, acyltransferases) and the crotonase superfamily. No general reasoning from the 310-aa sequence can determine which specific dioxoacid:acetyl-CoA transfer reaction this enzyme catalyzes. Selection depends on memorizing or looking up this particular protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both EC 2.3.1.322 and EC 2.3.1.319 are crotonase-superfamily transferases acting on dioxoacid substrates with acetyl-CoA. From the sequence alone, a model can plausibly identify the crotonase fold and narrow to transferases, but cannot definitively choose between these two nearly identical EC classifications without external annotation. Choices C (hydrolase) and D (ligase) are clearly eliminable by fold/motif analysis.


### Important caveats

- The EC 2.3.1.319 annotation is based on in vitro experimental evidence (ECO:0000269) from a single 2014 study, giving it strong evidential support.
- The UniProt entry was only created in February 2025; this is an extremely recent and obscure annotation unlikely to appear in any training corpus available to the evaluated model.
- The accession B1G5Y9 was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence with no identifier.
- Both A (2.3.1.322) and B (2.3.1.319) are highly specialized EC numbers with very few database entries, making this a near-lookup question even for domain experts without database access.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains crotonase-superfamily motifs (e.g., 'GAGRNQ', 'GGIGAHP', 'GGSPHMT'), which could help a knowledgeable model eliminate EC 3.6.1.5 (ATP diphosphohydrolase, a hydrolase with a distinct fold) and EC 6.3.5.1 (glutamine synthase, a ligase with a completely different fold). However, this only narrows the answer to transferases (A or B). Distinguishing EC 2.3.1.322 from EC 2.3.1.319 requires knowing the precise catalytic residues, substrate specificity, and reaction mechanism of this particular enzyme—information not derivable from the raw sequence by general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact identity of EC 2.3.1.319 as '3,5-dioxohexanoate:acetyl-CoA acetone transferase' and the specific catalytic mechanism that distinguishes it from EC 2.3.1.322 (2,3-dioxo-5-methylsulfonylpentanoate acetyl-CoA transferase). Both are extremely obscure, recently characterized crotonase-superfamily transferases with no obvious sequence-level distinction visible in the provided input.",
    "reason": "EC 2.3.1.319 was only experimentally characterized in 2014 (PubMed:24240508) and the UniProt entry was created in 2025. Both choices A and B belong to the same EC sub-subclass (2.3.1, acyltransferases) and the crotonase superfamily. No general reasoning from the 310-aa sequence can determine which specific dioxoacid:acetyl-CoA transfer reaction this enzyme catalyzes. Selection depends on memorizing or looking up this particular protein's database annotation."
  },
  "case_id": "EC_number_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B1G5Y9 (DOHCE_PARG4) is annotated with EC 2.3.1.319 (3,5-dioxohexanoate:acetyl-CoA acetone transferase), supported by experimental evidence (ECO:0000269, in vitro experiment, PubMed:24240508, Nat. Chem. Biol. 2014). The benchmark sequence (310 AA, SHA256 669119f3...) matches the UniProt sequence exactly. The catalytic reaction is 3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate."
  },
  "important_caveats": [
    "The EC 2.3.1.319 annotation is based on in vitro experimental evidence (ECO:0000269) from a single 2014 study, giving it strong evidential support.",
    "The UniProt entry was only created in February 2025; this is an extremely recent and obscure annotation unlikely to appear in any training corpus available to the evaluated model.",
    "The accession B1G5Y9 was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence with no identifier.",
    "Both A (2.3.1.322) and B (2.3.1.319) are highly specialized EC numbers with very few database entries, making this a near-lookup question even for domain experts without database access."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both EC 2.3.1.322 and EC 2.3.1.319 are crotonase-superfamily transferases acting on dioxoacid substrates with acetyl-CoA. From the sequence alone, a model can plausibly identify the crotonase fold and narrow to transferases, but cannot definitively choose between these two nearly identical EC classifications without external annotation. Choices C (hydrolase) and D (ligase) are clearly eliminable by fold/motif analysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B1G5Y9 (DOHCE_PARG4) is annotated with EC 2.3.1.319 (3,5-dioxohexanoate:acetyl-CoA acetone transferase), supported by experimental evidence (ECO:0000269, in vitro experiment, PubMed:24240508, Nat. Chem. Biol. 2014). The benchmark sequence (310 AA, SHA256 669119f3...) matches the UniProt sequence exactly. The catalytic reaction is 3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains crotonase-superfamily motifs (e.g., 'GAGRNQ', 'GGIGAHP', 'GGSPHMT'), which could help a knowledgeable model eliminate EC 3.6.1.5 (ATP diphosphohydrolase, a hydrolase with a distinct fold) and EC 6.3.5.1 (glutamine synthase, a ligase with a completely different fold). However, this only narrows the answer to transferases (A or B). Distinguishing EC 2.3.1.322 from EC 2.3.1.319 requires knowing the precise catalytic residues, substrate specificity, and reaction mechanism of this particular enzyme—information not derivable from the raw sequence by general biological reasoning.",
    "missing_item_specific_fact": "The exact identity of EC 2.3.1.319 as '3,5-dioxohexanoate:acetyl-CoA acetone transferase' and the specific catalytic mechanism that distinguishes it from EC 2.3.1.322 (2,3-dioxo-5-methylsulfonylpentanoate acetyl-CoA transferase). Both are extremely obscure, recently characterized crotonase-superfamily transferases with no obvious sequence-level distinction visible in the provided input.",
    "reason": "EC 2.3.1.319 was only experimentally characterized in 2014 (PubMed:24240508) and the UniProt entry was created in 2025. Both choices A and B belong to the same EC sub-subclass (2.3.1, acyltransferases) and the crotonase superfamily. No general reasoning from the 310-aa sequence can determine which specific dioxoacid:acetyl-CoA transfer reaction this enzyme catalyzes. Selection depends on memorizing or looking up this particular protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both EC 2.3.1.322 and EC 2.3.1.319 are crotonase-superfamily transferases acting on dioxoacid substrates with acetyl-CoA. From the sequence alone, a model can plausibly identify the crotonase fold and narrow to transferases, but cannot definitively choose between these two nearly identical EC classifications without external annotation. Choices C (hydrolase) and D (ligase) are clearly eliminable by fold/motif analysis."
  },
  "important_caveats": [
    "The EC 2.3.1.319 annotation is based on in vitro experimental evidence (ECO:0000269) from a single 2014 study, giving it strong evidential support.",
    "The UniProt entry was only created in February 2025; this is an extremely recent and obscure annotation unlikely to appear in any training corpus available to the evaluated model.",
    "The accession B1G5Y9 was inferred from dataset metadata (reviewer-only); the evaluated model received only the raw sequence with no identifier.",
    "Both A (2.3.1.322) and B (2.3.1.319) are highly specialized EC numbers with very few database entries, making this a near-lookup question even for domain experts without database access."
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

**Accession:** `B1G5Y9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 43. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.301562+00:00.  

```json
"B1G5Y9"
```

Source SHA-256: `2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.301562+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"3,5-dioxohexanoate cleavage enzyme"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24240508","source":"PubMed"}],"value":"BKACE_274"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24240508","source":"PubMed"}],"value":"2.3.1.319"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"3,5-dioxohexanoate:acetyl-CoA acetone transferase"}}}
```

Source SHA-256: `2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.301562+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.319","evidences":[{"evidenceCode":"ECO:0000269","id":"24240508","source":"PubMed"}],"name":"3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79655"},{"database":"ChEBI","id":"CHEBI:13705"},{"database":"ChEBI","id":"CHEBI:57286"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:57814"}]}}
```

Source SHA-256: `2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.301562+00:00.  

```json
{"citation":{"authors":["Bastard K.","Smith A.A.","Vergne-Vaxelaire C.","Perret A.","Zaparucha A.","De Melo-Minardi R.","Mariage A.","Boutard M.","Debard A.","Lechaplais C.","Pelle C.","Pellouin V.","Perchat N.","Petit J.L.","Kreimeyer A.","Medigue C.","Weissenbach J.","Artiguenave F.","De Berardinis V.","Vallenet D.","Salanoubat M."],"citationCrossReferences":[{"database":"PubMed","id":"24240508"},{"database":"DOI","id":"10.1038/nchembio.1387"}],"citationType":"journal article","firstPage":"42","id":"24240508","journal":"Nat. Chem. Biol.","lastPage":"49","publicationDate":"2014","title":"Revealing the hidden functional diversity of an enzyme family.","volume":"10"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-01T06:27:50.999580+00:00.  

```text
ID   DOHCE_PARG4             Reviewed;         310 AA.
AC   B1G5Y9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-APR-2008, sequence version 1.
DT   28-JAN-2026, entry version 43.
DE   RecName: Full=3,5-dioxohexanoate:acetyl-CoA acetone transferase {ECO:0000305};
DE            EC=2.3.1.319 {ECO:0000269|PubMed:24240508};
DE   AltName: Full=3,5-dioxohexanoate cleavage enzyme {ECO:0000305};
DE   AltName: Full=BKACE_274 {ECO:0000303|PubMed:24240508};
GN   Name=kce_3 {ECO:0000312|EMBL:CAB3715113.1};
GN   ORFNames=BgramDRAFT_4880 {ECO:0000312|EMBL:EDT08458.1},
GN   R8871_04389 {ECO:0000312|EMBL:CAB3715113.1};
OS   Paraburkholderia graminis (strain ATCC 700544 / DSM 17151 / LMG 18924 /
OS   NCIMB 13744 / C4D1M).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;
OC   Burkholderiales; Burkholderiaceae; Paraburkholderia.
OX   NCBI_TaxID=396598;
```

Source SHA-256: `d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-01T06:27:50.999580+00:00.  

```text
DE   RecName: Full=3,5-dioxohexanoate:acetyl-CoA acetone transferase {ECO:0000305};
DE            EC=2.3.1.319 {ECO:0000269|PubMed:24240508};
DE   AltName: Full=3,5-dioxohexanoate cleavage enzyme {ECO:0000305};
DE   AltName: Full=BKACE_274 {ECO:0000303|PubMed:24240508};
```

Source SHA-256: `d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)  
**Locator:** `lines 33-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-01T06:27:50.999580+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=24240508; DOI=10.1038/nchembio.1387;
RA   Bastard K., Smith A.A., Vergne-Vaxelaire C., Perret A., Zaparucha A.,
RA   De Melo-Minardi R., Mariage A., Boutard M., Debard A., Lechaplais C.,
RA   Pelle C., Pellouin V., Perchat N., Petit J.L., Kreimeyer A., Medigue C.,
RA   Weissenbach J., Artiguenave F., De Berardinis V., Vallenet D.,
RA   Salanoubat M.;
RT   "Revealing the hidden functional diversity of an enzyme family.";
RL   Nat. Chem. Biol. 10:42-49(2014).
```

Source SHA-256: `d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)  
**Locator:** `lines 47-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-01T06:27:50.999580+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA +
CC         acetoacetate; Xref=Rhea:RHEA:79655, ChEBI:CHEBI:13705,
CC         ChEBI:CHEBI:57286, ChEBI:CHEBI:57288, ChEBI:CHEBI:57814;
CC         EC=2.3.1.319; Evidence={ECO:0000269|PubMed:24240508};
```

Source SHA-256: `d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
