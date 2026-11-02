# pathway_0109

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELITLLSALLVLAIVSLSTFFVLYYNTPTKDGKTLPPGRMGWPFIGESYDFFAAGWKGKPESFIFDRLKKFAKGNLNGQFRTSLFGNKSIVVAGAAANKLLFSNEKKLVTMWWPPSIDKAFPSTAQLSANEEALLMRKFFPSFLIRREALQRYIPIMDDCTRRHFATGAWGPSDKIEAFNVTQDYTFWVACRVFMSIDAQEDPETVDSLFRHFNVLKAGIYSMHIDLPWTNFHHAMKASHAIRSAVEQIAKKRRAELAEGKAFPTQDMLSYMLETPITSAEDSKDGKAKYLNDADIGTKILGLLVGGHDTSSTVIAFFFKFMAENPHVYEAIYKEQMEVAATKAPGELLNWDDLQKMKYSWCAICEVMRLTPPVQGAFRQAITDFTHNGYLIPKGWKIYWSTHSTHRNPEIFPQPEKFDPTRFEGNGPPAFSFVPFGGGPRMCPGKEYARLQVLTFVHHIVTKFKWEQILPNEKIIVSPMPYPEKNLPLRMIARSESATLA

[Multiple Choices]
A. L-valine from pyruvate: step 3/4. .
B. L-threonine from L-aspartate: step 2/5. .
C. Amino-acid degradation
D. Secondary metabolite biosynthesis
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

> The exact sequence matches the UniProt entry for CYP716A379, annotated as a beta-amyrin 28-monooxygenase in terpenoid and secondary-metabolite biosynthesis. The pathway annotation carries experimental-evidence coding, and the same annotation appears in the historical entry.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features can suggest a membrane-associated cytochrome P450 and make the amino-acid biosynthesis options unlikely, but they do not establish which pathway this particular P450 serves.


**Missing item-specific fact**

> The protein-specific identity and function of CYP716A379 as a beta-amyrin 28-monooxygenase involved in terpenoid saponin biosynthesis.


**Reason**

> Distinguishing secondary-metabolite biosynthesis from other possible functions requires a protein-specific annotation or experimental result absent from the input; recognizing general P450 features is insufficient.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein's annotated pathway supports D; the sequence alone does not resolve its specific pathway, but the reviewer evidence does.


### Important caveats

- The pathway annotation is supported by evidence linked to a publication, but the primary study was not independently reviewed here.
- The historical matched entry supports that the annotation was present by the historical cutoff; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features can suggest a membrane-associated cytochrome P450 and make the amino-acid biosynthesis options unlikely, but they do not establish which pathway this particular P450 serves.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and function of CYP716A379 as a beta-amyrin 28-monooxygenase involved in terpenoid saponin biosynthesis.",
    "reason": "Distinguishing secondary-metabolite biosynthesis from other possible functions requires a protein-specific annotation or experimental result absent from the input; recognizing general P450 features is insufficient."
  },
  "case_id": "pathway_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for CYP716A379, annotated as a beta-amyrin 28-monooxygenase in terpenoid and secondary-metabolite biosynthesis. The pathway annotation carries experimental-evidence coding, and the same annotation appears in the historical entry."
  },
  "important_caveats": [
    "The pathway annotation is supported by evidence linked to a publication, but the primary study was not independently reviewed here.",
    "The historical matched entry supports that the annotation was present by the historical cutoff; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's annotated pathway supports D; the sequence alone does not resolve its specific pathway, but the reviewer evidence does."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for CYP716A379, annotated as a beta-amyrin 28-monooxygenase in terpenoid and secondary-metabolite biosynthesis. The pathway annotation carries experimental-evidence coding, and the same annotation appears in the historical entry.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features can suggest a membrane-associated cytochrome P450 and make the amino-acid biosynthesis options unlikely, but they do not establish which pathway this particular P450 serves.",
    "missing_item_specific_fact": "The protein-specific identity and function of CYP716A379 as a beta-amyrin 28-monooxygenase involved in terpenoid saponin biosynthesis.",
    "reason": "Distinguishing secondary-metabolite biosynthesis from other possible functions requires a protein-specific annotation or experimental result absent from the input; recognizing general P450 features is insufficient."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's annotated pathway supports D; the sequence alone does not resolve its specific pathway, but the reviewer evidence does."
  },
  "important_caveats": [
    "The pathway annotation is supported by evidence linked to a publication, but the primary study was not independently reviewed here.",
    "The historical matched entry supports that the annotation was present by the historical cutoff; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1JA93 (CYP716A379, Beta-amyrin 28-monooxygenase from Saponaria officinalis) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with evidence code ECO:0000269 (inferred from direct assay, PubMed:39043959). The protein catalyzes beta-amyrin 28-monooxygenase activity (EC 1.14.14.126), a key step in saponin (triterpenoid) biosynthesis. Saponins are classic plant secondary metabolites. The sequence is confirmed as an exact match to the annotated entry.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif (visible as 'FGGGPRMCPGKEYARLQ' with the conserved Cys that coordinates heme iron). Plant cytochrome P450s are overwhelmingly associated with secondary metabolite biosynthesis (terpenoids, alkaloids, phenylpropanoids) rather than amino acid degradation. Options A and B describe specific amino acid biosynthesis steps (valine, threonine) that involve entirely different enzyme classes (dehydrogenases, transaminases), not P450s. Option C (amino-acid degradation) is not a typical P450 function. Recognizing the P450 fold and knowing that plant P450s predominantly catalyze oxidative tailoring of secondary metabolites (terpenoids, etc.) provides a defensible reasoning path to D.


**Missing item-specific fact**

> The specific identification as CYP716A379 involved in saponin biosynthesis requires either database lookup or knowledge of the CYP716 family's association with triterpenoid pathways. However, the broader reasoning (P450 → plant secondary metabolism) is sufficient to eliminate A, B, and C.


**Reason**

> The P450 heme-binding signature is identifiable from the raw sequence, and the general biological principle that plant P450s are primarily involved in secondary metabolite biosynthesis (not amino acid biosynthesis or degradation) allows meaningful elimination of distractors A, B, and C without requiring memorization of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are specific amino acid biosynthesis steps involving non-P450 enzymes and are clearly incompatible with a P450 sequence. Option C (amino-acid degradation) is not a recognized primary function of plant P450s. Option D is the only pathway category consistent with a plant cytochrome P450 involved in oxidative modification of a triterpenoid scaffold.


### Important caveats

- The UniProt entry was first publicly released in June 2025; depending on the benchmark construction date, this annotation may or may not have been available in databases at the time of question creation.
- The pathway annotation carries ECO:0000269 (inferred from direct assay), indicating experimental support from the 2025 Nature Chemical Biology paper on saponin biosynthesis in soapwort.
- The P450 identification from sequence relies on recognizing the heme-binding motif, which is a standard but not trivial sequence feature; some models may struggle with this from raw sequence alone.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning path relies on general P450 biology rather than this specific annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (visible as 'FGGGPRMCPGKEYARLQ' with the conserved Cys that coordinates heme iron). Plant cytochrome P450s are overwhelmingly associated with secondary metabolite biosynthesis (terpenoids, alkaloids, phenylpropanoids) rather than amino acid degradation. Options A and B describe specific amino acid biosynthesis steps (valine, threonine) that involve entirely different enzyme classes (dehydrogenases, transaminases), not P450s. Option C (amino-acid degradation) is not a typical P450 function. Recognizing the P450 fold and knowing that plant P450s predominantly catalyze oxidative tailoring of secondary metabolites (terpenoids, etc.) provides a defensible reasoning path to D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identification as CYP716A379 involved in saponin biosynthesis requires either database lookup or knowledge of the CYP716 family's association with triterpenoid pathways. However, the broader reasoning (P450 → plant secondary metabolism) is sufficient to eliminate A, B, and C.",
    "reason": "The P450 heme-binding signature is identifiable from the raw sequence, and the general biological principle that plant P450s are primarily involved in secondary metabolite biosynthesis (not amino acid biosynthesis or degradation) allows meaningful elimination of distractors A, B, and C without requiring memorization of this specific protein's annotation."
  },
  "case_id": "pathway_0109",
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
    "reason": "The UniProt entry A0AAW1JA93 (CYP716A379, Beta-amyrin 28-monooxygenase from Saponaria officinalis) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with evidence code ECO:0000269 (inferred from direct assay, PubMed:39043959). The protein catalyzes beta-amyrin 28-monooxygenase activity (EC 1.14.14.126), a key step in saponin (triterpenoid) biosynthesis. Saponins are classic plant secondary metabolites. The sequence is confirmed as an exact match to the annotated entry."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released in June 2025; depending on the benchmark construction date, this annotation may or may not have been available in databases at the time of question creation.",
    "The pathway annotation carries ECO:0000269 (inferred from direct assay), indicating experimental support from the 2025 Nature Chemical Biology paper on saponin biosynthesis in soapwort.",
    "The P450 identification from sequence relies on recognizing the heme-binding motif, which is a standard but not trivial sequence feature; some models may struggle with this from raw sequence alone.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning path relies on general P450 biology rather than this specific annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are specific amino acid biosynthesis steps involving non-P450 enzymes and are clearly incompatible with a P450 sequence. Option C (amino-acid degradation) is not a recognized primary function of plant P450s. Option D is the only pathway category consistent with a plant cytochrome P450 involved in oxidative modification of a triterpenoid scaffold."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0109",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1JA93 (CYP716A379, Beta-amyrin 28-monooxygenase from Saponaria officinalis) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with evidence code ECO:0000269 (inferred from direct assay, PubMed:39043959). The protein catalyzes beta-amyrin 28-monooxygenase activity (EC 1.14.14.126), a key step in saponin (triterpenoid) biosynthesis. Saponins are classic plant secondary metabolites. The sequence is confirmed as an exact match to the annotated entry.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (visible as 'FGGGPRMCPGKEYARLQ' with the conserved Cys that coordinates heme iron). Plant cytochrome P450s are overwhelmingly associated with secondary metabolite biosynthesis (terpenoids, alkaloids, phenylpropanoids) rather than amino acid degradation. Options A and B describe specific amino acid biosynthesis steps (valine, threonine) that involve entirely different enzyme classes (dehydrogenases, transaminases), not P450s. Option C (amino-acid degradation) is not a typical P450 function. Recognizing the P450 fold and knowing that plant P450s predominantly catalyze oxidative tailoring of secondary metabolites (terpenoids, etc.) provides a defensible reasoning path to D.",
    "missing_item_specific_fact": "The specific identification as CYP716A379 involved in saponin biosynthesis requires either database lookup or knowledge of the CYP716 family's association with triterpenoid pathways. However, the broader reasoning (P450 → plant secondary metabolism) is sufficient to eliminate A, B, and C.",
    "reason": "The P450 heme-binding signature is identifiable from the raw sequence, and the general biological principle that plant P450s are primarily involved in secondary metabolite biosynthesis (not amino acid biosynthesis or degradation) allows meaningful elimination of distractors A, B, and C without requiring memorization of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are specific amino acid biosynthesis steps involving non-P450 enzymes and are clearly incompatible with a P450 sequence. Option C (amino-acid degradation) is not a recognized primary function of plant P450s. Option D is the only pathway category consistent with a plant cytochrome P450 involved in oxidative modification of a triterpenoid scaffold."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released in June 2025; depending on the benchmark construction date, this annotation may or may not have been available in databases at the time of question creation.",
    "The pathway annotation carries ECO:0000269 (inferred from direct assay), indicating experimental support from the 2025 Nature Chemical Biology paper on saponin biosynthesis in soapwort.",
    "The P450 identification from sequence relies on recognizing the heme-binding motif, which is a standard but not trivial sequence feature; some models may struggle with this from raw sequence alone.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning path relies on general P450 biology rather than this specific annotation."
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

**Accession:** `A0AAW1JA93` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
"A0AAW1JA93"
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"commonName":"Common soapwort","lineage":["Eukaryota","Viridiplantae","Streptophyta","Embryophyta","Tracheophyta","Spermatophyta","Magnoliopsida","eudicotyledons","Gunneridae","Pentapetalae","Caryophyllales","Caryophyllaceae","Caryophylleae","Saponaria"],"scientificName":"Saponaria officinalis","synonyms":["Lychnis saponaria"],"taxonId":3572}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"Cytochrome P450 716A379"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoCYP716A379"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"1.14.14.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Oleanolic acid 16-monooxygenase CYP716A379"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"1.14.14.126"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Beta-amyrin 28-monooxygenase CYP716A379"}}}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48155.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:38.624320+00:00.  

```text
ID   C7169_SAPOF             Reviewed;         502 AA.
AC   A0AAW1JA93;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A379 {ECO:0000305};
DE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};
DE   AltName: Full=Cytochrome P450 716A379 {ECO:0000303|PubMed:39043959};
DE            Short=SoCYP716A379 {ECO:0000303|PubMed:39043959};
DE   AltName: Full=Oleanolic acid 16-monooxygenase CYP716A379 {ECO:0000305};
DE            EC=1.14.14.- {ECO:0000269|PubMed:39043959};
GN   Name=CYP716A379 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11043486m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_08G189800 {ECO:0000312|EMBL:KAK9699696.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)  
**Locator:** `lines 20-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:38.624320+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:WWM48155.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE
RP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.
RX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;
RA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,
RA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,
RA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,
RA   Leebens-Mack J., Osbourn A.;
RT   "Unlocking saponin biosynthesis in soapwort.";
RL   Nat. Chem. Biol. 21:215-226(2025).
```

Source SHA-256: `49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)  
**Locator:** `lines 69-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:38.624320+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
