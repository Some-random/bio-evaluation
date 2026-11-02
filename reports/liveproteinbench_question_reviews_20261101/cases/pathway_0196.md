# pathway_0196

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQCSVQFRPCIDIHKGKVKQIVGSTLKDLKDDDGSDPITNFESDKSAAEYATLYKQDGLKGGHVIMLGADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEGASHVIVTSYVFNNGQMDLERLKDLVRIVGKERLVLDLSCRKKEGKYAIVTDRWQKFSDVSLDAKVMEFLANFADEFLVHGVDVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA

[Multiple Choices]
A. terpenoid biosynthesis.
B. Pigment biosynthesis. .
C. sterol biosynthesis. .
D. Amino-acid biosynthesis
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

> The exact sequence matches the annotated chloroplastic HISN3/5′-ProFAR isomerase. Its pathway annotation places it in L-histidine biosynthesis, a branch of amino-acid biosynthesis; the cited annotation carries experimental evidence and is also present in the historical record.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein-specific identification as HISN3, catalyzing a step in histidine biosynthesis, is not supplied in the question.


**Reason**

> The sequence and choices alone provide no sufficiently discriminating biological argument for this particular pathway. Selecting D depends on identifying the protein and knowing its specific function; recognizing the sequence from an external entry would be lookup or memorization, not reasoning from supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the matched annotation, amino-acid biosynthesis is the only listed choice that captures the protein’s histidine-biosynthesis pathway.


### Important caveats

- The reviewer-only database evidence was not provided to the evaluated model.
- The source sequence matches exactly, but the author's precise database snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as HISN3, catalyzing a step in histidine biosynthesis, is not supplied in the question.",
    "reason": "The sequence and choices alone provide no sufficiently discriminating biological argument for this particular pathway. Selecting D depends on identifying the protein and knowing its specific function; recognizing the sequence from an external entry would be lookup or memorization, not reasoning from supplied information."
  },
  "case_id": "pathway_0196",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated chloroplastic HISN3/5′-ProFAR isomerase. Its pathway annotation places it in L-histidine biosynthesis, a branch of amino-acid biosynthesis; the cited annotation carries experimental evidence and is also present in the historical record."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not provided to the evaluated model.",
    "The source sequence matches exactly, but the author's precise database snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched annotation, amino-acid biosynthesis is the only listed choice that captures the protein’s histidine-biosynthesis pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated chloroplastic HISN3/5′-ProFAR isomerase. Its pathway annotation places it in L-histidine biosynthesis, a branch of amino-acid biosynthesis; the cited annotation carries experimental evidence and is also present in the historical record.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein-specific identification as HISN3, catalyzing a step in histidine biosynthesis, is not supplied in the question.",
    "reason": "The sequence and choices alone provide no sufficiently discriminating biological argument for this particular pathway. Selecting D depends on identifying the protein and knowing its specific function; recognizing the sequence from an external entry would be lookup or memorization, not reasoning from supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched annotation, amino-acid biosynthesis is the only listed choice that captures the protein’s histidine-biosynthesis pathway."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not provided to the evaluated model.",
    "The source sequence matches exactly, but the author's precise database snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G7IFI7 (HISN3_MEDTR, Medicago truncatula) is annotated with the pathway 'Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9' supported by experimental evidence (ECO:0000269, PubMed:39186852). The protein is a chloroplastic proFAR isomerase (EC 5.3.1.16), which catalyzes step 4 of histidine biosynthesis. Histidine is an amino acid, so 'Amino-acid biosynthesis' (Choice D) is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region (MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQ...) is a chloroplast transit peptide, indicating a plastid-localized enzyme. This eliminates sterol biosynthesis (C), which occurs in the ER/cytosol. The remaining ~260 residues fold into a TIM barrel with catalytic residues characteristic of an isomerase (EC 5.3.x.x). In plant biochemistry, TIM-barrel isomerases are predominantly found in amino-acid and nucleotide biosynthetic pathways (e.g., HisD, HisA, TrpF, PRAI), whereas terpenoid biosynthesis (A) relies on terpene synthases and prenyltransferases with distinct folds, and carotenoid/pigment biosynthesis (B) uses desaturases, cyclases, and hydroxylases. The combination of plastid targeting, TIM-barrel isomerase architecture, and small size (~312 aa) is most consistent with an amino-acid biosynthesis enzyme.


**Missing item-specific fact**

> Precise recognition of the HisD/proFAR-isomerase family signature (e.g., motifs around the catalytic Glu/Asp residues) would definitively distinguish this from other TIM-barrel enzymes in plastid pathways, but the general fold-and-compartment argument above provides a reasonable biological basis for selecting D over A, B, and C.


**Reason**

> General enzymology and cell-biology knowledge (plastid localization, TIM-barrel isomerase distribution across pathways) provides meaningful grounds to favor amino-acid biosynthesis over the other three options. The argument is not mathematically certain but is a defensible biological inference rather than pure memorization of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While terpenoid and pigment biosynthesis also occur in plastids, the TIM-barrel isomerase architecture is strongly associated with amino-acid biosynthesis and is inconsistent with the enzyme families used in terpenoid or carotenoid pathways. Sterol biosynthesis is excluded by the chloroplast transit peptide. No option is equally defensible given the fold and compartment evidence.


### Important caveats

- The UniProt annotation for this entry was first publicly released in June 2025 (entry version 82 in Swiss-Prot by January 2026); the author's source snapshot date is unknown. If the question was constructed before this annotation existed, the key may have been derived from sequence similarity or the 2024 Witek et al. paper rather than a pre-existing database entry.
- The chloroplast-targeting argument eliminates sterol biosynthesis but does not fully separate terpenoid (A) and pigment (B) biosynthesis, which are also plastid-localized. The distinction relies on recognizing TIM-barrel isomerase architecture as atypical for those pathways.
- All reviewer evidence is UniProt annotation (with experimental evidence codes); no independent experimental validation of the pathway assignment was performed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region (MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQ...) is a chloroplast transit peptide, indicating a plastid-localized enzyme. This eliminates sterol biosynthesis (C), which occurs in the ER/cytosol. The remaining ~260 residues fold into a TIM barrel with catalytic residues characteristic of an isomerase (EC 5.3.x.x). In plant biochemistry, TIM-barrel isomerases are predominantly found in amino-acid and nucleotide biosynthetic pathways (e.g., HisD, HisA, TrpF, PRAI), whereas terpenoid biosynthesis (A) relies on terpene synthases and prenyltransferases with distinct folds, and carotenoid/pigment biosynthesis (B) uses desaturases, cyclases, and hydroxylases. The combination of plastid targeting, TIM-barrel isomerase architecture, and small size (~312 aa) is most consistent with an amino-acid biosynthesis enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of the HisD/proFAR-isomerase family signature (e.g., motifs around the catalytic Glu/Asp residues) would definitively distinguish this from other TIM-barrel enzymes in plastid pathways, but the general fold-and-compartment argument above provides a reasonable biological basis for selecting D over A, B, and C.",
    "reason": "General enzymology and cell-biology knowledge (plastid localization, TIM-barrel isomerase distribution across pathways) provides meaningful grounds to favor amino-acid biosynthesis over the other three options. The argument is not mathematically certain but is a defensible biological inference rather than pure memorization of a database entry."
  },
  "case_id": "pathway_0196",
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
    "reason": "UniProt entry G7IFI7 (HISN3_MEDTR, Medicago truncatula) is annotated with the pathway 'Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9' supported by experimental evidence (ECO:0000269, PubMed:39186852). The protein is a chloroplastic proFAR isomerase (EC 5.3.1.16), which catalyzes step 4 of histidine biosynthesis. Histidine is an amino acid, so 'Amino-acid biosynthesis' (Choice D) is directly and experimentally supported."
  },
  "important_caveats": [
    "The UniProt annotation for this entry was first publicly released in June 2025 (entry version 82 in Swiss-Prot by January 2026); the author's source snapshot date is unknown. If the question was constructed before this annotation existed, the key may have been derived from sequence similarity or the 2024 Witek et al. paper rather than a pre-existing database entry.",
    "The chloroplast-targeting argument eliminates sterol biosynthesis but does not fully separate terpenoid (A) and pigment (B) biosynthesis, which are also plastid-localized. The distinction relies on recognizing TIM-barrel isomerase architecture as atypical for those pathways.",
    "All reviewer evidence is UniProt annotation (with experimental evidence codes); no independent experimental validation of the pathway assignment was performed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While terpenoid and pigment biosynthesis also occur in plastids, the TIM-barrel isomerase architecture is strongly associated with amino-acid biosynthesis and is inconsistent with the enzyme families used in terpenoid or carotenoid pathways. Sterol biosynthesis is excluded by the chloroplast transit peptide. No option is equally defensible given the fold and compartment evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0196",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G7IFI7 (HISN3_MEDTR, Medicago truncatula) is annotated with the pathway 'Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9' supported by experimental evidence (ECO:0000269, PubMed:39186852). The protein is a chloroplastic proFAR isomerase (EC 5.3.1.16), which catalyzes step 4 of histidine biosynthesis. Histidine is an amino acid, so 'Amino-acid biosynthesis' (Choice D) is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region (MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQ...) is a chloroplast transit peptide, indicating a plastid-localized enzyme. This eliminates sterol biosynthesis (C), which occurs in the ER/cytosol. The remaining ~260 residues fold into a TIM barrel with catalytic residues characteristic of an isomerase (EC 5.3.x.x). In plant biochemistry, TIM-barrel isomerases are predominantly found in amino-acid and nucleotide biosynthetic pathways (e.g., HisD, HisA, TrpF, PRAI), whereas terpenoid biosynthesis (A) relies on terpene synthases and prenyltransferases with distinct folds, and carotenoid/pigment biosynthesis (B) uses desaturases, cyclases, and hydroxylases. The combination of plastid targeting, TIM-barrel isomerase architecture, and small size (~312 aa) is most consistent with an amino-acid biosynthesis enzyme.",
    "missing_item_specific_fact": "Precise recognition of the HisD/proFAR-isomerase family signature (e.g., motifs around the catalytic Glu/Asp residues) would definitively distinguish this from other TIM-barrel enzymes in plastid pathways, but the general fold-and-compartment argument above provides a reasonable biological basis for selecting D over A, B, and C.",
    "reason": "General enzymology and cell-biology knowledge (plastid localization, TIM-barrel isomerase distribution across pathways) provides meaningful grounds to favor amino-acid biosynthesis over the other three options. The argument is not mathematically certain but is a defensible biological inference rather than pure memorization of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While terpenoid and pigment biosynthesis also occur in plastids, the TIM-barrel isomerase architecture is strongly associated with amino-acid biosynthesis and is inconsistent with the enzyme families used in terpenoid or carotenoid pathways. Sterol biosynthesis is excluded by the chloroplast transit peptide. No option is equally defensible given the fold and compartment evidence."
  },
  "important_caveats": [
    "The UniProt annotation for this entry was first publicly released in June 2025 (entry version 82 in Swiss-Prot by January 2026); the author's source snapshot date is unknown. If the question was constructed before this annotation existed, the key may have been derived from sequence similarity or the 2024 Witek et al. paper rather than a pre-existing database entry.",
    "The chloroplast-targeting argument eliminates sterol biosynthesis but does not fully separate terpenoid (A) and pigment (B) biosynthesis, which are also plastid-localized. The distinction relies on recognizing TIM-barrel isomerase architecture as atypical for those pathways.",
    "All reviewer evidence is UniProt annotation (with experimental evidence codes); no independent experimental validation of the pathway assignment was performed here."
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

**Accession:** `G7IFI7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 82. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"5'-proFAR isomerase 3"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"Protein HISTIDINE BIOSYNTHESIS 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"MtHISN3"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39186852","source":"PubMed"}],"value":"5.3.1.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39186852","source":"PubMed"}],"value":"1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic"}}}
```

Source SHA-256: `12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39186852","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9"}]}
```

Source SHA-256: `12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
{"citation":{"authors":["Witek W.","Imiolczyk B.","Ruszkowski M."],"citationCrossReferences":[{"database":"PubMed","id":"39186852"},{"database":"DOI","id":"10.1016/j.plaphy.2024.109065"}],"citationType":"journal article","firstPage":"109065","id":"39186852","journal":"Plant Physiol. Biochem.","lastPage":"109065","publicationDate":"2024","title":"Structural, kinetic, and evolutionary peculiarities of HISN3, a plant 5'-ProFAR isomerase.","volume":"215"},"referenceNumber":5,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) OF 42-312 IN COMPLEX WITH SODIUM ION; 5'-PROFAR AND PRFAR","FUNCTION","MUTAGENESIS OF ASP-57 AND 74-LEU--SER-80","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","COFACTOR","PATHWAY"]}
```

Source SHA-256: `12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)  
**Locator:** `lines 1-21`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:28:50.784174+00:00.  

```text
ID   HISN3_MEDTR             Reviewed;         312 AA.
AC   G7IFI7; A0A396J617; B7FHU9;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   25-JAN-2012, sequence version 1.
DT   28-JAN-2026, entry version 82.
DE   RecName: Full=1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic {ECO:0000303|PubMed:39186852};
DE            EC=5.3.1.16 {ECO:0000269|PubMed:39186852};
DE   AltName: Full=5'-proFAR isomerase 3 {ECO:0000303|PubMed:39186852};
DE   AltName: Full=Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3 {ECO:0000303|PubMed:39186852};
DE   AltName: Full=Protein HISTIDINE BIOSYNTHESIS 3 {ECO:0000303|PubMed:39186852};
DE            Short=MtHISN3 {ECO:0000303|PubMed:39186852};
DE   Flags: Precursor;
GN   Name=HISN3 {ECO:0000303|PubMed:39186852};
GN   OrderedLocusNames=MTR_2g015010 {ECO:0000312|EMBL:AES63938.1},
GN   MtrunA17_Chr2g0283151 {ECO:0000312|EMBL:RHN72021.1};
OS   Medicago truncatula (Barrel medic) (Medicago tribuloides).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   rosids; fabids; Fabales; Fabaceae; Papilionoideae; 50 kb inversion clade;
OC   NPAAA clade; Hologalegina; IRL clade; Trifolieae; Medicago.
OX   NCBI_TaxID=3880;
```

Source SHA-256: `57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)  
**Locator:** `lines 77-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:28:50.784174+00:00.  

```text
RN   [5]
RP   X-RAY CRYSTALLOGRAPHY (1.54 ANGSTROMS) OF 42-312 IN COMPLEX WITH SODIUM
RP   ION; 5'-PROFAR AND PRFAR, FUNCTION, MUTAGENESIS OF ASP-57 AND
RP   74-LEU--SER-80, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES,
RP   COFACTOR, AND PATHWAY.
RX   PubMed=39186852; DOI=10.1016/j.plaphy.2024.109065;
RA   Witek W., Imiolczyk B., Ruszkowski M.;
RT   "Structural, kinetic, and evolutionary peculiarities of HISN3, a plant 5'-
RT   ProFAR isomerase.";
RL   Plant Physiol. Biochem. 215:109065-109065(2024).
```

Source SHA-256: `57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)  
**Locator:** `lines 115-117`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:28:50.784174+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine
CC       from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9.
CC       {ECO:0000269|PubMed:39186852}.
```

Source SHA-256: `57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 196. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
