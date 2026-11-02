# EC_number_0139

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.1.1.4

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKVLQMFFCVILLCVTSVLVEAKSTTKGDETASKRNFAQFAAMTYHTTHRWPKKYVGYGCYCGLGGYGIPVDPIDECCKTHDACYKKVEDSGICSYSWAIYLTIYKRKGGAECSEDNEKCQMEVCKCDSVAAKCLGKYKDIFNEKYAGYDKKGKCDPSFTLS

[Multiple Choices]
A. 3.1.1.80
B. 3.1.1.4
C. 1.2.1.46
D. 1.97.1.13
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

> The exact sequence matches the UniProt entry annotated as phospholipase A2 with EC 3.1.1.4, and its catalytic reaction is assigned that EC number. The EC assignment is supported by a PROSITE-ProRule computational annotation, not by the cited excerpts establishing a direct activity experiment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal peptide followed by a short, cysteine-rich secreted-protein region with a phospholipase-A2-like catalytic motif. This provides a defensible family-level basis for selecting the PLA2 EC option over the listed oxidoreductase and other hydrolase choices.


**Missing item-specific fact**

> No particular external fact is necessary to distinguish these choices by family-level inference; direct experimental confirmation of the precise catalytic activity is not supplied.


**Reason**

> The sequence features and the widely distinct candidate enzyme classes provide meaningful grounds for choosing EC 3.1.1.4, although the sequence alone is not a substitute for an activity assay.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the sequence’s secreted, cysteine-rich PLA2-like features favor 3.1.1.4; the other options correspond to different enzyme classes.


### Important caveats

- The sequence match is exact, but the UniProt EC annotation is attributed to PROSITE-ProRule and should be distinguished from experimental demonstration of catalysis.
- The cited publications support sequence identification and naming context in the excerpts; they do not, in the supplied evidence, independently establish the catalytic reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide followed by a short, cysteine-rich secreted-protein region with a phospholipase-A2-like catalytic motif. This provides a defensible family-level basis for selecting the PLA2 EC option over the listed oxidoreductase and other hydrolase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No particular external fact is necessary to distinguish these choices by family-level inference; direct experimental confirmation of the precise catalytic activity is not supplied.",
    "reason": "The sequence features and the widely distinct candidate enzyme classes provide meaningful grounds for choosing EC 3.1.1.4, although the sequence alone is not a substitute for an activity assay."
  },
  "case_id": "EC_number_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as phospholipase A2 with EC 3.1.1.4, and its catalytic reaction is assigned that EC number. The EC assignment is supported by a PROSITE-ProRule computational annotation, not by the cited excerpts establishing a direct activity experiment."
  },
  "important_caveats": [
    "The sequence match is exact, but the UniProt EC annotation is attributed to PROSITE-ProRule and should be distinguished from experimental demonstration of catalysis.",
    "The cited publications support sequence identification and naming context in the excerpts; they do not, in the supplied evidence, independently establish the catalytic reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence’s secreted, cysteine-rich PLA2-like features favor 3.1.1.4; the other options correspond to different enzyme classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as phospholipase A2 with EC 3.1.1.4, and its catalytic reaction is assigned that EC number. The EC assignment is supported by a PROSITE-ProRule computational annotation, not by the cited excerpts establishing a direct activity experiment.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal peptide followed by a short, cysteine-rich secreted-protein region with a phospholipase-A2-like catalytic motif. This provides a defensible family-level basis for selecting the PLA2 EC option over the listed oxidoreductase and other hydrolase choices.",
    "missing_item_specific_fact": "No particular external fact is necessary to distinguish these choices by family-level inference; direct experimental confirmation of the precise catalytic activity is not supplied.",
    "reason": "The sequence features and the widely distinct candidate enzyme classes provide meaningful grounds for choosing EC 3.1.1.4, although the sequence alone is not a substitute for an activity assay."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence’s secreted, cysteine-rich PLA2-like features favor 3.1.1.4; the other options correspond to different enzyme classes."
  },
  "important_caveats": [
    "The sequence match is exact, but the UniProt EC annotation is attributed to PROSITE-ProRule and should be distinguished from experimental demonstration of catalysis.",
    "The cited publications support sequence identification and naming context in the excerpts; they do not, in the supplied evidence, independently establish the catalytic reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DY42 (PLA2_CALPY) from Calliactis polypus is annotated with EC 3.1.1.4 (Phospholipase A2), with the sequence exactly matching the benchmark input (162 aa, SHA-256 confirmed). The EC assignment is supported by PROSITE-ProRule:PRU10035 (computational pattern match to the sPLA2 signature) and the protein name 'Phospholipase A2' is supported by mass spectrometry identification (PubMed 36977109, 39018436). The annotation is primarily computational (PROSITE-ProRule evidence code ECO:0000255), but the protein's identity as a PLA2 is corroborated by experimental mass-spec identification and sequence homology to known sPLA2 enzymes.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark 'GWCYCGLGGYGIP' motif (residues ~65-78), which is the canonical calcium-binding loop and catalytic-site signature of secreted phospholipase A2 (sPLA2) enzymes. This motif, together with the signal peptide (N-terminal hydrophobic stretch), the multiple conserved cysteines forming disulfide bonds, and the ~130-160 aa mature length, identifies the protein as a member of the sPLA2 superfamily. The oxidoreductase options (1.2.1.46, 1.97.1.13) are eliminated because the sequence lacks FAD/NAD-binding Rossmann motifs, heme-binding Cys-His pairs, or any cofactor-recognition architecture. The PLA1 option (3.1.1.80) is distinguished because PLA1 enzymes (e.g., phosphatidylcholine 1-acylhydrolase) use a serine-hydrolase catalytic mechanism with a GXSXG motif and lack the calcium-binding loop and the specific CGYCG/GWCYCGLGGYGIP arrangement diagnostic of PLA2. Thus, general knowledge of enzyme-family structural motifs allows meaningful discrimination among the four choices.


**Missing item-specific fact**

> None critical. The PLA2-specific motif is a well-established biochemical signature identifiable from the sequence. One could argue that confirming the exact EC number (vs. a novel PLA2 variant with altered specificity) would require an enzymatic assay, but the question asks for classification, and the sPLA2 motif is sufficient for EC 3.1.1.4 assignment.


**Reason**

> A knowledgeable biochemist can identify the sPLA2 calcium-binding loop motif 'GWCYCGLGGYGIP' in the sequence, recognize the secreted cysteine-rich architecture, rule out oxidoreductases by absence of cofactor motifs, and distinguish PLA2 from PLA1 by the specific catalytic-site and calcium-loop arrangement. This constitutes a concrete biological argument from the sequence itself rather than a database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PLA2-specific motif clearly points to 3.1.1.4 over 3.1.1.80 (PLA1, different catalytic mechanism and no calcium-binding loop). The oxidoreductase choices (1.2.1.46, 1.97.1.13) are incompatible with the secreted cysteine-rich hydrolase architecture. No other option is defensible given the sequence features.


### Important caveats

- The EC 3.1.1.4 assignment in UniProt is based on PROSITE-ProRule (ECO:0000255), i.e., pattern/similarity-based inference, not a direct enzymatic activity assay on this specific protein.
- The protein was identified by mass spectrometry and sequence analysis (PubMed 36977109, 39018436), but no in vitro kinetic characterization of this particular anemone PLA2 variant is cited in the UniProt entry.
- The reviewer-only UniProt accession (P0DY42) and metadata were absent from the evaluated model input; the model must rely solely on the sequence and general knowledge.
- The sequence is a precursor (162 aa including signal peptide); the mature enzyme is ~130-140 aa, consistent with sPLA2.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark 'GWCYCGLGGYGIP' motif (residues ~65-78), which is the canonical calcium-binding loop and catalytic-site signature of secreted phospholipase A2 (sPLA2) enzymes. This motif, together with the signal peptide (N-terminal hydrophobic stretch), the multiple conserved cysteines forming disulfide bonds, and the ~130-160 aa mature length, identifies the protein as a member of the sPLA2 superfamily. The oxidoreductase options (1.2.1.46, 1.97.1.13) are eliminated because the sequence lacks FAD/NAD-binding Rossmann motifs, heme-binding Cys-His pairs, or any cofactor-recognition architecture. The PLA1 option (3.1.1.80) is distinguished because PLA1 enzymes (e.g., phosphatidylcholine 1-acylhydrolase) use a serine-hydrolase catalytic mechanism with a GXSXG motif and lack the calcium-binding loop and the specific CGYCG/GWCYCGLGGYGIP arrangement diagnostic of PLA2. Thus, general knowledge of enzyme-family structural motifs allows meaningful discrimination among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PLA2-specific motif is a well-established biochemical signature identifiable from the sequence. One could argue that confirming the exact EC number (vs. a novel PLA2 variant with altered specificity) would require an enzymatic assay, but the question asks for classification, and the sPLA2 motif is sufficient for EC 3.1.1.4 assignment.",
    "reason": "A knowledgeable biochemist can identify the sPLA2 calcium-binding loop motif 'GWCYCGLGGYGIP' in the sequence, recognize the secreted cysteine-rich architecture, rule out oxidoreductases by absence of cofactor motifs, and distinguish PLA2 from PLA1 by the specific catalytic-site and calcium-loop arrangement. This constitutes a concrete biological argument from the sequence itself rather than a database lookup."
  },
  "case_id": "EC_number_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DY42 (PLA2_CALPY) from Calliactis polypus is annotated with EC 3.1.1.4 (Phospholipase A2), with the sequence exactly matching the benchmark input (162 aa, SHA-256 confirmed). The EC assignment is supported by PROSITE-ProRule:PRU10035 (computational pattern match to the sPLA2 signature) and the protein name 'Phospholipase A2' is supported by mass spectrometry identification (PubMed 36977109, 39018436). The annotation is primarily computational (PROSITE-ProRule evidence code ECO:0000255), but the protein's identity as a PLA2 is corroborated by experimental mass-spec identification and sequence homology to known sPLA2 enzymes."
  },
  "important_caveats": [
    "The EC 3.1.1.4 assignment in UniProt is based on PROSITE-ProRule (ECO:0000255), i.e., pattern/similarity-based inference, not a direct enzymatic activity assay on this specific protein.",
    "The protein was identified by mass spectrometry and sequence analysis (PubMed 36977109, 39018436), but no in vitro kinetic characterization of this particular anemone PLA2 variant is cited in the UniProt entry.",
    "The reviewer-only UniProt accession (P0DY42) and metadata were absent from the evaluated model input; the model must rely solely on the sequence and general knowledge.",
    "The sequence is a precursor (162 aa including signal peptide); the mature enzyme is ~130-140 aa, consistent with sPLA2."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PLA2-specific motif clearly points to 3.1.1.4 over 3.1.1.80 (PLA1, different catalytic mechanism and no calcium-binding loop). The oxidoreductase choices (1.2.1.46, 1.97.1.13) are incompatible with the secreted cysteine-rich hydrolase architecture. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DY42 (PLA2_CALPY) from Calliactis polypus is annotated with EC 3.1.1.4 (Phospholipase A2), with the sequence exactly matching the benchmark input (162 aa, SHA-256 confirmed). The EC assignment is supported by PROSITE-ProRule:PRU10035 (computational pattern match to the sPLA2 signature) and the protein name 'Phospholipase A2' is supported by mass spectrometry identification (PubMed 36977109, 39018436). The annotation is primarily computational (PROSITE-ProRule evidence code ECO:0000255), but the protein's identity as a PLA2 is corroborated by experimental mass-spec identification and sequence homology to known sPLA2 enzymes.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark 'GWCYCGLGGYGIP' motif (residues ~65-78), which is the canonical calcium-binding loop and catalytic-site signature of secreted phospholipase A2 (sPLA2) enzymes. This motif, together with the signal peptide (N-terminal hydrophobic stretch), the multiple conserved cysteines forming disulfide bonds, and the ~130-160 aa mature length, identifies the protein as a member of the sPLA2 superfamily. The oxidoreductase options (1.2.1.46, 1.97.1.13) are eliminated because the sequence lacks FAD/NAD-binding Rossmann motifs, heme-binding Cys-His pairs, or any cofactor-recognition architecture. The PLA1 option (3.1.1.80) is distinguished because PLA1 enzymes (e.g., phosphatidylcholine 1-acylhydrolase) use a serine-hydrolase catalytic mechanism with a GXSXG motif and lack the calcium-binding loop and the specific CGYCG/GWCYCGLGGYGIP arrangement diagnostic of PLA2. Thus, general knowledge of enzyme-family structural motifs allows meaningful discrimination among the four choices.",
    "missing_item_specific_fact": "None critical. The PLA2-specific motif is a well-established biochemical signature identifiable from the sequence. One could argue that confirming the exact EC number (vs. a novel PLA2 variant with altered specificity) would require an enzymatic assay, but the question asks for classification, and the sPLA2 motif is sufficient for EC 3.1.1.4 assignment.",
    "reason": "A knowledgeable biochemist can identify the sPLA2 calcium-binding loop motif 'GWCYCGLGGYGIP' in the sequence, recognize the secreted cysteine-rich architecture, rule out oxidoreductases by absence of cofactor motifs, and distinguish PLA2 from PLA1 by the specific catalytic-site and calcium-loop arrangement. This constitutes a concrete biological argument from the sequence itself rather than a database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PLA2-specific motif clearly points to 3.1.1.4 over 3.1.1.80 (PLA1, different catalytic mechanism and no calcium-binding loop). The oxidoreductase choices (1.2.1.46, 1.97.1.13) are incompatible with the secreted cysteine-rich hydrolase architecture. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The EC 3.1.1.4 assignment in UniProt is based on PROSITE-ProRule (ECO:0000255), i.e., pattern/similarity-based inference, not a direct enzymatic activity assay on this specific protein.",
    "The protein was identified by mass spectrometry and sequence analysis (PubMed 36977109, 39018436), but no in vitro kinetic characterization of this particular anemone PLA2 variant is cited in the UniProt entry.",
    "The reviewer-only UniProt accession (P0DY42) and metadata were absent from the evaluated model input; the model must rely solely on the sequence and general knowledge.",
    "The sequence is a precursor (162 aa including signal peptide); the mature enzyme is ~130-140 aa, consistent with sPLA2."
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

**Accession:** `P0DY42` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY42.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:08.181789+00:00.  

```json
"P0DY42"
```

Source SHA-256: `7c75de950f0fdf913641db8f4a8d9299a670f5c3bddde189822ce1370ac12348`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY42.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:08.181789+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Phosphatidylcholine 2-acylhydrolase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39018436","source":"PubMed"}],"value":"Phospholipase A2 Cpp1a"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39018436","source":"PubMed"}],"value":"PLA2-Cpp1a"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10035","source":"PROSITE-ProRule"}],"value":"3.1.1.4"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36977109","source":"PubMed"}],"value":"Phospholipase A2"},"shortNames":[{"value":"PLA2"}]}}
```

Source SHA-256: `7c75de950f0fdf913641db8f4a8d9299a670f5c3bddde189822ce1370ac12348`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY42.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:08.181789+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.1.1.4","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10035","source":"PROSITE-ProRule"}],"name":"a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15801"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:28868"},{"database":"ChEBI","id":"CHEBI:57643"},{"database":"ChEBI","id":"CHEBI:58168"}]}}
```

Source SHA-256: `7c75de950f0fdf913641db8f4a8d9299a670f5c3bddde189822ce1370ac12348`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY42?format=txt&versions=3)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:12.224282+00:00.  

```text
ID   PLA2_CALPY              Reviewed;         162 AA.
AC   P0DY42;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=Phospholipase A2 {ECO:0000303|PubMed:36977109};
DE            Short=PLA2;
DE            EC=3.1.1.4 {ECO:0000255|PROSITE-ProRule:PRU10035};
DE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;
DE   AltName: Full=Phospholipase A2 Cpp1a {ECO:0000303|PubMed:39018436};
DE            Short=PLA2-Cpp1a {ECO:0000303|PubMed:39018436};
DE   Flags: Precursor;
GN   ORFNames=c56806_g1_i1 {ECO:0000303|PubMed:36977109,
GN   ECO:0000303|PubMed:39018436};
OS   Calliactis polypus (Hermit crab anemone) (Priapus polypus).
OC   Eukaryota; Metazoa; Cnidaria; Anthozoa; Hexacorallia; Actiniaria;
OC   Nynantheae; Hormathiidae; Calliactis.
OX   NCBI_TaxID=656064;
```

Source SHA-256: `dd00dd8be405e70fb669825538e585e62a6604c98be8a7ee96e819b8ecce813e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY42?format=txt&versions=3)  
**Locator:** `lines 6-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:12.224282+00:00.  

```text
DE   RecName: Full=Phospholipase A2 {ECO:0000303|PubMed:36977109};
DE            Short=PLA2;
DE            EC=3.1.1.4 {ECO:0000255|PROSITE-ProRule:PRU10035};
DE   AltName: Full=Phosphatidylcholine 2-acylhydrolase;
DE   AltName: Full=Phospholipase A2 Cpp1a {ECO:0000303|PubMed:39018436};
DE            Short=PLA2-Cpp1a {ECO:0000303|PubMed:39018436};
DE   Flags: Precursor;
```

Source SHA-256: `dd00dd8be405e70fb669825538e585e62a6604c98be8a7ee96e819b8ecce813e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY42?format=txt&versions=3)  
**Locator:** `lines 37-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:12.224282+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-
CC         glycero-3-phosphocholine + a fatty acid + H(+); Xref=Rhea:RHEA:15801,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:28868,
CC         ChEBI:CHEBI:57643, ChEBI:CHEBI:58168; EC=3.1.1.4;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10035};
```

Source SHA-256: `dd00dd8be405e70fb669825538e585e62a6604c98be8a7ee96e819b8ecce813e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 139. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
