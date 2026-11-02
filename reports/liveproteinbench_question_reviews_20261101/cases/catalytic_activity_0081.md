# catalytic_activity_0081

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)

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
A. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
B. 3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate
C. L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)
D. dTMP + ATP = dTDP + ADP
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

> The supplied sequence exactly matches the UniProt entry annotated as homoserine kinase, with the listed reaction matching choice C. The reaction annotation is transferred by similarity from UniProtKB:P17423 (ECO:0000250), so it supports the key as a database-based functional assignment, not as direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could suggest an ATP-dependent enzyme, which may help distinguish kinase-type choices from the phosphatase or phosphorylase options. But that broad inference does not establish homoserine as the substrate rather than the alternative kinase substrate in choice D.


**Missing item-specific fact**

> The protein-specific assignment as homoserine kinase, including its substrate specificity for L-homoserine, is not supplied in the question.


**Reason**

> Choosing C over the other kinase option requires protein-specific functional annotation or equivalent external knowledge; general sequence-level kinase clues do not identify the precise reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reaction choices are distinct, and the matched protein annotation specifically supports choice C.


### Important caveats

- The annotation evidence is transferred by similarity rather than presented as a direct experimental measurement of this protein's catalytic activity.
- Reviewer-only accession and annotation evidence establishes support for the key but was absent from the evaluated input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could suggest an ATP-dependent enzyme, which may help distinguish kinase-type choices from the phosphatase or phosphorylase options. But that broad inference does not establish homoserine as the substrate rather than the alternative kinase substrate in choice D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment as homoserine kinase, including its substrate specificity for L-homoserine, is not supplied in the question.",
    "reason": "Choosing C over the other kinase option requires protein-specific functional annotation or equivalent external knowledge; general sequence-level kinase clues do not identify the precise reaction."
  },
  "case_id": "catalytic_activity_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as homoserine kinase, with the listed reaction matching choice C. The reaction annotation is transferred by similarity from UniProtKB:P17423 (ECO:0000250), so it supports the key as a database-based functional assignment, not as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The annotation evidence is transferred by similarity rather than presented as a direct experimental measurement of this protein's catalytic activity.",
    "Reviewer-only accession and annotation evidence establishes support for the key but was absent from the evaluated input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction choices are distinct, and the matched protein annotation specifically supports choice C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as homoserine kinase, with the listed reaction matching choice C. The reaction annotation is transferred by similarity from UniProtKB:P17423 (ECO:0000250), so it supports the key as a database-based functional assignment, not as direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could suggest an ATP-dependent enzyme, which may help distinguish kinase-type choices from the phosphatase or phosphorylase options. But that broad inference does not establish homoserine as the substrate rather than the alternative kinase substrate in choice D.",
    "missing_item_specific_fact": "The protein-specific assignment as homoserine kinase, including its substrate specificity for L-homoserine, is not supplied in the question.",
    "reason": "Choosing C over the other kinase option requires protein-specific functional annotation or equivalent external knowledge; general sequence-level kinase clues do not identify the precise reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reaction choices are distinct, and the matched protein annotation specifically supports choice C."
  },
  "important_caveats": [
    "The annotation evidence is transferred by similarity rather than presented as a direct experimental measurement of this protein's catalytic activity.",
    "Reviewer-only accession and annotation evidence establishes support for the key but was absent from the evaluated input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt J9VU26 (KHSE_CRYN9) exactly (SHA256 confirmed). The entry is annotated as Homoserine kinase (EC 2.7.1.39) with the catalytic reaction 'L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)', which is identical to option C. The annotation evidence code is ECO:0000250 (inferred by similarity from P17423), but the gene THR1 is also supported by experimental disruption phenotype data (PubMed:18757810) demonstrating its essential role in threonine biosynthesis. The sequence is 357 aa, consistent with fungal homoserine kinase.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options represent distinct enzyme classes: A is a phosphoserine phosphatase (hydrolase, EC 3.1.3.3), B is a glycosyl phosphorylase, C is a homoserine kinase (GHMP kinase family, EC 2.7.1.39), and D is a thymidylate kinase (P-loop NTPase fold). The sequence contains motifs characteristic of the GHMP kinase family (e.g., 'GIGHFVRFGW' and 'GAGPTILALATHNFEAIANEIERIFGDEQ' with the GxGxxG-type glycine-rich nucleotide-binding pattern), while lacking the canonical Walker A motif (GxxxxGK&#91;T/S&#93;) expected for P-loop NTPases like thymidylate kinase. The 357-aa length is consistent with GHMP kinases (~300–400 aa) rather than thymidylate kinases (~200–250 aa). The presence of kinase-like motifs and absence of phosphatase or glycosyltransferase signatures eliminate A and B. The GHMP kinase motif architecture over a P-loop NTPase fold distinguishes C from D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A solver with knowledge of major kinase-fold families (GHMP kinase vs. P-loop NTPase) can use the sequence's domain motifs, length, and absence of Walker A to reason toward C. This is general protein-domain knowledge, not a lookup of this specific protein's database entry. The distractors A and B are readily eliminated by recognizing phosphotransferase-type motifs; the C-vs-D distinction rests on fold-family signatures visible in the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span four different enzyme classes (phosphatase, phosphorylase, GHMP kinase, P-loop NTPase kinase). Once kinase activity is recognized, the GHMP-kinase vs. P-loop-NTPase distinction narrows the answer to C. No other option is defensible given the sequence motifs.


### Important caveats

- The UniProt catalytic-activity annotation is primarily by similarity (ECO:0000250 from P17423), not direct experimental measurement on this specific Cryptococcus enzyme. Experimental support comes indirectly from gene-disruption phenotype (PubMed:18757810).
- Distinguishing GHMP kinase motifs from P-loop NTPase motifs from raw sequence requires specialized but general biochemistry knowledge; a solver without domain-family training may struggle.
- The identity of the protein as homoserine kinase specifically (vs. other GHMP kinases such as galactokinase or mevalonate kinase) is not tested here because those alternatives are absent from the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options represent distinct enzyme classes: A is a phosphoserine phosphatase (hydrolase, EC 3.1.3.3), B is a glycosyl phosphorylase, C is a homoserine kinase (GHMP kinase family, EC 2.7.1.39), and D is a thymidylate kinase (P-loop NTPase fold). The sequence contains motifs characteristic of the GHMP kinase family (e.g., 'GIGHFVRFGW' and 'GAGPTILALATHNFEAIANEIERIFGDEQ' with the GxGxxG-type glycine-rich nucleotide-binding pattern), while lacking the canonical Walker A motif (GxxxxGK[T/S]) expected for P-loop NTPases like thymidylate kinase. The 357-aa length is consistent with GHMP kinases (~300–400 aa) rather than thymidylate kinases (~200–250 aa). The presence of kinase-like motifs and absence of phosphatase or glycosyltransferase signatures eliminate A and B. The GHMP kinase motif architecture over a P-loop NTPase fold distinguishes C from D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A solver with knowledge of major kinase-fold families (GHMP kinase vs. P-loop NTPase) can use the sequence's domain motifs, length, and absence of Walker A to reason toward C. This is general protein-domain knowledge, not a lookup of this specific protein's database entry. The distractors A and B are readily eliminated by recognizing phosphotransferase-type motifs; the C-vs-D distinction rests on fold-family signatures visible in the sequence."
  },
  "case_id": "catalytic_activity_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt J9VU26 (KHSE_CRYN9) exactly (SHA256 confirmed). The entry is annotated as Homoserine kinase (EC 2.7.1.39) with the catalytic reaction 'L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)', which is identical to option C. The annotation evidence code is ECO:0000250 (inferred by similarity from P17423), but the gene THR1 is also supported by experimental disruption phenotype data (PubMed:18757810) demonstrating its essential role in threonine biosynthesis. The sequence is 357 aa, consistent with fungal homoserine kinase."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation is primarily by similarity (ECO:0000250 from P17423), not direct experimental measurement on this specific Cryptococcus enzyme. Experimental support comes indirectly from gene-disruption phenotype (PubMed:18757810).",
    "Distinguishing GHMP kinase motifs from P-loop NTPase motifs from raw sequence requires specialized but general biochemistry knowledge; a solver without domain-family training may struggle.",
    "The identity of the protein as homoserine kinase specifically (vs. other GHMP kinases such as galactokinase or mevalonate kinase) is not tested here because those alternatives are absent from the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four different enzyme classes (phosphatase, phosphorylase, GHMP kinase, P-loop NTPase kinase). Once kinase activity is recognized, the GHMP-kinase vs. P-loop-NTPase distinction narrows the answer to C. No other option is defensible given the sequence motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt J9VU26 (KHSE_CRYN9) exactly (SHA256 confirmed). The entry is annotated as Homoserine kinase (EC 2.7.1.39) with the catalytic reaction 'L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)', which is identical to option C. The annotation evidence code is ECO:0000250 (inferred by similarity from P17423), but the gene THR1 is also supported by experimental disruption phenotype data (PubMed:18757810) demonstrating its essential role in threonine biosynthesis. The sequence is 357 aa, consistent with fungal homoserine kinase.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options represent distinct enzyme classes: A is a phosphoserine phosphatase (hydrolase, EC 3.1.3.3), B is a glycosyl phosphorylase, C is a homoserine kinase (GHMP kinase family, EC 2.7.1.39), and D is a thymidylate kinase (P-loop NTPase fold). The sequence contains motifs characteristic of the GHMP kinase family (e.g., 'GIGHFVRFGW' and 'GAGPTILALATHNFEAIANEIERIFGDEQ' with the GxGxxG-type glycine-rich nucleotide-binding pattern), while lacking the canonical Walker A motif (GxxxxGK[T/S]) expected for P-loop NTPases like thymidylate kinase. The 357-aa length is consistent with GHMP kinases (~300–400 aa) rather than thymidylate kinases (~200–250 aa). The presence of kinase-like motifs and absence of phosphatase or glycosyltransferase signatures eliminate A and B. The GHMP kinase motif architecture over a P-loop NTPase fold distinguishes C from D.",
    "missing_item_specific_fact": "",
    "reason": "A solver with knowledge of major kinase-fold families (GHMP kinase vs. P-loop NTPase) can use the sequence's domain motifs, length, and absence of Walker A to reason toward C. This is general protein-domain knowledge, not a lookup of this specific protein's database entry. The distractors A and B are readily eliminated by recognizing phosphotransferase-type motifs; the C-vs-D distinction rests on fold-family signatures visible in the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span four different enzyme classes (phosphatase, phosphorylase, GHMP kinase, P-loop NTPase kinase). Once kinase activity is recognized, the GHMP-kinase vs. P-loop-NTPase distinction narrows the answer to C. No other option is defensible given the sequence motifs."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation is primarily by similarity (ECO:0000250 from P17423), not direct experimental measurement on this specific Cryptococcus enzyme. Experimental support comes indirectly from gene-disruption phenotype (PubMed:18757810).",
    "Distinguishing GHMP kinase motifs from P-loop NTPase motifs from raw sequence requires specialized but general biochemistry knowledge; a solver without domain-family training may struggle.",
    "The identity of the protein as homoserine kinase specifically (vs. other GHMP kinases such as galactokinase or mevalonate kinase) is not tested here because those alternatives are absent from the choices."
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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.100039+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P17423","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13986"}}],"reaction":{"ecNumber":"2.7.1.39","evidences":[{"evidenceCode":"ECO:0000250","id":"P17423","source":"UniProtKB"}],"name":"L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13985"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:57476"},{"database":"ChEBI","id":"CHEBI:57590"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
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
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
DE   RecName: Full=Homoserine kinase {ECO:0000305};
DE            Short=HK {ECO:0000305};
DE            Short=HSK {ECO:0000305};
DE            EC=2.7.1.39 {ECO:0000250|UniProtKB:P17423};
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

### Evidence H3

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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)  
**Locator:** `lines 45-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:28:15.320227+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+);
CC         Xref=Rhea:RHEA:13985, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:57476, ChEBI:CHEBI:57590, ChEBI:CHEBI:456216;
CC         EC=2.7.1.39; Evidence={ECO:0000250|UniProtKB:P17423};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13986;
CC         Evidence={ECO:0000250|UniProtKB:P17423};
```

Source SHA-256: `fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
