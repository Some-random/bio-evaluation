# GO_cellular_component_0085

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — ribosome

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSEKAQNPMRELRIQKLVLNISVGESGDRLTRAAKVLEQLSGQTPVYSKARYTVRQFGIRRNEKIAVHVTVRGPKAEEILERGLKVKEYELRRRNFSETGNFGFGISEHIDLGIKYDPSIGIYGMDFYCCMTRPGERVAKRRRCKSRIGASHRITREETIRWFKQRFDGIVR

[Multiple Choices]
A. mitochondrial outer membrane
B. endocytic vesicle
C. ribosome
D. periplasmic space
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

> The sequence matches a UniProt entry identifying the protein as large ribosomal subunit protein uL5. The ribosome GO annotation is computational (IEA), while a cited structural study places the protein in a nascent 5S ribonucleoprotein complex. Together these support choice C, though the GO annotation itself is not experimental localization evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The protein is relatively short and lacks an obvious transmembrane segment or secretion signal; its basic character is compatible with an RNA-associated protein and makes ribosome more plausible than several alternatives. These are suggestive, not decisive, clues.


**Missing item-specific fact**

> Identifying this particular sequence as ribosomal protein uL5, or recognizing its conserved ribosomal-protein sequence features, is needed to distinguish ribosome reliably from other soluble or peripheral proteins.


**Reason**

> The supplied sequence offers broad localization clues but no unambiguous targeting signal or recognizable function stated in the prompt. A reliable choice depends on protein-specific identity or annotation not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> For the matched protein, the ribosomal-protein identity supports C; the alternatives lack comparable support.


### Important caveats

- The reviewer-only database identity and annotations were absent from the evaluated model input.
- The ribosome GO annotation is computational; the cited structural evidence concerns a nascent 5S RNP complex.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is relatively short and lacks an obvious transmembrane segment or secretion signal; its basic character is compatible with an RNA-associated protein and makes ribosome more plausible than several alternatives. These are suggestive, not decisive, clues.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this particular sequence as ribosomal protein uL5, or recognizing its conserved ribosomal-protein sequence features, is needed to distinguish ribosome reliably from other soluble or peripheral proteins.",
    "reason": "The supplied sequence offers broad localization clues but no unambiguous targeting signal or recognizable function stated in the prompt. A reliable choice depends on protein-specific identity or annotation not supplied to the evaluated model."
  },
  "case_id": "GO_cellular_component_0085",
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
    "reason": "The sequence matches a UniProt entry identifying the protein as large ribosomal subunit protein uL5. The ribosome GO annotation is computational (IEA), while a cited structural study places the protein in a nascent 5S ribonucleoprotein complex. Together these support choice C, though the GO annotation itself is not experimental localization evidence."
  },
  "important_caveats": [
    "The reviewer-only database identity and annotations were absent from the evaluated model input.",
    "The ribosome GO annotation is computational; the cited structural evidence concerns a nascent 5S RNP complex.",
    "The exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For the matched protein, the ribosomal-protein identity supports C; the alternatives lack comparable support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches a UniProt entry identifying the protein as large ribosomal subunit protein uL5. The ribosome GO annotation is computational (IEA), while a cited structural study places the protein in a nascent 5S ribonucleoprotein complex. Together these support choice C, though the GO annotation itself is not experimental localization evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The protein is relatively short and lacks an obvious transmembrane segment or secretion signal; its basic character is compatible with an RNA-associated protein and makes ribosome more plausible than several alternatives. These are suggestive, not decisive, clues.",
    "missing_item_specific_fact": "Identifying this particular sequence as ribosomal protein uL5, or recognizing its conserved ribosomal-protein sequence features, is needed to distinguish ribosome reliably from other soluble or peripheral proteins.",
    "reason": "The supplied sequence offers broad localization clues but no unambiguous targeting signal or recognizable function stated in the prompt. A reliable choice depends on protein-specific identity or annotation not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For the matched protein, the ribosomal-protein identity supports C; the alternatives lack comparable support."
  },
  "important_caveats": [
    "The reviewer-only database identity and annotations were absent from the evaluated model input.",
    "The ribosome GO annotation is computational; the cited structural evidence concerns a nascent 5S RNP complex.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt G0SHQ2 identifies this protein as 'Large ribosomal subunit protein uL5' (60S ribosomal protein L11) from Chaetomium thermophilum. GO annotation GO:0005840 (ribosome) is present. PDB structure 7OZS provides experimental evidence placing this protein in the ribosome (in complex with RPL5, RRS1, RPF2, SYO1, and 5S RNA). The sequence matches exactly. The expected answer C (ribosome) is well-supported by both computational annotation and structural biology evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 173-residue sequence exhibits multiple features diagnostic of a ribosomal protein: (1) small size typical of ribosomal proteins; (2) clusters of basic residues (RRR, KRR, RRRCKSR) consistent with RNA-binding; (3) a zinc-binding cysteine motif (CCMTRPGERVAKRRRCKSRIG) characteristic of ribosomal protein L11/L5 family folds; (4) no N-terminal amphipathic helix with positive charges that would indicate mitochondrial targeting (rules out A); (5) no transmembrane segments or vesicle-targeting motifs (rules out B); (6) no N-terminal signal peptide for secretion (rules out D, periplasmic space). The combination of positive ribosomal features and absence of targeting signals for other compartments provides a concrete biological argument for ribosome.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable biologist can distinguish the answer from the sequence alone: the small basic protein with a zinc-binding CC motif and absence of any targeting signal (mitochondrial presequence, signal peptide, TM domains) provides grounds to select ribosome over the alternatives. The zinc-binding motif pattern is a well-known hallmark of ribosomal proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> All four options are clearly distinguishable from the sequence features. Mitochondrial outer membrane requires a targeting presequence (absent). Endocytic vesicle requires TM domains or vesicle-sorting motifs (absent). Periplasmic space requires a signal peptide for secretion (absent). The ribosomal protein features (small size, basic residues, zinc-binding motif) positively support option C.


### Important caveats

- The primary GO annotation evidence code is IEA:InterPro (inferred from electronic annotation), though the PDB 7OZS structure provides experimental confirmation of ribosomal localization.
- The protein is from a fungus (Chaetomium thermophilum); periplasmic space exists in fungi but requires a signal peptide for targeting, which is absent here.
- The zinc-binding motif identification relies on general knowledge of ribosomal protein structural families; a reader unfamiliar with ribosomal protein folds might find the reasoning less straightforward.
- The UniProt entry was first publicly released in February 2025; the benchmark construction date is unknown but the sequence has been available since 2011.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 173-residue sequence exhibits multiple features diagnostic of a ribosomal protein: (1) small size typical of ribosomal proteins; (2) clusters of basic residues (RRR, KRR, RRRCKSR) consistent with RNA-binding; (3) a zinc-binding cysteine motif (CCMTRPGERVAKRRRCKSRIG) characteristic of ribosomal protein L11/L5 family folds; (4) no N-terminal amphipathic helix with positive charges that would indicate mitochondrial targeting (rules out A); (5) no transmembrane segments or vesicle-targeting motifs (rules out B); (6) no N-terminal signal peptide for secretion (rules out D, periplasmic space). The combination of positive ribosomal features and absence of targeting signals for other compartments provides a concrete biological argument for ribosome.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable biologist can distinguish the answer from the sequence alone: the small basic protein with a zinc-binding CC motif and absence of any targeting signal (mitochondrial presequence, signal peptide, TM domains) provides grounds to select ribosome over the alternatives. The zinc-binding motif pattern is a well-known hallmark of ribosomal proteins."
  },
  "case_id": "GO_cellular_component_0085",
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
    "reason": "UniProt G0SHQ2 identifies this protein as 'Large ribosomal subunit protein uL5' (60S ribosomal protein L11) from Chaetomium thermophilum. GO annotation GO:0005840 (ribosome) is present. PDB structure 7OZS provides experimental evidence placing this protein in the ribosome (in complex with RPL5, RRS1, RPF2, SYO1, and 5S RNA). The sequence matches exactly. The expected answer C (ribosome) is well-supported by both computational annotation and structural biology evidence."
  },
  "important_caveats": [
    "The primary GO annotation evidence code is IEA:InterPro (inferred from electronic annotation), though the PDB 7OZS structure provides experimental confirmation of ribosomal localization.",
    "The protein is from a fungus (Chaetomium thermophilum); periplasmic space exists in fungi but requires a signal peptide for targeting, which is absent here.",
    "The zinc-binding motif identification relies on general knowledge of ribosomal protein structural families; a reader unfamiliar with ribosomal protein folds might find the reasoning less straightforward.",
    "The UniProt entry was first publicly released in February 2025; the benchmark construction date is unknown but the sequence has been available since 2011."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "All four options are clearly distinguishable from the sequence features. Mitochondrial outer membrane requires a targeting presequence (absent). Endocytic vesicle requires TM domains or vesicle-sorting motifs (absent). Periplasmic space requires a signal peptide for secretion (absent). The ribosomal protein features (small size, basic residues, zinc-binding motif) positively support option C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt G0SHQ2 identifies this protein as 'Large ribosomal subunit protein uL5' (60S ribosomal protein L11) from Chaetomium thermophilum. GO annotation GO:0005840 (ribosome) is present. PDB structure 7OZS provides experimental evidence placing this protein in the ribosome (in complex with RPL5, RRS1, RPF2, SYO1, and 5S RNA). The sequence matches exactly. The expected answer C (ribosome) is well-supported by both computational annotation and structural biology evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 173-residue sequence exhibits multiple features diagnostic of a ribosomal protein: (1) small size typical of ribosomal proteins; (2) clusters of basic residues (RRR, KRR, RRRCKSR) consistent with RNA-binding; (3) a zinc-binding cysteine motif (CCMTRPGERVAKRRRCKSRIG) characteristic of ribosomal protein L11/L5 family folds; (4) no N-terminal amphipathic helix with positive charges that would indicate mitochondrial targeting (rules out A); (5) no transmembrane segments or vesicle-targeting motifs (rules out B); (6) no N-terminal signal peptide for secretion (rules out D, periplasmic space). The combination of positive ribosomal features and absence of targeting signals for other compartments provides a concrete biological argument for ribosome.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable biologist can distinguish the answer from the sequence alone: the small basic protein with a zinc-binding CC motif and absence of any targeting signal (mitochondrial presequence, signal peptide, TM domains) provides grounds to select ribosome over the alternatives. The zinc-binding motif pattern is a well-known hallmark of ribosomal proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "All four options are clearly distinguishable from the sequence features. Mitochondrial outer membrane requires a targeting presequence (absent). Endocytic vesicle requires TM domains or vesicle-sorting motifs (absent). Periplasmic space requires a signal peptide for secretion (absent). The ribosomal protein features (small size, basic residues, zinc-binding motif) positively support option C."
  },
  "important_caveats": [
    "The primary GO annotation evidence code is IEA:InterPro (inferred from electronic annotation), though the PDB 7OZS structure provides experimental confirmation of ribosomal localization.",
    "The protein is from a fungus (Chaetomium thermophilum); periplasmic space exists in fungi but requires a signal peptide for targeting, which is absent here.",
    "The zinc-binding motif identification relies on general knowledge of ribosomal protein structural families; a reader unfamiliar with ribosomal protein folds might find the reasoning less straightforward.",
    "The UniProt entry was first publicly released in February 2025; the benchmark construction date is unknown but the sequence has been available since 2011."
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

**Accession:** `G0SHQ2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 53. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SHQ2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:28.267161+00:00.  

```json
"G0SHQ2"
```

Source SHA-256: `93360df0d16107081f9d9e8f13a70e6d32229c478daab4d9194a6b07f3ea13c6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SHQ2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:28.267161+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"60S ribosomal protein L11"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"ctRPL11"}]}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"Large ribosomal subunit protein uL5"}}}
```

Source SHA-256: `93360df0d16107081f9d9e8f13a70e6d32229c478daab4d9194a6b07f3ea13c6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SHQ2.json)  
**Locator:** `/uniProtKBCrossReferences/70`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:28.267161+00:00.  

```json
{"database":"GO","id":"GO:0005840","properties":[{"key":"GoTerm","value":"C:ribosome"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `93360df0d16107081f9d9e8f13a70e6d32229c478daab4d9194a6b07f3ea13c6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SHQ2.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:28.267161+00:00.  

```json
{"citation":{"authors":["Castillo Duque de Estrada N.M.","Thoms M.","Flemming D.","Hammaren H.M.","Buschauer R.","Ameismeier M.","Bassler J.","Beck M.","Beckmann R.","Hurt E."],"citationCrossReferences":[{"database":"PubMed","id":"37291423"},{"database":"DOI","id":"10.1038/s41594-023-01006-7"}],"citationType":"journal article","firstPage":"1119","id":"37291423","journal":"Nat. Struct. Mol. Biol.","lastPage":"1131","publicationDate":"2023","title":"Structure of nascent 5S RNPs at the crossroad between ribosome assembly and MDM2-p53 pathways.","volume":"30"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7OZS","source":"PDB"}],"referenceNumber":7,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (3.50 ANGSTROMS) IN COMPLEX WITH RPL5; RRS1; RPF2; SYO1 AND 5S RNA","FUNCTION","SUBUNIT"]}
```

Source SHA-256: `93360df0d16107081f9d9e8f13a70e6d32229c478daab4d9194a6b07f3ea13c6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SHQ2?format=txt&versions=53)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 53 / 1.  
**Retrieved:** 2026-11-02T04:28:31.089069+00:00.  

```text
ID   RL11_CHATD              Reviewed;         173 AA.
AC   G0SHQ2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-OCT-2011, sequence version 1.
DT   28-JAN-2026, entry version 53.
DE   RecName: Full=Large ribosomal subunit protein uL5 {ECO:0000305|PubMed:37291423};
DE   AltName: Full=60S ribosomal protein L11 {ECO:0000305|PubMed:37291423};
DE            Short=ctRPL11 {ECO:0000305|PubMed:37291423};
GN   ORFNames=HT_0072970 {ECO:0000312|EMBL:EGS16972.1};
OS   Chaetomium thermophilum (strain DSM 1495 / CBS 144.50 / IMI 039719)
OS   (Thermochaetoides thermophila).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Thermochaetoides.
OX   NCBI_TaxID=759272;
```

Source SHA-256: `72c3302c793ecbc5f0bfc6b777abbb1139c3555a4df5e636bd916a71b826d7f8`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SHQ2?format=txt&versions=53)  
**Locator:** `lines 63-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 53 / 1.  
**Retrieved:** 2026-11-02T04:28:31.089069+00:00.  

```text
RN   [7] {ECO:0007744|PDB:7OZS}
RP   STRUCTURE BY ELECTRON MICROSCOPY (3.50 ANGSTROMS) IN COMPLEX WITH RPL5;
RP   RRS1; RPF2; SYO1 AND 5S RNA, FUNCTION, AND SUBUNIT.
RX   PubMed=37291423; DOI=10.1038/s41594-023-01006-7;
RA   Castillo Duque de Estrada N.M., Thoms M., Flemming D., Hammaren H.M.,
RA   Buschauer R., Ameismeier M., Bassler J., Beck M., Beckmann R., Hurt E.;
RT   "Structure of nascent 5S RNPs at the crossroad between ribosome assembly
RT   and MDM2-p53 pathways.";
RL   Nat. Struct. Mol. Biol. 30:1119-1131(2023).
```

Source SHA-256: `72c3302c793ecbc5f0bfc6b777abbb1139c3555a4df5e636bd916a71b826d7f8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SHQ2?format=txt&versions=53)  
**Locator:** `lines 163-163`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 53 / 1.  
**Retrieved:** 2026-11-02T04:28:31.089069+00:00.  

```text
DR   GO; GO:0005840; C:ribosome; IEA:UniProtKB-KW.
```

Source SHA-256: `72c3302c793ecbc5f0bfc6b777abbb1139c3555a4df5e636bd916a71b826d7f8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
