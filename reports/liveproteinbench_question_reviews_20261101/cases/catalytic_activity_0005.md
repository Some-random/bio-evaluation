# catalytic_activity_0005

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — S-ubiquitinyl-&#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + &#91;acceptor protein&#93;-L-lysine = &#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + N(6)-ubiquitinyl-&#91;acceptor protein&#93;-L-lysine.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPIMLNFSNGRILPESEVEALRNVARSNQSDVLLVGSRSLRLHHISFMDGFSVEPIPGSFLDRIGERRHRRLAESLERQLNGGSSFLQAFSQYIEQTSSAPPLQESVRNEVQSRVNSYAFSVNPGDFPCSVLHLSCPITLCVPETGVFVKNARCSKVCSLYDISALTEMLRRNASHPLSREAFTPGMIVHKEECNFNTTEQHFCILPRSDTRL

[Multiple Choices]
A. (1S,3S,6S,7S,8R)-7-hydroxy-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecan-9-one + NADPH + H(+) = (1S,3S,6S,7S,8S,9S)-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecane-7,9-diol + NADP(+)
B. S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.
C. 3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
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

> The exact 213-aa sequence matches the UniProt entry annotated as E3 ubiquitin-protein ligase NleG8, whose catalytic-activity annotation gives choice B. The annotation cites experimental evidence (ECO:0000269, PubMed 36511702), though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme activities, but the supplied sequence and context do not provide a clear, general biological feature that identifies this protein's specific reaction as ubiquitin transfer from E2 to a lysine acceptor.


**Missing item-specific fact**

> The protein-specific identity or functional annotation as NleG8, an E3 ubiquitin-protein ligase catalyzing the reaction in choice B.


**Reason**

> Selecting B depends on knowing or retrieving the function of this particular protein; recognizing the sequence or invoking a predictor would not constitute reasoning from information supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify distinct reactions, and the matched protein annotation supports B.


### Important caveats

- The UniProt annotation matches the supplied sequence and cites experimental evidence, but the primary publication was not independently validated here.
- Reviewer-only database evidence supports the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the supplied sequence and context do not provide a clear, general biological feature that identifies this protein's specific reaction as ubiquitin transfer from E2 to a lysine acceptor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation as NleG8, an E3 ubiquitin-protein ligase catalyzing the reaction in choice B.",
    "reason": "Selecting B depends on knowing or retrieving the function of this particular protein; recognizing the sequence or invoking a predictor would not constitute reasoning from information supplied in the question."
  },
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 213-aa sequence matches the UniProt entry annotated as E3 ubiquitin-protein ligase NleG8, whose catalytic-activity annotation gives choice B. The annotation cites experimental evidence (ECO:0000269, PubMed 36511702), though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt annotation matches the supplied sequence and cites experimental evidence, but the primary publication was not independently validated here.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct reactions, and the matched protein annotation supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 213-aa sequence matches the UniProt entry annotated as E3 ubiquitin-protein ligase NleG8, whose catalytic-activity annotation gives choice B. The annotation cites experimental evidence (ECO:0000269, PubMed 36511702), though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the supplied sequence and context do not provide a clear, general biological feature that identifies this protein's specific reaction as ubiquitin transfer from E2 to a lysine acceptor.",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation as NleG8, an E3 ubiquitin-protein ligase catalyzing the reaction in choice B.",
    "reason": "Selecting B depends on knowing or retrieving the function of this particular protein; recognizing the sequence or invoking a predictor would not constitute reasoning from information supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct reactions, and the matched protein annotation supports B."
  },
  "important_caveats": [
    "The UniProt annotation matches the supplied sequence and cites experimental evidence, but the primary publication was not independently validated here.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt entry A0A482PJY4 (NLEG8_CITRO, 213 aa, SHA256 match). The entry is annotated as E3 ubiquitin-protein ligase NleG8 with EC 2.3.2.27, and the catalytic activity annotation (evidence code ECO:0000269, experimental, from PubMed 36511702) states exactly the reaction in choice B: S-ubiquitinyl-&#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + &#91;acceptor protein&#93;-L-lysine = &#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + N(6)-ubiquitinyl-&#91;acceptor protein&#93;-L-lysine.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal region contains a cysteine-rich pattern (CPITLCVPETGVFVKNARCSKVCSLYDISALTEMLRRNASHPLSREAFTPGMIVHKEECNFNTTEQHFCILPRSDTRL) that could in principle be recognized as a U-box domain fold, which is characteristic of E3 ubiquitin ligases. However, recognizing this specific cysteine arrangement as a U-box (rather than a RING or other zinc-binding motif) from a raw 213-aa bacterial sequence without organism or structural context requires specialized domain-architecture knowledge. The four choices span very different enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), but no obvious positive or negative motifs in the sequence definitively eliminate A, C, or D through general reasoning alone.


**Missing item-specific fact**

> The specific identification of this sequence as an NleG-family U-box E3 ligase from Citrobacter rodentium, or the ability to recognize the U-box domain fold from this particular cysteine spacing pattern without prior knowledge of the NleG protein family, is not derivable from general biological reasoning applied to the bare sequence.


**Reason**

> The input provides only a 213-aa sequence with no organism, gene name, or functional context. While the four choices represent different enzyme classes, the sequence does not contain widely recognizable motifs (e.g., a canonical kinase catalytic loop, a methyltransferase Rossmann fold, or a clear NADPH-binding site) that would allow confident elimination of distractors through general reasoning. Correct identification depends on recognizing the U-box domain architecture specific to the NleG family, which is specialized structural biology knowledge rather than general biological inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent clearly distinct enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), so they are not ambiguous with respect to each other. The question is well-formed in that only one answer is correct per the database annotation.


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269, PubMed 36511702), strengthening the key beyond mere computational annotation.
- The sequence is from Citrobacter rodentium (a bacterial pathogen), making the NleG effector family context important but absent from the model input.
- The reviewer-only accession (A0A482PJY4) was inferred from dataset metadata and was not available to the evaluated model.
- The U-box domain in NleG proteins is structurally validated (PDB structures exist for family members), but this structural knowledge is not provided in the question input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains a cysteine-rich pattern (CPITLCVPETGVFVKNARCSKVCSLYDISALTEMLRRNASHPLSREAFTPGMIVHKEECNFNTTEQHFCILPRSDTRL) that could in principle be recognized as a U-box domain fold, which is characteristic of E3 ubiquitin ligases. However, recognizing this specific cysteine arrangement as a U-box (rather than a RING or other zinc-binding motif) from a raw 213-aa bacterial sequence without organism or structural context requires specialized domain-architecture knowledge. The four choices span very different enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), but no obvious positive or negative motifs in the sequence definitively eliminate A, C, or D through general reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this sequence as an NleG-family U-box E3 ligase from Citrobacter rodentium, or the ability to recognize the U-box domain fold from this particular cysteine spacing pattern without prior knowledge of the NleG protein family, is not derivable from general biological reasoning applied to the bare sequence.",
    "reason": "The input provides only a 213-aa sequence with no organism, gene name, or functional context. While the four choices represent different enzyme classes, the sequence does not contain widely recognizable motifs (e.g., a canonical kinase catalytic loop, a methyltransferase Rossmann fold, or a clear NADPH-binding site) that would allow confident elimination of distractors through general reasoning. Correct identification depends on recognizing the U-box domain architecture specific to the NleG family, which is specialized structural biology knowledge rather than general biological inference."
  },
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A482PJY4 (NLEG8_CITRO, 213 aa, SHA256 match). The entry is annotated as E3 ubiquitin-protein ligase NleG8 with EC 2.3.2.27, and the catalytic activity annotation (evidence code ECO:0000269, experimental, from PubMed 36511702) states exactly the reaction in choice B: S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed 36511702), strengthening the key beyond mere computational annotation.",
    "The sequence is from Citrobacter rodentium (a bacterial pathogen), making the NleG effector family context important but absent from the model input.",
    "The reviewer-only accession (A0A482PJY4) was inferred from dataset metadata and was not available to the evaluated model.",
    "The U-box domain in NleG proteins is structurally validated (PDB structures exist for family members), but this structural knowledge is not provided in the question input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent clearly distinct enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), so they are not ambiguous with respect to each other. The question is well-formed in that only one answer is correct per the database annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A482PJY4 (NLEG8_CITRO, 213 aa, SHA256 match). The entry is annotated as E3 ubiquitin-protein ligase NleG8 with EC 2.3.2.27, and the catalytic activity annotation (evidence code ECO:0000269, experimental, from PubMed 36511702) states exactly the reaction in choice B: S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal region contains a cysteine-rich pattern (CPITLCVPETGVFVKNARCSKVCSLYDISALTEMLRRNASHPLSREAFTPGMIVHKEECNFNTTEQHFCILPRSDTRL) that could in principle be recognized as a U-box domain fold, which is characteristic of E3 ubiquitin ligases. However, recognizing this specific cysteine arrangement as a U-box (rather than a RING or other zinc-binding motif) from a raw 213-aa bacterial sequence without organism or structural context requires specialized domain-architecture knowledge. The four choices span very different enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), but no obvious positive or negative motifs in the sequence definitively eliminate A, C, or D through general reasoning alone.",
    "missing_item_specific_fact": "The specific identification of this sequence as an NleG-family U-box E3 ligase from Citrobacter rodentium, or the ability to recognize the U-box domain fold from this particular cysteine spacing pattern without prior knowledge of the NleG protein family, is not derivable from general biological reasoning applied to the bare sequence.",
    "reason": "The input provides only a 213-aa sequence with no organism, gene name, or functional context. While the four choices represent different enzyme classes, the sequence does not contain widely recognizable motifs (e.g., a canonical kinase catalytic loop, a methyltransferase Rossmann fold, or a clear NADPH-binding site) that would allow confident elimination of distractors through general reasoning. Correct identification depends on recognizing the U-box domain architecture specific to the NleG family, which is specialized structural biology knowledge rather than general biological inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent clearly distinct enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), so they are not ambiguous with respect to each other. The question is well-formed in that only one answer is correct per the database annotation."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed 36511702), strengthening the key beyond mere computational annotation.",
    "The sequence is from Citrobacter rodentium (a bacterial pathogen), making the NleG effector family context important but absent from the model input.",
    "The reviewer-only accession (A0A482PJY4) was inferred from dataset metadata and was not available to the evaluated model.",
    "The U-box domain in NleG proteins is structurally validated (PDB structures exist for family members), but this structural knowledge is not provided in the question input."
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

**Accession:** `A0A482PJY4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:20.391051+00:00.  

```json
"A0A482PJY4"
```

Source SHA-256: `b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:20.391051+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36511702","source":"PubMed"}],"value":"2.3.2.27"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"E3 ubiquitin-protein ligase NleG8"}}}
```

Source SHA-256: `b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:20.391051+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.2.27","evidences":[{"evidenceCode":"ECO:0000269","id":"36511702","source":"PubMed"}],"name":"S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine."}}
```

Source SHA-256: `b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:20.391051+00:00.  

```json
{"citation":{"authors":["Popov G.","Fiebig-Comyn A.","Syriste L.","Little D.J.","Skarina T.","Stogios P.J.","Birstonas S.","Coombes B.K.","Savchenko A."],"citationCrossReferences":[{"database":"PubMed","id":"36511702"},{"database":"DOI","id":"10.1128/iai.00505-22"}],"citationType":"journal article","firstPage":"e0050522","id":"36511702","journal":"Infect. Immun.","lastPage":"e0050522","publicationDate":"2023","title":"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for Different Roles during Citrobacter rodentium Infection in Mice.","volume":"91"},"referenceComments":[{"type":"STRAIN","value":"DBS100"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBUNIT","INTERACTION WITH HOST GOPC","SUBCELLULAR LOCATION","INDUCTION","DOMAIN","DISRUPTION PHENOTYPE","MOTIF","MUTAGENESIS OF ILE-138 AND 210-ASP--LEU-213"]}
```

Source SHA-256: `b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:23.897522+00:00.  

```text
DE   RecName: Full=E3 ubiquitin-protein ligase NleG8 {ECO:0000305};
DE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};
```

Source SHA-256: `2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)  
**Locator:** `lines 47-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:23.897522+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine +
CC         [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-
CC         cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.;
CC         EC=2.3.2.27; Evidence={ECO:0000269|PubMed:36511702};
```

Source SHA-256: `2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
