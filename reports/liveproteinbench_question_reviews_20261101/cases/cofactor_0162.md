# cofactor_0162

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSEEVQERIWILITPDKCSGCRLCEVTCSLEHEGIIWPEASRIRVFELFPGINVPHTCVQCPDYPCVNACPTNALSVDEKTGAVVVNEEKCITCGACVLACPGKVPRIPAGKGSVVICDLCGGNPKCVEICHEAGHDALKIVTGNYRPIYRTFAKDPQEKSLDIARKVFGEDF

[Multiple Choices]
A. [2Fe-2S] cluster
B. [4Fe-4S] cluster
C. Ca(2+)
D. Zn(2+)
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

> The supplied sequence exactly matches the referenced protein. UniProt records an experimentally evidenced &#91;4Fe-4S&#93; cofactor and states that it binds four such clusters per subunit; the cited structural work reports X-ray structures in complex with &#91;4Fe-4S&#93; clusters.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many cysteines provide a reasonable clue to iron-sulfur binding, distinguishing the iron-sulfur choices from Ca2+ or Zn2+ as likely candidates. They do not reliably distinguish &#91;2Fe-2S&#93; from &#91;4Fe-4S&#93; for this specific protein.


**Missing item-specific fact**

> The protein-specific finding that this subunit binds four &#91;4Fe-4S&#93; clusters, established by the cited annotation and structural study, is absent from the input.


**Reason**

> The sequence offers a broad cofactor-class clue but does not supply a dependable basis for selecting the cluster nuclearity. The correct choice depends on a protein-specific experimental or annotation fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports &#91;4Fe-4S&#93; for the sequence-matched protein; the sequence's cysteine richness alone does not make another listed option equally supported.


### Important caveats

- The experimental support is reported through UniProt evidence linked to a 2022 study and PDB structures; the primary study was not independently reviewed here.
- The reviewer-only accession and annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many cysteines provide a reasonable clue to iron-sulfur binding, distinguishing the iron-sulfur choices from Ca2+ or Zn2+ as likely candidates. They do not reliably distinguish [2Fe-2S] from [4Fe-4S] for this specific protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that this subunit binds four [4Fe-4S] clusters, established by the cited annotation and structural study, is absent from the input.",
    "reason": "The sequence offers a broad cofactor-class clue but does not supply a dependable basis for selecting the cluster nuclearity. The correct choice depends on a protein-specific experimental or annotation fact."
  },
  "case_id": "cofactor_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the referenced protein. UniProt records an experimentally evidenced [4Fe-4S] cofactor and states that it binds four such clusters per subunit; the cited structural work reports X-ray structures in complex with [4Fe-4S] clusters."
  },
  "important_caveats": [
    "The experimental support is reported through UniProt evidence linked to a 2022 study and PDB structures; the primary study was not independently reviewed here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports [4Fe-4S] for the sequence-matched protein; the sequence's cysteine richness alone does not make another listed option equally supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the referenced protein. UniProt records an experimentally evidenced [4Fe-4S] cofactor and states that it binds four such clusters per subunit; the cited structural work reports X-ray structures in complex with [4Fe-4S] clusters.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many cysteines provide a reasonable clue to iron-sulfur binding, distinguishing the iron-sulfur choices from Ca2+ or Zn2+ as likely candidates. They do not reliably distinguish [2Fe-2S] from [4Fe-4S] for this specific protein.",
    "missing_item_specific_fact": "The protein-specific finding that this subunit binds four [4Fe-4S] clusters, established by the cited annotation and structural study, is absent from the input.",
    "reason": "The sequence offers a broad cofactor-class clue but does not supply a dependable basis for selecting the cluster nuclearity. The correct choice depends on a protein-specific experimental or annotation fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports [4Fe-4S] for the sequence-matched protein; the sequence's cysteine richness alone does not make another listed option equally supported."
  },
  "important_caveats": [
    "The experimental support is reported through UniProt evidence linked to a 2022 study and PDB structures; the primary study was not independently reviewed here.",
    "The reviewer-only accession and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8U0V2 (ASORS_PYRFU, Aliphatic sulfonate oxidoreductase polyferredoxin-like subunit from Pyrococcus furiosus) annotates &#91;4Fe-4S&#93; cluster with ECO:0000269 (direct assay) from PubMed:36269456, noting 4 &#91;4Fe-4S&#93; clusters per subunit. X-ray crystallography at 1.94 Å (PDB 6X1O, 6X6U) confirmed iron-sulfur (4Fe-4S) clusters. Sequence match is exact (173 aa). The answer is well-supported by experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 173-residue sequence contains at least four Cys-X2-Cys motifs (e.g., CSGCRLCEVTCS, TCVQCPDYPCVNACP, CITCGACVLACP, ICDLCGGNPKCVEICHE) spread across the sequence, yielding ~12+ cysteines in a very small protein. This high-density, repeated Cys-X2-Cys spacing in a compact protein is the classic polyferredoxin architecture. Polyferredoxins are overwhelmingly &#91;4Fe-4S&#93; cluster proteins (textbook biochemistry: bacterial/archaeal ferredoxins carry &#91;4Fe-4S&#93;, whereas &#91;2Fe-2S&#93; clusters occur in single-cluster proteins such as Rieske proteins, plant-type ferredoxins, or glutamate synthase). Additionally, the hyperthermophilic archaeal context (Pyrococcus) favors &#91;4Fe-4S&#93; clusters, which are thermodynamically more stable at extreme temperatures than &#91;2Fe-2S&#93;. Ca(2+) and Zn(2+) are implausible for a Cys-rich electron-transfer protein lacking His/Glu/Asp metal-binding triads typical of Zn or Ca sites.


**Missing item-specific fact**

> None critical. The distinction between &#91;2Fe-2S&#93; and &#91;4Fe-4S&#93; from raw sequence motifs alone is genuinely subtle (both can be coordinated by 4 Cys), but the multiplicity of Cys-X2-Cys motifs in a 173-aa protein constitutes a recognizable polyferredoxin signature, and the general rule that polyferredoxins carry &#91;4Fe-4S&#93; clusters is standard biochemistry.


**Reason**

> A knowledgeable biologist can identify the polyferredoxin fold from the repeated Cys-X2-Cys spacing in a small protein and apply the well-established rule that polyferredoxins coordinate &#91;4Fe-4S&#93; clusters. The hyperthermophilic origin further supports &#91;4Fe-4S&#93; over &#91;2Fe-2S&#93;. While the Cys spacing alone cannot definitively exclude &#91;2Fe-2S&#93; in an isolated motif, the multiplicity and overall architecture provide meaningful grounds for the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Ca(2+) and Zn(2+) are clearly incompatible with a Cys-rich electron-transfer protein lacking canonical Zn/Ca coordination geometry. &#91;2Fe-2S&#93; is the only plausible distractor, but the polyferredoxin architecture (multiple Cys-X2-Cys motifs in a 173-aa protein) and hyperthermophilic archaeal context make &#91;4Fe-4S&#93; the strongly preferred and standard answer. No other option is genuinely defensible.


### Important caveats

- The UniProt annotation uses ECO:0000269 (direct assay) and is corroborated by X-ray crystallography (PDB 6X1O, 6X6U), so the &#91;4Fe-4S&#93; assignment is experimentally grounded, not merely computational.
- Distinguishing &#91;2Fe-2S&#93; from &#91;4Fe-4S&#93; from cysteine spacing alone is a known difficulty in bioinformatics; the reasoning here relies on the polyferredoxin architectural inference and the general rule that polyferredoxins carry &#91;4Fe-4S&#93; clusters.
- The protein is the polyferredoxin-like small subunit (WOR5-S) of a tungsten-containing aliphatic sulfonate oxidoreductase; the &#91;4Fe-4S&#93; clusters serve as electron-transfer cofactors within this complex.
- All reviewer evidence is from the current UniProt snapshot (entry version 118, 2026-09-02 annotation update); the author's source snapshot is unknown but sequence match is exact.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 173-residue sequence contains at least four Cys-X2-Cys motifs (e.g., CSGCRLCEVTCS, TCVQCPDYPCVNACP, CITCGACVLACP, ICDLCGGNPKCVEICHE) spread across the sequence, yielding ~12+ cysteines in a very small protein. This high-density, repeated Cys-X2-Cys spacing in a compact protein is the classic polyferredoxin architecture. Polyferredoxins are overwhelmingly [4Fe-4S] cluster proteins (textbook biochemistry: bacterial/archaeal ferredoxins carry [4Fe-4S], whereas [2Fe-2S] clusters occur in single-cluster proteins such as Rieske proteins, plant-type ferredoxins, or glutamate synthase). Additionally, the hyperthermophilic archaeal context (Pyrococcus) favors [4Fe-4S] clusters, which are thermodynamically more stable at extreme temperatures than [2Fe-2S]. Ca(2+) and Zn(2+) are implausible for a Cys-rich electron-transfer protein lacking His/Glu/Asp metal-binding triads typical of Zn or Ca sites.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The distinction between [2Fe-2S] and [4Fe-4S] from raw sequence motifs alone is genuinely subtle (both can be coordinated by 4 Cys), but the multiplicity of Cys-X2-Cys motifs in a 173-aa protein constitutes a recognizable polyferredoxin signature, and the general rule that polyferredoxins carry [4Fe-4S] clusters is standard biochemistry.",
    "reason": "A knowledgeable biologist can identify the polyferredoxin fold from the repeated Cys-X2-Cys spacing in a small protein and apply the well-established rule that polyferredoxins coordinate [4Fe-4S] clusters. The hyperthermophilic origin further supports [4Fe-4S] over [2Fe-2S]. While the Cys spacing alone cannot definitively exclude [2Fe-2S] in an isolated motif, the multiplicity and overall architecture provide meaningful grounds for the answer."
  },
  "case_id": "cofactor_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8U0V2 (ASORS_PYRFU, Aliphatic sulfonate oxidoreductase polyferredoxin-like subunit from Pyrococcus furiosus) annotates [4Fe-4S] cluster with ECO:0000269 (direct assay) from PubMed:36269456, noting 4 [4Fe-4S] clusters per subunit. X-ray crystallography at 1.94 Å (PDB 6X1O, 6X6U) confirmed iron-sulfur (4Fe-4S) clusters. Sequence match is exact (173 aa). The answer is well-supported by experimental evidence."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000269 (direct assay) and is corroborated by X-ray crystallography (PDB 6X1O, 6X6U), so the [4Fe-4S] assignment is experimentally grounded, not merely computational.",
    "Distinguishing [2Fe-2S] from [4Fe-4S] from cysteine spacing alone is a known difficulty in bioinformatics; the reasoning here relies on the polyferredoxin architectural inference and the general rule that polyferredoxins carry [4Fe-4S] clusters.",
    "The protein is the polyferredoxin-like small subunit (WOR5-S) of a tungsten-containing aliphatic sulfonate oxidoreductase; the [4Fe-4S] clusters serve as electron-transfer cofactors within this complex.",
    "All reviewer evidence is from the current UniProt snapshot (entry version 118, 2026-09-02 annotation update); the author's source snapshot is unknown but sequence match is exact."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Ca(2+) and Zn(2+) are clearly incompatible with a Cys-rich electron-transfer protein lacking canonical Zn/Ca coordination geometry. [2Fe-2S] is the only plausible distractor, but the polyferredoxin architecture (multiple Cys-X2-Cys motifs in a 173-aa protein) and hyperthermophilic archaeal context make [4Fe-4S] the strongly preferred and standard answer. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8U0V2 (ASORS_PYRFU, Aliphatic sulfonate oxidoreductase polyferredoxin-like subunit from Pyrococcus furiosus) annotates [4Fe-4S] cluster with ECO:0000269 (direct assay) from PubMed:36269456, noting 4 [4Fe-4S] clusters per subunit. X-ray crystallography at 1.94 Å (PDB 6X1O, 6X6U) confirmed iron-sulfur (4Fe-4S) clusters. Sequence match is exact (173 aa). The answer is well-supported by experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 173-residue sequence contains at least four Cys-X2-Cys motifs (e.g., CSGCRLCEVTCS, TCVQCPDYPCVNACP, CITCGACVLACP, ICDLCGGNPKCVEICHE) spread across the sequence, yielding ~12+ cysteines in a very small protein. This high-density, repeated Cys-X2-Cys spacing in a compact protein is the classic polyferredoxin architecture. Polyferredoxins are overwhelmingly [4Fe-4S] cluster proteins (textbook biochemistry: bacterial/archaeal ferredoxins carry [4Fe-4S], whereas [2Fe-2S] clusters occur in single-cluster proteins such as Rieske proteins, plant-type ferredoxins, or glutamate synthase). Additionally, the hyperthermophilic archaeal context (Pyrococcus) favors [4Fe-4S] clusters, which are thermodynamically more stable at extreme temperatures than [2Fe-2S]. Ca(2+) and Zn(2+) are implausible for a Cys-rich electron-transfer protein lacking His/Glu/Asp metal-binding triads typical of Zn or Ca sites.",
    "missing_item_specific_fact": "None critical. The distinction between [2Fe-2S] and [4Fe-4S] from raw sequence motifs alone is genuinely subtle (both can be coordinated by 4 Cys), but the multiplicity of Cys-X2-Cys motifs in a 173-aa protein constitutes a recognizable polyferredoxin signature, and the general rule that polyferredoxins carry [4Fe-4S] clusters is standard biochemistry.",
    "reason": "A knowledgeable biologist can identify the polyferredoxin fold from the repeated Cys-X2-Cys spacing in a small protein and apply the well-established rule that polyferredoxins coordinate [4Fe-4S] clusters. The hyperthermophilic origin further supports [4Fe-4S] over [2Fe-2S]. While the Cys spacing alone cannot definitively exclude [2Fe-2S] in an isolated motif, the multiplicity and overall architecture provide meaningful grounds for the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Ca(2+) and Zn(2+) are clearly incompatible with a Cys-rich electron-transfer protein lacking canonical Zn/Ca coordination geometry. [2Fe-2S] is the only plausible distractor, but the polyferredoxin architecture (multiple Cys-X2-Cys motifs in a 173-aa protein) and hyperthermophilic archaeal context make [4Fe-4S] the strongly preferred and standard answer. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000269 (direct assay) and is corroborated by X-ray crystallography (PDB 6X1O, 6X6U), so the [4Fe-4S] assignment is experimentally grounded, not merely computational.",
    "Distinguishing [2Fe-2S] from [4Fe-4S] from cysteine spacing alone is a known difficulty in bioinformatics; the reasoning here relies on the polyferredoxin architectural inference and the general rule that polyferredoxins carry [4Fe-4S] clusters.",
    "The protein is the polyferredoxin-like small subunit (WOR5-S) of a tungsten-containing aliphatic sulfonate oxidoreductase; the [4Fe-4S] clusters serve as electron-transfer cofactors within this complex.",
    "All reviewer evidence is from the current UniProt snapshot (entry version 118, 2026-09-02 annotation update); the author's source snapshot is unknown but sequence match is exact."
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

**Accession:** `Q8U0V2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 116. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:28.261641+00:00.  

```json
"Q8U0V2"
```

Source SHA-256: `8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:28.261641+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"Polyferredoxin-like protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"WOR5 small subunit"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"WOR5-S"}]}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aliphatic sulfonate oxidoreductase, polyferredoxin-like subunit"}}}
```

Source SHA-256: `8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:28.261641+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:49883"},"evidences":[{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"name":"[4Fe-4S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"value":"Binds 4 [4Fe-4S] clusters per subunit."}]}}
```

Source SHA-256: `8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8U0V2.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:28.261641+00:00.  

```json
{"citation":{"authors":["Mathew L.G.","Haja D.K.","Pritchett C.","McCormick W.","Zeineddine R.","Fontenot L.S.","Rivera M.E.","Glushka J.","Adams M.W.W.","Lanzilotta W.N."],"citationCrossReferences":[{"database":"PubMed","id":"36269456"},{"database":"DOI","id":"10.1007/s00775-022-01965-0"}],"citationType":"journal article","firstPage":"747","id":"36269456","journal":"J. Biol. Inorg. Chem.","lastPage":"758","publicationDate":"2022","title":"An unprecedented function for a tungsten-containing oxidoreductase.","volume":"27"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6X1O","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6X6U","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"COM1"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) IN COMPLEX WITH IRON-SULFUR (4FE-4S) CLUSTERS","FUNCTION","COFACTOR","SUBUNIT","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `8f4a9c6075c752ab49d0f94624b0784286820ad3a49f400624eec4571d207905`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:32:31.663381+00:00.  

```text
ID   ASORS_PYRFU             Reviewed;         173 AA.
AC   Q8U0V2; A0A5C0XS91;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2002, sequence version 1.
DT   28-JAN-2026, entry version 116.
DE   RecName: Full=Aliphatic sulfonate oxidoreductase, polyferredoxin-like subunit {ECO:0000305};
DE   AltName: Full=Polyferredoxin-like protein {ECO:0000303|PubMed:36269456};
DE   AltName: Full=WOR5 small subunit {ECO:0000303|PubMed:36269456};
DE            Short=WOR5-S {ECO:0000303|PubMed:36269456};
GN   OrderedLocusNames=PF1479 {ECO:0000312|EMBL:AAL81603.1};
GN   ORFNames=PFDSM3638_07415 {ECO:0000312|EMBL:QEK79108.1};
OS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).
OC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;
OC   Thermococcaceae; Pyrococcus.
OX   NCBI_TaxID=186497;
```

Source SHA-256: `baad763742d1a3d7a7dacb9ee236e356c8dd0b8bcc03e25f4cf422f6a1ec4510`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116)  
**Locator:** `lines 32-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:32:31.663381+00:00.  

```text
RN   [3] {ECO:0007744|PDB:6X1O, ECO:0007744|PDB:6X6U}
RP   X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) IN COMPLEX WITH IRON-SULFUR (4FE-4S)
RP   CLUSTERS, FUNCTION, COFACTOR, SUBUNIT, AND SUBCELLULAR LOCATION.
RC   STRAIN=COM1;
RX   PubMed=36269456; DOI=10.1007/s00775-022-01965-0;
RA   Mathew L.G., Haja D.K., Pritchett C., McCormick W., Zeineddine R.,
RA   Fontenot L.S., Rivera M.E., Glushka J., Adams M.W.W., Lanzilotta W.N.;
RT   "An unprecedented function for a tungsten-containing oxidoreductase.";
RL   J. Biol. Inorg. Chem. 27:747-758(2022).
```

Source SHA-256: `baad763742d1a3d7a7dacb9ee236e356c8dd0b8bcc03e25f4cf422f6a1ec4510`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8U0V2?format=txt&versions=116)  
**Locator:** `lines 46-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:32:31.663381+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;
CC         Evidence={ECO:0000269|PubMed:36269456};
CC       Note=Binds 4 [4Fe-4S] clusters per subunit.
CC       {ECO:0000269|PubMed:36269456};
```

Source SHA-256: `baad763742d1a3d7a7dacb9ee236e356c8dd0b8bcc03e25f4cf422f6a1ec4510`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 162. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
