# active_site_0072

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 26 (Proton donor/acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIRILYLLVKPESMSHEQFRKECVVHFQMSAGMPGLHKYEVRLVAGNPTDTHVPYLDVGRIDAIGECWFASEEQYQVYMESDIRKAWFEHGKYFIGQLKPFVTEELV

[Multiple Choices]
A. Position 1156 (Proton donor; for dehydratase activity)
B. Position 350 (Nucleophile)
C. Position 26 (Proton donor/acceptor)
D. Position 242 (Charge relay system)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the 107-residue protein record, which annotates position 26 as an active-site proton donor/acceptor. The annotation cites a primary study that reports structural and mutagenesis work, although the annotation itself is curated evidence rather than a direct experimental result shown here.

Citations as saved: [C5](#evidence-c5), [C10](#evidence-c10), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is 107 residues long, so options at positions 242, 350, and 1156 cannot refer to residues in this protein. Position 26 is in range and is histidine, a residue chemically compatible with proton donor/acceptor activity.


**Missing item-specific fact**

> The specific assignment of His26 as this enzyme's catalytic proton donor/acceptor is protein-specific and is not established by sequence chemistry alone.


**Reason**

> The out-of-range positions provide a concrete way to distinguish the listed options from the supplied sequence; the exact catalytic role is independently supported by reviewer-only annotation, not proven from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 26 lies within the 107-residue sequence.


### Important caveats

- The database annotation and cited primary study support the expected answer, but the exact catalytic assignment is not inferable with certainty from the sequence alone.
- Reviewer-only source information was not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 107 residues long, so options at positions 242, 350, and 1156 cannot refer to residues in this protein. Position 26 is in range and is histidine, a residue chemically compatible with proton donor/acceptor activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific assignment of His26 as this enzyme's catalytic proton donor/acceptor is protein-specific and is not established by sequence chemistry alone.",
    "reason": "The out-of-range positions provide a concrete way to distinguish the listed options from the supplied sequence; the exact catalytic role is independently supported by reviewer-only annotation, not proven from the sequence."
  },
  "case_id": "active_site_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C10",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the 107-residue protein record, which annotates position 26 as an active-site proton donor/acceptor. The annotation cites a primary study that reports structural and mutagenesis work, although the annotation itself is curated evidence rather than a direct experimental result shown here."
  },
  "important_caveats": [
    "The database annotation and cited primary study support the expected answer, but the exact catalytic assignment is not inferable with certainty from the sequence alone.",
    "Reviewer-only source information was not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 26 lies within the 107-residue sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the 107-residue protein record, which annotates position 26 as an active-site proton donor/acceptor. The annotation cites a primary study that reports structural and mutagenesis work, although the annotation itself is curated evidence rather than a direct experimental result shown here.",
    "evidence_ids": ["C5", "C10", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is 107 residues long, so options at positions 242, 350, and 1156 cannot refer to residues in this protein. Position 26 is in range and is histidine, a residue chemically compatible with proton donor/acceptor activity.",
    "missing_item_specific_fact": "The specific assignment of His26 as this enzyme's catalytic proton donor/acceptor is protein-specific and is not established by sequence chemistry alone.",
    "reason": "The out-of-range positions provide a concrete way to distinguish the listed options from the supplied sequence; the exact catalytic role is independently supported by reviewer-only annotation, not proven from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 26 lies within the 107-residue sequence."
  },
  "important_caveats": [
    "The database annotation and cited primary study support the expected answer, but the exact catalytic assignment is not inferable with certainty from the sequence alone.",
    "Reviewer-only source information was not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is UniProt C5MR76 (4-carboxymethyl-4-methylbutenolide mutase / 4-methylmuconolactone methylisomerase, EC 5.4.99.14), 107 residues. UniProt annotates position 26 as Active site 'Proton donor/acceptor' (ECO:0000305, PubMed:19801657). Experimental evidence includes X-ray crystallography (PDB 3HF5, 3HFK) showing His-26 binds both 3-methylmuconolactone and 4-methylmuconolactone, and site-directed mutagenesis of His-26 (among others) from the same publication. The 26th residue in the supplied sequence is indeed H (Histidine), consistent with the annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C10](#evidence-c10), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence is 107 amino acids long. Options A (position 1156), B (position 350), and D (position 242) all reference residue numbers far exceeding the protein's length, making them physically impossible. Only option C (position 26) falls within the valid range. Additionally, position 26 in the sequence is Histidine (H), a residue well-known for proton donor/acceptor roles in enzyme catalysis, which is chemically consistent with the functional description in option C.


**Missing item-specific fact**

> None required for elimination; however, confirming that His-26 specifically acts as the proton donor/acceptor in this methylisomerase (rather than another nearby residue) would require knowledge of the crystal structure or mutagenesis data, though this is not needed to select the only viable answer.


**Reason**

> A model can determine the correct answer by (1) counting or estimating the sequence length (~107 residues), (2) eliminating options referencing positions >107 as impossible, and (3) noting that the remaining option's residue identity (His) and functional label (proton donor/acceptor) are biochemically plausible. This is a concrete logical/biological argument derivable from the supplied sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Positions 1156, 350, and 242 are all beyond the 107-residue protein, rendering options A, B, and D physically impossible. Only option C references a valid position. No ambiguity exists among the choices.


### Important caveats

- The three distractors are trivially eliminated by sequence-length arithmetic, making the question much easier than a typical active-site prediction task that would require biochemical reasoning about catalytic mechanisms.
- The UniProt annotation uses evidence code ECO:0000305 (inferred from experiment) for the active site assignment, supported by the 2009 JBC crystallography/mutagenesis study (PubMed:19801657).
- The reviewer-only evidence confirms the sequence match (SHA-256 identical between benchmark input and UniProt entry), so the annotation applies directly to the supplied sequence.
- The functional descriptions in distractors (dehydratase, nucleophile, charge relay) are mechanistically irrelevant to this methylisomerase, but this is moot given the impossible positions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence is 107 amino acids long. Options A (position 1156), B (position 350), and D (position 242) all reference residue numbers far exceeding the protein's length, making them physically impossible. Only option C (position 26) falls within the valid range. Additionally, position 26 in the sequence is Histidine (H), a residue well-known for proton donor/acceptor roles in enzyme catalysis, which is chemically consistent with the functional description in option C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required for elimination; however, confirming that His-26 specifically acts as the proton donor/acceptor in this methylisomerase (rather than another nearby residue) would require knowledge of the crystal structure or mutagenesis data, though this is not needed to select the only viable answer.",
    "reason": "A model can determine the correct answer by (1) counting or estimating the sequence length (~107 residues), (2) eliminating options referencing positions >107 as impossible, and (3) noting that the remaining option's residue identity (His) and functional label (proton donor/acceptor) are biochemically plausible. This is a concrete logical/biological argument derivable from the supplied sequence alone."
  },
  "case_id": "active_site_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C10",
      "H1",
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The protein is UniProt C5MR76 (4-carboxymethyl-4-methylbutenolide mutase / 4-methylmuconolactone methylisomerase, EC 5.4.99.14), 107 residues. UniProt annotates position 26 as Active site 'Proton donor/acceptor' (ECO:0000305, PubMed:19801657). Experimental evidence includes X-ray crystallography (PDB 3HF5, 3HFK) showing His-26 binds both 3-methylmuconolactone and 4-methylmuconolactone, and site-directed mutagenesis of His-26 (among others) from the same publication. The 26th residue in the supplied sequence is indeed H (Histidine), consistent with the annotation."
  },
  "important_caveats": [
    "The three distractors are trivially eliminated by sequence-length arithmetic, making the question much easier than a typical active-site prediction task that would require biochemical reasoning about catalytic mechanisms.",
    "The UniProt annotation uses evidence code ECO:0000305 (inferred from experiment) for the active site assignment, supported by the 2009 JBC crystallography/mutagenesis study (PubMed:19801657).",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical between benchmark input and UniProt entry), so the annotation applies directly to the supplied sequence.",
    "The functional descriptions in distractors (dehydratase, nucleophile, charge relay) are mechanistically irrelevant to this methylisomerase, but this is moot given the impossible positions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Positions 1156, 350, and 242 are all beyond the 107-residue protein, rendering options A, B, and D physically impossible. Only option C references a valid position. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is UniProt C5MR76 (4-carboxymethyl-4-methylbutenolide mutase / 4-methylmuconolactone methylisomerase, EC 5.4.99.14), 107 residues. UniProt annotates position 26 as Active site 'Proton donor/acceptor' (ECO:0000305, PubMed:19801657). Experimental evidence includes X-ray crystallography (PDB 3HF5, 3HFK) showing His-26 binds both 3-methylmuconolactone and 4-methylmuconolactone, and site-directed mutagenesis of His-26 (among others) from the same publication. The 26th residue in the supplied sequence is indeed H (Histidine), consistent with the annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C10", "H1", "H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence is 107 amino acids long. Options A (position 1156), B (position 350), and D (position 242) all reference residue numbers far exceeding the protein's length, making them physically impossible. Only option C (position 26) falls within the valid range. Additionally, position 26 in the sequence is Histidine (H), a residue well-known for proton donor/acceptor roles in enzyme catalysis, which is chemically consistent with the functional description in option C.",
    "missing_item_specific_fact": "None required for elimination; however, confirming that His-26 specifically acts as the proton donor/acceptor in this methylisomerase (rather than another nearby residue) would require knowledge of the crystal structure or mutagenesis data, though this is not needed to select the only viable answer.",
    "reason": "A model can determine the correct answer by (1) counting or estimating the sequence length (~107 residues), (2) eliminating options referencing positions >107 as impossible, and (3) noting that the remaining option's residue identity (His) and functional label (proton donor/acceptor) are biochemically plausible. This is a concrete logical/biological argument derivable from the supplied sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Positions 1156, 350, and 242 are all beyond the 107-residue protein, rendering options A, B, and D physically impossible. Only option C references a valid position. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The three distractors are trivially eliminated by sequence-length arithmetic, making the question much easier than a typical active-site prediction task that would require biochemical reasoning about catalytic mechanisms.",
    "The UniProt annotation uses evidence code ECO:0000305 (inferred from experiment) for the active site assignment, supported by the 2009 JBC crystallography/mutagenesis study (PubMed:19801657).",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical between benchmark input and UniProt entry), so the annotation applies directly to the supplied sequence.",
    "The functional descriptions in distractors (dehydratase, nucleophile, charge relay) are mechanistically irrelevant to this methylisomerase, but this is moot given the impossible positions."
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

**Accession:** `C5MR76` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 66. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
"C5MR76"
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"19801657","source":"PubMed"}],"value":"4-methylmuconolactone methylisomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"19801657","source":"PubMed"}],"value":"MLMI"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"}],"value":"5.4.99.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4-carboxymethyl-4-methylbutenolide mutase"}}}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"description":"Proton donor/acceptor","evidences":[{"evidenceCode":"ECO:0000305","id":"19801657","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":26},"start":{"modifier":"EXACT","value":26}},"type":"Active site"}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"3HF5","source":"PDB"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:57883"}],"ligand":{"id":"ChEBI:CHEBI:57883","name":"3-methylmuconolactone"},"location":{"end":{"modifier":"EXACT","value":26},"start":{"modifier":"EXACT","value":26}},"type":"Binding site"}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"3HFK","source":"PDB"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:57888"}],"ligand":{"id":"ChEBI:CHEBI:57888","name":"4-methylmuconolactone"},"location":{"end":{"modifier":"EXACT","value":26},"start":{"modifier":"EXACT","value":26}},"type":"Binding site"}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"citation":{"authors":["Marin M.","Heinz D.W.","Pieper D.H.","Klink B.U."],"citationCrossReferences":[{"database":"PubMed","id":"19801657"},{"database":"DOI","id":"10.1074/jbc.m109.024604"}],"citationType":"journal article","firstPage":"32709","id":"19801657","journal":"J. Biol. Chem.","lastPage":"32716","publicationDate":"2009","title":"Crystal structure and catalytic mechanism of 4-methylmuconolactone methylisomerase.","volume":"284"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ACR82080.1","source":"EMBL"},{"evidenceCode":"ECO:0007744","id":"3HDS","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"3HF5","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"3HFK","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 18361 / CCUG 53116 / MT1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","X-RAY CRYSTALLOGRAPHY (1.40 ANGSTROMS) IN COMPLEX WITH 3-METHYLMUCONOLACTONE AND OF MUTANT ALA-52 IN COMPLEX WITH 4-METHYLMUCONOLACTONE","FUNCTION","CATALYTIC ACTIVITY","PROPOSED REACTION MECHANISM","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN","ACTIVE SITE","MUTAGENESIS OF HIS-26; TYR-39; HIS-52 AND CYS-67"]}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
ID   MMLI_PSERE              Reviewed;         107 AA.
AC   C5MR76;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-JUL-2009, sequence version 1.
DT   28-JAN-2026, entry version 66.
DE   RecName: Full=4-carboxymethyl-4-methylbutenolide mutase {ECO:0000305};
DE            EC=5.4.99.14 {ECO:0000269|PubMed:19801657};
DE   AltName: Full=4-methylmuconolactone methylisomerase {ECO:0000303|PubMed:19801657};
DE            Short=MLMI {ECO:0000303|PubMed:19801657};
GN   Name=mmlI {ECO:0000303|PubMed:19801657, ECO:0000303|PubMed:20061479};
GN   ORFNames=BVK86_00405 {ECO:0000312|EMBL:OLU05856.1},
GN   F7R15_00410 {ECO:0000312|EMBL:KAB0488369.1},
GN   SAMN04490202_5523 {ECO:0000312|EMBL:SDP67526.1};
OS   Pseudomonas reinekei.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.
OX   NCBI_TaxID=395598;
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 18-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:ACR82080.1, ECO:0007744|PDB:3HDS, ECO:0007744|PDB:3HF5, ECO:0007744|PDB:3HFK}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (1.40 ANGSTROMS)
RP   IN COMPLEX WITH 3-METHYLMUCONOLACTONE AND OF MUTANT ALA-52 IN COMPLEX WITH
RP   4-METHYLMUCONOLACTONE, FUNCTION, CATALYTIC ACTIVITY, PROPOSED REACTION
RP   MECHANISM, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT,
RP   DOMAIN, ACTIVE SITE, AND MUTAGENESIS OF HIS-26; TYR-39; HIS-52 AND CYS-67.
RC   STRAIN=DSM 18361 / CCUG 53116 / MT1;
RX   PubMed=19801657; DOI=10.1074/jbc.m109.024604;
RA   Marin M., Heinz D.W., Pieper D.H., Klink B.U.;
RT   "Crystal structure and catalytic mechanism of 4-methylmuconolactone
RT   methylisomerase.";
RL   J. Biol. Chem. 284:32709-32716(2009).
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 115-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
FT   ACT_SITE        26
FT                   /note="Proton donor/acceptor"
FT                   /evidence="ECO:0000305|PubMed:19801657"
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 118-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
FT   BINDING         26
FT                   /ligand="3-methylmuconolactone"
FT                   /ligand_id="ChEBI:CHEBI:57883"
FT                   /evidence="ECO:0000269|PubMed:19801657,
FT                   ECO:0007744|PDB:3HF5"
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 123-127`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
FT   BINDING         26
FT                   /ligand="4-methylmuconolactone"
FT                   /ligand_id="ChEBI:CHEBI:57888"
FT                   /evidence="ECO:0000269|PubMed:19801657,
FT                   ECO:0007744|PDB:3HFK"
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
