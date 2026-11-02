# catalytic_activity_0040

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKEKGEEKMNDSRKITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRKIERIEKGDSYIPDVSSNVLKDLVQNKQLVVYTPHTGIEEFQNSEYVIVTVPTPINKQKEPDLSALIAASHYIKQNLQAGQTFIFESSTYPGTLEEVIIPIIAQSGKEVGKDYYIGYSPERIDPANQQYTVQTIPKVISGQTERCKQQVQKLYSTIFDTVVPVSSPKVAEMCKLFENIQRLVNISLVNELNILCEKLGIDFREALEAAATKPFGFTPYWPGPGIGGHCIPVDPLYFQWKARQLGQSSQLIEVAHMINEKMPQQIVTQVKELSAPPGTVFLIGIAYKKDVNDLRESPALPIIELLVNEGYKVQYHDPYISSAKIGDKIYDSIPLKKKTLEKADCILIVTDHSNIDWNICKGMKHVIDTRGVLKKVSA

[Multiple Choices]
A. deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+)
B. UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)
C. deacetylisoipecoside + S-adenosyl-L-methionine = 6-O-methyldeacetylisoipecoside + S-adenosyl-L-homocysteine + H(+)
D. L-homocysteine + glycine betaine = N,N-dimethylglycine + L-methionine
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

> The supplied sequence exactly matches the referenced UniProt sequence, whose catalytic-activity annotation gives reaction B and cites experimental evidence (ECO:0000269; PubMed 20529859).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A glycine-rich nucleotide-cofactor-binding pattern and the options' chemistry may suggest an oxidoreductase, favoring B over the transferase-like reactions. That does not establish the specific UDP-sugar substrate or the exact reaction.


**Missing item-specific fact**

> The protein's specific identity or experimentally established substrate and catalytic activity is absent from the input.


**Reason**

> The sequence may support a broad enzyme-class inference, but distinguishing the precise reaction in B requires protein-specific functional information not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reaction types, and the sequence-matched annotation supports B; no other listed reaction is supported by the supplied evidence.


### Important caveats

- The experimental-evidence code and cited paper support the database annotation, but the primary study was not independently reviewed here.
- Reviewer-only sequence identity and annotation were not available to the evaluated model; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A glycine-rich nucleotide-cofactor-binding pattern and the options' chemistry may suggest an oxidoreductase, favoring B over the transferase-like reactions. That does not establish the specific UDP-sugar substrate or the exact reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific identity or experimentally established substrate and catalytic activity is absent from the input.",
    "reason": "The sequence may support a broad enzyme-class inference, but distinguishing the precise reaction in B requires protein-specific functional information not supplied in the question."
  },
  "case_id": "catalytic_activity_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the referenced UniProt sequence, whose catalytic-activity annotation gives reaction B and cites experimental evidence (ECO:0000269; PubMed 20529859)."
  },
  "important_caveats": [
    "The experimental-evidence code and cited paper support the database annotation, but the primary study was not independently reviewed here.",
    "Reviewer-only sequence identity and annotation were not available to the evaluated model; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the sequence-matched annotation supports B; no other listed reaction is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the referenced UniProt sequence, whose catalytic-activity annotation gives reaction B and cites experimental evidence (ECO:0000269; PubMed 20529859).",
    "evidence_ids": ["C1", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A glycine-rich nucleotide-cofactor-binding pattern and the options' chemistry may suggest an oxidoreductase, favoring B over the transferase-like reactions. That does not establish the specific UDP-sugar substrate or the exact reaction.",
    "missing_item_specific_fact": "The protein's specific identity or experimentally established substrate and catalytic activity is absent from the input.",
    "reason": "The sequence may support a broad enzyme-class inference, but distinguishing the precise reaction in B requires protein-specific functional information not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the sequence-matched annotation supports B; no other listed reaction is supported by the supplied evidence."
  },
  "important_caveats": [
    "The experimental-evidence code and cited paper support the database annotation, but the primary study was not independently reviewed here.",
    "Reviewer-only sequence identity and annotation were not available to the evaluated model; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (423 AA, SHA256 matched) corresponds exactly to UniProt A7GKX6, annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136). The catalytic activity annotation (C5, H4) states the reaction 'UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)', which is identical to Choice B. The annotation is backed by experimental evidence (ECO:0000269, PubMed 20529859, Gu et al. 2010 JBC), not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal region 'TVIGLGYVGLPLAIHFAERGYNVVGL' contains a Rossmann-fold-like GxGxxG motif (G-Y-V-G-L-P), suggesting NAD-binding dehydrogenase activity. This weakly disfavors Choice C (methyltransferase, SAM-dependent) and Choice D (methionine synthase, cobalamin-dependent), and to a lesser extent Choice A (NAD synthetase, ATP-dependent synthetase rather than dehydrogenase). However, this generic Rossmann-fold inference cannot identify the specific substrate (UDP-GlcNAc) or the precise 6-dehydrogenation mechanism requiring two NAD+ molecules.


**Missing item-specific fact**

> The specific identification of this protein as a UDP-GlcNAc 6-dehydrogenase (EC 1.1.1.136) acting on UDP-N-acetyl-alpha-D-glucosamine at C6, rather than any other NAD-dependent dehydrogenase, requires knowledge of the UDP-sugar dehydrogenase family's catalytic residues and substrate-binding pocket. This is a rare enzyme characterized in a 2010 paper; the substrate specificity and stoichiometry (2 NAD+ per reaction) are not derivable from general sequence features.


**Reason**

> While the Rossmann-fold motif provides a weak hint toward dehydrogenase activity (narrowing from four choices to roughly two), the precise reaction—oxidation of UDP-GlcNAc at C6 to yield UDP-GlcNAcA with 2 NAD+ as electron acceptors—is an item-specific enzymological fact. No general biological reasoning from a 423-residue bacterial sequence can uniquely identify this substrate and this specific two-electron/two-NAD+ oxidation without database lookup or memorization of the EC 1.1.1.136 reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (NAD synthetase, UDP-sugar dehydrogenase, O-methyltransferase, methionine synthase). Given the correct annotation, only B is correct. The choices are not ambiguous with respect to the ground truth; the difficulty lies in determining the correct answer from sequence alone, not in distinguishing between equally plausible options.


### Important caveats

- The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed 20529859), not just computational prediction.
- The sequence match is exact (SHA256 identical) across both current and historical (entry version 96) UniProt records.
- The Rossmann-fold motif in the N-terminus provides only a very generic 'dehydrogenase-like' signal shared by thousands of unrelated enzymes; it does not constitute reasoning that identifies EC 1.1.1.136 specifically.
- The entry was first publicly released in 2025-02-05; if the benchmark was constructed before that date, the annotation may not have been available in public databases at construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'TVIGLGYVGLPLAIHFAERGYNVVGL' contains a Rossmann-fold-like GxGxxG motif (G-Y-V-G-L-P), suggesting NAD-binding dehydrogenase activity. This weakly disfavors Choice C (methyltransferase, SAM-dependent) and Choice D (methionine synthase, cobalamin-dependent), and to a lesser extent Choice A (NAD synthetase, ATP-dependent synthetase rather than dehydrogenase). However, this generic Rossmann-fold inference cannot identify the specific substrate (UDP-GlcNAc) or the precise 6-dehydrogenation mechanism requiring two NAD+ molecules.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this protein as a UDP-GlcNAc 6-dehydrogenase (EC 1.1.1.136) acting on UDP-N-acetyl-alpha-D-glucosamine at C6, rather than any other NAD-dependent dehydrogenase, requires knowledge of the UDP-sugar dehydrogenase family's catalytic residues and substrate-binding pocket. This is a rare enzyme characterized in a 2010 paper; the substrate specificity and stoichiometry (2 NAD+ per reaction) are not derivable from general sequence features.",
    "reason": "While the Rossmann-fold motif provides a weak hint toward dehydrogenase activity (narrowing from four choices to roughly two), the precise reaction—oxidation of UDP-GlcNAc at C6 to yield UDP-GlcNAcA with 2 NAD+ as electron acceptors—is an item-specific enzymological fact. No general biological reasoning from a 423-residue bacterial sequence can uniquely identify this substrate and this specific two-electron/two-NAD+ oxidation without database lookup or memorization of the EC 1.1.1.136 reaction."
  },
  "case_id": "catalytic_activity_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence (423 AA, SHA256 matched) corresponds exactly to UniProt A7GKX6, annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136). The catalytic activity annotation (C5, H4) states the reaction 'UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)', which is identical to Choice B. The annotation is backed by experimental evidence (ECO:0000269, PubMed 20529859, Gu et al. 2010 JBC), not merely computational inference."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed 20529859), not just computational prediction.",
    "The sequence match is exact (SHA256 identical) across both current and historical (entry version 96) UniProt records.",
    "The Rossmann-fold motif in the N-terminus provides only a very generic 'dehydrogenase-like' signal shared by thousands of unrelated enzymes; it does not constitute reasoning that identifies EC 1.1.1.136 specifically.",
    "The entry was first publicly released in 2025-02-05; if the benchmark was constructed before that date, the annotation may not have been available in public databases at construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (NAD synthetase, UDP-sugar dehydrogenase, O-methyltransferase, methionine synthase). Given the correct annotation, only B is correct. The choices are not ambiguous with respect to the ground truth; the difficulty lies in determining the correct answer from sequence alone, not in distinguishing between equally plausible options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (423 AA, SHA256 matched) corresponds exactly to UniProt A7GKX6, annotated as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136). The catalytic activity annotation (C5, H4) states the reaction 'UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)', which is identical to Choice B. The annotation is backed by experimental evidence (ECO:0000269, PubMed 20529859, Gu et al. 2010 JBC), not merely computational inference.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal region 'TVIGLGYVGLPLAIHFAERGYNVVGL' contains a Rossmann-fold-like GxGxxG motif (G-Y-V-G-L-P), suggesting NAD-binding dehydrogenase activity. This weakly disfavors Choice C (methyltransferase, SAM-dependent) and Choice D (methionine synthase, cobalamin-dependent), and to a lesser extent Choice A (NAD synthetase, ATP-dependent synthetase rather than dehydrogenase). However, this generic Rossmann-fold inference cannot identify the specific substrate (UDP-GlcNAc) or the precise 6-dehydrogenation mechanism requiring two NAD+ molecules.",
    "missing_item_specific_fact": "The specific identification of this protein as a UDP-GlcNAc 6-dehydrogenase (EC 1.1.1.136) acting on UDP-N-acetyl-alpha-D-glucosamine at C6, rather than any other NAD-dependent dehydrogenase, requires knowledge of the UDP-sugar dehydrogenase family's catalytic residues and substrate-binding pocket. This is a rare enzyme characterized in a 2010 paper; the substrate specificity and stoichiometry (2 NAD+ per reaction) are not derivable from general sequence features.",
    "reason": "While the Rossmann-fold motif provides a weak hint toward dehydrogenase activity (narrowing from four choices to roughly two), the precise reaction—oxidation of UDP-GlcNAc at C6 to yield UDP-GlcNAcA with 2 NAD+ as electron acceptors—is an item-specific enzymological fact. No general biological reasoning from a 423-residue bacterial sequence can uniquely identify this substrate and this specific two-electron/two-NAD+ oxidation without database lookup or memorization of the EC 1.1.1.136 reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (NAD synthetase, UDP-sugar dehydrogenase, O-methyltransferase, methionine synthase). Given the correct annotation, only B is correct. The choices are not ambiguous with respect to the ground truth; the difficulty lies in determining the correct answer from sequence alone, not in distinguishing between equally plausible options."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (ECO:0000269, PubMed 20529859), not just computational prediction.",
    "The sequence match is exact (SHA256 identical) across both current and historical (entry version 96) UniProt records.",
    "The Rossmann-fold motif in the N-terminus provides only a very generic 'dehydrogenase-like' signal shared by thousands of unrelated enzymes; it does not constitute reasoning that identifies EC 1.1.1.136 specifically.",
    "The entry was first publicly released in 2025-02-05; if the benchmark was constructed before that date, the annotation may not have been available in public databases at construction time."
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

**Accession:** `A7GKX6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 96. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
"A7GKX6"
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"value":"1.1.1.136"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-N-acetyl-D-glucosamine 6-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-GlcNAc 6-dehydrogenase"}]}}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13326"}}],"reaction":{"ecNumber":"1.1.1.136","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13325"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:65040"}]}}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"citation":{"authors":["Gu X.","Glushka J.","Lee S.G.","Bar-Peled M."],"citationCrossReferences":[{"database":"PubMed","id":"20529859"},{"database":"DOI","id":"10.1074/jbc.m110.125872"}],"citationType":"journal article","firstPage":"24825","id":"20529859","journal":"J. Biol. Chem.","lastPage":"24833","publicationDate":"2010","title":"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.","volume":"285"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ADE43879.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
DE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000303|PubMed:20529859};
DE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000303|PubMed:20529859};
DE            EC=1.1.1.136 {ECO:0000269|PubMed:20529859};
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 26-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
RN   [2] {ECO:0000312|EMBL:ADE43879.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND CATALYTIC ACTIVITY.
RC   STRAIN=DSM 22905 / CIP 110041 / 391-98 / NVH 391-98;
RX   PubMed=20529859; DOI=10.1074/jbc.m110.125872;
RA   Gu X., Glushka J., Lee S.G., Bar-Peled M.;
RT   "Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the
RT   human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.";
RL   J. Biol. Chem. 285:24825-24833(2010).
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-
CC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);
CC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:65040; EC=1.1.1.136;
CC         Evidence={ECO:0000269|PubMed:20529859};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;
CC         Evidence={ECO:0000269|PubMed:20529859};
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 40. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
