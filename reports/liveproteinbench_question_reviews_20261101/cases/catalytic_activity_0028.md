# catalytic_activity_0028

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — N(omega)-(ADP-D-ribosyl)-L-arginyl-&#91;protein&#93; + H2O = ADP-D-ribose + L-arginyl-&#91;protein&#93;

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSTFGAEVDQVWPAVTGDSPHLTNFGRKLLKDCRQVQKPIGGYENLGNVIKLSAEFPLEFGVNSVKVYRQSPSRLARINEEVASAYPLIHERTLGLYLQYLEHKCRWGNAVEKPIYRNLSLCGFVQRLLVKRCASFFARNDKYLLVSGESGASGFEAVGTREEKAPLVLANVLSYDDIKLSALLSVSSRTEFVNEGERTNCGHVDLNTKTLERHGVIVGMIGARLSRRNLMEFQDIVIARQQNTRERGYGMALDEPATTRDEDYRRLWREFYATRDLIHGQAVIDNQRFGPSKNKMDVFDNLVMKRRYAISFDMLLLEAEARAKRVKKLAYIHVVGFGLGVWKAAEQQERIFMETFEQRMRTLGNRLNNVGLVHFSWFSITHCGGLSNGSLIEIPGHPKDGIRVLISKRNPARKLSDPEHAGMLLVVSYAWDGNALPGNEFWMKMLQSTGDSSTACSTLVAELHNPYINTKFCNGGNLHIASPEHGVLHIAEYAKRVIRSESDAL

[Multiple Choices]
A. N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]
B. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
C. a quinone + NADPH + H(+) = a quinol + NADP(+)
D. a 5'-end (5'-triphosphoguanosine)-adenylyl-adenylyl-cytidylyl-adenosine in mRNA + S-adenosyl-L-methionine = a 5'-end (5'-triphosphoguanosine)-(2'-O-methyladenylyl)-adenylyl-cytidylyl-adenosine in mRNA + S-adenosyl-L-homocysteine + H(+)
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

> The sequence exactly matches the UniProt entry for Drosophila ADP-ribosylarginine hydrolase CG2909, whose annotated catalytic reaction is choice A. The reaction annotation cites experimental evidence (ECO:0000269); the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe different enzyme activities, but the input provides no biological context or explicit substrate evidence that establishes this protein's particular activity.


**Missing item-specific fact**

> The protein-specific identification or experimental annotation that this sequence encodes an ADP-ribosylarginine hydrolase.


**Reason**

> Choosing A depends on knowing the identity or functional annotation of this particular sequence. The reviewer-only database match supports the key but was not supplied to the evaluated model; exact-sequence recognition or a predictor's output would not itself make the question reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's cited catalytic-activity annotation specifies choice A; no competing reaction is supported by the supplied reviewer evidence.


### Important caveats

- The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.
- The cited experimental evidence is represented through UniProt annotation; the primary paper was not independently validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe different enzyme activities, but the input provides no biological context or explicit substrate evidence that establishes this protein's particular activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification or experimental annotation that this sequence encodes an ADP-ribosylarginine hydrolase.",
    "reason": "Choosing A depends on knowing the identity or functional annotation of this particular sequence. The reviewer-only database match supports the key but was not supplied to the evaluated model; exact-sequence recognition or a predictor's output would not itself make the question reasoning-supported."
  },
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for Drosophila ADP-ribosylarginine hydrolase CG2909, whose annotated catalytic reaction is choice A. The reaction annotation cites experimental evidence (ECO:0000269); the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.",
    "The cited experimental evidence is represented through UniProt annotation; the primary paper was not independently validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's cited catalytic-activity annotation specifies choice A; no competing reaction is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt entry for Drosophila ADP-ribosylarginine hydrolase CG2909, whose annotated catalytic reaction is choice A. The reaction annotation cites experimental evidence (ECO:0000269); the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe different enzyme activities, but the input provides no biological context or explicit substrate evidence that establishes this protein's particular activity.",
    "missing_item_specific_fact": "The protein-specific identification or experimental annotation that this sequence encodes an ADP-ribosylarginine hydrolase.",
    "reason": "Choosing A depends on knowing the identity or functional annotation of this particular sequence. The reviewer-only database match supports the key but was not supplied to the evaluated model; exact-sequence recognition or a predictor's output would not itself make the question reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's cited catalytic-activity annotation specifies choice A; no competing reaction is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The sequence match is exact in both current and historical UniProt records, but the author's source snapshot is unknown.",
    "The cited experimental evidence is represented through UniProt annotation; the primary paper was not independently validated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9W2W5 (ADPR1_DROME) is annotated as 'ADP-ribosylarginine hydrolase CG2909' with EC 3.2.2.19. The catalytic activity is explicitly stated as 'N(omega)-(ADP-D-ribosyl)-L-arginyl-&#91;protein&#93; + H2O = ADP-D-ribose + L-arginyl-&#91;protein&#93;' (Rhea:RHEA:14885), matching Choice A verbatim. The annotation carries evidence code ECO:0000269 (direct assay) from PubMed:38503748 and is corroborated by X-ray crystallography (PDB 8DMT, 2.28 Å). Sequence match is exact (505 aa, SHA256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No obvious sequence motif in the 505-aa sequence uniquely identifies ADP-ribosylarginine hydrolase activity over the three distractors. While the sequence contains nucleotide-binding-like elements (e.g., 'GNSVKVY', 'SGESGASGF' P-loop-like region), these are shared across many nucleotide-binding enzymes and do not distinguish a macrodomain hydrolase from an ACP synthase (B), a quinone reductase (C), or a cap methyltransferase (D). The macrodomain fold responsible for arginine-specific ADP-ribosyl hydrolysis is a structural feature not reliably identifiable from primary sequence by general biological reasoning.


**Missing item-specific fact**

> The specific identification of this Drosophila CG2909 protein as a macrodomain-containing ADP-ribosylarginine hydrolase (EC 3.2.2.19) requires either database lookup of the sequence or specialized knowledge of macrodomain structural signatures, neither of which is derivable from general enzymology reasoning about the provided sequence.


**Reason**

> The four choices represent entirely different enzyme classes (glycosyl hydrolase, transferase, oxidoreductase, methyltransferase). Distinguishing them from a raw 505-aa sequence without structural context or recognizable class-specific motifs demands item-specific annotation knowledge rather than general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt annotation with direct experimental evidence (ECO:0000269) and crystallographic confirmation uniquely identifies Choice A. The other three choices describe mechanistically unrelated reactions that are not supported for this protein.


### Important caveats

- The UniProt entry was first publicly released in 2025-02-05; the catalytic activity annotation (PubMed:38503748, 2024) may postdate the original benchmark construction, though the sequence itself has been in databases since 2000.
- The accession Q9W2W5 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.
- The annotation evidence is experimental (direct assay + crystallography), not merely computational inference, strengthening the key's reliability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No obvious sequence motif in the 505-aa sequence uniquely identifies ADP-ribosylarginine hydrolase activity over the three distractors. While the sequence contains nucleotide-binding-like elements (e.g., 'GNSVKVY', 'SGESGASGF' P-loop-like region), these are shared across many nucleotide-binding enzymes and do not distinguish a macrodomain hydrolase from an ACP synthase (B), a quinone reductase (C), or a cap methyltransferase (D). The macrodomain fold responsible for arginine-specific ADP-ribosyl hydrolysis is a structural feature not reliably identifiable from primary sequence by general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this Drosophila CG2909 protein as a macrodomain-containing ADP-ribosylarginine hydrolase (EC 3.2.2.19) requires either database lookup of the sequence or specialized knowledge of macrodomain structural signatures, neither of which is derivable from general enzymology reasoning about the provided sequence.",
    "reason": "The four choices represent entirely different enzyme classes (glycosyl hydrolase, transferase, oxidoreductase, methyltransferase). Distinguishing them from a raw 505-aa sequence without structural context or recognizable class-specific motifs demands item-specific annotation knowledge rather than general biological reasoning."
  },
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9W2W5 (ADPR1_DROME) is annotated as 'ADP-ribosylarginine hydrolase CG2909' with EC 3.2.2.19. The catalytic activity is explicitly stated as 'N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]' (Rhea:RHEA:14885), matching Choice A verbatim. The annotation carries evidence code ECO:0000269 (direct assay) from PubMed:38503748 and is corroborated by X-ray crystallography (PDB 8DMT, 2.28 Å). Sequence match is exact (505 aa, SHA256 identical)."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released in 2025-02-05; the catalytic activity annotation (PubMed:38503748, 2024) may postdate the original benchmark construction, though the sequence itself has been in databases since 2000.",
    "The accession Q9W2W5 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.",
    "The annotation evidence is experimental (direct assay + crystallography), not merely computational inference, strengthening the key's reliability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt annotation with direct experimental evidence (ECO:0000269) and crystallographic confirmation uniquely identifies Choice A. The other three choices describe mechanistically unrelated reactions that are not supported for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9W2W5 (ADPR1_DROME) is annotated as 'ADP-ribosylarginine hydrolase CG2909' with EC 3.2.2.19. The catalytic activity is explicitly stated as 'N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]' (Rhea:RHEA:14885), matching Choice A verbatim. The annotation carries evidence code ECO:0000269 (direct assay) from PubMed:38503748 and is corroborated by X-ray crystallography (PDB 8DMT, 2.28 Å). Sequence match is exact (505 aa, SHA256 identical).",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No obvious sequence motif in the 505-aa sequence uniquely identifies ADP-ribosylarginine hydrolase activity over the three distractors. While the sequence contains nucleotide-binding-like elements (e.g., 'GNSVKVY', 'SGESGASGF' P-loop-like region), these are shared across many nucleotide-binding enzymes and do not distinguish a macrodomain hydrolase from an ACP synthase (B), a quinone reductase (C), or a cap methyltransferase (D). The macrodomain fold responsible for arginine-specific ADP-ribosyl hydrolysis is a structural feature not reliably identifiable from primary sequence by general biological reasoning.",
    "missing_item_specific_fact": "The specific identification of this Drosophila CG2909 protein as a macrodomain-containing ADP-ribosylarginine hydrolase (EC 3.2.2.19) requires either database lookup of the sequence or specialized knowledge of macrodomain structural signatures, neither of which is derivable from general enzymology reasoning about the provided sequence.",
    "reason": "The four choices represent entirely different enzyme classes (glycosyl hydrolase, transferase, oxidoreductase, methyltransferase). Distinguishing them from a raw 505-aa sequence without structural context or recognizable class-specific motifs demands item-specific annotation knowledge rather than general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt annotation with direct experimental evidence (ECO:0000269) and crystallographic confirmation uniquely identifies Choice A. The other three choices describe mechanistically unrelated reactions that are not supported for this protein."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released in 2025-02-05; the catalytic activity annotation (PubMed:38503748, 2024) may postdate the original benchmark construction, though the sequence itself has been in databases since 2000.",
    "The accession Q9W2W5 was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model.",
    "The annotation evidence is experimental (direct assay + crystallography), not merely computational inference, strengthening the key's reliability."
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

**Accession:** `Q9W2W5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 173. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
"Q9W2W5"
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"value":"3.2.2.19"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"ADP-ribosylarginine hydrolase CG2909"}}}
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.2.19","evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"name":"N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14885"},{"database":"Rhea","id":"RHEA-COMP:10532"},{"database":"Rhea","id":"RHEA-COMP:15087"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29965"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142554"}]}}
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W2W5.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:49.227169+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Fu J.","Rack J.G.M.","Li C.","Voorneveld J.","Filippov D.V.","Ahel I.","Luo Z.Q.","Das C."],"citationCrossReferences":[{"database":"PubMed","id":"38503748"},{"database":"DOI","id":"10.1038/s41467-024-46649-2"}],"citationType":"journal article","firstPage":"2452","id":"38503748","journal":"Nat. Commun.","lastPage":"2452","publicationDate":"2024","title":"Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a conserved arginine-specific macrodomain.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8DMT","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.28 ANGSTROMS) OF 12-498","FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `8c4b1ff81ea684e2da8c73dc92c892e3febdbf00a6956c5246fef6a8101ec96b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 173 / 1.  
**Retrieved:** 2026-11-02T04:33:51.554411+00:00.  

```text
DE   RecName: Full=ADP-ribosylarginine hydrolase CG2909 {ECO:0000305};
DE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};
```

Source SHA-256: `d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)  
**Locator:** `lines 77-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 173 / 1.  
**Retrieved:** 2026-11-02T04:33:51.554411+00:00.  

```text
RN   [4] {ECO:0007744|PDB:8DMT}
RP   X-RAY CRYSTALLOGRAPHY (2.28 ANGSTROMS) OF 12-498, FUNCTION, AND CATALYTIC
RP   ACTIVITY.
RX   PubMed=38503748; DOI=10.1038/s41467-024-46649-2;
RA   Zhang Z., Fu J., Rack J.G.M., Li C., Voorneveld J., Filippov D.V., Ahel I.,
RA   Luo Z.Q., Das C.;
RT   "Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a
RT   conserved arginine-specific macrodomain.";
RL   Nat. Commun. 15:2452-2452(2024).
```

Source SHA-256: `d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W2W5?format=txt&versions=173)  
**Locator:** `lines 89-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 173 / 1.  
**Retrieved:** 2026-11-02T04:33:51.554411+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-
CC         ribose + L-arginyl-[protein]; Xref=Rhea:RHEA:14885, Rhea:RHEA-
CC         COMP:10532, Rhea:RHEA-COMP:15087, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:29965, ChEBI:CHEBI:57967, ChEBI:CHEBI:142554;
CC         EC=3.2.2.19; Evidence={ECO:0000269|PubMed:38503748};
```

Source SHA-256: `d3e88c24a09fe094e0e6b61003b0b7cb6a21443d379625c0284868d597f8c494`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
