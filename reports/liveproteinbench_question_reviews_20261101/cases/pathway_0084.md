# pathway_0084

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Lipid metabolism. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRYAVVTGVSSGIGKAICEKFLAKGLYVFGSVRKKEDAKYFEEKYPNTFHTLVFDTTDYPAVDKAVEEIHKVVGKKGLSVLVNNAGVAKYGPIQHVPIEELRQQYEVNVFASVYLTQKLLWLLGASKEAKWQGKVIQISSTAGVMTRPMLGPYSSSKHAVEAIYDALRRELMIYGVEVVLIEPGPIKTEIWGKAKSGGNPYKDTDYGEIFAQLDKAVDEIEKIGLPVEAVAGKAWEAFVAKKPKARYVVAPKKLMFKAAMYLIPDRMLDKIFYKDLKKLTQES

[Multiple Choices]
A. L-threonine from L-aspartate: step 4/5. .
B. Amino-acid degradation
C. Lipid metabolism. .
D. capsule polysaccharide biosynthesis. .
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

> The supplied sequence exactly matches the archived UniProt entry for NADPH-dependent 3-dehydrocapnine reductase. That entry assigns it to lipid metabolism and cites research on capnine biosynthesis. The pathway assignment is a database annotation (ECO:0000305), while the entry separately marks the enzyme activity as experimentally supported (ECO:0000269); this supports choice C without implying that the pathway label itself is a direct experimental measurement.

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently specific, recognizable signal to distinguish this enzyme's role in capnine lipid biosynthesis from the listed alternatives. Its protein-specific enzyme identity is needed.


**Missing item-specific fact**

> That this exact sequence is NADPH-dependent 3-dehydrocapnine reductase, an enzyme in capnine biosynthesis.


**Reason**

> The decisive identity and pathway annotation are absent from the question. Inferring a broad enzyme class from sequence features would not establish this particular pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports lipid metabolism; the other choices are not supported by the available protein-specific evidence.


### Important caveats

- The archived sequence-matched pathway annotation is a database assertion citing the capnine biosynthesis study, not itself a direct experimental pathway measurement.
- The exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, recognizable signal to distinguish this enzyme's role in capnine lipid biosynthesis from the listed alternatives. Its protein-specific enzyme identity is needed.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this exact sequence is NADPH-dependent 3-dehydrocapnine reductase, an enzyme in capnine biosynthesis.",
    "reason": "The decisive identity and pathway annotation are absent from the question. Inferring a broad enzyme class from sequence features would not establish this particular pathway."
  },
  "case_id": "pathway_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "H3",
      "C1",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived UniProt entry for NADPH-dependent 3-dehydrocapnine reductase. That entry assigns it to lipid metabolism and cites research on capnine biosynthesis. The pathway assignment is a database annotation (ECO:0000305), while the entry separately marks the enzyme activity as experimentally supported (ECO:0000269); this supports choice C without implying that the pathway label itself is a direct experimental measurement."
  },
  "important_caveats": [
    "The archived sequence-matched pathway annotation is a database assertion citing the capnine biosynthesis study, not itself a direct experimental pathway measurement.",
    "The exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports lipid metabolism; the other choices are not supported by the available protein-specific evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived UniProt entry for NADPH-dependent 3-dehydrocapnine reductase. That entry assigns it to lipid metabolism and cites research on capnine biosynthesis. The pathway assignment is a database annotation (ECO:0000305), while the entry separately marks the enzyme activity as experimentally supported (ECO:0000269); this supports choice C without implying that the pathway label itself is a direct experimental measurement.",
    "evidence_ids": ["H1", "H2", "H3", "C1", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, recognizable signal to distinguish this enzyme's role in capnine lipid biosynthesis from the listed alternatives. Its protein-specific enzyme identity is needed.",
    "missing_item_specific_fact": "That this exact sequence is NADPH-dependent 3-dehydrocapnine reductase, an enzyme in capnine biosynthesis.",
    "reason": "The decisive identity and pathway annotation are absent from the question. Inferring a broad enzyme class from sequence features would not establish this particular pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports lipid metabolism; the other choices are not supported by the available protein-specific evidence."
  },
  "important_caveats": [
    "The archived sequence-matched pathway annotation is a database assertion citing the capnine biosynthesis study, not itself a direct experimental pathway measurement.",
    "The exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5, H3) explicitly states PATHWAY: Lipid metabolism with evidence code ECO:0000305 linked to PubMed:35414181 (Liu et al., Biochemistry 2022, 'Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine'). The protein is NADPH-dependent 3-dehydrocapnine reductase (CapC), functioning in the biosynthetic pathway of capnine, a sulfonolipid. Sulfonolipids are lipids, making the 'Lipid metabolism' pathway assignment scientifically accurate. The evidence is from a 2022 experimental characterization paper (ECO:0000269 for EC assignment, ECO:0000305 for pathway curator inference from the same publication).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains N-terminal motifs (VSSGIG) consistent with a short-chain dehydrogenase/reductase (SDR) family Rossmann-fold nucleotide-binding site, indicating an NAD(P)H-dependent oxidoreductase. However, reductases participate in lipid metabolism, amino acid biosynthesis/degradation, and other pathways alike. No sequence feature uniquely identifies this as a sulfonolipid (capnine) biosynthetic enzyme rather than, e.g., homoserine dehydrogenase (threonine pathway, option A) or an amino acid degradation reductase (option B). The critical distinguishing fact—that capnine is a sulfonolipid and this protein is CapC in its biosynthetic pathway—is an item-specific annotation not derivable from the sequence alone.


**Missing item-specific fact**

> Knowledge that this specific 283-aa protein from Ornithobacterium rhinotracheale is CapC, the NADPH-dependent 3-dehydrocapnine reductase in the biosynthetic pathway of the sulfonolipid capnine, and that capnine is classified as a lipid (sulfonolipid). This requires the 2022 Biochemistry paper or the UniProt annotation.


**Reason**

> While one can infer the protein is a reductase from sequence motifs, distinguishing lipid metabolism (C) from amino-acid-related pathways (A, B) requires knowing the specific substrate (capnine, a sulfonolipid) and the specific pathway context. Option D (capsule polysaccharide biosynthesis) is somewhat less plausible since polysaccharide biosynthesis typically involves glycosyltransferases rather than NADPH-dependent reductases, but this alone does not uniquely select C over A or B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D (capsule polysaccharide biosynthesis) is the weakest distractor because polysaccharide biosynthesis rarely involves NADPH-dependent reductases as key steps. Options A and B are plausible at the family level (reductases exist in both), but neither is specifically supported by sequence features. With the correct annotation, C is the uniquely correct answer. No two options are equally defensible from the sequence alone.


### Important caveats

- The pathway annotation carries evidence code ECO:0000305 (inferred by curator from the cited publication), meaning it is a curator-assigned classification based on the 2022 paper rather than a direct experimental pathway measurement.
- The EC number is incomplete (1.1.1.-), indicating the specific substrate specificity was characterized but a full four-digit EC was not assigned.
- The protein was first integrated into Swiss-Prot on 2025-04-09; if the benchmark was constructed before this date, the annotation may have been derived from the primary literature directly.
- The identity of the sequence as CapC_ORNRH was inferred by the reviewer from dataset metadata; the evaluated model had only the raw sequence and four pathway choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains N-terminal motifs (VSSGIG) consistent with a short-chain dehydrogenase/reductase (SDR) family Rossmann-fold nucleotide-binding site, indicating an NAD(P)H-dependent oxidoreductase. However, reductases participate in lipid metabolism, amino acid biosynthesis/degradation, and other pathways alike. No sequence feature uniquely identifies this as a sulfonolipid (capnine) biosynthetic enzyme rather than, e.g., homoserine dehydrogenase (threonine pathway, option A) or an amino acid degradation reductase (option B). The critical distinguishing fact—that capnine is a sulfonolipid and this protein is CapC in its biosynthetic pathway—is an item-specific annotation not derivable from the sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowledge that this specific 283-aa protein from Ornithobacterium rhinotracheale is CapC, the NADPH-dependent 3-dehydrocapnine reductase in the biosynthetic pathway of the sulfonolipid capnine, and that capnine is classified as a lipid (sulfonolipid). This requires the 2022 Biochemistry paper or the UniProt annotation.",
    "reason": "While one can infer the protein is a reductase from sequence motifs, distinguishing lipid metabolism (C) from amino-acid-related pathways (A, B) requires knowing the specific substrate (capnine, a sulfonolipid) and the specific pathway context. Option D (capsule polysaccharide biosynthesis) is somewhat less plausible since polysaccharide biosynthesis typically involves glycosyltransferases rather than NADPH-dependent reductases, but this alone does not uniquely select C over A or B."
  },
  "case_id": "pathway_0084",
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
    "reason": "UniProt annotation (C5, H3) explicitly states PATHWAY: Lipid metabolism with evidence code ECO:0000305 linked to PubMed:35414181 (Liu et al., Biochemistry 2022, 'Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine'). The protein is NADPH-dependent 3-dehydrocapnine reductase (CapC), functioning in the biosynthetic pathway of capnine, a sulfonolipid. Sulfonolipids are lipids, making the 'Lipid metabolism' pathway assignment scientifically accurate. The evidence is from a 2022 experimental characterization paper (ECO:0000269 for EC assignment, ECO:0000305 for pathway curator inference from the same publication)."
  },
  "important_caveats": [
    "The pathway annotation carries evidence code ECO:0000305 (inferred by curator from the cited publication), meaning it is a curator-assigned classification based on the 2022 paper rather than a direct experimental pathway measurement.",
    "The EC number is incomplete (1.1.1.-), indicating the specific substrate specificity was characterized but a full four-digit EC was not assigned.",
    "The protein was first integrated into Swiss-Prot on 2025-04-09; if the benchmark was constructed before this date, the annotation may have been derived from the primary literature directly.",
    "The identity of the sequence as CapC_ORNRH was inferred by the reviewer from dataset metadata; the evaluated model had only the raw sequence and four pathway choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D (capsule polysaccharide biosynthesis) is the weakest distractor because polysaccharide biosynthesis rarely involves NADPH-dependent reductases as key steps. Options A and B are plausible at the family level (reductases exist in both), but neither is specifically supported by sequence features. With the correct annotation, C is the uniquely correct answer. No two options are equally defensible from the sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) explicitly states PATHWAY: Lipid metabolism with evidence code ECO:0000305 linked to PubMed:35414181 (Liu et al., Biochemistry 2022, 'Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine'). The protein is NADPH-dependent 3-dehydrocapnine reductase (CapC), functioning in the biosynthetic pathway of capnine, a sulfonolipid. Sulfonolipids are lipids, making the 'Lipid metabolism' pathway assignment scientifically accurate. The evidence is from a 2022 experimental characterization paper (ECO:0000269 for EC assignment, ECO:0000305 for pathway curator inference from the same publication).",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains N-terminal motifs (VSSGIG) consistent with a short-chain dehydrogenase/reductase (SDR) family Rossmann-fold nucleotide-binding site, indicating an NAD(P)H-dependent oxidoreductase. However, reductases participate in lipid metabolism, amino acid biosynthesis/degradation, and other pathways alike. No sequence feature uniquely identifies this as a sulfonolipid (capnine) biosynthetic enzyme rather than, e.g., homoserine dehydrogenase (threonine pathway, option A) or an amino acid degradation reductase (option B). The critical distinguishing fact—that capnine is a sulfonolipid and this protein is CapC in its biosynthetic pathway—is an item-specific annotation not derivable from the sequence alone.",
    "missing_item_specific_fact": "Knowledge that this specific 283-aa protein from Ornithobacterium rhinotracheale is CapC, the NADPH-dependent 3-dehydrocapnine reductase in the biosynthetic pathway of the sulfonolipid capnine, and that capnine is classified as a lipid (sulfonolipid). This requires the 2022 Biochemistry paper or the UniProt annotation.",
    "reason": "While one can infer the protein is a reductase from sequence motifs, distinguishing lipid metabolism (C) from amino-acid-related pathways (A, B) requires knowing the specific substrate (capnine, a sulfonolipid) and the specific pathway context. Option D (capsule polysaccharide biosynthesis) is somewhat less plausible since polysaccharide biosynthesis typically involves glycosyltransferases rather than NADPH-dependent reductases, but this alone does not uniquely select C over A or B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D (capsule polysaccharide biosynthesis) is the weakest distractor because polysaccharide biosynthesis rarely involves NADPH-dependent reductases as key steps. Options A and B are plausible at the family level (reductases exist in both), but neither is specifically supported by sequence features. With the correct annotation, C is the uniquely correct answer. No two options are equally defensible from the sequence alone."
  },
  "important_caveats": [
    "The pathway annotation carries evidence code ECO:0000305 (inferred by curator from the cited publication), meaning it is a curator-assigned classification based on the 2022 paper rather than a direct experimental pathway measurement.",
    "The EC number is incomplete (1.1.1.-), indicating the specific substrate specificity was characterized but a full four-digit EC was not assigned.",
    "The protein was first integrated into Swiss-Prot on 2025-04-09; if the benchmark was constructed before this date, the annotation may have been derived from the primary literature directly.",
    "The identity of the sequence as CapC_ORNRH was inferred by the reviewer from dataset metadata; the evaluated model had only the raw sequence and four pathway choices."
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
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:46.269818+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"35414181","source":"PubMed"}],"value":"Lipid metabolism"}]}
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
**Locator:** `lines 21-28`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:30.826829+00:00.  

```text
RN   [2]
RP   FUNCTION, AND CATALYTIC ACTIVITY.
RX   PubMed=35414181; DOI=10.1021/acs.biochem.2c00102;
RA   Liu Y., Wei Y., Teh T.M., Liu D., Zhou Y., Zhao S., Ang E.L., Zhao H.,
RA   Zhang Y.;
RT   "Identification and Characterization of the Biosynthetic Pathway of the
RT   Sulfonolipid Capnine.";
RL   Biochemistry 61:2861-2869(2022).
```

Source SHA-256: `6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)  
**Locator:** `lines 41-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:30.826829+00:00.  

```text
CC   -!- PATHWAY: Lipid metabolism. {ECO:0000305|PubMed:35414181}.
```

Source SHA-256: `6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
