# catalytic_activity_0104

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — 3-oxocapnine + NADPH + H(+) = capnine + NADP(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRYAVVTGVSSGIGKAICEKFLAKGLYVFGSVRKKEDAKYFEEKYPNTFHTLVFDTTDYPAVDKAVEEIHKVVGKKGLSVLVNNAGVAKYGPIQHVPIEELRQQYEVNVFASVYLTQKLLWLLGASKEAKWQGKVIQISSTAGVMTRPMLGPYSSSKHAVEAIYDALRRELMIYGVEVVLIEPGPIKTEIWGKAKSGGNPYKDTDYGEIFAQLDKAVDEIEKIGLPVEAVAGKAWEAFVAKKPKARYVVAPKKLMFKAAMYLIPDRMLDKIFYKDLKKLTQES

[Multiple Choices]
A. 3-oxocapnine + NADPH + H(+) = capnine + NADP(+)
B. vomilenine = perakine
C. spirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2-hydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. 3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
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

> The supplied sequence exactly matches the UniProt record annotated as NADPH-dependent 3-dehydrocapnine reductase, with the catalytic reaction in choice A. The annotation cites experimental evidence (ECO:0000269, PubMed 35414181), though the primary study was not independently assessed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options describe distinct, specific enzyme reactions, but the sequence alone provides no clear general biological argument that identifies the capnine reductase reaction over the others.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental evidence identifying this sequence as a 3-dehydrocapnine reductase.


**Reason**

> Identifying the exact substrate and product requires a protein-specific fact absent from the prompt; recognizing the sequence from a database would be lookup or memorization, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices specify distinct reactions, and the sequence-matched annotation supports choice A.


### Important caveats

- The reviewer-only annotation supports the key but was not supplied to the evaluated model.
- The cited experimental source is identified in the annotation, but its primary results were not independently reviewed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options describe distinct, specific enzyme reactions, but the sequence alone provides no clear general biological argument that identifies the capnine reductase reaction over the others.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence identifying this sequence as a 3-dehydrocapnine reductase.",
    "reason": "Identifying the exact substrate and product requires a protein-specific fact absent from the prompt; recognizing the sequence from a database would be lookup or memorization, not sequence-based reasoning."
  },
  "case_id": "catalytic_activity_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record annotated as NADPH-dependent 3-dehydrocapnine reductase, with the catalytic reaction in choice A. The annotation cites experimental evidence (ECO:0000269, PubMed 35414181), though the primary study was not independently assessed here."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not supplied to the evaluated model.",
    "The cited experimental source is identified in the annotation, but its primary results were not independently reviewed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices specify distinct reactions, and the sequence-matched annotation supports choice A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt record annotated as NADPH-dependent 3-dehydrocapnine reductase, with the catalytic reaction in choice A. The annotation cites experimental evidence (ECO:0000269, PubMed 35414181), though the primary study was not independently assessed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options describe distinct, specific enzyme reactions, but the sequence alone provides no clear general biological argument that identifies the capnine reductase reaction over the others.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental evidence identifying this sequence as a 3-dehydrocapnine reductase.",
    "reason": "Identifying the exact substrate and product requires a protein-specific fact absent from the prompt; recognizing the sequence from a database would be lookup or memorization, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices specify distinct reactions, and the sequence-matched annotation supports choice A."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not supplied to the evaluated model.",
    "The cited experimental source is identified in the annotation, but its primary results were not independently reviewed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A3R5XUE6 (CAPC_ORNRH), which matches the supplied 283-aa sequence exactly (SHA256 match), is annotated as 'NADPH-dependent 3-dehydrocapnine reductase' (EC 1.1.1.-) with the catalytic reaction '3-oxocapnine + NADPH + H(+) = capnine + NADP(+)'. The evidence code ECO:0000269 (inferred from direct assay) cites PubMed:35414181 (Liu et al., Biochemistry 2022), indicating experimental characterization. The historical Swiss-Prot record (entry version 16, released 2026-01-28) contains the same annotation, confirming the key was present before the benchmark cutoff.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region 'GSSGIG' (positions 7–12) resembles the Rossmann-fold GxGxxG nucleotide-binding motif, and the 'SSTAG' segment (~positions 128–132) is consistent with the SDR catalytic 'TGxxxSx' region. The 283-aa length and overall hydrophobic core pattern are compatible with the short-chain dehydrogenase/reductase (SDR) family. Among the four choices, only A is an NADPH-dependent reduction (EC 1.1.1.- oxidoreductase). Choice B is a cofactor-free isomerization (terpene cyclase fold), C requires Fe-S clusters and O2 (carotenoid hydroxylase), and D uses SAM (methyltransferase fold). Recognizing the SDR/Rossmann fold and NADPH cofactor dependency eliminates B, C, and D on cofactor/chemistry-type grounds.


**Missing item-specific fact**

> The specific substrate '3-oxocapnine' and product 'capnine' (a niche sulfonolipid pathway characterized only in 2022) cannot be deduced from sequence alone; however, selecting the correct option among the four does not require naming the substrate—only recognizing the enzyme as an NADPH-dependent oxidoreductase.


**Reason**

> Fold-level recognition (SDR/Rossmann) provides a concrete biological argument that distinguishes the NADPH-dependent reduction (A) from an isomerase (B), an Fe-S/O2 hydroxylase (C), and a SAM methyltransferase (D). While the exact substrate identity is lookup-dependent, the answer can be selected by cofactor and reaction-type elimination without memorizing the capnine pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span distinct enzyme classes (oxidoreductase, isomerase, Fe-S hydroxylase, methyltransferase) with mutually exclusive cofactor requirements. The SDR fold features in the sequence are inconsistent with B, C, and D, leaving A as the only chemically coherent option.


### Important caveats

- The GxGxxG motif match ('GSSGIG') is approximate (GxxGxG pattern) rather than a textbook-perfect SDR signature; fold assignment relies on cumulative sequence context rather than a single unambiguous motif.
- The specific substrate '3-oxocapnine' is an extremely niche sulfonolipid metabolite; no general biological reasoning can name it from sequence alone.
- The UniProt annotation carries ECO:0000269 (direct assay) from a single 2022 publication; no independent replication is noted in the evidence.
- The identity of the UniProt accession was inferred mechanically from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'GSSGIG' (positions 7–12) resembles the Rossmann-fold GxGxxG nucleotide-binding motif, and the 'SSTAG' segment (~positions 128–132) is consistent with the SDR catalytic 'TGxxxSx' region. The 283-aa length and overall hydrophobic core pattern are compatible with the short-chain dehydrogenase/reductase (SDR) family. Among the four choices, only A is an NADPH-dependent reduction (EC 1.1.1.- oxidoreductase). Choice B is a cofactor-free isomerization (terpene cyclase fold), C requires Fe-S clusters and O2 (carotenoid hydroxylase), and D uses SAM (methyltransferase fold). Recognizing the SDR/Rossmann fold and NADPH cofactor dependency eliminates B, C, and D on cofactor/chemistry-type grounds.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate '3-oxocapnine' and product 'capnine' (a niche sulfonolipid pathway characterized only in 2022) cannot be deduced from sequence alone; however, selecting the correct option among the four does not require naming the substrate—only recognizing the enzyme as an NADPH-dependent oxidoreductase.",
    "reason": "Fold-level recognition (SDR/Rossmann) provides a concrete biological argument that distinguishes the NADPH-dependent reduction (A) from an isomerase (B), an Fe-S/O2 hydroxylase (C), and a SAM methyltransferase (D). While the exact substrate identity is lookup-dependent, the answer can be selected by cofactor and reaction-type elimination without memorizing the capnine pathway."
  },
  "case_id": "catalytic_activity_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A3R5XUE6 (CAPC_ORNRH), which matches the supplied 283-aa sequence exactly (SHA256 match), is annotated as 'NADPH-dependent 3-dehydrocapnine reductase' (EC 1.1.1.-) with the catalytic reaction '3-oxocapnine + NADPH + H(+) = capnine + NADP(+)'. The evidence code ECO:0000269 (inferred from direct assay) cites PubMed:35414181 (Liu et al., Biochemistry 2022), indicating experimental characterization. The historical Swiss-Prot record (entry version 16, released 2026-01-28) contains the same annotation, confirming the key was present before the benchmark cutoff."
  },
  "important_caveats": [
    "The GxGxxG motif match ('GSSGIG') is approximate (GxxGxG pattern) rather than a textbook-perfect SDR signature; fold assignment relies on cumulative sequence context rather than a single unambiguous motif.",
    "The specific substrate '3-oxocapnine' is an extremely niche sulfonolipid metabolite; no general biological reasoning can name it from sequence alone.",
    "The UniProt annotation carries ECO:0000269 (direct assay) from a single 2022 publication; no independent replication is noted in the evidence.",
    "The identity of the UniProt accession was inferred mechanically from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span distinct enzyme classes (oxidoreductase, isomerase, Fe-S hydroxylase, methyltransferase) with mutually exclusive cofactor requirements. The SDR fold features in the sequence are inconsistent with B, C, and D, leaving A as the only chemically coherent option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A3R5XUE6 (CAPC_ORNRH), which matches the supplied 283-aa sequence exactly (SHA256 match), is annotated as 'NADPH-dependent 3-dehydrocapnine reductase' (EC 1.1.1.-) with the catalytic reaction '3-oxocapnine + NADPH + H(+) = capnine + NADP(+)'. The evidence code ECO:0000269 (inferred from direct assay) cites PubMed:35414181 (Liu et al., Biochemistry 2022), indicating experimental characterization. The historical Swiss-Prot record (entry version 16, released 2026-01-28) contains the same annotation, confirming the key was present before the benchmark cutoff.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region 'GSSGIG' (positions 7–12) resembles the Rossmann-fold GxGxxG nucleotide-binding motif, and the 'SSTAG' segment (~positions 128–132) is consistent with the SDR catalytic 'TGxxxSx' region. The 283-aa length and overall hydrophobic core pattern are compatible with the short-chain dehydrogenase/reductase (SDR) family. Among the four choices, only A is an NADPH-dependent reduction (EC 1.1.1.- oxidoreductase). Choice B is a cofactor-free isomerization (terpene cyclase fold), C requires Fe-S clusters and O2 (carotenoid hydroxylase), and D uses SAM (methyltransferase fold). Recognizing the SDR/Rossmann fold and NADPH cofactor dependency eliminates B, C, and D on cofactor/chemistry-type grounds.",
    "missing_item_specific_fact": "The specific substrate '3-oxocapnine' and product 'capnine' (a niche sulfonolipid pathway characterized only in 2022) cannot be deduced from sequence alone; however, selecting the correct option among the four does not require naming the substrate—only recognizing the enzyme as an NADPH-dependent oxidoreductase.",
    "reason": "Fold-level recognition (SDR/Rossmann) provides a concrete biological argument that distinguishes the NADPH-dependent reduction (A) from an isomerase (B), an Fe-S/O2 hydroxylase (C), and a SAM methyltransferase (D). While the exact substrate identity is lookup-dependent, the answer can be selected by cofactor and reaction-type elimination without memorizing the capnine pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span distinct enzyme classes (oxidoreductase, isomerase, Fe-S hydroxylase, methyltransferase) with mutually exclusive cofactor requirements. The SDR fold features in the sequence are inconsistent with B, C, and D, leaving A as the only chemically coherent option."
  },
  "important_caveats": [
    "The GxGxxG motif match ('GSSGIG') is approximate (GxxGxG pattern) rather than a textbook-perfect SDR signature; fold assignment relies on cumulative sequence context rather than a single unambiguous motif.",
    "The specific substrate '3-oxocapnine' is an extremely niche sulfonolipid metabolite; no general biological reasoning can name it from sequence alone.",
    "The UniProt annotation carries ECO:0000269 (direct assay) from a single 2022 publication; no independent replication is noted in the evidence.",
    "The identity of the UniProt accession was inferred mechanically from dataset metadata and was not provided to the evaluated model."
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

**Accession:** `A0A3R5XUE6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 16. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.269818+00:00.  

```json
"A0A3R5XUE6"
```

Source SHA-256: `eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.269818+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35414181","source":"PubMed"}],"value":"1.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35414181","source":"PubMed"}],"value":"NADPH-dependent 3-dehydrocapnine reductase"}}}
```

Source SHA-256: `eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.269818+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"35414181","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81576"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"35414181","source":"PubMed"}],"name":"3-oxocapnine + NADPH + H(+) = capnine + NADP(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81575"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:231947"},{"database":"ChEBI","id":"CHEBI:231953"}]}}
```

Source SHA-256: `eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.269818+00:00.  

```json
{"citation":{"authors":["Liu Y.","Wei Y.","Teh T.M.","Liu D.","Zhou Y.","Zhao S.","Ang E.L.","Zhao H.","Zhang Y."],"citationCrossReferences":[{"database":"PubMed","id":"35414181"},{"database":"DOI","id":"10.1021/acs.biochem.2c00102"}],"citationType":"journal article","firstPage":"2861","id":"35414181","journal":"Biochemistry","lastPage":"2869","publicationDate":"2022","title":"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.","volume":"61"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:30.826829+00:00.  

```text
ID   CAPC_ORNRH              Reviewed;         283 AA.
AC   A0A3R5XUE6;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-APR-2019, sequence version 1.
DT   28-JAN-2026, entry version 16.
DE   RecName: Full=NADPH-dependent 3-dehydrocapnine reductase {ECO:0000303|PubMed:35414181};
DE            EC=1.1.1.- {ECO:0000269|PubMed:35414181};
GN   Name=capC {ECO:0000303|PubMed:35414181};
GN   ORFNames=EQP59_04780 {ECO:0000312|EMBL:QAR30703.1};
OS   Ornithobacterium rhinotracheale.
OC   Bacteria; Pseudomonadati; Bacteroidota; Flavobacteriia; Flavobacteriales;
OC   Weeksellaceae; Ornithobacterium.
OX   NCBI_TaxID=28251;
```

Source SHA-256: `6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:30.826829+00:00.  

```text
DE   RecName: Full=NADPH-dependent 3-dehydrocapnine reductase {ECO:0000303|PubMed:35414181};
DE            EC=1.1.1.- {ECO:0000269|PubMed:35414181};
```

Source SHA-256: `6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:30.826829+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=3-oxocapnine + NADPH + H(+) = capnine + NADP(+);
CC         Xref=Rhea:RHEA:81575, ChEBI:CHEBI:15378, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:231947, ChEBI:CHEBI:231953;
CC         Evidence={ECO:0000269|PubMed:35414181};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81576;
CC         Evidence={ECO:0000269|PubMed:35414181};
```

Source SHA-256: `6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 104. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
