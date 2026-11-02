# catalytic_activity_0181

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ

[Multiple Choices]
A. (S)-norprotosinomenine + S-adenosyl-L-methionine = (S)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)
B. N(6)-acetyl-L-lysyl-[protein] + H2O = L-lysyl-[protein] + acetate
C. an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)
D. deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+)
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

> The exact 552-aa sequence matches the UniProt entry annotated as glutamine-dependent NAD(+) synthetase, and its annotated catalytic reaction is choice D. The reaction annotation is supported by a HAMAP computational rule; the cited paper is described as reporting a disruption phenotype, not a direct catalytic assay.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a glutamine-dependent NAD synthetase architecture: an N-terminal glutamine-amidotransferase-like region with a catalytic cysteine, followed by a larger ATP-dependent synthetase region. That combination supports the coupled glutamine-consuming synthesis represented in D, unlike the methyltransferase, protein deacetylation, or dolichol-linked glycan-transfer reactions in the other choices.


**Missing item-specific fact**

> No indispensable item-specific fact is missing for a defensible family-level inference, though assigning this exact protein family from sequence requires recognizing its conserved domains.


**Reason**

> The sequence and distinct reaction classes provide a biological basis to favor D through enzyme-family and domain reasoning. Reviewer-only database annotations support the key but are not being treated as information supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe substantially different enzyme activities, and the sequence-based family inference favors only the NAD synthetase reaction.


### Important caveats

- The available catalytic-activity annotation is computationally supported by a HAMAP rule, not shown here as direct experimental measurement of the reaction.
- The cited publication concerns a disruption phenotype; it does not by itself establish an experimental assay of the listed catalytic reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a glutamine-dependent NAD synthetase architecture: an N-terminal glutamine-amidotransferase-like region with a catalytic cysteine, followed by a larger ATP-dependent synthetase region. That combination supports the coupled glutamine-consuming synthesis represented in D, unlike the methyltransferase, protein deacetylation, or dolichol-linked glycan-transfer reactions in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No indispensable item-specific fact is missing for a defensible family-level inference, though assigning this exact protein family from sequence requires recognizing its conserved domains.",
    "reason": "The sequence and distinct reaction classes provide a biological basis to favor D through enzyme-family and domain reasoning. Reviewer-only database annotations support the key but are not being treated as information supplied to the evaluated model."
  },
  "case_id": "catalytic_activity_0181",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact 552-aa sequence matches the UniProt entry annotated as glutamine-dependent NAD(+) synthetase, and its annotated catalytic reaction is choice D. The reaction annotation is supported by a HAMAP computational rule; the cited paper is described as reporting a disruption phenotype, not a direct catalytic assay."
  },
  "important_caveats": [
    "The available catalytic-activity annotation is computationally supported by a HAMAP rule, not shown here as direct experimental measurement of the reaction.",
    "The cited publication concerns a disruption phenotype; it does not by itself establish an experimental assay of the listed catalytic reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe substantially different enzyme activities, and the sequence-based family inference favors only the NAD synthetase reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 552-aa sequence matches the UniProt entry annotated as glutamine-dependent NAD(+) synthetase, and its annotated catalytic reaction is choice D. The reaction annotation is supported by a HAMAP computational rule; the cited paper is described as reporting a disruption phenotype, not a direct catalytic assay.",
    "evidence_ids": ["C1", "C4", "C5", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a glutamine-dependent NAD synthetase architecture: an N-terminal glutamine-amidotransferase-like region with a catalytic cysteine, followed by a larger ATP-dependent synthetase region. That combination supports the coupled glutamine-consuming synthesis represented in D, unlike the methyltransferase, protein deacetylation, or dolichol-linked glycan-transfer reactions in the other choices.",
    "missing_item_specific_fact": "No indispensable item-specific fact is missing for a defensible family-level inference, though assigning this exact protein family from sequence requires recognizing its conserved domains.",
    "reason": "The sequence and distinct reaction classes provide a biological basis to favor D through enzyme-family and domain reasoning. Reviewer-only database annotations support the key but are not being treated as information supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe substantially different enzyme activities, and the sequence-based family inference favors only the NAD synthetase reaction."
  },
  "important_caveats": [
    "The available catalytic-activity annotation is computationally supported by a HAMAP rule, not shown here as direct experimental measurement of the reaction.",
    "The cited publication concerns a disruption phenotype; it does not by itself establish an experimental assay of the listed catalytic reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A0H2X6L3 (NADE_XANC8) from Xanthomonas campestris pv. campestris strain 8004, annotated as Glutamine-dependent NAD(+) synthetase (EC 6.3.5.1). The UniProt CATALYTIC ACTIVITY annotation (evidence code ECO:0000255, HAMAP-Rule MF_02090) states exactly the reaction in choice D. A 2024 PubMed reference (38429435) provides structural and disruption-phenotype experimental support for NadE function in this organism. Sequence match is confirmed (SHA-256 identical, 552 aa).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable glutamine amidotransferase domain features: an early Cys-Glu pair ('CEQALARIAAATRG' near the N-terminus) and a 'GDMCG' motif near position ~430 consistent with the catalytic Cys-His-Glu triad of the glutaminase subdomain. Among the four choices, only D involves L-glutamine as a substrate (a glutamine-hydrolyzing synthetase reaction). Options A (SAM-dependent methyltransferase), B (protein deacetylase/hydrolase), and C (oligosaccharyltransferase) are mechanistically incompatible with a glutamine amidotransferase fold. Thus, identifying the glutaminase domain from sequence motifs is sufficient to eliminate A, B, and C and select D.


**Missing item-specific fact**

> None critical. Recognizing the glutamine amidotransferase superfamily motifs and noting that only one choice involves glutamine-dependent chemistry constitutes general biochemistry reasoning. The specific identification as NadE (rather than, say, GMP synthase) is not needed because no other option involves glutamine.


**Reason**

> A model with knowledge of glutamine amidotransferase sequence signatures (Cys-His-Glu triad, 'GxCG' motif) can observe these in the supplied sequence and use the substrate logic (only D uses glutamine) to select the answer without memorizing this particular protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different enzyme classes (methyltransferase, hydrolase, glycosyltransferase, ligase/synthetase). The presence of glutamine amidotransferase motifs in the sequence uniquely points to D, as it is the only option requiring glutamine as a substrate. No other choice is mechanistically compatible with the observed domain architecture.


### Important caveats

- The primary annotation evidence is HAMAP-Rule (ECO:0000255), a computational rule-based inference, though the 2024 PubMed paper provides experimental structural and genetic disruption data supporting NadE function in this strain.
- The sequence-to-NadE identification relies on recognizing glutamine amidotransferase family motifs; a model lacking this specific domain knowledge might struggle, though the substrate logic (only D uses glutamine) provides a strong secondary discriminator.
- The accession was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable glutamine amidotransferase domain features: an early Cys-Glu pair ('CEQALARIAAATRG' near the N-terminus) and a 'GDMCG' motif near position ~430 consistent with the catalytic Cys-His-Glu triad of the glutaminase subdomain. Among the four choices, only D involves L-glutamine as a substrate (a glutamine-hydrolyzing synthetase reaction). Options A (SAM-dependent methyltransferase), B (protein deacetylase/hydrolase), and C (oligosaccharyltransferase) are mechanistically incompatible with a glutamine amidotransferase fold. Thus, identifying the glutaminase domain from sequence motifs is sufficient to eliminate A, B, and C and select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing the glutamine amidotransferase superfamily motifs and noting that only one choice involves glutamine-dependent chemistry constitutes general biochemistry reasoning. The specific identification as NadE (rather than, say, GMP synthase) is not needed because no other option involves glutamine.",
    "reason": "A model with knowledge of glutamine amidotransferase sequence signatures (Cys-His-Glu triad, 'GxCG' motif) can observe these in the supplied sequence and use the substrate logic (only D uses glutamine) to select the answer without memorizing this particular protein's database entry."
  },
  "case_id": "catalytic_activity_0181",
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
    "reason": "The sequence matches UniProt entry A0A0H2X6L3 (NADE_XANC8) from Xanthomonas campestris pv. campestris strain 8004, annotated as Glutamine-dependent NAD(+) synthetase (EC 6.3.5.1). The UniProt CATALYTIC ACTIVITY annotation (evidence code ECO:0000255, HAMAP-Rule MF_02090) states exactly the reaction in choice D. A 2024 PubMed reference (38429435) provides structural and disruption-phenotype experimental support for NadE function in this organism. Sequence match is confirmed (SHA-256 identical, 552 aa)."
  },
  "important_caveats": [
    "The primary annotation evidence is HAMAP-Rule (ECO:0000255), a computational rule-based inference, though the 2024 PubMed paper provides experimental structural and genetic disruption data supporting NadE function in this strain.",
    "The sequence-to-NadE identification relies on recognizing glutamine amidotransferase family motifs; a model lacking this specific domain knowledge might struggle, though the substrate logic (only D uses glutamine) provides a strong secondary discriminator.",
    "The accession was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (methyltransferase, hydrolase, glycosyltransferase, ligase/synthetase). The presence of glutamine amidotransferase motifs in the sequence uniquely points to D, as it is the only option requiring glutamine as a substrate. No other choice is mechanistically compatible with the observed domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0181",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A0H2X6L3 (NADE_XANC8) from Xanthomonas campestris pv. campestris strain 8004, annotated as Glutamine-dependent NAD(+) synthetase (EC 6.3.5.1). The UniProt CATALYTIC ACTIVITY annotation (evidence code ECO:0000255, HAMAP-Rule MF_02090) states exactly the reaction in choice D. A 2024 PubMed reference (38429435) provides structural and disruption-phenotype experimental support for NadE function in this organism. Sequence match is confirmed (SHA-256 identical, 552 aa).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable glutamine amidotransferase domain features: an early Cys-Glu pair ('CEQALARIAAATRG' near the N-terminus) and a 'GDMCG' motif near position ~430 consistent with the catalytic Cys-His-Glu triad of the glutaminase subdomain. Among the four choices, only D involves L-glutamine as a substrate (a glutamine-hydrolyzing synthetase reaction). Options A (SAM-dependent methyltransferase), B (protein deacetylase/hydrolase), and C (oligosaccharyltransferase) are mechanistically incompatible with a glutamine amidotransferase fold. Thus, identifying the glutaminase domain from sequence motifs is sufficient to eliminate A, B, and C and select D.",
    "missing_item_specific_fact": "None critical. Recognizing the glutamine amidotransferase superfamily motifs and noting that only one choice involves glutamine-dependent chemistry constitutes general biochemistry reasoning. The specific identification as NadE (rather than, say, GMP synthase) is not needed because no other option involves glutamine.",
    "reason": "A model with knowledge of glutamine amidotransferase sequence signatures (Cys-His-Glu triad, 'GxCG' motif) can observe these in the supplied sequence and use the substrate logic (only D uses glutamine) to select the answer without memorizing this particular protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (methyltransferase, hydrolase, glycosyltransferase, ligase/synthetase). The presence of glutamine amidotransferase motifs in the sequence uniquely points to D, as it is the only option requiring glutamine as a substrate. No other choice is mechanistically compatible with the observed domain architecture."
  },
  "important_caveats": [
    "The primary annotation evidence is HAMAP-Rule (ECO:0000255), a computational rule-based inference, though the 2024 PubMed paper provides experimental structural and genetic disruption data supporting NadE function in this strain.",
    "The sequence-to-NadE identification relies on recognizing glutamine amidotransferase family motifs; a model lacking this specific domain knowledge might struggle, though the substrate logic (only D uses glutamine) provides a strong secondary discriminator.",
    "The accession was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone."
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

**Accession:** `A0A0H2X6L3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 49. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
"A0A0H2X6L3"
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"NAD(+) synthase [glutamine-hydrolyzing]"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NAD(+) synthetase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NADS"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"6.3.5.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"Glutamine-dependent NAD(+) synthetase"}}}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"6.3.5.1","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"name":"deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24384"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29985"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:33019"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:58359"},{"database":"ChEBI","id":"CHEBI:58437"},{"database":"ChEBI","id":"CHEBI:456215"}]}}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"citation":{"authors":["Xu G.","Ma J.","Fang Q.","Peng Q.","Jiao X.","Hu W.","Zhao Q.","Kong Y.","Liu F.","Shi X.","Tang D.J.","Tang J.L.","Ming Z."],"citationCrossReferences":[{"database":"PubMed","id":"38429435"},{"database":"DOI","id":"10.1038/s42003-024-05921-3"}],"citationType":"journal article","firstPage":"255","id":"38429435","journal":"Commun. Biol.","lastPage":"255","publicationDate":"2024","title":"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.","volume":"7"},"referenceComments":[{"type":"STRAIN","value":"8004"}],"referenceNumber":2,"referencePositions":["DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
ID   NADE_XANC8              Reviewed;         552 AA.
AC   A0A0H2X6L3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-SEP-2015, sequence version 1.
DT   28-JAN-2026, entry version 49.
DE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};
DE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};
DE            Short=NADS {ECO:0000303|PubMed:38429435};
GN   Name=nadE {ECO:0000255|HAMAP-Rule:MF_02090};
GN   OrderedLocusNames=XC_1067 {ECO:0000312|EMBL:AAY48137.1};
OS   Xanthomonas campestris pv. campestris (strain 8004).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Lysobacterales; Lysobacteraceae; Xanthomonas.
OX   NCBI_TaxID=314565;
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
DE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};
DE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};
DE            Short=NADS {ECO:0000303|PubMed:38429435};
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 28-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
RN   [2]
RP   DISRUPTION PHENOTYPE.
RC   STRAIN=8004;
RX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;
RA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,
RA   Shi X., Tang D.J., Tang J.L., Ming Z.;
RT   "Structural insights into Xanthomonas campestris pv. campestris NAD+
RT   biosynthesis via the NAM salvage pathway.";
RL   Commun. Biol. 7:255-255(2024).
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 40-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP +
CC         diphosphate + NAD(+) + H(+); Xref=Rhea:RHEA:24384, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29985, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:33019, ChEBI:CHEBI:57540, ChEBI:CHEBI:58359,
CC         ChEBI:CHEBI:58437, ChEBI:CHEBI:456215; EC=6.3.5.1;
CC         Evidence={ECO:0000255|HAMAP-Rule:MF_02090};
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 181. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
