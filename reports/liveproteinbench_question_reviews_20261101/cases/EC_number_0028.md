# EC_number_0028

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.1.20

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPPLGVLLLLVALGHSTQGHRPLPIRKAHKFDWWERGNFYQIYPRSFKDSDGDGIGDLKGITQTIDYLKTIGIDGVWLSPIFKSPMNDFGYDISDFYAIQEEYGTMEDFEELAAKCASIGLKLILDFVPNHSSDEHEHFRLSEEGIEPYKDYYIWHSGVLDANGTRHPPSNWISVFRGSAWQWSDKRQQYYLHQFQKKQPDLNYRNPALVEEMKNVMRFWLNKGIAGFRIDALPYLFESEEVDGHYRDEPLSGQATDDPDNPAYLTHTETKDQPETYDMVHQWRQVVDEYTARDNFTRIILTEAYTAVQNMTRFYGTPAAPGAQIPFNFQLITLLTVNSTGRDFVNAVQSWTRAMPSGAIANWVLGNHDNSRIASRLGVARADLYNIALQTLPGIAVTYYGEEIAMVDQWISWNDTIDPAACNADPATYELYSRDPVRTPFQWSNGTNAGFSNASRTWLPVADGYRELNVAAQLAAPRSHLKTFMQLTAYRKRRLLAEGNFVLRTVGRDLVMYKRSVPGVGYVVVALNFGPEPATLPVASQFPGTGEHWLKVIASSLQAQPQAGTWINTRLYKLAPDSGIVLERLTGRNDLMT

[Multiple Choices]
A. 3.2.1.20
B. 3.2.1.8
C. 3.1.1.80
D. 5.3.3.21
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

> The sequence matches the annotated Anopheles gambiae salivary alpha-glucosidase, whose EC 3.2.1.20 catalytic activity is recorded with experimental evidence linked to PubMed 38428508.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support broad enzyme-family inferences, but it does not by itself establish the precise substrate specificity needed to distinguish alpha-glucosidase EC 3.2.1.20 from the other candidate activities.


**Missing item-specific fact**

> The protein-specific experimentally characterized catalytic activity—hydrolysis of terminal non-reducing alpha-D-glucose residues—is absent from the question input.


**Reason**

> Selecting the exact EC number depends on protein-specific functional annotation or experimental knowledge, not merely on general reasoning from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports choice A; the supplied evidence does not support another listed EC number.


### Important caveats

- The functional annotation cites experimental evidence, but the primary study was not independently reviewed here.
- Reviewer-only accession and database information establish answer support; they were not available in the original question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support broad enzyme-family inferences, but it does not by itself establish the precise substrate specificity needed to distinguish alpha-glucosidase EC 3.2.1.20 from the other candidate activities.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimentally characterized catalytic activity—hydrolysis of terminal non-reducing alpha-D-glucose residues—is absent from the question input.",
    "reason": "Selecting the exact EC number depends on protein-specific functional annotation or experimental knowledge, not merely on general reasoning from the supplied sequence."
  },
  "case_id": "EC_number_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated Anopheles gambiae salivary alpha-glucosidase, whose EC 3.2.1.20 catalytic activity is recorded with experimental evidence linked to PubMed 38428508."
  },
  "important_caveats": [
    "The functional annotation cites experimental evidence, but the primary study was not independently reviewed here.",
    "Reviewer-only accession and database information establish answer support; they were not available in the original question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports choice A; the supplied evidence does not support another listed EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated Anopheles gambiae salivary alpha-glucosidase, whose EC 3.2.1.20 catalytic activity is recorded with experimental evidence linked to PubMed 38428508.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support broad enzyme-family inferences, but it does not by itself establish the precise substrate specificity needed to distinguish alpha-glucosidase EC 3.2.1.20 from the other candidate activities.",
    "missing_item_specific_fact": "The protein-specific experimentally characterized catalytic activity—hydrolysis of terminal non-reducing alpha-D-glucose residues—is absent from the question input.",
    "reason": "Selecting the exact EC number depends on protein-specific functional annotation or experimental knowledge, not merely on general reasoning from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports choice A; the supplied evidence does not support another listed EC number."
  },
  "important_caveats": [
    "The functional annotation cites experimental evidence, but the primary study was not independently reviewed here.",
    "Reviewer-only accession and database information establish answer support; they were not available in the original question."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q7PYT9 (MALT_ANOGA, Salivary alpha-glucosidase/AnGluc from Anopheles gambiae) is annotated with EC 3.2.1.20 backed by experimental evidence (ECO:0000269, PubMed:38428508, 2024). The catalytic activity is defined as 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' The benchmark sequence SHA256 matches the UniProt canonical sequence exactly (593 aa, sequence version 3). Both current (v134) and historical (v132) records confirm EC=3.2.1.20.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several sequence features support GH31-family alpha-glucosidase (3.2.1.20) over alternatives: (1) The 'NFGPE' motif near the C-terminus is a recognized GH31 family signature; (2) The 'DFVPNHSS' region is consistent with the GH31 catalytic nucleophile Asp in a conserved context; (3) The N-terminal hydrophobic stretch 'MPPLGVLLLLVALGHSTQ' is a signal peptide indicating a secreted enzyme, consistent with a salivary digestive role; (4) Option C (3.1.1.80, pyrethroid hydrolase) requires a GxSxG serine hydrolase motif absent here; (5) Option D (5.3.3.21, steroid isomerase) requires an isomerase fold with no corresponding motifs in this sequence. The A-vs-B distinction (alpha-glucosidase vs beta-glucanase) is the hardest: GH5/GH7/GH9 beta-glucanases have distinct folds (e.g., GH5's conserved E-x-x-x-x-E) not present here, while the NFG and DFVP motifs favor GH31. However, this distinction requires specialized glycosidase-family motif knowledge rather than broad enzymology.


**Missing item-specific fact**

> Definitive assignment of GH31 family membership from primary sequence alone is borderline; without structural prediction or homology search, the alpha-vs-beta distinction relies on recognizing family-specific motifs (NFG, DFVP) that are not universally taught in general biochemistry. The actual experimental confirmation came from the 2024 Williams et al. study.


**Reason**

> The sequence provides identifiable motifs (NFGPE, DFVP, signal peptide) that a knowledgeable model could use to favor GH31 alpha-glucosidase over beta-glucanase and to exclude the esterase and isomerase options. While the A-vs-B discrimination requires specialized glycosidase-family knowledge, it is grounded in recognizable sequence features rather than pure database lookup. The distractors C and D are clearly eliminable by motif absence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (esterase) and D (isomerase) are clearly inconsistent with the sequence's domain architecture and motif content. Option B (beta-glucanase, 3.2.1.8) is the closest competitor to A, but the NFGPE and DFVP motifs favor GH31 (alpha-glucosidase) over GH5/GH7/GH9 (beta-glucanase) families. While the A-vs-B distinction is the most challenging, the available sequence features provide a defensible basis for choosing A.


### Important caveats

- The EC assignment is supported by experimental evidence (ECO:0000269) from a 2024 publication, not merely computational inference.
- The A-vs-B distinction (alpha-glucosidase vs beta-glucanase) from primary sequence alone is genuinely difficult and relies on recognizing specific GH31-family motifs; this is specialized knowledge rather than general enzymology.
- The identity of the protein as a mosquito salivary enzyme (which contextualizes the alpha-glucosidase function) is not derivable from the sequence alone without database lookup.
- The UniProt entry was first publicly released 2025-04-09; the benchmark's construction date relative to this release is unknown, though the sequence itself dates to 2007.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several sequence features support GH31-family alpha-glucosidase (3.2.1.20) over alternatives: (1) The 'NFGPE' motif near the C-terminus is a recognized GH31 family signature; (2) The 'DFVPNHSS' region is consistent with the GH31 catalytic nucleophile Asp in a conserved context; (3) The N-terminal hydrophobic stretch 'MPPLGVLLLLVALGHSTQ' is a signal peptide indicating a secreted enzyme, consistent with a salivary digestive role; (4) Option C (3.1.1.80, pyrethroid hydrolase) requires a GxSxG serine hydrolase motif absent here; (5) Option D (5.3.3.21, steroid isomerase) requires an isomerase fold with no corresponding motifs in this sequence. The A-vs-B distinction (alpha-glucosidase vs beta-glucanase) is the hardest: GH5/GH7/GH9 beta-glucanases have distinct folds (e.g., GH5's conserved E-x-x-x-x-E) not present here, while the NFG and DFVP motifs favor GH31. However, this distinction requires specialized glycosidase-family motif knowledge rather than broad enzymology.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Definitive assignment of GH31 family membership from primary sequence alone is borderline; without structural prediction or homology search, the alpha-vs-beta distinction relies on recognizing family-specific motifs (NFG, DFVP) that are not universally taught in general biochemistry. The actual experimental confirmation came from the 2024 Williams et al. study.",
    "reason": "The sequence provides identifiable motifs (NFGPE, DFVP, signal peptide) that a knowledgeable model could use to favor GH31 alpha-glucosidase over beta-glucanase and to exclude the esterase and isomerase options. While the A-vs-B discrimination requires specialized glycosidase-family knowledge, it is grounded in recognizable sequence features rather than pure database lookup. The distractors C and D are clearly eliminable by motif absence."
  },
  "case_id": "EC_number_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q7PYT9 (MALT_ANOGA, Salivary alpha-glucosidase/AnGluc from Anopheles gambiae) is annotated with EC 3.2.1.20 backed by experimental evidence (ECO:0000269, PubMed:38428508, 2024). The catalytic activity is defined as 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' The benchmark sequence SHA256 matches the UniProt canonical sequence exactly (593 aa, sequence version 3). Both current (v134) and historical (v132) records confirm EC=3.2.1.20."
  },
  "important_caveats": [
    "The EC assignment is supported by experimental evidence (ECO:0000269) from a 2024 publication, not merely computational inference.",
    "The A-vs-B distinction (alpha-glucosidase vs beta-glucanase) from primary sequence alone is genuinely difficult and relies on recognizing specific GH31-family motifs; this is specialized knowledge rather than general enzymology.",
    "The identity of the protein as a mosquito salivary enzyme (which contextualizes the alpha-glucosidase function) is not derivable from the sequence alone without database lookup.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark's construction date relative to this release is unknown, though the sequence itself dates to 2007."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (esterase) and D (isomerase) are clearly inconsistent with the sequence's domain architecture and motif content. Option B (beta-glucanase, 3.2.1.8) is the closest competitor to A, but the NFGPE and DFVP motifs favor GH31 (alpha-glucosidase) over GH5/GH7/GH9 (beta-glucanase) families. While the A-vs-B distinction is the most challenging, the available sequence features provide a defensible basis for choosing A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q7PYT9 (MALT_ANOGA, Salivary alpha-glucosidase/AnGluc from Anopheles gambiae) is annotated with EC 3.2.1.20 backed by experimental evidence (ECO:0000269, PubMed:38428508, 2024). The catalytic activity is defined as 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' The benchmark sequence SHA256 matches the UniProt canonical sequence exactly (593 aa, sequence version 3). Both current (v134) and historical (v132) records confirm EC=3.2.1.20.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several sequence features support GH31-family alpha-glucosidase (3.2.1.20) over alternatives: (1) The 'NFGPE' motif near the C-terminus is a recognized GH31 family signature; (2) The 'DFVPNHSS' region is consistent with the GH31 catalytic nucleophile Asp in a conserved context; (3) The N-terminal hydrophobic stretch 'MPPLGVLLLLVALGHSTQ' is a signal peptide indicating a secreted enzyme, consistent with a salivary digestive role; (4) Option C (3.1.1.80, pyrethroid hydrolase) requires a GxSxG serine hydrolase motif absent here; (5) Option D (5.3.3.21, steroid isomerase) requires an isomerase fold with no corresponding motifs in this sequence. The A-vs-B distinction (alpha-glucosidase vs beta-glucanase) is the hardest: GH5/GH7/GH9 beta-glucanases have distinct folds (e.g., GH5's conserved E-x-x-x-x-E) not present here, while the NFG and DFVP motifs favor GH31. However, this distinction requires specialized glycosidase-family motif knowledge rather than broad enzymology.",
    "missing_item_specific_fact": "Definitive assignment of GH31 family membership from primary sequence alone is borderline; without structural prediction or homology search, the alpha-vs-beta distinction relies on recognizing family-specific motifs (NFG, DFVP) that are not universally taught in general biochemistry. The actual experimental confirmation came from the 2024 Williams et al. study.",
    "reason": "The sequence provides identifiable motifs (NFGPE, DFVP, signal peptide) that a knowledgeable model could use to favor GH31 alpha-glucosidase over beta-glucanase and to exclude the esterase and isomerase options. While the A-vs-B discrimination requires specialized glycosidase-family knowledge, it is grounded in recognizable sequence features rather than pure database lookup. The distractors C and D are clearly eliminable by motif absence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (esterase) and D (isomerase) are clearly inconsistent with the sequence's domain architecture and motif content. Option B (beta-glucanase, 3.2.1.8) is the closest competitor to A, but the NFGPE and DFVP motifs favor GH31 (alpha-glucosidase) over GH5/GH7/GH9 (beta-glucanase) families. While the A-vs-B distinction is the most challenging, the available sequence features provide a defensible basis for choosing A."
  },
  "important_caveats": [
    "The EC assignment is supported by experimental evidence (ECO:0000269) from a 2024 publication, not merely computational inference.",
    "The A-vs-B distinction (alpha-glucosidase vs beta-glucanase) from primary sequence alone is genuinely difficult and relies on recognizing specific GH31-family motifs; this is specialized knowledge rather than general enzymology.",
    "The identity of the protein as a mosquito salivary enzyme (which contextualizes the alpha-glucosidase function) is not derivable from the sequence alone without database lookup.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark's construction date relative to this release is unknown, though the sequence itself dates to 2007."
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

**Accession:** `Q7PYT9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 132. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"value":"3.2.1.20"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"Salivary alpha-glucosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"AnGluc"}]}}
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.20","evidences":[{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"name":"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose."}}
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.588074+00:00.  

```json
{"citation":{"authors":["Williams A.E.","Gittis A.G.","Botello K.","Cruz P.","Martin-Martin I.","Valenzuela Leon P.C.","Sumner B.","Bonilla B.","Calvo E."],"citationCrossReferences":[{"database":"PubMed","id":"38428508"},{"database":"DOI","id":"10.1016/j.ibmb.2024.104097"}],"citationType":"journal article","firstPage":"104097","id":"38428508","journal":"Insect Biochem. Mol. Biol.","lastPage":"104097","publicationDate":"2024","title":"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.","volume":"167"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION","TISSUE SPECIFICITY"]}
```

Source SHA-256: `b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
ID   MALT_ANOGA              Reviewed;         593 AA.
AC   Q7PYT9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-JAN-2007, sequence version 3.
DT   28-JAN-2026, entry version 132.
DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};
DE            Short=AnGluc {ECO:0000303|PubMed:38428508};
DE            EC=3.2.1.20 {ECO:0000269|PubMed:38428508};
DE   Flags: Precursor;
GN   Name=MAL1 {ECO:0000250|UniProtKB:P13080};
GN   ORFNames=AgaP_AGAP002102 {ECO:0000312|EMBL:EAA00998.3};
OS   Anopheles gambiae (African malaria mosquito).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;
OC   Anophelinae; Anopheles.
OX   NCBI_TaxID=7165 {ECO:0000312|EMBL:EAA00998.3};
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};
DE            Short=AnGluc {ECO:0000303|PubMed:38428508};
DE            EC=3.2.1.20 {ECO:0000269|PubMed:38428508};
DE   Flags: Precursor;
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 60-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR
RP   LOCATION, AND TISSUE SPECIFICITY.
RX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;
RA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,
RA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;
RT   "Structural and functional comparisons of salivary alpha-glucosidases from
RT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex
RT   quinquefasciatus.";
RL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)  
**Locator:** `lines 74-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 3.  
**Retrieved:** 2026-11-01T06:42:03.279027+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-
CC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;
CC         Evidence={ECO:0000269|PubMed:38428508};
```

Source SHA-256: `de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
