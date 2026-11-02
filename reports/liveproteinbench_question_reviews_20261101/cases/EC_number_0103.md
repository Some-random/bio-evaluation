# EC_number_0103

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.2.3.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAQEMRYFSTRGGKETLSFEDAVLTGLAPNGGLYIPTHIPALPKDWKTKWAGLSFPELSHEILSLFVPTSVIPSDDLQSIINTAYSSFRSPATTPIRQTGDNEYVLELWHGPTWAFKDVALQFLGELFRYFLERRNKDKTEDMEELTVVGATSGDTGSAAIYGLRSKPSITIFILYPDGRVSPIQEAQMATVPDANVYCVAVEDSDFDTCQSIVKTLFSDAQFNATHRLGAINSINWARILAQIVYYFSAYFQLPEEARKDGAKLQFVVPTGNFGDILAGWYAKKLGLPMEQLVVATNENDILERFFRTGRYEADDAVQQDQTAETAAVNGSSDGQQAVSAVKATHSPAMDILLSSNFERLLYYLALETNGTEGSDEEKRFKAQERLNDWMSTLKKDGKVDLGEDVRQAAGKDFWAERVSDGQTLEEIQKYYRREKYGPYVVDPHTAVGLTAQERSAKKASPDTTWITLSTAHPAKFSGAVELALSASEFPDFDFRRDVLPDELKKLEGLEKRVHRVKGEEGVRALIEKVKSASHEKVDAEEGRGSL

[Multiple Choices]
A. 4.2.3.5
B. 4.2.1.9
C. 4.2.3.1
D. 4.2.1.183
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

> The supplied sequence exactly matches the UniProt sequence annotated as threonine synthase, EC 4.2.3.1, catalyzing conversion of O-phospho-L-homoserine to L-threonine. The annotation is supported by transfer from UniProtKB:P16120 (ECO:0000250), so it is not direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a clear general biological argument for identifying the precise reaction and EC subtype; recognizing the enzyme family or exact protein would rely on protein-specific knowledge.


**Missing item-specific fact**

> That this sequence is annotated as threonine synthase, catalyzing O-phospho-L-homoserine to L-threonine, with EC 4.2.3.1.


**Reason**

> The key is supported by a sequence-matched annotation, but the annotation is an external protein-specific fact absent from the question. A predictor might infer the function from sequence, but that does not supply a concrete reasoning basis available from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation and specified catalytic reaction support one listed EC number; no evidence here supports another option.


### Important caveats

- The EC assignment for the matched protein is transferred by similarity from UniProtKB:P16120, rather than shown here as an experimental determination for this exact protein.
- The historical and current records match the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a clear general biological argument for identifying the precise reaction and EC subtype; recognizing the enzyme family or exact protein would rely on protein-specific knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence is annotated as threonine synthase, catalyzing O-phospho-L-homoserine to L-threonine, with EC 4.2.3.1.",
    "reason": "The key is supported by a sequence-matched annotation, but the annotation is an external protein-specific fact absent from the question. A predictor might infer the function from sequence, but that does not supply a concrete reasoning basis available from the provided input."
  },
  "case_id": "EC_number_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as threonine synthase, EC 4.2.3.1, catalyzing conversion of O-phospho-L-homoserine to L-threonine. The annotation is supported by transfer from UniProtKB:P16120 (ECO:0000250), so it is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The EC assignment for the matched protein is transferred by similarity from UniProtKB:P16120, rather than shown here as an experimental determination for this exact protein.",
    "The historical and current records match the supplied sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and specified catalytic reaction support one listed EC number; no evidence here supports another option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as threonine synthase, EC 4.2.3.1, catalyzing conversion of O-phospho-L-homoserine to L-threonine. The annotation is supported by transfer from UniProtKB:P16120 (ECO:0000250), so it is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a clear general biological argument for identifying the precise reaction and EC subtype; recognizing the enzyme family or exact protein would rely on protein-specific knowledge.",
    "missing_item_specific_fact": "That this sequence is annotated as threonine synthase, catalyzing O-phospho-L-homoserine to L-threonine, with EC 4.2.3.1.",
    "reason": "The key is supported by a sequence-matched annotation, but the annotation is an external protein-specific fact absent from the question. A predictor might infer the function from sequence, but that does not supply a concrete reasoning basis available from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and specified catalytic reaction support one listed EC number; no evidence here supports another option."
  },
  "important_caveats": [
    "The EC assignment for the matched protein is transferred by similarity from UniProtKB:P16120, rather than shown here as an experimental determination for this exact protein.",
    "The historical and current records match the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt entry J9VI85 (THRC_CRYN9, 547 AA, Cryptococcus neoformans), which is annotated as Threonine synthase with EC 4.2.3.1. The catalytic reaction (O-phospho-L-homoserine + H2O = L-threonine + phosphate) is confirmed. The EC assignment carries evidence code ECO:0000250 (transferred by similarity to UniProtKB:P16120), meaning it is computational/similarity-based rather than directly experimentally validated for this specific fungal protein, though a supporting publication (PubMed:18757810) on threonine biosynthetic genes in C. neoformans provides biological context.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A partial reasoning argument exists: threonine synthase (4.2.3.1) is a PLP-dependent enzyme (fold-type II), whereas fumarase (4.2.1.9) and HMG-CoA lyase (4.2.3.5) are not PLP-dependent. Identifying PLP-binding motifs (e.g., a conserved active-site lysine forming a Schiff base) in the sequence could help eliminate non-PLP options. However, distinguishing 4.2.3.1 from 4.2.3.5 (both in the 4.2.3.x phospho-oxygen lyase subclass) or from 4.2.1.183 requires knowing the specific substrate specificity encoded in the sequence, which is not reliably derivable from general biological reasoning alone.


**Missing item-specific fact**

> The specific substrate-binding and catalytic-site residues that uniquely encode O-phospho-L-homoserine lyase activity (as opposed to other 4.2.3.x or 4.2.1.x activities) are not identifiable from the raw sequence without alignment to characterized threonine synthases or database lookup. Additionally, the identity and PLP-dependence of EC 4.2.1.183 is an obscure item-specific fact needed to fully eliminate that distractor.


**Reason**

> While recognizing general PLP-dependent enzyme architecture provides a partial narrowing argument, the final distinction between EC 4.2.3.1 and the other 4.2.x.x options depends on knowing which specific enzymes in this EC family are PLP-dependent and what their substrates are — knowledge that is essentially database-level annotation rather than derivable from the sequence through general biological reasoning. The EC assignment itself is transferred by similarity (ECO:0000250), underscoring its lookup nature.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options span distinct EC subclasses (4.2.1.x vs 4.2.3.x) and different enzyme families, so only one (C, 4.2.3.1) matches the annotated threonine synthase. The distractors represent mechanistically different enzymes (fumarase, HMG-CoA lyase, and an obscure hydro-lyase), making them defensibly incorrect even if the reasoning path to the correct answer is difficult.


### Important caveats

- The EC 4.2.3.1 annotation is transferred by similarity (ECO:0000250 from P16120), not directly experimentally verified for this specific C. neoformans protein.
- The UniProt entry was first publicly released in February 2025; the author's source snapshot date is unknown, so the annotation may not have existed at benchmark construction time.
- EC 4.2.1.183 is an obscure entry whose identity and mechanistic class are not easily recalled, reducing the ability to reason it away.
- The sequence is 547 AA, consistent with fungal threonine synthases (longer than bacterial ~420-450 AA forms), but this length alone does not uniquely identify the enzyme.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A partial reasoning argument exists: threonine synthase (4.2.3.1) is a PLP-dependent enzyme (fold-type II), whereas fumarase (4.2.1.9) and HMG-CoA lyase (4.2.3.5) are not PLP-dependent. Identifying PLP-binding motifs (e.g., a conserved active-site lysine forming a Schiff base) in the sequence could help eliminate non-PLP options. However, distinguishing 4.2.3.1 from 4.2.3.5 (both in the 4.2.3.x phospho-oxygen lyase subclass) or from 4.2.1.183 requires knowing the specific substrate specificity encoded in the sequence, which is not reliably derivable from general biological reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate-binding and catalytic-site residues that uniquely encode O-phospho-L-homoserine lyase activity (as opposed to other 4.2.3.x or 4.2.1.x activities) are not identifiable from the raw sequence without alignment to characterized threonine synthases or database lookup. Additionally, the identity and PLP-dependence of EC 4.2.1.183 is an obscure item-specific fact needed to fully eliminate that distractor.",
    "reason": "While recognizing general PLP-dependent enzyme architecture provides a partial narrowing argument, the final distinction between EC 4.2.3.1 and the other 4.2.x.x options depends on knowing which specific enzymes in this EC family are PLP-dependent and what their substrates are — knowledge that is essentially database-level annotation rather than derivable from the sequence through general biological reasoning. The EC assignment itself is transferred by similarity (ECO:0000250), underscoring its lookup nature."
  },
  "case_id": "EC_number_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry J9VI85 (THRC_CRYN9, 547 AA, Cryptococcus neoformans), which is annotated as Threonine synthase with EC 4.2.3.1. The catalytic reaction (O-phospho-L-homoserine + H2O = L-threonine + phosphate) is confirmed. The EC assignment carries evidence code ECO:0000250 (transferred by similarity to UniProtKB:P16120), meaning it is computational/similarity-based rather than directly experimentally validated for this specific fungal protein, though a supporting publication (PubMed:18757810) on threonine biosynthetic genes in C. neoformans provides biological context."
  },
  "important_caveats": [
    "The EC 4.2.3.1 annotation is transferred by similarity (ECO:0000250 from P16120), not directly experimentally verified for this specific C. neoformans protein.",
    "The UniProt entry was first publicly released in February 2025; the author's source snapshot date is unknown, so the annotation may not have existed at benchmark construction time.",
    "EC 4.2.1.183 is an obscure entry whose identity and mechanistic class are not easily recalled, reducing the ability to reason it away.",
    "The sequence is 547 AA, consistent with fungal threonine synthases (longer than bacterial ~420-450 AA forms), but this length alone does not uniquely identify the enzyme."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options span distinct EC subclasses (4.2.1.x vs 4.2.3.x) and different enzyme families, so only one (C, 4.2.3.1) matches the annotated threonine synthase. The distractors represent mechanistically different enzymes (fumarase, HMG-CoA lyase, and an obscure hydro-lyase), making them defensibly incorrect even if the reasoning path to the correct answer is difficult."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry J9VI85 (THRC_CRYN9, 547 AA, Cryptococcus neoformans), which is annotated as Threonine synthase with EC 4.2.3.1. The catalytic reaction (O-phospho-L-homoserine + H2O = L-threonine + phosphate) is confirmed. The EC assignment carries evidence code ECO:0000250 (transferred by similarity to UniProtKB:P16120), meaning it is computational/similarity-based rather than directly experimentally validated for this specific fungal protein, though a supporting publication (PubMed:18757810) on threonine biosynthetic genes in C. neoformans provides biological context.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A partial reasoning argument exists: threonine synthase (4.2.3.1) is a PLP-dependent enzyme (fold-type II), whereas fumarase (4.2.1.9) and HMG-CoA lyase (4.2.3.5) are not PLP-dependent. Identifying PLP-binding motifs (e.g., a conserved active-site lysine forming a Schiff base) in the sequence could help eliminate non-PLP options. However, distinguishing 4.2.3.1 from 4.2.3.5 (both in the 4.2.3.x phospho-oxygen lyase subclass) or from 4.2.1.183 requires knowing the specific substrate specificity encoded in the sequence, which is not reliably derivable from general biological reasoning alone.",
    "missing_item_specific_fact": "The specific substrate-binding and catalytic-site residues that uniquely encode O-phospho-L-homoserine lyase activity (as opposed to other 4.2.3.x or 4.2.1.x activities) are not identifiable from the raw sequence without alignment to characterized threonine synthases or database lookup. Additionally, the identity and PLP-dependence of EC 4.2.1.183 is an obscure item-specific fact needed to fully eliminate that distractor.",
    "reason": "While recognizing general PLP-dependent enzyme architecture provides a partial narrowing argument, the final distinction between EC 4.2.3.1 and the other 4.2.x.x options depends on knowing which specific enzymes in this EC family are PLP-dependent and what their substrates are — knowledge that is essentially database-level annotation rather than derivable from the sequence through general biological reasoning. The EC assignment itself is transferred by similarity (ECO:0000250), underscoring its lookup nature."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options span distinct EC subclasses (4.2.1.x vs 4.2.3.x) and different enzyme families, so only one (C, 4.2.3.1) matches the annotated threonine synthase. The distractors represent mechanistically different enzymes (fumarase, HMG-CoA lyase, and an obscure hydro-lyase), making them defensibly incorrect even if the reasoning path to the correct answer is difficult."
  },
  "important_caveats": [
    "The EC 4.2.3.1 annotation is transferred by similarity (ECO:0000250 from P16120), not directly experimentally verified for this specific C. neoformans protein.",
    "The UniProt entry was first publicly released in February 2025; the author's source snapshot date is unknown, so the annotation may not have existed at benchmark construction time.",
    "EC 4.2.1.183 is an obscure entry whose identity and mechanistic class are not easily recalled, reducing the ability to reason it away.",
    "The sequence is 547 AA, consistent with fungal threonine synthases (longer than bacterial ~420-450 AA forms), but this length alone does not uniquely identify the enzyme."
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

**Accession:** `J9VI85` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 52. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.629626+00:00.  

```json
"J9VI85"
```

Source SHA-256: `056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.629626+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P16120","source":"UniProtKB"}],"value":"4.2.3.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Threonine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"TS"}]}}
```

Source SHA-256: `056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.629626+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P16120","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:10841"}}],"reaction":{"ecNumber":"4.2.3.1","evidences":[{"evidenceCode":"ECO:0000250","id":"P16120","source":"UniProtKB"}],"name":"O-phospho-L-homoserine + H2O = L-threonine + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:10840"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57590"},{"database":"ChEBI","id":"CHEBI:57926"}]}}
```

Source SHA-256: `056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 52 / 1.  
**Retrieved:** 2026-11-02T04:28:56.836361+00:00.  

```text
ID   THRC_CRYN9              Reviewed;         547 AA.
AC   J9VI85; B2MW84;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-NOV-2012, sequence version 1.
DT   28-JAN-2026, entry version 52.
DE   RecName: Full=Threonine synthase {ECO:0000305};
DE            Short=TS {ECO:0000305};
DE            EC=4.2.3.1 {ECO:0000250|UniProtKB:P16120};
GN   Name=THR4 {ECO:0000303|PubMed:18757810};
GN   ORFNames=CNAG_03612 {ECO:0000312|EMBL:AFR93116.1};
OS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)
OS   (Cryptococcus neoformans var. grubii serotype A).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=235443 {ECO:0000312|EMBL:AFR93116.1, ECO:0000312|Proteomes:UP000010091};
```

Source SHA-256: `5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 52 / 1.  
**Retrieved:** 2026-11-02T04:28:56.836361+00:00.  

```text
DE   RecName: Full=Threonine synthase {ECO:0000305};
DE            Short=TS {ECO:0000305};
DE            EC=4.2.3.1 {ECO:0000250|UniProtKB:P16120};
```

Source SHA-256: `5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)  
**Locator:** `lines 17-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 52 / 1.  
**Retrieved:** 2026-11-02T04:28:56.836361+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:ACC94295.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, AND PATHWAY.
RC   STRAIN=H99 / ATCC 208821 / CBS 10515 / FGSC 9487
RC   {ECO:0000303|PubMed:18757810};
RX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;
RA   Kingsbury J.M., McCusker J.H.;
RT   "Threonine biosynthetic genes are essential in Cryptococcus neoformans.";
RL   Microbiology 154:2767-2775(2008).
```

Source SHA-256: `5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)  
**Locator:** `lines 47-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 52 / 1.  
**Retrieved:** 2026-11-02T04:28:56.836361+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-homoserine + H2O = L-threonine + phosphate;
CC         Xref=Rhea:RHEA:10840, ChEBI:CHEBI:15377, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:57590, ChEBI:CHEBI:57926; EC=4.2.3.1;
CC         Evidence={ECO:0000250|UniProtKB:P16120};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:10841;
CC         Evidence={ECO:0000250|UniProtKB:P16120};
```

Source SHA-256: `5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 103. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
