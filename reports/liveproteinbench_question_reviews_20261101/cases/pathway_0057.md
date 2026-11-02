# pathway_0057

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGETTQLDLSVKAVGWGAADASGTLQPIKFYRRTPGERDVKIRVLYCGVCNFDMEMVRNKWGFTRYPYVFGHETAGEVIEVGSKVQKFKVGDKVGVGCMVGSCGKCFNCQNGMENYCPEPNMADGSVYREQQGEPSFGGCSNVMVVDEKFVLRWPENLPQDTGVPLLCAGIVVYSPMKYMGLDKPGKHIGVIGLGGLGSIAVKFIKAFGGKATVISTSKRKEKEAIEEHGADAFVVNTDTEKLQALAGTMDGVVDTTPGGRTPMSLMLNLLKFDGVVLLVGAPETLFELPVQPLILGRRKIIGSSTGGLKEYQETLDFAAQHNIVCDTEVIGIDYLSTAMERIKNLDVKYRFAIDIGNTLKYED

[Multiple Choices]
A. Alkaloid biosynthesis
B. protein glycosylation. .
C. Pyrimidine metabolism
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

> The matched sequence is annotated as geissoschizine synthase in the ajmaline/alkaloid biosynthesis pathway. The pathway annotation carries an experimental-evidence code and is also present in the historical entry available by the stated cutoff; this supports choice A, though the primary paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H1](#evidence-h1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently specific, defensible basis to identify its pathway as alkaloid biosynthesis rather than the other choices. Recognizing the protein's exact identity would require protein-specific knowledge.


**Missing item-specific fact**

> The protein-specific functional annotation identifying this sequence as geissoschizine synthase and linking it to ajmaline/alkaloid biosynthesis.


**Reason**

> The supplied sequence and choices do not state the organism or protein function. A pathway selection depends on an item-specific identification or annotation absent from the input, not merely on general pathway knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports alkaloid biosynthesis, and the alternatives describe distinct pathways. The sequence alone may not distinguish them, but no alternative is independently supported by the supplied information.


### Important caveats

- Reviewer-only accession and annotation evidence was not available to the evaluated model.
- The sequence matches both the historical and current UniProt sequence records; the author's exact source snapshot is unknown.
- The pathway annotation carries experimental evidence coding, but the cited primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, defensible basis to identify its pathway as alkaloid biosynthesis rather than the other choices. Recognizing the protein's exact identity would require protein-specific knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation identifying this sequence as geissoschizine synthase and linking it to ajmaline/alkaloid biosynthesis.",
    "reason": "The supplied sequence and choices do not state the organism or protein function. A pathway selection depends on an item-specific identification or annotation absent from the input, not merely on general pathway knowledge."
  },
  "case_id": "pathway_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H1"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as geissoschizine synthase in the ajmaline/alkaloid biosynthesis pathway. The pathway annotation carries an experimental-evidence code and is also present in the historical entry available by the stated cutoff; this supports choice A, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence was not available to the evaluated model.",
    "The sequence matches both the historical and current UniProt sequence records; the author's exact source snapshot is unknown.",
    "The pathway annotation carries experimental evidence coding, but the cited primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports alkaloid biosynthesis, and the alternatives describe distinct pathways. The sequence alone may not distinguish them, but no alternative is independently supported by the supplied information."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as geissoschizine synthase in the ajmaline/alkaloid biosynthesis pathway. The pathway annotation carries an experimental-evidence code and is also present in the historical entry available by the stated cutoff; this supports choice A, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H3", "H1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, defensible basis to identify its pathway as alkaloid biosynthesis rather than the other choices. Recognizing the protein's exact identity would require protein-specific knowledge.",
    "missing_item_specific_fact": "The protein-specific functional annotation identifying this sequence as geissoschizine synthase and linking it to ajmaline/alkaloid biosynthesis.",
    "reason": "The supplied sequence and choices do not state the organism or protein function. A pathway selection depends on an item-specific identification or annotation absent from the input, not merely on general pathway knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports alkaloid biosynthesis, and the alternatives describe distinct pathways. The sequence alone may not distinguish them, but no alternative is independently supported by the supplied information."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence was not available to the evaluated model.",
    "The sequence matches both the historical and current UniProt sequence records; the author's exact source snapshot is unknown.",
    "The pathway annotation carries experimental evidence coding, but the cited primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina carries the explicit PATHWAY annotation 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:38212296). The benchmark sequence SHA256 matches the source sequence exactly (365 aa). Choice A directly corresponds to the annotated pathway.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains Rossmann-fold-like motifs (e.g., 'GGLGSIAVK', 'GSSTGGL', 'GAPETL') suggesting an NAD(P)-dependent oxidoreductase, which could weakly argue against protein glycosylation (B, typically glycosyltransferases) and pyrimidine metabolism (C, different enzyme classes). However, this does not positively identify 'alkaloid biosynthesis' (A) over other oxidoreductase-containing pathways. No sequence-intrinsic feature uniquely points to terpene indole alkaloid biosynthesis.


**Missing item-specific fact**

> The identity of this specific protein as Geissoschizine synthase (EC 1.3.1.36) in the ajmaline/alkaloid biosynthetic pathway of Rauvolfia serpentina, and the organism context, are required to select A over other plausible oxidoreductase pathways. The question provides no organism name or enzyme context.


**Reason**

> While the sequence motifs hint at an oxidoreductase class, the specific pathway assignment to 'Alkaloid biosynthesis' cannot be derived from general biological reasoning on the sequence alone. It requires knowing this particular enzyme's identity and its role in Rauvolfia's monoterpene indole alkaloid pathway—a protein-specific database/experimental fact absent from the model input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only A matches the actual annotation. B (glycosylation), C (pyrimidine metabolism), and D (histidine biosynthesis step 4) are clearly inconsistent with an oxidoreductase of this type. The distractors are sufficiently distinct that the question is not ambiguous in terms of which answer is correct, though the reasoning path to A is not derivable from sequence alone.


### Important caveats

- The UniProt entry was first published 2025-06-18; if the benchmark was constructed before that date, the author may have used a different source or the entry may not have existed at construction time.
- The EC number assignment carries evidence code ECO:0000250 (similarity to W8JWW7), meaning the enzymatic classification is by homology, not direct experimental characterization of this exact sequence.
- The pathway annotation itself carries experimental evidence (ECO:0000269) from the 2024 Nat. Commun. paper, which is robust.
- The organism (Rauvolfia serpentina) is not provided in the question input, removing a strong contextual clue for alkaloid biosynthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains Rossmann-fold-like motifs (e.g., 'GGLGSIAVK', 'GSSTGGL', 'GAPETL') suggesting an NAD(P)-dependent oxidoreductase, which could weakly argue against protein glycosylation (B, typically glycosyltransferases) and pyrimidine metabolism (C, different enzyme classes). However, this does not positively identify 'alkaloid biosynthesis' (A) over other oxidoreductase-containing pathways. No sequence-intrinsic feature uniquely points to terpene indole alkaloid biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of this specific protein as Geissoschizine synthase (EC 1.3.1.36) in the ajmaline/alkaloid biosynthetic pathway of Rauvolfia serpentina, and the organism context, are required to select A over other plausible oxidoreductase pathways. The question provides no organism name or enzyme context.",
    "reason": "While the sequence motifs hint at an oxidoreductase class, the specific pathway assignment to 'Alkaloid biosynthesis' cannot be derived from general biological reasoning on the sequence alone. It requires knowing this particular enzyme's identity and its role in Rauvolfia's monoterpene indole alkaloid pathway—a protein-specific database/experimental fact absent from the model input."
  },
  "case_id": "pathway_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina carries the explicit PATHWAY annotation 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:38212296). The benchmark sequence SHA256 matches the source sequence exactly (365 aa). Choice A directly corresponds to the annotated pathway."
  },
  "important_caveats": [
    "The UniProt entry was first published 2025-06-18; if the benchmark was constructed before that date, the author may have used a different source or the entry may not have existed at construction time.",
    "The EC number assignment carries evidence code ECO:0000250 (similarity to W8JWW7), meaning the enzymatic classification is by homology, not direct experimental characterization of this exact sequence.",
    "The pathway annotation itself carries experimental evidence (ECO:0000269) from the 2024 Nat. Commun. paper, which is robust.",
    "The organism (Rauvolfia serpentina) is not provided in the question input, removing a strong contextual clue for alkaloid biosynthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only A matches the actual annotation. B (glycosylation), C (pyrimidine metabolism), and D (histidine biosynthesis step 4) are clearly inconsistent with an oxidoreductase of this type. The distractors are sufficiently distinct that the question is not ambiguous in terms of which answer is correct, though the reasoning path to A is not derivable from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ1 (Geissoschizine synthase, EC 1.3.1.36) from Rauvolfia serpentina carries the explicit PATHWAY annotation 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:38212296). The benchmark sequence SHA256 matches the source sequence exactly (365 aa). Choice A directly corresponds to the annotated pathway.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains Rossmann-fold-like motifs (e.g., 'GGLGSIAVK', 'GSSTGGL', 'GAPETL') suggesting an NAD(P)-dependent oxidoreductase, which could weakly argue against protein glycosylation (B, typically glycosyltransferases) and pyrimidine metabolism (C, different enzyme classes). However, this does not positively identify 'alkaloid biosynthesis' (A) over other oxidoreductase-containing pathways. No sequence-intrinsic feature uniquely points to terpene indole alkaloid biosynthesis.",
    "missing_item_specific_fact": "The identity of this specific protein as Geissoschizine synthase (EC 1.3.1.36) in the ajmaline/alkaloid biosynthetic pathway of Rauvolfia serpentina, and the organism context, are required to select A over other plausible oxidoreductase pathways. The question provides no organism name or enzyme context.",
    "reason": "While the sequence motifs hint at an oxidoreductase class, the specific pathway assignment to 'Alkaloid biosynthesis' cannot be derived from general biological reasoning on the sequence alone. It requires knowing this particular enzyme's identity and its role in Rauvolfia's monoterpene indole alkaloid pathway—a protein-specific database/experimental fact absent from the model input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only A matches the actual annotation. B (glycosylation), C (pyrimidine metabolism), and D (histidine biosynthesis step 4) are clearly inconsistent with an oxidoreductase of this type. The distractors are sufficiently distinct that the question is not ambiguous in terms of which answer is correct, though the reasoning path to A is not derivable from sequence alone."
  },
  "important_caveats": [
    "The UniProt entry was first published 2025-06-18; if the benchmark was constructed before that date, the author may have used a different source or the entry may not have existed at construction time.",
    "The EC number assignment carries evidence code ECO:0000250 (similarity to W8JWW7), meaning the enzymatic classification is by homology, not direct experimental characterization of this exact sequence.",
    "The pathway annotation itself carries experimental evidence (ECO:0000269) from the 2024 Nat. Commun. paper, which is robust.",
    "The organism (Rauvolfia serpentina) is not provided in the question input, removing a strong contextual clue for alkaloid biosynthesis."
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

**Accession:** `P0DXJ1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
"P0DXJ1"
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
{"commonName":"Serpentine wood","lineage":["Eukaryota","Viridiplantae","Streptophyta","Embryophyta","Tracheophyta","Spermatophyta","Magnoliopsida","eudicotyledons","Gunneridae","Pentapetalae","asterids","lamiids","Gentianales","Apocynaceae","Rauvolfioideae","Vinceae","Rauvolfiinae","Rauvolfia"],"scientificName":"Rauvolfia serpentina","synonyms":["Ophioxylon serpentinum"],"taxonId":4060}
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"W8JWW7","source":"UniProtKB"}],"value":"1.3.1.36"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Geissoschizine synthase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsGS"}]}}
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:29.884516+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WKU61919.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","BIOTECHNOLOGY","TISSUE SPECIFICITY","PATHWAY"]}
```

Source SHA-256: `6eda11173d33f799125da302047e13f2dbcebc81de87a50235cb3bf62d181ed5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:32.265438+00:00.  

```text
ID   GS_RAUSE                Reviewed;         365 AA.
AC   P0DXJ1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=Geissoschizine synthase {ECO:0000303|PubMed:38212296};
DE            Short=RsGS {ECO:0000303|PubMed:38212296};
DE            EC=1.3.1.36 {ECO:0000250|UniProtKB:W8JWW7};
GN   Name=GS {ECO:0000303|PubMed:38212296};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)  
**Locator:** `lines 16-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:32.265438+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:WKU61919.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, BIOTECHNOLOGY, TISSUE SPECIFICITY,
RP   AND PATHWAY.
RX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;
RA   Guo J., Gao D., Lian J., Qu Y.;
RT   "De novo biosynthesis of antiarrhythmic alkaloid ajmaline.";
RL   Nat. Commun. 15:457-457(2024).
```

Source SHA-256: `7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ1?format=txt&versions=2)  
**Locator:** `lines 42-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-02T04:29:32.265438+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `7ba973e38966d3d8089bcd88dfc1f173357dd4d1bed310495b9a3912403794b7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
