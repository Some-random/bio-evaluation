# GO_biological_process_0175

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — threonine biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPARKYKIHVPCTSANIGPGFDVCGIALSLSLSLVVTIPSVSSGAEPLPKIIYTGLDSDNVPLSPYKNLLTRVALYVLRANGITTFPPGVTIEARNEIPFGRGLGSSGAAVIAGVLLGDLLGNLSLPKSRLLDFALMVERHPDNVTAALMGGFVGSYLRELSPEDMSAASIPLAEVLPEYPPDAGPDWGKSPPQPPHGIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARSPPDPDLIYDAMGDRVHQPYRMTLIPGLPKILSTLTPTSHPGLLGICLSGAGPTILALATHNFEAIANEIERIFGDEQVLVDHKVLNIDEKGSWVEDITEA

[Multiple Choices]
A. threonine biosynthetic process
B. pre-miRNA processing
C. positive regulation of transcription elongation by RNA polymerase II
D. oligopeptide export from mitochondrion
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as homoserine kinase, which commits homoserine to threonine biosynthesis. The cited function and pathway annotations carry experimental evidence, and the matching GO annotation is for threonine biosynthesis.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a globular enzyme rather than an obvious RNA-processing factor or mitochondrial oligopeptide transporter, but that does not establish its specific role in threonine biosynthesis.


**Missing item-specific fact**

> Identifying this particular sequence as homoserine kinase, and knowing that it catalyzes a step in threonine biosynthesis.


**Reason**

> The supplied sequence does not provide an explicit organism, protein identity, or pathway context. Choosing A requires sequence-family identification or an external protein-specific annotation; generic sequence features do not distinguish the precise biological process.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched evidence supports A; the other choices describe processes unrelated to the annotated function.


### Important caveats

- The reviewer-only UniProt evidence identifies the sequence and supports the expected answer, but was not available to the evaluated model.
- The cited experimental support is reported in the database annotation; the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a globular enzyme rather than an obvious RNA-processing factor or mitochondrial oligopeptide transporter, but that does not establish its specific role in threonine biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this particular sequence as homoserine kinase, and knowing that it catalyzes a step in threonine biosynthesis.",
    "reason": "The supplied sequence does not provide an explicit organism, protein identity, or pathway context. Choosing A requires sequence-family identification or an external protein-specific annotation; generic sequence features do not distinguish the precise biological process."
  },
  "case_id": "GO_biological_process_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as homoserine kinase, which commits homoserine to threonine biosynthesis. The cited function and pathway annotations carry experimental evidence, and the matching GO annotation is for threonine biosynthesis."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence identifies the sequence and supports the expected answer, but was not available to the evaluated model.",
    "The cited experimental support is reported in the database annotation; the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched evidence supports A; the other choices describe processes unrelated to the annotated function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as homoserine kinase, which commits homoserine to threonine biosynthesis. The cited function and pathway annotations carry experimental evidence, and the matching GO annotation is for threonine biosynthesis.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a globular enzyme rather than an obvious RNA-processing factor or mitochondrial oligopeptide transporter, but that does not establish its specific role in threonine biosynthesis.",
    "missing_item_specific_fact": "Identifying this particular sequence as homoserine kinase, and knowing that it catalyzes a step in threonine biosynthesis.",
    "reason": "The supplied sequence does not provide an explicit organism, protein identity, or pathway context. Choosing A requires sequence-family identification or an external protein-specific annotation; generic sequence features do not distinguish the precise biological process."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched evidence supports A; the other choices describe processes unrelated to the annotated function."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence identifies the sequence and supports the expected answer, but was not available to the evaluated model.",
    "The cited experimental support is reported in the database annotation; the primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (SHA256-matched to UniProt J9VU26, KHSE_CRYN9) is annotated as Homoserine kinase (EC 2.7.1.39), gene name THR1, from Cryptococcus neoformans. Experimental evidence (PubMed:18757810, disruption phenotype, ECO:0000269) confirms it 'commits homoserine to the threonine biosynthesis pathway by catalyzing its O-phosphorylation' and places it in 'L-threonine from L-aspartate: step 4/5.' The GO annotation GO:0009088 (P:threonine biosynthetic process) carries IMP evidence code. The expected answer A is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark GHMP kinase family motifs: the glycine-rich loop 'GLGSSG' (residues ~101-106: 'PFGRGLGSSGAA') and the conserved 'GIGHF' motif (residues ~175-179: 'GIGHFVRFG'). These identify the protein as a small-molecule kinase of the GHMP (Galactokinase/Homoserine kinase/Mevalonate kinase/Phosphomevalonate kinase) superfamily. Among the four options, only A (threonine biosynthetic process) involves a kinase-mediated phosphorylation step. Option B (pre-miRNA processing) requires RNase III-type enzymes (Drosha/Dicer) with characteristic ribonuclease domains absent here. Option C (transcription elongation regulation) requires transcription factors or elongation factors with entirely different folds. Option D (oligopeptide export from mitochondrion) requires membrane-spanning ABC transporters or similar export machinery. Identifying the protein as a kinase eliminates B, C, and D, leaving A as the only option consistent with a phosphoryl-transfer enzyme acting on a small metabolite in a biosynthetic pathway.


**Missing item-specific fact**

> None critical. While distinguishing homoserine kinase specifically from other GHMP kinases (galactokinase, mevalonate kinase) from sequence alone is non-trivial, the question's distractors do not include competing kinase pathways, so the reasoning only requires identifying the protein as a kinase involved in biosynthesis.


**Reason**

> A model with general knowledge of protein domain architecture can recognize GHMP kinase motifs in the sequence and eliminate the three non-kinase distractors through domain-based reasoning. The biological argument is concrete: kinase motifs present → kinase function → only option A involves kinase-mediated biosynthesis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span completely different protein functional classes (kinase vs. RNase vs. transcription factor vs. transporter). The presence of GHMP kinase motifs unambiguously points to a kinase-mediated biosynthetic process, making A the sole defensible answer. No other option is consistent with the observed sequence features.


### Important caveats

- The GHMP kinase identification relies on recognizing short conserved motifs (GLGSSG, GIGHF) in a 357-aa fungal sequence; a model lacking knowledge of this specific superfamily might struggle.
- The specific assignment to threonine (vs. galactose or mevalonate) biosynthesis within the GHMP family is not trivially derivable from sequence alone, but is moot here because no competing kinase pathway appears among the options.
- UniProt annotation evidence for the GO term is IMP (Inferred by Mutant Phenotype), i.e., experimental, lending high confidence to the key.
- The sequence match is confirmed (SHA256 identical) between the benchmark input and the UniProt entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark GHMP kinase family motifs: the glycine-rich loop 'GLGSSG' (residues ~101-106: 'PFGRGLGSSGAA') and the conserved 'GIGHF' motif (residues ~175-179: 'GIGHFVRFG'). These identify the protein as a small-molecule kinase of the GHMP (Galactokinase/Homoserine kinase/Mevalonate kinase/Phosphomevalonate kinase) superfamily. Among the four options, only A (threonine biosynthetic process) involves a kinase-mediated phosphorylation step. Option B (pre-miRNA processing) requires RNase III-type enzymes (Drosha/Dicer) with characteristic ribonuclease domains absent here. Option C (transcription elongation regulation) requires transcription factors or elongation factors with entirely different folds. Option D (oligopeptide export from mitochondrion) requires membrane-spanning ABC transporters or similar export machinery. Identifying the protein as a kinase eliminates B, C, and D, leaving A as the only option consistent with a phosphoryl-transfer enzyme acting on a small metabolite in a biosynthetic pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While distinguishing homoserine kinase specifically from other GHMP kinases (galactokinase, mevalonate kinase) from sequence alone is non-trivial, the question's distractors do not include competing kinase pathways, so the reasoning only requires identifying the protein as a kinase involved in biosynthesis.",
    "reason": "A model with general knowledge of protein domain architecture can recognize GHMP kinase motifs in the sequence and eliminate the three non-kinase distractors through domain-based reasoning. The biological argument is concrete: kinase motifs present → kinase function → only option A involves kinase-mediated biosynthesis."
  },
  "case_id": "GO_biological_process_0175",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence (SHA256-matched to UniProt J9VU26, KHSE_CRYN9) is annotated as Homoserine kinase (EC 2.7.1.39), gene name THR1, from Cryptococcus neoformans. Experimental evidence (PubMed:18757810, disruption phenotype, ECO:0000269) confirms it 'commits homoserine to the threonine biosynthesis pathway by catalyzing its O-phosphorylation' and places it in 'L-threonine from L-aspartate: step 4/5.' The GO annotation GO:0009088 (P:threonine biosynthetic process) carries IMP evidence code. The expected answer A is directly and experimentally supported."
  },
  "important_caveats": [
    "The GHMP kinase identification relies on recognizing short conserved motifs (GLGSSG, GIGHF) in a 357-aa fungal sequence; a model lacking knowledge of this specific superfamily might struggle.",
    "The specific assignment to threonine (vs. galactose or mevalonate) biosynthesis within the GHMP family is not trivially derivable from sequence alone, but is moot here because no competing kinase pathway appears among the options.",
    "UniProt annotation evidence for the GO term is IMP (Inferred by Mutant Phenotype), i.e., experimental, lending high confidence to the key.",
    "The sequence match is confirmed (SHA256 identical) between the benchmark input and the UniProt entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span completely different protein functional classes (kinase vs. RNase vs. transcription factor vs. transporter). The presence of GHMP kinase motifs unambiguously points to a kinase-mediated biosynthetic process, making A the sole defensible answer. No other option is consistent with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0175",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (SHA256-matched to UniProt J9VU26, KHSE_CRYN9) is annotated as Homoserine kinase (EC 2.7.1.39), gene name THR1, from Cryptococcus neoformans. Experimental evidence (PubMed:18757810, disruption phenotype, ECO:0000269) confirms it 'commits homoserine to the threonine biosynthesis pathway by catalyzing its O-phosphorylation' and places it in 'L-threonine from L-aspartate: step 4/5.' The GO annotation GO:0009088 (P:threonine biosynthetic process) carries IMP evidence code. The expected answer A is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark GHMP kinase family motifs: the glycine-rich loop 'GLGSSG' (residues ~101-106: 'PFGRGLGSSGAA') and the conserved 'GIGHF' motif (residues ~175-179: 'GIGHFVRFG'). These identify the protein as a small-molecule kinase of the GHMP (Galactokinase/Homoserine kinase/Mevalonate kinase/Phosphomevalonate kinase) superfamily. Among the four options, only A (threonine biosynthetic process) involves a kinase-mediated phosphorylation step. Option B (pre-miRNA processing) requires RNase III-type enzymes (Drosha/Dicer) with characteristic ribonuclease domains absent here. Option C (transcription elongation regulation) requires transcription factors or elongation factors with entirely different folds. Option D (oligopeptide export from mitochondrion) requires membrane-spanning ABC transporters or similar export machinery. Identifying the protein as a kinase eliminates B, C, and D, leaving A as the only option consistent with a phosphoryl-transfer enzyme acting on a small metabolite in a biosynthetic pathway.",
    "missing_item_specific_fact": "None critical. While distinguishing homoserine kinase specifically from other GHMP kinases (galactokinase, mevalonate kinase) from sequence alone is non-trivial, the question's distractors do not include competing kinase pathways, so the reasoning only requires identifying the protein as a kinase involved in biosynthesis.",
    "reason": "A model with general knowledge of protein domain architecture can recognize GHMP kinase motifs in the sequence and eliminate the three non-kinase distractors through domain-based reasoning. The biological argument is concrete: kinase motifs present → kinase function → only option A involves kinase-mediated biosynthesis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span completely different protein functional classes (kinase vs. RNase vs. transcription factor vs. transporter). The presence of GHMP kinase motifs unambiguously points to a kinase-mediated biosynthetic process, making A the sole defensible answer. No other option is consistent with the observed sequence features."
  },
  "important_caveats": [
    "The GHMP kinase identification relies on recognizing short conserved motifs (GLGSSG, GIGHF) in a 357-aa fungal sequence; a model lacking knowledge of this specific superfamily might struggle.",
    "The specific assignment to threonine (vs. galactose or mevalonate) biosynthesis within the GHMP family is not trivially derivable from sequence alone, but is moot here because no competing kinase pathway appears among the options.",
    "UniProt annotation evidence for the GO term is IMP (Inferred by Mutant Phenotype), i.e., experimental, lending high confidence to the key.",
    "The sequence match is confirmed (SHA256 identical) between the benchmark input and the UniProt entry."
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

**Accession:** `J9VU26` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
"J9VU26"
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P17423","source":"UniProtKB"}],"value":"2.7.1.39"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Homoserine kinase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HK"},{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HSK"}]}}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18757810","source":"PubMed"}],"value":"Commits homoserine to the threonine biosynthesis pathway by catalyzing its O-phosphorylation"}]}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18757810","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 4/5"}]}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000315","id":"18757810","source":"PubMed"}],"id":"GO:0009088","properties":[{"key":"GoTerm","value":"P:L-threonine biosynthetic process"},{"key":"GoEvidenceType","value":"IMP:UniProtKB"}]}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"citation":{"authors":["Kingsbury J.M.","McCusker J.H."],"citationCrossReferences":[{"database":"PubMed","id":"18757810"},{"database":"DOI","id":"10.1099/mic.0.2008/019729-0"}],"citationType":"journal article","firstPage":"2767","id":"18757810","journal":"Microbiology","lastPage":"2775","publicationDate":"2008","title":"Threonine biosynthetic genes are essential in Cryptococcus neoformans.","volume":"154"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ACC85591.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
ID   KHSE_CRYN9              Reviewed;         357 AA.
AC   J9VU26; B2MVI2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-NOV-2012, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Homoserine kinase {ECO:0000305};
DE            Short=HK {ECO:0000305};
DE            Short=HSK {ECO:0000305};
DE            EC=2.7.1.39 {ECO:0000250|UniProtKB:P17423};
GN   Name=THR1 {ECO:0000303|PubMed:18757810};
GN   ORFNames=CNAG_04156 {ECO:0000312|EMBL:AFR96886.1};
OS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)
OS   (Cryptococcus neoformans var. grubii serotype A).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 18-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:ACC85591.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.
RX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;
RA   Kingsbury J.M., McCusker J.H.;
RT   "Threonine biosynthetic genes are essential in Cryptococcus neoformans.";
RL   Microbiology 154:2767-2775(2008).
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 43-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
CC   -!- FUNCTION: Commits homoserine to the threonine biosynthesis pathway by
CC       catalyzing its O-phosphorylation. {ECO:0000269|PubMed:18757810}.
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 52-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine
CC       from L-aspartate: step 4/5. {ECO:0000269|PubMed:18757810}.
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 78-78`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
DR   GO; GO:0009088; P:threonine biosynthetic process; IMP:UniProtKB.
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 175. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
