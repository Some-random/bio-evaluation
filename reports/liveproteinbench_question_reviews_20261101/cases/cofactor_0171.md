# cofactor_0171

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLSLFNRLPWLHRVLITAFSAIIVFAIFFLPNSEDLRKPDAQREVGRHYPVTLDNQLVSTPEEEVIAPPSVMLRWETYQVANGESAALLFQRAGLSSRVLYELTSSNSDINNQLSKLMPKDELKFGFDKDNQLVQLKRTISPYETFVVTRSDSGFTSEFDKKEVTFQLNYAEAKITSNFWNAGVTAGLSANQIIELANMFGWDIDFALDIREGDQFKLLYQEKIVEGSVIGRGNIIAATFINQGSTFTAILDDNTGNYYDQNGRAMKKAFLRSPLDFRRVSSNFNPRRLHPVTGQIKAHRGTDYVAPVGTPIWAAGDGVVEKSSYNQFNGNYVYIRHSNTYITKYLHLQRRLVKTGERVKQGQTIGTLGGTGRVTGPHLHYEFLVNGIHKNPRTVELPQAQSLTGKAKETFIANAKQRMEKLERYSQLLYANQ

[Multiple Choices]
A. Ca(2+)
B. Zn(2+)
C. heme b
D. pantetheine 4'-phosphate
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

> The exact-matching UniProt record annotates Zn(2+) as the cofactor, with one zinc ion per subunit. This annotation is transferred by similarity from Q9KN86, so it supports the key but is not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an HxH motif (in the segment containing GPHLH) and nearby histidines, a plausible metal-binding signature for a metalloprotease; among these choices, Zn(2+) is the biologically defensible cofactor inference.


**Missing item-specific fact**

> Direct confirmation that this particular protein binds zinc is not supplied; the database evidence is a similarity-based annotation.


**Reason**

> A recognizable histidine-rich metal-binding motif provides a concrete biological clue favoring zinc over heme, pantetheine phosphate, or calcium, although it does not establish the cofactor experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence motif supports zinc as the distinctive choice among the listed options; no alternative is comparably supported by the supplied sequence.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but its cofactor evidence is transferred from a homolog rather than demonstrated directly for this protein.
- The sequence-based motif interpretation is predictive, not proof of zinc binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an HxH motif (in the segment containing GPHLH) and nearby histidines, a plausible metal-binding signature for a metalloprotease; among these choices, Zn(2+) is the biologically defensible cofactor inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Direct confirmation that this particular protein binds zinc is not supplied; the database evidence is a similarity-based annotation.",
    "reason": "A recognizable histidine-rich metal-binding motif provides a concrete biological clue favoring zinc over heme, pantetheine phosphate, or calcium, although it does not establish the cofactor experimentally."
  },
  "case_id": "cofactor_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates Zn(2+) as the cofactor, with one zinc ion per subunit. This annotation is transferred by similarity from Q9KN86, so it supports the key but is not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its cofactor evidence is transferred from a homolog rather than demonstrated directly for this protein.",
    "The sequence-based motif interpretation is predictive, not proof of zinc binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motif supports zinc as the distinctive choice among the listed options; no alternative is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates Zn(2+) as the cofactor, with one zinc ion per subunit. This annotation is transferred by similarity from Q9KN86, so it supports the key but is not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an HxH motif (in the segment containing GPHLH) and nearby histidines, a plausible metal-binding signature for a metalloprotease; among these choices, Zn(2+) is the biologically defensible cofactor inference.",
    "missing_item_specific_fact": "Direct confirmation that this particular protein binds zinc is not supplied; the database evidence is a similarity-based annotation.",
    "reason": "A recognizable histidine-rich metal-binding motif provides a concrete biological clue favoring zinc over heme, pantetheine phosphate, or calcium, although it does not establish the cofactor experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motif supports zinc as the distinctive choice among the listed options; no alternative is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but its cofactor evidence is transferred from a homolog rather than demonstrated directly for this protein.",
    "The sequence-based motif interpretation is predictive, not proof of zinc binding."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9KU93 (ShyC, Peptidoglycan DD-endopeptidase, EC 3.4.24.-) annotates Zn(2+) as the cofactor (evidence C5/H5). The annotation uses ECO:0000250 (inferred by similarity to Q9KN86), making it a transferred annotation rather than a direct experimental measurement on this protein. However, the EC class 3.4.24 is specifically for metalloendopeptidases, and the 2019 reference (PubMed:30782657, H4/C7) explicitly links this protein to the Zur-dependent zinc starvation response, providing strong indirect experimental context for zinc dependence. The answer is well-supported.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C4](#evidence-c4), [H2](#evidence-h2), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several sequence-level features allow elimination of three options and favor Zn(2+): (1) The N-terminal hydrophobic stretch (~20 residues) is a classic signal peptide, indicating a secreted/periplasmic protein, which eliminates pantetheine 4'-phosphate (an intracellular acyl-carrier cofactor for fatty-acid synthases). (2) The sequence lacks Cys-X-X-Cys motifs or closely spaced bis-His axial ligands characteristic of heme b coordination, making heme b unlikely. (3) The protein is small (~433 aa), secreted, and contains multiple histidine residues in spatially proximate clusters (e.g., HYPVTLDN near the N-terminus; HSNTYITKYLHL and HPHLHY regions in the C-terminal half), consistent with a zinc-coordinating metalloprotease active site. (4) Peptidoglycan DD-endopeptidases (EC 3.4.24) are overwhelmingly zinc-dependent metalloenzymes; the absence of EF-hand or other calcium-binding loop motifs further disfavors Ca(2+). Together these general biological arguments form a defensible reasoning chain favoring Zn(2+).


**Missing item-specific fact**

> Precise identification of the M23 peptidoglycan endopeptidase family fold and its canonical HxxH zinc-binding motif would strengthen confidence, but is not strictly required given the elimination logic above.


**Reason**

> The combination of signal peptide (eliminates pantetheine), absence of heme-binding motifs (eliminates heme b), histidine-rich metal-coordination pattern, small secreted architecture, and general knowledge that peptidoglycan hydrolases are zinc metalloenzymes provides a concrete, general-biology reasoning path to Zn(2+) without requiring memorization of this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While Zn(2+) vs. Ca(2+) is the closest pair, the histidine coordination pattern and metalloendopeptidase context clearly favor Zn(2+). Heme b and pantetheine 4'-phosphate are readily excluded by sequence features. No other option is genuinely defensible.


### Important caveats

- The UniProt Zn(2+) cofactor annotation carries evidence code ECO:0000250 (similarity to Q9KN86), i.e., it is a transferred computational annotation rather than a direct experimental zinc-binding measurement on ShyC itself.
- The 2019 paper (PubMed:30782657) on zinc starvation regulation provides strong indirect experimental support for zinc dependence but was not independently retrieved to confirm the exact nature of the evidence.
- The reviewer-only evidence was not available to the evaluated model; the reasoning_supported judgment is based solely on what a knowledgeable model could infer from the sequence and general biology.
- The M23-family HxxH zinc-binding motif is not trivially recognizable in this sequence without prior family knowledge, making the question moderately difficult but still answerable through elimination and general metalloenzyme reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several sequence-level features allow elimination of three options and favor Zn(2+): (1) The N-terminal hydrophobic stretch (~20 residues) is a classic signal peptide, indicating a secreted/periplasmic protein, which eliminates pantetheine 4'-phosphate (an intracellular acyl-carrier cofactor for fatty-acid synthases). (2) The sequence lacks Cys-X-X-Cys motifs or closely spaced bis-His axial ligands characteristic of heme b coordination, making heme b unlikely. (3) The protein is small (~433 aa), secreted, and contains multiple histidine residues in spatially proximate clusters (e.g., HYPVTLDN near the N-terminus; HSNTYITKYLHL and HPHLHY regions in the C-terminal half), consistent with a zinc-coordinating metalloprotease active site. (4) Peptidoglycan DD-endopeptidases (EC 3.4.24) are overwhelmingly zinc-dependent metalloenzymes; the absence of EF-hand or other calcium-binding loop motifs further disfavors Ca(2+). Together these general biological arguments form a defensible reasoning chain favoring Zn(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the M23 peptidoglycan endopeptidase family fold and its canonical HxxH zinc-binding motif would strengthen confidence, but is not strictly required given the elimination logic above.",
    "reason": "The combination of signal peptide (eliminates pantetheine), absence of heme-binding motifs (eliminates heme b), histidine-rich metal-coordination pattern, small secreted architecture, and general knowledge that peptidoglycan hydrolases are zinc metalloenzymes provides a concrete, general-biology reasoning path to Zn(2+) without requiring memorization of this specific UniProt entry."
  },
  "case_id": "cofactor_0171",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C4",
      "H2",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9KU93 (ShyC, Peptidoglycan DD-endopeptidase, EC 3.4.24.-) annotates Zn(2+) as the cofactor (evidence C5/H5). The annotation uses ECO:0000250 (inferred by similarity to Q9KN86), making it a transferred annotation rather than a direct experimental measurement on this protein. However, the EC class 3.4.24 is specifically for metalloendopeptidases, and the 2019 reference (PubMed:30782657, H4/C7) explicitly links this protein to the Zur-dependent zinc starvation response, providing strong indirect experimental context for zinc dependence. The answer is well-supported."
  },
  "important_caveats": [
    "The UniProt Zn(2+) cofactor annotation carries evidence code ECO:0000250 (similarity to Q9KN86), i.e., it is a transferred computational annotation rather than a direct experimental zinc-binding measurement on ShyC itself.",
    "The 2019 paper (PubMed:30782657) on zinc starvation regulation provides strong indirect experimental support for zinc dependence but was not independently retrieved to confirm the exact nature of the evidence.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning_supported judgment is based solely on what a knowledgeable model could infer from the sequence and general biology.",
    "The M23-family HxxH zinc-binding motif is not trivially recognizable in this sequence without prior family knowledge, making the question moderately difficult but still answerable through elimination and general metalloenzyme reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While Zn(2+) vs. Ca(2+) is the closest pair, the histidine coordination pattern and metalloendopeptidase context clearly favor Zn(2+). Heme b and pantetheine 4'-phosphate are readily excluded by sequence features. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0171",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9KU93 (ShyC, Peptidoglycan DD-endopeptidase, EC 3.4.24.-) annotates Zn(2+) as the cofactor (evidence C5/H5). The annotation uses ECO:0000250 (inferred by similarity to Q9KN86), making it a transferred annotation rather than a direct experimental measurement on this protein. However, the EC class 3.4.24 is specifically for metalloendopeptidases, and the 2019 reference (PubMed:30782657, H4/C7) explicitly links this protein to the Zur-dependent zinc starvation response, providing strong indirect experimental context for zinc dependence. The answer is well-supported.",
    "evidence_ids": ["C5", "H5", "C4", "H2", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several sequence-level features allow elimination of three options and favor Zn(2+): (1) The N-terminal hydrophobic stretch (~20 residues) is a classic signal peptide, indicating a secreted/periplasmic protein, which eliminates pantetheine 4'-phosphate (an intracellular acyl-carrier cofactor for fatty-acid synthases). (2) The sequence lacks Cys-X-X-Cys motifs or closely spaced bis-His axial ligands characteristic of heme b coordination, making heme b unlikely. (3) The protein is small (~433 aa), secreted, and contains multiple histidine residues in spatially proximate clusters (e.g., HYPVTLDN near the N-terminus; HSNTYITKYLHL and HPHLHY regions in the C-terminal half), consistent with a zinc-coordinating metalloprotease active site. (4) Peptidoglycan DD-endopeptidases (EC 3.4.24) are overwhelmingly zinc-dependent metalloenzymes; the absence of EF-hand or other calcium-binding loop motifs further disfavors Ca(2+). Together these general biological arguments form a defensible reasoning chain favoring Zn(2+).",
    "missing_item_specific_fact": "Precise identification of the M23 peptidoglycan endopeptidase family fold and its canonical HxxH zinc-binding motif would strengthen confidence, but is not strictly required given the elimination logic above.",
    "reason": "The combination of signal peptide (eliminates pantetheine), absence of heme-binding motifs (eliminates heme b), histidine-rich metal-coordination pattern, small secreted architecture, and general knowledge that peptidoglycan hydrolases are zinc metalloenzymes provides a concrete, general-biology reasoning path to Zn(2+) without requiring memorization of this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While Zn(2+) vs. Ca(2+) is the closest pair, the histidine coordination pattern and metalloendopeptidase context clearly favor Zn(2+). Heme b and pantetheine 4'-phosphate are readily excluded by sequence features. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The UniProt Zn(2+) cofactor annotation carries evidence code ECO:0000250 (similarity to Q9KN86), i.e., it is a transferred computational annotation rather than a direct experimental zinc-binding measurement on ShyC itself.",
    "The 2019 paper (PubMed:30782657) on zinc starvation regulation provides strong indirect experimental support for zinc dependence but was not independently retrieved to confirm the exact nature of the evidence.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning_supported judgment is based solely on what a knowledgeable model could infer from the sequence and general biology.",
    "The M23-family HxxH zinc-binding motif is not trivially recognizable in this sequence without prior family knowledge, making the question moderately difficult but still answerable through elimination and general metalloenzyme reasoning."
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

**Accession:** `Q9KU93` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 105. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.755646+00:00.  

```json
"Q9KU93"
```

Source SHA-256: `4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.755646+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30782657","source":"PubMed"}],"value":"Autolysin ShyC"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23834664","source":"PubMed"}],"value":"Sidewall hydrolase C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30782657","source":"PubMed"}],"value":"3.4.24.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30782657","source":"PubMed"}],"value":"Peptidoglycan DD-endopeptidase ShyC"}}}
```

Source SHA-256: `4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.755646+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9KN86","source":"UniProtKB"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9KN86","source":"UniProtKB"}],"value":"Binds 1 zinc ion per subunit."}]}}
```

Source SHA-256: `4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KU93.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.755646+00:00.  

```json
{"citation":{"authors":["Murphy S.G.","Alvarez L.","Adams M.C.","Liu S.","Chappie J.S.","Cava F.","Doerr T."],"citationCrossReferences":[{"database":"PubMed","id":"30782657"},{"database":"DOI","id":"10.1128/mbio.02620-18"}],"citationType":"journal article","firstPage":"0","id":"30782657","journal":"MBio","lastPage":"0","publicationDate":"2019","title":"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc Starvation Response.","volume":"10"},"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30782657","source":"PubMed"}],"type":"STRAIN","value":"ATCC 39315 / El Tor Inaba N16961"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `4c68a5a19b097a0a13e179bb05c32e6e535e30c5a35f230053fa015d7637a8eb`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-01T06:28:46.934559+00:00.  

```text
DE   RecName: Full=Peptidoglycan DD-endopeptidase ShyC {ECO:0000303|PubMed:30782657};
DE            EC=3.4.24.- {ECO:0000269|PubMed:30782657};
DE   AltName: Full=Autolysin ShyC {ECO:0000303|PubMed:30782657};
DE   AltName: Full=Sidewall hydrolase C {ECO:0000303|PubMed:23834664};
```

Source SHA-256: `69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)  
**Locator:** `lines 40-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-01T06:28:46.934559+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION
RP   PHENOTYPE.
RC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:30782657};
RX   PubMed=30782657; DOI=10.1128/mbio.02620-18;
RA   Murphy S.G., Alvarez L., Adams M.C., Liu S., Chappie J.S., Cava F.,
RA   Doerr T.;
RT   "Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc
RT   Starvation Response.";
RL   MBio 10:0-0(2019).
```

Source SHA-256: `69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KU93?format=txt&versions=105)  
**Locator:** `lines 55-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-01T06:28:46.934559+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000250|UniProtKB:Q9KN86};
CC       Note=Binds 1 zinc ion per subunit. {ECO:0000250|UniProtKB:Q9KN86};
```

Source SHA-256: `69827fcfb90c56fef1edc54124463fb027192860af52edf1a74b01902c49973c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 171. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
