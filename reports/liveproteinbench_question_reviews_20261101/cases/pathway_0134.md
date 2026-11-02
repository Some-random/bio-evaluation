# pathway_0134

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGFAPLLVFSLFVFAGTTKGFICSFDSIYQLGDSFSDTGNLIRQPPDGPTFCSAHFPYGETFPGMPTGRCSDGRLIIDFIATALNLPLLNPYLQQNVSFRHGVNFAVGGATALDLSFLAARGVQVYDVHSPLSTQLKWFRTYLGSICSSPKECSNKLKNALFILGNIGNNDVNYAFPNRSIEEIRAYLPFITEAVANATREIIRLGGTRVIVPGMFPLGCLARNLYFFPDGDKDDLGCLSSLNDLSIYFNSLIQQALASLRIEFPQAVIIYADYYNAWGFLFRNGPALGFNSTTMLKCCCGIGGPYNYDPDRECASQGVPVCSNPTEYIQWDGTHFTQAAYRRVAEYIIPDIIKELKCSYSSIQHLTEGREALHINERE

[Multiple Choices]
A. Alkaloid biosynthesis
B. NAD(+) biosynthesis
C. iron-sulfur cluster biosynthesis. .
D. L-valine from pyruvate: step 3/4. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry for acetylajmalan esterase 1, annotated to alkaloid and ajmaline biosynthesis with experimental evidence cited to PubMed 38212296. The historical entry also matches the sequence and carries the same pathway annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a secreted enzyme, but that does not identify its specific substrate or place it in ajmaline/alkaloid biosynthesis rather than another pathway.


**Missing item-specific fact**

> The protein-specific identity and experimentally supported function of this enzyme in ajmaline biosynthesis.


**Reason**

> Distinguishing choice A requires an item-specific functional annotation or knowledge of this protein; the sequence and choices alone provide no meaningful pathway-level discriminator.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein annotation supports alkaloid biosynthesis; no supplied evidence supports the other listed pathways.


### Important caveats

- The pathway evidence is a database annotation citing a 2024 publication; the primary study was not independently reviewed here.
- Reviewer-only accession and annotation evidence supports the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a secreted enzyme, but that does not identify its specific substrate or place it in ajmaline/alkaloid biosynthesis rather than another pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and experimentally supported function of this enzyme in ajmaline biosynthesis.",
    "reason": "Distinguishing choice A requires an item-specific functional annotation or knowledge of this protein; the sequence and choices alone provide no meaningful pathway-level discriminator."
  },
  "case_id": "pathway_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for acetylajmalan esterase 1, annotated to alkaloid and ajmaline biosynthesis with experimental evidence cited to PubMed 38212296. The historical entry also matches the sequence and carries the same pathway annotation."
  },
  "important_caveats": [
    "The pathway evidence is a database annotation citing a 2024 publication; the primary study was not independently reviewed here.",
    "Reviewer-only accession and annotation evidence supports the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation supports alkaloid biosynthesis; no supplied evidence supports the other listed pathways."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for acetylajmalan esterase 1, annotated to alkaloid and ajmaline biosynthesis with experimental evidence cited to PubMed 38212296. The historical entry also matches the sequence and carries the same pathway annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a secreted enzyme, but that does not identify its specific substrate or place it in ajmaline/alkaloid biosynthesis rather than another pathway.",
    "missing_item_specific_fact": "The protein-specific identity and experimentally supported function of this enzyme in ajmaline biosynthesis.",
    "reason": "Distinguishing choice A requires an item-specific functional annotation or knowledge of this protein; the sequence and choices alone provide no meaningful pathway-level discriminator."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation supports alkaloid biosynthesis; no supplied evidence supports the other listed pathways."
  },
  "important_caveats": [
    "The pathway evidence is a database annotation citing a 2024 publication; the primary study was not independently reviewed here.",
    "Reviewer-only accession and annotation evidence supports the key but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ4 (Acetylajmalan esterase 1, EC 3.1.1.80) from Rauvolfia serpentina is explicitly annotated with the pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' under evidence code ECO:0000269 (experimental evidence from PubMed:38212296, Guo et al. 2024 Nat. Commun.). The sequence in the question matches the UniProt entry exactly (379 aa, SHA256 match). The expected answer 'Alkaloid biosynthesis' is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus (MGFAPLLVFSLFVFAGTTKG…) displays a classic ER signal peptide (hydrophobic core followed by a small-residue cleavage region), indicating secretion via the classical secretory pathway. The protein also contains a GDSL-like motif consistent with a serine esterase (confirmed EC 3.1.1.80). Among the four choices, NAD(+) biosynthesis (cytosolic Nad enzymes), iron-sulfur cluster biosynthesis (mitochondrial Isc/Nif machinery), and L-valine biosynthesis (plastidial AHAS/KARI/DHAD) are all central/primary metabolic pathways whose enzymes are intracellular and lack ER signal peptides. A secreted esterase from what appears to be a plant protein (sequence composition, length, plant-like features) is most consistent with plant specialized/secondary metabolism, i.e., alkaloid biosynthesis. This eliminates B, C, and D on general biological grounds.


**Missing item-specific fact**

> Positive identification of 'ajmaline biosynthesis' specifically (as opposed to any other secreted plant esterase pathway) would require knowing the organism is Rauvolfia serpentina and that this esterase acts on acetylajmalan. However, among the four provided choices, the signal-peptide + esterase + plant-context reasoning is sufficient to select A over B/C/D.


**Reason**

> The discriminating argument (secreted esterase inconsistent with intracellular central-metabolism pathways) is a concrete biological inference from the sequence features and the answer choices. It does not require memorizing the UniProt annotation for this specific protein, though it benefits from general knowledge of plant pathway compartmentalization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (NAD+ biosynthesis, iron-sulfur cluster biosynthesis, valine biosynthesis) are all central metabolic pathways with intracellular enzymes, making them clearly inconsistent with a secreted esterase. Alkaloid biosynthesis is the only option compatible with a secreted plant esterase involved in specialized metabolism.


### Important caveats

- The positive identification of alkaloid biosynthesis is partly by elimination of the other three choices rather than a direct sequence-to-pathway mapping.
- The signal-peptide argument is a strong but not absolute discriminator; some central-metabolism enzymes can be membrane-associated, though none of the three distractor pathways involve secreted proteins.
- The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:38212296), so the key is not merely a computational transfer.
- The entry was first public in June 2025; the author's source snapshot date is unknown, but the sequence and annotation were stable at the historical checkpoint (entry version 2, Jan 2026).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus (MGFAPLLVFSLFVFAGTTKG…) displays a classic ER signal peptide (hydrophobic core followed by a small-residue cleavage region), indicating secretion via the classical secretory pathway. The protein also contains a GDSL-like motif consistent with a serine esterase (confirmed EC 3.1.1.80). Among the four choices, NAD(+) biosynthesis (cytosolic Nad enzymes), iron-sulfur cluster biosynthesis (mitochondrial Isc/Nif machinery), and L-valine biosynthesis (plastidial AHAS/KARI/DHAD) are all central/primary metabolic pathways whose enzymes are intracellular and lack ER signal peptides. A secreted esterase from what appears to be a plant protein (sequence composition, length, plant-like features) is most consistent with plant specialized/secondary metabolism, i.e., alkaloid biosynthesis. This eliminates B, C, and D on general biological grounds.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of 'ajmaline biosynthesis' specifically (as opposed to any other secreted plant esterase pathway) would require knowing the organism is Rauvolfia serpentina and that this esterase acts on acetylajmalan. However, among the four provided choices, the signal-peptide + esterase + plant-context reasoning is sufficient to select A over B/C/D.",
    "reason": "The discriminating argument (secreted esterase inconsistent with intracellular central-metabolism pathways) is a concrete biological inference from the sequence features and the answer choices. It does not require memorizing the UniProt annotation for this specific protein, though it benefits from general knowledge of plant pathway compartmentalization."
  },
  "case_id": "pathway_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ4 (Acetylajmalan esterase 1, EC 3.1.1.80) from Rauvolfia serpentina is explicitly annotated with the pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' under evidence code ECO:0000269 (experimental evidence from PubMed:38212296, Guo et al. 2024 Nat. Commun.). The sequence in the question matches the UniProt entry exactly (379 aa, SHA256 match). The expected answer 'Alkaloid biosynthesis' is directly and experimentally supported."
  },
  "important_caveats": [
    "The positive identification of alkaloid biosynthesis is partly by elimination of the other three choices rather than a direct sequence-to-pathway mapping.",
    "The signal-peptide argument is a strong but not absolute discriminator; some central-metabolism enzymes can be membrane-associated, though none of the three distractor pathways involve secreted proteins.",
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:38212296), so the key is not merely a computational transfer.",
    "The entry was first public in June 2025; the author's source snapshot date is unknown, but the sequence and annotation were stable at the historical checkpoint (entry version 2, Jan 2026)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (NAD+ biosynthesis, iron-sulfur cluster biosynthesis, valine biosynthesis) are all central metabolic pathways with intracellular enzymes, making them clearly inconsistent with a secreted esterase. Alkaloid biosynthesis is the only option compatible with a secreted plant esterase involved in specialized metabolism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ4 (Acetylajmalan esterase 1, EC 3.1.1.80) from Rauvolfia serpentina is explicitly annotated with the pathway 'Alkaloid biosynthesis; ajmaline biosynthesis' under evidence code ECO:0000269 (experimental evidence from PubMed:38212296, Guo et al. 2024 Nat. Commun.). The sequence in the question matches the UniProt entry exactly (379 aa, SHA256 match). The expected answer 'Alkaloid biosynthesis' is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus (MGFAPLLVFSLFVFAGTTKG…) displays a classic ER signal peptide (hydrophobic core followed by a small-residue cleavage region), indicating secretion via the classical secretory pathway. The protein also contains a GDSL-like motif consistent with a serine esterase (confirmed EC 3.1.1.80). Among the four choices, NAD(+) biosynthesis (cytosolic Nad enzymes), iron-sulfur cluster biosynthesis (mitochondrial Isc/Nif machinery), and L-valine biosynthesis (plastidial AHAS/KARI/DHAD) are all central/primary metabolic pathways whose enzymes are intracellular and lack ER signal peptides. A secreted esterase from what appears to be a plant protein (sequence composition, length, plant-like features) is most consistent with plant specialized/secondary metabolism, i.e., alkaloid biosynthesis. This eliminates B, C, and D on general biological grounds.",
    "missing_item_specific_fact": "Positive identification of 'ajmaline biosynthesis' specifically (as opposed to any other secreted plant esterase pathway) would require knowing the organism is Rauvolfia serpentina and that this esterase acts on acetylajmalan. However, among the four provided choices, the signal-peptide + esterase + plant-context reasoning is sufficient to select A over B/C/D.",
    "reason": "The discriminating argument (secreted esterase inconsistent with intracellular central-metabolism pathways) is a concrete biological inference from the sequence features and the answer choices. It does not require memorizing the UniProt annotation for this specific protein, though it benefits from general knowledge of plant pathway compartmentalization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (NAD+ biosynthesis, iron-sulfur cluster biosynthesis, valine biosynthesis) are all central metabolic pathways with intracellular enzymes, making them clearly inconsistent with a secreted esterase. Alkaloid biosynthesis is the only option compatible with a secreted plant esterase involved in specialized metabolism."
  },
  "important_caveats": [
    "The positive identification of alkaloid biosynthesis is partly by elimination of the other three choices rather than a direct sequence-to-pathway mapping.",
    "The signal-peptide argument is a strong but not absolute discriminator; some central-metabolism enzymes can be membrane-associated, though none of the three distractor pathways involve secreted proteins.",
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:38212296), so the key is not merely a computational transfer.",
    "The entry was first public in June 2025; the author's source snapshot date is unknown, but the sequence and annotation were stable at the historical checkpoint (entry version 2, Jan 2026)."
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

**Accession:** `P0DXJ4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.205752+00:00.  

```json
"P0DXJ4"
```

Source SHA-256: `bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.205752+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"3.1.1.80"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Acetylajmalan esterase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsAAE1"}]}}
```

Source SHA-256: `bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.205752+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.205752+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `bbe0aec87943a21f5f78aea35d37428c98cc5513ccdfd4e5fbdf6c718d2d5053`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:19.289362+00:00.  

```text
ID   AAE1_RAUSE              Reviewed;         379 AA.
AC   P0DXJ4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=Acetylajmalan esterase 1 {ECO:0000303|PubMed:38212296};
DE            Short=RsAAE1 {ECO:0000303|PubMed:38212296};
DE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};
DE   Flags: Precursor;
GN   Name=AAE1 {ECO:0000303|PubMed:38212296};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)  
**Locator:** `lines 17-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:19.289362+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE
RP   SPECIFICITY, AND BIOTECHNOLOGY.
RX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;
RA   Guo J., Gao D., Lian J., Qu Y.;
RT   "De novo biosynthesis of antiarrhythmic alkaloid ajmaline.";
RL   Nat. Commun. 15:457-457(2024).
```

Source SHA-256: `e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ4?format=txt&versions=2)  
**Locator:** `lines 45-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:19.289362+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `e5ce655d6be475337315d399ec6a21f2651b9e605e4c4cdcee020c20ed785069`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
