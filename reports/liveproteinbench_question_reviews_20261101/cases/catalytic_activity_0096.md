# catalytic_activity_0096

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTQPCIISVAITGSLPRKRDNPAVPITVSEQVESTQAAFEAGATLVHLHVRNDDETPSSEPDRFARVLEGIRKHAPGIITQVSTGGRSGAGRERGGMLSLRPDMASLATGSVNFPTRVYDNPPDLVDWLAAEMKAYAIKPEIEAFDLSMIFQAVAMQQAGKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGGHCRTGLEDNVRLDKQTLAPSNAALVSQVAALCEEYGRPVATVAQARALLGLPSMEIDGRSPW

[Multiple Choices]
A. N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) + H(+)
B. 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA
C. L-phenylalanine = (E)-cinnamate + NH4(+)
D. K(+)(in) = K(+)(out)
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

> The supplied sequence exactly matches the cited UniProt entry, which assigns this enzyme the reaction in choice B and cites experimental evidence (ECO:0000269, PubMed:24240508). The primary paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C1](#evidence-c1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The input provides a sequence but no biological context or distinctive evidence that identifies this exact substrate-to-product transformation over the alternatives.


**Missing item-specific fact**

> The protein-specific catalytic activity, established by annotation or experimental characterization, is needed to select the 3-oxoadipate:acetyl-CoA reaction.


**Reason**

> The key is supported by reviewer-only evidence, but that evidence was not supplied to the evaluated model. The specific reaction cannot be confidently inferred from general biological knowledge alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence-specific annotation supports B; the other choices describe distinct reactions with no supplied evidence linking them to this protein.


### Important caveats

- The cited UniProt evidence assigns an experimental evidence code and references PubMed:24240508, but the primary paper was not independently validated.
- The current and historical UniProt records match the sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The input provides a sequence but no biological context or distinctive evidence that identifies this exact substrate-to-product transformation over the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity, established by annotation or experimental characterization, is needed to select the 3-oxoadipate:acetyl-CoA reaction.",
    "reason": "The key is supported by reviewer-only evidence, but that evidence was not supplied to the evaluated model. The specific reaction cannot be confidently inferred from general biological knowledge alone."
  },
  "case_id": "catalytic_activity_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited UniProt entry, which assigns this enzyme the reaction in choice B and cites experimental evidence (ECO:0000269, PubMed:24240508). The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The cited UniProt evidence assigns an experimental evidence code and references PubMed:24240508, but the primary paper was not independently validated.",
    "The current and historical UniProt records match the sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence-specific annotation supports B; the other choices describe distinct reactions with no supplied evidence linking them to this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited UniProt entry, which assigns this enzyme the reaction in choice B and cites experimental evidence (ECO:0000269, PubMed:24240508). The primary paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4", "C1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The input provides a sequence but no biological context or distinctive evidence that identifies this exact substrate-to-product transformation over the alternatives.",
    "missing_item_specific_fact": "The protein-specific catalytic activity, established by annotation or experimental characterization, is needed to select the 3-oxoadipate:acetyl-CoA reaction.",
    "reason": "The key is supported by reviewer-only evidence, but that evidence was not supplied to the evaluated model. The specific reaction cannot be confidently inferred from general biological knowledge alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence-specific annotation supports B; the other choices describe distinct reactions with no supplied evidence linking them to this protein."
  },
  "important_caveats": [
    "The cited UniProt evidence assigns an experimental evidence code and references PubMed:24240508, but the primary paper was not independently validated.",
    "The current and historical UniProt records match the sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 284-aa sequence matches UniProt Q0KAA1 (3OXCE_CUPNH, Cupriavidus necator) exactly. The reviewed Swiss-Prot entry annotates the catalytic activity as '3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA' (EC 2.3.1.318) with evidence code ECO:0000269 (in vitro experiment, PubMed:24240508, Bastard et al. 2014 Nat Chem Biol). The expected answer B is a verbatim match to the experimentally determined reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical thiolase-superfamily catalytic motif GGRSG (visible around residues ~80–86) together with the characteristic CoA-binding/thiolase fold architecture (GKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGGHCRTGLEDNVRLDKQTLAPSNAALVSQVAALCEEYGRPVATVAQARALLGLPSMEIDGRSPW). This identifies the protein as a member of the thiolase/CoA-transferase superfamily. Among the four choices, only B is a CoA-transferase/thiolase-type reaction. Choice A (peptidyl transferase on tRNA), C (phenylalanine ammonia-lyase, a lyase), and D (potassium channel, a membrane transporter) belong to entirely unrelated enzyme/protein classes and are incompatible with a thiolase fold. Elimination by enzyme-class matching yields B.


**Missing item-specific fact**

> The specific novel substrate 3-oxoadipate (rather than the classical acetyl-CoA dimerization substrate of thiolases) is a 2014 discovery not predictable from sequence alone, but it is not needed to select B because B is the only CoA-transferase option among the four distractors.


**Reason**

> A model that recognizes the GGRSG thiolase motif and CoA-binding features can eliminate A, C, and D as belonging to unrelated protein families, leaving B as the only mechanistically consistent choice. The reasoning does not require memorizing the specific 3-oxoadipate substrate; it requires only identifying the enzyme superfamily and matching it to the sole CoA-transferase reaction listed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four distinct protein/enzyme classes (peptidyl transferase, thiolase/CoA-transferase, ammonia-lyase, ion channel). Only B is consistent with a thiolase-superfamily sequence. No other option is defensible for a protein bearing the GGRSG catalytic motif and CoA-binding architecture.


### Important caveats

- The specific reaction with 3-oxoadipate as substrate was a novel discovery (2014, Nat Chem Biol) revealing 'hidden functional diversity' within the thiolase family; a model could identify the thiolase fold but might not predict the unusual substrate without prior knowledge. However, the question is answerable by elimination because no other choice represents a CoA-transferase reaction.
- The UniProt entry was first publicly released in 2025-02-05; the benchmark author's source snapshot is unknown, but the sequence and annotation have been stable since sequence version 1 (2006-10-03).
- Evidence is experimental (ECO:0000269, in vitro assay), not merely computational or similarity-based transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical thiolase-superfamily catalytic motif GGRSG (visible around residues ~80–86) together with the characteristic CoA-binding/thiolase fold architecture (GKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGGHCRTGLEDNVRLDKQTLAPSNAALVSQVAALCEEYGRPVATVAQARALLGLPSMEIDGRSPW). This identifies the protein as a member of the thiolase/CoA-transferase superfamily. Among the four choices, only B is a CoA-transferase/thiolase-type reaction. Choice A (peptidyl transferase on tRNA), C (phenylalanine ammonia-lyase, a lyase), and D (potassium channel, a membrane transporter) belong to entirely unrelated enzyme/protein classes and are incompatible with a thiolase fold. Elimination by enzyme-class matching yields B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific novel substrate 3-oxoadipate (rather than the classical acetyl-CoA dimerization substrate of thiolases) is a 2014 discovery not predictable from sequence alone, but it is not needed to select B because B is the only CoA-transferase option among the four distractors.",
    "reason": "A model that recognizes the GGRSG thiolase motif and CoA-binding features can eliminate A, C, and D as belonging to unrelated protein families, leaving B as the only mechanistically consistent choice. The reasoning does not require memorizing the specific 3-oxoadipate substrate; it requires only identifying the enzyme superfamily and matching it to the sole CoA-transferase reaction listed."
  },
  "case_id": "catalytic_activity_0096",
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
    "reason": "The supplied 284-aa sequence matches UniProt Q0KAA1 (3OXCE_CUPNH, Cupriavidus necator) exactly. The reviewed Swiss-Prot entry annotates the catalytic activity as '3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA' (EC 2.3.1.318) with evidence code ECO:0000269 (in vitro experiment, PubMed:24240508, Bastard et al. 2014 Nat Chem Biol). The expected answer B is a verbatim match to the experimentally determined reaction."
  },
  "important_caveats": [
    "The specific reaction with 3-oxoadipate as substrate was a novel discovery (2014, Nat Chem Biol) revealing 'hidden functional diversity' within the thiolase family; a model could identify the thiolase fold but might not predict the unusual substrate without prior knowledge. However, the question is answerable by elimination because no other choice represents a CoA-transferase reaction.",
    "The UniProt entry was first publicly released in 2025-02-05; the benchmark author's source snapshot is unknown, but the sequence and annotation have been stable since sequence version 1 (2006-10-03).",
    "Evidence is experimental (ECO:0000269, in vitro assay), not merely computational or similarity-based transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct protein/enzyme classes (peptidyl transferase, thiolase/CoA-transferase, ammonia-lyase, ion channel). Only B is consistent with a thiolase-superfamily sequence. No other option is defensible for a protein bearing the GGRSG catalytic motif and CoA-binding architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 284-aa sequence matches UniProt Q0KAA1 (3OXCE_CUPNH, Cupriavidus necator) exactly. The reviewed Swiss-Prot entry annotates the catalytic activity as '3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA' (EC 2.3.1.318) with evidence code ECO:0000269 (in vitro experiment, PubMed:24240508, Bastard et al. 2014 Nat Chem Biol). The expected answer B is a verbatim match to the experimentally determined reaction.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical thiolase-superfamily catalytic motif GGRSG (visible around residues ~80–86) together with the characteristic CoA-binding/thiolase fold architecture (GKIDGALHIQFVMGIKNAMPVDREVLAFYVHTLRRLAPDATWTGAGIGRDQLTMARWSLELGGHCRTGLEDNVRLDKQTLAPSNAALVSQVAALCEEYGRPVATVAQARALLGLPSMEIDGRSPW). This identifies the protein as a member of the thiolase/CoA-transferase superfamily. Among the four choices, only B is a CoA-transferase/thiolase-type reaction. Choice A (peptidyl transferase on tRNA), C (phenylalanine ammonia-lyase, a lyase), and D (potassium channel, a membrane transporter) belong to entirely unrelated enzyme/protein classes and are incompatible with a thiolase fold. Elimination by enzyme-class matching yields B.",
    "missing_item_specific_fact": "The specific novel substrate 3-oxoadipate (rather than the classical acetyl-CoA dimerization substrate of thiolases) is a 2014 discovery not predictable from sequence alone, but it is not needed to select B because B is the only CoA-transferase option among the four distractors.",
    "reason": "A model that recognizes the GGRSG thiolase motif and CoA-binding features can eliminate A, C, and D as belonging to unrelated protein families, leaving B as the only mechanistically consistent choice. The reasoning does not require memorizing the specific 3-oxoadipate substrate; it requires only identifying the enzyme superfamily and matching it to the sole CoA-transferase reaction listed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four distinct protein/enzyme classes (peptidyl transferase, thiolase/CoA-transferase, ammonia-lyase, ion channel). Only B is consistent with a thiolase-superfamily sequence. No other option is defensible for a protein bearing the GGRSG catalytic motif and CoA-binding architecture."
  },
  "important_caveats": [
    "The specific reaction with 3-oxoadipate as substrate was a novel discovery (2014, Nat Chem Biol) revealing 'hidden functional diversity' within the thiolase family; a model could identify the thiolase fold but might not predict the unusual substrate without prior knowledge. However, the question is answerable by elimination because no other choice represents a CoA-transferase reaction.",
    "The UniProt entry was first publicly released in 2025-02-05; the benchmark author's source snapshot is unknown, but the sequence and annotation have been stable since sequence version 1 (2006-10-03).",
    "Evidence is experimental (ECO:0000269, in vitro assay), not merely computational or similarity-based transfer."
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

**Accession:** `Q0KAA1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 87. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.682394+00:00.  

```json
"Q0KAA1"
```

Source SHA-256: `c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.682394+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"3-oxoadipate cleavage enzyme"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24240508","source":"PubMed"}],"value":"BKACE_378"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24240508","source":"PubMed"}],"value":"2.3.1.318"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"3-oxoadipate:acetyl-CoA acetyltransferase"}}}
```

Source SHA-256: `c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.682394+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.1.318","evidences":[{"evidenceCode":"ECO:0000269","id":"24240508","source":"PubMed"}],"name":"3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79651"},{"database":"ChEBI","id":"CHEBI:13705"},{"database":"ChEBI","id":"CHEBI:15775"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:57292"}]}}
```

Source SHA-256: `c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0KAA1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.682394+00:00.  

```json
{"citation":{"authors":["Bastard K.","Smith A.A.","Vergne-Vaxelaire C.","Perret A.","Zaparucha A.","De Melo-Minardi R.","Mariage A.","Boutard M.","Debard A.","Lechaplais C.","Pelle C.","Pellouin V.","Perchat N.","Petit J.L.","Kreimeyer A.","Medigue C.","Weissenbach J.","Artiguenave F.","De Berardinis V.","Vallenet D.","Salanoubat M."],"citationCrossReferences":[{"database":"PubMed","id":"24240508"},{"database":"DOI","id":"10.1038/nchembio.1387"}],"citationType":"journal article","firstPage":"42","id":"24240508","journal":"Nat. Chem. Biol.","lastPage":"49","publicationDate":"2014","title":"Revealing the hidden functional diversity of an enzyme family.","volume":"10"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `c8f71ccfa4b417ca33bf6e9e7b333cdb179beaa73d1bbbba6e6d86bbeaaac140`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:30:29.925890+00:00.  

```text
ID   3OXCE_CUPNH             Reviewed;         284 AA.
AC   Q0KAA1;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-OCT-2006, sequence version 1.
DT   28-JAN-2026, entry version 87.
DE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};
DE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};
DE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};
DE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};
GN   OrderedLocusNames=H16_A1969 {ECO:0000312|EMBL:CAJ93070.1};
GN   ORFNames=E6A55_10065 {ECO:0000312|EMBL:QCC00902.1};
OS   Cupriavidus necator (strain ATCC 17699 / DSM 428 / KCTC 22496 / NCIMB 10442
OS   / H16 / Stanier 337) (Ralstonia eutropha).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;
OC   Burkholderiales; Burkholderiaceae; Cupriavidus.
OX   NCBI_TaxID=381666;
```

Source SHA-256: `6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:30:29.925890+00:00.  

```text
DE   RecName: Full=3-oxoadipate:acetyl-CoA acetyltransferase {ECO:0000305};
DE            EC=2.3.1.318 {ECO:0000269|PubMed:24240508};
DE   AltName: Full=3-oxoadipate cleavage enzyme {ECO:0000305};
DE   AltName: Full=BKACE_378 {ECO:0000303|PubMed:24240508};
```

Source SHA-256: `6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)  
**Locator:** `lines 34-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:30:29.925890+00:00.  

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

Source SHA-256: `6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0KAA1?format=txt&versions=87)  
**Locator:** `lines 49-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-02T04:30:29.925890+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA;
CC         Xref=Rhea:RHEA:79651, ChEBI:CHEBI:13705, ChEBI:CHEBI:15775,
CC         ChEBI:CHEBI:57288, ChEBI:CHEBI:57292; EC=2.3.1.318;
CC         Evidence={ECO:0000269|PubMed:24240508};
```

Source SHA-256: `6f05fdb130e65dbd4fe594e672961fa4042d9e020ec6cf0253a116bc497dc13e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
