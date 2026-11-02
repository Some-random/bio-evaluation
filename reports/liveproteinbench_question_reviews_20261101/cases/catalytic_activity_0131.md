# catalytic_activity_0131

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVIAVIPARSGSKGIKNKNLVLLNNQPLIYYTIKAALNSKCISKVLVSSDSEEILSYAKSQNVDILKRPIELAQDDTTSDKVLLHALEFYKDYEDVIFLQPTSPLRTNIHIDEAFKIYKNSDANALISVTECDNKILKAFICDNKGDLKGICDDEYPFMPRQKLPKTYMSNGAIYILSIKDFLNKPSFLQSKTKYFLMNKISSLDIDNLEDLKQVENIQKMKGCVVWISGLAGAGKTTISSGLYKKLKEKYNNSVLLDGDELRKIFKHTGYTREERLESAKKISSLCSFLAKNDIIVICATISLFEEIYLLNRNTIENYFEVFVDCPMEELILRDQKGLYSGALKGEIKDVVGVDIKYAKPNAHYIIDNSSKTDLEKKINNLYNEVELFFNKER

[Multiple Choices]
A. a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol
B. (2S)-3-(4-methoxyphenyl)-2-[(3S)-3-(methylamino)-8-oxo-1-azaspiro[4.5]decan-1-yl]propanal = (1S,3S,6S,7S,8R)-7-hydroxy-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecan-9-one
C. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
D. an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied 394-residue sequence exactly matches the UniProt sequence annotated with reaction D. The annotation cites experimental evidence (ECO:0000269) for the N-acylneuraminate + CTP reaction, including its N-acetylneuraminate-specific form. This supports the key, while remaining an annotation tied to the cited study rather than an independent review of the experiment.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The reaction choices describe distinct enzyme activities, but the sequence and prompt provide no biological context or substrate information that identifies which activity this protein has. Generic sequence inspection does not establish the specific N-acylneuraminate substrate and CTP-dependent product.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence that this sequence encodes an N-acylneuraminate cytidylyltransferase.


**Reason**

> The key is supported by reviewer-only evidence, but that annotation and its cited experimental basis were not supplied to the evaluated model. Selecting D therefore depends on an external protein-specific fact, not merely on recognizing a general biochemical pattern.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports D, and the alternatives describe different reactions; no evidence makes another listed option defensible for this sequence.


### Important caveats

- The current and retrieved historical UniProt records both match the supplied sequence, but the author's exact source snapshot is unknown.
- The cited experimental evidence is reported in the database annotation; the underlying study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The reaction choices describe distinct enzyme activities, but the sequence and prompt provide no biological context or substrate information that identifies which activity this protein has. Generic sequence inspection does not establish the specific N-acylneuraminate substrate and CTP-dependent product.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence that this sequence encodes an N-acylneuraminate cytidylyltransferase.",
    "reason": "The key is supported by reviewer-only evidence, but that annotation and its cited experimental basis were not supplied to the evaluated model. Selecting D therefore depends on an external protein-specific fact, not merely on recognizing a general biochemical pattern."
  },
  "case_id": "catalytic_activity_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied 394-residue sequence exactly matches the UniProt sequence annotated with reaction D. The annotation cites experimental evidence (ECO:0000269) for the N-acylneuraminate + CTP reaction, including its N-acetylneuraminate-specific form. This supports the key, while remaining an annotation tied to the cited study rather than an independent review of the experiment."
  },
  "important_caveats": [
    "The current and retrieved historical UniProt records both match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited experimental evidence is reported in the database annotation; the underlying study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D, and the alternatives describe different reactions; no evidence makes another listed option defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 394-residue sequence exactly matches the UniProt sequence annotated with reaction D. The annotation cites experimental evidence (ECO:0000269) for the N-acylneuraminate + CTP reaction, including its N-acetylneuraminate-specific form. This supports the key, while remaining an annotation tied to the cited study rather than an independent review of the experiment.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The reaction choices describe distinct enzyme activities, but the sequence and prompt provide no biological context or substrate information that identifies which activity this protein has. Generic sequence inspection does not establish the specific N-acylneuraminate substrate and CTP-dependent product.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence that this sequence encodes an N-acylneuraminate cytidylyltransferase.",
    "reason": "The key is supported by reviewer-only evidence, but that annotation and its cited experimental basis were not supplied to the evaluated model. Selecting D therefore depends on an external protein-specific fact, not merely on recognizing a general biochemical pattern."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D, and the alternatives describe different reactions; no evidence makes another listed option defensible for this sequence."
  },
  "important_caveats": [
    "The current and retrieved historical UniProt records both match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited experimental evidence is reported in the database annotation; the underlying study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence (394 AA, SHA256 match) corresponds to UniProt P0DY07, N-acylneuraminate cytidylyltransferase (EC 2.7.7.43) from Campylobacter jejuni. The UniProt entry explicitly annotates the catalytic activity as 'an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate' with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). This matches option D verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold nucleotide-binding motif (GLAGAGKTT, ~residues 200-210), characteristic of the NTP transferase superfamily. Among the four options, only D involves a nucleotide substrate (CTP) and a cytidylyltransferase mechanism. Option A is a glycosidase (hydrolase, no nucleotide), B is an intramolecular cyclization of a complex spiro/azatricyclic compound (no nucleotide), and C is a dehydratase (dihydroxy-acid dehydratase, no nucleotide). The presence of a Rossmann-like nucleotide-binding motif provides a concrete structural argument favoring a nucleotide-dependent transferase reaction, which uniquely matches D among the choices.


**Missing item-specific fact**

> The specific acceptor substrate identity (N-acylneuraminate) and the particular NTP (CTP rather than UTP, ATP, etc.) cannot be determined from the fold alone; this requires knowledge of the CMP-Neu5Ac synthase family's substrate specificity. However, among the four given options, only D involves any nucleotide, so the fold-based argument is sufficient to select D over A, B, and C.


**Reason**

> The Rossmann-like motif is a recognizable, generalizable feature indicating nucleotide binding. Since only one option (D) involves a nucleotide substrate, this structural inference meaningfully discriminates the answer without requiring memorization of this specific protein's annotation. The specific substrate name (N-acylneuraminate) is not derivable from the fold, but the question's option set makes that detail unnecessary for correct selection.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe reactions (glycoside hydrolysis, intramolecular cyclization, dehydratase) that are mechanistically and structurally inconsistent with a protein bearing a Rossmann-fold nucleotide-binding motif. Only D is compatible with a nucleotide transferase fold. No ambiguity among the choices.


### Important caveats

- The Rossmann-fold motif supports nucleotide involvement but does not uniquely identify CTP as the specific NTP or N-acylneuraminate as the acceptor; the question's option set compensates by making D the only nucleotide-involving choice.
- The UniProt annotation is supported by experimental evidence (PubMed:38382015, Ghosh & Raushel 2024), not merely computational prediction.
- The sequence match is exact (same length, same SHA256) between the benchmark input and UniProt P0DY07 sequence version 1.
- Option B describes an extraordinarily complex intramolecular rearrangement that is not a typical enzymatic reaction for a 394-residue protein and serves as an implausible distractor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold nucleotide-binding motif (GLAGAGKTT, ~residues 200-210), characteristic of the NTP transferase superfamily. Among the four options, only D involves a nucleotide substrate (CTP) and a cytidylyltransferase mechanism. Option A is a glycosidase (hydrolase, no nucleotide), B is an intramolecular cyclization of a complex spiro/azatricyclic compound (no nucleotide), and C is a dehydratase (dihydroxy-acid dehydratase, no nucleotide). The presence of a Rossmann-like nucleotide-binding motif provides a concrete structural argument favoring a nucleotide-dependent transferase reaction, which uniquely matches D among the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific acceptor substrate identity (N-acylneuraminate) and the particular NTP (CTP rather than UTP, ATP, etc.) cannot be determined from the fold alone; this requires knowledge of the CMP-Neu5Ac synthase family's substrate specificity. However, among the four given options, only D involves any nucleotide, so the fold-based argument is sufficient to select D over A, B, and C.",
    "reason": "The Rossmann-like motif is a recognizable, generalizable feature indicating nucleotide binding. Since only one option (D) involves a nucleotide substrate, this structural inference meaningfully discriminates the answer without requiring memorization of this specific protein's annotation. The specific substrate name (N-acylneuraminate) is not derivable from the fold, but the question's option set makes that detail unnecessary for correct selection."
  },
  "case_id": "catalytic_activity_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The protein sequence (394 AA, SHA256 match) corresponds to UniProt P0DY07, N-acylneuraminate cytidylyltransferase (EC 2.7.7.43) from Campylobacter jejuni. The UniProt entry explicitly annotates the catalytic activity as 'an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate' with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). This matches option D verbatim."
  },
  "important_caveats": [
    "The Rossmann-fold motif supports nucleotide involvement but does not uniquely identify CTP as the specific NTP or N-acylneuraminate as the acceptor; the question's option set compensates by making D the only nucleotide-involving choice.",
    "The UniProt annotation is supported by experimental evidence (PubMed:38382015, Ghosh & Raushel 2024), not merely computational prediction.",
    "The sequence match is exact (same length, same SHA256) between the benchmark input and UniProt P0DY07 sequence version 1.",
    "Option B describes an extraordinarily complex intramolecular rearrangement that is not a typical enzymatic reaction for a 394-residue protein and serves as an implausible distractor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe reactions (glycoside hydrolysis, intramolecular cyclization, dehydratase) that are mechanistically and structurally inconsistent with a protein bearing a Rossmann-fold nucleotide-binding motif. Only D is compatible with a nucleotide transferase fold. No ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence (394 AA, SHA256 match) corresponds to UniProt P0DY07, N-acylneuraminate cytidylyltransferase (EC 2.7.7.43) from Campylobacter jejuni. The UniProt entry explicitly annotates the catalytic activity as 'an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate' with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). This matches option D verbatim.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold nucleotide-binding motif (GLAGAGKTT, ~residues 200-210), characteristic of the NTP transferase superfamily. Among the four options, only D involves a nucleotide substrate (CTP) and a cytidylyltransferase mechanism. Option A is a glycosidase (hydrolase, no nucleotide), B is an intramolecular cyclization of a complex spiro/azatricyclic compound (no nucleotide), and C is a dehydratase (dihydroxy-acid dehydratase, no nucleotide). The presence of a Rossmann-like nucleotide-binding motif provides a concrete structural argument favoring a nucleotide-dependent transferase reaction, which uniquely matches D among the choices.",
    "missing_item_specific_fact": "The specific acceptor substrate identity (N-acylneuraminate) and the particular NTP (CTP rather than UTP, ATP, etc.) cannot be determined from the fold alone; this requires knowledge of the CMP-Neu5Ac synthase family's substrate specificity. However, among the four given options, only D involves any nucleotide, so the fold-based argument is sufficient to select D over A, B, and C.",
    "reason": "The Rossmann-like motif is a recognizable, generalizable feature indicating nucleotide binding. Since only one option (D) involves a nucleotide substrate, this structural inference meaningfully discriminates the answer without requiring memorization of this specific protein's annotation. The specific substrate name (N-acylneuraminate) is not derivable from the fold, but the question's option set makes that detail unnecessary for correct selection."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe reactions (glycoside hydrolysis, intramolecular cyclization, dehydratase) that are mechanistically and structurally inconsistent with a protein bearing a Rossmann-fold nucleotide-binding motif. Only D is compatible with a nucleotide transferase fold. No ambiguity among the choices."
  },
  "important_caveats": [
    "The Rossmann-fold motif supports nucleotide involvement but does not uniquely identify CTP as the specific NTP or N-acylneuraminate as the acceptor; the question's option set compensates by making D the only nucleotide-involving choice.",
    "The UniProt annotation is supported by experimental evidence (PubMed:38382015, Ghosh & Raushel 2024), not merely computational prediction.",
    "The sequence match is exact (same length, same SHA256) between the benchmark input and UniProt P0DY07 sequence version 1.",
    "Option B describes an extraordinarily complex intramolecular rearrangement that is not a typical enzymatic reaction for a 394-residue protein and serves as an implausible distractor."
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

**Accession:** `P0DY07` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"CMP-N-acetylneuraminate synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"CMP-Neu5Ac synthase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"2.7.7.43"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"N-acylneuraminate cytidylyltransferase"}}}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:11345"}}],"reaction":{"ecNumber":"2.7.7.43","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:11344"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:37563"},{"database":"ChEBI","id":"CHEBI:60073"},{"database":"ChEBI","id":"CHEBI:68671"}]}}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:17.113205+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:80844"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"N-acetylneuraminate + CTP = CMP-N-acetyl-beta-neuraminate + diphosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80843"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:35418"},{"database":"ChEBI","id":"CHEBI:37563"},{"database":"ChEBI","id":"CHEBI:57812"}]}}
```

Source SHA-256: `b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
DE   RecName: Full=N-acylneuraminate cytidylyltransferase {ECO:0000305};
DE            EC=2.7.7.43 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=CMP-N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};
DE            Short=CMP-Neu5Ac synthase {ECO:0000303|PubMed:38382015};
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate +
CC         diphosphate; Xref=Rhea:RHEA:11344, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:37563, ChEBI:CHEBI:60073, ChEBI:CHEBI:68671; EC=2.7.7.43;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:11345;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)  
**Locator:** `lines 47-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:24.379520+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-acetylneuraminate + CTP = CMP-N-acetyl-beta-neuraminate +
CC         diphosphate; Xref=Rhea:RHEA:80843, ChEBI:CHEBI:33019,
CC         ChEBI:CHEBI:35418, ChEBI:CHEBI:37563, ChEBI:CHEBI:57812;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80844;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
