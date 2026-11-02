# catalytic_activity_0026

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — Fe(2+)(in) = Fe(2+)(out)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHQDNSMRRAINQSRNGGSDSCDINNDREHDNINRNSYINNFHIENINSDKNEQSYIYCSDRAQVTDSILGNRKYTHEENINSTEMFSRTNYEYSNKNNVDIEMYNISNNNFYNGNNNGHSNDIIDYINNNNVNKDLSNTSNNADINTYIKKLTSNQSTAYCDGKGYNESANGSNFDINFRDVIKNNNNKNYKNNNHVPDDMLELGDRSFDSSFYIHNNVEEIDTERSNRLSFMSKLKMYFNYFGPGWIVAIAYLDPGNICGNLNVGLIRSDDFINVNSSVKDYTGYRLLWVLVYGHILGFIFHTLSMKLGHITGLDLAALCRKEFSSKFSYFLYICVQIAIWGAHLQAIIGVFVAINLILGIPVKIAILYTLIEAFAYSFLENKSLDLLEKVLSLLIGILVCCFMFNVFMTPINFQEVASSILYPRIPKGKLLDTMGLLGSVISAHIFYLHSNLTSKKKPVIYNDRMVKRYNKLGTIESGGSLLVSCITNCIIVLTFAEVNISGDDRKADYNLFNAYDVMKKYFGKTSMYIWSFGLLSSGNNASFMCEYASKSVFEGFLNKNVNPFFRVIFSRIILFIMLYAYVSYDKYTIDQLSNFINVVQILLLPLAIIPLYRFSIHKNVLGKFAIKGAFKYLVFVLVISIIVANFLLTLFDFLQYAPSNLYVIFIFISSIFYLLFIIYFFNMPITKTYYKDS

[Multiple Choices]
A. 5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O
B. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
C. demethylluteothin + S-adenosyl-L-methionine = luteothin + S-adenosyl-L-homocysteine
D. Fe(2+)(in) = Fe(2+)(out)
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

> The supplied sequence exactly matches the UniProt entry annotating Fe(2+)(in) = Fe(2+)(out) as catalytic activity, with experimental evidence code ECO:0000269 citing a 2023 paper. The archived entry also contains this annotation. This supports D for this sequence, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic stretches support a multipass membrane protein, making the transport option more plausible than the listed reactions typical of soluble enzymes. That does not establish that the transported substrate is Fe(2+).


**Missing item-specific fact**

> The protein-specific transporter annotation or experimental evidence identifying Fe(2+) transport is needed to distinguish D on substrate identity.


**Reason**

> Sequence topology offers a useful clue toward a transporter, but the precise transport activity is not established by the supplied sequence and choices alone; selecting Fe(2+) depends on a protein-specific fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only listed transport reaction and is supported by the sequence-matched annotation. The sequence alone, however, does not demonstrate its Fe(2+) specificity.


### Important caveats

- The experimental evidence is reported in a UniProt annotation citing a paper; the paper was not independently assessed.
- The reviewer-only database identity and annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic stretches support a multipass membrane protein, making the transport option more plausible than the listed reactions typical of soluble enzymes. That does not establish that the transported substrate is Fe(2+).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transporter annotation or experimental evidence identifying Fe(2+) transport is needed to distinguish D on substrate identity.",
    "reason": "Sequence topology offers a useful clue toward a transporter, but the precise transport activity is not established by the supplied sequence and choices alone; selecting Fe(2+) depends on a protein-specific fact."
  },
  "case_id": "catalytic_activity_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotating Fe(2+)(in) = Fe(2+)(out) as catalytic activity, with experimental evidence code ECO:0000269 citing a 2023 paper. The archived entry also contains this annotation. This supports D for this sequence, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental evidence is reported in a UniProt annotation citing a paper; the paper was not independently assessed.",
    "The reviewer-only database identity and annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only listed transport reaction and is supported by the sequence-matched annotation. The sequence alone, however, does not demonstrate its Fe(2+) specificity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotating Fe(2+)(in) = Fe(2+)(out) as catalytic activity, with experimental evidence code ECO:0000269 citing a 2023 paper. The archived entry also contains this annotation. This supports D for this sequence, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic stretches support a multipass membrane protein, making the transport option more plausible than the listed reactions typical of soluble enzymes. That does not establish that the transported substrate is Fe(2+).",
    "missing_item_specific_fact": "The protein-specific transporter annotation or experimental evidence identifying Fe(2+) transport is needed to distinguish D on substrate identity.",
    "reason": "Sequence topology offers a useful clue toward a transporter, but the precise transport activity is not established by the supplied sequence and choices alone; selecting Fe(2+) depends on a protein-specific fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only listed transport reaction and is supported by the sequence-matched annotation. The sequence alone, however, does not demonstrate its Fe(2+) specificity."
  },
  "important_caveats": [
    "The experimental evidence is reported in a UniProt annotation citing a paper; the paper was not independently assessed.",
    "The reviewer-only database identity and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A077Y877 (DMT1_PLAYE, Plasmodium yoelii Divalent metal transporter 1 / PyDMT1) explicitly lists the catalytic/transporter activity as 'Fe(2+)(in) = Fe(2+)(out)' with experimental evidence (ECO:0000269, PubMed:38049852). The sequence in the question matches the UniProt entry exactly (696 AA, SHA-256 match confirmed in both current and historical records).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains numerous long hydrophobic stretches in the C-terminal ~400 residues forming at least 10-12 transmembrane helices, characteristic of a polytopic membrane transporter. The N-terminal ~200 residues are polar and asparagine-rich (typical of Plasmodium proteins). Among the four choices, A (PRPP synthetase), B (chitinase), and C (methyltransferase) are all soluble enzymes with no membrane-spanning architecture. Only D describes a membrane transport reaction. Identifying the protein as a polytopic membrane transporter from the sequence architecture is a general biological reasoning step that eliminates the three soluble-enzyme distractors.


**Missing item-specific fact**

> The specific identification of the transported ion as Fe(2+) rather than Zn(2+), Mn(2+), or another divalent metal would require NRAMP/DMT-family-specific motif recognition or database lookup. However, since D is the only transporter option among the four choices, the membrane-architecture argument is sufficient to select D.


**Reason**

> The sequence clearly encodes a multi-pass membrane protein (≥10 TM domains), which is incompatible with soluble enzymes (PRPP synthetase, chitinase, methyltransferase). This architectural reasoning meaningfully distinguishes D from A, B, and C. The specific Fe2+ vs. other metal identification is a secondary detail not needed given the choice structure.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (A, B, C) are all soluble enzymes with no transmembrane architecture, making them clearly incompatible with the sequence. D is the only membrane transport reaction. No ambiguity among the choices given the sequence evidence.


### Important caveats

- The specific identification of Fe(2+) as the transported ion (rather than another divalent metal) relies on NRAMP-family knowledge not derivable from generic sequence heuristics alone; however, the choice structure makes this moot since D is the sole transporter option.
- The UniProt annotation for this entry was first publicly released 2025-04-09 with the PubMed reference from 2023; the entry was integrated into Swiss-Prot on 28-Jan-2026. The author's source snapshot is unknown but the sequence and annotation are consistent across versions 38 and 40.
- The N-terminal asparagine-rich region is a hallmark of Plasmodium proteins and aids organism-level recognition but does not by itself specify the transporter's substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic stretches in the C-terminal ~400 residues forming at least 10-12 transmembrane helices, characteristic of a polytopic membrane transporter. The N-terminal ~200 residues are polar and asparagine-rich (typical of Plasmodium proteins). Among the four choices, A (PRPP synthetase), B (chitinase), and C (methyltransferase) are all soluble enzymes with no membrane-spanning architecture. Only D describes a membrane transport reaction. Identifying the protein as a polytopic membrane transporter from the sequence architecture is a general biological reasoning step that eliminates the three soluble-enzyme distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identification of the transported ion as Fe(2+) rather than Zn(2+), Mn(2+), or another divalent metal would require NRAMP/DMT-family-specific motif recognition or database lookup. However, since D is the only transporter option among the four choices, the membrane-architecture argument is sufficient to select D.",
    "reason": "The sequence clearly encodes a multi-pass membrane protein (≥10 TM domains), which is incompatible with soluble enzymes (PRPP synthetase, chitinase, methyltransferase). This architectural reasoning meaningfully distinguishes D from A, B, and C. The specific Fe2+ vs. other metal identification is a secondary detail not needed given the choice structure."
  },
  "case_id": "catalytic_activity_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A077Y877 (DMT1_PLAYE, Plasmodium yoelii Divalent metal transporter 1 / PyDMT1) explicitly lists the catalytic/transporter activity as 'Fe(2+)(in) = Fe(2+)(out)' with experimental evidence (ECO:0000269, PubMed:38049852). The sequence in the question matches the UniProt entry exactly (696 AA, SHA-256 match confirmed in both current and historical records)."
  },
  "important_caveats": [
    "The specific identification of Fe(2+) as the transported ion (rather than another divalent metal) relies on NRAMP-family knowledge not derivable from generic sequence heuristics alone; however, the choice structure makes this moot since D is the sole transporter option.",
    "The UniProt annotation for this entry was first publicly released 2025-04-09 with the PubMed reference from 2023; the entry was integrated into Swiss-Prot on 28-Jan-2026. The author's source snapshot is unknown but the sequence and annotation are consistent across versions 38 and 40.",
    "The N-terminal asparagine-rich region is a hallmark of Plasmodium proteins and aids organism-level recognition but does not by itself specify the transporter's substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (A, B, C) are all soluble enzymes with no transmembrane architecture, making them clearly incompatible with the sequence. D is the only membrane transport reaction. No ambiguity among the choices given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A077Y877 (DMT1_PLAYE, Plasmodium yoelii Divalent metal transporter 1 / PyDMT1) explicitly lists the catalytic/transporter activity as 'Fe(2+)(in) = Fe(2+)(out)' with experimental evidence (ECO:0000269, PubMed:38049852). The sequence in the question matches the UniProt entry exactly (696 AA, SHA-256 match confirmed in both current and historical records).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains numerous long hydrophobic stretches in the C-terminal ~400 residues forming at least 10-12 transmembrane helices, characteristic of a polytopic membrane transporter. The N-terminal ~200 residues are polar and asparagine-rich (typical of Plasmodium proteins). Among the four choices, A (PRPP synthetase), B (chitinase), and C (methyltransferase) are all soluble enzymes with no membrane-spanning architecture. Only D describes a membrane transport reaction. Identifying the protein as a polytopic membrane transporter from the sequence architecture is a general biological reasoning step that eliminates the three soluble-enzyme distractors.",
    "missing_item_specific_fact": "The specific identification of the transported ion as Fe(2+) rather than Zn(2+), Mn(2+), or another divalent metal would require NRAMP/DMT-family-specific motif recognition or database lookup. However, since D is the only transporter option among the four choices, the membrane-architecture argument is sufficient to select D.",
    "reason": "The sequence clearly encodes a multi-pass membrane protein (≥10 TM domains), which is incompatible with soluble enzymes (PRPP synthetase, chitinase, methyltransferase). This architectural reasoning meaningfully distinguishes D from A, B, and C. The specific Fe2+ vs. other metal identification is a secondary detail not needed given the choice structure."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (A, B, C) are all soluble enzymes with no transmembrane architecture, making them clearly incompatible with the sequence. D is the only membrane transport reaction. No ambiguity among the choices given the sequence evidence."
  },
  "important_caveats": [
    "The specific identification of Fe(2+) as the transported ion (rather than another divalent metal) relies on NRAMP-family knowledge not derivable from generic sequence heuristics alone; however, the choice structure makes this moot since D is the sole transporter option.",
    "The UniProt annotation for this entry was first publicly released 2025-04-09 with the PubMed reference from 2023; the entry was integrated into Swiss-Prot on 28-Jan-2026. The author's source snapshot is unknown but the sequence and annotation are consistent across versions 38 and 40.",
    "The N-terminal asparagine-rich region is a hallmark of Plasmodium proteins and aids organism-level recognition but does not by itself specify the transporter's substrate."
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

**Accession:** `A0A077Y877` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
"A0A077Y877"
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8I3M7","source":"UniProtKB"}],"value":"Food vacuole resident transporter 1"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38049852","source":"PubMed"}],"value":"Divalent metal transporter 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38049852","source":"PubMed"}],"value":"PyDMT1"}]}}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38049852","source":"PubMed"}],"name":"Fe(2+)(in) = Fe(2+)(out)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:28486"},{"database":"ChEBI","id":"CHEBI:29033"}]}}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A077Y877.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.473191+00:00.  

```json
{"citation":{"authors":["Zhong M.","Zhou B."],"citationCrossReferences":[{"database":"PubMed","id":"38049852"},{"database":"DOI","id":"10.1186/s12915-023-01776-y"}],"citationType":"journal article","firstPage":"279","id":"38049852","journal":"BMC Biol.","lastPage":"279","publicationDate":"2023","title":"Plasmodium yoelii iron transporter PyDMT1 interacts with host ferritin and is required in full activity for malarial pathogenesis.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","TRANSPORTER ACTIVITY","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `40ae967522d3c49e686d4ca88a1b70ecbe6d0cae59d2d1589a2e894a199b51f8`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
ID   DMT1_PLAYE              Reviewed;         696 AA.
AC   A0A077Y877;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-OCT-2014, sequence version 1.
DT   28-JAN-2026, entry version 38.
DE   RecName: Full=Divalent metal transporter 1 {ECO:0000303|PubMed:38049852};
DE            Short=PyDMT1 {ECO:0000303|PubMed:38049852};
DE   AltName: Full=Food vacuole resident transporter 1 {ECO:0000250|UniProtKB:Q8I3M7};
GN   Name=FVRT1 {ECO:0000250|UniProtKB:Q8I3M7};
GN   ORFNames=PY17X_1241800 {ECO:0000312|EMBL:VTZ80216.1},
GN   PYYM_1241000 {ECO:0000312|EMBL:CDU19580.1};
OS   Plasmodium yoelii.
OC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;
OC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).
OX   NCBI_TaxID=5861 {ECO:0000312|Proteomes:UP000072904};
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
DE   RecName: Full=Divalent metal transporter 1 {ECO:0000303|PubMed:38049852};
DE            Short=PyDMT1 {ECO:0000303|PubMed:38049852};
DE   AltName: Full=Food vacuole resident transporter 1 {ECO:0000250|UniProtKB:Q8I3M7};
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 29-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, TRANSPORTER ACTIVITY, SUBCELLULAR LOCATION, AND DISRUPTION
RP   PHENOTYPE.
RX   PubMed=38049852; DOI=10.1186/s12915-023-01776-y;
RA   Zhong M., Zhou B.;
RT   "Plasmodium yoelii iron transporter PyDMT1 interacts with host ferritin and
RT   is required in full activity for malarial pathogenesis.";
RL   BMC Biol. 21:279-279(2023).
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A077Y877?format=txt&versions=38)  
**Locator:** `lines 40-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:55.877262+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Fe(2+)(in) = Fe(2+)(out); Xref=Rhea:RHEA:28486,
CC         ChEBI:CHEBI:29033; Evidence={ECO:0000269|PubMed:38049852};
```

Source SHA-256: `37d8308df1bef1cc329abc6c16923e33dab13fd5f51df70f00187771ddf50b47`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
