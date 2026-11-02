# catalytic_activity_0082

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — Endohydrolysis of (1-&gt;4)-beta-D-xylosidic linkages in xylans.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSIALALAAAPAVLAQSQLWGQCGGIGWNGPTTCVSGATCTKINDWYHQCLPGGNNNNPPPATTSQWTPPPAQTSSNPPPNNGGGGGNTLHEKFKARGKQYFGTEIDHYHLNNNQLMEIARREFGQITHENSMKWDATEPSRGSFSFGNADRVVDWATSNGKLIRGHTLLWHSQLPQWVQNINDRNTLTQVIENHVKTIMTRYKGKIFHYDVVNEILDENGGLRNSVFSRVLGEDFVGIAFRAARATDPDAKLYINDYNLDSANYAKTRGMINLVNKWVSQGVPIDGIGTQAHLAGPGGWNPASGVPAALQALAGANVKEVAITELDIQGAGANDYVTVANACLNVQKCVGITVWGVSDRDSWRSNENPLLYDGSYRPKAAYNALMNAL

[Multiple Choices]
A. cytidine(in) = cytidine(out)
B. tetrahydroalstonine + A + reduced [NADPH--hemoprotein reductase] + O2 = alstonine + AH2 + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
C. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
D. FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-dione + FMNH2 + AMP + diphosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt sequence annotated as endo-1,4-beta-xylanase C, and the matched record assigns the stated reaction with experimental evidence linked to PubMed 23306124.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal signal peptide and lack of multiple transmembrane segments favor a secreted soluble enzyme, making a transporter or intracellular enzyme less plausible. These features do not establish xylan as the substrate or identify the precise reaction.


**Missing item-specific fact**

> The sequence-specific identification as an endo-1,4-beta-xylanase, or equivalent evidence of its substrate specificity and catalytic activity.


**Reason**

> The supplied sequence gives broad clues about secretion and protein type, but distinguishing xylan hydrolysis from other possible extracellular enzyme activities requires protein-specific family or activity information not stated in the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only matched-sequence annotation supports C; none of the other listed reactions is supported by the supplied evidence.


### Important caveats

- The UniProt catalytic-activity annotation cites experimental evidence, but the primary paper was not independently retrieved and validated here.
- The historical sequence match is established, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal signal peptide and lack of multiple transmembrane segments favor a secreted soluble enzyme, making a transporter or intracellular enzyme less plausible. These features do not establish xylan as the substrate or identify the precise reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific identification as an endo-1,4-beta-xylanase, or equivalent evidence of its substrate specificity and catalytic activity.",
    "reason": "The supplied sequence gives broad clues about secretion and protein type, but distinguishing xylan hydrolysis from other possible extracellular enzyme activities requires protein-specific family or activity information not stated in the input."
  },
  "case_id": "catalytic_activity_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as endo-1,4-beta-xylanase C, and the matched record assigns the stated reaction with experimental evidence linked to PubMed 23306124."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation cites experimental evidence, but the primary paper was not independently retrieved and validated here.",
    "The historical sequence match is established, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports C; none of the other listed reactions is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as endo-1,4-beta-xylanase C, and the matched record assigns the stated reaction with experimental evidence linked to PubMed 23306124.",
    "evidence_ids": ["C4", "C5", "C6", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal signal peptide and lack of multiple transmembrane segments favor a secreted soluble enzyme, making a transporter or intracellular enzyme less plausible. These features do not establish xylan as the substrate or identify the precise reaction.",
    "missing_item_specific_fact": "The sequence-specific identification as an endo-1,4-beta-xylanase, or equivalent evidence of its substrate specificity and catalytic activity.",
    "reason": "The supplied sequence gives broad clues about secretion and protein type, but distinguishing xylan hydrolysis from other possible extracellular enzyme activities requires protein-specific family or activity information not stated in the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports C; none of the other listed reactions is supported by the supplied evidence."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation cites experimental evidence, but the primary paper was not independently retrieved and validated here.",
    "The historical sequence match is established, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry M4MEY9 (XYNC_HUMIN) exactly (390 AA, SHA256 confirmed). The entry is annotated as Endo-1,4-beta-xylanase C (EC 3.2.1.8) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' supported by experimental evidence (ECO:0000269, PubMed:23306124, a 2013 Bioresour. Technol. paper characterizing three thermophilic xylanases from Humicola insolens Y1). The expected answer text matches the UniProt CATALYTIC ACTIVITY comment verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence provides several identifiable features: (1) An N-terminal signal peptide (MRSIALALAAAPAVLAQSQLWGQ...) indicating a secreted enzyme, which eliminates choice A (a membrane nucleoside transporter requiring transmembrane helices absent here). (2) No heme-binding Cys-rich motifs or P450 signature sequences, eliminating choice B (a monooxygenase requiring a heme prosthetic group). (3) No FMN-binding motifs (e.g., the Rossmann-like GXGXXG or the FMN-specific 'NXXG' motifs), eliminating choice D (a flavin-dependent enzyme). (4) The mature protein (~340 AA after signal peptide cleavage) contains the GH11-family catalytic glutamate motifs 'EIDHYHL' (first catalytic Glu) and 'EILDENGG' (second catalytic Glu), which are well-documented signatures of endo-1,4-beta-xylanases (EC 3.2.1.8). The overall β-jelly-roll-like architecture and fungal secretion context further support a glycoside hydrolase, specifically a xylanase. Among the four choices, C is the only glycoside hydrolase reaction, and the catalytic motifs are consistent with the GH11 subfamily.


**Missing item-specific fact**

> None strictly required. Full confidence in the GH11 assignment benefits from knowledge of the EIDHY/EILD catalytic motifs, but the elimination of A, B, and D by absence of their obligatory structural features (TM helices, heme-binding Cys, FMN-binding motifs) combined with identification as a secreted glycoside hydrolase of appropriate size provides a defensible reasoning path to C.


**Reason**

> The question is answerable by systematic elimination of non-transporter, non-P450, non-flavoenzyme options based on absent structural motifs, combined with recognition of GH11 catalytic glutamate motifs in the sequence. This constitutes a concrete biological argument from the supplied sequence rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent entirely different enzyme classes (nucleoside transporter, P450 monooxygenase, glycoside hydrolase, flavoenzyme). The sequence's features unambiguously align with a glycoside hydrolase and specifically with GH11 xylanase motifs. No other choice is defensible given the absence of their required cofactor-binding or membrane-spanning features.


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269) from a 2013 paper, not merely computational inference, strengthening the key.
- The sequence match is exact (SHA256 confirmed) in both current (v43) and historical (v41) records.
- The GH11 catalytic motif recognition (EIDHY, EILD) requires specialized glycoside hydrolase knowledge but is within the scope of general enzymology training.
- The entry was first public in Feb 2025; the underlying sequence was deposited in 2013. The author's source snapshot date is unknown but the sequence has been stable since version 1.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence provides several identifiable features: (1) An N-terminal signal peptide (MRSIALALAAAPAVLAQSQLWGQ...) indicating a secreted enzyme, which eliminates choice A (a membrane nucleoside transporter requiring transmembrane helices absent here). (2) No heme-binding Cys-rich motifs or P450 signature sequences, eliminating choice B (a monooxygenase requiring a heme prosthetic group). (3) No FMN-binding motifs (e.g., the Rossmann-like GXGXXG or the FMN-specific 'NXXG' motifs), eliminating choice D (a flavin-dependent enzyme). (4) The mature protein (~340 AA after signal peptide cleavage) contains the GH11-family catalytic glutamate motifs 'EIDHYHL' (first catalytic Glu) and 'EILDENGG' (second catalytic Glu), which are well-documented signatures of endo-1,4-beta-xylanases (EC 3.2.1.8). The overall β-jelly-roll-like architecture and fungal secretion context further support a glycoside hydrolase, specifically a xylanase. Among the four choices, C is the only glycoside hydrolase reaction, and the catalytic motifs are consistent with the GH11 subfamily.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Full confidence in the GH11 assignment benefits from knowledge of the EIDHY/EILD catalytic motifs, but the elimination of A, B, and D by absence of their obligatory structural features (TM helices, heme-binding Cys, FMN-binding motifs) combined with identification as a secreted glycoside hydrolase of appropriate size provides a defensible reasoning path to C.",
    "reason": "The question is answerable by systematic elimination of non-transporter, non-P450, non-flavoenzyme options based on absent structural motifs, combined with recognition of GH11 catalytic glutamate motifs in the sequence. This constitutes a concrete biological argument from the supplied sequence rather than pure database lookup."
  },
  "case_id": "catalytic_activity_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry M4MEY9 (XYNC_HUMIN) exactly (390 AA, SHA256 confirmed). The entry is annotated as Endo-1,4-beta-xylanase C (EC 3.2.1.8) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' supported by experimental evidence (ECO:0000269, PubMed:23306124, a 2013 Bioresour. Technol. paper characterizing three thermophilic xylanases from Humicola insolens Y1). The expected answer text matches the UniProt CATALYTIC ACTIVITY comment verbatim."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2013 paper, not merely computational inference, strengthening the key.",
    "The sequence match is exact (SHA256 confirmed) in both current (v43) and historical (v41) records.",
    "The GH11 catalytic motif recognition (EIDHY, EILD) requires specialized glycoside hydrolase knowledge but is within the scope of general enzymology training.",
    "The entry was first public in Feb 2025; the underlying sequence was deposited in 2013. The author's source snapshot date is unknown but the sequence has been stable since version 1."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent entirely different enzyme classes (nucleoside transporter, P450 monooxygenase, glycoside hydrolase, flavoenzyme). The sequence's features unambiguously align with a glycoside hydrolase and specifically with GH11 xylanase motifs. No other choice is defensible given the absence of their required cofactor-binding or membrane-spanning features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry M4MEY9 (XYNC_HUMIN) exactly (390 AA, SHA256 confirmed). The entry is annotated as Endo-1,4-beta-xylanase C (EC 3.2.1.8) with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans' supported by experimental evidence (ECO:0000269, PubMed:23306124, a 2013 Bioresour. Technol. paper characterizing three thermophilic xylanases from Humicola insolens Y1). The expected answer text matches the UniProt CATALYTIC ACTIVITY comment verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence provides several identifiable features: (1) An N-terminal signal peptide (MRSIALALAAAPAVLAQSQLWGQ...) indicating a secreted enzyme, which eliminates choice A (a membrane nucleoside transporter requiring transmembrane helices absent here). (2) No heme-binding Cys-rich motifs or P450 signature sequences, eliminating choice B (a monooxygenase requiring a heme prosthetic group). (3) No FMN-binding motifs (e.g., the Rossmann-like GXGXXG or the FMN-specific 'NXXG' motifs), eliminating choice D (a flavin-dependent enzyme). (4) The mature protein (~340 AA after signal peptide cleavage) contains the GH11-family catalytic glutamate motifs 'EIDHYHL' (first catalytic Glu) and 'EILDENGG' (second catalytic Glu), which are well-documented signatures of endo-1,4-beta-xylanases (EC 3.2.1.8). The overall β-jelly-roll-like architecture and fungal secretion context further support a glycoside hydrolase, specifically a xylanase. Among the four choices, C is the only glycoside hydrolase reaction, and the catalytic motifs are consistent with the GH11 subfamily.",
    "missing_item_specific_fact": "None strictly required. Full confidence in the GH11 assignment benefits from knowledge of the EIDHY/EILD catalytic motifs, but the elimination of A, B, and D by absence of their obligatory structural features (TM helices, heme-binding Cys, FMN-binding motifs) combined with identification as a secreted glycoside hydrolase of appropriate size provides a defensible reasoning path to C.",
    "reason": "The question is answerable by systematic elimination of non-transporter, non-P450, non-flavoenzyme options based on absent structural motifs, combined with recognition of GH11 catalytic glutamate motifs in the sequence. This constitutes a concrete biological argument from the supplied sequence rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent entirely different enzyme classes (nucleoside transporter, P450 monooxygenase, glycoside hydrolase, flavoenzyme). The sequence's features unambiguously align with a glycoside hydrolase and specifically with GH11 xylanase motifs. No other choice is defensible given the absence of their required cofactor-binding or membrane-spanning features."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2013 paper, not merely computational inference, strengthening the key.",
    "The sequence match is exact (SHA256 confirmed) in both current (v43) and historical (v41) records.",
    "The GH11 catalytic motif recognition (EIDHY, EILD) requires specialized glycoside hydrolase knowledge but is within the scope of general enzymology training.",
    "The entry was first public in Feb 2025; the underlying sequence was deposited in 2013. The author's source snapshot date is unknown but the sequence has been stable since version 1."
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

**Accession:** `M4MEY9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 41. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.429543+00:00.  

```json
"M4MEY9"
```

Source SHA-256: `d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.429543+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"1,4-beta-D-xylan xylanohydrolase C"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23306124","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase C"}}}
```

Source SHA-256: `d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.429543+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000269","id":"23306124","source":"PubMed"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MEY9.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:11.429543+00:00.  

```json
{"citation":{"authors":["Du Y.","Shi P.","Huang H.","Zhang X.","Luo H.","Wang Y.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"23306124"},{"database":"DOI","id":"10.1016/j.biortech.2012.12.067"}],"citationType":"journal article","firstPage":"161","id":"23306124","journal":"Bioresour. Technol.","lastPage":"167","publicationDate":"2013","title":"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.","volume":"130"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `d9bd8bfd23517f3f8126109abf780bdee9a19b52cb516a046043eacb8db8c61e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:28:15.495114+00:00.  

```text
ID   XYNC_HUMIN              Reviewed;         390 AA.
AC   M4MEY9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-MAY-2013, sequence version 1.
DT   28-JAN-2026, entry version 41.
DE   RecName: Full=Endo-1,4-beta-xylanase C {ECO:0000303|PubMed:23306124};
DE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};
DE   AltName: Full=1,4-beta-D-xylan xylanohydrolase C {ECO:0000305};
DE   Flags: Precursor;
GN   Name=XynC {ECO:0000303|PubMed:23306124};
GN   Synonyms=Xyl3 {ECO:0000303|PubMed:8190078},
GN   XynW {ECO:0000303|PubMed:23306124};
OS   Humicola insolens (Soft-rot fungus).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.
OX   NCBI_TaxID=85995;
```

Source SHA-256: `9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:28:15.495114+00:00.  

```text
DE   RecName: Full=Endo-1,4-beta-xylanase C {ECO:0000303|PubMed:23306124};
DE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};
DE   AltName: Full=1,4-beta-D-xylan xylanohydrolase C {ECO:0000305};
DE   Flags: Precursor;
```

Source SHA-256: `9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)  
**Locator:** `lines 17-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:28:15.495114+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,
RP   AND BIOTECHNOLOGY.
RC   STRAIN=Y1;
RX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;
RA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;
RT   "Characterization of three novel thermophilic xylanases from Humicola
RT   insolens Y1 with application potentials in the brewing industry.";
RL   Bioresour. Technol. 130:161-167(2013).
```

Source SHA-256: `9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MEY9?format=txt&versions=41)  
**Locator:** `lines 49-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:28:15.495114+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:23306124};
```

Source SHA-256: `9dc7e9736e7d34c8bccd0868438a05ae778ddd272d60de362475169c62466a2b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
