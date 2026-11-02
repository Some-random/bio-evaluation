# pathway_0107

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Lipid metabolism. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKDLFEHIYANKGSIGRWSDHAEGYYVFPKLEGELGPHMKFQGKEILNWSINDYLGLANHPEVRKVDAEAAAEYGAAYPMGARMMSGHTTMHEELEKRLAKFVHKEASYLLNFGYQGMVSIIDALVTKNDVIVYDVDAHACIIDGVRLHFGKRYTYQHNDMESFEKNLERAAKLAETTGGGILVISEGVFGMRGEQGKLKEIVALKKKYPFRLLVDDAHGFGTLGPRGEGTGVHQGVQDEIDVYFSTFAKSMAGIGAFVAGNAKVVDYLKYNLRSQMFAKSLPMIYVKGALKRLEMMETMPELQQKLWDNVNRLQNGLKERGFNIGNTNTCVTPVFLHGSIPEAMAMVNDLREHYGIFLSIVVYPVIPKGMILLRIIPTASHSKEDIDRTLEAFSAIREKLETGVYRAINAELTKEMGDM

[Multiple Choices]
A. Lipid metabolism. .
B. Carbohydrate degradation
C. terpenoid biosynthesis. .
D. L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as cysteate-C-fatty acyltransferase, with its pathway listed as lipid metabolism. The annotation cites a 2022 study on capnine biosynthesis, supporting choice A for this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a soluble enzyme-like protein, but the supplied sequence and choices do not provide a specific, reliable clue that identifies its substrate or pathway.


**Missing item-specific fact**

> The protein-specific function—cysteate-C-fatty acyltransferase in lipid metabolism—is needed to distinguish choice A.


**Reason**

> Choosing the annotated pathway depends on knowing this protein’s identity or experimentally characterized function; recognizing the exact sequence or relying on generic sequence heuristics would not constitute reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence pathway annotation supports lipid metabolism; the other options are not supported by the supplied sequence-level evidence.


### Important caveats

- The pathway annotation is a database assertion citing a publication, not itself a direct experimental measurement.
- The actual author source snapshot is unknown, although the sequence matches both the archived and current entries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble enzyme-like protein, but the supplied sequence and choices do not provide a specific, reliable clue that identifies its substrate or pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific function—cysteate-C-fatty acyltransferase in lipid metabolism—is needed to distinguish choice A.",
    "reason": "Choosing the annotated pathway depends on knowing this protein’s identity or experimentally characterized function; recognizing the exact sequence or relying on generic sequence heuristics would not constitute reasoning from the supplied input."
  },
  "case_id": "pathway_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as cysteate-C-fatty acyltransferase, with its pathway listed as lipid metabolism. The annotation cites a 2022 study on capnine biosynthesis, supporting choice A for this protein."
  },
  "important_caveats": [
    "The pathway annotation is a database assertion citing a publication, not itself a direct experimental measurement.",
    "The actual author source snapshot is unknown, although the sequence matches both the archived and current entries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence pathway annotation supports lipid metabolism; the other options are not supported by the supplied sequence-level evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as cysteate-C-fatty acyltransferase, with its pathway listed as lipid metabolism. The annotation cites a 2022 study on capnine biosynthesis, supporting choice A for this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a soluble enzyme-like protein, but the supplied sequence and choices do not provide a specific, reliable clue that identifies its substrate or pathway.",
    "missing_item_specific_fact": "The protein-specific function—cysteate-C-fatty acyltransferase in lipid metabolism—is needed to distinguish choice A.",
    "reason": "Choosing the annotated pathway depends on knowing this protein’s identity or experimentally characterized function; recognizing the exact sequence or relying on generic sequence heuristics would not constitute reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence pathway annotation supports lipid metabolism; the other options are not supported by the supplied sequence-level evidence."
  },
  "important_caveats": [
    "The pathway annotation is a database assertion citing a publication, not itself a direct experimental measurement.",
    "The actual author source snapshot is unknown, although the sequence matches both the archived and current entries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation for C7M8J6 (Cysteate-C-fatty acyltransferase, EC 2.3.1.-) explicitly lists 'PATHWAY: Lipid metabolism' (evidence code ECO:0000305, PubMed:35414181). The protein catalyzes fatty acyl transfer in sulfonolipid capnine biosynthesis, confirmed experimentally in the 2022 Biochemistry paper by Liu et al. The EC class 2.3.1 (acyltransferases) and the fatty-acyl transfer reaction are consistent with lipid metabolism.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains motifs loosely resembling acyltransferase domains (e.g., the 'GGILVISEGVFGMRGEQGKLKEIVALKKK' region), which could weakly suggest transferase activity. However, acyltransferases participate in many pathways (amino acid modification, secondary metabolism, lipid metabolism), so this alone does not uniquely point to 'Lipid metabolism' over the other three choices. Eliminating carbohydrate degradation, terpenoid biosynthesis, and histidine biosynthesis requires knowing this is specifically a cysteate-C-fatty acyltransferase in the sulfonolipid capnine biosynthetic pathway.


**Missing item-specific fact**

> The specific identity of this protein as Cysteate-C-fatty acyltransferase (CapB) in the sulfonolipid capnine biosynthetic pathway of Capnocytophaga ochracea, and its UniProt pathway assignment to 'Lipid metabolism.' This is a highly specialized, recently characterized enzyme (Swiss-Prot entry first public 2025-04-09) whose pathway annotation rests on a single 2022 experimental study.


**Reason**

> While the sequence has faint acyltransferase-like features, the leap from 'possibly an acyltransferase' to the broad pathway category 'Lipid metabolism' (as opposed to, say, amino acid metabolism or secondary metabolite biosynthesis) requires the specific item-level knowledge that this enzyme transfers a fatty acyl group onto cysteate to build a sulfonolipid. Without recognizing the exact protein or having prior knowledge of capnine biosynthesis, general sequence reasoning cannot reliably distinguish option A from B, C, or D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct metabolic categories (lipid, carbohydrate, terpenoid, amino acid biosynthesis). Given the correct protein identity, only 'Lipid metabolism' is defensible. No ambiguity among options once the protein is identified.


### Important caveats

- The UniProt Swiss-Prot entry for C7M8J6 was first publicly released on 2025-04-09, making it very recent. The pathway annotation (ECO:0000305) indicates it was curated based on the 2022 experimental paper rather than being an inferred or transferred annotation.
- The EC number is incomplete (2.3.1.-), indicating the exact substrate specificity classification is still being refined.
- Sulfonolipid biosynthesis is a niche pathway primarily studied in Capnocytophaga and a few other Bacteroidota; the broad 'Lipid metabolism' UniProt pathway label may not be intuitive from sequence alone.
- The reviewer-only evidence confirms sequence match (SHA-256 identical, 420 AA) between the benchmark sequence and the UniProt entry, so the annotation applies to the exact sequence presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs loosely resembling acyltransferase domains (e.g., the 'GGILVISEGVFGMRGEQGKLKEIVALKKK' region), which could weakly suggest transferase activity. However, acyltransferases participate in many pathways (amino acid modification, secondary metabolism, lipid metabolism), so this alone does not uniquely point to 'Lipid metabolism' over the other three choices. Eliminating carbohydrate degradation, terpenoid biosynthesis, and histidine biosynthesis requires knowing this is specifically a cysteate-C-fatty acyltransferase in the sulfonolipid capnine biosynthetic pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as Cysteate-C-fatty acyltransferase (CapB) in the sulfonolipid capnine biosynthetic pathway of Capnocytophaga ochracea, and its UniProt pathway assignment to 'Lipid metabolism.' This is a highly specialized, recently characterized enzyme (Swiss-Prot entry first public 2025-04-09) whose pathway annotation rests on a single 2022 experimental study.",
    "reason": "While the sequence has faint acyltransferase-like features, the leap from 'possibly an acyltransferase' to the broad pathway category 'Lipid metabolism' (as opposed to, say, amino acid metabolism or secondary metabolite biosynthesis) requires the specific item-level knowledge that this enzyme transfers a fatty acyl group onto cysteate to build a sulfonolipid. Without recognizing the exact protein or having prior knowledge of capnine biosynthesis, general sequence reasoning cannot reliably distinguish option A from B, C, or D."
  },
  "case_id": "pathway_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation for C7M8J6 (Cysteate-C-fatty acyltransferase, EC 2.3.1.-) explicitly lists 'PATHWAY: Lipid metabolism' (evidence code ECO:0000305, PubMed:35414181). The protein catalyzes fatty acyl transfer in sulfonolipid capnine biosynthesis, confirmed experimentally in the 2022 Biochemistry paper by Liu et al. The EC class 2.3.1 (acyltransferases) and the fatty-acyl transfer reaction are consistent with lipid metabolism."
  },
  "important_caveats": [
    "The UniProt Swiss-Prot entry for C7M8J6 was first publicly released on 2025-04-09, making it very recent. The pathway annotation (ECO:0000305) indicates it was curated based on the 2022 experimental paper rather than being an inferred or transferred annotation.",
    "The EC number is incomplete (2.3.1.-), indicating the exact substrate specificity classification is still being refined.",
    "Sulfonolipid biosynthesis is a niche pathway primarily studied in Capnocytophaga and a few other Bacteroidota; the broad 'Lipid metabolism' UniProt pathway label may not be intuitive from sequence alone.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical, 420 AA) between the benchmark sequence and the UniProt entry, so the annotation applies to the exact sequence presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct metabolic categories (lipid, carbohydrate, terpenoid, amino acid biosynthesis). Given the correct protein identity, only 'Lipid metabolism' is defensible. No ambiguity among options once the protein is identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation for C7M8J6 (Cysteate-C-fatty acyltransferase, EC 2.3.1.-) explicitly lists 'PATHWAY: Lipid metabolism' (evidence code ECO:0000305, PubMed:35414181). The protein catalyzes fatty acyl transfer in sulfonolipid capnine biosynthesis, confirmed experimentally in the 2022 Biochemistry paper by Liu et al. The EC class 2.3.1 (acyltransferases) and the fatty-acyl transfer reaction are consistent with lipid metabolism.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains motifs loosely resembling acyltransferase domains (e.g., the 'GGILVISEGVFGMRGEQGKLKEIVALKKK' region), which could weakly suggest transferase activity. However, acyltransferases participate in many pathways (amino acid modification, secondary metabolism, lipid metabolism), so this alone does not uniquely point to 'Lipid metabolism' over the other three choices. Eliminating carbohydrate degradation, terpenoid biosynthesis, and histidine biosynthesis requires knowing this is specifically a cysteate-C-fatty acyltransferase in the sulfonolipid capnine biosynthetic pathway.",
    "missing_item_specific_fact": "The specific identity of this protein as Cysteate-C-fatty acyltransferase (CapB) in the sulfonolipid capnine biosynthetic pathway of Capnocytophaga ochracea, and its UniProt pathway assignment to 'Lipid metabolism.' This is a highly specialized, recently characterized enzyme (Swiss-Prot entry first public 2025-04-09) whose pathway annotation rests on a single 2022 experimental study.",
    "reason": "While the sequence has faint acyltransferase-like features, the leap from 'possibly an acyltransferase' to the broad pathway category 'Lipid metabolism' (as opposed to, say, amino acid metabolism or secondary metabolite biosynthesis) requires the specific item-level knowledge that this enzyme transfers a fatty acyl group onto cysteate to build a sulfonolipid. Without recognizing the exact protein or having prior knowledge of capnine biosynthesis, general sequence reasoning cannot reliably distinguish option A from B, C, or D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct metabolic categories (lipid, carbohydrate, terpenoid, amino acid biosynthesis). Given the correct protein identity, only 'Lipid metabolism' is defensible. No ambiguity among options once the protein is identified."
  },
  "important_caveats": [
    "The UniProt Swiss-Prot entry for C7M8J6 was first publicly released on 2025-04-09, making it very recent. The pathway annotation (ECO:0000305) indicates it was curated based on the 2022 experimental paper rather than being an inferred or transferred annotation.",
    "The EC number is incomplete (2.3.1.-), indicating the exact substrate specificity classification is still being refined.",
    "Sulfonolipid biosynthesis is a niche pathway primarily studied in Capnocytophaga and a few other Bacteroidota; the broad 'Lipid metabolism' UniProt pathway label may not be intuitive from sequence alone.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical, 420 AA) between the benchmark sequence and the UniProt entry, so the annotation applies to the exact sequence presented."
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

**Accession:** `C7M8J6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 70. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:36.271476+00:00.  

```json
"C7M8J6"
```

Source SHA-256: `b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:36.271476+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35414181","source":"PubMed"}],"value":"2.3.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35414181","source":"PubMed"}],"value":"Cysteate-C-fatty acyltransferase"}}}
```

Source SHA-256: `b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:36.271476+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"35414181","source":"PubMed"}],"value":"Lipid metabolism"}]}
```

Source SHA-256: `b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:36.271476+00:00.  

```json
{"citation":{"authors":["Liu Y.","Wei Y.","Teh T.M.","Liu D.","Zhou Y.","Zhao S.","Ang E.L.","Zhao H.","Zhang Y."],"citationCrossReferences":[{"database":"PubMed","id":"35414181"},{"database":"DOI","id":"10.1021/acs.biochem.2c00102"}],"citationType":"journal article","firstPage":"2861","id":"35414181","journal":"Biochemistry","lastPage":"2869","publicationDate":"2022","title":"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.","volume":"61"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR"]}
```

Source SHA-256: `b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:41.947109+00:00.  

```text
ID   CAPB_CAPOD              Reviewed;         420 AA.
AC   C7M8J6;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-OCT-2009, sequence version 1.
DT   28-JAN-2026, entry version 70.
DE   RecName: Full=Cysteate-C-fatty acyltransferase {ECO:0000303|PubMed:35414181};
DE            EC=2.3.1.- {ECO:0000269|PubMed:35414181};
GN   Name=capB {ECO:0000303|PubMed:35414181};
GN   OrderedLocusNames=Coch_1830 {ECO:0000312|EMBL:ACU93375.1};
OS   Capnocytophaga ochracea (strain ATCC 27872 / DSM 7271 / CCUG 9716 / JCM
OS   12966 / NCTC 12371 / SS31 / VPI 2845) (Bacteroides ochraceus).
OC   Bacteria; Pseudomonadati; Bacteroidota; Flavobacteriia; Flavobacteriales;
OC   Flavobacteriaceae; Capnocytophaga.
OX   NCBI_TaxID=521097;
```

Source SHA-256: `a7856db74c2257c0ae32918e6ed89fb2b1448ac6527c4a62ff2b4a4bf082737a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70)  
**Locator:** `lines 29-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:41.947109+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND COFACTOR.
RX   PubMed=35414181; DOI=10.1021/acs.biochem.2c00102;
RA   Liu Y., Wei Y., Teh T.M., Liu D., Zhou Y., Zhao S., Ang E.L., Zhao H.,
RA   Zhang Y.;
RT   "Identification and Characterization of the Biosynthetic Pathway of the
RT   Sulfonolipid Capnine.";
RL   Biochemistry 61:2861-2869(2022).
```

Source SHA-256: `a7856db74c2257c0ae32918e6ed89fb2b1448ac6527c4a62ff2b4a4bf082737a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70)  
**Locator:** `lines 55-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 70 / 1.  
**Retrieved:** 2026-11-02T04:27:41.947109+00:00.  

```text
CC   -!- PATHWAY: Lipid metabolism. {ECO:0000305|PubMed:35414181}.
```

Source SHA-256: `a7856db74c2257c0ae32918e6ed89fb2b1448ac6527c4a62ff2b4a4bf082737a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
