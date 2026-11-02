# EC_number_0153

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.1.1.393

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAENQEALAEFYDKGVGVWDNLSREHMHFGYYAPGATATIGGHRASLVRLIDEALCFAEFPDDPEKKPRNMLDVGCGIGGTCLHVAKKYDIQCKGINISPEQVKIAQGLAAAQGLESKVSFDVGDALDMPYPDGAFDLVLSIHCIEHLQDKEKFIREMVRVAASGATIIILSHVHRDLSPSEQSLKPQEERVLRKIGSSVQAWFCPLSNYVSLLAPLPVEVIKIADWSRNIDPSSRLMLKVAFSVKGIVSNLMKGVQGWTAIKNVLPMKLLHKALHDGLVKFVVLTCRKSN

[Multiple Choices]
A. 2.1.1.27
B. 3.2.1.8
C. 1.14.14.154
D. 2.1.1.393
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

> The supplied sequence exactly matches the 291-aa UniProt entry for Rauvolfia serpentina ajmaline N-methyltransferase. That entry assigns EC 2.1.1.393 and cites experimental evidence for methylation of ajmaline and norajmaline. The cited primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a methyltransferase, which could favor EC-class 2.1.1 over the hydrolase and oxidoreductase options. But choices A and D are both methyltransferases, and broad sequence-based recognition does not establish the specific substrate reaction that distinguishes their complete EC numbers.


**Missing item-specific fact**

> The protein's specific catalytic activity—methylation of ajmaline/norajmaline—or an equivalent protein-specific functional annotation is needed to distinguish EC 2.1.1.393 from the other methyltransferase choice.


**Reason**

> The sequence may support a broad functional class, but the exact EC assignment depends on substrate specificity not supplied in the question. Recognizing this particular sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The enzyme has a specific EC assignment when its catalytic activity is known. The issue is that the sequence and choices alone do not provide enough information to distinguish the two methyltransferase EC numbers, rather than the wording defining multiple correct answers.


### Important caveats

- The sequence-to-entry match applies to the supplied sequence; the reviewer-only accession and annotation were not provided to the evaluated model.
- The experimental-support claim is based on UniProt annotations citing PubMed 27122470; the primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a methyltransferase, which could favor EC-class 2.1.1 over the hydrolase and oxidoreductase options. But choices A and D are both methyltransferases, and broad sequence-based recognition does not establish the specific substrate reaction that distinguishes their complete EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific catalytic activity—methylation of ajmaline/norajmaline—or an equivalent protein-specific functional annotation is needed to distinguish EC 2.1.1.393 from the other methyltransferase choice.",
    "reason": "The sequence may support a broad functional class, but the exact EC assignment depends on substrate specificity not supplied in the question. Recognizing this particular sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 291-aa UniProt entry for Rauvolfia serpentina ajmaline N-methyltransferase. That entry assigns EC 2.1.1.393 and cites experimental evidence for methylation of ajmaline and norajmaline. The cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence-to-entry match applies to the supplied sequence; the reviewer-only accession and annotation were not provided to the evaluated model.",
    "The experimental-support claim is based on UniProt annotations citing PubMed 27122470; the primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has a specific EC assignment when its catalytic activity is known. The issue is that the sequence and choices alone do not provide enough information to distinguish the two methyltransferase EC numbers, rather than the wording defining multiple correct answers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 291-aa UniProt entry for Rauvolfia serpentina ajmaline N-methyltransferase. That entry assigns EC 2.1.1.393 and cites experimental evidence for methylation of ajmaline and norajmaline. The cited primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a methyltransferase, which could favor EC-class 2.1.1 over the hydrolase and oxidoreductase options. But choices A and D are both methyltransferases, and broad sequence-based recognition does not establish the specific substrate reaction that distinguishes their complete EC numbers.",
    "missing_item_specific_fact": "The protein's specific catalytic activity—methylation of ajmaline/norajmaline—or an equivalent protein-specific functional annotation is needed to distinguish EC 2.1.1.393 from the other methyltransferase choice.",
    "reason": "The sequence may support a broad functional class, but the exact EC assignment depends on substrate specificity not supplied in the question. Recognizing this particular sequence or recalling its database annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme has a specific EC assignment when its catalytic activity is known. The issue is that the sequence and choices alone do not provide enough information to distinguish the two methyltransferase EC numbers, rather than the wording defining multiple correct answers."
  },
  "important_caveats": [
    "The sequence-to-entry match applies to the supplied sequence; the reviewer-only accession and annotation were not provided to the evaluated model.",
    "The experimental-support claim is based on UniProt annotations citing PubMed 27122470; the primary paper was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A075D654 (sequence SHA256 matched) annotates this protein as Ajmaline N-methyltransferase with EC=2.1.1.393, supported by experimental evidence (ECO:0000269, PubMed:27122470). The catalytic reactions (ajmaline + SAM → 4-methylajmaline + SAH + H+; norajmaline + SAM → 4-methylnorajmaline + SAH + H+) confirm an N-methyltransferase (EC class 2.1.1.x). The expected answer D is well-supported by experimental data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a canonical GxGxG SAM-binding motif (GCGIGGT) and overall Class I methyltransferase architecture (Rossmann-like fold region), which allows elimination of B (3.2.1.8, a glycosidase/hydrolase) and C (1.14.14.154, a cytochrome P450 oxidoreductase) through general enzyme-structure knowledge. However, both remaining options A (2.1.1.27) and D (2.1.1.393) are methyltransferases, and no general sequence feature distinguishes which specific substrate (ajmaline vs. the substrate of 2.1.1.27) this enzyme methylates.


**Missing item-specific fact**

> The specific substrate identity (ajmaline/norajmaline N-methylation) and the evolutionary derivation from gamma-tocopherol C-methyltransferase are protein-specific facts not inferable from the bare 291-aa sequence without prior knowledge of this enzyme's characterization in Rauvolfia serpentina alkaloid biosynthesis.


**Reason**

> While sequence-level methyltransferase motifs eliminate two of four choices, the final distinction between two EC 2.1.1.x numbers requires knowing this particular enzyme's substrate specificity, which is an item-specific experimental annotation (PubMed:27122470) rather than a generalizable sequence-to-function inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (2.1.1.27) and D (2.1.1.393) are methyltransferase EC numbers. Without organism context, substrate information, or pathway annotation in the input, a model relying solely on sequence cannot definitively choose between two methyltransferase EC numbers. The GxGxG motif and overall fold confirm methyltransferase class but not the specific substrate.


### Important caveats

- The UniProt annotation is Swiss-Prot (reviewed) with experimental evidence (ECO:0000269), providing high confidence for the EC assignment.
- The organism (Rauvolfia serpentina) and pathway context (ajmaline biosynthesis) are not provided in the model input, removing a potential contextual clue.
- The alternative name 'Gamma-tocopherol-like methyltransferase ANMT' reflects evolutionary origin but does not help distinguish EC 2.1.1.27 from 2.1.1.393 by sequence alone.
- The sequence-match between benchmark input and UniProt entry is exact (SHA256 confirmed), so the annotation applies directly to this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical GxGxG SAM-binding motif (GCGIGGT) and overall Class I methyltransferase architecture (Rossmann-like fold region), which allows elimination of B (3.2.1.8, a glycosidase/hydrolase) and C (1.14.14.154, a cytochrome P450 oxidoreductase) through general enzyme-structure knowledge. However, both remaining options A (2.1.1.27) and D (2.1.1.393) are methyltransferases, and no general sequence feature distinguishes which specific substrate (ajmaline vs. the substrate of 2.1.1.27) this enzyme methylates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (ajmaline/norajmaline N-methylation) and the evolutionary derivation from gamma-tocopherol C-methyltransferase are protein-specific facts not inferable from the bare 291-aa sequence without prior knowledge of this enzyme's characterization in Rauvolfia serpentina alkaloid biosynthesis.",
    "reason": "While sequence-level methyltransferase motifs eliminate two of four choices, the final distinction between two EC 2.1.1.x numbers requires knowing this particular enzyme's substrate specificity, which is an item-specific experimental annotation (PubMed:27122470) rather than a generalizable sequence-to-function inference."
  },
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A075D654 (sequence SHA256 matched) annotates this protein as Ajmaline N-methyltransferase with EC=2.1.1.393, supported by experimental evidence (ECO:0000269, PubMed:27122470). The catalytic reactions (ajmaline + SAM → 4-methylajmaline + SAH + H+; norajmaline + SAM → 4-methylnorajmaline + SAH + H+) confirm an N-methyltransferase (EC class 2.1.1.x). The expected answer D is well-supported by experimental data."
  },
  "important_caveats": [
    "The UniProt annotation is Swiss-Prot (reviewed) with experimental evidence (ECO:0000269), providing high confidence for the EC assignment.",
    "The organism (Rauvolfia serpentina) and pathway context (ajmaline biosynthesis) are not provided in the model input, removing a potential contextual clue.",
    "The alternative name 'Gamma-tocopherol-like methyltransferase ANMT' reflects evolutionary origin but does not help distinguish EC 2.1.1.27 from 2.1.1.393 by sequence alone.",
    "The sequence-match between benchmark input and UniProt entry is exact (SHA256 confirmed), so the annotation applies directly to this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (2.1.1.27) and D (2.1.1.393) are methyltransferase EC numbers. Without organism context, substrate information, or pathway annotation in the input, a model relying solely on sequence cannot definitively choose between two methyltransferase EC numbers. The GxGxG motif and overall fold confirm methyltransferase class but not the specific substrate."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A075D654 (sequence SHA256 matched) annotates this protein as Ajmaline N-methyltransferase with EC=2.1.1.393, supported by experimental evidence (ECO:0000269, PubMed:27122470). The catalytic reactions (ajmaline + SAM → 4-methylajmaline + SAH + H+; norajmaline + SAM → 4-methylnorajmaline + SAH + H+) confirm an N-methyltransferase (EC class 2.1.1.x). The expected answer D is well-supported by experimental data.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a canonical GxGxG SAM-binding motif (GCGIGGT) and overall Class I methyltransferase architecture (Rossmann-like fold region), which allows elimination of B (3.2.1.8, a glycosidase/hydrolase) and C (1.14.14.154, a cytochrome P450 oxidoreductase) through general enzyme-structure knowledge. However, both remaining options A (2.1.1.27) and D (2.1.1.393) are methyltransferases, and no general sequence feature distinguishes which specific substrate (ajmaline vs. the substrate of 2.1.1.27) this enzyme methylates.",
    "missing_item_specific_fact": "The specific substrate identity (ajmaline/norajmaline N-methylation) and the evolutionary derivation from gamma-tocopherol C-methyltransferase are protein-specific facts not inferable from the bare 291-aa sequence without prior knowledge of this enzyme's characterization in Rauvolfia serpentina alkaloid biosynthesis.",
    "reason": "While sequence-level methyltransferase motifs eliminate two of four choices, the final distinction between two EC 2.1.1.x numbers requires knowing this particular enzyme's substrate specificity, which is an item-specific experimental annotation (PubMed:27122470) rather than a generalizable sequence-to-function inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (2.1.1.27) and D (2.1.1.393) are methyltransferase EC numbers. Without organism context, substrate information, or pathway annotation in the input, a model relying solely on sequence cannot definitively choose between two methyltransferase EC numbers. The GxGxG motif and overall fold confirm methyltransferase class but not the specific substrate."
  },
  "important_caveats": [
    "The UniProt annotation is Swiss-Prot (reviewed) with experimental evidence (ECO:0000269), providing high confidence for the EC assignment.",
    "The organism (Rauvolfia serpentina) and pathway context (ajmaline biosynthesis) are not provided in the model input, removing a potential contextual clue.",
    "The alternative name 'Gamma-tocopherol-like methyltransferase ANMT' reflects evolutionary origin but does not help distinguish EC 2.1.1.27 from 2.1.1.393 by sequence alone.",
    "The sequence-match between benchmark input and UniProt entry is exact (SHA256 confirmed), so the annotation applies directly to this sequence."
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

**Accession:** `A0A075D654` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
"A0A075D654"
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AHH02777.1","source":"EMBL"}],"value":"Gamma-tocopherol-like methyltransferase ANMT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"value":"2.1.1.393"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"}],"value":"Ajmaline N-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"}],"value":"RsANMT"}]}}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79632"}}],"reaction":{"ecNumber":"2.1.1.393","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"name":"ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79631"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:58567"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:230509"}]}}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79628"}}],"reaction":{"ecNumber":"2.1.1.393","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"name":"norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79627"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:77618"},{"database":"ChEBI","id":"CHEBI:230510"}]}}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"citation":{"authors":["Cazares-Flores P.","Levac D.","De Luca V."],"citationCrossReferences":[{"database":"PubMed","id":"27122470"},{"database":"DOI","id":"10.1111/tpj.13186"}],"citationType":"journal article","firstPage":"335","id":"27122470","journal":"Plant J.","lastPage":"342","publicationDate":"2016","title":"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.","volume":"87"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
ID   ANMT_RAUSE              Reviewed;         291 AA.
AC   A0A075D654;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-OCT-2014, sequence version 1.
DT   28-JAN-2026, entry version 32.
DE   RecName: Full=Ajmaline N-methyltransferase {ECO:0000303|PubMed:27122470};
DE            Short=RsANMT {ECO:0000303|PubMed:27122470};
DE            EC=2.1.1.393 {ECO:0000269|PubMed:27122470};
DE   AltName: Full=Gamma-tocopherol-like methyltransferase ANMT {ECO:0000312|EMBL:AHH02777.1};
GN   Name=ANMT {ECO:0000303|PubMed:27122470};
GN   Synonyms=Rs820 {ECO:0000312|EMBL:AHH02777.1};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
DE   RecName: Full=Ajmaline N-methyltransferase {ECO:0000303|PubMed:27122470};
DE            Short=RsANMT {ECO:0000303|PubMed:27122470};
DE            EC=2.1.1.393 {ECO:0000269|PubMed:27122470};
DE   AltName: Full=Gamma-tocopherol-like methyltransferase ANMT {ECO:0000312|EMBL:AHH02777.1};
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-
CC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:79631,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58567,
CC         ChEBI:CHEBI:59789, ChEBI:CHEBI:230509; EC=2.1.1.393;
CC         Evidence={ECO:0000269|PubMed:27122470};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79632;
CC         Evidence={ECO:0000269|PubMed:27122470};
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 50-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline +
CC         S-adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:79627,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:77618, ChEBI:CHEBI:230510; EC=2.1.1.393;
CC         Evidence={ECO:0000269|PubMed:27122470};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79628;
CC         Evidence={ECO:0000269|PubMed:27122470};
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 153. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
