# pathway_0149

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Cofactor biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MHYLDNLLLNTDSYKASHWLQYPPGTDASFFYVESRGGVYDQTAFFGLQSILKEAINRPVTHADIDDAKALLAAHGEPFNEAGWRDIVDRLGGQLPIRIRAVPEGCVVPTHNVLMTIESTDAKAFWVPSYLETLLLRVWYPVTVATVSWQVKQIVRDFLQRTSDDPEGQLPFKLHDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHTPVAGYSIPAAEHSTITSWGREREVDAYRNMLTQFARPGAIVAVVSDSYDIYRAIREHWGTTLREEIIASGATVVIRPDSGDPVDVVEQCLLLLDEAFGHQVNGKGYKVLNHVRVIQGDGINPQSLRAILERITAAGYAADNVAFGMGGALLQKVDRDTQKFALKCSAVRVDGAWIDVYKDPITDQGKQSKRGRLTLLRDRATGQYRSALLDEVATHAGDSDDALVTVWENGQMLREWTLEQVRAHADAARL

[Multiple Choices]
A. Antifungal biosynthesis. .
B. protein ubiquitination. .
C. IMP biosynthesis via de novo pathway
D. Cofactor biosynthesis
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

> The supplied sequence exactly matches the annotated 468-aa Xanthomonas campestris NAMPT. The entry identifies it as nicotinamide phosphoribosyltransferase and assigns it to NAD(+) cofactor biosynthesis; the pathway annotation cites experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a soluble enzyme, which makes the signaling and ubiquitination options less plausible, but that broad observation does not distinguish cofactor biosynthesis from other metabolic pathways.


**Missing item-specific fact**

> Identifying this sequence as nicotinamide phosphoribosyltransferase, which catalyzes a step in NAD(+) biosynthesis.


**Reason**

> The sequence and choices do not provide a sufficiently specific, readily interpretable motif or context to establish its pathway without protein-specific identification or equivalent annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the matched NAMPT annotation and its NAD(+) biosynthesis role, cofactor biosynthesis is the clear listed choice.


### Important caveats

- The pathway annotation and experimental support are reviewer-only evidence, not information supplied to the evaluated model.
- The exact author source snapshot is unknown, although the sequence matches both the current entry and a historical entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble enzyme, which makes the signaling and ubiquitination options less plausible, but that broad observation does not distinguish cofactor biosynthesis from other metabolic pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this sequence as nicotinamide phosphoribosyltransferase, which catalyzes a step in NAD(+) biosynthesis.",
    "reason": "The sequence and choices do not provide a sufficiently specific, readily interpretable motif or context to establish its pathway without protein-specific identification or equivalent annotation."
  },
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 468-aa Xanthomonas campestris NAMPT. The entry identifies it as nicotinamide phosphoribosyltransferase and assigns it to NAD(+) cofactor biosynthesis; the pathway annotation cites experimental evidence."
  },
  "important_caveats": [
    "The pathway annotation and experimental support are reviewer-only evidence, not information supplied to the evaluated model.",
    "The exact author source snapshot is unknown, although the sequence matches both the current entry and a historical entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched NAMPT annotation and its NAD(+) biosynthesis role, cofactor biosynthesis is the clear listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 468-aa Xanthomonas campestris NAMPT. The entry identifies it as nicotinamide phosphoribosyltransferase and assigns it to NAD(+) cofactor biosynthesis; the pathway annotation cites experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a soluble enzyme, which makes the signaling and ubiquitination options less plausible, but that broad observation does not distinguish cofactor biosynthesis from other metabolic pathways.",
    "missing_item_specific_fact": "Identifying this sequence as nicotinamide phosphoribosyltransferase, which catalyzes a step in NAD(+) biosynthesis.",
    "reason": "The sequence and choices do not provide a sufficiently specific, readily interpretable motif or context to establish its pathway without protein-specific identification or equivalent annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched NAMPT annotation and its NAD(+) biosynthesis role, cofactor biosynthesis is the clear listed choice."
  },
  "important_caveats": [
    "The pathway annotation and experimental support are reviewer-only evidence, not information supplied to the evaluated model.",
    "The exact author source snapshot is unknown, although the sequence matches both the current entry and a historical entry."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (468 aa, SHA256 matched) corresponds to UniProt A0A0H2X5R2, annotated as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) from Xanthomonas campestris pv. campestris 8004. The UniProt PATHWAY comment reads: 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1' (ECO:0000269, PubMed:38429435). This is backed by X-ray crystallography (PDB: 7YQO, 7YQP, 7YQQ, 7YQR, 8IGZ) and enzymatic characterization. The expected answer 'Cofactor biosynthesis' directly matches the top-level pathway category.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark PRTase (phosphoribosyltransferase) superfamily motifs: the 'HDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHT' block, the 'VSDSYDIY' SD-motif, and 'GAWIDVYKDP' — diagnostic of the Type I PRTase fold. This immediately eliminates B (protein ubiquitination: no E2/E3 ligase, RING, or UBA motifs) and A (antifungal biosynthesis: no PKS, NRPS, or terpene cyclase features). Between C and D: the de novo IMP biosynthesis pathway proceeds through amidotransferases, formyltransferases, synthetases, and lyases (e.g., PRPP amidotransferase, GAR synthetase, FGAM synthetase, AIR carboxylase, SAICAR synthetase) and does not employ Type I PRTases. In contrast, NAD+ biosynthesis via the NAM salvage pathway is catalyzed by NAMPT, a canonical Type I PRTase, and NAD+ is universally classified as a cofactor. Thus, identifying the protein as a Type I PRTase and applying standard pathway biochemistry (IMP de novo lacks PRTases; NAD+ is a cofactor) provides a concrete chain of reasoning that selects D over C.


**Missing item-specific fact**

> Precise subfamily assignment (NAMPT vs. HGPRT vs. other Type I PRTases) from sequence alone requires detailed knowledge of substrate-binding-site residues; however, the pathway-level distinction (cofactor vs. nucleotide de novo) is resolvable without that specificity because IMP de novo does not use PRTases at all.


**Reason**

> The PRTase fold identification narrows the choices from four to two (C vs. D), and standard biochemistry knowledge that the de novo purine pathway does not employ PRTases while NAD+ biosynthesis does eliminates C. The remaining choice D is supported by the general classification of NAD+ as a cofactor. This constitutes a meaningful biological reasoning chain rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are eliminated by absence of any relevant enzymatic motifs. Option C (IMP de novo) is eliminated because that pathway does not utilize Type I PRTases. Option D (Cofactor biosynthesis) is the only pathway among the four that employs a Type I PRTase. No other option is defensible given the PRTase identification.


### Important caveats

- The UniProt annotation is Swiss-Prot (manually curated) with experimental evidence codes (ECO:0000269, X-ray crystallography), providing strong support for the pathway assignment.
- The entry was first released in 2025-02-05; if the benchmark was constructed before that date, the annotation may have been derived from computational inference or transferred annotation rather than the 2024 experimental paper.
- The reasoning chain relies on the examinee recognizing PRTase motifs and knowing that IMP de novo does not use PRTases — this is standard biochemistry but still requires specific pathway-level knowledge beyond generic sequence analysis.
- The sequence-match is exact (SHA256 identical) between the benchmark input and the UniProt entry, confirming applicability of the annotation to this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark PRTase (phosphoribosyltransferase) superfamily motifs: the 'HDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHT' block, the 'VSDSYDIY' SD-motif, and 'GAWIDVYKDP' — diagnostic of the Type I PRTase fold. This immediately eliminates B (protein ubiquitination: no E2/E3 ligase, RING, or UBA motifs) and A (antifungal biosynthesis: no PKS, NRPS, or terpene cyclase features). Between C and D: the de novo IMP biosynthesis pathway proceeds through amidotransferases, formyltransferases, synthetases, and lyases (e.g., PRPP amidotransferase, GAR synthetase, FGAM synthetase, AIR carboxylase, SAICAR synthetase) and does not employ Type I PRTases. In contrast, NAD+ biosynthesis via the NAM salvage pathway is catalyzed by NAMPT, a canonical Type I PRTase, and NAD+ is universally classified as a cofactor. Thus, identifying the protein as a Type I PRTase and applying standard pathway biochemistry (IMP de novo lacks PRTases; NAD+ is a cofactor) provides a concrete chain of reasoning that selects D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise subfamily assignment (NAMPT vs. HGPRT vs. other Type I PRTases) from sequence alone requires detailed knowledge of substrate-binding-site residues; however, the pathway-level distinction (cofactor vs. nucleotide de novo) is resolvable without that specificity because IMP de novo does not use PRTases at all.",
    "reason": "The PRTase fold identification narrows the choices from four to two (C vs. D), and standard biochemistry knowledge that the de novo purine pathway does not employ PRTases while NAD+ biosynthesis does eliminates C. The remaining choice D is supported by the general classification of NAD+ as a cofactor. This constitutes a meaningful biological reasoning chain rather than pure database lookup."
  },
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence (468 aa, SHA256 matched) corresponds to UniProt A0A0H2X5R2, annotated as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) from Xanthomonas campestris pv. campestris 8004. The UniProt PATHWAY comment reads: 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1' (ECO:0000269, PubMed:38429435). This is backed by X-ray crystallography (PDB: 7YQO, 7YQP, 7YQQ, 7YQR, 8IGZ) and enzymatic characterization. The expected answer 'Cofactor biosynthesis' directly matches the top-level pathway category."
  },
  "important_caveats": [
    "The UniProt annotation is Swiss-Prot (manually curated) with experimental evidence codes (ECO:0000269, X-ray crystallography), providing strong support for the pathway assignment.",
    "The entry was first released in 2025-02-05; if the benchmark was constructed before that date, the annotation may have been derived from computational inference or transferred annotation rather than the 2024 experimental paper.",
    "The reasoning chain relies on the examinee recognizing PRTase motifs and knowing that IMP de novo does not use PRTases — this is standard biochemistry but still requires specific pathway-level knowledge beyond generic sequence analysis.",
    "The sequence-match is exact (SHA256 identical) between the benchmark input and the UniProt entry, confirming applicability of the annotation to this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eliminated by absence of any relevant enzymatic motifs. Option C (IMP de novo) is eliminated because that pathway does not utilize Type I PRTases. Option D (Cofactor biosynthesis) is the only pathway among the four that employs a Type I PRTase. No other option is defensible given the PRTase identification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (468 aa, SHA256 matched) corresponds to UniProt A0A0H2X5R2, annotated as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) from Xanthomonas campestris pv. campestris 8004. The UniProt PATHWAY comment reads: 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1' (ECO:0000269, PubMed:38429435). This is backed by X-ray crystallography (PDB: 7YQO, 7YQP, 7YQQ, 7YQR, 8IGZ) and enzymatic characterization. The expected answer 'Cofactor biosynthesis' directly matches the top-level pathway category.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark PRTase (phosphoribosyltransferase) superfamily motifs: the 'HDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHT' block, the 'VSDSYDIY' SD-motif, and 'GAWIDVYKDP' — diagnostic of the Type I PRTase fold. This immediately eliminates B (protein ubiquitination: no E2/E3 ligase, RING, or UBA motifs) and A (antifungal biosynthesis: no PKS, NRPS, or terpene cyclase features). Between C and D: the de novo IMP biosynthesis pathway proceeds through amidotransferases, formyltransferases, synthetases, and lyases (e.g., PRPP amidotransferase, GAR synthetase, FGAM synthetase, AIR carboxylase, SAICAR synthetase) and does not employ Type I PRTases. In contrast, NAD+ biosynthesis via the NAM salvage pathway is catalyzed by NAMPT, a canonical Type I PRTase, and NAD+ is universally classified as a cofactor. Thus, identifying the protein as a Type I PRTase and applying standard pathway biochemistry (IMP de novo lacks PRTases; NAD+ is a cofactor) provides a concrete chain of reasoning that selects D over C.",
    "missing_item_specific_fact": "Precise subfamily assignment (NAMPT vs. HGPRT vs. other Type I PRTases) from sequence alone requires detailed knowledge of substrate-binding-site residues; however, the pathway-level distinction (cofactor vs. nucleotide de novo) is resolvable without that specificity because IMP de novo does not use PRTases at all.",
    "reason": "The PRTase fold identification narrows the choices from four to two (C vs. D), and standard biochemistry knowledge that the de novo purine pathway does not employ PRTases while NAD+ biosynthesis does eliminates C. The remaining choice D is supported by the general classification of NAD+ as a cofactor. This constitutes a meaningful biological reasoning chain rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eliminated by absence of any relevant enzymatic motifs. Option C (IMP de novo) is eliminated because that pathway does not utilize Type I PRTases. Option D (Cofactor biosynthesis) is the only pathway among the four that employs a Type I PRTase. No other option is defensible given the PRTase identification."
  },
  "important_caveats": [
    "The UniProt annotation is Swiss-Prot (manually curated) with experimental evidence codes (ECO:0000269, X-ray crystallography), providing strong support for the pathway assignment.",
    "The entry was first released in 2025-02-05; if the benchmark was constructed before that date, the annotation may have been derived from computational inference or transferred annotation rather than the 2024 experimental paper.",
    "The reasoning chain relies on the examinee recognizing PRTase motifs and knowing that IMP de novo does not use PRTases — this is standard biochemistry but still requires specific pathway-level knowledge beyond generic sequence analysis.",
    "The sequence-match is exact (SHA256 identical) between the benchmark input and the UniProt entry, confirming applicability of the annotation to this exact protein."
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

**Accession:** `A0A0H2X5R2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 45. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
"A0A0H2X5R2"
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38429435","source":"PubMed"}],"value":"2.4.2.12"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"Nicotinamide phosphoribosyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NAM phosphoribosyltransferase"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NAMPT"}]}}
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38429435","source":"PubMed"}],"value":"Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1"}]}
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.426700+00:00.  

```json
{"citation":{"authors":["Xu G.","Ma J.","Fang Q.","Peng Q.","Jiao X.","Hu W.","Zhao Q.","Kong Y.","Liu F.","Shi X.","Tang D.J.","Tang J.L.","Ming Z."],"citationCrossReferences":[{"database":"PubMed","id":"38429435"},{"database":"DOI","id":"10.1038/s42003-024-05921-3"}],"citationType":"journal article","firstPage":"255","id":"38429435","journal":"Commun. Biol.","lastPage":"255","publicationDate":"2024","title":"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.","volume":"7"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7YQO","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YQP","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YQQ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7YQR","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8IGZ","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"8004"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) OF APOENZYME; WILD-TYPE IN COMPLEXES WITH NICOTINAMIDE AND BETA-NICOTINAMIDE D-RIBONUCLEOTIDE AND QUADRUPLE MUTANT PHE-175/PHE-224/PHE-291/PHE-332","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT","DOMAIN","PHOSPHORYLATION AT HIS-229","DISRUPTION PHENOTYPE","MUTAGENESIS OF HIS-175; ARG-180; ASP-203; ILE-224; HIS-229; VAL-291; ARG-293; ILE-332; ASP-335 AND ARG-373"]}
```

Source SHA-256: `b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:24:08.378348+00:00.  

```text
ID   NAMPT_XANC8             Reviewed;         468 AA.
AC   A0A0H2X5R2;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-SEP-2015, sequence version 1.
DT   28-JAN-2026, entry version 45.
DE   RecName: Full=Nicotinamide phosphoribosyltransferase {ECO:0000303|PubMed:38429435};
DE            Short=NAM phosphoribosyltransferase {ECO:0000303|PubMed:38429435};
DE            Short=NAMPT {ECO:0000303|PubMed:38429435};
DE            EC=2.4.2.12 {ECO:0000269|PubMed:38429435};
GN   OrderedLocusNames=XC_0719 {ECO:0000312|EMBL:AAY47797.1};
OS   Xanthomonas campestris pv. campestris (strain 8004).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Lysobacterales; Lysobacteraceae; Xanthomonas.
OX   NCBI_TaxID=314565;
```

Source SHA-256: `9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)  
**Locator:** `lines 26-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:24:08.378348+00:00.  

```text
RN   [2] {ECO:0007744|PDB:7YQO, ECO:0007744|PDB:7YQP, ECO:0007744|PDB:7YQQ, ECO:0007744|PDB:7YQR, ECO:0007744|PDB:8IGZ}
RP   X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) OF APOENZYME; WILD-TYPE IN COMPLEXES
RP   WITH NICOTINAMIDE AND BETA-NICOTINAMIDE D-RIBONUCLEOTIDE AND QUADRUPLE
RP   MUTANT PHE-175/PHE-224/PHE-291/PHE-332, FUNCTION, CATALYTIC ACTIVITY,
RP   ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBUNIT,
RP   DOMAIN, PHOSPHORYLATION AT HIS-229, DISRUPTION PHENOTYPE, AND MUTAGENESIS
RP   OF HIS-175; ARG-180; ASP-203; ILE-224; HIS-229; VAL-291; ARG-293; ILE-332;
RP   ASP-335 AND ARG-373.
RC   STRAIN=8004;
RX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;
RA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,
RA   Shi X., Tang D.J., Tang J.L., Ming Z.;
RT   "Structural insights into Xanthomonas campestris pv. campestris NAD+
RT   biosynthesis via the NAM salvage pathway.";
RL   Commun. Biol. 7:255-255(2024).
```

Source SHA-256: `9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)  
**Locator:** `lines 70-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 45 / 1.  
**Retrieved:** 2026-11-02T04:24:08.378348+00:00.  

```text
CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-
CC       ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and
CC       nicotinamide: step 1/1. {ECO:0000269|PubMed:38429435}.
```

Source SHA-256: `9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
