# catalytic_activity_0170

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — ATP-independent breakage of single-stranded DNA, followed by passage and rejoining.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNLCNVNNYYLIIAEKSKAAKKIAEALSEKPILCRKYNVSYWIIKDHNSSKYVIVPAAGHLFGLKGESGFPVYDADWKPLWEIDKNSYYTKRYYQLISSLSKYALGFINACDYDIEGSVIGYLIIKNLGDIKKAKRMKFSALTKSDILSAFRNISALDYDMINAGIARHKIDWLWGINVSRALMISLQDFAKKRVILSAGRVQSPTLVQVVNSEIERNLFIPLPKFTVSIIVKIKDYSLNIKVNKEFEKITEAKEFLNKLINKTVKVVEVENRVRLLERPSPFNLTDLQIEAGRIYGISPYNVERIAEDLYLDGLISYPRTNSQKIPSTISIYNIIKGLENSSYRKLVDLVRKITGGKYVVKQGIKDDPAHPAIHPTGEAPKNLPNSKFKIYDLIARRFLGSVSADAKLSNTIYTLKVSDFPLEFTVSYTKILERNWLDIYHFHNVKEDKPIFLSKGDEGKIVDGKVNISLSKPTSRYTKVSLLKWMESSNLGTEATRGRIIEILVKRKYLTNNGRYIIPTKLGFYIAEILNKFFPDIVDVRMTADMESKLEMIKTGKVLESKVIKENIEKLNKFIEEYKVNKDKVGESLAKALGLIKIVKCKYCDLEQYKDGLCKYHYEAKVRLLDAVEIWKERTKYDHKKILKRISSSKSTGKYVKDIVTYMLSSE

[Multiple Choices]
A. (R)-norprotosinomenine + S-adenosyl-L-methionine = (R)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)
B. vinorine + reduced [NADPH--hemoprotein reductase] + O2 = vomilenine + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
C. L-arginine(in) = L-arginine(out)
D. ATP-independent breakage of single-stranded DNA, followed by passage and rejoining.
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

> The exact sequence matches the UniProt entry for DNA topoisomerase 3, whose catalytic-activity annotation is choice D and carries experimental evidence codes. The archived entry also supports this annotation, though the authors’ exact source snapshot is unknown.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, soluble sequence is consistent with a DNA topoisomerase rather than a membrane transporter, and includes a putative conserved catalytic-tyrosine motif (around YGISPYN) consistent with a type IA topoisomerase. That makes the DNA breakage, passage, and rejoining reaction a defensible choice over the distinct methyltransferase, oxidase, and transport alternatives.


**Missing item-specific fact**

> No external annotation is necessary to distinguish these choices if the topoisomerase sequence features are recognized; the exact protein identity would otherwise be an item-specific fact.


**Reason**

> The sequence offers a family-level biological clue for a topoisomerase, and choice D describes its characteristic strand-passage reaction. This is more than recognizing or recalling the exact database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reaction types, and the sequence features favor a DNA topoisomerase rather than any of the other listed activities.


### Important caveats

- The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.
- The cited annotation carries experimental evidence codes, but the primary studies were not independently reviewed here; the authors’ exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, soluble sequence is consistent with a DNA topoisomerase rather than a membrane transporter, and includes a putative conserved catalytic-tyrosine motif (around YGISPYN) consistent with a type IA topoisomerase. That makes the DNA breakage, passage, and rejoining reaction a defensible choice over the distinct methyltransferase, oxidase, and transport alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external annotation is necessary to distinguish these choices if the topoisomerase sequence features are recognized; the exact protein identity would otherwise be an item-specific fact.",
    "reason": "The sequence offers a family-level biological clue for a topoisomerase, and choice D describes its characteristic strand-passage reaction. This is more than recognizing or recalling the exact database entry."
  },
  "case_id": "catalytic_activity_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for DNA topoisomerase 3, whose catalytic-activity annotation is choice D and carries experimental evidence codes. The archived entry also supports this annotation, though the authors’ exact source snapshot is unknown."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.",
    "The cited annotation carries experimental evidence codes, but the primary studies were not independently reviewed here; the authors’ exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the sequence features favor a DNA topoisomerase rather than any of the other listed activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for DNA topoisomerase 3, whose catalytic-activity annotation is choice D and carries experimental evidence codes. The archived entry also supports this annotation, though the authors’ exact source snapshot is unknown.",
    "evidence_ids": ["C1", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, soluble sequence is consistent with a DNA topoisomerase rather than a membrane transporter, and includes a putative conserved catalytic-tyrosine motif (around YGISPYN) consistent with a type IA topoisomerase. That makes the DNA breakage, passage, and rejoining reaction a defensible choice over the distinct methyltransferase, oxidase, and transport alternatives.",
    "missing_item_specific_fact": "No external annotation is necessary to distinguish these choices if the topoisomerase sequence features are recognized; the exact protein identity would otherwise be an item-specific fact.",
    "reason": "The sequence offers a family-level biological clue for a topoisomerase, and choice D describes its characteristic strand-passage reaction. This is more than recognizing or recalling the exact database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reaction types, and the sequence features favor a DNA topoisomerase rather than any of the other listed activities."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports the key but was not supplied to the evaluated model.",
    "The cited annotation carries experimental evidence codes, but the primary studies were not independently reviewed here; the authors’ exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The benchmark sequence (668 aa, SHA256-matched) corresponds to UniProt Q97ZJ8, DNA topoisomerase 3 (SsTop3/SsTopA) from Saccharolobus solfataricus. The UniProt entry explicitly annotates the catalytic activity as 'ATP-independent breakage of single-stranded DNA, followed by passage and rejoining' (EC 5.6.2.1), supported by experimental evidence (ECO:0000269) from two independent peer-reviewed studies (PubMed 22722926, 29253195). The expected answer D is a verbatim match to the UniProt CATALYTIC ACTIVITY annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable zinc-binding motif of type IA topoisomerases: the region 'KYCDLEQYKDGLCKYHYEAKV' presents the conserved CxxC…CxxC zinc-binding cluster flanking a catalytic tyrosine (the Y in YKDGL), which is the nucleophile for transient DNA cleavage. This TOPRIM-domain signature is a well-known hallmark of the type IA topoisomerase superfamily (Topo I, Topo III, Topo IV subunits), all of which share the mechanism of ATP-independent single-strand DNA breakage, passage, and rejoining. The other options can be eliminated by absence of their defining features: no heme-binding FxxGxxxCxG motif (rules out B, a cytochrome P450); no transmembrane helical segments (rules out C, an arginine transporter); no Rossmann-fold SAM-binding motif (rules out A, an O-methyltransferase). Among the four choices, only D matches a type IA topoisomerase mechanism.


**Missing item-specific fact**

> None critical. Distinguishing Topo III specifically from Topo I by sequence alone is difficult, but since only one topoisomerase option (D) is offered, the TOPRIM/zinc-binding motif is sufficient to select D over the non-topoisomerase distractors.


**Reason**

> A model with knowledge of type IA topoisomerase structural motifs (zinc-binding CxxC cluster, catalytic Tyr, TOPRIM fold) can identify the enzyme class from the sequence and eliminate the three non-topoisomerase distractors. This is a concrete biological argument from the supplied sequence, not mere database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The zinc-binding motif and catalytic tyrosine context in the sequence are inconsistent with methyltransferase (A), cytochrome P450 (B), or membrane transporter (C) folds. Only D is compatible with the identifiable topoisomerase-type IA features.


### Important caveats

- The UniProt annotation is supported by experimental evidence (ECO:0000269) from two independent studies, not merely computational inference.
- The sequence match is exact (SHA256 identical) between the benchmark input and the UniProt entry, confirming the annotation applies to this exact protein.
- Distinguishing Topo III from Topo I by sequence alone is non-trivial, but the question design (only one topoisomerase option) makes this distinction unnecessary for answering correctly.
- The reviewer-only UniProt accession (Q97ZJ8) was not available to the evaluated model; the reasoning argument relies solely on observable sequence motifs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable zinc-binding motif of type IA topoisomerases: the region 'KYCDLEQYKDGLCKYHYEAKV' presents the conserved CxxC…CxxC zinc-binding cluster flanking a catalytic tyrosine (the Y in YKDGL), which is the nucleophile for transient DNA cleavage. This TOPRIM-domain signature is a well-known hallmark of the type IA topoisomerase superfamily (Topo I, Topo III, Topo IV subunits), all of which share the mechanism of ATP-independent single-strand DNA breakage, passage, and rejoining. The other options can be eliminated by absence of their defining features: no heme-binding FxxGxxxCxG motif (rules out B, a cytochrome P450); no transmembrane helical segments (rules out C, an arginine transporter); no Rossmann-fold SAM-binding motif (rules out A, an O-methyltransferase). Among the four choices, only D matches a type IA topoisomerase mechanism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Distinguishing Topo III specifically from Topo I by sequence alone is difficult, but since only one topoisomerase option (D) is offered, the TOPRIM/zinc-binding motif is sufficient to select D over the non-topoisomerase distractors.",
    "reason": "A model with knowledge of type IA topoisomerase structural motifs (zinc-binding CxxC cluster, catalytic Tyr, TOPRIM fold) can identify the enzyme class from the sequence and eliminate the three non-topoisomerase distractors. This is a concrete biological argument from the supplied sequence, not mere database lookup."
  },
  "case_id": "catalytic_activity_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The benchmark sequence (668 aa, SHA256-matched) corresponds to UniProt Q97ZJ8, DNA topoisomerase 3 (SsTop3/SsTopA) from Saccharolobus solfataricus. The UniProt entry explicitly annotates the catalytic activity as 'ATP-independent breakage of single-stranded DNA, followed by passage and rejoining' (EC 5.6.2.1), supported by experimental evidence (ECO:0000269) from two independent peer-reviewed studies (PubMed 22722926, 29253195). The expected answer D is a verbatim match to the UniProt CATALYTIC ACTIVITY annotation."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (ECO:0000269) from two independent studies, not merely computational inference.",
    "The sequence match is exact (SHA256 identical) between the benchmark input and the UniProt entry, confirming the annotation applies to this exact protein.",
    "Distinguishing Topo III from Topo I by sequence alone is non-trivial, but the question design (only one topoisomerase option) makes this distinction unnecessary for answering correctly.",
    "The reviewer-only UniProt accession (Q97ZJ8) was not available to the evaluated model; the reasoning argument relies solely on observable sequence motifs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The zinc-binding motif and catalytic tyrosine context in the sequence are inconsistent with methyltransferase (A), cytochrome P450 (B), or membrane transporter (C) folds. Only D is compatible with the identifiable topoisomerase-type IA features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The benchmark sequence (668 aa, SHA256-matched) corresponds to UniProt Q97ZJ8, DNA topoisomerase 3 (SsTop3/SsTopA) from Saccharolobus solfataricus. The UniProt entry explicitly annotates the catalytic activity as 'ATP-independent breakage of single-stranded DNA, followed by passage and rejoining' (EC 5.6.2.1), supported by experimental evidence (ECO:0000269) from two independent peer-reviewed studies (PubMed 22722926, 29253195). The expected answer D is a verbatim match to the UniProt CATALYTIC ACTIVITY annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable zinc-binding motif of type IA topoisomerases: the region 'KYCDLEQYKDGLCKYHYEAKV' presents the conserved CxxC…CxxC zinc-binding cluster flanking a catalytic tyrosine (the Y in YKDGL), which is the nucleophile for transient DNA cleavage. This TOPRIM-domain signature is a well-known hallmark of the type IA topoisomerase superfamily (Topo I, Topo III, Topo IV subunits), all of which share the mechanism of ATP-independent single-strand DNA breakage, passage, and rejoining. The other options can be eliminated by absence of their defining features: no heme-binding FxxGxxxCxG motif (rules out B, a cytochrome P450); no transmembrane helical segments (rules out C, an arginine transporter); no Rossmann-fold SAM-binding motif (rules out A, an O-methyltransferase). Among the four choices, only D matches a type IA topoisomerase mechanism.",
    "missing_item_specific_fact": "None critical. Distinguishing Topo III specifically from Topo I by sequence alone is difficult, but since only one topoisomerase option (D) is offered, the TOPRIM/zinc-binding motif is sufficient to select D over the non-topoisomerase distractors.",
    "reason": "A model with knowledge of type IA topoisomerase structural motifs (zinc-binding CxxC cluster, catalytic Tyr, TOPRIM fold) can identify the enzyme class from the sequence and eliminate the three non-topoisomerase distractors. This is a concrete biological argument from the supplied sequence, not mere database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The zinc-binding motif and catalytic tyrosine context in the sequence are inconsistent with methyltransferase (A), cytochrome P450 (B), or membrane transporter (C) folds. Only D is compatible with the identifiable topoisomerase-type IA features."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (ECO:0000269) from two independent studies, not merely computational inference.",
    "The sequence match is exact (SHA256 identical) between the benchmark input and the UniProt entry, confirming the annotation applies to this exact protein.",
    "Distinguishing Topo III from Topo I by sequence alone is non-trivial, but the question design (only one topoisomerase option) makes this distinction unnecessary for answering correctly.",
    "The reviewer-only UniProt accession (Q97ZJ8) was not available to the evaluated model; the reasoning argument relies solely on observable sequence motifs."
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

**Accession:** `Q97ZJ8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 132. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
"Q97ZJ8"
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29253195","source":"PubMed"}],"value":"DNA topoisomerase III"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22722926","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29253195","source":"PubMed"}],"value":"5.6.2.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22722926","source":"PubMed"}],"value":"DNA topoisomerase 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22722926","source":"PubMed"}],"value":"SsTop3"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"29253195","source":"PubMed"}],"value":"SsTopA"}]}}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.6.2.1","evidences":[{"evidenceCode":"ECO:0000269","id":"22722926","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29253195","source":"PubMed"}],"name":"ATP-independent breakage of single-stranded DNA, followed by passage and rejoining."}}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"citation":{"authors":["Valenti A.","De Felice M.","Perugino G.","Bizard A.","Nadal M.","Rossi M.","Ciaramella M."],"citationCrossReferences":[{"database":"PubMed","id":"22722926"},{"database":"DOI","id":"10.1074/jbc.m112.366377"}],"citationType":"journal article","firstPage":"30282","id":"22722926","journal":"J. Biol. Chem.","lastPage":"30295","publicationDate":"2012","title":"Synergic and opposing activities of thermophilic RecQ-like helicase and topoisomerase 3 proteins in Holliday junction processing and replication fork stabilization.","volume":"287"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBUNIT","INTERACTION WITH LHR","DNA-BINDING"]}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"citation":{"authors":["Bizard A.H.","Yang X.","Debat H.","Fogg J.M.","Zechiedrich L.","Strick T.R.","Garnier F.","Nadal M."],"citationCrossReferences":[{"database":"PubMed","id":"29253195"},{"database":"DOI","id":"10.1093/nar/gkx1247"}],"citationType":"journal article","firstPage":"861","id":"29253195","journal":"Nucleic Acids Res.","lastPage":"872","publicationDate":"2018","title":"TopA, the Sulfolobus solfataricus topoisomerase III, is a decatenase.","volume":"46"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
ID   TOP3_SACS2              Reviewed;         668 AA.
AC   Q97ZJ8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2001, sequence version 1.
DT   28-JAN-2026, entry version 132.
DE   RecName: Full=DNA topoisomerase 3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTop3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTopA {ECO:0000303|PubMed:29253195};
DE            EC=5.6.2.1 {ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:29253195};
DE   AltName: Full=DNA topoisomerase III {ECO:0000303|PubMed:29253195};
GN   Name=topA {ECO:0000303|PubMed:22722926, ECO:0000312|EMBL:AAK41190.1};
GN   OrderedLocusNames=SSO0907 {ECO:0000312|EMBL:AAK41190.1};
OS   Saccharolobus solfataricus (strain ATCC 35092 / DSM 1617 / JCM 11322 / P2)
OS   (Sulfolobus solfataricus).
OC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;
OC   Saccharolobus.
OX   NCBI_TaxID=273057;
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
DE   RecName: Full=DNA topoisomerase 3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTop3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTopA {ECO:0000303|PubMed:29253195};
DE            EC=5.6.2.1 {ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:29253195};
DE   AltName: Full=DNA topoisomerase III {ECO:0000303|PubMed:29253195};
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, INTERACTION WITH LHR, AND
RP   DNA-BINDING.
RX   PubMed=22722926; DOI=10.1074/jbc.m112.366377;
RA   Valenti A., De Felice M., Perugino G., Bizard A., Nadal M., Rossi M.,
RA   Ciaramella M.;
RT   "Synergic and opposing activities of thermophilic RecQ-like helicase and
RT   topoisomerase 3 proteins in Holliday junction processing and replication
RT   fork stabilization.";
RL   J. Biol. Chem. 287:30282-30295(2012).
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 40-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, AND
RP   BIOPHYSICOCHEMICAL PROPERTIES.
RX   PubMed=29253195; DOI=10.1093/nar/gkx1247;
RA   Bizard A.H., Yang X., Debat H., Fogg J.M., Zechiedrich L., Strick T.R.,
RA   Garnier F., Nadal M.;
RT   "TopA, the Sulfolobus solfataricus topoisomerase III, is a decatenase.";
RL   Nucleic Acids Res. 46:861-872(2018).
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 68-71`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP-independent breakage of single-stranded DNA, followed by
CC         passage and rejoining.; EC=5.6.2.1;
CC         Evidence={ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:29253195};
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
