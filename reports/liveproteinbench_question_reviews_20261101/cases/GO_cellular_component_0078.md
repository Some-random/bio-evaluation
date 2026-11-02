# GO_cellular_component_0078

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — cytosol

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVPAARSGRKVYFIGLNAVPFLPLVAGLLRTYAEQDPRVAAGYDFQEPVFLVDGVQEMAAGITDPDVLALSCYVWNFRRQMKVARLVKERHPGMLVVAGGPHVPDRPGDFFARHPYVDVLVHGEGETAFRELLIERLADHPDYTRVPGVSVRHGTEAVPGRPAERLPRRIETPSPYLLGVMDGAVATCRQRDLRFYALWETNRGCPYSCAFCDWGSATMSALRLFDAERLQEEIEWFAEHDVEDLFVCDANFGILPRDLEIARALADARAATGAPKLIRVNFAKNSNDRVFEISKTWHDADLLMGTTLSMQSTDLDVLEAIDRKNIGLENYRKLQQRYATENIHTYTELILGLPLESPRSFRDGIGSLLEAGNHEDIRVYEFGILPNAPINTPEKIAGYGLRTVPKRLYVEEPGTPDDEAETVDMVMETNAMSRDEWVDCFGFVQAVQFLHNGCYTRYLSMYLRQRHDIGYTAFYERLQQYFGARPDTVLGSIYLRMRKLYHDYIDIPELPLANLVASQPDMAADLARYGKRRGWTIDNWGWLRIANDFERTYTELRDFVAALGVDDTSDPDLAEVFRFQQDVMLRPDYDPAAGRTTEYTADWPGYFTTGELRRRPVRMRLADQRFGANGRYTPVPGDLKAFARAAIGPSYPVSRIGHYRHRFEAAEVTSPAEPVLTEQR

[Multiple Choices]
A. incipient cellular bud site
B. cytosol
C. protein-containing complex
D. vesicle
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated to cytosol (GO:0005829) with IEA:TreeGrafter evidence. This supports the key as a computational annotation, not as direct experimental localization evidence.

Citations as saved: [H6](#evidence-h6), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long enzyme-like sequence lacks an obvious organelle-targeting signal or multiple transmembrane segments, which makes a soluble location plausible and bud-site or vesicle localization less likely. That does not establish cytosol over other possibilities, including association with a stable protein complex.


**Missing item-specific fact**

> The protein-specific cytosolic localization annotation or experimental localization evidence is not supplied in the question.


**Reason**

> The sequence gives a broad solubility-based clue but no decisive localization signal. Choosing cytosol over the remaining plausible options requires item-specific localization knowledge rather than sequence reasoning alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence alone does not establish multiple localizations; the reviewer-only annotation supports cytosol, while no evidence here establishes a stable protein-containing complex, vesicle, or bud-site localization.


### Important caveats

- The cytosol annotation is computationally inferred (IEA:TreeGrafter), not shown here to be experimentally demonstrated.
- The sequence match is exact, but the author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long enzyme-like sequence lacks an obvious organelle-targeting signal or multiple transmembrane segments, which makes a soluble location plausible and bud-site or vesicle localization less likely. That does not establish cytosol over other possibilities, including association with a stable protein complex.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cytosolic localization annotation or experimental localization evidence is not supplied in the question.",
    "reason": "The sequence gives a broad solubility-based clue but no decisive localization signal. Choosing cytosol over the remaining plausible options requires item-specific localization knowledge rather than sequence reasoning alone."
  },
  "case_id": "GO_cellular_component_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to cytosol (GO:0005829) with IEA:TreeGrafter evidence. This supports the key as a computational annotation, not as direct experimental localization evidence."
  },
  "important_caveats": [
    "The cytosol annotation is computationally inferred (IEA:TreeGrafter), not shown here to be experimentally demonstrated.",
    "The sequence match is exact, but the author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not establish multiple localizations; the reviewer-only annotation supports cytosol, while no evidence here establishes a stable protein-containing complex, vesicle, or bud-site localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to cytosol (GO:0005829) with IEA:TreeGrafter evidence. This supports the key as a computational annotation, not as direct experimental localization evidence.",
    "evidence_ids": ["H6", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long enzyme-like sequence lacks an obvious organelle-targeting signal or multiple transmembrane segments, which makes a soluble location plausible and bud-site or vesicle localization less likely. That does not establish cytosol over other possibilities, including association with a stable protein complex.",
    "missing_item_specific_fact": "The protein-specific cytosolic localization annotation or experimental localization evidence is not supplied in the question.",
    "reason": "The sequence gives a broad solubility-based clue but no decisive localization signal. Choosing cytosol over the remaining plausible options requires item-specific localization knowledge rather than sequence reasoning alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not establish multiple localizations; the reviewer-only annotation supports cytosol, while no evidence here establishes a stable protein-containing complex, vesicle, or bud-site localization."
  },
  "important_caveats": [
    "The cytosol annotation is computationally inferred (IEA:TreeGrafter), not shown here to be experimentally demonstrated.",
    "The sequence match is exact, but the author's source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q83XP3, ThnK) carries GO:0005829 (cytosol) as its sole cellular-component annotation, though with evidence code IEA:TreeGrafter (computational inference, not experimental). Biologically, ThnK is a cobalamin-dependent radical SAM methyltransferase (EC 2.1.1.394) in the thienamycin (carbapenem) biosynthetic pathway of Streptomyces cattleya. Radical SAM enzymes are soluble, cytoplasmic catalysts that use SAM and iron-sulfur clusters; they operate on small-molecule substrates in the bacterial cytoplasm. The sequence contains the canonical radical SAM motif (C-P-Y-S-C-A-F-C-D) and lacks any signal peptide or transmembrane segments. The cytosol assignment is therefore well-supported by general biochemistry, even though the specific annotation is computational.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple concrete biological arguments from the sequence and context distinguish the answer: (1) The organism is a bacterium (Streptomyces), so GO:0000131 'incipient cellular bud site'—defined in the ontology as specific to budding yeast plasma membrane—is irrelevant. (2) GO:0031982 'vesicle' is defined as a membrane-bounded organelle, a eukaryotic concept inapplicable to this bacterial soluble enzyme. (3) The sequence contains the radical SAM CxxxCxxC motif (CPYSCAFCD), identifying a soluble iron-sulfur-cluster enzyme; radical SAM enzymes are cytoplasmic. (4) The protein lacks an N-terminal signal peptide or transmembrane helices, ruling out secretion or membrane association. (5) GO:0032991 'protein-containing complex' requires evidence of a stable, experimentally verified multi-protein assembly; no such evidence exists for ThnK, and secondary-metabolite biosynthetic enzymes in Actinobacteria typically act as individual soluble catalysts. The remaining and default compartment for a soluble bacterial enzyme is cytosol.


**Missing item-specific fact**

> None that is essential. The only annotation is IEA (computational), but the biological reasoning from organism type, radical SAM biochemistry, absence of targeting signals, and GO term definitions is sufficient to select cytosol over the three distractors.


**Reason**

> A model with general knowledge of bacterial cell biology, radical SAM enzyme biochemistry, and GO term definitions can eliminate options A (yeast-specific), D (membrane-bounded organelle, inapplicable to bacteria), and C (requires stable-complex evidence absent here) to arrive at B (cytosol) without needing to look up this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are clearly inapplicable to a bacterial protein (bud site is yeast-specific; vesicle implies a membrane-bounded organelle). Option C (protein-containing complex) is a theoretical possibility for any enzyme but requires specific experimental evidence of stable multi-protein assembly, which is absent for ThnK. The default and well-supported location for a soluble bacterial radical SAM enzyme is cytosol, making B the single defensible choice.


### Important caveats

- The sole GO cellular-component annotation (GO:0005829) carries evidence code IEA:TreeGrafter, i.e., it is a computational phylogenetic inference rather than direct experimental localization. No experimental subcellular-localization data (e.g., fractionation, fluorescence microscopy) were found in the entry.
- The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), well after the original sequence submission in 2003. The benchmark author's exact source snapshot is unknown, though the sequence matches across versions.
- The protein-containing-complex option (C) is not strictly impossible in principle—some radical SAM enzymes participate in multi-enzyme assemblies—but no annotation or literature evidence supports a stable complex for ThnK specifically.
- The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence features and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple concrete biological arguments from the sequence and context distinguish the answer: (1) The organism is a bacterium (Streptomyces), so GO:0000131 'incipient cellular bud site'—defined in the ontology as specific to budding yeast plasma membrane—is irrelevant. (2) GO:0031982 'vesicle' is defined as a membrane-bounded organelle, a eukaryotic concept inapplicable to this bacterial soluble enzyme. (3) The sequence contains the radical SAM CxxxCxxC motif (CPYSCAFCD), identifying a soluble iron-sulfur-cluster enzyme; radical SAM enzymes are cytoplasmic. (4) The protein lacks an N-terminal signal peptide or transmembrane helices, ruling out secretion or membrane association. (5) GO:0032991 'protein-containing complex' requires evidence of a stable, experimentally verified multi-protein assembly; no such evidence exists for ThnK, and secondary-metabolite biosynthetic enzymes in Actinobacteria typically act as individual soluble catalysts. The remaining and default compartment for a soluble bacterial enzyme is cytosol.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None that is essential. The only annotation is IEA (computational), but the biological reasoning from organism type, radical SAM biochemistry, absence of targeting signals, and GO term definitions is sufficient to select cytosol over the three distractors.",
    "reason": "A model with general knowledge of bacterial cell biology, radical SAM enzyme biochemistry, and GO term definitions can eliminate options A (yeast-specific), D (membrane-bounded organelle, inapplicable to bacteria), and C (requires stable-complex evidence absent here) to arrive at B (cytosol) without needing to look up this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q83XP3, ThnK) carries GO:0005829 (cytosol) as its sole cellular-component annotation, though with evidence code IEA:TreeGrafter (computational inference, not experimental). Biologically, ThnK is a cobalamin-dependent radical SAM methyltransferase (EC 2.1.1.394) in the thienamycin (carbapenem) biosynthetic pathway of Streptomyces cattleya. Radical SAM enzymes are soluble, cytoplasmic catalysts that use SAM and iron-sulfur clusters; they operate on small-molecule substrates in the bacterial cytoplasm. The sequence contains the canonical radical SAM motif (C-P-Y-S-C-A-F-C-D) and lacks any signal peptide or transmembrane segments. The cytosol assignment is therefore well-supported by general biochemistry, even though the specific annotation is computational."
  },
  "important_caveats": [
    "The sole GO cellular-component annotation (GO:0005829) carries evidence code IEA:TreeGrafter, i.e., it is a computational phylogenetic inference rather than direct experimental localization. No experimental subcellular-localization data (e.g., fractionation, fluorescence microscopy) were found in the entry.",
    "The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), well after the original sequence submission in 2003. The benchmark author's exact source snapshot is unknown, though the sequence matches across versions.",
    "The protein-containing-complex option (C) is not strictly impossible in principle—some radical SAM enzymes participate in multi-enzyme assemblies—but no annotation or literature evidence supports a stable complex for ThnK specifically.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence features and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are clearly inapplicable to a bacterial protein (bud site is yeast-specific; vesicle implies a membrane-bounded organelle). Option C (protein-containing complex) is a theoretical possibility for any enzyme but requires specific experimental evidence of stable multi-protein assembly, which is absent for ThnK. The default and well-supported location for a soluble bacterial radical SAM enzyme is cytosol, making B the single defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q83XP3, ThnK) carries GO:0005829 (cytosol) as its sole cellular-component annotation, though with evidence code IEA:TreeGrafter (computational inference, not experimental). Biologically, ThnK is a cobalamin-dependent radical SAM methyltransferase (EC 2.1.1.394) in the thienamycin (carbapenem) biosynthetic pathway of Streptomyces cattleya. Radical SAM enzymes are soluble, cytoplasmic catalysts that use SAM and iron-sulfur clusters; they operate on small-molecule substrates in the bacterial cytoplasm. The sequence contains the canonical radical SAM motif (C-P-Y-S-C-A-F-C-D) and lacks any signal peptide or transmembrane segments. The cytosol assignment is therefore well-supported by general biochemistry, even though the specific annotation is computational.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H1", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple concrete biological arguments from the sequence and context distinguish the answer: (1) The organism is a bacterium (Streptomyces), so GO:0000131 'incipient cellular bud site'—defined in the ontology as specific to budding yeast plasma membrane—is irrelevant. (2) GO:0031982 'vesicle' is defined as a membrane-bounded organelle, a eukaryotic concept inapplicable to this bacterial soluble enzyme. (3) The sequence contains the radical SAM CxxxCxxC motif (CPYSCAFCD), identifying a soluble iron-sulfur-cluster enzyme; radical SAM enzymes are cytoplasmic. (4) The protein lacks an N-terminal signal peptide or transmembrane helices, ruling out secretion or membrane association. (5) GO:0032991 'protein-containing complex' requires evidence of a stable, experimentally verified multi-protein assembly; no such evidence exists for ThnK, and secondary-metabolite biosynthetic enzymes in Actinobacteria typically act as individual soluble catalysts. The remaining and default compartment for a soluble bacterial enzyme is cytosol.",
    "missing_item_specific_fact": "None that is essential. The only annotation is IEA (computational), but the biological reasoning from organism type, radical SAM biochemistry, absence of targeting signals, and GO term definitions is sufficient to select cytosol over the three distractors.",
    "reason": "A model with general knowledge of bacterial cell biology, radical SAM enzyme biochemistry, and GO term definitions can eliminate options A (yeast-specific), D (membrane-bounded organelle, inapplicable to bacteria), and C (requires stable-complex evidence absent here) to arrive at B (cytosol) without needing to look up this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are clearly inapplicable to a bacterial protein (bud site is yeast-specific; vesicle implies a membrane-bounded organelle). Option C (protein-containing complex) is a theoretical possibility for any enzyme but requires specific experimental evidence of stable multi-protein assembly, which is absent for ThnK. The default and well-supported location for a soluble bacterial radical SAM enzyme is cytosol, making B the single defensible choice."
  },
  "important_caveats": [
    "The sole GO cellular-component annotation (GO:0005829) carries evidence code IEA:TreeGrafter, i.e., it is a computational phylogenetic inference rather than direct experimental localization. No experimental subcellular-localization data (e.g., fractionation, fluorescence microscopy) were found in the entry.",
    "The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), well after the original sequence submission in 2003. The benchmark author's exact source snapshot is unknown, though the sequence matches across versions.",
    "The protein-containing-complex option (C) is not strictly impossible in principle—some radical SAM enzymes participate in multi-enzyme assemblies—but no annotation or literature evidence supports a stable complex for ThnK specifically.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence features and general biological knowledge."
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

**Accession:** `Q83XP3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
"Q83XP3"
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26240322","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"31774078","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36042702","source":"PubMed"}],"value":"2.1.1.394"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase"}}}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"citation":{"authors":["Marous D.R.","Lloyd E.P.","Buller A.R.","Moshos K.A.","Grove T.L.","Blaszczyk A.J.","Booker S.J.","Townsend C.A."],"citationCrossReferences":[{"database":"PubMed","id":"26240322"},{"database":"DOI","id":"10.1073/pnas.1508615112"}],"citationType":"journal article","firstPage":"10354","id":"26240322","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"10358","publicationDate":"2015","title":"Consecutive radical S-adenosylmethionine methylations form the ethyl side chain in thienamycin biosynthesis.","volume":"112"},"referenceComments":[{"type":"STRAIN","value":"ATCC 35852 / DSM 46488 / JCM 4925 / NBRC 14057 / NCIMB 11928 / NRRL 8057 / MA-4297"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","PATHWAY"]}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"citation":{"authors":["Sinner E.K.","Lichstrahl M.S.","Li R.","Marous D.R.","Townsend C.A."],"citationCrossReferences":[{"database":"PubMed","id":"31774078"},{"database":"DOI","id":"10.1039/c9cc07197k"}],"citationType":"journal article","firstPage":"14934","id":"31774078","journal":"Chem. Commun. (Camb.)","lastPage":"14937","publicationDate":"2019","title":"Methylations in complex carbapenem biosynthesis are catalyzed by a single cobalamin-dependent radical S-adenosylmethionine enzyme.","volume":"55"},"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83XP3.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:53.086451+00:00.  

```json
{"citation":{"authors":["Lichstrahl M.S.","Townsend C.A.","Sinner E.K."],"citationCrossReferences":[{"database":"PubMed","id":"36042702"},{"database":"DOI","id":"10.1039/d2cb00113f"}],"citationType":"journal article","firstPage":"1028","id":"36042702","journal":"RSC Chem. Biol.","lastPage":"1034","publicationDate":"2022","title":"Stereochemical course of cobalamin-dependent radical SAM methylation by TokK and ThnK.","volume":"3"},"referenceNumber":6,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","REACTION MECHANISM FOR THE FIRST METHYLATION"]}
```

Source SHA-256: `7c691f44889f41a52c576e4cd1ae8e11c3cf7188b087ddf90064e3b8af6124a1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:31:56.526994+00:00.  

```text
ID   THNK_STREN              Reviewed;         681 AA.
AC   Q83XP3; F8JND9; G8XDF2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2003, sequence version 1.
DT   28-JAN-2026, entry version 74.
DE   RecName: Full=2-(S-pantetheinyl)-carbapenam-3-carboxylate methyltransferase {ECO:0000305};
DE            EC=2.1.1.394 {ECO:0000269|PubMed:26240322, ECO:0000269|PubMed:31774078, ECO:0000269|PubMed:36042702};
GN   Name=thnK {ECO:0000303|PubMed:12725858};
GN   OrderedLocusNames=SCATT_p09050 {ECO:0000312|EMBL:AEW99098.1};
OS   Streptantibioticus cattleyicolor (strain ATCC 35852 / DSM 46488 / JCM 4925
OS   / NBRC 14057 / NRRL 8057) (Streptomyces cattleya).
OG   Plasmid pSCATT {ECO:0000312|EMBL:AEW99098.1}.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptantibioticus.
OX   NCBI_TaxID=1003195;
```

Source SHA-256: `c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83XP3?format=txt&versions=74)  
**Locator:** `lines 134-134`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:31:56.526994+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; IEA:TreeGrafter.
```

Source SHA-256: `c71dc726e36b019728f318f6abb151a59107da10d242b3c7f4b371257db94606`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
