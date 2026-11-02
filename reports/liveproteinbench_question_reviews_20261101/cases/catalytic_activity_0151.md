# catalytic_activity_0151

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASSDLEAATALKVQGNKAFGQHEWPTAVDFYTQAIAKYDREPSFFSNRAQAHIKLEAYGFAIADATKALELDPAYTKAYWRRALANTAILNYKDALRDFKVVAKREPNNRDAKVKLADCEKLVRRMEFEKAIEVGDPPSAFEDLDIDAIAVDDSYDGVRLEKEMTQEFIDDMIERFKNGKKIHRKYAFQIVKAVKDIVYAEPTMVEIGVDQGTKLTVCGDTHGQFFDLLEIFRLNGYPSEKHAYLFNGDFVDRGSWSTEIALLLYAYKWLRPNGIFLNRGNHETDDMNKVYGFEGECKAKYNERMFKVFSESFSALPLATLIGNKYLVLHGGLFSDDNTSLDDIRKLDRHNQRQPGQQGLMMEMLWTDPQTEPGRGPSKRGVGLQFGPDVTKRFCEKNGLEAIIRSHEVRMEGYEVEHDGRCITVFSAPKYCDTTENKGAFINVGPELKLDFQVFEAVPHPDIKPMAYAQNSIMSMM

[Multiple Choices]
A. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
B. tyramine + reduced [NADPH--hemoprotein reductase] + O2 = dopamine + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
C. a secondary alcohol + NAD(+) = a ketone + NADH + H(+)
D. 2 a Fe(II)-siderophore + NADP(+) + H(+) = 2 a Fe(III)-siderophore + NADPH
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

> The sequence-matched UniProt record annotates this protein with the serine dephosphorylation reaction in choice A, citing PubMed 17475320. This supports the key, though the supplied evidence is an annotation tied to a publication rather than an independently reviewed assay report.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains conserved protein-phosphatase catalytic motifs, including GDTHG, consistent with a phosphoprotein phosphatase. Among the choices, A is the protein dephosphorylation reaction; the others describe unrelated enzyme activities.


**Missing item-specific fact**

> The exact serine and threonine reaction annotations are not supplied, so the sequence alone does not establish which residue-specific reactions are recorded for this protein. That detail is not needed to distinguish A from the other choices.


**Reason**

> The conserved catalytic signatures provide a meaningful basis to identify the enzyme as a protein phosphatase and select the matching reaction class from the options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A among the listed options describes protein dephosphorylation. The annotated protein is also assigned a threonyl dephosphorylation reaction, but that reaction is not offered as a separate choice.


### Important caveats

- The sequence match and UniProt reaction annotation support the key; the annotation cites a publication, but the primary experimental evidence was not independently assessed here.
- The record annotates both serine and threonine dephosphorylation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains conserved protein-phosphatase catalytic motifs, including GDTHG, consistent with a phosphoprotein phosphatase. Among the choices, A is the protein dephosphorylation reaction; the others describe unrelated enzyme activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact serine and threonine reaction annotations are not supplied, so the sequence alone does not establish which residue-specific reactions are recorded for this protein. That detail is not needed to distinguish A from the other choices.",
    "reason": "The conserved catalytic signatures provide a meaningful basis to identify the enzyme as a protein phosphatase and select the matching reaction class from the options."
  },
  "case_id": "catalytic_activity_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein with the serine dephosphorylation reaction in choice A, citing PubMed 17475320. This supports the key, though the supplied evidence is an annotation tied to a publication rather than an independently reviewed assay report."
  },
  "important_caveats": [
    "The sequence match and UniProt reaction annotation support the key; the annotation cites a publication, but the primary experimental evidence was not independently assessed here.",
    "The record annotates both serine and threonine dephosphorylation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the listed options describes protein dephosphorylation. The annotated protein is also assigned a threonyl dephosphorylation reaction, but that reaction is not offered as a separate choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein with the serine dephosphorylation reaction in choice A, citing PubMed 17475320. This supports the key, though the supplied evidence is an annotation tied to a publication rather than an independently reviewed assay report.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains conserved protein-phosphatase catalytic motifs, including GDTHG, consistent with a phosphoprotein phosphatase. Among the choices, A is the protein dephosphorylation reaction; the others describe unrelated enzyme activities.",
    "missing_item_specific_fact": "The exact serine and threonine reaction annotations are not supplied, so the sequence alone does not establish which residue-specific reactions are recorded for this protein. That detail is not needed to distinguish A from the other choices.",
    "reason": "The conserved catalytic signatures provide a meaningful basis to identify the enzyme as a protein phosphatase and select the matching reaction class from the options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A among the listed options describes protein dephosphorylation. The annotated protein is also assigned a threonyl dephosphorylation reaction, but that reaction is not offered as a separate choice."
  },
  "important_caveats": [
    "The sequence match and UniProt reaction annotation support the key; the annotation cites a publication, but the primary experimental evidence was not independently assessed here.",
    "The record annotates both serine and threonine dephosphorylation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q2U919 (PPP5_ASPOR, Serine/threonine-protein phosphatase T from Aspergillus oryzae, EC 3.1.3.16). The catalytic activity annotation explicitly lists 'O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate' with evidence code ECO:0000305|PubMed:17475320 (experimental data from Feng et al. 2007). Choice A matches this annotation verbatim. The protein also catalyzes the analogous threonyl reaction, but that reaction is not among the choices.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple features diagnostic of the PPP-family (PP1/PP2A/PP5) phosphatase superfamily: (1) a GDxHG-like motif ('GDTHGQ') corresponding to the conserved metal-binding catalytic core GDxVHGN of PPP phosphatases; (2) additional conserved HG motifs ('HGGLFSDD', 'HDGRC') forming the binuclear metal site; (3) C-terminal PPP-family signatures ('GPELKLDFQVFEAVPHPDIKPMAYAQNSIMSMM'). Additionally, the N-terminal region displays the helical-repeat pattern characteristic of TPR domains, which are diagnostic of PP5 specifically. PPP-family enzymes are protein Ser/Thr phosphatases that hydrolyze phosphoester bonds on phosphorylated serine/threonine residues. This reasoning distinguishes Choice A (phosphatase reaction) from Choice B (cytochrome P450 monooxygenase, which requires an FxxGxxxCxG heme-binding motif absent here), Choice C (NAD-dependent alcohol dehydrogenase, requiring a Rossmann-fold NAD-binding motif absent here), and Choice D (siderophore oxidase, a completely different enzyme class).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the PPP-family catalytic motif (GDxHG + additional HG residues) and TPR domain architecture constitutes general biochemical knowledge about enzyme superfamilies. A knowledgeable student can identify the enzyme class from sequence motifs without needing to memorize this specific protein's annotation. The distractors represent entirely different enzyme classes with incompatible sequence signatures.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the enzyme catalyzes both seryl and threonyl dephosphorylation (EC 3.1.3.16), only the seryl reaction appears among the choices. The other three options (P450 monooxygenase, alcohol dehydrogenase, siderophore oxidase) are mechanistically and structurally incompatible with a PPP-family phosphatase, leaving no ambiguity.


### Important caveats

- The GDxHG motif in this sequence ('GDTHGQ') is somewhat divergent from the canonical PPP-family GDxVHGN motif; identification requires familiarity with PP5-specific sequence variation.
- The evidence code ECO:0000305 indicates the catalytic activity was experimentally determined (PubMed:17475320), but the protein name annotation itself is transferred by similarity (ECO:0000250 from P53043, human PP5).
- The reviewer-only evidence was not available to the evaluated model; the model must rely on sequence motif recognition and general biochemical knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple features diagnostic of the PPP-family (PP1/PP2A/PP5) phosphatase superfamily: (1) a GDxHG-like motif ('GDTHGQ') corresponding to the conserved metal-binding catalytic core GDxVHGN of PPP phosphatases; (2) additional conserved HG motifs ('HGGLFSDD', 'HDGRC') forming the binuclear metal site; (3) C-terminal PPP-family signatures ('GPELKLDFQVFEAVPHPDIKPMAYAQNSIMSMM'). Additionally, the N-terminal region displays the helical-repeat pattern characteristic of TPR domains, which are diagnostic of PP5 specifically. PPP-family enzymes are protein Ser/Thr phosphatases that hydrolyze phosphoester bonds on phosphorylated serine/threonine residues. This reasoning distinguishes Choice A (phosphatase reaction) from Choice B (cytochrome P450 monooxygenase, which requires an FxxGxxxCxG heme-binding motif absent here), Choice C (NAD-dependent alcohol dehydrogenase, requiring a Rossmann-fold NAD-binding motif absent here), and Choice D (siderophore oxidase, a completely different enzyme class).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PPP-family catalytic motif (GDxHG + additional HG residues) and TPR domain architecture constitutes general biochemical knowledge about enzyme superfamilies. A knowledgeable student can identify the enzyme class from sequence motifs without needing to memorize this specific protein's annotation. The distractors represent entirely different enzyme classes with incompatible sequence signatures."
  },
  "case_id": "catalytic_activity_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q2U919 (PPP5_ASPOR, Serine/threonine-protein phosphatase T from Aspergillus oryzae, EC 3.1.3.16). The catalytic activity annotation explicitly lists 'O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate' with evidence code ECO:0000305|PubMed:17475320 (experimental data from Feng et al. 2007). Choice A matches this annotation verbatim. The protein also catalyzes the analogous threonyl reaction, but that reaction is not among the choices."
  },
  "important_caveats": [
    "The GDxHG motif in this sequence ('GDTHGQ') is somewhat divergent from the canonical PPP-family GDxVHGN motif; identification requires familiarity with PP5-specific sequence variation.",
    "The evidence code ECO:0000305 indicates the catalytic activity was experimentally determined (PubMed:17475320), but the protein name annotation itself is transferred by similarity (ECO:0000250 from P53043, human PP5).",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely on sequence motif recognition and general biochemical knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the enzyme catalyzes both seryl and threonyl dephosphorylation (EC 3.1.3.16), only the seryl reaction appears among the choices. The other three options (P450 monooxygenase, alcohol dehydrogenase, siderophore oxidase) are mechanistically and structurally incompatible with a PPP-family phosphatase, leaving no ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q2U919 (PPP5_ASPOR, Serine/threonine-protein phosphatase T from Aspergillus oryzae, EC 3.1.3.16). The catalytic activity annotation explicitly lists 'O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate' with evidence code ECO:0000305|PubMed:17475320 (experimental data from Feng et al. 2007). Choice A matches this annotation verbatim. The protein also catalyzes the analogous threonyl reaction, but that reaction is not among the choices.",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple features diagnostic of the PPP-family (PP1/PP2A/PP5) phosphatase superfamily: (1) a GDxHG-like motif ('GDTHGQ') corresponding to the conserved metal-binding catalytic core GDxVHGN of PPP phosphatases; (2) additional conserved HG motifs ('HGGLFSDD', 'HDGRC') forming the binuclear metal site; (3) C-terminal PPP-family signatures ('GPELKLDFQVFEAVPHPDIKPMAYAQNSIMSMM'). Additionally, the N-terminal region displays the helical-repeat pattern characteristic of TPR domains, which are diagnostic of PP5 specifically. PPP-family enzymes are protein Ser/Thr phosphatases that hydrolyze phosphoester bonds on phosphorylated serine/threonine residues. This reasoning distinguishes Choice A (phosphatase reaction) from Choice B (cytochrome P450 monooxygenase, which requires an FxxGxxxCxG heme-binding motif absent here), Choice C (NAD-dependent alcohol dehydrogenase, requiring a Rossmann-fold NAD-binding motif absent here), and Choice D (siderophore oxidase, a completely different enzyme class).",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PPP-family catalytic motif (GDxHG + additional HG residues) and TPR domain architecture constitutes general biochemical knowledge about enzyme superfamilies. A knowledgeable student can identify the enzyme class from sequence motifs without needing to memorize this specific protein's annotation. The distractors represent entirely different enzyme classes with incompatible sequence signatures."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the enzyme catalyzes both seryl and threonyl dephosphorylation (EC 3.1.3.16), only the seryl reaction appears among the choices. The other three options (P450 monooxygenase, alcohol dehydrogenase, siderophore oxidase) are mechanistically and structurally incompatible with a PPP-family phosphatase, leaving no ambiguity."
  },
  "important_caveats": [
    "The GDxHG motif in this sequence ('GDTHGQ') is somewhat divergent from the canonical PPP-family GDxVHGN motif; identification requires familiarity with PP5-specific sequence variation.",
    "The evidence code ECO:0000305 indicates the catalytic activity was experimentally determined (PubMed:17475320), but the protein name annotation itself is transferred by similarity (ECO:0000250 from P53043, human PP5).",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely on sequence motif recognition and general biochemical knowledge."
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

**Accession:** `Q2U919` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 127. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
"Q2U919"
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17475320","source":"PubMed"}],"value":"AoPPT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53043","source":"UniProtKB"}],"value":"Serine/threonine-protein phosphatase T"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53043","source":"UniProtKB"}],"value":"PPT"}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"citation":{"authors":["Feng B.","Zhao C.H.","Tanaka S.","Imanaka H.","Imamura K.","Nakanishi K."],"citationCrossReferences":[{"database":"PubMed","id":"17475320"},{"database":"DOI","id":"10.1016/j.ijbiomac.2007.03.005"}],"citationType":"journal article","firstPage":"281","id":"17475320","journal":"Int. J. Biol. Macromol.","lastPage":"285","publicationDate":"2007","title":"TPR domain of Ser/Thr phosphatase of Aspergillus oryzae shows no auto-inhibitory effect on the dephosphorylation activity.","volume":"41"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"17475320","source":"PubMed"}],"type":"STRAIN","value":"AGL142-72"}],"referenceNumber":2,"referencePositions":["CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
ID   PPP5_ASPOR              Reviewed;         478 AA.
AC   Q2U919;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   24-JAN-2006, sequence version 1.
DT   28-JAN-2026, entry version 127.
DE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000250|UniProtKB:P53043};
DE            Short=PPT {ECO:0000250|UniProtKB:P53043};
DE            EC=3.1.3.16 {ECO:0000305|PubMed:17475320};
DE   AltName: Full=AoPPT {ECO:0000303|PubMed:17475320};
GN   Name=ppt1 {ECO:0000305};
GN   ORFNames=AO090701000208 {ECO:0000312|EMBL:BAE61946.1};
OS   Aspergillus oryzae (strain ATCC 42149 / RIB 40) (Yellow koji mold).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=510516 {ECO:0000312|Proteomes:UP000006564};
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
DE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000250|UniProtKB:P53043};
DE            Short=PPT {ECO:0000250|UniProtKB:P53043};
DE            EC=3.1.3.16 {ECO:0000305|PubMed:17475320};
DE   AltName: Full=AoPPT {ECO:0000303|PubMed:17475320};
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 47-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:17475320};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000305|PubMed:17475320};
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 151. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
