# catalytic_activity_0095

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — Endohydrolysis of (1-&gt;4)-beta-D-xylosidic linkages in xylans.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSFTTLLAGFVAVTGVLSAPTETVEVVDVEKRQTIGPGTGFNNGYYYSYWNDGHSGVTYTNGAGGSFSVNWANSGNFVGGKGWNPGSSSRVINFSGSYNPNGNSYLSVYGWSKNPLIEYYIVENFGTYNPSTGTTKLGEVTSDGSVYDIYRTQRVNQPSIIGTATFYQYWSVRRNHAPAARSRLRTTSNAWRNLGLTLGTLDYQIIAVEGYFSSGNANINVS

[Multiple Choices]
A. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
B. ATP + protein L-histidine = ADP + protein N-phospho-L-histidine.
C. an aliphatic sulfonate + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + an aldehyde + sulfite + 3 H(+)
D. GDGT-0 + AH2 + 2 S-adenosyl-L-methionine = GMGT-0 + 2 5'-deoxyadenosine + 2 L-methionine + A + 2 H(+)
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

> The sequence exactly matches the UniProt record whose catalytic-activity annotation gives choice A. That annotation cites experimental evidence (ECO:0000269) and a paper reporting catalytic activity; this supports the key for this sequence, though the original source snapshot is unknown.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region is consistent with a secretion signal, and the sequence is compatible with a small secreted enzyme. This makes the extracellular enzyme option more plausible than the kinase, iron-sulfur, or archaeal lipid-synthesis alternatives, but does not establish the specific xylan substrate or linkage.


**Missing item-specific fact**

> The protein-specific catalytic activity (endo-1,4-beta-xylanase), established by annotation or experimental characterization, is not supplied in the question.


**Reason**

> Broad sequence features can favor an extracellular enzyme, but the precise reaction in choice A requires identifying its substrate specificity; those features alone do not reliably distinguish a xylanase from other secreted enzymes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports A for the matched sequence, and the listed alternatives describe substantially different enzyme activities.


### Important caveats

- The supporting UniProt annotation and experimental references are reviewer-only evidence, not information available in the original question.
- The current and historical UniProt records both match the supplied sequence; the author's exact source snapshot remains unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with a secretion signal, and the sequence is compatible with a small secreted enzyme. This makes the extracellular enzyme option more plausible than the kinase, iron-sulfur, or archaeal lipid-synthesis alternatives, but does not establish the specific xylan substrate or linkage.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity (endo-1,4-beta-xylanase), established by annotation or experimental characterization, is not supplied in the question.",
    "reason": "Broad sequence features can favor an extracellular enzyme, but the precise reaction in choice A requires identifying its substrate specificity; those features alone do not reliably distinguish a xylanase from other secreted enzymes."
  },
  "case_id": "catalytic_activity_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record whose catalytic-activity annotation gives choice A. That annotation cites experimental evidence (ECO:0000269) and a paper reporting catalytic activity; this supports the key for this sequence, though the original source snapshot is unknown."
  },
  "important_caveats": [
    "The supporting UniProt annotation and experimental references are reviewer-only evidence, not information available in the original question.",
    "The current and historical UniProt records both match the supplied sequence; the author's exact source snapshot remains unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A for the matched sequence, and the listed alternatives describe substantially different enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0095",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record whose catalytic-activity annotation gives choice A. That annotation cites experimental evidence (ECO:0000269) and a paper reporting catalytic activity; this supports the key for this sequence, though the original source snapshot is unknown.",
    "evidence_ids": ["C5", "C8", "H6", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with a secretion signal, and the sequence is compatible with a small secreted enzyme. This makes the extracellular enzyme option more plausible than the kinase, iron-sulfur, or archaeal lipid-synthesis alternatives, but does not establish the specific xylan substrate or linkage.",
    "missing_item_specific_fact": "The protein-specific catalytic activity (endo-1,4-beta-xylanase), established by annotation or experimental characterization, is not supplied in the question.",
    "reason": "Broad sequence features can favor an extracellular enzyme, but the precise reaction in choice A requires identifying its substrate specificity; those features alone do not reliably distinguish a xylanase from other secreted enzymes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A for the matched sequence, and the listed alternatives describe substantially different enzyme activities."
  },
  "important_caveats": [
    "The supporting UniProt annotation and experimental references are reviewer-only evidence, not information available in the original question.",
    "The current and historical UniProt records both match the supplied sequence; the author's exact source snapshot remains unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9UVF9 (EIX_HYPRU) matches the 223-aa benchmark sequence exactly (same SHA256). The entry assigns EC 3.2.1.8 with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' supported by direct assay evidence (ECO:0000269, PubMed:16668223). Multiple independent papers (Fuchs 1989, Dean 1991, Furman-Matarasso 1999) confirm the endo-xylanase function. The answer text matches the UniProt annotation verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark GH11 xylanase motifs: the N-terminal signal peptide (MVSFTTLLAGFVAVTGVLSAPTET) indicates a secreted protein; the 'GTGFNNGYYYSYWNDG' region is the conserved catalytic/substrate-binding signature of glycoside hydrolase family 11; the small size (~223 aa) and beta-sheet-rich composition (abundant G, Y, N, S) are consistent with the beta-jellyroll fold of GH11. The distractors require motifs entirely absent here: (B) a P-loop/NTPase fold for histidine kinase; (C) multiple Cys-rich clusters for &#91;4Fe-4S&#93; ferredoxin-type dioxygenase; (D) a radical SAM CxxxCxxC motif and SAM-binding domain for GDGT methyltransferase. A model with general enzyme-family knowledge can identify the GH11 signature and eliminate the other three options by absence of their required structural motifs.


**Missing item-specific fact**

> None critical. Recognition of the GTG…YYYSY GH11 signature is general biochemical knowledge about glycoside hydrolase families, not a protein-specific lookup.


**Reason**

> The sequence provides concrete, identifiable features (signal peptide, GH11 catalytic motif, small beta-rich architecture) that positively support choice A, while the three distractors each demand structural motifs (Fe-S clusters, SAM-binding, P-loop) that are demonstrably absent from the sequence. This allows meaningful elimination by general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent vastly different enzyme classes (glycosidase, kinase, Fe-S dioxygenase, radical SAM methyltransferase). Only the xylanase option is consistent with the sequence's motifs, size, and predicted secretion. No other option is defensible.


### Important caveats

- The EC annotation carries ECO:0000255 (PROSITE-ProRule, computational) for the EC number itself, but the catalytic activity statement carries ECO:0000269 (direct assay), indicating experimental confirmation.
- The protein is also known as an ethylene-inducing elicitor (EIX); its xylanase activity and elicitor activity are separable (Furman-Matarasso 1999 showed a point mutation uncoupled them). The question asks about catalytic activity, for which the xylanase function is the correct answer.
- Reviewer-only evidence was unavailable to the evaluated model; the reasoning-supported classification relies on general GH11 knowledge being part of standard biochemistry training.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark GH11 xylanase motifs: the N-terminal signal peptide (MVSFTTLLAGFVAVTGVLSAPTET) indicates a secreted protein; the 'GTGFNNGYYYSYWNDG' region is the conserved catalytic/substrate-binding signature of glycoside hydrolase family 11; the small size (~223 aa) and beta-sheet-rich composition (abundant G, Y, N, S) are consistent with the beta-jellyroll fold of GH11. The distractors require motifs entirely absent here: (B) a P-loop/NTPase fold for histidine kinase; (C) multiple Cys-rich clusters for [4Fe-4S] ferredoxin-type dioxygenase; (D) a radical SAM CxxxCxxC motif and SAM-binding domain for GDGT methyltransferase. A model with general enzyme-family knowledge can identify the GH11 signature and eliminate the other three options by absence of their required structural motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the GTG…YYYSY GH11 signature is general biochemical knowledge about glycoside hydrolase families, not a protein-specific lookup.",
    "reason": "The sequence provides concrete, identifiable features (signal peptide, GH11 catalytic motif, small beta-rich architecture) that positively support choice A, while the three distractors each demand structural motifs (Fe-S clusters, SAM-binding, P-loop) that are demonstrably absent from the sequence. This allows meaningful elimination by general biological reasoning."
  },
  "case_id": "catalytic_activity_0095",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9UVF9 (EIX_HYPRU) matches the 223-aa benchmark sequence exactly (same SHA256). The entry assigns EC 3.2.1.8 with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' supported by direct assay evidence (ECO:0000269, PubMed:16668223). Multiple independent papers (Fuchs 1989, Dean 1991, Furman-Matarasso 1999) confirm the endo-xylanase function. The answer text matches the UniProt annotation verbatim."
  },
  "important_caveats": [
    "The EC annotation carries ECO:0000255 (PROSITE-ProRule, computational) for the EC number itself, but the catalytic activity statement carries ECO:0000269 (direct assay), indicating experimental confirmation.",
    "The protein is also known as an ethylene-inducing elicitor (EIX); its xylanase activity and elicitor activity are separable (Furman-Matarasso 1999 showed a point mutation uncoupled them). The question asks about catalytic activity, for which the xylanase function is the correct answer.",
    "Reviewer-only evidence was unavailable to the evaluated model; the reasoning-supported classification relies on general GH11 knowledge being part of standard biochemistry training."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent vastly different enzyme classes (glycosidase, kinase, Fe-S dioxygenase, radical SAM methyltransferase). Only the xylanase option is consistent with the sequence's motifs, size, and predicted secretion. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0095",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9UVF9 (EIX_HYPRU) matches the 223-aa benchmark sequence exactly (same SHA256). The entry assigns EC 3.2.1.8 with catalytic activity 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans,' supported by direct assay evidence (ECO:0000269, PubMed:16668223). Multiple independent papers (Fuchs 1989, Dean 1991, Furman-Matarasso 1999) confirm the endo-xylanase function. The answer text matches the UniProt annotation verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark GH11 xylanase motifs: the N-terminal signal peptide (MVSFTTLLAGFVAVTGVLSAPTET) indicates a secreted protein; the 'GTGFNNGYYYSYWNDG' region is the conserved catalytic/substrate-binding signature of glycoside hydrolase family 11; the small size (~223 aa) and beta-sheet-rich composition (abundant G, Y, N, S) are consistent with the beta-jellyroll fold of GH11. The distractors require motifs entirely absent here: (B) a P-loop/NTPase fold for histidine kinase; (C) multiple Cys-rich clusters for [4Fe-4S] ferredoxin-type dioxygenase; (D) a radical SAM CxxxCxxC motif and SAM-binding domain for GDGT methyltransferase. A model with general enzyme-family knowledge can identify the GH11 signature and eliminate the other three options by absence of their required structural motifs.",
    "missing_item_specific_fact": "None critical. Recognition of the GTG…YYYSY GH11 signature is general biochemical knowledge about glycoside hydrolase families, not a protein-specific lookup.",
    "reason": "The sequence provides concrete, identifiable features (signal peptide, GH11 catalytic motif, small beta-rich architecture) that positively support choice A, while the three distractors each demand structural motifs (Fe-S clusters, SAM-binding, P-loop) that are demonstrably absent from the sequence. This allows meaningful elimination by general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent vastly different enzyme classes (glycosidase, kinase, Fe-S dioxygenase, radical SAM methyltransferase). Only the xylanase option is consistent with the sequence's motifs, size, and predicted secretion. No other option is defensible."
  },
  "important_caveats": [
    "The EC annotation carries ECO:0000255 (PROSITE-ProRule, computational) for the EC number itself, but the catalytic activity statement carries ECO:0000269 (direct assay), indicating experimental confirmation.",
    "The protein is also known as an ethylene-inducing elicitor (EIX); its xylanase activity and elicitor activity are separable (Furman-Matarasso 1999 showed a point mutation uncoupled them). The question asks about catalytic activity, for which the xylanase function is the correct answer.",
    "Reviewer-only evidence was unavailable to the evaluated model; the reasoning-supported classification relies on general GH11 knowledge being part of standard biochemistry training."
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

**Accession:** `Q9UVF9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 91. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"Endo-1,4-beta-xylanase EIX"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16666504","source":"PubMed"}],"value":"Ethylene biosynthesis-inducing factor"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"16666504","source":"PubMed"}],"value":"EIF"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01097","source":"PROSITE-ProRule"}],"value":"3.2.1.8"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"Ethylene-inducing xylanase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10517825","source":"PubMed"}],"value":"EIX"}]}}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.8","evidences":[{"evidenceCode":"ECO:0000269","id":"16668223","source":"PubMed"}],"name":"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans."}}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"citation":{"authors":["Furman-Matarasso N.","Cohen E.","Du Q.","Chejanovsky N.","Hanania U.","Avni A."],"citationCrossReferences":[{"database":"PubMed","id":"10517825"},{"database":"DOI","id":"10.1104/pp.121.2.345"}],"citationType":"journal article","firstPage":"345","id":"10517825","journal":"Plant Physiol.","lastPage":"351","publicationDate":"1999","title":"A point mutation in the ethylene-inducing xylanase elicitor inhibits the beta-1-4-endoxylanase activity but not the elicitation activity.","volume":"121"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","SUBCELLULAR LOCATION","MUTAGENESIS OF GLU-86 AND GLU-177"]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"citation":{"authors":["Fuchs Y.","Saxena A.","Gamble H.R.","Anderson J.D."],"citationCrossReferences":[{"database":"PubMed","id":"16666504"},{"database":"DOI","id":"10.1104/pp.89.1.138"}],"citationType":"journal article","firstPage":"138","id":"16666504","journal":"Plant Physiol.","lastPage":"143","publicationDate":"1989","title":"Ethylene biosynthesis-inducing protein from cellulysin is an endoxylanase.","volume":"89"},"referenceNumber":2,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.394840+00:00.  

```json
{"citation":{"authors":["Dean J.F.","Gross K.C.","Anderson J.D."],"citationCrossReferences":[{"database":"PubMed","id":"16668223"},{"database":"DOI","id":"10.1104/pp.96.2.571"}],"citationType":"journal article","firstPage":"571","id":"16668223","journal":"Plant Physiol.","lastPage":"576","publicationDate":"1991","title":"Ethylene Biosynthesis-Inducing Xylanase: III. Product Characterization.","volume":"96"},"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
ID   EIX_HYPRU               Reviewed;         223 AA.
AC   Q9UVF9;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 91.
DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:10517825};
DE            Short=EIX {ECO:0000303|PubMed:10517825};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:10517825};
DE   AltName: Full=Ethylene biosynthesis-inducing factor {ECO:0000303|PubMed:16666504};
DE            Short=EIF {ECO:0000303|PubMed:16666504};
DE   Flags: Precursor;
GN   Name=EIX {ECO:0000303|PubMed:10517825};
OS   Hypocrea rufa (Trichoderma viride).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Trichoderma.
OX   NCBI_TaxID=5547;
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 6-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:10517825};
DE            Short=EIX {ECO:0000303|PubMed:10517825};
DE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};
DE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:10517825};
DE   AltName: Full=Ethylene biosynthesis-inducing factor {ECO:0000303|PubMed:16666504};
DE            Short=EIF {ECO:0000303|PubMed:16666504};
DE   Flags: Precursor;
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 47-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
RN   [5]
RP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=16668223; DOI=10.1104/pp.96.2.571;
RA   Dean J.F., Gross K.C., Anderson J.D.;
RT   "Ethylene Biosynthesis-Inducing Xylanase: III. Product Characterization.";
RL   Plant Physiol. 96:571-576(1991).
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)  
**Locator:** `lines 156-158`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-01T06:28:50.576003+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;
CC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:16668223};
```

Source SHA-256: `58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 95. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
