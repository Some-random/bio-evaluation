# EC_number_0072

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 5.3.1.16

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSPASTPSIRGGAFASSPILRHNHLPFLRLNPPSSSPTRSSPPSIQCSVQFRPCIDIHKGKVKQIVGSTLKDLKDDDGSDPITNFESDKSAAEYATLYKQDGLKGGHVIMLGADPFSKAASLEALHAYPGGLQVGGGINSDNCLSYIEEGASHVIVTSYVFNNGQMDLERLKDLVRIVGKERLVLDLSCRKKEGKYAIVTDRWQKFSDVSLDAKVMEFLANFADEFLVHGVDVEGKKLGIDEELVALLGKHSPIPVTYAGGVTVMDDLERIRTAGMDNVDVTVGSALDIFGGNLAYKDVVAWHNQQKVSVA

[Multiple Choices]
A. 5.3.1.16
B. 5.3.1.8
C. 2.7.4.9
D. 2.1.1.348
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

> The matched 312-aa sequence is annotated as HISN3 / 5′-ProFAR isomerase with EC 5.3.1.16. The catalytic-activity annotation cites experimental evidence (ECO:0000269, PubMed:39186852), supporting choice A for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices span different reaction classes, but the supplied sequence and choices do not provide a reliable basis for identifying this particular protein's substrate and reaction, or for distinguishing EC 5.3.1.16 from another isomerase.


**Missing item-specific fact**

> The protein-specific functional identification of this sequence as HISN3 / 5′-ProFAR isomerase, catalyzing the reaction assigned EC 5.3.1.16.


**Reason**

> The correct choice is supported by sequence-matched functional annotation and cited experimental evidence, but that annotation or experimental result is absent from the question. Recognizing or retrieving the protein-specific function would be needed to select the exact EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports A for the matched sequence; no competing choice is supported by that evidence.


### Important caveats

- The sequence match is exact to the cited UniProt record, and the EC assignment is linked to experimental evidence, though the primary paper was not independently reviewed here.
- Reviewer-only accession and annotation information establish key support but were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices span different reaction classes, but the supplied sequence and choices do not provide a reliable basis for identifying this particular protein's substrate and reaction, or for distinguishing EC 5.3.1.16 from another isomerase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification of this sequence as HISN3 / 5′-ProFAR isomerase, catalyzing the reaction assigned EC 5.3.1.16.",
    "reason": "The correct choice is supported by sequence-matched functional annotation and cited experimental evidence, but that annotation or experimental result is absent from the question. Recognizing or retrieving the protein-specific function would be needed to select the exact EC number."
  },
  "case_id": "EC_number_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched 312-aa sequence is annotated as HISN3 / 5′-ProFAR isomerase with EC 5.3.1.16. The catalytic-activity annotation cites experimental evidence (ECO:0000269, PubMed:39186852), supporting choice A for this sequence."
  },
  "important_caveats": [
    "The sequence match is exact to the cited UniProt record, and the EC assignment is linked to experimental evidence, though the primary paper was not independently reviewed here.",
    "Reviewer-only accession and annotation information establish key support but were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports A for the matched sequence; no competing choice is supported by that evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched 312-aa sequence is annotated as HISN3 / 5′-ProFAR isomerase with EC 5.3.1.16. The catalytic-activity annotation cites experimental evidence (ECO:0000269, PubMed:39186852), supporting choice A for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices span different reaction classes, but the supplied sequence and choices do not provide a reliable basis for identifying this particular protein's substrate and reaction, or for distinguishing EC 5.3.1.16 from another isomerase.",
    "missing_item_specific_fact": "The protein-specific functional identification of this sequence as HISN3 / 5′-ProFAR isomerase, catalyzing the reaction assigned EC 5.3.1.16.",
    "reason": "The correct choice is supported by sequence-matched functional annotation and cited experimental evidence, but that annotation or experimental result is absent from the question. Recognizing or retrieving the protein-specific function would be needed to select the exact EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports A for the matched sequence; no competing choice is supported by that evidence."
  },
  "important_caveats": [
    "The sequence match is exact to the cited UniProt record, and the EC assignment is linked to experimental evidence, though the primary paper was not independently reviewed here.",
    "Reviewer-only accession and annotation information establish key support but were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G7IFI7 (HISN3_MEDTR, Medicago truncatula) is annotated with EC 5.3.1.16 (ProFAR isomerase) supported by experimental evidence (ECO:0000269, PubMed:39186852), including X-ray crystallography at 1.54 Å in complex with substrates 5'-ProFAR and PRFAR, catalytic activity assays, and biophysical characterization. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed, 312 aa). The annotation was made based on direct experimental characterization published in 2024.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can reason from the sequence that the protein likely adopts a TIM barrel fold (repeating βα motifs visible in the core domain) and may be an isomerase (class 5), which helps eliminate options C (2.7.4.9, a nucleotidyltransferase) and D (2.1.1.348, a methyltransferase) as different enzyme classes. However, distinguishing EC 5.3.1.16 (ProFAR isomerase) from EC 5.3.1.8 (another intramolecular oxidoreductase in the same 5.3.1.x sub-subclass) from sequence alone requires knowing the specific substrate and chemical reaction catalyzed, which cannot be determined from primary sequence without recognizing the protein's identity or having structural/active-site information.


**Missing item-specific fact**

> The specific identity of this protein as HISN3/HisA (ProFAR isomerase) and its substrate specificity (converting 5'-ProFAR to PRFAR in histidine biosynthesis) cannot be inferred from the 312-aa sequence alone. The EC assignment was established experimentally in a 2024 paper (Witek et al., Plant Physiol. Biochem.) through X-ray crystallography and kinetic assays. Distinguishing 5.3.1.16 from 5.3.1.8 requires knowledge of the exact chemical reaction, which is an item-specific experimental fact not derivable from sequence features.


**Reason**

> While the TIM barrel architecture and chloroplast transit peptide provide some class-level reasoning (isomerase, plant enzyme), the critical discrimination between two isomerases in the same EC sub-subclass (5.3.1.16 vs 5.3.1.8) depends on recognizing this specific sequence as a known HisA homolog or knowing the exact substrate. The annotation itself rests on 2024 experimental work (crystallography, kinetics), making this fundamentally a lookup/memorization task rather than a reasoning task.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (2.7.4.9, transferase) and D (2.1.1.348, methyltransferase) represent different enzyme classes and can be reasonably eliminated by recognizing the TIM barrel isomerase architecture. The real challenge is A vs B, but only A (5.3.1.16) is experimentally validated for this sequence. B (5.3.1.8) is a different isomerase with a different substrate. No genuine ambiguity exists in the correct answer, though the question is difficult without protein identification.


### Important caveats

- The UniProt entry was first public on 2025-06-18 and the key characterization paper is from 2024 (PubMed:39186852), meaning the EC annotation is very recent and unlikely to be in training data for models with earlier cutoffs.
- The EC assignment is based on experimental evidence (ECO:0000269) including X-ray crystallography at 1.54 Å resolution with substrate complexes, not computational inference.
- The sequence matches exactly (SHA256 confirmed) to UniProt G7IFI7 at both current (v84) and historical (v82) versions.
- The protein is a chloroplast-targeted precursor (312 aa) of the plant HisA homolog, which explains its longer length compared to bacterial HisA (~230 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can reason from the sequence that the protein likely adopts a TIM barrel fold (repeating βα motifs visible in the core domain) and may be an isomerase (class 5), which helps eliminate options C (2.7.4.9, a nucleotidyltransferase) and D (2.1.1.348, a methyltransferase) as different enzyme classes. However, distinguishing EC 5.3.1.16 (ProFAR isomerase) from EC 5.3.1.8 (another intramolecular oxidoreductase in the same 5.3.1.x sub-subclass) from sequence alone requires knowing the specific substrate and chemical reaction catalyzed, which cannot be determined from primary sequence without recognizing the protein's identity or having structural/active-site information.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as HISN3/HisA (ProFAR isomerase) and its substrate specificity (converting 5'-ProFAR to PRFAR in histidine biosynthesis) cannot be inferred from the 312-aa sequence alone. The EC assignment was established experimentally in a 2024 paper (Witek et al., Plant Physiol. Biochem.) through X-ray crystallography and kinetic assays. Distinguishing 5.3.1.16 from 5.3.1.8 requires knowledge of the exact chemical reaction, which is an item-specific experimental fact not derivable from sequence features.",
    "reason": "While the TIM barrel architecture and chloroplast transit peptide provide some class-level reasoning (isomerase, plant enzyme), the critical discrimination between two isomerases in the same EC sub-subclass (5.3.1.16 vs 5.3.1.8) depends on recognizing this specific sequence as a known HisA homolog or knowing the exact substrate. The annotation itself rests on 2024 experimental work (crystallography, kinetics), making this fundamentally a lookup/memorization task rather than a reasoning task."
  },
  "case_id": "EC_number_0072",
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
    "reason": "UniProt entry G7IFI7 (HISN3_MEDTR, Medicago truncatula) is annotated with EC 5.3.1.16 (ProFAR isomerase) supported by experimental evidence (ECO:0000269, PubMed:39186852), including X-ray crystallography at 1.54 Å in complex with substrates 5'-ProFAR and PRFAR, catalytic activity assays, and biophysical characterization. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed, 312 aa). The annotation was made based on direct experimental characterization published in 2024."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-06-18 and the key characterization paper is from 2024 (PubMed:39186852), meaning the EC annotation is very recent and unlikely to be in training data for models with earlier cutoffs.",
    "The EC assignment is based on experimental evidence (ECO:0000269) including X-ray crystallography at 1.54 Å resolution with substrate complexes, not computational inference.",
    "The sequence matches exactly (SHA256 confirmed) to UniProt G7IFI7 at both current (v84) and historical (v82) versions.",
    "The protein is a chloroplast-targeted precursor (312 aa) of the plant HisA homolog, which explains its longer length compared to bacterial HisA (~230 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (2.7.4.9, transferase) and D (2.1.1.348, methyltransferase) represent different enzyme classes and can be reasonably eliminated by recognizing the TIM barrel isomerase architecture. The real challenge is A vs B, but only A (5.3.1.16) is experimentally validated for this sequence. B (5.3.1.8) is a different isomerase with a different substrate. No genuine ambiguity exists in the correct answer, though the question is difficult without protein identification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G7IFI7 (HISN3_MEDTR, Medicago truncatula) is annotated with EC 5.3.1.16 (ProFAR isomerase) supported by experimental evidence (ECO:0000269, PubMed:39186852), including X-ray crystallography at 1.54 Å in complex with substrates 5'-ProFAR and PRFAR, catalytic activity assays, and biophysical characterization. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed, 312 aa). The annotation was made based on direct experimental characterization published in 2024.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can reason from the sequence that the protein likely adopts a TIM barrel fold (repeating βα motifs visible in the core domain) and may be an isomerase (class 5), which helps eliminate options C (2.7.4.9, a nucleotidyltransferase) and D (2.1.1.348, a methyltransferase) as different enzyme classes. However, distinguishing EC 5.3.1.16 (ProFAR isomerase) from EC 5.3.1.8 (another intramolecular oxidoreductase in the same 5.3.1.x sub-subclass) from sequence alone requires knowing the specific substrate and chemical reaction catalyzed, which cannot be determined from primary sequence without recognizing the protein's identity or having structural/active-site information.",
    "missing_item_specific_fact": "The specific identity of this protein as HISN3/HisA (ProFAR isomerase) and its substrate specificity (converting 5'-ProFAR to PRFAR in histidine biosynthesis) cannot be inferred from the 312-aa sequence alone. The EC assignment was established experimentally in a 2024 paper (Witek et al., Plant Physiol. Biochem.) through X-ray crystallography and kinetic assays. Distinguishing 5.3.1.16 from 5.3.1.8 requires knowledge of the exact chemical reaction, which is an item-specific experimental fact not derivable from sequence features.",
    "reason": "While the TIM barrel architecture and chloroplast transit peptide provide some class-level reasoning (isomerase, plant enzyme), the critical discrimination between two isomerases in the same EC sub-subclass (5.3.1.16 vs 5.3.1.8) depends on recognizing this specific sequence as a known HisA homolog or knowing the exact substrate. The annotation itself rests on 2024 experimental work (crystallography, kinetics), making this fundamentally a lookup/memorization task rather than a reasoning task."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (2.7.4.9, transferase) and D (2.1.1.348, methyltransferase) represent different enzyme classes and can be reasonably eliminated by recognizing the TIM barrel isomerase architecture. The real challenge is A vs B, but only A (5.3.1.16) is experimentally validated for this sequence. B (5.3.1.8) is a different isomerase with a different substrate. No genuine ambiguity exists in the correct answer, though the question is difficult without protein identification."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-06-18 and the key characterization paper is from 2024 (PubMed:39186852), meaning the EC annotation is very recent and unlikely to be in training data for models with earlier cutoffs.",
    "The EC assignment is based on experimental evidence (ECO:0000269) including X-ray crystallography at 1.54 Å resolution with substrate complexes, not computational inference.",
    "The sequence matches exactly (SHA256 confirmed) to UniProt G7IFI7 at both current (v84) and historical (v82) versions.",
    "The protein is a chloroplast-targeted precursor (312 aa) of the plant HisA homolog, which explains its longer length compared to bacterial HisA (~230 aa)."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G7IFI7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
"G7IFI7"
```

Source SHA-256: `12df9c09d392299f1b4f480c73681f58d6ac3674fbbe0ae26a955d032db1acad`.

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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:47.235961+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39186852","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:15470"}}],"reaction":{"ecNumber":"5.3.1.16","evidences":[{"evidenceCode":"ECO:0000269","id":"39186852","source":"PubMed"}],"name":"1-(5-phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-ribosylamino)methylideneamino]imidazole-4-carboxamide = 5-[(5-phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15469"},{"database":"ChEBI","id":"CHEBI:58435"},{"database":"ChEBI","id":"CHEBI:58525"}]}}
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
**Locator:** `lines 6-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:28:50.784174+00:00.  

```text
DE   RecName: Full=1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase HISN3, chloroplastic {ECO:0000303|PubMed:39186852};
DE            EC=5.3.1.16 {ECO:0000269|PubMed:39186852};
DE   AltName: Full=5'-proFAR isomerase 3 {ECO:0000303|PubMed:39186852};
DE   AltName: Full=Phosphoribosylformimino-5-aminoimidazole carboxamide ribotide isomerase HISN3 {ECO:0000303|PubMed:39186852};
DE   AltName: Full=Protein HISTIDINE BIOSYNTHESIS 3 {ECO:0000303|PubMed:39186852};
DE            Short=MtHISN3 {ECO:0000303|PubMed:39186852};
DE   Flags: Precursor;
```

Source SHA-256: `57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8`.

### Evidence H3

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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G7IFI7?format=txt&versions=82)  
**Locator:** `lines 96-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 82 / 1.  
**Retrieved:** 2026-11-02T04:28:50.784174+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=1-(5-phospho-beta-D-ribosyl)-5-[(5-phospho-beta-D-
CC         ribosylamino)methylideneamino]imidazole-4-carboxamide = 5-[(5-
CC         phospho-1-deoxy-D-ribulos-1-ylimino)methylamino]-1-(5-phospho-beta-D-
CC         ribosyl)imidazole-4-carboxamide; Xref=Rhea:RHEA:15469,
CC         ChEBI:CHEBI:58435, ChEBI:CHEBI:58525; EC=5.3.1.16;
CC         Evidence={ECO:0000269|PubMed:39186852};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:15470;
CC         Evidence={ECO:0000269|PubMed:39186852};
```

Source SHA-256: `57f4fb448243930685a2bcd3763f9d87af8412276cc9bec134a2b71d3eff2db8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
