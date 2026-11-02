# EC_number_0131

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 4.1.1.128

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKKRCLITGGAGFIGSHLAEELVKRGHPVTIVDNFYKGKSKYHEELTGNIPIIPISILDKNSMHELVNQHDVVFHLAAILGVKTTMEKSIELIETNFDGTRNILQAALKGKKKVIFASTSEVYGKGTPPFSEDDDRLYGATSKIRWSYAICKTLEETLCLGYALQGLPVTIVRYFNIYGPRAKDGPYAGVIPRFIRAALQGDDLLVYGDGKQTRCFTYVSDAVEATIAAMDEKVNGEIINIGSEDEKSIQEVAQDIHQLTHSSSKIVHVPFEKVYPHGFEEIPNRKPDVTKLKEMCQFHPNVSWEQGLKETIQWFREIEND

[Multiple Choices]
A. 4.1.1.36
B. 5.6.1.1
C. 4.1.1.128
D. 1.14.14.154
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied 321-aa sequence exactly matches the UniProt sequence for A7GKX7. UniProt assigns it EC 4.1.1.128 and links the catalytic-activity annotation to PubMed 20529859 with experimental evidence code ECO:0000269. The reported reaction is decarboxylation of UDP-2-acetamido-2-deoxy-alpha-D-glucuronate to UDP-N-acetyl-alpha-D-xylosamine and CO2, supporting choice C.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently specific substrate or reaction context to distinguish this exact decarboxylase EC number from the other enzyme classes listed.


**Missing item-specific fact**

> The protein-specific functional identification and catalytic reaction—UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase activity—are needed to select EC 4.1.1.128.


**Reason**

> The EC number specifies a particular catalyzed reaction. Recognizing the sequence or relying on general sequence heuristics would not establish that exact activity without protein-specific functional information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence has a supported annotation for choice C; the evidence provided does not support another listed choice.


### Important caveats

- The annotation and sequence-match evidence are reviewer-only and were not supplied to the evaluated model.
- The EC assignment is linked in UniProt to experimental evidence from PubMed 20529859, but the primary paper was not independently retrieved and validated here.
- The historical UniProt sequence matches exactly; the author's actual source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific substrate or reaction context to distinguish this exact decarboxylase EC number from the other enzyme classes listed.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification and catalytic reaction—UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase activity—are needed to select EC 4.1.1.128.",
    "reason": "The EC number specifies a particular catalyzed reaction. Recognizing the sequence or relying on general sequence heuristics would not establish that exact activity without protein-specific functional information."
  },
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 321-aa sequence exactly matches the UniProt sequence for A7GKX7. UniProt assigns it EC 4.1.1.128 and links the catalytic-activity annotation to PubMed 20529859 with experimental evidence code ECO:0000269. The reported reaction is decarboxylation of UDP-2-acetamido-2-deoxy-alpha-D-glucuronate to UDP-N-acetyl-alpha-D-xylosamine and CO2, supporting choice C."
  },
  "important_caveats": [
    "The annotation and sequence-match evidence are reviewer-only and were not supplied to the evaluated model.",
    "The EC assignment is linked in UniProt to experimental evidence from PubMed 20529859, but the primary paper was not independently retrieved and validated here.",
    "The historical UniProt sequence matches exactly; the author's actual source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has a supported annotation for choice C; the evidence provided does not support another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 321-aa sequence exactly matches the UniProt sequence for A7GKX7. UniProt assigns it EC 4.1.1.128 and links the catalytic-activity annotation to PubMed 20529859 with experimental evidence code ECO:0000269. The reported reaction is decarboxylation of UDP-2-acetamido-2-deoxy-alpha-D-glucuronate to UDP-N-acetyl-alpha-D-xylosamine and CO2, supporting choice C.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific substrate or reaction context to distinguish this exact decarboxylase EC number from the other enzyme classes listed.",
    "missing_item_specific_fact": "The protein-specific functional identification and catalytic reaction—UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase activity—are needed to select EC 4.1.1.128.",
    "reason": "The EC number specifies a particular catalyzed reaction. Recognizing the sequence or relying on general sequence heuristics would not establish that exact activity without protein-specific functional information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence has a supported annotation for choice C; the evidence provided does not support another listed choice."
  },
  "important_caveats": [
    "The annotation and sequence-match evidence are reviewer-only and were not supplied to the evaluated model.",
    "The EC assignment is linked in UniProt to experimental evidence from PubMed 20529859, but the primary paper was not independently retrieved and validated here.",
    "The historical UniProt sequence matches exactly; the author's actual source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 321-aa sequence matches UniProt entry A7GKX7 (UXNAS_BACCN) exactly (SHA256 confirmed). The entry annotates this protein as EC 4.1.1.128 (UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase) with evidence code ECO:0000269 (experimental evidence) from PubMed:20529859 (Gu et al., J. Biol. Chem. 2010). The catalytic reaction (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ → UDP-N-acetyl-alpha-D-xylosamine + CO2) is experimentally characterized. The sequence is 321 aa, matching the benchmark sequence length.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal region contains a Rossmann-like nucleotide-binding motif (GGAGFIGSHL…VTIVDNFYKG) and a GDGKQ motif characteristic of UDP-sugar-binding proteins, which could help a knowledgeable reader narrow the class toward nucleotide-sugar enzymes and away from a generic monooxygenase (D: 1.14.14.154) or isomerase (B: 5.6.1.1). However, both A (4.1.1.36) and C (4.1.1.128) are carboxy-lyases (decarboxylases) acting on UDP-sugar substrates. Distinguishing these two specific 4-digit EC numbers requires knowing the exact substrate (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate for 128 vs. whatever 4.1.1.36 acts on), which is not encoded in any generalizable sequence motif visible in the input.


**Missing item-specific fact**

> The specific substrate identity and reaction chemistry that differentiate EC 4.1.1.36 from EC 4.1.1.128, which must be looked up or memorized from the UniProt/database entry or the primary literature (PubMed:20529859). No sequence-derived feature in the provided 321-aa chain uniquely identifies the glucuronate→xylosamine decarboxylation over another 4.1.1.x decarboxylation.


**Reason**

> While sequence features (UDP-binding motifs, overall fold) may plausibly eliminate B and D, the critical discrimination between A and C—both 4.1.1.x decarboxylases—cannot be achieved through general biological reasoning from the sequence alone. It requires the item-specific fact of which particular UDP-sugar decarboxylation this enzyme catalyzes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (4.1.1.36) and C (4.1.1.128) belong to the same EC 4.1.1.x subclass (carboxy-lyases/decarboxylases). Without the specific substrate information, a model relying on sequence-level reasoning cannot confidently prefer one over the other. B (isomerase) and D (monooxygenase) are more readily eliminated by the UDP-binding motifs and overall architecture.


### Important caveats

- The UniProt annotation for EC 4.1.1.128 carries experimental evidence (ECO:0000269, PubMed:20529859), not merely computational inference.
- The identity of EC 4.1.1.36 (the distractor) was not independently verified in the supplied evidence; its exact reaction is not provided in the reviewer excerpts.
- The sequence was first released in 2007 but the Swiss-Prot entry was only created in 2025-02-05; the benchmark author's source snapshot is unknown.
- The Rossmann-like N-terminal motif could superficially mislead toward oxidoreductase assignments, adding noise to any sequence-based reasoning path.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a Rossmann-like nucleotide-binding motif (GGAGFIGSHL…VTIVDNFYKG) and a GDGKQ motif characteristic of UDP-sugar-binding proteins, which could help a knowledgeable reader narrow the class toward nucleotide-sugar enzymes and away from a generic monooxygenase (D: 1.14.14.154) or isomerase (B: 5.6.1.1). However, both A (4.1.1.36) and C (4.1.1.128) are carboxy-lyases (decarboxylases) acting on UDP-sugar substrates. Distinguishing these two specific 4-digit EC numbers requires knowing the exact substrate (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate for 128 vs. whatever 4.1.1.36 acts on), which is not encoded in any generalizable sequence motif visible in the input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity and reaction chemistry that differentiate EC 4.1.1.36 from EC 4.1.1.128, which must be looked up or memorized from the UniProt/database entry or the primary literature (PubMed:20529859). No sequence-derived feature in the provided 321-aa chain uniquely identifies the glucuronate→xylosamine decarboxylation over another 4.1.1.x decarboxylation.",
    "reason": "While sequence features (UDP-binding motifs, overall fold) may plausibly eliminate B and D, the critical discrimination between A and C—both 4.1.1.x decarboxylases—cannot be achieved through general biological reasoning from the sequence alone. It requires the item-specific fact of which particular UDP-sugar decarboxylation this enzyme catalyzes."
  },
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 321-aa sequence matches UniProt entry A7GKX7 (UXNAS_BACCN) exactly (SHA256 confirmed). The entry annotates this protein as EC 4.1.1.128 (UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase) with evidence code ECO:0000269 (experimental evidence) from PubMed:20529859 (Gu et al., J. Biol. Chem. 2010). The catalytic reaction (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ → UDP-N-acetyl-alpha-D-xylosamine + CO2) is experimentally characterized. The sequence is 321 aa, matching the benchmark sequence length."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.1.1.128 carries experimental evidence (ECO:0000269, PubMed:20529859), not merely computational inference.",
    "The identity of EC 4.1.1.36 (the distractor) was not independently verified in the supplied evidence; its exact reaction is not provided in the reviewer excerpts.",
    "The sequence was first released in 2007 but the Swiss-Prot entry was only created in 2025-02-05; the benchmark author's source snapshot is unknown.",
    "The Rossmann-like N-terminal motif could superficially mislead toward oxidoreductase assignments, adding noise to any sequence-based reasoning path."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (4.1.1.36) and C (4.1.1.128) belong to the same EC 4.1.1.x subclass (carboxy-lyases/decarboxylases). Without the specific substrate information, a model relying on sequence-level reasoning cannot confidently prefer one over the other. B (isomerase) and D (monooxygenase) are more readily eliminated by the UDP-binding motifs and overall architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 321-aa sequence matches UniProt entry A7GKX7 (UXNAS_BACCN) exactly (SHA256 confirmed). The entry annotates this protein as EC 4.1.1.128 (UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase) with evidence code ECO:0000269 (experimental evidence) from PubMed:20529859 (Gu et al., J. Biol. Chem. 2010). The catalytic reaction (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H+ → UDP-N-acetyl-alpha-D-xylosamine + CO2) is experimentally characterized. The sequence is 321 aa, matching the benchmark sequence length.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal region contains a Rossmann-like nucleotide-binding motif (GGAGFIGSHL…VTIVDNFYKG) and a GDGKQ motif characteristic of UDP-sugar-binding proteins, which could help a knowledgeable reader narrow the class toward nucleotide-sugar enzymes and away from a generic monooxygenase (D: 1.14.14.154) or isomerase (B: 5.6.1.1). However, both A (4.1.1.36) and C (4.1.1.128) are carboxy-lyases (decarboxylases) acting on UDP-sugar substrates. Distinguishing these two specific 4-digit EC numbers requires knowing the exact substrate (UDP-2-acetamido-2-deoxy-alpha-D-glucuronate for 128 vs. whatever 4.1.1.36 acts on), which is not encoded in any generalizable sequence motif visible in the input.",
    "missing_item_specific_fact": "The specific substrate identity and reaction chemistry that differentiate EC 4.1.1.36 from EC 4.1.1.128, which must be looked up or memorized from the UniProt/database entry or the primary literature (PubMed:20529859). No sequence-derived feature in the provided 321-aa chain uniquely identifies the glucuronate→xylosamine decarboxylation over another 4.1.1.x decarboxylation.",
    "reason": "While sequence features (UDP-binding motifs, overall fold) may plausibly eliminate B and D, the critical discrimination between A and C—both 4.1.1.x decarboxylases—cannot be achieved through general biological reasoning from the sequence alone. It requires the item-specific fact of which particular UDP-sugar decarboxylation this enzyme catalyzes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (4.1.1.36) and C (4.1.1.128) belong to the same EC 4.1.1.x subclass (carboxy-lyases/decarboxylases). Without the specific substrate information, a model relying on sequence-level reasoning cannot confidently prefer one over the other. B (isomerase) and D (monooxygenase) are more readily eliminated by the UDP-binding motifs and overall architecture."
  },
  "important_caveats": [
    "The UniProt annotation for EC 4.1.1.128 carries experimental evidence (ECO:0000269, PubMed:20529859), not merely computational inference.",
    "The identity of EC 4.1.1.36 (the distractor) was not independently verified in the supplied evidence; its exact reaction is not provided in the reviewer excerpts.",
    "The sequence was first released in 2007 but the Swiss-Prot entry was only created in 2025-02-05; the benchmark author's source snapshot is unknown.",
    "The Rossmann-like N-terminal motif could superficially mislead toward oxidoreductase assignments, adding noise to any sequence-based reasoning path."
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

**Accession:** `A7GKX7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 94. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
"A7GKX7"
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-XylNAc synthase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"value":"4.1.1.128"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-GlcNAcA decarboxylase"}]}}
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81488"}}],"reaction":{"ecNumber":"4.1.1.128","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"name":"UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81487"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:65040"},{"database":"ChEBI","id":"CHEBI:231888"}]}}
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.082856+00:00.  

```json
{"citation":{"authors":["Gu X.","Glushka J.","Lee S.G.","Bar-Peled M."],"citationCrossReferences":[{"database":"PubMed","id":"20529859"},{"database":"DOI","id":"10.1074/jbc.m110.125872"}],"citationType":"journal article","firstPage":"24825","id":"20529859","journal":"J. Biol. Chem.","lastPage":"24833","publicationDate":"2010","title":"Biosynthesis of a new UDP-sugar, UDP-2-acetamido-2-deoxyxylose, in the human pathogen Bacillus cereus subspecies cytotoxis NVH 391-98.","volume":"285"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ADE43880.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"DSM 22905 / CIP 110041 / 391-98 / NVH 391-98"}],"referenceNumber":2,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `e37b9430cdb758a34827140a4468b1360af7ce820a7d40f214a2160c678d65be`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
ID   UXNAS_BACCN             Reviewed;         321 AA.
AC   A7GKX7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-SEP-2007, sequence version 1.
DT   28-JAN-2026, entry version 94.
DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};
DE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};
DE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};
DE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};
GN   Name=UXNAcS {ECO:0000303|PubMed:20529859};
GN   OrderedLocusNames=Bcer98_0430 {ECO:0000312|EMBL:ABS20785.1};
OS   Bacillus cytotoxicus (strain DSM 22905 / CIP 110041 / 391-98 / NVH 391-98).
OC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus;
OC   Bacillus cereus group.
OX   NCBI_TaxID=315749;
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminuronate decarboxylase {ECO:0000305};
DE            Short=UDP-GlcNAcA decarboxylase {ECO:0000303|PubMed:20529859};
DE            EC=4.1.1.128 {ECO:0000269|PubMed:20529859};
DE   AltName: Full=UDP-XylNAc synthase {ECO:0000303|PubMed:20529859};
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX7?format=txt&versions=94)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 94 / 1.  
**Retrieved:** 2026-11-01T06:27:51.337169+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-
CC         acetyl-alpha-D-xylosamine + CO2; Xref=Rhea:RHEA:81487,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:65040,
CC         ChEBI:CHEBI:231888; EC=4.1.1.128;
CC         Evidence={ECO:0000269|PubMed:20529859};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81488;
CC         Evidence={ECO:0000269|PubMed:20529859};
```

Source SHA-256: `3e6a7818add6ff28d4f35cd226e812162be4e132f88da510bdff71af66aa4fea`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
