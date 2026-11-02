# catalytic_activity_0045

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDNTPTPQKNPDTNPYASLISQQIAIIPSFTLESGVTLNNVPVAYKTWGKLNEKADNCLVICHALTGSADVEDWWGPLLGLNKAFDPTRFFIFCGNVIGSPYGTISSVTTNPETGKPFGPEMPGSSVKDDVRLHYIILKSLGVRSVAAVVGGSMGGMTVLEYPLNTPPGFVRAIIPLATSARHSAWCISWGEAQRQSIYSDPDYKDGYYYEIEEEGGKVDLARQPARGLAAARMAALLTYRSRDSFESRFGRRAGGGKSSVPKGGVRIMGGQETTDPSVPSESDLAAKSPSWRAWREHNDGHRSAGARPISRSGSEGPAHREGDAAQAEVVKTQDVKANGNKIGTGGEAPPKIFSAQSYLRYQGDKFTGRFDANCYIHITRKLDTHDLSAPSRDTSLSSLSSGLPSSPDATEEELNARLIHALSLEPPALVIGIESDGLFTTSEQRELAAGIPDAELVVIPSPDGHDGFLLEFEAINGWVEGWLKRKMPEFYERRVINPEEYVQGEEGFGIKKESVFGEAEADVTRW

[Multiple Choices]
A. L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA
B. O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate
C. 4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+)
D. 3-oxoadipate + acetyl-CoA = acetoacetate + succinyl-CoA
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

> The supplied sequence exactly matches the UniProt sequence annotated as homoserine O-acetyltransferase, with the L-homoserine + acetyl-CoA reaction recorded as catalytic activity and linked to experimental evidence (ECO:0000269, PubMed 17353245).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a sufficiently specific biological argument to identify this reaction without knowing the protein's function. Generic sequence-based enzyme-family inference would not establish this particular substrate-to-product transformation.


**Missing item-specific fact**

> The protein-specific identification or functional annotation as homoserine O-acetyltransferase, or an experimental determination of its catalytic activity.


**Reason**

> The reviewer-only evidence supports A for this exact sequence, but that annotation and its linked experimental evidence were not included in the evaluated input. Recognizing or looking up the sequence would supply the key fact, rather than reasoning from information given.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported catalytic-activity annotation matches A; the other choices describe different reactions.


### Important caveats

- The sequence match is exact, and the annotation cites experimental evidence, but the primary paper was not independently retrieved and validated here.
- Reviewer-only database evidence supports the expected answer but does not make the question answerable by reasoning from the supplied input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific biological argument to identify this reaction without knowing the protein's function. Generic sequence-based enzyme-family inference would not establish this particular substrate-to-product transformation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification or functional annotation as homoserine O-acetyltransferase, or an experimental determination of its catalytic activity.",
    "reason": "The reviewer-only evidence supports A for this exact sequence, but that annotation and its linked experimental evidence were not included in the evaluated input. Recognizing or looking up the sequence would supply the key fact, rather than reasoning from information given."
  },
  "case_id": "catalytic_activity_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as homoserine O-acetyltransferase, with the L-homoserine + acetyl-CoA reaction recorded as catalytic activity and linked to experimental evidence (ECO:0000269, PubMed 17353245)."
  },
  "important_caveats": [
    "The sequence match is exact, and the annotation cites experimental evidence, but the primary paper was not independently retrieved and validated here.",
    "Reviewer-only database evidence supports the expected answer but does not make the question answerable by reasoning from the supplied input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported catalytic-activity annotation matches A; the other choices describe different reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as homoserine O-acetyltransferase, with the L-homoserine + acetyl-CoA reaction recorded as catalytic activity and linked to experimental evidence (ECO:0000269, PubMed 17353245).",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific biological argument to identify this reaction without knowing the protein's function. Generic sequence-based enzyme-family inference would not establish this particular substrate-to-product transformation.",
    "missing_item_specific_fact": "The protein-specific identification or functional annotation as homoserine O-acetyltransferase, or an experimental determination of its catalytic activity.",
    "reason": "The reviewer-only evidence supports A for this exact sequence, but that annotation and its linked experimental evidence were not included in the evaluated input. Recognizing or looking up the sequence would supply the key fact, rather than reasoning from information given."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported catalytic-activity annotation matches A; the other choices describe different reactions."
  },
  "important_caveats": [
    "The sequence match is exact, and the annotation cites experimental evidence, but the primary paper was not independently retrieved and validated here.",
    "Reviewer-only database evidence supports the expected answer but does not make the question answerable by reasoning from the supplied input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9VIY8 (MET2_CRYN9) for Cryptococcus neoformans matches the supplied 528-aa sequence exactly (SHA256 confirmed). The catalytic activity annotation 'L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA' (EC 2.3.1.31) is backed by experimental evidence (ECO:0000269, PubMed:17353245, a 2007 enzymology paper by Nazi et al.). This is direct experimental evidence, not mere computational inference or transferred annotation. The expected answer A matches the annotated reaction verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains glycine-rich stretches (e.g., 'GGSMGGMTVLEY', 'GRRAGGGKSSVPKGGVRIMGG') that are weakly suggestive of a GNAT (GCN5-related N-acetyltransferase) fold, and the absence of Cys-rich clusters typical of 4Fe-4S ferredoxin-dependent oxidoreductases could weakly argue against option C. However, these signals are too generic and weak to reliably distinguish an acetyltransferase (A) from a phosphothreonine phosphatase (B) or a thiolase (D) on the basis of general biological reasoning from a linear sequence alone.


**Missing item-specific fact**

> The specific identification of this 528-aa sequence as a GNAT-family homoserine O-acetyltransferase (Met2) from Cryptococcus neoformans, annotated with EC 2.3.1.31. This requires either exact sequence recognition tied to a database entry or a trained sequence-to-function predictor; neither constitutes general biological reasoning from the supplied information.


**Reason**

> Distinguishing among four very different enzyme classes (acetyltransferase, phosphatase, oxidoreductase, thiolase) from a raw linear amino acid sequence without structural prediction, homology search, or prior knowledge of this specific protein's annotation is not feasible through general biological reasoning. The glycine-rich motifs are too common across protein families to serve as a reliable discriminator. Correct selection depends on recognizing this specific sequence or recalling its database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent clearly distinct enzyme classes (transferase/acetyltransferase, hydrolase/phosphatase, oxidoreductase, thiolase). Once the correct annotation is known, only A is correct. No ambiguity in the answer key itself.


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269, direct assay), not merely computational inference, strengthening the key's reliability.
- The entry was first released in Swiss-Prot on 2025-02-05; if the benchmark was constructed before that date, the annotation may have been sourced from the 2007 PubMed paper or a TrEMBL entry rather than the Swiss-Prot reviewed record.
- The identity of the protein (J9VIY8 / MET2_CRYN9) was inferred by the reviewer from dataset metadata, not from the model input; the evaluated model received only the raw sequence and choices.
- The GNAT fold identification from sequence alone is a recognized challenge in protein function prediction; this question effectively tests sequence-to-function prediction capability rather than reasoning from first principles.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains glycine-rich stretches (e.g., 'GGSMGGMTVLEY', 'GRRAGGGKSSVPKGGVRIMGG') that are weakly suggestive of a GNAT (GCN5-related N-acetyltransferase) fold, and the absence of Cys-rich clusters typical of 4Fe-4S ferredoxin-dependent oxidoreductases could weakly argue against option C. However, these signals are too generic and weak to reliably distinguish an acetyltransferase (A) from a phosphothreonine phosphatase (B) or a thiolase (D) on the basis of general biological reasoning from a linear sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this 528-aa sequence as a GNAT-family homoserine O-acetyltransferase (Met2) from Cryptococcus neoformans, annotated with EC 2.3.1.31. This requires either exact sequence recognition tied to a database entry or a trained sequence-to-function predictor; neither constitutes general biological reasoning from the supplied information.",
    "reason": "Distinguishing among four very different enzyme classes (acetyltransferase, phosphatase, oxidoreductase, thiolase) from a raw linear amino acid sequence without structural prediction, homology search, or prior knowledge of this specific protein's annotation is not feasible through general biological reasoning. The glycine-rich motifs are too common across protein families to serve as a reliable discriminator. Correct selection depends on recognizing this specific sequence or recalling its database annotation."
  },
  "case_id": "catalytic_activity_0045",
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
    "reason": "The UniProt entry J9VIY8 (MET2_CRYN9) for Cryptococcus neoformans matches the supplied 528-aa sequence exactly (SHA256 confirmed). The catalytic activity annotation 'L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA' (EC 2.3.1.31) is backed by experimental evidence (ECO:0000269, PubMed:17353245, a 2007 enzymology paper by Nazi et al.). This is direct experimental evidence, not mere computational inference or transferred annotation. The expected answer A matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, direct assay), not merely computational inference, strengthening the key's reliability.",
    "The entry was first released in Swiss-Prot on 2025-02-05; if the benchmark was constructed before that date, the annotation may have been sourced from the 2007 PubMed paper or a TrEMBL entry rather than the Swiss-Prot reviewed record.",
    "The identity of the protein (J9VIY8 / MET2_CRYN9) was inferred by the reviewer from dataset metadata, not from the model input; the evaluated model received only the raw sequence and choices.",
    "The GNAT fold identification from sequence alone is a recognized challenge in protein function prediction; this question effectively tests sequence-to-function prediction capability rather than reasoning from first principles."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct enzyme classes (transferase/acetyltransferase, hydrolase/phosphatase, oxidoreductase, thiolase). Once the correct annotation is known, only A is correct. No ambiguity in the answer key itself."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9VIY8 (MET2_CRYN9) for Cryptococcus neoformans matches the supplied 528-aa sequence exactly (SHA256 confirmed). The catalytic activity annotation 'L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA' (EC 2.3.1.31) is backed by experimental evidence (ECO:0000269, PubMed:17353245, a 2007 enzymology paper by Nazi et al.). This is direct experimental evidence, not mere computational inference or transferred annotation. The expected answer A matches the annotated reaction verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains glycine-rich stretches (e.g., 'GGSMGGMTVLEY', 'GRRAGGGKSSVPKGGVRIMGG') that are weakly suggestive of a GNAT (GCN5-related N-acetyltransferase) fold, and the absence of Cys-rich clusters typical of 4Fe-4S ferredoxin-dependent oxidoreductases could weakly argue against option C. However, these signals are too generic and weak to reliably distinguish an acetyltransferase (A) from a phosphothreonine phosphatase (B) or a thiolase (D) on the basis of general biological reasoning from a linear sequence alone.",
    "missing_item_specific_fact": "The specific identification of this 528-aa sequence as a GNAT-family homoserine O-acetyltransferase (Met2) from Cryptococcus neoformans, annotated with EC 2.3.1.31. This requires either exact sequence recognition tied to a database entry or a trained sequence-to-function predictor; neither constitutes general biological reasoning from the supplied information.",
    "reason": "Distinguishing among four very different enzyme classes (acetyltransferase, phosphatase, oxidoreductase, thiolase) from a raw linear amino acid sequence without structural prediction, homology search, or prior knowledge of this specific protein's annotation is not feasible through general biological reasoning. The glycine-rich motifs are too common across protein families to serve as a reliable discriminator. Correct selection depends on recognizing this specific sequence or recalling its database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct enzyme classes (transferase/acetyltransferase, hydrolase/phosphatase, oxidoreductase, thiolase). Once the correct annotation is known, only A is correct. No ambiguity in the answer key itself."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, direct assay), not merely computational inference, strengthening the key's reliability.",
    "The entry was first released in Swiss-Prot on 2025-02-05; if the benchmark was constructed before that date, the annotation may have been sourced from the 2007 PubMed paper or a TrEMBL entry rather than the Swiss-Prot reviewed record.",
    "The identity of the protein (J9VIY8 / MET2_CRYN9) was inferred by the reviewer from dataset metadata, not from the model input; the evaluated model received only the raw sequence and choices.",
    "The GNAT fold identification from sequence alone is a recognized challenge in protein function prediction; this question effectively tests sequence-to-function prediction capability rather than reasoning from first principles."
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

**Accession:** `J9VIY8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
"J9VIY8"
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"value":"2.3.1.31"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Homoserine O-acetyltransferase"}}}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13702"}}],"reaction":{"ecNumber":"2.3.1.31","evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"name":"L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13701"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:57476"},{"database":"ChEBI","id":"CHEBI:57716"}]}}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"citation":{"authors":["Nazi I.","Scott A.","Sham A.","Rossi L.","Williamson P.R.","Kronstad J.W.","Wright G.D."],"citationCrossReferences":[{"database":"PubMed","id":"17353245"},{"database":"DOI","id":"10.1128/aac.01400-06"}],"citationType":"journal article","firstPage":"1731","id":"17353245","journal":"Antimicrob. Agents Chemother.","lastPage":"1736","publicationDate":"2007","title":"Role of homoserine transacetylase as a new target for antifungal agents.","volume":"51"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
DE   RecName: Full=Homoserine O-acetyltransferase {ECO:0000305};
DE            EC=2.3.1.31 {ECO:0000269|PubMed:17353245};
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 35-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION
RP   PHENOTYPE.
RX   PubMed=17353245; DOI=10.1128/aac.01400-06;
RA   Nazi I., Scott A., Sham A., Rossi L., Williamson P.R., Kronstad J.W.,
RA   Wright G.D.;
RT   "Role of homoserine transacetylase as a new target for antifungal agents.";
RL   Antimicrob. Agents Chemother. 51:1731-1736(2007).
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 45-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-homoserine + acetyl-CoA = O-acetyl-L-homoserine + CoA;
CC         Xref=Rhea:RHEA:13701, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,
CC         ChEBI:CHEBI:57476, ChEBI:CHEBI:57716; EC=2.3.1.31;
CC         Evidence={ECO:0000269|PubMed:17353245};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13702;
CC         Evidence={ECO:0000269|PubMed:17353245};
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
