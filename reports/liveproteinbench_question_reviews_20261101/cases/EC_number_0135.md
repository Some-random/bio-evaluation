# EC_number_0135

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.3.1.31

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDNTPTPQKNPDTNPYASLISQQIAIIPSFTLESGVTLNNVPVAYKTWGKLNEKADNCLVICHALTGSADVEDWWGPLLGLNKAFDPTRFFIFCGNVIGSPYGTISSVTTNPETGKPFGPEMPGSSVKDDVRLHYIILKSLGVRSVAAVVGGSMGGMTVLEYPLNTPPGFVRAIIPLATSARHSAWCISWGEAQRQSIYSDPDYKDGYYYEIEEEGGKVDLARQPARGLAAARMAALLTYRSRDSFESRFGRRAGGGKSSVPKGGVRIMGGQETTDPSVPSESDLAAKSPSWRAWREHNDGHRSAGARPISRSGSEGPAHREGDAAQAEVVKTQDVKANGNKIGTGGEAPPKIFSAQSYLRYQGDKFTGRFDANCYIHITRKLDTHDLSAPSRDTSLSSLSSGLPSSPDATEEELNARLIHALSLEPPALVIGIESDGLFTTSEQRELAAGIPDAELVVIPSPDGHDGFLLEFEAINGWVEGWLKRKMPEFYERRVINPEEYVQGEEGFGIKKESVFGEAEADVTRW

[Multiple Choices]
A. 2.3.1.322
B. 4.1.1.129
C. 2.3.1.31
D. 3.1.1.4
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

> The exact supplied sequence matches the UniProt entry annotated as homoserine O-acetyltransferase, EC 2.3.1.31. The catalytic reaction and EC annotation cite experimental evidence (ECO:0000269, PubMed 17353245), supporting choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but it does not provide a sufficiently specific biological argument to establish the substrate and reaction needed to distinguish EC 2.3.1.31 from other candidate acyltransferase classifications.


**Missing item-specific fact**

> The protein-specific catalytic activity: transfer of an acetyl group from acetyl-CoA to L-homoserine to form O-acetyl-L-homoserine.


**Reason**

> The exact EC assignment is supported by a sequence-matched database annotation citing experimental evidence, but that annotation and reaction fact are not supplied in the question. Inferring the precise reaction from the sequence alone would depend on protein-specific lookup or prior knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports EC 2.3.1.31 for the sequence-matched protein; the other listed choices are not supported by that evidence.


### Important caveats

- The annotation and supporting source were available only to the reviewer, not to the evaluated model.
- The evidence cites an experimental publication, but the primary paper was not independently reviewed here.
- The exact author source snapshot is unknown, although the sequence match is established for the retrieved historical record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but it does not provide a sufficiently specific biological argument to establish the substrate and reaction needed to distinguish EC 2.3.1.31 from other candidate acyltransferase classifications.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity: transfer of an acetyl group from acetyl-CoA to L-homoserine to form O-acetyl-L-homoserine.",
    "reason": "The exact EC assignment is supported by a sequence-matched database annotation citing experimental evidence, but that annotation and reaction fact are not supplied in the question. Inferring the precise reaction from the sequence alone would depend on protein-specific lookup or prior knowledge."
  },
  "case_id": "EC_number_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as homoserine O-acetyltransferase, EC 2.3.1.31. The catalytic reaction and EC annotation cite experimental evidence (ECO:0000269, PubMed 17353245), supporting choice C."
  },
  "important_caveats": [
    "The annotation and supporting source were available only to the reviewer, not to the evaluated model.",
    "The evidence cites an experimental publication, but the primary paper was not independently reviewed here.",
    "The exact author source snapshot is unknown, although the sequence match is established for the retrieved historical record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports EC 2.3.1.31 for the sequence-matched protein; the other listed choices are not supported by that evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as homoserine O-acetyltransferase, EC 2.3.1.31. The catalytic reaction and EC annotation cite experimental evidence (ECO:0000269, PubMed 17353245), supporting choice C.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but it does not provide a sufficiently specific biological argument to establish the substrate and reaction needed to distinguish EC 2.3.1.31 from other candidate acyltransferase classifications.",
    "missing_item_specific_fact": "The protein-specific catalytic activity: transfer of an acetyl group from acetyl-CoA to L-homoserine to form O-acetyl-L-homoserine.",
    "reason": "The exact EC assignment is supported by a sequence-matched database annotation citing experimental evidence, but that annotation and reaction fact are not supplied in the question. Inferring the precise reaction from the sequence alone would depend on protein-specific lookup or prior knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports EC 2.3.1.31 for the sequence-matched protein; the other listed choices are not supported by that evidence."
  },
  "important_caveats": [
    "The annotation and supporting source were available only to the reviewer, not to the evaluated model.",
    "The evidence cites an experimental publication, but the primary paper was not independently reviewed here.",
    "The exact author source snapshot is unknown, although the sequence match is established for the retrieved historical record."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry J9VIY8 (MET2_CRYN9, Cryptococcus neoformans H99) annotates this 528-aa protein as Homoserine O-acetyltransferase with EC 2.3.1.31, supported by experimental evidence (ECO:0000269, PubMed 17353245: Nazi et al. 2007, Antimicrob. Agents Chemother. 51:1731-1736). The catalytic reaction L-homoserine + acetyl-CoA → O-acetyl-L-homoserine + CoA is confirmed. Sequence match is exact (SHA-256 identical).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The presence of a GxGxxG-like motif (GGSMGGMTV) and overall fold architecture could, in principle, support classifying this as an acyltransferase (EC 2.3.x.x), thereby eliminating B (EC 4.1.1.129, a lyase) and D (EC 3.1.1.4, a hydrolase). However, distinguishing EC 2.3.1.31 (homoserine O-acetyltransferase) from EC 2.3.1.322 (another acyltransferase) requires knowledge of the specific small-molecule substrate (homoserine) and the particular active-site architecture conferring that specificity, which is not reliably inferable from the raw sequence through general biological reasoning.


**Missing item-specific fact**

> The specific substrate identity (L-homoserine) and the active-site residue configuration that distinguishes EC 2.3.1.31 from other members of the 2.3.1.x acyltransferase family (e.g., EC 2.3.1.322). Identifying this protein as fungal MET2 and recalling its assigned EC number constitutes database lookup or memorization rather than de novo reasoning from sequence features.


**Reason**

> While the broad enzyme class (transferase vs. lyase vs. hydrolase) might be partially inferable from structural motifs, the question asks for a complete 4-digit EC number. Distinguishing 2.3.1.31 from 2.3.1.322 requires item-specific knowledge of substrate specificity and active-site chemistry that is not derivable from the sequence alone through general biological principles. The correct answer depends on recognizing this as MET2/homoserine O-acetyltransferase, which is a lookup-dependent identification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, B (lyase) and D (hydrolase) are in entirely different EC top-level classes and are not defensible for a transferase-fold protein. A (2.3.1.322) is in the same top-level class as C but represents a different specific reaction. Given the experimental annotation, C is uniquely correct. No ambiguity in the answer key itself.


### Important caveats

- The identity of EC 2.3.1.322 was not independently verified from the supplied evidence; it is treated as a plausible acyltransferase distractor based on its EC prefix.
- The reviewer-only UniProt annotation (experimental, PubMed 17353245) was not available to the evaluated model; the model must work from sequence alone.
- The entry was first released in Swiss-Prot on 2025-02-05 (entry version 54 archived at 2026-01-28); whether the benchmark was constructed after this date is unknown.
- The Rossmann-fold-like GxGxxG motif supports transferase classification but does not uniquely specify the substrate or the 4th EC digit.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The presence of a GxGxxG-like motif (GGSMGGMTV) and overall fold architecture could, in principle, support classifying this as an acyltransferase (EC 2.3.x.x), thereby eliminating B (EC 4.1.1.129, a lyase) and D (EC 3.1.1.4, a hydrolase). However, distinguishing EC 2.3.1.31 (homoserine O-acetyltransferase) from EC 2.3.1.322 (another acyltransferase) requires knowledge of the specific small-molecule substrate (homoserine) and the particular active-site architecture conferring that specificity, which is not reliably inferable from the raw sequence through general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (L-homoserine) and the active-site residue configuration that distinguishes EC 2.3.1.31 from other members of the 2.3.1.x acyltransferase family (e.g., EC 2.3.1.322). Identifying this protein as fungal MET2 and recalling its assigned EC number constitutes database lookup or memorization rather than de novo reasoning from sequence features.",
    "reason": "While the broad enzyme class (transferase vs. lyase vs. hydrolase) might be partially inferable from structural motifs, the question asks for a complete 4-digit EC number. Distinguishing 2.3.1.31 from 2.3.1.322 requires item-specific knowledge of substrate specificity and active-site chemistry that is not derivable from the sequence alone through general biological principles. The correct answer depends on recognizing this as MET2/homoserine O-acetyltransferase, which is a lookup-dependent identification."
  },
  "case_id": "EC_number_0135",
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
    "reason": "UniProt entry J9VIY8 (MET2_CRYN9, Cryptococcus neoformans H99) annotates this 528-aa protein as Homoserine O-acetyltransferase with EC 2.3.1.31, supported by experimental evidence (ECO:0000269, PubMed 17353245: Nazi et al. 2007, Antimicrob. Agents Chemother. 51:1731-1736). The catalytic reaction L-homoserine + acetyl-CoA → O-acetyl-L-homoserine + CoA is confirmed. Sequence match is exact (SHA-256 identical)."
  },
  "important_caveats": [
    "The identity of EC 2.3.1.322 was not independently verified from the supplied evidence; it is treated as a plausible acyltransferase distractor based on its EC prefix.",
    "The reviewer-only UniProt annotation (experimental, PubMed 17353245) was not available to the evaluated model; the model must work from sequence alone.",
    "The entry was first released in Swiss-Prot on 2025-02-05 (entry version 54 archived at 2026-01-28); whether the benchmark was constructed after this date is unknown.",
    "The Rossmann-fold-like GxGxxG motif supports transferase classification but does not uniquely specify the substrate or the 4th EC digit."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, B (lyase) and D (hydrolase) are in entirely different EC top-level classes and are not defensible for a transferase-fold protein. A (2.3.1.322) is in the same top-level class as C but represents a different specific reaction. Given the experimental annotation, C is uniquely correct. No ambiguity in the answer key itself."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry J9VIY8 (MET2_CRYN9, Cryptococcus neoformans H99) annotates this 528-aa protein as Homoserine O-acetyltransferase with EC 2.3.1.31, supported by experimental evidence (ECO:0000269, PubMed 17353245: Nazi et al. 2007, Antimicrob. Agents Chemother. 51:1731-1736). The catalytic reaction L-homoserine + acetyl-CoA → O-acetyl-L-homoserine + CoA is confirmed. Sequence match is exact (SHA-256 identical).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The presence of a GxGxxG-like motif (GGSMGGMTV) and overall fold architecture could, in principle, support classifying this as an acyltransferase (EC 2.3.x.x), thereby eliminating B (EC 4.1.1.129, a lyase) and D (EC 3.1.1.4, a hydrolase). However, distinguishing EC 2.3.1.31 (homoserine O-acetyltransferase) from EC 2.3.1.322 (another acyltransferase) requires knowledge of the specific small-molecule substrate (homoserine) and the particular active-site architecture conferring that specificity, which is not reliably inferable from the raw sequence through general biological reasoning.",
    "missing_item_specific_fact": "The specific substrate identity (L-homoserine) and the active-site residue configuration that distinguishes EC 2.3.1.31 from other members of the 2.3.1.x acyltransferase family (e.g., EC 2.3.1.322). Identifying this protein as fungal MET2 and recalling its assigned EC number constitutes database lookup or memorization rather than de novo reasoning from sequence features.",
    "reason": "While the broad enzyme class (transferase vs. lyase vs. hydrolase) might be partially inferable from structural motifs, the question asks for a complete 4-digit EC number. Distinguishing 2.3.1.31 from 2.3.1.322 requires item-specific knowledge of substrate specificity and active-site chemistry that is not derivable from the sequence alone through general biological principles. The correct answer depends on recognizing this as MET2/homoserine O-acetyltransferase, which is a lookup-dependent identification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, B (lyase) and D (hydrolase) are in entirely different EC top-level classes and are not defensible for a transferase-fold protein. A (2.3.1.322) is in the same top-level class as C but represents a different specific reaction. Given the experimental annotation, C is uniquely correct. No ambiguity in the answer key itself."
  },
  "important_caveats": [
    "The identity of EC 2.3.1.322 was not independently verified from the supplied evidence; it is treated as a plausible acyltransferase distractor based on its EC prefix.",
    "The reviewer-only UniProt annotation (experimental, PubMed 17353245) was not available to the evaluated model; the model must work from sequence alone.",
    "The entry was first released in Swiss-Prot on 2025-02-05 (entry version 54 archived at 2026-01-28); whether the benchmark was constructed after this date is unknown.",
    "The Rossmann-fold-like GxGxxG motif supports transferase classification but does not uniquely specify the substrate or the 4th EC digit."
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

**Accession:** `J9VIY8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
"J9VIY8"
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"value":"2.3.1.31"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Homoserine O-acetyltransferase"}}}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13702"}}],"reaction":{"ecNumber":"2.3.1.31","evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"name":"L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13701"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:57476"},{"database":"ChEBI","id":"CHEBI:57716"}]}}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"citation":{"authors":["Nazi I.","Scott A.","Sham A.","Rossi L.","Williamson P.R.","Kronstad J.W.","Wright G.D."],"citationCrossReferences":[{"database":"PubMed","id":"17353245"},{"database":"DOI","id":"10.1128/aac.01400-06"}],"citationType":"journal article","firstPage":"1731","id":"17353245","journal":"Antimicrob. Agents Chemother.","lastPage":"1736","publicationDate":"2007","title":"Role of homoserine transacetylase as a new target for antifungal agents.","volume":"51"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
ID   MET2_CRYN9              Reviewed;         528 AA.
AC   J9VIY8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-NOV-2012, sequence version 1.
DT   28-JAN-2026, entry version 54.
DE   RecName: Full=Homoserine O-acetyltransferase {ECO:0000305};
DE            EC=2.3.1.31 {ECO:0000269|PubMed:17353245};
GN   Name=MET2 {ECO:0000303|PubMed:17353245};
GN   ORFNames=CNAG_05122 {ECO:0000312|EMBL:AFR94387.1};
OS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)
OS   (Cryptococcus neoformans var. grubii serotype A).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
DE   RecName: Full=Homoserine O-acetyltransferase {ECO:0000305};
DE            EC=2.3.1.31 {ECO:0000269|PubMed:17353245};
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 35-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION
RP   PHENOTYPE.
RX   PubMed=17353245; DOI=10.1128/aac.01400-06;
RA   Nazi I., Scott A., Sham A., Rossi L., Williamson P.R., Kronstad J.W.,
RA   Wright G.D.;
RT   "Role of homoserine transacetylase as a new target for antifungal agents.";
RL   Antimicrob. Agents Chemother. 51:1731-1736(2007).
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 45-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA;
CC         Xref=Rhea:RHEA:13701, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:57476, ChEBI:CHEBI:57716; EC=2.3.1.31;
CC         Evidence={ECO:0000269|PubMed:17353245};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13702;
CC         Evidence={ECO:0000269|PubMed:17353245};
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 135. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
