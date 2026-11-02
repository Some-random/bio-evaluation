# catalytic_activity_0132

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3&#x27;-5&#x27; direction.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPAATDLANAWFAKRGWKPFAFQRRVWAAVERGESGLLHASTGAGKTYAVWLAALRAFKPRPQGRHLAPIQVLWVTPMRALAADTARALQAPLDELQLPWSVGVRSGDTNSAERARQARRLPSVLITTPESLTLLLTRAKAREDFATLQLVVVDEWHELLGNKRGVQLQLALARLRHWHPGLPTWGLSATLGNLQHARDVLLPQGGLLVQGRQDKALQVDTLLPKAIERFPWAGHMGLKMLDQVCHEIDASASSLVFTNTRAQAEIWYQALLEARPDWAGLIALHHASLARDTRDWVERSLKQGSLKAVICTSSLDLGVDFLPVERVLQIGSAKGIARLMQRAGRSGHAPGRRSRVTLVPTHSLELVEAAAARQALLAGHIEARFSPRLCMDVLVQHLVSMALGSGFRPEQLLAEVRSTWAFRQLRDSQWQWALDFVCHGGSSLTAYPDYQRVERQADGVYRVTSERLARRHRMGIGTIVSDANLQLKYWSKGGGGKTLGSVEEAFIARLRPGDTLVFAGRVLELVRVENMTAYVRRSTARKAAVARWNGGRMPLSSELADALVEQLDAAAHERFEGPEMRAVRPLLALQAQWSALPTTSTLLAETFKSRQGWHLFLYPFAGRMANLGLANLIAWRVSRAQPLSVSIAVNDYGFELLSPAQVDWASHLPQALGTADLLEDVLASLNAGEMALRRFREIAQIAGLVFGGYPAAQKSTRQIQASSGLFYEVFRKHDAGNLLLGQARDEVLSEELEIERLHRQLLKMSELQLDLQALRRPGPLAFALLVEGMRETLSTEKLADRIARMVAELEQAANAG

[Multiple Choices]
A. Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction.
B. (1S,4S)-4-[(4-methoxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
C. (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-methionine = (1S,4S)-4-[(4-methoxyphenyl)methyl]-2-methyl-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + S-adenosyl-L-homocysteine + H(+)
D. L-methionine(in) = L-methionine(out)
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

> The exact sequence matches the UniProt entry for ATP-dependent helicase Lhr-Core, whose catalytic-activity annotation gives the reaction in choice A and cites experimental evidence (ECO:0000269). This supports the key for this sequence, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence may offer clues to an ATP-dependent helicase, making A more plausible than the methyltransferase and transporter alternatives. But those clues do not establish this protein's DNA-unwinding activity or its specific 3′-to-5′ direction.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence that this sequence encodes Lhr-Core, a helicase that couples ATP hydrolysis to duplex-DNA unwinding with 3′-to-5′ translocation.


**Reason**

> Choosing the precise reaction requires a protein-specific functional fact not supplied in the question. Recognizing generic helicase-like sequence features would not by itself determine the stated substrate, coupling, and directionality.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation supports choice A; the other options describe distinct activities.


### Important caveats

- The supporting UniProt annotation is sequence-matched and cites experimental evidence, but the cited primary paper was not independently validated here.
- Reviewer-only accession and annotation information was not present in the original question and does not make the question reasoning-supported.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence may offer clues to an ATP-dependent helicase, making A more plausible than the methyltransferase and transporter alternatives. But those clues do not establish this protein's DNA-unwinding activity or its specific 3′-to-5′ direction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence that this sequence encodes Lhr-Core, a helicase that couples ATP hydrolysis to duplex-DNA unwinding with 3′-to-5′ translocation.",
    "reason": "Choosing the precise reaction requires a protein-specific functional fact not supplied in the question. Recognizing generic helicase-like sequence features would not by itself determine the stated substrate, coupling, and directionality."
  },
  "case_id": "catalytic_activity_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for ATP-dependent helicase Lhr-Core, whose catalytic-activity annotation gives the reaction in choice A and cites experimental evidence (ECO:0000269). This supports the key for this sequence, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The supporting UniProt annotation is sequence-matched and cites experimental evidence, but the cited primary paper was not independently validated here.",
    "Reviewer-only accession and annotation information was not present in the original question and does not make the question reasoning-supported."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports choice A; the other options describe distinct activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for ATP-dependent helicase Lhr-Core, whose catalytic-activity annotation gives the reaction in choice A and cites experimental evidence (ECO:0000269). This supports the key for this sequence, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence may offer clues to an ATP-dependent helicase, making A more plausible than the methyltransferase and transporter alternatives. But those clues do not establish this protein's DNA-unwinding activity or its specific 3′-to-5′ direction.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence that this sequence encodes Lhr-Core, a helicase that couples ATP hydrolysis to duplex-DNA unwinding with 3′-to-5′ translocation.",
    "reason": "Choosing the precise reaction requires a protein-specific functional fact not supplied in the question. Recognizing generic helicase-like sequence features would not by itself determine the stated substrate, coupling, and directionality."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation supports choice A; the other options describe distinct activities."
  },
  "important_caveats": [
    "The supporting UniProt annotation is sequence-matched and cites experimental evidence, but the cited primary paper was not independently validated here.",
    "Reviewer-only accession and annotation information was not present in the original question and does not make the question reasoning-supported."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q88NV1 (LHRC_PSEPK, ATP-dependent helicase Lhr-Core from Pseudomonas putida KT2440) with exact sequence match confirmed in both current and historical entries. The catalytic activity annotation (EC 5.6.2.4) explicitly states 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction,' supported by experimental evidence (ECO:0000269, PubMed:30224353, Ejaz & Shuman 2018). This is direct experimental evidence, not computational inference.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 816-residue sequence contains motifs suggestive of a RecA-like helicase: a Walker B-like motif (VVVDEW in a hydrophobic context), a Motif VI-like 'GSAK' element, and a large RecA-fold-sized architecture. The methyltransferase distractors (B, C) require a Rossmann-like SAM-binding fold (VIGXG motif) and act on highly specific unusual spiro substrates—neither the fold nor the substrate context is evident. The methionine transporter (D) would require multiple transmembrane helices, which are absent from this soluble protein. Among the four choices, only A describes an ATP-dependent nucleic acid motor, consistent with the recognizable helicase motifs. The specific '3'-5' translocation directionality is a database-annotated fact, but since no 5'-3' helicase option is offered, identifying the protein as a helicase is sufficient to select A.


**Missing item-specific fact**

> The precise 3'-5' translocation directionality of Lhr-Core is an experimentally determined property (PubMed:30224353) not trivially deducible from sequence motifs alone; however, this detail is not the distinguishing factor among the provided choices since no opposing-direction helicase option exists.


**Reason**

> A model with general knowledge of RecA-like helicase motifs (Walker B, Motif VI) and the structural requirements of methyltransferases and membrane transporters can meaningfully narrow the choices to A. The distractors belong to entirely different enzyme classes with incompatible structural signatures. The specific directionality embedded in A's text is an annotation fact, but it does not create ambiguity among the offered options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are methyltransferases acting on exotic spiro compounds requiring a Rossmann fold; option D is a membrane transporter. None of these structural or functional features are present in the sequence. Only A (ATP-dependent helicase) is consistent with the observable RecA-like motifs and the protein's soluble, large-domain architecture.


### Important caveats

- The specific '3'-5' directionality in option A is an experimentally determined annotation (ECO:0000269) and is not independently derivable from sequence motifs alone; however, this does not affect answer selection because no 5'-3' helicase alternative is provided.
- The Walker A motif in this sequence is degenerate and not a textbook GxxxxGKT; identification relies on a combination of Walker B (VVVDEW), Motif VI (GSAK), and overall RecA-fold architecture.
- The methyltransferase substrates in B and C are highly unusual spiro compounds; even if a model recognized a SAM-binding motif, these specific substrates would be implausible without the exact enzyme identity.
- Sequence match to Q88NV1 is confirmed (SHA-256 match, 816 AA, both current and historical entries).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 816-residue sequence contains motifs suggestive of a RecA-like helicase: a Walker B-like motif (VVVDEW in a hydrophobic context), a Motif VI-like 'GSAK' element, and a large RecA-fold-sized architecture. The methyltransferase distractors (B, C) require a Rossmann-like SAM-binding fold (VIGXG motif) and act on highly specific unusual spiro substrates—neither the fold nor the substrate context is evident. The methionine transporter (D) would require multiple transmembrane helices, which are absent from this soluble protein. Among the four choices, only A describes an ATP-dependent nucleic acid motor, consistent with the recognizable helicase motifs. The specific '3'-5' translocation directionality is a database-annotated fact, but since no 5'-3' helicase option is offered, identifying the protein as a helicase is sufficient to select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise 3'-5' translocation directionality of Lhr-Core is an experimentally determined property (PubMed:30224353) not trivially deducible from sequence motifs alone; however, this detail is not the distinguishing factor among the provided choices since no opposing-direction helicase option exists.",
    "reason": "A model with general knowledge of RecA-like helicase motifs (Walker B, Motif VI) and the structural requirements of methyltransferases and membrane transporters can meaningfully narrow the choices to A. The distractors belong to entirely different enzyme classes with incompatible structural signatures. The specific directionality embedded in A's text is an annotation fact, but it does not create ambiguity among the offered options."
  },
  "case_id": "catalytic_activity_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q88NV1 (LHRC_PSEPK, ATP-dependent helicase Lhr-Core from Pseudomonas putida KT2440) with exact sequence match confirmed in both current and historical entries. The catalytic activity annotation (EC 5.6.2.4) explicitly states 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction,' supported by experimental evidence (ECO:0000269, PubMed:30224353, Ejaz & Shuman 2018). This is direct experimental evidence, not computational inference."
  },
  "important_caveats": [
    "The specific '3'-5' directionality in option A is an experimentally determined annotation (ECO:0000269) and is not independently derivable from sequence motifs alone; however, this does not affect answer selection because no 5'-3' helicase alternative is provided.",
    "The Walker A motif in this sequence is degenerate and not a textbook GxxxxGKT; identification relies on a combination of Walker B (VVVDEW), Motif VI (GSAK), and overall RecA-fold architecture.",
    "The methyltransferase substrates in B and C are highly unusual spiro compounds; even if a model recognized a SAM-binding motif, these specific substrates would be implausible without the exact enzyme identity.",
    "Sequence match to Q88NV1 is confirmed (SHA-256 match, 816 AA, both current and historical entries)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are methyltransferases acting on exotic spiro compounds requiring a Rossmann fold; option D is a membrane transporter. None of these structural or functional features are present in the sequence. Only A (ATP-dependent helicase) is consistent with the observable RecA-like motifs and the protein's soluble, large-domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q88NV1 (LHRC_PSEPK, ATP-dependent helicase Lhr-Core from Pseudomonas putida KT2440) with exact sequence match confirmed in both current and historical entries. The catalytic activity annotation (EC 5.6.2.4) explicitly states 'Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction,' supported by experimental evidence (ECO:0000269, PubMed:30224353, Ejaz & Shuman 2018). This is direct experimental evidence, not computational inference.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 816-residue sequence contains motifs suggestive of a RecA-like helicase: a Walker B-like motif (VVVDEW in a hydrophobic context), a Motif VI-like 'GSAK' element, and a large RecA-fold-sized architecture. The methyltransferase distractors (B, C) require a Rossmann-like SAM-binding fold (VIGXG motif) and act on highly specific unusual spiro substrates—neither the fold nor the substrate context is evident. The methionine transporter (D) would require multiple transmembrane helices, which are absent from this soluble protein. Among the four choices, only A describes an ATP-dependent nucleic acid motor, consistent with the recognizable helicase motifs. The specific '3'-5' translocation directionality is a database-annotated fact, but since no 5'-3' helicase option is offered, identifying the protein as a helicase is sufficient to select A.",
    "missing_item_specific_fact": "The precise 3'-5' translocation directionality of Lhr-Core is an experimentally determined property (PubMed:30224353) not trivially deducible from sequence motifs alone; however, this detail is not the distinguishing factor among the provided choices since no opposing-direction helicase option exists.",
    "reason": "A model with general knowledge of RecA-like helicase motifs (Walker B, Motif VI) and the structural requirements of methyltransferases and membrane transporters can meaningfully narrow the choices to A. The distractors belong to entirely different enzyme classes with incompatible structural signatures. The specific directionality embedded in A's text is an annotation fact, but it does not create ambiguity among the offered options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are methyltransferases acting on exotic spiro compounds requiring a Rossmann fold; option D is a membrane transporter. None of these structural or functional features are present in the sequence. Only A (ATP-dependent helicase) is consistent with the observable RecA-like motifs and the protein's soluble, large-domain architecture."
  },
  "important_caveats": [
    "The specific '3'-5' directionality in option A is an experimentally determined annotation (ECO:0000269) and is not independently derivable from sequence motifs alone; however, this does not affect answer selection because no 5'-3' helicase alternative is provided.",
    "The Walker A motif in this sequence is degenerate and not a textbook GxxxxGKT; identification relies on a combination of Walker B (VVVDEW), Motif VI (GSAK), and overall RecA-fold architecture.",
    "The methyltransferase substrates in B and C are highly unusual spiro compounds; even if a model recognized a SAM-binding motif, these specific substrates would be implausible without the exact enzyme identity.",
    "Sequence match to Q88NV1 is confirmed (SHA-256 match, 816 AA, both current and historical entries)."
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

**Accession:** `Q88NV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 134. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:56.411071+00:00.  

```json
"Q88NV1"
```

Source SHA-256: `6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:56.411071+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"DNA and RNA:DNA 3'-5' helicase Lhr-Core"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30224353","source":"PubMed"}],"value":"5.6.2.-"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"30224353","source":"PubMed"}],"value":"5.6.2.4"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30224353","source":"PubMed"}],"value":"ATP-dependent helicase Lhr-Core"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30224353","source":"PubMed"}],"value":"Lhr-Core"}]}}
```

Source SHA-256: `6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:56.411071+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.6.2.4","evidences":[{"evidenceCode":"ECO:0000269","id":"30224353","source":"PubMed"}],"name":"Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction."}}
```

Source SHA-256: `6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q88NV1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:56.411071+00:00.  

```json
{"citation":{"authors":["Ejaz A.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"30224353"},{"database":"DOI","id":"10.1074/jbc.ra118.005296"}],"citationType":"journal article","firstPage":"17491","id":"30224353","journal":"J. Biol. Chem.","lastPage":"17504","publicationDate":"2018","title":"Characterization of Lhr-Core DNA helicase and manganese- dependent DNA nuclease components of a bacterial gene cluster encoding nucleic acid repair enzymes.","volume":"293"},"referenceComments":[{"type":"STRAIN","value":"ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440"}],"referenceNumber":2,"referencePositions":["FUNCTION AS A HELICASE","FUNCTION AS AN ATPASE","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `6d8894082892e958a6d474c6369d1253a40ea091c6c725a7684d7987f6ec7875`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 134 / 1.  
**Retrieved:** 2026-11-02T04:32:03.031844+00:00.  

```text
DE   RecName: Full=ATP-dependent helicase Lhr-Core {ECO:0000303|PubMed:30224353};
DE            Short=Lhr-Core {ECO:0000303|PubMed:30224353};
DE            EC=5.6.2.- {ECO:0000269|PubMed:30224353};
DE            EC=5.6.2.4 {ECO:0000269|PubMed:30224353};
DE   AltName: Full=DNA and RNA:DNA 3'-5' helicase Lhr-Core {ECO:0000305};
```

Source SHA-256: `abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134)  
**Locator:** `lines 32-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 134 / 1.  
**Retrieved:** 2026-11-02T04:32:03.031844+00:00.  

```text
RN   [2]
RP   FUNCTION AS A HELICASE, FUNCTION AS AN ATPASE, COFACTOR, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RC   STRAIN=ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440;
RX   PubMed=30224353; DOI=10.1074/jbc.ra118.005296;
RA   Ejaz A., Shuman S.;
RT   "Characterization of Lhr-Core DNA helicase and manganese- dependent DNA
RT   nuclease components of a bacterial gene cluster encoding nucleic acid
RT   repair enzymes.";
RL   J. Biol. Chem. 293:17491-17504(2018).
```

Source SHA-256: `abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q88NV1?format=txt&versions=134)  
**Locator:** `lines 49-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 134 / 1.  
**Retrieved:** 2026-11-02T04:32:03.031844+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Couples ATP hydrolysis with the unwinding of duplex DNA by
CC         translocating in the 3'-5' direction.; EC=5.6.2.4;
CC         Evidence={ECO:0000269|PubMed:30224353};
```

Source SHA-256: `abb725c0c25289242145250b8c248a3dabbf40cb4984bd0802e1533569e5a66f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
