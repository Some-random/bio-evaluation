# EC_number_0010

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.6.1.5

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MALVRFATIITVLCHLAIQDGAAKSFPHGEKAPFPLTLIHINDLHARFDETNQKSSTCTNSKECIAGIARVYHTIKQLKSEYKTKNPLYLNAGDNFQGTLWYNLLRWNVTAYFIKELPPDAMTLGNHEFDHSPKGLAPYLAELEKMKIPTVVANLEKNGEPALKDSKIARSIVLKVGNRKVGVIGALYDKTHLVAQTGMVTLTNSIEAVRKEAQELKKKNVNIIVVLSHCGLDGDKQLAEEAGDLIDVIVGAHSHSLLLNKDAKVPYDTKYDTIEGDYPLVVKKSNNHTVLITQARSFGKYVGRLTVNFDCEGEVQSWEGYPIYMNNSVKQDEEVLRELEPWRAEVKRLGTQVIGTTEVFLDRESCRWCECTLGDLIADAYADQYTNSTVQPVAFVQAGNFRNPIEKGDITNGLAIEAAPYGSSVDMIKLSGADLWSAIDHSFTLDDEFRYNTAQVSGMAVVADLSKKPYERVQSIDIVGANGAKTALKKDQIYYVVVPSYLADGKDGFAMLKKGTNRVTGPLDSDVLIEYVRKRQTIAKTMFQEKRVVIENHTNGTCSWDLDSQRYKPK

[Multiple Choices]
A. 3.6.1.5
B. 3.4.21.62
C. 2.3.1.193
D. 1.5.1.32
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

> The exact sequence matches the UniProt entry annotated as apyrase, EC 3.6.1.5. Its catalytic-activity annotation assigns that EC number with experimental evidence linked to PubMed 39294191, supporting choice A for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a secreted enzyme, but that broad feature does not establish its specific catalytic reaction or distinguish EC 3.6.1.5 from the other listed enzyme activities.


**Missing item-specific fact**

> The sequence-specific functional identification and catalytic-activity evidence for this mosquito protein, which are not provided in the question.


**Reason**

> The exact EC assignment is supported by an external, experimentally evidenced annotation, not by a sufficiently discriminating argument available from the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched entry supports EC 3.6.1.5; the supplied evidence does not support another listed choice for this sequence.


### Important caveats

- The sequence match and annotation are reviewer-only evidence, not information supplied to the evaluated model.
- The UniProt catalytic-activity annotation cites experimental evidence, but the primary study was not independently retrieved and validated here.
- The author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a secreted enzyme, but that broad feature does not establish its specific catalytic reaction or distinguish EC 3.6.1.5 from the other listed enzyme activities.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific functional identification and catalytic-activity evidence for this mosquito protein, which are not provided in the question.",
    "reason": "The exact EC assignment is supported by an external, experimentally evidenced annotation, not by a sufficiently discriminating argument available from the sequence and choices alone."
  },
  "case_id": "EC_number_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as apyrase, EC 3.6.1.5. Its catalytic-activity annotation assigns that EC number with experimental evidence linked to PubMed 39294191, supporting choice A for this sequence."
  },
  "important_caveats": [
    "The sequence match and annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The UniProt catalytic-activity annotation cites experimental evidence, but the primary study was not independently retrieved and validated here.",
    "The author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry supports EC 3.6.1.5; the supplied evidence does not support another listed choice for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as apyrase, EC 3.6.1.5. Its catalytic-activity annotation assigns that EC number with experimental evidence linked to PubMed 39294191, supporting choice A for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a secreted enzyme, but that broad feature does not establish its specific catalytic reaction or distinguish EC 3.6.1.5 from the other listed enzyme activities.",
    "missing_item_specific_fact": "The sequence-specific functional identification and catalytic-activity evidence for this mosquito protein, which are not provided in the question.",
    "reason": "The exact EC assignment is supported by an external, experimentally evidenced annotation, not by a sufficiently discriminating argument available from the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched entry supports EC 3.6.1.5; the supplied evidence does not support another listed choice for this sequence."
  },
  "important_caveats": [
    "The sequence match and annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The UniProt catalytic-activity annotation cites experimental evidence, but the primary study was not independently retrieved and validated here.",
    "The author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q5TVM9 (APY_ANOGA, Anopheles gambiae apyrase). The EC 3.6.1.5 annotation carries evidence code ECO:0000269 (inferred from direct assay) from PubMed:39294191 (Nat Commun 2024), which experimentally characterized the catalytic activity (ribonucleoside 5'-triphosphate + 2 H2O → ribonucleoside 5'-phosphate + 2 Pi + 2 H+). The historical entry (version 120) also confirms EC=3.6.1.5. Sequence match is exact (SHA-256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four choices span four different EC classes (3.6 hydrolase acting on phosphorus-containing anhydrides; 3.4 peptidase; 2.3 acyltransferase; 1.5 oxidoreductase). From the sequence one can eliminate: (B) 3.4.21.62 Cathepsin G — no chymotrypsin-fold catalytic triad (His-Asp-Ser in GDSGG context) is present and the ~570-aa length is inconsistent with the ~250-aa chymotrypsin fold; (D) 1.5.1.32 dihydrofolate dehydrogenase — no Rossmann-fold GxGxxG nucleotide-binding motif and the length is roughly double that of typical DHFRs (~200 aa); (C) 2.3.1.193 acyltransferase — no acyl-CoA-binding or HAT/DAT motifs. Positive features supporting (A) 3.6.1.5 apyrase: an N-terminal hydrophobic signal peptide consistent with a secreted ecto-enzyme, a length (~570 aa) typical of NTPDase-family apyrases, and conserved NTPDase signature regions including 'GDNGAKT' and 'VGANGAKT' motifs found in the C-terminal half.


**Missing item-specific fact**

> None strictly required. Positive identification of NTPDase motifs requires somewhat specialized knowledge, but elimination of the three distractors (each from a different EC class with clearly absent diagnostic motifs/folds) is achievable with general enzymology knowledge.


**Reason**

> The distractors are drawn from four distinct EC classes and enzyme superfamilies, each with well-known structural/motif signatures that are visibly absent from this sequence. The remaining option (apyrase) is positively supported by the signal peptide, correct size range, and NTPDase-conserved motifs. A knowledgeable model can reach the answer through elimination plus partial motif recognition without needing to memorize this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices belong to different EC classes (1, 2, 3.4, 3.6) and enzyme families with distinct structural signatures. Only 3.6.1.5 is consistent with the observed sequence features (signal peptide, NTPDase motifs, length). No other option is defensible.


### Important caveats

- The EC 3.6.1.5 annotation was added to this entry relatively recently (PubMed:39294191, 2024) with experimental evidence (ECO:0000269). Before that, the protein was annotated as 'apyrase-like 1' with uncertain activity. The benchmark question is valid under the current annotation.
- Positive identification of NTPDase motifs (GDNGAKT, VGANGAKT) from raw sequence requires specialized knowledge of the NTPDase family; the elimination-based path is more robust for a general model.
- The identity of the protein as Q5TVM9 was inferred by the reviewer from dataset metadata, not provided to the evaluated model. The model must work from sequence alone.
- The 2024 Nat Commun paper (PubMed:39294191) provided direct experimental evidence for the apyrase catalytic activity, making the annotation experimentally grounded rather than purely computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices span four different EC classes (3.6 hydrolase acting on phosphorus-containing anhydrides; 3.4 peptidase; 2.3 acyltransferase; 1.5 oxidoreductase). From the sequence one can eliminate: (B) 3.4.21.62 Cathepsin G — no chymotrypsin-fold catalytic triad (His-Asp-Ser in GDSGG context) is present and the ~570-aa length is inconsistent with the ~250-aa chymotrypsin fold; (D) 1.5.1.32 dihydrofolate dehydrogenase — no Rossmann-fold GxGxxG nucleotide-binding motif and the length is roughly double that of typical DHFRs (~200 aa); (C) 2.3.1.193 acyltransferase — no acyl-CoA-binding or HAT/DAT motifs. Positive features supporting (A) 3.6.1.5 apyrase: an N-terminal hydrophobic signal peptide consistent with a secreted ecto-enzyme, a length (~570 aa) typical of NTPDase-family apyrases, and conserved NTPDase signature regions including 'GDNGAKT' and 'VGANGAKT' motifs found in the C-terminal half.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Positive identification of NTPDase motifs requires somewhat specialized knowledge, but elimination of the three distractors (each from a different EC class with clearly absent diagnostic motifs/folds) is achievable with general enzymology knowledge.",
    "reason": "The distractors are drawn from four distinct EC classes and enzyme superfamilies, each with well-known structural/motif signatures that are visibly absent from this sequence. The remaining option (apyrase) is positively supported by the signal peptide, correct size range, and NTPDase-conserved motifs. A knowledgeable model can reach the answer through elimination plus partial motif recognition without needing to memorize this specific UniProt entry."
  },
  "case_id": "EC_number_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5TVM9 (APY_ANOGA, Anopheles gambiae apyrase). The EC 3.6.1.5 annotation carries evidence code ECO:0000269 (inferred from direct assay) from PubMed:39294191 (Nat Commun 2024), which experimentally characterized the catalytic activity (ribonucleoside 5'-triphosphate + 2 H2O → ribonucleoside 5'-phosphate + 2 Pi + 2 H+). The historical entry (version 120) also confirms EC=3.6.1.5. Sequence match is exact (SHA-256 identical)."
  },
  "important_caveats": [
    "The EC 3.6.1.5 annotation was added to this entry relatively recently (PubMed:39294191, 2024) with experimental evidence (ECO:0000269). Before that, the protein was annotated as 'apyrase-like 1' with uncertain activity. The benchmark question is valid under the current annotation.",
    "Positive identification of NTPDase motifs (GDNGAKT, VGANGAKT) from raw sequence requires specialized knowledge of the NTPDase family; the elimination-based path is more robust for a general model.",
    "The identity of the protein as Q5TVM9 was inferred by the reviewer from dataset metadata, not provided to the evaluated model. The model must work from sequence alone.",
    "The 2024 Nat Commun paper (PubMed:39294191) provided direct experimental evidence for the apyrase catalytic activity, making the annotation experimentally grounded rather than purely computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices belong to different EC classes (1, 2, 3.4, 3.6) and enzyme families with distinct structural signatures. Only 3.6.1.5 is consistent with the observed sequence features (signal peptide, NTPDase motifs, length). No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5TVM9 (APY_ANOGA, Anopheles gambiae apyrase). The EC 3.6.1.5 annotation carries evidence code ECO:0000269 (inferred from direct assay) from PubMed:39294191 (Nat Commun 2024), which experimentally characterized the catalytic activity (ribonucleoside 5'-triphosphate + 2 H2O → ribonucleoside 5'-phosphate + 2 Pi + 2 H+). The historical entry (version 120) also confirms EC=3.6.1.5. Sequence match is exact (SHA-256 identical).",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four choices span four different EC classes (3.6 hydrolase acting on phosphorus-containing anhydrides; 3.4 peptidase; 2.3 acyltransferase; 1.5 oxidoreductase). From the sequence one can eliminate: (B) 3.4.21.62 Cathepsin G — no chymotrypsin-fold catalytic triad (His-Asp-Ser in GDSGG context) is present and the ~570-aa length is inconsistent with the ~250-aa chymotrypsin fold; (D) 1.5.1.32 dihydrofolate dehydrogenase — no Rossmann-fold GxGxxG nucleotide-binding motif and the length is roughly double that of typical DHFRs (~200 aa); (C) 2.3.1.193 acyltransferase — no acyl-CoA-binding or HAT/DAT motifs. Positive features supporting (A) 3.6.1.5 apyrase: an N-terminal hydrophobic signal peptide consistent with a secreted ecto-enzyme, a length (~570 aa) typical of NTPDase-family apyrases, and conserved NTPDase signature regions including 'GDNGAKT' and 'VGANGAKT' motifs found in the C-terminal half.",
    "missing_item_specific_fact": "None strictly required. Positive identification of NTPDase motifs requires somewhat specialized knowledge, but elimination of the three distractors (each from a different EC class with clearly absent diagnostic motifs/folds) is achievable with general enzymology knowledge.",
    "reason": "The distractors are drawn from four distinct EC classes and enzyme superfamilies, each with well-known structural/motif signatures that are visibly absent from this sequence. The remaining option (apyrase) is positively supported by the signal peptide, correct size range, and NTPDase-conserved motifs. A knowledgeable model can reach the answer through elimination plus partial motif recognition without needing to memorize this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices belong to different EC classes (1, 2, 3.4, 3.6) and enzyme families with distinct structural signatures. Only 3.6.1.5 is consistent with the observed sequence features (signal peptide, NTPDase motifs, length). No other option is defensible."
  },
  "important_caveats": [
    "The EC 3.6.1.5 annotation was added to this entry relatively recently (PubMed:39294191, 2024) with experimental evidence (ECO:0000269). Before that, the protein was annotated as 'apyrase-like 1' with uncertain activity. The benchmark question is valid under the current annotation.",
    "Positive identification of NTPDase motifs (GDNGAKT, VGANGAKT) from raw sequence requires specialized knowledge of the NTPDase family; the elimination-based path is more robust for a general model.",
    "The identity of the protein as Q5TVM9 was inferred by the reviewer from dataset metadata, not provided to the evaluated model. The model must work from sequence alone.",
    "The 2024 Nat Commun paper (PubMed:39294191) provided direct experimental evidence for the apyrase catalytic activity, making the annotation experimentally grounded rather than purely computational."
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

**Accession:** `Q5TVM9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 120. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
"Q5TVM9"
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39294191","source":"PubMed"}],"value":"5' nucleotidase ecto"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39294191","source":"PubMed"}],"value":"Ag5'NTE"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10801886","source":"PubMed"}],"value":"Apyrase-like 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10801886","source":"PubMed"}],"value":"AgApyL1"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39294191","source":"PubMed"}],"value":"3.6.1.5"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39294191","source":"PubMed"}],"value":"Apyrase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39294191","source":"PubMed"}],"value":"AgApy"}]}}
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.6.1.5","evidences":[{"evidenceCode":"ECO:0000269","id":"39294191","source":"PubMed"}],"name":"a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside 5'-phosphate + 2 phosphate + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:36795"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:58043"},{"database":"ChEBI","id":"CHEBI:61557"}]}}
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
{"citation":{"authors":["Pala Z.R.","Alves E Silva T.L.","Minai M.","Crews B.","Patino-Martinez E.","Carmona-Rivera C.","Valenzuela Leon P.C.","Martin-Martin I.","Flores-Garcia Y.","Cachau R.E.","Muslinkina L.","Gittis A.G.","Srivastava N.","Garboczi D.N.","Alves D.A.","Kaplan M.J.","Fischer E.","Calvo E.","Vega-Rodriguez J."],"citationCrossReferences":[{"database":"PubMed","id":"39294191"},{"database":"DOI","id":"10.1038/s41467-024-52502-3"}],"citationType":"journal article","firstPage":"8194","id":"39294191","journal":"Nat. Commun.","lastPage":"8194","publicationDate":"2024","title":"Mosquito salivary apyrase regulates blood meal hemostasis and facilitates malaria parasite transmission.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["IDENTIFICATION BY MASS SPECTROMETRY","FUNCTION","FUNCTION (MICROBIAL INFECTION)","CATALYTIC ACTIVITY","COFACTOR","INTERACTION WITH HUMAN PLAT","SUBCELLULAR LOCATION","TISSUE SPECIFICITY"]}
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)  
**Locator:** `lines 6-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-01T06:28:38.028811+00:00.  

```text
DE   RecName: Full=Apyrase {ECO:0000303|PubMed:39294191};
DE            Short=AgApy {ECO:0000303|PubMed:39294191};
DE            EC=3.6.1.5 {ECO:0000269|PubMed:39294191};
DE   AltName: Full=5' nucleotidase ecto {ECO:0000303|PubMed:39294191};
DE            Short=Ag5'NTE {ECO:0000303|PubMed:39294191};
DE   AltName: Full=Apyrase-like 1 {ECO:0000303|PubMed:10801886};
DE            Short=AgApyL1 {ECO:0000303|PubMed:10801886};
DE   Flags: Precursor;
```

Source SHA-256: `dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)  
**Locator:** `lines 73-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-01T06:28:38.028811+00:00.  

```text
RN   [5] {ECO:0000305}
RP   IDENTIFICATION BY MASS SPECTROMETRY, FUNCTION, FUNCTION (MICROBIAL
RP   INFECTION), CATALYTIC ACTIVITY, COFACTOR, INTERACTION WITH HUMAN PLAT,
RP   SUBCELLULAR LOCATION, AND TISSUE SPECIFICITY.
RX   PubMed=39294191; DOI=10.1038/s41467-024-52502-3;
RA   Pala Z.R., Alves E Silva T.L., Minai M., Crews B., Patino-Martinez E.,
RA   Carmona-Rivera C., Valenzuela Leon P.C., Martin-Martin I.,
RA   Flores-Garcia Y., Cachau R.E., Muslinkina L., Gittis A.G., Srivastava N.,
RA   Garboczi D.N., Alves D.A., Kaplan M.J., Fischer E., Calvo E.,
RA   Vega-Rodriguez J.;
RT   "Mosquito salivary apyrase regulates blood meal hemostasis and facilitates
RT   malaria parasite transmission.";
RL   Nat. Commun. 15:8194-8194(2024).
```

Source SHA-256: `dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)  
**Locator:** `lines 102-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-01T06:28:38.028811+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a ribonucleoside 5'-triphosphate + 2 H2O = a ribonucleoside
CC         5'-phosphate + 2 phosphate + 2 H(+); Xref=Rhea:RHEA:36795,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:58043, ChEBI:CHEBI:61557; EC=3.6.1.5;
CC         Evidence={ECO:0000269|PubMed:39294191};
```

Source SHA-256: `dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
