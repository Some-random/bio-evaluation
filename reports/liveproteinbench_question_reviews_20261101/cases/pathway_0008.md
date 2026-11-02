# pathway_0008

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPRPQIKVGVLGATGTVGQRFIELLAAHPYFALHALGASSRSAGQQYARVVRWKLPSPIPDAVRHMVVHECRPDAPGFAECGVVFSGLDADVAGDIENAFRAADLVVYSNAKNYRRDPLCPLIVPLVNPSHLSIIPYQREQLGLKKGYIVTNANCSTTGIVVPLAALEKAFGPLDTVIVTTLQAISGAGYPGVSSLDIMDNVVPLISGEEDKIEWETNKILGGVTPDNKAFDLHAPKQINVSATCTRVPVIDGHTGCVSVKFARSPPPSVAEVENAFREYTCDAQHLGVPSAPAQAIVVHDAPDRPQPRLDKNLHNGACVSVGRIRECPVFDIKFVCLIDNVRLGAATSSIINAEIAVEKGLIQ

[Multiple Choices]
A. Capsule biogenesis
B. iron-sulfur cluster biosynthesis. .
C. Amino-acid biosynthesis
D. L-fucose degradation. .
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

> The supplied sequence exactly matches the reviewed UniProt entry for aspartate-semialdehyde dehydrogenase, annotated in amino-acid biosynthesis, including methionine and threonine biosynthesis. The pathway annotations cite experimental evidence (ECO:0000269).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble metabolic enzyme, but its visible features alone do not reliably distinguish amino-acid biosynthesis from the other offered pathways.


**Missing item-specific fact**

> The protein's identity as aspartate-semialdehyde dehydrogenase, whose pathway role places it in amino-acid biosynthesis, is not stated in the input.


**Reason**

> Selecting C requires identifying the specific enzyme from sequence homology or recalling a protein-specific annotation. That information is not provided by the question; merely predicting from the sequence does not make the choice reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimentally supported annotations place this enzyme in amino-acid biosynthesis; the other options do not present a comparably supported role.


### Important caveats

- The sequence match applies to the supplied 365-residue sequence; the author's exact source snapshot is unknown.
- The pathway evidence is a curated database annotation citing experimental evidence; the cited primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble metabolic enzyme, but its visible features alone do not reliably distinguish amino-acid biosynthesis from the other offered pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as aspartate-semialdehyde dehydrogenase, whose pathway role places it in amino-acid biosynthesis, is not stated in the input.",
    "reason": "Selecting C requires identifying the specific enzyme from sequence homology or recalling a protein-specific annotation. That information is not provided by the question; merely predicting from the sequence does not make the choice reasoning-supported."
  },
  "case_id": "pathway_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry for aspartate-semialdehyde dehydrogenase, annotated in amino-acid biosynthesis, including methionine and threonine biosynthesis. The pathway annotations cite experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The sequence match applies to the supplied 365-residue sequence; the author's exact source snapshot is unknown.",
    "The pathway evidence is a curated database annotation citing experimental evidence; the cited primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimentally supported annotations place this enzyme in amino-acid biosynthesis; the other options do not present a comparably supported role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt entry for aspartate-semialdehyde dehydrogenase, annotated in amino-acid biosynthesis, including methionine and threonine biosynthesis. The pathway annotations cite experimental evidence (ECO:0000269).",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble metabolic enzyme, but its visible features alone do not reliably distinguish amino-acid biosynthesis from the other offered pathways.",
    "missing_item_specific_fact": "The protein's identity as aspartate-semialdehyde dehydrogenase, whose pathway role places it in amino-acid biosynthesis, is not stated in the input.",
    "reason": "Selecting C requires identifying the specific enzyme from sequence homology or recalling a protein-specific annotation. That information is not provided by the question; merely predicting from the sequence does not make the choice reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimentally supported annotations place this enzyme in amino-acid biosynthesis; the other options do not present a comparably supported role."
  },
  "important_caveats": [
    "The sequence match applies to the supplied 365-residue sequence; the author's exact source snapshot is unknown.",
    "The pathway evidence is a curated database annotation citing experimental evidence; the cited primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5KPK7 is experimentally characterized as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with evidence codes ECO:0000269 (PubMed:26527262 crystal structure, PubMed:29608391 enzymology). The PATHWAY annotations explicitly state 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The sequence matches (SHA256 identical) in both current and historical (v121) records.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold NAD(P)-binding motif (GVLGATGTVG at positions ~9-18), identifying this as a NAD(P)-dependent dehydrogenase. Among the four choices: (A) Capsule biogenesis involves glycosyltransferases and polymerases, not NAD(P)-dependent dehydrogenases; (B) Iron-sulfur cluster biosynthesis involves scaffold proteins (e.g., Isu/Ufd), chaperones, and Fe-S assembly factors, not Rossmann-fold dehydrogenases; (D) Canonical L-fucose degradation involves fucose mutarotase, fucose kinase, and L-fucose-1-phosphate aldolase—none are NAD(P)-dependent dehydrogenases. Amino-acid biosynthesis (C) is the pathway most commonly associated with NAD(P)-dependent reduction steps (e.g., aspartate-semialdehyde dehydrogenase, glutamate dehydrogenase, dihydrodipicolinate reductase). Thus, identifying the Rossmann fold and eliminating the three non-dehydrogenase pathways provides a defensible reasoning path to C.


**Missing item-specific fact**

> Precise identification of the enzyme as aspartate-semialdehyde dehydrogenase (rather than another NADPH-dependent dehydrogenase in amino-acid biosynthesis) would require recognizing specific ASADH catalytic residues (e.g., the catalytic Cys) or family-specific motifs, but this level of specificity is not required to select among the four given choices.


**Reason**

> The visible Rossmann-fold motif provides a concrete, sequence-based biological argument that the protein is a dehydrogenase. General pathway biochemistry then allows elimination of capsule biogenesis, Fe-S cluster assembly, and L-fucose degradation as pathways not centered on NAD(P)-dependent dehydrogenases, leaving amino-acid biosynthesis as the only consistent option. This constitutes meaningful reasoning rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the Rossmann-fold dehydrogenase identification, options A, B, and D are clearly inconsistent with the enzyme class. No other option is defensible.


### Important caveats

- The UniProt annotation is supported by experimental evidence (X-ray crystallography PDB 5CEF, enzymatic assays in PubMed:26527262 and PubMed:29608391), not merely computational inference.
- The reasoning path relies on recognizing the Rossmann fold and applying general pathway biochemistry; it does not require memorizing this specific protein's database entry.
- The author key 'Amino-acid biosynthesis' matches the UniProt PATHWAY annotation verbatim.
- All reviewer evidence is sequence-matched (SHA256 identical) to the benchmark sequence, confirming applicability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif (GVLGATGTVG at positions ~9-18), identifying this as a NAD(P)-dependent dehydrogenase. Among the four choices: (A) Capsule biogenesis involves glycosyltransferases and polymerases, not NAD(P)-dependent dehydrogenases; (B) Iron-sulfur cluster biosynthesis involves scaffold proteins (e.g., Isu/Ufd), chaperones, and Fe-S assembly factors, not Rossmann-fold dehydrogenases; (D) Canonical L-fucose degradation involves fucose mutarotase, fucose kinase, and L-fucose-1-phosphate aldolase—none are NAD(P)-dependent dehydrogenases. Amino-acid biosynthesis (C) is the pathway most commonly associated with NAD(P)-dependent reduction steps (e.g., aspartate-semialdehyde dehydrogenase, glutamate dehydrogenase, dihydrodipicolinate reductase). Thus, identifying the Rossmann fold and eliminating the three non-dehydrogenase pathways provides a defensible reasoning path to C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the enzyme as aspartate-semialdehyde dehydrogenase (rather than another NADPH-dependent dehydrogenase in amino-acid biosynthesis) would require recognizing specific ASADH catalytic residues (e.g., the catalytic Cys) or family-specific motifs, but this level of specificity is not required to select among the four given choices.",
    "reason": "The visible Rossmann-fold motif provides a concrete, sequence-based biological argument that the protein is a dehydrogenase. General pathway biochemistry then allows elimination of capsule biogenesis, Fe-S cluster assembly, and L-fucose degradation as pathways not centered on NAD(P)-dependent dehydrogenases, leaving amino-acid biosynthesis as the only consistent option. This constitutes meaningful reasoning rather than pure lookup."
  },
  "case_id": "pathway_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5KPK7 is experimentally characterized as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with evidence codes ECO:0000269 (PubMed:26527262 crystal structure, PubMed:29608391 enzymology). The PATHWAY annotations explicitly state 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The sequence matches (SHA256 identical) in both current and historical (v121) records."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (X-ray crystallography PDB 5CEF, enzymatic assays in PubMed:26527262 and PubMed:29608391), not merely computational inference.",
    "The reasoning path relies on recognizing the Rossmann fold and applying general pathway biochemistry; it does not require memorizing this specific protein's database entry.",
    "The author key 'Amino-acid biosynthesis' matches the UniProt PATHWAY annotation verbatim.",
    "All reviewer evidence is sequence-matched (SHA256 identical) to the benchmark sequence, confirming applicability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the Rossmann-fold dehydrogenase identification, options A, B, and D are clearly inconsistent with the enzyme class. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5KPK7 is experimentally characterized as Aspartate-semialdehyde dehydrogenase (EC 1.2.1.11) with evidence codes ECO:0000269 (PubMed:26527262 crystal structure, PubMed:29608391 enzymology). The PATHWAY annotations explicitly state 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3' and 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5.' The sequence matches (SHA256 identical) in both current and historical (v121) records.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold NAD(P)-binding motif (GVLGATGTVG at positions ~9-18), identifying this as a NAD(P)-dependent dehydrogenase. Among the four choices: (A) Capsule biogenesis involves glycosyltransferases and polymerases, not NAD(P)-dependent dehydrogenases; (B) Iron-sulfur cluster biosynthesis involves scaffold proteins (e.g., Isu/Ufd), chaperones, and Fe-S assembly factors, not Rossmann-fold dehydrogenases; (D) Canonical L-fucose degradation involves fucose mutarotase, fucose kinase, and L-fucose-1-phosphate aldolase—none are NAD(P)-dependent dehydrogenases. Amino-acid biosynthesis (C) is the pathway most commonly associated with NAD(P)-dependent reduction steps (e.g., aspartate-semialdehyde dehydrogenase, glutamate dehydrogenase, dihydrodipicolinate reductase). Thus, identifying the Rossmann fold and eliminating the three non-dehydrogenase pathways provides a defensible reasoning path to C.",
    "missing_item_specific_fact": "Precise identification of the enzyme as aspartate-semialdehyde dehydrogenase (rather than another NADPH-dependent dehydrogenase in amino-acid biosynthesis) would require recognizing specific ASADH catalytic residues (e.g., the catalytic Cys) or family-specific motifs, but this level of specificity is not required to select among the four given choices.",
    "reason": "The visible Rossmann-fold motif provides a concrete, sequence-based biological argument that the protein is a dehydrogenase. General pathway biochemistry then allows elimination of capsule biogenesis, Fe-S cluster assembly, and L-fucose degradation as pathways not centered on NAD(P)-dependent dehydrogenases, leaving amino-acid biosynthesis as the only consistent option. This constitutes meaningful reasoning rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the Rossmann-fold dehydrogenase identification, options A, B, and D are clearly inconsistent with the enzyme class. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt annotation is supported by experimental evidence (X-ray crystallography PDB 5CEF, enzymatic assays in PubMed:26527262 and PubMed:29608391), not merely computational inference.",
    "The reasoning path relies on recognizing the Rossmann fold and applying general pathway biochemistry; it does not require memorizing this specific protein's database entry.",
    "The author key 'Amino-acid biosynthesis' matches the UniProt PATHWAY annotation verbatim.",
    "All reviewer evidence is sequence-matched (SHA256 identical) to the benchmark sequence, confirming applicability."
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

**Accession:** `Q5KPK7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 121. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26527262","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29608391","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26527262","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; L-homoserine from L-aspartate: step 2/3"}]}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26527262","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 2/5"}]}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"citation":{"authors":["Dahal G.P.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"29608391"},{"database":"DOI","id":"10.1177/2472555218767844"}],"citationType":"journal article","firstPage":"520","id":"29608391","journal":"SLAS Discovery","lastPage":"531","publicationDate":"2018","title":"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.","volume":"23"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION"]}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"citation":{"authors":["Dahal G.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"26527262"},{"database":"DOI","id":"10.1107/s2053230x15017495"}],"citationType":"journal article","firstPage":"1365","id":"26527262","journal":"Acta Crystallogr. F Struct. Biol. Commun.","lastPage":"1371","publicationDate":"2015","title":"Structure of a fungal form of aspartate semialdehyde dehydrogenase from Cryptococcus neoformans.","volume":"71"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5CEF","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.60 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT"]}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
ID   DHAS_CRYD1              Reviewed;         365 AA.
AC   Q5KPK7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-FEB-2005, sequence version 1.
DT   28-JAN-2026, entry version 121.
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:26527262, ECO:0000269|PubMed:29608391};
GN   OrderedLocusNames=CNA02450 {ECO:0000312|EMBL:AAW40826.1};
OS   Cryptococcus deneoformans (strain JEC21 / ATCC MYA-565) (Cryptococcus
OS   neoformans var. neoformans serotype D).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=214684 {ECO:0000312|Proteomes:UP000002149};
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 39-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.
RX   PubMed=29608391; DOI=10.1177/2472555218767844;
RA   Dahal G.P., Viola R.E.;
RT   "A Fragment Library Screening Approach to Identify Selective Inhibitors
RT   against an Essential Fungal Enzyme.";
RL   SLAS Discovery 23:520-531(2018).
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 46-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
RN   [4] {ECO:0007744|PDB:5CEF}
RP   X-RAY CRYSTALLOGRAPHY (2.60 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.
RX   PubMed=26527262; DOI=10.1107/s2053230x15017495;
RA   Dahal G., Viola R.E.;
RT   "Structure of a fungal form of aspartate semialdehyde dehydrogenase from
RT   Cryptococcus neoformans.";
RL   Acta Crystallogr. F Struct. Biol. Commun. 71:1365-1371(2015).
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 81-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo
CC       pathway; L-homoserine from L-aspartate: step 2/3.
CC       {ECO:0000269|PubMed:26527262}.
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 84-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine
CC       from L-aspartate: step 2/5. {ECO:0000269|PubMed:26527262}.
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
