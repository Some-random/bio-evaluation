# catalytic_activity_0172

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — (S,S)-2,5-di-(p-hydroxybenzyl)piperazine + reduced &#91;NADPH--hemoprotein reductase&#93; + O2 = (1S,4S)-4-&#91;(4-hydroxyphenyl)methyl&#93;-2,5-diazaspiro&#91;bicyclo&#91;3.2.1&#93;octane-6,1&#x27;-cyclohexane&#93;-2&#x27;,5&#x27;-dien-4&#x27;-one + oxidized &#91;NADPH--hemoprotein reductase&#93; + 2 H2O + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDLLQRAGLVVGLWVTYHILLGTYNVFFHPLRRFPGPRLAAATQLVNVYYIIRGINCKYLYELHEKYGDVVRTGPNELSFRTASAIRTIYGGNPGPDDTFHKNMIANIQETGDSDNLFFATGQQHNRYRRLIMPVFAERTIQGQGPMMQEYCSQLIQGLRNRCGRGYFPTQDGVVDIVPWTHFIISDILSHMLFGSGMNCLLNGDYHPWVMAGYKALIESTYIEAAHRLRPYHRILEYLLIPTRLRDGFRVHSAVSREKLQARSKEAEPYQFSLPSFTSESLSEQELFDNINVIATAAGETTSSALSAIMYYLTANPAAYDKAVTEVRQAFSNEAEITAASSASLPYLKAVIREAFRIRPTIPVGLHRLTPKGGREIDGKWVPAGTWISVANLAACRTSSHWKEAGRFIPERWLGDPEFASDNRDTSVPYSIGVRNCIGMSHANTQLRLILSRLLWNFDFEACPGNADPYDYLEYGTWQVEPLKLRVVDIRGQPK

[Multiple Choices]
A. (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
B. luteothin + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = aureothin + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
C. (1S,3S,6S,7S,8S,9S)-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecane-7,9-diol + ATP = (-)-FR901483 + ADP + 2 H(+)
D. (S,S)-2,5-di-(p-hydroxybenzyl)piperazine + reduced [NADPH--hemoprotein reductase] + O2 = (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexane]-2',5'-dien-4'-one + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
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

> The supplied sequence exactly matches the historical and current UniProt entry for FrzC, whose catalytic-activity annotation gives the reaction in choice D and cites experimental evidence (ECO:0000269, PubMed 33372776).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a membrane-associated cytochrome P450, supporting an oxidative reaction over methylation or ATP-dependent chemistry. But that broad inference does not distinguish D from B, which is also an oxygen-dependent oxidation.


**Missing item-specific fact**

> The protein-specific substrate and reaction assignment for FrzC, established by its annotation or experimental characterization, is needed to select D over the other oxidative option.


**Reason**

> Sequence-based family recognition may narrow the choices, but the exact substrate transformation and electron-donor system are not established by the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reactions, and the sequence-matched experimental annotation supports D. The limitation is that the supplied sequence alone does not uniquely establish that reaction.


### Important caveats

- The cited experimental evidence is reported in the database annotation; the primary paper was not independently reviewed here.
- The historical and current database records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450, supporting an oxidative reaction over methylation or ATP-dependent chemistry. But that broad inference does not distinguish D from B, which is also an oxygen-dependent oxidation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate and reaction assignment for FrzC, established by its annotation or experimental characterization, is needed to select D over the other oxidative option.",
    "reason": "Sequence-based family recognition may narrow the choices, but the exact substrate transformation and electron-donor system are not established by the supplied input."
  },
  "case_id": "catalytic_activity_0172",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt entry for FrzC, whose catalytic-activity annotation gives the reaction in choice D and cites experimental evidence (ECO:0000269, PubMed 33372776)."
  },
  "important_caveats": [
    "The cited experimental evidence is reported in the database annotation; the primary paper was not independently reviewed here.",
    "The historical and current database records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the sequence-matched experimental annotation supports D. The limitation is that the supplied sequence alone does not uniquely establish that reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the historical and current UniProt entry for FrzC, whose catalytic-activity annotation gives the reaction in choice D and cites experimental evidence (ECO:0000269, PubMed 33372776).",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated cytochrome P450, supporting an oxidative reaction over methylation or ATP-dependent chemistry. But that broad inference does not distinguish D from B, which is also an oxygen-dependent oxidation.",
    "missing_item_specific_fact": "The protein-specific substrate and reaction assignment for FrzC, established by its annotation or experimental characterization, is needed to select D over the other oxidative option.",
    "reason": "Sequence-based family recognition may narrow the choices, but the exact substrate transformation and electron-donor system are not established by the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the sequence-matched experimental annotation supports D. The limitation is that the supplied sequence alone does not uniquely establish that reaction."
  },
  "important_caveats": [
    "The cited experimental evidence is reported in the database annotation; the primary paper was not independently reviewed here.",
    "The historical and current database records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7T8F1I4 (FRZC_CLASX, 495 AA, sequence SHA256 match confirmed) annotates the catalytic activity as exactly Choice D, supported by experimental evidence (ECO:0000269, PubMed:33372776, Zhang et al. JACS 2021). The reaction converts (S,S)-2,5-di-(p-hydroxybenzyl)piperazine to the spirocyclic intermediate in the FR901483 biosynthetic pathway using NADPH-hemoprotein reductase and O2, consistent with its annotation as Cytochrome P450 monooxygenase FrzC (EC 1.14.14.-).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the canonical P450 heme-binding motif (FGSG...CIGM around residues ~170-370), allowing identification as a cytochrome P450 monooxygenase. This eliminates Choice A (SAM-dependent methyltransferase) and Choice C (ATP-dependent cyclase), as neither involves NADPH-hemoprotein reductase/O2 chemistry. However, both remaining options B and D are P450 reactions; distinguishing the substrate (luteothin vs. 2,5-di-(p-hydroxybenzyl)piperazine) requires knowledge of the specific enzyme identity (FrzC from the FR901483 pathway vs. an aureothin-pathway P450).


**Missing item-specific fact**

> The specific substrate identity of this P450 (i.e., that it is FrzC acting on (S,S)-2,5-di-(p-hydroxybenzyl)piperazine in the FR901483 biosynthetic cluster) cannot be inferred from the amino acid sequence alone without database lookup or memorization of the 2021 JACS paper.


**Reason**

> While P450 identification from the heme-binding motif narrows four choices to two, the final discrimination between B (aureothin pathway P450) and D (FR901483 pathway P450) depends entirely on knowing which specific natural-product biosynthetic cluster this enzyme belongs to—an item-specific annotation fact not derivable from general sequence features or biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A and C are clearly incompatible with P450 chemistry (no NADPH-hemoprotein reductase/O2 involvement). Choices B and D are both P450 reactions, but only D matches the annotated substrate. Given the sequence is a P450, a model that correctly identifies the enzyme class and knows the FR901483 pathway can select D; however, without pathway-specific knowledge, B and D are equally plausible from sequence alone. The question is not truly ambiguous in the sense that only one is correct, but the discrimination between B and D is not reasoning-accessible.


### Important caveats

- The P450 heme-binding motif (FGSG...CIGM) is clearly present, enabling elimination of non-P450 options (A, C).
- The annotation evidence code ECO:0000269 confirms experimental (not computational) support for the catalytic activity.
- The sequence-to-substrate mapping for P450s is not predictable from primary sequence alone; active-site architecture determines substrate specificity.
- Both B and D involve the same cofactor system (NADPH-hemoprotein reductase + O2), making the distinction purely substrate-specific.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif (FGSG...CIGM around residues ~170-370), allowing identification as a cytochrome P450 monooxygenase. This eliminates Choice A (SAM-dependent methyltransferase) and Choice C (ATP-dependent cyclase), as neither involves NADPH-hemoprotein reductase/O2 chemistry. However, both remaining options B and D are P450 reactions; distinguishing the substrate (luteothin vs. 2,5-di-(p-hydroxybenzyl)piperazine) requires knowledge of the specific enzyme identity (FrzC from the FR901483 pathway vs. an aureothin-pathway P450).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of this P450 (i.e., that it is FrzC acting on (S,S)-2,5-di-(p-hydroxybenzyl)piperazine in the FR901483 biosynthetic cluster) cannot be inferred from the amino acid sequence alone without database lookup or memorization of the 2021 JACS paper.",
    "reason": "While P450 identification from the heme-binding motif narrows four choices to two, the final discrimination between B (aureothin pathway P450) and D (FR901483 pathway P450) depends entirely on knowing which specific natural-product biosynthetic cluster this enzyme belongs to—an item-specific annotation fact not derivable from general sequence features or biological reasoning."
  },
  "case_id": "catalytic_activity_0172",
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
    "reason": "UniProt entry A0A7T8F1I4 (FRZC_CLASX, 495 AA, sequence SHA256 match confirmed) annotates the catalytic activity as exactly Choice D, supported by experimental evidence (ECO:0000269, PubMed:33372776, Zhang et al. JACS 2021). The reaction converts (S,S)-2,5-di-(p-hydroxybenzyl)piperazine to the spirocyclic intermediate in the FR901483 biosynthetic pathway using NADPH-hemoprotein reductase and O2, consistent with its annotation as Cytochrome P450 monooxygenase FrzC (EC 1.14.14.-)."
  },
  "important_caveats": [
    "The P450 heme-binding motif (FGSG...CIGM) is clearly present, enabling elimination of non-P450 options (A, C).",
    "The annotation evidence code ECO:0000269 confirms experimental (not computational) support for the catalytic activity.",
    "The sequence-to-substrate mapping for P450s is not predictable from primary sequence alone; active-site architecture determines substrate specificity.",
    "Both B and D involve the same cofactor system (NADPH-hemoprotein reductase + O2), making the distinction purely substrate-specific."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and C are clearly incompatible with P450 chemistry (no NADPH-hemoprotein reductase/O2 involvement). Choices B and D are both P450 reactions, but only D matches the annotated substrate. Given the sequence is a P450, a model that correctly identifies the enzyme class and knows the FR901483 pathway can select D; however, without pathway-specific knowledge, B and D are equally plausible from sequence alone. The question is not truly ambiguous in the sense that only one is correct, but the discrimination between B and D is not reasoning-accessible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0172",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1I4 (FRZC_CLASX, 495 AA, sequence SHA256 match confirmed) annotates the catalytic activity as exactly Choice D, supported by experimental evidence (ECO:0000269, PubMed:33372776, Zhang et al. JACS 2021). The reaction converts (S,S)-2,5-di-(p-hydroxybenzyl)piperazine to the spirocyclic intermediate in the FR901483 biosynthetic pathway using NADPH-hemoprotein reductase and O2, consistent with its annotation as Cytochrome P450 monooxygenase FrzC (EC 1.14.14.-).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif (FGSG...CIGM around residues ~170-370), allowing identification as a cytochrome P450 monooxygenase. This eliminates Choice A (SAM-dependent methyltransferase) and Choice C (ATP-dependent cyclase), as neither involves NADPH-hemoprotein reductase/O2 chemistry. However, both remaining options B and D are P450 reactions; distinguishing the substrate (luteothin vs. 2,5-di-(p-hydroxybenzyl)piperazine) requires knowledge of the specific enzyme identity (FrzC from the FR901483 pathway vs. an aureothin-pathway P450).",
    "missing_item_specific_fact": "The specific substrate identity of this P450 (i.e., that it is FrzC acting on (S,S)-2,5-di-(p-hydroxybenzyl)piperazine in the FR901483 biosynthetic cluster) cannot be inferred from the amino acid sequence alone without database lookup or memorization of the 2021 JACS paper.",
    "reason": "While P450 identification from the heme-binding motif narrows four choices to two, the final discrimination between B (aureothin pathway P450) and D (FR901483 pathway P450) depends entirely on knowing which specific natural-product biosynthetic cluster this enzyme belongs to—an item-specific annotation fact not derivable from general sequence features or biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A and C are clearly incompatible with P450 chemistry (no NADPH-hemoprotein reductase/O2 involvement). Choices B and D are both P450 reactions, but only D matches the annotated substrate. Given the sequence is a P450, a model that correctly identifies the enzyme class and knows the FR901483 pathway can select D; however, without pathway-specific knowledge, B and D are equally plausible from sequence alone. The question is not truly ambiguous in the sense that only one is correct, but the discrimination between B and D is not reasoning-accessible."
  },
  "important_caveats": [
    "The P450 heme-binding motif (FGSG...CIGM) is clearly present, enabling elimination of non-P450 options (A, C).",
    "The annotation evidence code ECO:0000269 confirms experimental (not computational) support for the catalytic activity.",
    "The sequence-to-substrate mapping for P450s is not predictable from primary sequence alone; active-site architecture determines substrate specificity.",
    "Both B and D involve the same cofactor system (NADPH-hemoprotein reductase + O2), making the distinction purely substrate-specific."
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

**Accession:** `A0A7T8F1I4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:44.613598+00:00.  

```json
"A0A7T8F1I4"
```

Source SHA-256: `a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:44.613598+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"1.14.14.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase FrzC"}}}
```

Source SHA-256: `a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:44.613598+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:83580"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"name":"(S,S)-2,5-di-(p-hydroxybenzyl)piperazine + reduced [NADPH--hemoprotein reductase] + O2 = (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexane]-2',5'-dien-4'-one + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:83579"},{"database":"Rhea","id":"RHEA-COMP:11964"},{"database":"Rhea","id":"RHEA-COMP:11965"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:57618"},{"database":"ChEBI","id":"CHEBI:58210"},{"database":"ChEBI","id":"CHEBI:145882"},{"database":"ChEBI","id":"CHEBI:233174"}]}}
```

Source SHA-256: `a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1I4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:44.613598+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Tamura Y.","Tang M.","Qiao T.","Sato M.","Otsu Y.","Sasamura S.","Taniguchi M.","Watanabe K.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33372776"},{"database":"DOI","id":"10.1021/jacs.0c12352"}],"citationType":"journal article","firstPage":"132","id":"33372776","journal":"J. Am. Chem. Soc.","lastPage":"136","publicationDate":"2021","title":"Biosynthesis of the Immunosuppressant (-)-FR901483.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"11231"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `a450aa333c0480566d67fc577725d57e8ffabeeea7f1c8ff429be621fd79b04b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1I4?format=txt&versions=18)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:47.051386+00:00.  

```text
ID   FRZC_CLASX              Reviewed;         495 AA.
AC   A0A7T8F1I4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-JUN-2021, sequence version 1.
DT   28-JAN-2026, entry version 18.
DE   RecName: Full=Cytochrome P450 monooxygenase FrzC {ECO:0000303|PubMed:33372776};
DE            EC=1.14.14.- {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein C {ECO:0000303|PubMed:33372776};
GN   Name=FrzC {ECO:0000303|PubMed:33372776};
OS   Cladobotryum sp.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.
OX   NCBI_TaxID=2040732;
```

Source SHA-256: `9364b021301c1c0c3fb659db92b723838ee62210edc6aa3fb3422781d6bcadb6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1I4?format=txt&versions=18)  
**Locator:** `lines 57-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:47.051386+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(S,S)-2,5-di-(p-hydroxybenzyl)piperazine + reduced [NADPH--
CC         hemoprotein reductase] + O2 = (1S,4S)-4-[(4-hydroxyphenyl)methyl]-
CC         2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexane]-2',5'-dien-4'-
CC         one + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+);
CC         Xref=Rhea:RHEA:83579, Rhea:RHEA-COMP:11964, Rhea:RHEA-COMP:11965,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:145882,
CC         ChEBI:CHEBI:233174; Evidence={ECO:0000269|PubMed:33372776};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83580;
CC         Evidence={ECO:0000269|PubMed:33372776};
```

Source SHA-256: `9364b021301c1c0c3fb659db92b723838ee62210edc6aa3fb3422781d6bcadb6`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 172. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
