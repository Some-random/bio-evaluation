# cofactor_0170

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MISKSIILRFSELSMRKKATLVGLPLLAVAAISSSLNSPTRQQRIELSLPESPLVQFSSAEHTVEVVKVGHPDYEYEIKPGDNLSTIFNQLGFAYTELMKVMETDLNYLALDTLRPGNVLRFWKGSDNTLAKMELEFSLVDRAVYTRLNDGSYEFEERKIPGTWKVEPLIGEVDGSFSLSANRAGLGAADVDQIVTLLKDKINFGRDLRRGDRFEVVLSRQLVGEKLTGNSEIQAIKIFNRGKEITAYLHQDGQYYDKNGDSLQRAFQRYPVDSKWRISSNFDPRRLHPVTKRVAPHNGTDFAMPIGTPVYTSGDGVVVMTRNHPYAGNYVVIQHGNTYMTRYLHLSKILVKKGQKVSRGQRIGLSGNTGRVTGPHLHYELIVRGRPVNAMKANIPMASSVPKKEMAQFIAKRKELDQMLARQESMLAAQ

[Multiple Choices]
A. Zn(2+)
B. pantetheine 4'-phosphate
C. FAD
D. Mo-bis(molybdopterin guanine dinucleotide)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact sequence matches the annotated ShyA protein. UniProt records Zn(2+) as its cofactor, one ion per subunit, with experimental evidence attribution; the cited structural study reports a crystal structure in complex with Zn(2+).

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has several histidine- and acidic-residue-containing regions, which could be consistent with metal binding, but the supplied input does not establish the protein's function or identify a specific metal-binding active site well enough to determine the required cofactor.


**Missing item-specific fact**

> That this sequence is ShyA, a zinc-dependent peptidoglycan endopeptidase; the reported one-Zn-per-subunit cofactor assignment is an item-specific annotation supported by cited experimental evidence.


**Reason**

> Selecting Zn depends on protein-specific functional or cofactor information absent from the question. Generic sequence heuristics do not distinguish a required Zn cofactor from the listed alternatives with adequate support.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation explicitly assigns Zn(2+); no supplied evidence supports another listed cofactor.


### Important caveats

- The cofactor annotation and cited structural evidence are reviewer-only and were not supplied to the evaluated model.
- The current and checked historical UniProt records match the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has several histidine- and acidic-residue-containing regions, which could be consistent with metal binding, but the supplied input does not establish the protein's function or identify a specific metal-binding active site well enough to determine the required cofactor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence is ShyA, a zinc-dependent peptidoglycan endopeptidase; the reported one-Zn-per-subunit cofactor assignment is an item-specific annotation supported by cited experimental evidence.",
    "reason": "Selecting Zn depends on protein-specific functional or cofactor information absent from the question. Generic sequence heuristics do not distinguish a required Zn cofactor from the listed alternatives with adequate support."
  },
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated ShyA protein. UniProt records Zn(2+) as its cofactor, one ion per subunit, with experimental evidence attribution; the cited structural study reports a crystal structure in complex with Zn(2+)."
  },
  "important_caveats": [
    "The cofactor annotation and cited structural evidence are reviewer-only and were not supplied to the evaluated model.",
    "The current and checked historical UniProt records match the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation explicitly assigns Zn(2+); no supplied evidence supports another listed cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated ShyA protein. UniProt records Zn(2+) as its cofactor, one ion per subunit, with experimental evidence attribution; the cited structural study reports a crystal structure in complex with Zn(2+).",
    "evidence_ids": ["C5", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has several histidine- and acidic-residue-containing regions, which could be consistent with metal binding, but the supplied input does not establish the protein's function or identify a specific metal-binding active site well enough to determine the required cofactor.",
    "missing_item_specific_fact": "That this sequence is ShyA, a zinc-dependent peptidoglycan endopeptidase; the reported one-Zn-per-subunit cofactor assignment is an item-specific annotation supported by cited experimental evidence.",
    "reason": "Selecting Zn depends on protein-specific functional or cofactor information absent from the question. Generic sequence heuristics do not distinguish a required Zn cofactor from the listed alternatives with adequate support."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation explicitly assigns Zn(2+); no supplied evidence supports another listed cofactor."
  },
  "important_caveats": [
    "The cofactor annotation and cited structural evidence are reviewer-only and were not supplied to the evaluated model.",
    "The current and checked historical UniProt records match the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9KN86 (ShyA, Vibrio cholerae) explicitly annotates Zn(2+) as the cofactor (ECO:0000269|PubMed:32393643, 'Binds 1 zinc ion per subunit'). The alternative name 'Zn-metalloprotease' and EC 3.4.24.- (metalloprotease class) confirm this. X-ray crystallography at 2.08 Å (PDB 6U2A, 6UE4) shows the protein in complex with Zn(2+). The sequence matches the benchmark input exactly (SHA-256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple H-x-H motifs (e.g., 'HPYAGNYVVIQHGNTY', 'HLHYELIVRGRPVNAMKANIPMASSVPKKEMAQFIAKRKELDQMLARQESMLAAQ') consistent with zinc-coordinating metalloprotease active sites. The protein has a signal peptide indicating a periplasmic/extracellular peptidase. Critically, the three distractors are organic cofactors tied to entirely different enzyme classes: FAD requires Rossmann-fold motifs (GxGxxG, absent here), Mo-bis(molybdopterin guanine dinucleotide) requires molybdenum enzyme motifs (absent), and pantetheine 4'-phosphate is for acyl-carrier/acyltransferase systems (no such motifs present). By elimination of organic-cofactor enzyme classes and positive identification of His-rich metal-binding patterns, Zn(2+) is the only biochemically consistent choice for a peptidoglycan-degrading endopeptidase.


**Missing item-specific fact**

> Precise recognition of the M23 peptidase family fold would strengthen the argument, but is not strictly required given the strong elimination of all three organic-cofactor options and the visible His-rich coordination motifs.


**Reason**

> A model with general biological knowledge can (a) note the absence of any flavin, molybdopterin, or acyl-carrier binding motifs, eliminating B, C, and D; (b) observe HxxH-type patterns suggestive of a zinc metalloprotease active site; and (c) infer that a peptidoglycan-degrading endopeptidase (EC 3.4.24.-) uses Zn(2+). This constitutes a concrete biological argument rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three non-metal distractors are associated with mechanistically distinct enzyme classes (oxidoreductases, molybdoenzymes, acyltransferases) that are clearly inconsistent with the sequence architecture and His-rich motifs. Only Zn(2+) is compatible with a metalloprotease.


### Important caveats

- The M23 peptidase family assignment from raw sequence is non-trivial; a model relying solely on motif scanning might struggle to positively identify the family, though elimination of the three organic-cofactor choices is straightforward.
- The UniProt COFACTOR annotation carries evidence code ECO:0000269 (experimental, from PubMed:32393643 / PDB structures), so the key is experimentally grounded, not merely computational.
- The entry was first publicly released in April 2025; depending on the benchmark construction date, the annotation may or may not have been available to the author at question-creation time, though the sequence itself has been in databases since 2000.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple H-x-H motifs (e.g., 'HPYAGNYVVIQHGNTY', 'HLHYELIVRGRPVNAMKANIPMASSVPKKEMAQFIAKRKELDQMLARQESMLAAQ') consistent with zinc-coordinating metalloprotease active sites. The protein has a signal peptide indicating a periplasmic/extracellular peptidase. Critically, the three distractors are organic cofactors tied to entirely different enzyme classes: FAD requires Rossmann-fold motifs (GxGxxG, absent here), Mo-bis(molybdopterin guanine dinucleotide) requires molybdenum enzyme motifs (absent), and pantetheine 4'-phosphate is for acyl-carrier/acyltransferase systems (no such motifs present). By elimination of organic-cofactor enzyme classes and positive identification of His-rich metal-binding patterns, Zn(2+) is the only biochemically consistent choice for a peptidoglycan-degrading endopeptidase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of the M23 peptidase family fold would strengthen the argument, but is not strictly required given the strong elimination of all three organic-cofactor options and the visible His-rich coordination motifs.",
    "reason": "A model with general biological knowledge can (a) note the absence of any flavin, molybdopterin, or acyl-carrier binding motifs, eliminating B, C, and D; (b) observe HxxH-type patterns suggestive of a zinc metalloprotease active site; and (c) infer that a peptidoglycan-degrading endopeptidase (EC 3.4.24.-) uses Zn(2+). This constitutes a concrete biological argument rather than pure lookup."
  },
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9KN86 (ShyA, Vibrio cholerae) explicitly annotates Zn(2+) as the cofactor (ECO:0000269|PubMed:32393643, 'Binds 1 zinc ion per subunit'). The alternative name 'Zn-metalloprotease' and EC 3.4.24.- (metalloprotease class) confirm this. X-ray crystallography at 2.08 Å (PDB 6U2A, 6UE4) shows the protein in complex with Zn(2+). The sequence matches the benchmark input exactly (SHA-256 identical)."
  },
  "important_caveats": [
    "The M23 peptidase family assignment from raw sequence is non-trivial; a model relying solely on motif scanning might struggle to positively identify the family, though elimination of the three organic-cofactor choices is straightforward.",
    "The UniProt COFACTOR annotation carries evidence code ECO:0000269 (experimental, from PubMed:32393643 / PDB structures), so the key is experimentally grounded, not merely computational.",
    "The entry was first publicly released in April 2025; depending on the benchmark construction date, the annotation may or may not have been available to the author at question-creation time, though the sequence itself has been in databases since 2000."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three non-metal distractors are associated with mechanistically distinct enzyme classes (oxidoreductases, molybdoenzymes, acyltransferases) that are clearly inconsistent with the sequence architecture and His-rich motifs. Only Zn(2+) is compatible with a metalloprotease."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9KN86 (ShyA, Vibrio cholerae) explicitly annotates Zn(2+) as the cofactor (ECO:0000269|PubMed:32393643, 'Binds 1 zinc ion per subunit'). The alternative name 'Zn-metalloprotease' and EC 3.4.24.- (metalloprotease class) confirm this. X-ray crystallography at 2.08 Å (PDB 6U2A, 6UE4) shows the protein in complex with Zn(2+). The sequence matches the benchmark input exactly (SHA-256 identical).",
    "evidence_ids": ["C4", "C5", "C8", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple H-x-H motifs (e.g., 'HPYAGNYVVIQHGNTY', 'HLHYELIVRGRPVNAMKANIPMASSVPKKEMAQFIAKRKELDQMLARQESMLAAQ') consistent with zinc-coordinating metalloprotease active sites. The protein has a signal peptide indicating a periplasmic/extracellular peptidase. Critically, the three distractors are organic cofactors tied to entirely different enzyme classes: FAD requires Rossmann-fold motifs (GxGxxG, absent here), Mo-bis(molybdopterin guanine dinucleotide) requires molybdenum enzyme motifs (absent), and pantetheine 4'-phosphate is for acyl-carrier/acyltransferase systems (no such motifs present). By elimination of organic-cofactor enzyme classes and positive identification of His-rich metal-binding patterns, Zn(2+) is the only biochemically consistent choice for a peptidoglycan-degrading endopeptidase.",
    "missing_item_specific_fact": "Precise recognition of the M23 peptidase family fold would strengthen the argument, but is not strictly required given the strong elimination of all three organic-cofactor options and the visible His-rich coordination motifs.",
    "reason": "A model with general biological knowledge can (a) note the absence of any flavin, molybdopterin, or acyl-carrier binding motifs, eliminating B, C, and D; (b) observe HxxH-type patterns suggestive of a zinc metalloprotease active site; and (c) infer that a peptidoglycan-degrading endopeptidase (EC 3.4.24.-) uses Zn(2+). This constitutes a concrete biological argument rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three non-metal distractors are associated with mechanistically distinct enzyme classes (oxidoreductases, molybdoenzymes, acyltransferases) that are clearly inconsistent with the sequence architecture and His-rich motifs. Only Zn(2+) is compatible with a metalloprotease."
  },
  "important_caveats": [
    "The M23 peptidase family assignment from raw sequence is non-trivial; a model relying solely on motif scanning might struggle to positively identify the family, though elimination of the three organic-cofactor choices is straightforward.",
    "The UniProt COFACTOR annotation carries evidence code ECO:0000269 (experimental, from PubMed:32393643 / PDB structures), so the key is experimentally grounded, not merely computational.",
    "The entry was first publicly released in April 2025; depending on the benchmark construction date, the annotation may or may not have been available to the author at question-creation time, though the sequence itself has been in databases since 2000."
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

**Accession:** `Q9KN86` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 110. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:59.163450+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32393643","source":"PubMed"}],"value":"Autolysin ShyA"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32393643","source":"PubMed"}],"value":"Major peptidoglycan endopeptidase ShyA"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32393643","source":"PubMed"}],"value":"Major PG EP ShyA"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23834664","source":"PubMed"}],"value":"Sidewall hydrolase A"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23834664","source":"PubMed"}],"value":"Zn-metalloprotease"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23834664","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30782657","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32393643","source":"PubMed"}],"value":"3.4.24.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23834664","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"30782657","source":"PubMed"}],"value":"Peptidoglycan DD-endopeptidase ShyA"}}}
```

Source SHA-256: `44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:59.163450+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000269","id":"32393643","source":"PubMed"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32393643","source":"PubMed"}],"value":"Binds 1 zinc ion per subunit."}]}}
```

Source SHA-256: `44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:59.163450+00:00.  

```json
{"citation":{"authors":["Shin J.H.","Sulpizio A.G.","Kelley A.","Alvarez L.","Murphy S.G.","Fan L.","Cava F.","Mao Y.","Saper M.A.","Dorr T."],"citationCrossReferences":[{"database":"PubMed","id":"32393643"},{"database":"DOI","id":"10.1073/pnas.2001661117"}],"citationType":"journal article","firstPage":"11692","id":"32393643","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"11702","publicationDate":"2020","title":"Structural basis of peptidoglycan endopeptidase regulation.","volume":"117"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6U2A","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6UE4","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32393643","source":"PubMed"}],"type":"STRAIN","value":"ATCC 39315 / El Tor Inaba N16961"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.08 ANGSTROMS) OF 36-430 IN COMPLEX WITH ZN(2+)","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","PATHWAY","SUBCELLULAR LOCATION","DOMAIN","DISRUPTION PHENOTYPE","MUTAGENESIS OF 1-MET--ARG-265; 1-MET--ILE-160; 1-MET--VAL-66; GLU-103; LEU-109; ASP-112; ARG-286; HIS-297; ASP-301; LEU-344; HIS-345; HIS-376; HIS-378 AND 427-LEU--GLN-430"]}
```

Source SHA-256: `44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)  
**Locator:** `lines 56-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 1.  
**Retrieved:** 2026-11-02T04:33:01.774065+00:00.  

```text
RN   [4] {ECO:0007744|PDB:6U2A, ECO:0007744|PDB:6UE4}
RP   X-RAY CRYSTALLOGRAPHY (2.08 ANGSTROMS) OF 36-430 IN COMPLEX WITH ZN(2+),
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, PATHWAY,
RP   SUBCELLULAR LOCATION, DOMAIN, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF
RP   1-MET--ARG-265; 1-MET--ILE-160; 1-MET--VAL-66; GLU-103; LEU-109; ASP-112;
RP   ARG-286; HIS-297; ASP-301; LEU-344; HIS-345; HIS-376; HIS-378 AND
RP   427-LEU--GLN-430.
RC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:32393643};
RX   PubMed=32393643; DOI=10.1073/pnas.2001661117;
RA   Shin J.H., Sulpizio A.G., Kelley A., Alvarez L., Murphy S.G., Fan L.,
RA   Cava F., Mao Y., Saper M.A., Dorr T.;
RT   "Structural basis of peptidoglycan endopeptidase regulation.";
RL   Proc. Natl. Acad. Sci. U.S.A. 117:11692-11702(2020).
```

Source SHA-256: `cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)  
**Locator:** `lines 87-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 110 / 1.  
**Retrieved:** 2026-11-02T04:33:01.774065+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000269|PubMed:32393643};
CC       Note=Binds 1 zinc ion per subunit. {ECO:0000269|PubMed:32393643};
```

Source SHA-256: `cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
