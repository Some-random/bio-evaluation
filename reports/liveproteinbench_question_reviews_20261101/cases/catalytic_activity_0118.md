# catalytic_activity_0118

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDGYAVRAEAMEKRYGEKRALDGFDLAVGEGTVHGLLGPNGAGKTTAVRILSTLVRLDGGRATVAGLDVARQPREVRARIGLTGQYAAVDEVLTGRQNLEMFGRLFHLGGRRARLRATELLEQFDLTDAGDRGVGKYSGGMRRRLDLAASMILAPAVLFLDEPTTGLDPRSRGEVWESVRALVAGGTTVLLTTQYLEEADKLASRITVIDQGRAIADDTPDGLKNLVGGDRIEVVVAERAEIPRVVKVVARVADGEPEADETESRVHAPVTDRVTALTEVARTLQDEGVRVEDIGLRRPSLDDVFLRLTGHRTENTEAKEAA

[Multiple Choices]
A. daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)
B. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
C. 2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2'-hydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. guanosine in U6 snRNA + S-adenosyl-L-methionine = N(2)-methylguanosine in U6 snRNA + S-adenosyl-L-homocysteine + H(+)
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

> The supplied sequence matches the annotated DrrA2 protein. UniProt assigns it EC 7.6.2.2 and the daunorubicin efflux reaction in both the historical and current records. This supports A as a database annotation; the excerpts cite a paper but do not independently establish the underlying experimental details.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The GPNGAGKTT P-loop and Walker-B-like acidic motif support an ATPase, plausibly an ABC transporter ATP-binding component, which favors the ATP-coupled transport chemistry in A over the transferase, oxygenase, and methyltransferase alternatives.


**Missing item-specific fact**

> The sequence motifs do not establish daunorubicin as the transported substrate; identifying that specific cargo and reaction requires protein-specific functional annotation or experimental evidence.


**Reason**

> Sequence-based family reasoning can favor A's general mechanism, but the precise substrate named in the answer is an item-specific fact absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct enzyme classes, and the sequence's ATPase motifs favor the transporter reaction. No other listed choice is comparably supported, although the exact cargo is not inferable from those motifs alone.


### Important caveats

- Reviewer-only database evidence supports the key but was not available to the evaluated model.
- The cited annotation is not independently validated here against the primary paper.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The GPNGAGKTT P-loop and Walker-B-like acidic motif support an ATPase, plausibly an ABC transporter ATP-binding component, which favors the ATP-coupled transport chemistry in A over the transferase, oxygenase, and methyltransferase alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence motifs do not establish daunorubicin as the transported substrate; identifying that specific cargo and reaction requires protein-specific functional annotation or experimental evidence.",
    "reason": "Sequence-based family reasoning can favor A's general mechanism, but the precise substrate named in the answer is an item-specific fact absent from the input."
  },
  "case_id": "catalytic_activity_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated DrrA2 protein. UniProt assigns it EC 7.6.2.2 and the daunorubicin efflux reaction in both the historical and current records. This supports A as a database annotation; the excerpts cite a paper but do not independently establish the underlying experimental details."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The cited annotation is not independently validated here against the primary paper."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct enzyme classes, and the sequence's ATPase motifs favor the transporter reaction. No other listed choice is comparably supported, although the exact cargo is not inferable from those motifs alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated DrrA2 protein. UniProt assigns it EC 7.6.2.2 and the daunorubicin efflux reaction in both the historical and current records. This supports A as a database annotation; the excerpts cite a paper but do not independently establish the underlying experimental details.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The GPNGAGKTT P-loop and Walker-B-like acidic motif support an ATPase, plausibly an ABC transporter ATP-binding component, which favors the ATP-coupled transport chemistry in A over the transferase, oxygenase, and methyltransferase alternatives.",
    "missing_item_specific_fact": "The sequence motifs do not establish daunorubicin as the transported substrate; identifying that specific cargo and reaction requires protein-specific functional annotation or experimental evidence.",
    "reason": "Sequence-based family reasoning can favor A's general mechanism, but the precise substrate named in the answer is an item-specific fact absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct enzyme classes, and the sequence's ATPase motifs favor the transporter reaction. No other listed choice is comparably supported, although the exact cargo is not inferable from those motifs alone."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The cited annotation is not independently validated here against the primary paper."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt P0DXU5 (DRRA2_STRC4) exactly (322 aa, SHA-256 confirmed). The UniProt entry annotates this protein as 'Daunorubicin resistance ATP-binding protein DrrA2' with EC 7.6.2.2 and catalytic activity 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)', which is identical to option A. Evidence code ECO:0000305 (inferred by similarity) is used, referencing PubMed:39375957 which provides experimental context (FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, DISRUPTION PHENOTYPE). The annotation is database-supported with experimental backing from the cited paper.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Walker A motif (GPNGAGKTT at positions ~30-38) and a Walker B-like region (DEPTT), characteristic of ABC transporter nucleotide-binding domains. Among the four options, only A describes an ATP-hydrolysis-driven transport reaction (ABC transporter mechanism). Option B is a CoA-dependent transferase (no ATP hydrolysis), C is a monooxygenase using reduced ferredoxin and O2 (no ATP), and D is a SAM-dependent methyltransferase (no ATP). Recognizing the P-loop/ABC-transporter architecture and matching it to the only ATP-hydrolysis-coupled option provides a concrete reasoning path to select A.


**Missing item-specific fact**

> The specific substrate identity 'daunorubicin' cannot be determined from sequence motifs alone; one would need to know the protein is DrrA2 from Streptomyces coeruleorubidus. However, since only option A is an ABC transporter reaction, the Walker A motif recognition is sufficient to eliminate B, C, and D without knowing the exact substrate.


**Reason**

> The Walker A motif and ABC-transporter domain architecture are directly readable from the sequence. The mechanistic distinction (ATP hydrolysis vs. CoA transfer vs. monooxygenase vs. methyltransferase) is a matter of general enzymology knowledge applied to the four options. The specific substrate name adds a lookup component but is not strictly necessary to eliminate the three non-ABC-transporter options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A involves ATP hydrolysis as the primary catalytic mechanism, which is the only mechanism consistent with the visible Walker A/P-loop motif. Options B, C, and D describe fundamentally different enzyme classes (transferase, monooxygenase, methyltransferase) that would not contain an ABC-transporter NBD architecture. The sequence clearly shows ABC-transporter features, making A the uniquely defensible choice.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the catalytic activity assignment is not from direct in vitro characterization of this exact protein but from similarity to known DrrA-family proteins, supported by experimental genetic evidence (disruption phenotype, induction) in the cited 2024 paper.
- The specific identification of daunorubicin (rather than doxorubicin or other anthracyclines) as the substrate relies on the database annotation and the cited paper's experimental context; sequence motifs alone cannot distinguish among anthracycline substrates.
- The entry was first public in February 2025, so the annotation is relatively recent; the author's data-construction date is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif (GPNGAGKTT at positions ~30-38) and a Walker B-like region (DEPTT), characteristic of ABC transporter nucleotide-binding domains. Among the four options, only A describes an ATP-hydrolysis-driven transport reaction (ABC transporter mechanism). Option B is a CoA-dependent transferase (no ATP hydrolysis), C is a monooxygenase using reduced ferredoxin and O2 (no ATP), and D is a SAM-dependent methyltransferase (no ATP). Recognizing the P-loop/ABC-transporter architecture and matching it to the only ATP-hydrolysis-coupled option provides a concrete reasoning path to select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity 'daunorubicin' cannot be determined from sequence motifs alone; one would need to know the protein is DrrA2 from Streptomyces coeruleorubidus. However, since only option A is an ABC transporter reaction, the Walker A motif recognition is sufficient to eliminate B, C, and D without knowing the exact substrate.",
    "reason": "The Walker A motif and ABC-transporter domain architecture are directly readable from the sequence. The mechanistic distinction (ATP hydrolysis vs. CoA transfer vs. monooxygenase vs. methyltransferase) is a matter of general enzymology knowledge applied to the four options. The specific substrate name adds a lookup component but is not strictly necessary to eliminate the three non-ABC-transporter options."
  },
  "case_id": "catalytic_activity_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DXU5 (DRRA2_STRC4) exactly (322 aa, SHA-256 confirmed). The UniProt entry annotates this protein as 'Daunorubicin resistance ATP-binding protein DrrA2' with EC 7.6.2.2 and catalytic activity 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)', which is identical to option A. Evidence code ECO:0000305 (inferred by similarity) is used, referencing PubMed:39375957 which provides experimental context (FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, DISRUPTION PHENOTYPE). The annotation is database-supported with experimental backing from the cited paper."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the catalytic activity assignment is not from direct in vitro characterization of this exact protein but from similarity to known DrrA-family proteins, supported by experimental genetic evidence (disruption phenotype, induction) in the cited 2024 paper.",
    "The specific identification of daunorubicin (rather than doxorubicin or other anthracyclines) as the substrate relies on the database annotation and the cited paper's experimental context; sequence motifs alone cannot distinguish among anthracycline substrates.",
    "The entry was first public in February 2025, so the annotation is relatively recent; the author's data-construction date is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A involves ATP hydrolysis as the primary catalytic mechanism, which is the only mechanism consistent with the visible Walker A/P-loop motif. Options B, C, and D describe fundamentally different enzyme classes (transferase, monooxygenase, methyltransferase) that would not contain an ABC-transporter NBD architecture. The sequence clearly shows ABC-transporter features, making A the uniquely defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DXU5 (DRRA2_STRC4) exactly (322 aa, SHA-256 confirmed). The UniProt entry annotates this protein as 'Daunorubicin resistance ATP-binding protein DrrA2' with EC 7.6.2.2 and catalytic activity 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)', which is identical to option A. Evidence code ECO:0000305 (inferred by similarity) is used, referencing PubMed:39375957 which provides experimental context (FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, DISRUPTION PHENOTYPE). The annotation is database-supported with experimental backing from the cited paper.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif (GPNGAGKTT at positions ~30-38) and a Walker B-like region (DEPTT), characteristic of ABC transporter nucleotide-binding domains. Among the four options, only A describes an ATP-hydrolysis-driven transport reaction (ABC transporter mechanism). Option B is a CoA-dependent transferase (no ATP hydrolysis), C is a monooxygenase using reduced ferredoxin and O2 (no ATP), and D is a SAM-dependent methyltransferase (no ATP). Recognizing the P-loop/ABC-transporter architecture and matching it to the only ATP-hydrolysis-coupled option provides a concrete reasoning path to select A.",
    "missing_item_specific_fact": "The specific substrate identity 'daunorubicin' cannot be determined from sequence motifs alone; one would need to know the protein is DrrA2 from Streptomyces coeruleorubidus. However, since only option A is an ABC transporter reaction, the Walker A motif recognition is sufficient to eliminate B, C, and D without knowing the exact substrate.",
    "reason": "The Walker A motif and ABC-transporter domain architecture are directly readable from the sequence. The mechanistic distinction (ATP hydrolysis vs. CoA transfer vs. monooxygenase vs. methyltransferase) is a matter of general enzymology knowledge applied to the four options. The specific substrate name adds a lookup component but is not strictly necessary to eliminate the three non-ABC-transporter options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A involves ATP hydrolysis as the primary catalytic mechanism, which is the only mechanism consistent with the visible Walker A/P-loop motif. Options B, C, and D describe fundamentally different enzyme classes (transferase, monooxygenase, methyltransferase) that would not contain an ABC-transporter NBD architecture. The sequence clearly shows ABC-transporter features, making A the uniquely defensible choice."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the catalytic activity assignment is not from direct in vitro characterization of this exact protein but from similarity to known DrrA-family proteins, supported by experimental genetic evidence (disruption phenotype, induction) in the cited 2024 paper.",
    "The specific identification of daunorubicin (rather than doxorubicin or other anthracyclines) as the substrate relies on the database annotation and the cited paper's experimental context; sequence motifs alone cannot distinguish among anthracycline substrates.",
    "The entry was first public in February 2025, so the annotation is relatively recent; the author's data-construction date is unknown."
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

**Accession:** `P0DXU5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
"P0DXU5"
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"value":"7.6.2.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Daunorubicin resistance ATP-binding protein DrrA2"}}}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:33148"}}],"reaction":{"ecNumber":"7.6.2.2","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"name":"daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:33147"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:64677"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:36.968817+00:00.  

```json
{"citation":{"authors":["Dong J.","Ning J.","Tian Y.","Li H.","Chen H.","Guan W."],"citationCrossReferences":[{"database":"PubMed","id":"39375957"},{"database":"DOI","id":"10.1111/1751-7915.70023"}],"citationType":"journal article","firstPage":"e70023","id":"39375957","journal":"Microb. Biotechnol.","lastPage":"e70023","publicationDate":"2024","title":"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.","volume":"17"},"referenceNumber":2,"referencePositions":["FUNCTION IN DAUNORUBICIN EFFLUX","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
ID   DRRA2_STRC4             Reviewed;         322 AA.
AC   P0DXU5;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA2 {ECO:0000305};
DE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};
GN   Name=drrA2 {ECO:0000303|PubMed:39375957};
GN   ORFNames=R5U08_15995 {ECO:0000312|EMBL:WOT35541.1};
OS   Streptomyces coeruleorubidus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=116188;
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA2 {ECO:0000305};
DE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 19-25`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
RN   [2]
RP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.
RX   PubMed=39375957; DOI=10.1111/1751-7915.70023;
RA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;
RT   "The involvement of multiple ABC transporters in daunorubicin efflux in
RT   Streptomyces coeruleorubidus.";
RL   Microb. Biotechnol. 17:e70023-e70023(2024).
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)  
**Locator:** `lines 31-38`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:38.836268+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP +
CC         phosphate + H(+); Xref=Rhea:RHEA:33147, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30616, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:64677, ChEBI:CHEBI:456216; EC=7.6.2.2;
CC         Evidence={ECO:0000305|PubMed:39375957};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33148;
CC         Evidence={ECO:0000305|PubMed:39375957};
```

Source SHA-256: `f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
