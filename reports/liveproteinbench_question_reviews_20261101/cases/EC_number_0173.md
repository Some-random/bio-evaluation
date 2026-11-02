# EC_number_0173

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 6.3.2.35

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKKIAIIFGGNSPEYTVSLASATSAIEALQSSPYDYDLSLIGIAPDAMDWYLYTGELENIRQDTWLLDTKHKQKIQPLFEGNGFWLSEEQQTLVPDVLFPIMHGKYGEDGSIQGLFELMKLPYVGCGVAGSALCMNKWLLHQAAAAIGVQSAPTILLTNQANQQEQIEAFIQTHGFPVFFKPNEAGSSKGITKVTCVEEIASALKEAFTYCSAVLLQKNIAGVEIGCGILGNDSLTVGACDAISLVDGFFDFEEKYQLISAKITVPAPLPETIETKVKEQAQLLYRSLGLKGLARIDFFVTERGELYLNEINTMPGFTSHSRYPAMMAAVGLSYQELLQKLLVLAKEEVK

[Multiple Choices]
A. 6.3.5.1
B. 1.1.1.1
C. 6.3.2.35
D. 3.2.1.31
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

> The exact 350-aa sequence matches the UniProt VanC2 entry, whose annotated reaction is D-serine + D-alanine + ATP → D-alanyl-D-serine + ADP + phosphate. The EC 6.3.2.35 annotation cites publications reporting experimental characterization of VanC2 as a D-Ala-D-Ser ligase.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support recognizing an ATP-dependent ligase rather than the dehydrogenase or glycosidase options, but it does not establish the substrate specificity needed to distinguish EC 6.3.2.35 from another ligase class.


**Missing item-specific fact**

> The protein's specific catalytic reaction—ligation of D-alanine and D-serine to form D-alanyl-D-serine—is not provided and is needed to identify the complete EC number.


**Reason**

> The precise EC assignment depends on protein-specific substrate and reaction knowledge absent from the input. Reviewer-only sequence-matched annotations and experimental citations support the key, but do not make that fact available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options name distinct EC activities, and the sequence-matched evidence supports C. The limitation is that the input does not supply enough information to infer that precise activity, not that multiple options are supported by the evidence.


### Important caveats

- The supporting database annotation is linked to experimental evidence in cited publications; the cited papers were not independently reviewed here.
- The author’s exact source snapshot is unknown, but the sequence matches both the current and checked historical UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support recognizing an ATP-dependent ligase rather than the dehydrogenase or glycosidase options, but it does not establish the substrate specificity needed to distinguish EC 6.3.2.35 from another ligase class.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific catalytic reaction—ligation of D-alanine and D-serine to form D-alanyl-D-serine—is not provided and is needed to identify the complete EC number.",
    "reason": "The precise EC assignment depends on protein-specific substrate and reaction knowledge absent from the input. Reviewer-only sequence-matched annotations and experimental citations support the key, but do not make that fact available to the evaluated model."
  },
  "case_id": "EC_number_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact 350-aa sequence matches the UniProt VanC2 entry, whose annotated reaction is D-serine + D-alanine + ATP → D-alanyl-D-serine + ADP + phosphate. The EC 6.3.2.35 annotation cites publications reporting experimental characterization of VanC2 as a D-Ala-D-Ser ligase."
  },
  "important_caveats": [
    "The supporting database annotation is linked to experimental evidence in cited publications; the cited papers were not independently reviewed here.",
    "The author’s exact source snapshot is unknown, but the sequence matches both the current and checked historical UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options name distinct EC activities, and the sequence-matched evidence supports C. The limitation is that the input does not supply enough information to infer that precise activity, not that multiple options are supported by the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 350-aa sequence matches the UniProt VanC2 entry, whose annotated reaction is D-serine + D-alanine + ATP → D-alanyl-D-serine + ADP + phosphate. The EC 6.3.2.35 annotation cites publications reporting experimental characterization of VanC2 as a D-Ala-D-Ser ligase.",
    "evidence_ids": ["C1", "C5", "C6", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support recognizing an ATP-dependent ligase rather than the dehydrogenase or glycosidase options, but it does not establish the substrate specificity needed to distinguish EC 6.3.2.35 from another ligase class.",
    "missing_item_specific_fact": "The protein's specific catalytic reaction—ligation of D-alanine and D-serine to form D-alanyl-D-serine—is not provided and is needed to identify the complete EC number.",
    "reason": "The precise EC assignment depends on protein-specific substrate and reaction knowledge absent from the input. Reviewer-only sequence-matched annotations and experimental citations support the key, but do not make that fact available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options name distinct EC activities, and the sequence-matched evidence supports C. The limitation is that the input does not supply enough information to infer that precise activity, not that multiple options are supported by the evidence."
  },
  "important_caveats": [
    "The supporting database annotation is linked to experimental evidence in cited publications; the cited papers were not independently reviewed here.",
    "The author’s exact source snapshot is unknown, but the sequence matches both the current and checked historical UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q47720 (VanC2 from Enterococcus casseliflavus) is annotated as EC 6.3.2.35 with experimental evidence codes (ECO:0000269) from PubMed:9294159 (Park et al. 1997, PNAS) and PubMed:9545431 (Healy et al. 1998, Chem. Biol.). The catalytic reaction D-serine + D-alanine + ATP → D-alanyl-D-serine + ADP + phosphate + H(+) is experimentally characterized. Sequence match is exact (SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmarks of the D-Ala-D-Ala/Van-type ligase superfamily: (1) an N-terminal lipoprotein signal peptide (GGNSPEY) characteristic of membrane-anchored Van ligases, (2) a glycine-rich loop region (GCGVAGSALCM) typical of the Ddl/VanA/VanB/VanC fold, and (3) a total length (~350 aa) consistent with this family rather than glutamine synthase (~450 aa, octameric, distinct fold). These features eliminate EC 6.3.5.1 (glutamine synthase, wrong family/size/fold). The absence of a Rossmann fold (GxGxxG) or NAD(P)-binding motifs eliminates EC 1.1.1.1 (oxidoreductase). The absence of catalytic aspartate/glutamate pairs and the overall fold eliminate EC 3.2.1.31 (beta-glucuronidase, a glycosidase). Since 6.3.2.35 is the only 6.3.2.x option, identifying the protein as a Van-type D-amino-acid ligase suffices to select C.


**Missing item-specific fact**

> None critical. Distinguishing 6.3.2.35 from other 6.3.2.x sub-numbers (e.g., 6.3.2.1 D-Ala-D-Ala ligase) would require active-site residue analysis, but no such competing option is presented.


**Reason**

> A knowledgeable reader can eliminate three of four options through structural/family-level sequence reasoning (signal peptide, glycine-rich loop, absence of oxidoreductase or glycosidase motifs). The remaining option is the correct answer. This requires specialized enzyme-family knowledge but is grounded in observable sequence features rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC classes (1, 3, 6) and two different 6.3 subclasses (6.3.2 vs 6.3.5). The sequence features clearly point to the Ddl/Van ligase family, making C the only defensible choice. No other option is biologically plausible for this sequence.


### Important caveats

- The VanC2 entry was first released in Swiss-Prot in 2025 (firstPublicDate 2025-04-09); the historical entry version 147 is from 2026-01-28. The author's source snapshot is unknown, but the sequence and EC annotation have been stable since the 1997/1998 characterization papers.
- Recognizing the Ddl/Van ligase family from sequence requires familiarity with this well-studied antibiotic-resistance enzyme superfamily; this is specialized but standard biochemistry knowledge rather than obscure database lookup.
- The specific distinction between VanC2 (6.3.2.35, D-Ala-D-Ser) and VanA (6.3.2.-, D-Ala-D-Ala/D-Lac) ligases relies on active-site residues (Phe-250, Arg-322 per Healy 1998), but this level of discrimination is not needed here since no competing 6.3.2.x option is offered.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmarks of the D-Ala-D-Ala/Van-type ligase superfamily: (1) an N-terminal lipoprotein signal peptide (GGNSPEY) characteristic of membrane-anchored Van ligases, (2) a glycine-rich loop region (GCGVAGSALCM) typical of the Ddl/VanA/VanB/VanC fold, and (3) a total length (~350 aa) consistent with this family rather than glutamine synthase (~450 aa, octameric, distinct fold). These features eliminate EC 6.3.5.1 (glutamine synthase, wrong family/size/fold). The absence of a Rossmann fold (GxGxxG) or NAD(P)-binding motifs eliminates EC 1.1.1.1 (oxidoreductase). The absence of catalytic aspartate/glutamate pairs and the overall fold eliminate EC 3.2.1.31 (beta-glucuronidase, a glycosidase). Since 6.3.2.35 is the only 6.3.2.x option, identifying the protein as a Van-type D-amino-acid ligase suffices to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Distinguishing 6.3.2.35 from other 6.3.2.x sub-numbers (e.g., 6.3.2.1 D-Ala-D-Ala ligase) would require active-site residue analysis, but no such competing option is presented.",
    "reason": "A knowledgeable reader can eliminate three of four options through structural/family-level sequence reasoning (signal peptide, glycine-rich loop, absence of oxidoreductase or glycosidase motifs). The remaining option is the correct answer. This requires specialized enzyme-family knowledge but is grounded in observable sequence features rather than pure database lookup."
  },
  "case_id": "EC_number_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q47720 (VanC2 from Enterococcus casseliflavus) is annotated as EC 6.3.2.35 with experimental evidence codes (ECO:0000269) from PubMed:9294159 (Park et al. 1997, PNAS) and PubMed:9545431 (Healy et al. 1998, Chem. Biol.). The catalytic reaction D-serine + D-alanine + ATP → D-alanyl-D-serine + ADP + phosphate + H(+) is experimentally characterized. Sequence match is exact (SHA256 confirmed)."
  },
  "important_caveats": [
    "The VanC2 entry was first released in Swiss-Prot in 2025 (firstPublicDate 2025-04-09); the historical entry version 147 is from 2026-01-28. The author's source snapshot is unknown, but the sequence and EC annotation have been stable since the 1997/1998 characterization papers.",
    "Recognizing the Ddl/Van ligase family from sequence requires familiarity with this well-studied antibiotic-resistance enzyme superfamily; this is specialized but standard biochemistry knowledge rather than obscure database lookup.",
    "The specific distinction between VanC2 (6.3.2.35, D-Ala-D-Ser) and VanA (6.3.2.-, D-Ala-D-Ala/D-Lac) ligases relies on active-site residues (Phe-250, Arg-322 per Healy 1998), but this level of discrimination is not needed here since no competing 6.3.2.x option is offered."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (1, 3, 6) and two different 6.3 subclasses (6.3.2 vs 6.3.5). The sequence features clearly point to the Ddl/Van ligase family, making C the only defensible choice. No other option is biologically plausible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q47720 (VanC2 from Enterococcus casseliflavus) is annotated as EC 6.3.2.35 with experimental evidence codes (ECO:0000269) from PubMed:9294159 (Park et al. 1997, PNAS) and PubMed:9545431 (Healy et al. 1998, Chem. Biol.). The catalytic reaction D-serine + D-alanine + ATP → D-alanyl-D-serine + ADP + phosphate + H(+) is experimentally characterized. Sequence match is exact (SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmarks of the D-Ala-D-Ala/Van-type ligase superfamily: (1) an N-terminal lipoprotein signal peptide (GGNSPEY) characteristic of membrane-anchored Van ligases, (2) a glycine-rich loop region (GCGVAGSALCM) typical of the Ddl/VanA/VanB/VanC fold, and (3) a total length (~350 aa) consistent with this family rather than glutamine synthase (~450 aa, octameric, distinct fold). These features eliminate EC 6.3.5.1 (glutamine synthase, wrong family/size/fold). The absence of a Rossmann fold (GxGxxG) or NAD(P)-binding motifs eliminates EC 1.1.1.1 (oxidoreductase). The absence of catalytic aspartate/glutamate pairs and the overall fold eliminate EC 3.2.1.31 (beta-glucuronidase, a glycosidase). Since 6.3.2.35 is the only 6.3.2.x option, identifying the protein as a Van-type D-amino-acid ligase suffices to select C.",
    "missing_item_specific_fact": "None critical. Distinguishing 6.3.2.35 from other 6.3.2.x sub-numbers (e.g., 6.3.2.1 D-Ala-D-Ala ligase) would require active-site residue analysis, but no such competing option is presented.",
    "reason": "A knowledgeable reader can eliminate three of four options through structural/family-level sequence reasoning (signal peptide, glycine-rich loop, absence of oxidoreductase or glycosidase motifs). The remaining option is the correct answer. This requires specialized enzyme-family knowledge but is grounded in observable sequence features rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (1, 3, 6) and two different 6.3 subclasses (6.3.2 vs 6.3.5). The sequence features clearly point to the Ddl/Van ligase family, making C the only defensible choice. No other option is biologically plausible for this sequence."
  },
  "important_caveats": [
    "The VanC2 entry was first released in Swiss-Prot in 2025 (firstPublicDate 2025-04-09); the historical entry version 147 is from 2026-01-28. The author's source snapshot is unknown, but the sequence and EC annotation have been stable since the 1997/1998 characterization papers.",
    "Recognizing the Ddl/Van ligase family from sequence requires familiarity with this well-studied antibiotic-resistance enzyme superfamily; this is specialized but standard biochemistry knowledge rather than obscure database lookup.",
    "The specific distinction between VanC2 (6.3.2.35, D-Ala-D-Ser) and VanA (6.3.2.-, D-Ala-D-Ala/D-Lac) ligases relies on active-site residues (Phe-250, Arg-322 per Healy 1998), but this level of discrimination is not needed here since no competing 6.3.2.x option is offered."
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

**Accession:** `Q47720` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 147. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
"Q47720"
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00047","source":"HAMAP-Rule"}],"value":"D-alanine--D-serine ligase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"VanC2 ligase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"9294159","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9545431","source":"PubMed"}],"value":"6.3.2.35"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"9294159","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Vancomycin C-type resistance protein VanC2"}}}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"6.3.2.35","evidences":[{"evidenceCode":"ECO:0000269","id":"9294159","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9545431","source":"PubMed"}],"name":"D-serine + D-alanine + ATP = D-alanyl-D-serine + ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:27706"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:35247"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57416"},{"database":"ChEBI","id":"CHEBI:60390"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"citation":{"authors":["Park I.S.","Lin C.H.","Walsh C.T."],"citationCrossReferences":[{"database":"PubMed","id":"9294159"},{"database":"DOI","id":"10.1073/pnas.94.19.10040"}],"citationType":"journal article","firstPage":"10040","id":"9294159","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"10044","publicationDate":"1997","title":"Bacterial resistance to vancomycin: overproduction, purification, and characterization of VanC2 from Enterococcus casseliflavus as a D-Ala-D-Ser ligase.","volume":"94"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"9294159","source":"PubMed"}],"type":"STRAIN","value":"ATCC 25788"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION","SUBUNIT"]}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"citation":{"authors":["Healy V.L.","Park I.S.","Walsh C.T."],"citationCrossReferences":[{"database":"PubMed","id":"9545431"},{"database":"DOI","id":"10.1016/s1074-5521(98)90633-0"}],"citationType":"journal article","firstPage":"197","id":"9545431","journal":"Chem. Biol.","lastPage":"207","publicationDate":"1998","title":"Active-site mutants of the VanC2 D-alanyl-D-serine ligase, characteristic of one vancomycin-resistant bacterial phenotype, revert towards wild-type D-alanyl-D-alanine ligases.","volume":"5"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF PHE-250 AND ARG-322"]}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:30:51.643943+00:00.  

```text
DE   RecName: Full=Vancomycin C-type resistance protein VanC2 {ECO:0000303|PubMed:9294159, ECO:0000305};
DE            EC=6.3.2.35 {ECO:0000269|PubMed:9294159, ECO:0000269|PubMed:9545431};
DE   AltName: Full=D-alanine--D-serine ligase {ECO:0000255|HAMAP-Rule:MF_00047};
DE   AltName: Full=VanC2 ligase {ECO:0000305};
```

Source SHA-256: `7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)  
**Locator:** `lines 42-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:30:51.643943+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, ACTIVITY
RP   REGULATION, AND SUBUNIT.
RC   STRAIN=ATCC 25788 {ECO:0000303|PubMed:9294159};
RX   PubMed=9294159; DOI=10.1073/pnas.94.19.10040;
RA   Park I.S., Lin C.H., Walsh C.T.;
RT   "Bacterial resistance to vancomycin: overproduction, purification, and
RT   characterization of VanC2 from Enterococcus casseliflavus as a D-Ala-D-Ser
RT   ligase.";
RL   Proc. Natl. Acad. Sci. U.S.A. 94:10040-10044(1997).
```

Source SHA-256: `7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)  
**Locator:** `lines 52-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:30:51.643943+00:00.  

```text
RN   [5] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND
RP   MUTAGENESIS OF PHE-250 AND ARG-322.
RX   PubMed=9545431; DOI=10.1016/s1074-5521(98)90633-0;
RA   Healy V.L., Park I.S., Walsh C.T.;
RT   "Active-site mutants of the VanC2 D-alanyl-D-serine ligase, characteristic
RT   of one vancomycin-resistant bacterial phenotype, revert towards wild-type
RT   D-alanyl-D-alanine ligases.";
RL   Chem. Biol. 5:197-207(1998).
```

Source SHA-256: `7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)  
**Locator:** `lines 70-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:30:51.643943+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=D-serine + D-alanine + ATP = D-alanyl-D-serine + ADP +
CC         phosphate + H(+); Xref=Rhea:RHEA:27706, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:30616, ChEBI:CHEBI:35247, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:57416, ChEBI:CHEBI:60390, ChEBI:CHEBI:456216;
CC         EC=6.3.2.35; Evidence={ECO:0000269|PubMed:9294159,
CC         ECO:0000269|PubMed:9545431};
```

Source SHA-256: `7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
