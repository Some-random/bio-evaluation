# pathway_0049

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Bacterial outer membrane biogenesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1. .
B. sterol biosynthesis. .
C. Bacterial outer membrane biogenesis
D. L-threonine from L-aspartate: step 2/5. .
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

> The exact supplied sequence matches the annotated UDP-N-acetyl-D-glucosamine 6-dehydrogenase WbpO, whose pathway annotation includes bacterial outer membrane biogenesis and LPS O-antigen biosynthesis. The annotation cites experimental and curated evidence; the cited primary papers were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could suggest an NAD-dependent dehydrogenase, but the input provides no organism, genomic context, substrate identification, or other supplied evidence that specifically connects the enzyme to O-antigen biosynthesis rather than the other listed pathways.


**Missing item-specific fact**

> The identity and pathway role of this particular enzyme—WbpO in LPS O-antigen biosynthesis—are needed to select C.


**Reason**

> The sequence alone does not supply a concrete, sufficiently specific argument for distinguishing these pathways. Knowing the matched protein annotation or experimental function is an item-specific fact absent from the evaluated input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports C; none of the other options is supported for this protein by the available evidence.


### Important caveats

- The protein-to-accession mapping and database records are reviewer-only evidence, not information supplied to the evaluated model.
- The source snapshot used by the author is unknown, although the sequence matches both current and historical records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could suggest an NAD-dependent dehydrogenase, but the input provides no organism, genomic context, substrate identification, or other supplied evidence that specifically connects the enzyme to O-antigen biosynthesis rather than the other listed pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity and pathway role of this particular enzyme—WbpO in LPS O-antigen biosynthesis—are needed to select C.",
    "reason": "The sequence alone does not supply a concrete, sufficiently specific argument for distinguishing these pathways. Knowing the matched protein annotation or experimental function is an item-specific fact absent from the evaluated input."
  },
  "case_id": "pathway_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the annotated UDP-N-acetyl-D-glucosamine 6-dehydrogenase WbpO, whose pathway annotation includes bacterial outer membrane biogenesis and LPS O-antigen biosynthesis. The annotation cites experimental and curated evidence; the cited primary papers were not independently reviewed here."
  },
  "important_caveats": [
    "The protein-to-accession mapping and database records are reviewer-only evidence, not information supplied to the evaluated model.",
    "The source snapshot used by the author is unknown, although the sequence matches both current and historical records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports C; none of the other options is supported for this protein by the available evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the annotated UDP-N-acetyl-D-glucosamine 6-dehydrogenase WbpO, whose pathway annotation includes bacterial outer membrane biogenesis and LPS O-antigen biosynthesis. The annotation cites experimental and curated evidence; the cited primary papers were not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could suggest an NAD-dependent dehydrogenase, but the input provides no organism, genomic context, substrate identification, or other supplied evidence that specifically connects the enzyme to O-antigen biosynthesis rather than the other listed pathways.",
    "missing_item_specific_fact": "The identity and pathway role of this particular enzyme—WbpO in LPS O-antigen biosynthesis—are needed to select C.",
    "reason": "The sequence alone does not supply a concrete, sufficiently specific argument for distinguishing these pathways. Knowing the matched protein annotation or experimental function is an item-specific fact absent from the evaluated input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports C; none of the other options is supported for this protein by the available evidence."
  },
  "important_caveats": [
    "The protein-to-accession mapping and database records are reviewer-only evidence, not information supplied to the evaluated model.",
    "The source snapshot used by the author is unknown, although the sequence matches both current and historical records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9RHD7 (WbpO, UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136) explicitly annotates the pathway as 'Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis' with experimental evidence codes (ECO:0000269 from PubMed:10627048; ECO:0000305 from PubMed:10931835 and PubMed:18065759). Functional studies, disruption phenotypes, and catalytic activity assays support WbpO's role in LPS O-antigen biosynthesis, which is a component of bacterial outer membrane biogenesis. The sequence in the question matches the UniProt entry exactly (422 aa, SHA-256 confirmed).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a Rossmann-fold NAD-binding motif (GLGYVGLPLAV at the N-terminus), confirming it is an NAD-dependent dehydrogenase. However, this fold is shared by thousands of dehydrogenases across all metabolic pathways. No sequence motif uniquely identifies this enzyme as a UDP-GlcNAc 6-dehydrogenase acting in LPS O-antigen biosynthesis rather than in NAD biosynthesis (option A) or threonine biosynthesis (option D). One can eliminate option B (sterol biosynthesis) on the general ground that bacteria rarely synthesize sterols, but distinguishing C from A and D requires knowing the specific substrate (UDP-N-acetyl-D-glucosamine) and the specific gene cluster (wbp) context, which is not inferable from sequence alone.


**Missing item-specific fact**

> The identity of the protein as WbpO and its specific role in the wbp gene cluster for Pseudomonas aeruginosa B-band O-antigen biosynthesis. Without recognizing this exact sequence as WbpO or recalling the wbp locus annotation, a model cannot determine that the NAD-dependent dehydrogenase acts on UDP-GlcNAc in LPS O-antigen biosynthesis rather than in NAD metabolism or amino acid biosynthesis.


**Reason**

> The question provides only a raw amino acid sequence and four pathway options. The NAD-binding Rossmann fold is a generic feature of dehydrogenases and does not discriminate among the metabolic pathways listed. Correctly selecting 'Bacterial outer membrane biogenesis' requires either recognizing the exact sequence as WbpO (database lookup) or memorizing the wbp gene cluster's role in LPS biosynthesis. No general biological reasoning from sequence features alone distinguishes C from A or D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are clearly distinct pathways. Option B (sterol biosynthesis) is trivially eliminable for a bacterial protein. Options A (NAD biosynthesis) and D (threonine biosynthesis) describe specific enzymatic steps in unrelated pathways. Option C (bacterial outer membrane biogenesis) is the UniProt-annotated pathway. No two options are genuinely ambiguous given the correct annotation.


### Important caveats

- The UniProt pathway annotation 'Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis' is broad; WbpO specifically acts in O-antigen biosynthesis, a sub-pathway. However, among the given options, C is the only viable match.
- The evidence codes include ECO:0000305 (inferred by similarity) for two of the three pathway references, though ECO:0000269 (experimental) from PubMed:10627048 provides direct functional/pathway evidence.
- The sequence is from Pseudomonas aeruginosa (a Gram-negative bacterium), which is consistent with outer membrane biogenesis being relevant, but this alone does not uniquely select C over A or D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold NAD-binding motif (GLGYVGLPLAV at the N-terminus), confirming it is an NAD-dependent dehydrogenase. However, this fold is shared by thousands of dehydrogenases across all metabolic pathways. No sequence motif uniquely identifies this enzyme as a UDP-GlcNAc 6-dehydrogenase acting in LPS O-antigen biosynthesis rather than in NAD biosynthesis (option A) or threonine biosynthesis (option D). One can eliminate option B (sterol biosynthesis) on the general ground that bacteria rarely synthesize sterols, but distinguishing C from A and D requires knowing the specific substrate (UDP-N-acetyl-D-glucosamine) and the specific gene cluster (wbp) context, which is not inferable from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the protein as WbpO and its specific role in the wbp gene cluster for Pseudomonas aeruginosa B-band O-antigen biosynthesis. Without recognizing this exact sequence as WbpO or recalling the wbp locus annotation, a model cannot determine that the NAD-dependent dehydrogenase acts on UDP-GlcNAc in LPS O-antigen biosynthesis rather than in NAD metabolism or amino acid biosynthesis.",
    "reason": "The question provides only a raw amino acid sequence and four pathway options. The NAD-binding Rossmann fold is a generic feature of dehydrogenases and does not discriminate among the metabolic pathways listed. Correctly selecting 'Bacterial outer membrane biogenesis' requires either recognizing the exact sequence as WbpO (database lookup) or memorizing the wbp gene cluster's role in LPS biosynthesis. No general biological reasoning from sequence features alone distinguishes C from A or D."
  },
  "case_id": "pathway_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9RHD7 (WbpO, UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136) explicitly annotates the pathway as 'Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis' with experimental evidence codes (ECO:0000269 from PubMed:10627048; ECO:0000305 from PubMed:10931835 and PubMed:18065759). Functional studies, disruption phenotypes, and catalytic activity assays support WbpO's role in LPS O-antigen biosynthesis, which is a component of bacterial outer membrane biogenesis. The sequence in the question matches the UniProt entry exactly (422 aa, SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis' is broad; WbpO specifically acts in O-antigen biosynthesis, a sub-pathway. However, among the given options, C is the only viable match.",
    "The evidence codes include ECO:0000305 (inferred by similarity) for two of the three pathway references, though ECO:0000269 (experimental) from PubMed:10627048 provides direct functional/pathway evidence.",
    "The sequence is from Pseudomonas aeruginosa (a Gram-negative bacterium), which is consistent with outer membrane biogenesis being relevant, but this alone does not uniquely select C over A or D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are clearly distinct pathways. Option B (sterol biosynthesis) is trivially eliminable for a bacterial protein. Options A (NAD biosynthesis) and D (threonine biosynthesis) describe specific enzymatic steps in unrelated pathways. Option C (bacterial outer membrane biogenesis) is the UniProt-annotated pathway. No two options are genuinely ambiguous given the correct annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9RHD7 (WbpO, UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136) explicitly annotates the pathway as 'Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis' with experimental evidence codes (ECO:0000269 from PubMed:10627048; ECO:0000305 from PubMed:10931835 and PubMed:18065759). Functional studies, disruption phenotypes, and catalytic activity assays support WbpO's role in LPS O-antigen biosynthesis, which is a component of bacterial outer membrane biogenesis. The sequence in the question matches the UniProt entry exactly (422 aa, SHA-256 confirmed).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H1", "H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold NAD-binding motif (GLGYVGLPLAV at the N-terminus), confirming it is an NAD-dependent dehydrogenase. However, this fold is shared by thousands of dehydrogenases across all metabolic pathways. No sequence motif uniquely identifies this enzyme as a UDP-GlcNAc 6-dehydrogenase acting in LPS O-antigen biosynthesis rather than in NAD biosynthesis (option A) or threonine biosynthesis (option D). One can eliminate option B (sterol biosynthesis) on the general ground that bacteria rarely synthesize sterols, but distinguishing C from A and D requires knowing the specific substrate (UDP-N-acetyl-D-glucosamine) and the specific gene cluster (wbp) context, which is not inferable from sequence alone.",
    "missing_item_specific_fact": "The identity of the protein as WbpO and its specific role in the wbp gene cluster for Pseudomonas aeruginosa B-band O-antigen biosynthesis. Without recognizing this exact sequence as WbpO or recalling the wbp locus annotation, a model cannot determine that the NAD-dependent dehydrogenase acts on UDP-GlcNAc in LPS O-antigen biosynthesis rather than in NAD metabolism or amino acid biosynthesis.",
    "reason": "The question provides only a raw amino acid sequence and four pathway options. The NAD-binding Rossmann fold is a generic feature of dehydrogenases and does not discriminate among the metabolic pathways listed. Correctly selecting 'Bacterial outer membrane biogenesis' requires either recognizing the exact sequence as WbpO (database lookup) or memorizing the wbp gene cluster's role in LPS biosynthesis. No general biological reasoning from sequence features alone distinguishes C from A or D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are clearly distinct pathways. Option B (sterol biosynthesis) is trivially eliminable for a bacterial protein. Options A (NAD biosynthesis) and D (threonine biosynthesis) describe specific enzymatic steps in unrelated pathways. Option C (bacterial outer membrane biogenesis) is the UniProt-annotated pathway. No two options are genuinely ambiguous given the correct annotation."
  },
  "important_caveats": [
    "The UniProt pathway annotation 'Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis' is broad; WbpO specifically acts in O-antigen biosynthesis, a sub-pathway. However, among the given options, C is the only viable match.",
    "The evidence codes include ECO:0000305 (inferred by similarity) for two of the three pathway references, though ECO:0000269 (experimental) from PubMed:10627048 provides direct functional/pathway evidence.",
    "The sequence is from Pseudomonas aeruginosa (a Gram-negative bacterium), which is consistent with outer membrane biogenesis being relevant, but this alone does not uniquely select C over A or D."
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

**Accession:** `Q9RHD7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 111. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
"Q9RHD7"
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"1.1.1.136"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-D-glucosamine 6-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-GlcNAc 6-dehydrogenase"}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10627048","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"10931835","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"18065759","source":"PubMed"}],"value":"Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis"}]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"citation":{"authors":["Belanger M.","Burrows L.L.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"10627048"},{"database":"DOI","id":"10.1099/00221287-145-12-3505"}],"citationType":"journal article","firstPage":"3505","id":"10627048","journal":"Microbiology","lastPage":"3521","publicationDate":"1999","title":"Functional analysis of genes responsible for the synthesis of the B-band O antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.","volume":"145"},"evidences":[{"evidenceCode":"ECO:0000312","id":"AAF23997.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 33354 / Serotype O6"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"citation":{"authors":["Zhao X.","Creuzenet C.","Belanger M.","Egbosimba E.","Li J.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"10931835"},{"database":"DOI","id":"10.1074/jbc.m004191200"}],"citationType":"journal article","firstPage":"33252","id":"10931835","journal":"J. Biol. Chem.","lastPage":"33259","publicationDate":"2000","title":"WbpO, a UDP-N-acetyl-D-galactosamine dehydrogenase from Pseudomonas aeruginosa serotype O6.","volume":"275"},"referenceComments":[{"type":"STRAIN","value":"Serotype O6"}],"referenceNumber":4,"referencePositions":["FUNCTION","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"citation":{"authors":["Miller W.L.","Matewish M.J.","McNally D.J.","Ishiyama N.","Anderson E.M.","Brewer D.","Brisson J.R.","Berghuis A.M.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"18065759"},{"database":"DOI","id":"10.1074/jbc.m708894200"}],"citationType":"journal article","firstPage":"3507","id":"18065759","journal":"J. Biol. Chem.","lastPage":"3518","publicationDate":"2008","title":"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.","volume":"283"},"referenceComments":[{"type":"STRAIN","value":"PAK / Serotype O6"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
ID   WBPO_PSEAI              Reviewed;         422 AA.
AC   Q9RHD7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 111.
DE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000305};
DE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000305};
DE            EC=1.1.1.136 {ECO:0000269|PubMed:18065759};
GN   Name=wbpO {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};
GN   ORFNames=CAZ10_03215 {ECO:0000312|EMBL:OTI64803.1};
OS   Pseudomonas aeruginosa.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.
OX   NCBI_TaxID=287;
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 15-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:AAF23997.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, PATHWAY, AND DISRUPTION
RP   PHENOTYPE.
RC   STRAIN=ATCC 33354 / Serotype O6;
RX   PubMed=10627048; DOI=10.1099/00221287-145-12-3505;
RA   Belanger M., Burrows L.L., Lam J.S.;
RT   "Functional analysis of genes responsible for the synthesis of the B-band O
RT   antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.";
RL   Microbiology 145:3505-3521(1999).
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 39-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
RN   [4]
RP   FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.
RC   STRAIN=Serotype O6;
RX   PubMed=10931835; DOI=10.1074/jbc.m004191200;
RA   Zhao X., Creuzenet C., Belanger M., Egbosimba E., Li J., Lam J.S.;
RT   "WbpO, a UDP-N-acetyl-D-galactosamine dehydrogenase from Pseudomonas
RT   aeruginosa serotype O6.";
RL   J. Biol. Chem. 275:33252-33259(2000).
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 47-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
RN   [5]
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, AND DISRUPTION PHENOTYPE.
RC   STRAIN=PAK / Serotype O6;
RX   PubMed=18065759; DOI=10.1074/jbc.m708894200;
RA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,
RA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;
RT   "Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-
RT   antigen biosynthesis enzyme WbpO.";
RL   J. Biol. Chem. 283:3507-3518(2008).
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 110-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
CC   -!- PATHWAY: Bacterial outer membrane biogenesis; LPS O-antigen
CC       biosynthesis. {ECO:0000269|PubMed:10627048,
CC       ECO:0000305|PubMed:10931835, ECO:0000305|PubMed:18065759}.
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
