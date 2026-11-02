# active_site_0139

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **D** — Position 268 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDKKEVQHHRSQQAMTKSLYAIGMGLLGKSATNMDCANTNLESAGKSSSTNYNRNRFYNERFVPMASGTMPSVSGTNHHSRHQQLLLQQAPKCTADLNEKLVKINRQNANKELSTIQAKDMQSVDKNEEALKELQESIPEINKIFDVHCRIGSGTFSTVLLGTLQRERGLVETQRRRFAIKHHNPTNHPERILRELECMYRIGGVENVIGINCCIRYNDNVAFIMPYMTHDRFHDIYRSLNFPEIRDYLRNLLIALRHVHKFNVIHRDVKPSNILYNRRTGKFLLCDFGLAQRIADDGSVVQSSDLSSREVFSILRDLENGRSVTLTDGNSAQAEAEDYMARRRMRALGGGGSVERAVTGPPSIQKLREQAGGHLTKKDVANQRADTMRLLNRLRLVSPNADPNNYVVSTNTSKKEMHASRAGTPGYRPPEVLLRYPKQSTAVDVWAAGVIMLSLLSGLHPFFKAPHDCGALAEIINLFGDMPVRKTAFLLDRLILLAQKVNTLDLRRVCMRFRHADFFLAPEIQRKYQRPDGTTEMCRSCEQPTFNCLCSNSGHNLERYDGLDIFPAVAYDLLSRLLEVNPQKRITAEEALKHPFFSDQHRITPGIPLHQQQLIMHQQQHIMQHQQHLQRSRETLPSSAARTLKAFVCYPMEITSTASQAAGNI

[Multiple Choices]
A. Position 511 (Proton acceptor)
B. Position 266 (Proton acceptor)
C. Position 376 (Proton acceptor)
D. Position 268 (Proton acceptor)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt record, whose current and historical annotations identify residue 268 as the proton-accepting active-site residue. The annotation is supported by PROSITE-ProRule computational evidence, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conserved HRD catalytic-loop motif characteristic of protein kinases. Its Asp is the catalytic proton acceptor; this distinguishes the Asp at position 268 from nearby candidate positions.


**Missing item-specific fact**

> No item-specific fact is required for the motif-based inference, though the precise residue annotation is independently confirmed by the reviewer-only UniProt record.


**Reason**

> The sequence’s kinase motif and the choices provide a concrete biological basis for selecting the catalytic Asp, rather than requiring recognition of the exact protein or recall of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The conserved kinase catalytic-loop Asp supports position 268; the neighboring listed positions do not denote that Asp.


### Important caveats

- The cited active-site annotation is computationally assigned by PROSITE-ProRule; the supplied evidence does not establish direct experimental validation.
- The exact sequence matches both current and historical UniProt records, but the author’s precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved HRD catalytic-loop motif characteristic of protein kinases. Its Asp is the catalytic proton acceptor; this distinguishes the Asp at position 268 from nearby candidate positions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is required for the motif-based inference, though the precise residue annotation is independently confirmed by the reviewer-only UniProt record.",
    "reason": "The sequence’s kinase motif and the choices provide a concrete biological basis for selecting the catalytic Asp, rather than requiring recognition of the exact protein or recall of a database entry."
  },
  "case_id": "active_site_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, whose current and historical annotations identify residue 268 as the proton-accepting active-site residue. The annotation is supported by PROSITE-ProRule computational evidence, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The cited active-site annotation is computationally assigned by PROSITE-ProRule; the supplied evidence does not establish direct experimental validation.",
    "The exact sequence matches both current and historical UniProt records, but the author’s precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved kinase catalytic-loop Asp supports position 268; the neighboring listed positions do not denote that Asp."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, whose current and historical annotations identify residue 268 as the proton-accepting active-site residue. The annotation is supported by PROSITE-ProRule computational evidence, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conserved HRD catalytic-loop motif characteristic of protein kinases. Its Asp is the catalytic proton acceptor; this distinguishes the Asp at position 268 from nearby candidate positions.",
    "missing_item_specific_fact": "No item-specific fact is required for the motif-based inference, though the precise residue annotation is independently confirmed by the reviewer-only UniProt record.",
    "reason": "The sequence’s kinase motif and the choices provide a concrete biological basis for selecting the catalytic Asp, rather than requiring recognition of the exact protein or recall of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved kinase catalytic-loop Asp supports position 268; the neighboring listed positions do not denote that Asp."
  },
  "important_caveats": [
    "The cited active-site annotation is computationally assigned by PROSITE-ProRule; the supplied evidence does not establish direct experimental validation.",
    "The exact sequence matches both current and historical UniProt records, but the author’s precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q9VJ90 (CDC7B_DROME, a Drosophila non-specific serine/threonine protein kinase, EC 2.7.11.1) explicitly annotates position 268 as 'Proton acceptor' (Active site type), consistent across both the current entry (C5) and the archived entry (H2). The sequence at positions 266-268 is H-R-D, the canonical HRD catalytic motif of protein kinases, where the aspartate (D268) is the well-established proton acceptor. The annotation evidence code is ECO:0000255 (PROSITE-ProRule), a curated/computational assignment, but the HRD aspartate proton-acceptor role is supported by extensive experimental biochemistry across the kinase superfamily. The sequence match is confirmed (SHA-256 identical between benchmark and source).

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2), [C4](#evidence-c4), [C1](#evidence-c1), [C3](#evidence-c3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is identifiable as a protein kinase from multiple conserved sequence features: the glycine-rich loop (GXGXXG around residues 151-159: 'GSGTFSTVL'), the VAIK catalytic lysine region (~171-175), the HRD catalytic motif (H266-R267-D268), and the DFG metal-binding motif (D287-F288-G289 in 'CDFGLAQR'). The HRD motif is one of the most universally conserved and well-characterized features of the protein kinase fold. Its aspartate (the 'D' in HRD) is the catalytic proton acceptor in essentially all active protein kinases. A model with general kinase biochemistry knowledge can locate the HRD motif in the sequence, identify D268 as the aspartate, and select it as the proton acceptor. Position 266 (the H of HRD) is a plausible but incorrect distractor; positions 376 (T) and 511 (M) are not in any catalytic motif.


**Missing item-specific fact**

> None critical. The question is answerable from general protein kinase catalytic mechanism knowledge and motif identification in the supplied sequence.


**Reason**

> The HRD motif and the proton-acceptor role of its aspartate are textbook kinase biochemistry, not an obscure item-specific annotation. The sequence contains recognizable kinase landmarks (Gly-rich loop, VAIK, HRD, DFG) that allow a knowledgeable model to locate the catalytic center without memorizing this particular protein's database entry. The distractor at 266 (histidine of HRD) tests whether the model knows the D rather than the H is the proton acceptor, which is standard mechanistic knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 268 (the aspartate of the HRD motif) is the proton acceptor. Position 266 is the histidine of HRD (not the proton acceptor), position 376 is a threonine outside any catalytic motif, and position 511 is a methionine also outside any catalytic motif. The choices are well-distinguished for a model that recognizes the kinase fold.


### Important caveats

- The UniProt annotation uses ECO:0000255 (PROSITE-ProRule), a curated computational assignment rather than a direct experimental measurement for this specific protein. However, the HRD-aspartate proton-acceptor role is supported by extensive experimental evidence across the kinase superfamily.
- The sequence is 665 AA and matches the canonical Q9VJ90 entry exactly (SHA-256 confirmed); no isoform or construct numbering issues arise.
- The identity of the protein (CDC7B_DROME) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.
- The annotation has been stable across entry versions (v211 archived and v213 current both show ACT_SITE 268).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is identifiable as a protein kinase from multiple conserved sequence features: the glycine-rich loop (GXGXXG around residues 151-159: 'GSGTFSTVL'), the VAIK catalytic lysine region (~171-175), the HRD catalytic motif (H266-R267-D268), and the DFG metal-binding motif (D287-F288-G289 in 'CDFGLAQR'). The HRD motif is one of the most universally conserved and well-characterized features of the protein kinase fold. Its aspartate (the 'D' in HRD) is the catalytic proton acceptor in essentially all active protein kinases. A model with general kinase biochemistry knowledge can locate the HRD motif in the sequence, identify D268 as the aspartate, and select it as the proton acceptor. Position 266 (the H of HRD) is a plausible but incorrect distractor; positions 376 (T) and 511 (M) are not in any catalytic motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The question is answerable from general protein kinase catalytic mechanism knowledge and motif identification in the supplied sequence.",
    "reason": "The HRD motif and the proton-acceptor role of its aspartate are textbook kinase biochemistry, not an obscure item-specific annotation. The sequence contains recognizable kinase landmarks (Gly-rich loop, VAIK, HRD, DFG) that allow a knowledgeable model to locate the catalytic center without memorizing this particular protein's database entry. The distractor at 266 (histidine of HRD) tests whether the model knows the D rather than the H is the proton acceptor, which is standard mechanistic knowledge."
  },
  "case_id": "active_site_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2",
      "C4",
      "C1",
      "C3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9VJ90 (CDC7B_DROME, a Drosophila non-specific serine/threonine protein kinase, EC 2.7.11.1) explicitly annotates position 268 as 'Proton acceptor' (Active site type), consistent across both the current entry (C5) and the archived entry (H2). The sequence at positions 266-268 is H-R-D, the canonical HRD catalytic motif of protein kinases, where the aspartate (D268) is the well-established proton acceptor. The annotation evidence code is ECO:0000255 (PROSITE-ProRule), a curated/computational assignment, but the HRD aspartate proton-acceptor role is supported by extensive experimental biochemistry across the kinase superfamily. The sequence match is confirmed (SHA-256 identical between benchmark and source)."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000255 (PROSITE-ProRule), a curated computational assignment rather than a direct experimental measurement for this specific protein. However, the HRD-aspartate proton-acceptor role is supported by extensive experimental evidence across the kinase superfamily.",
    "The sequence is 665 AA and matches the canonical Q9VJ90 entry exactly (SHA-256 confirmed); no isoform or construct numbering issues arise.",
    "The identity of the protein (CDC7B_DROME) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.",
    "The annotation has been stable across entry versions (v211 archived and v213 current both show ACT_SITE 268)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 268 (the aspartate of the HRD motif) is the proton acceptor. Position 266 is the histidine of HRD (not the proton acceptor), position 376 is a threonine outside any catalytic motif, and position 511 is a methionine also outside any catalytic motif. The choices are well-distinguished for a model that recognizes the kinase fold."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9VJ90 (CDC7B_DROME, a Drosophila non-specific serine/threonine protein kinase, EC 2.7.11.1) explicitly annotates position 268 as 'Proton acceptor' (Active site type), consistent across both the current entry (C5) and the archived entry (H2). The sequence at positions 266-268 is H-R-D, the canonical HRD catalytic motif of protein kinases, where the aspartate (D268) is the well-established proton acceptor. The annotation evidence code is ECO:0000255 (PROSITE-ProRule), a curated/computational assignment, but the HRD aspartate proton-acceptor role is supported by extensive experimental biochemistry across the kinase superfamily. The sequence match is confirmed (SHA-256 identical between benchmark and source).",
    "evidence_ids": ["C5", "H2", "C4", "C1", "C3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is identifiable as a protein kinase from multiple conserved sequence features: the glycine-rich loop (GXGXXG around residues 151-159: 'GSGTFSTVL'), the VAIK catalytic lysine region (~171-175), the HRD catalytic motif (H266-R267-D268), and the DFG metal-binding motif (D287-F288-G289 in 'CDFGLAQR'). The HRD motif is one of the most universally conserved and well-characterized features of the protein kinase fold. Its aspartate (the 'D' in HRD) is the catalytic proton acceptor in essentially all active protein kinases. A model with general kinase biochemistry knowledge can locate the HRD motif in the sequence, identify D268 as the aspartate, and select it as the proton acceptor. Position 266 (the H of HRD) is a plausible but incorrect distractor; positions 376 (T) and 511 (M) are not in any catalytic motif.",
    "missing_item_specific_fact": "None critical. The question is answerable from general protein kinase catalytic mechanism knowledge and motif identification in the supplied sequence.",
    "reason": "The HRD motif and the proton-acceptor role of its aspartate are textbook kinase biochemistry, not an obscure item-specific annotation. The sequence contains recognizable kinase landmarks (Gly-rich loop, VAIK, HRD, DFG) that allow a knowledgeable model to locate the catalytic center without memorizing this particular protein's database entry. The distractor at 266 (histidine of HRD) tests whether the model knows the D rather than the H is the proton acceptor, which is standard mechanistic knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 268 (the aspartate of the HRD motif) is the proton acceptor. Position 266 is the histidine of HRD (not the proton acceptor), position 376 is a threonine outside any catalytic motif, and position 511 is a methionine also outside any catalytic motif. The choices are well-distinguished for a model that recognizes the kinase fold."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000255 (PROSITE-ProRule), a curated computational assignment rather than a direct experimental measurement for this specific protein. However, the HRD-aspartate proton-acceptor role is supported by extensive experimental evidence across the kinase superfamily.",
    "The sequence is 665 AA and matches the canonical Q9VJ90 entry exactly (SHA-256 confirmed); no isoform or construct numbering issues arise.",
    "The identity of the protein (CDC7B_DROME) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from sequence alone.",
    "The annotation has been stable across entry versions (v211 archived and v213 current both show ACT_SITE 268)."
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

**Accession:** `Q9VJ90` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 211. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
"Q9VJ90"
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"commonName":"Fruit fly","evidences":[{"evidenceCode":"ECO:0000312","id":"UP000000803","source":"Proteomes"}],"lineage":["Eukaryota","Metazoa","Ecdysozoa","Arthropoda","Altocrustacea","Allotriocarida","Hexapoda","Insecta","Pterygota","Neoptera","Eumetabola","Endopterygota","Aparaglossata","Panorpida","Diptera","Brachycera","Muscomorpha","Ephydroidea","Drosophilidae","Drosophila","Sophophora"],"scientificName":"Drosophila melanogaster","taxonId":7227}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0032677","source":"FlyBase"}],"value":"non-specific serine/threonine protein kinase"}}}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ90.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:29.717422+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":268},"start":{"modifier":"EXACT","value":268}},"type":"Active site"}
```

Source SHA-256: `177914c48338430696a74cf52e87b7f49f48b4ca32de82ca011e5b54aee3f781`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
ID   CDC7B_DROME             Reviewed;         665 AA.
AC   Q9VJ90; Q8T0Q5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 211.
DE   RecName: Full=non-specific serine/threonine protein kinase {ECO:0000312|FlyBase:FBgn0032677};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
GN   ORFNames=CG5790 {ECO:0000312|FlyBase:FBgn0032677};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ90?format=txt&versions=211)  
**Locator:** `lines 173-176`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 211 / 1.  
**Retrieved:** 2026-11-01T06:28:52.103896+00:00.  

```text
FT   ACT_SITE        268
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159,
FT                   ECO:0000255|PROSITE-ProRule:PRU10027"
```

Source SHA-256: `c1962f875faa59cf2daf56603e62eda0a032d31878e9736a7a26d2867f81dd54`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 139. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
