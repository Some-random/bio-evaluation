# pathway_0035

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAEKQQAVTEFYNNTSPRGAWEFLLGDHLHEGFYDPGTTATISGSQAAAARMIDEALRFANIYDDPSKKPKNMLDIGCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK

[Multiple Choices]
A. L-threonine from L-aspartate: step 1/5. .
B. L-homoserine from L-aspartate: step 1/3. .
C. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
D. Alkaloid biosynthesis
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

> The sequence-matched UniProt entry annotates this protein to alkaloid biosynthesis, specifically ajmaline biosynthesis, with experimental-evidence citations. This supports choice D, while preserving the distinction that the pathway annotation is broader than the specific ajmaline pathway.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C1](#evidence-c1), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a glycine-rich segment, DIGCGVGGTC, consistent with the SAM-binding motif of a SAM-dependent methyltransferase. That enzyme class is biologically plausible in alkaloid biosynthesis and unlike the aspartate-pathway kinases or chorismate synthase represented by choices A–C.


**Missing item-specific fact**

> The sequence motif does not by itself establish this protein’s exact substrate or its specific role in alkaloid biosynthesis; those details require protein-specific functional knowledge.


**Reason**

> The motif and contrasting enzyme types provide a meaningful basis to favor D among these choices, although identifying the precise alkaloid pathway would depend on protein-specific annotation or experimental facts not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct pathway contexts, and the sequence offers a plausible methyltransferase-family clue favoring D over the enzyme types in A–C.


### Important caveats

- The reviewer-only evidence identifies a sequence-matched UniProt annotation and cites experimental evidence, but the primary studies were not independently reviewed here.
- The actual source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a glycine-rich segment, DIGCGVGGTC, consistent with the SAM-binding motif of a SAM-dependent methyltransferase. That enzyme class is biologically plausible in alkaloid biosynthesis and unlike the aspartate-pathway kinases or chorismate synthase represented by choices A–C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence motif does not by itself establish this protein’s exact substrate or its specific role in alkaloid biosynthesis; those details require protein-specific functional knowledge.",
    "reason": "The motif and contrasting enzyme types provide a meaningful basis to favor D among these choices, although identifying the precise alkaloid pathway would depend on protein-specific annotation or experimental facts not supplied in the question."
  },
  "case_id": "pathway_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C1",
      "H1"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein to alkaloid biosynthesis, specifically ajmaline biosynthesis, with experimental-evidence citations. This supports choice D, while preserving the distinction that the pathway annotation is broader than the specific ajmaline pathway."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched UniProt annotation and cites experimental evidence, but the primary studies were not independently reviewed here.",
    "The actual source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct pathway contexts, and the sequence offers a plausible methyltransferase-family clue favoring D over the enzyme types in A–C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein to alkaloid biosynthesis, specifically ajmaline biosynthesis, with experimental-evidence citations. This supports choice D, while preserving the distinction that the pathway annotation is broader than the specific ajmaline pathway.",
    "evidence_ids": ["C5", "H4", "C1", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a glycine-rich segment, DIGCGVGGTC, consistent with the SAM-binding motif of a SAM-dependent methyltransferase. That enzyme class is biologically plausible in alkaloid biosynthesis and unlike the aspartate-pathway kinases or chorismate synthase represented by choices A–C.",
    "missing_item_specific_fact": "The sequence motif does not by itself establish this protein’s exact substrate or its specific role in alkaloid biosynthesis; those details require protein-specific functional knowledge.",
    "reason": "The motif and contrasting enzyme types provide a meaningful basis to favor D among these choices, although identifying the precise alkaloid pathway would depend on protein-specific annotation or experimental facts not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct pathway contexts, and the sequence offers a plausible methyltransferase-family clue favoring D over the enzyme types in A–C."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched UniProt annotation and cites experimental evidence, but the primary studies were not independently reviewed here.",
    "The actual source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A075D6M1 (sequence SHA256 match confirmed in both current and historical snapshots) annotates this protein as Norajmaline N-methyltransferase (EC 2.1.1.392) from Rauvolfia serpentina. The PATHWAY comment explicitly states 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence codes (ECO:0000269) from two independent peer-reviewed publications (Cazares-Flores et al. 2016 Plant J.; Guo et al. 2024 Nat. Commun.). The expected answer D matches this annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs characteristic of methyltransferases (e.g., the GCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK region resembles the Rossmann-like methyltransferase fold). Options A, B, and C describe enzymatic steps that are NOT methyltransferase reactions: step 1/5 of threonine biosynthesis is aspartate kinase (phosphorylation), step 1/3 of homoserine biosynthesis is aspartate semialdehyde dehydrogenase (oxidation/reduction), and step 7/7 of chorismate biosynthesis is DAHP synthase (condensation). A methyltransferase cannot catalyze any of these three reactions. By process of elimination, only option D (Alkaloid biosynthesis), which involves N-methylation steps, is mechanistically compatible with a methyltransferase.


**Missing item-specific fact**

> None strictly required for elimination; however, confirming the specific alkaloid (ajmaline) and the protein's evolutionary derivation from gamma-tocopherol C-methyltransferase would require database lookup. The elimination logic among the four given options does not depend on this.


**Reason**

> A model with general knowledge of enzyme mechanisms can recognize methyltransferase motifs in the sequence and eliminate options A, B, C because those steps involve phosphorylation, oxidation, and condensation respectively—not methyl group transfer. This leaves D as the only mechanistically consistent choice. The reasoning is concrete and does not require memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are all primary amino acid/aromatic biosynthesis steps catalyzed by non-methyltransferase enzymes, making them mechanistically incompatible with the protein's methyltransferase identity. Option D (Alkaloid biosynthesis) is the only option in which N-methyltransferase reactions occur. No other option is defensible.


### Important caveats

- The methyltransferase motif recognition from sequence alone is a heuristic; the specific assignment to 'alkaloid biosynthesis' (rather than, e.g., tocopherol biosynthesis from which the enzyme family is derived) relies on the elimination logic among the four provided options rather than positive identification of an alkaloid-specific motif.
- The UniProt annotation was first published in 2025-06-18 (entry version 36 integrated 2026-01-28), but the underlying experimental evidence dates to 2016 and 2024 publications, so the functional assignment predates the Swiss-Prot entry.
- Option D is broad ('Alkaloid biosynthesis') while the specific sub-pathway is ajmaline biosynthesis; this generality is acceptable given the option set.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs characteristic of methyltransferases (e.g., the GCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK region resembles the Rossmann-like methyltransferase fold). Options A, B, and C describe enzymatic steps that are NOT methyltransferase reactions: step 1/5 of threonine biosynthesis is aspartate kinase (phosphorylation), step 1/3 of homoserine biosynthesis is aspartate semialdehyde dehydrogenase (oxidation/reduction), and step 7/7 of chorismate biosynthesis is DAHP synthase (condensation). A methyltransferase cannot catalyze any of these three reactions. By process of elimination, only option D (Alkaloid biosynthesis), which involves N-methylation steps, is mechanistically compatible with a methyltransferase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required for elimination; however, confirming the specific alkaloid (ajmaline) and the protein's evolutionary derivation from gamma-tocopherol C-methyltransferase would require database lookup. The elimination logic among the four given options does not depend on this.",
    "reason": "A model with general knowledge of enzyme mechanisms can recognize methyltransferase motifs in the sequence and eliminate options A, B, C because those steps involve phosphorylation, oxidation, and condensation respectively—not methyl group transfer. This leaves D as the only mechanistically consistent choice. The reasoning is concrete and does not require memorizing the specific UniProt entry."
  },
  "case_id": "pathway_0035",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A075D6M1 (sequence SHA256 match confirmed in both current and historical snapshots) annotates this protein as Norajmaline N-methyltransferase (EC 2.1.1.392) from Rauvolfia serpentina. The PATHWAY comment explicitly states 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence codes (ECO:0000269) from two independent peer-reviewed publications (Cazares-Flores et al. 2016 Plant J.; Guo et al. 2024 Nat. Commun.). The expected answer D matches this annotation."
  },
  "important_caveats": [
    "The methyltransferase motif recognition from sequence alone is a heuristic; the specific assignment to 'alkaloid biosynthesis' (rather than, e.g., tocopherol biosynthesis from which the enzyme family is derived) relies on the elimination logic among the four provided options rather than positive identification of an alkaloid-specific motif.",
    "The UniProt annotation was first published in 2025-06-18 (entry version 36 integrated 2026-01-28), but the underlying experimental evidence dates to 2016 and 2024 publications, so the functional assignment predates the Swiss-Prot entry.",
    "Option D is broad ('Alkaloid biosynthesis') while the specific sub-pathway is ajmaline biosynthesis; this generality is acceptable given the option set."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are all primary amino acid/aromatic biosynthesis steps catalyzed by non-methyltransferase enzymes, making them mechanistically incompatible with the protein's methyltransferase identity. Option D (Alkaloid biosynthesis) is the only option in which N-methyltransferase reactions occur. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0035",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A075D6M1 (sequence SHA256 match confirmed in both current and historical snapshots) annotates this protein as Norajmaline N-methyltransferase (EC 2.1.1.392) from Rauvolfia serpentina. The PATHWAY comment explicitly states 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence codes (ECO:0000269) from two independent peer-reviewed publications (Cazares-Flores et al. 2016 Plant J.; Guo et al. 2024 Nat. Commun.). The expected answer D matches this annotation.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs characteristic of methyltransferases (e.g., the GCGVGGTCVHVAKQYGIQCKGITLSPEEVKCAQGIAKAQGLEEKVSFDVGDALNLPYKDGTFDLVLTIECIEHVQDKEKFIREMIRVAAPGAPIVILSYAHRNLSPSAESLKPDEKKVLKKICDNLALSCLCSSADFVRWLTQLPAEDIKTADWTQNTSPFFPLLMKETFTWKGFTSLLMKGGWTAIKELLALRMMSKAADDGLLKFVAITCRKSK region resembles the Rossmann-like methyltransferase fold). Options A, B, and C describe enzymatic steps that are NOT methyltransferase reactions: step 1/5 of threonine biosynthesis is aspartate kinase (phosphorylation), step 1/3 of homoserine biosynthesis is aspartate semialdehyde dehydrogenase (oxidation/reduction), and step 7/7 of chorismate biosynthesis is DAHP synthase (condensation). A methyltransferase cannot catalyze any of these three reactions. By process of elimination, only option D (Alkaloid biosynthesis), which involves N-methylation steps, is mechanistically compatible with a methyltransferase.",
    "missing_item_specific_fact": "None strictly required for elimination; however, confirming the specific alkaloid (ajmaline) and the protein's evolutionary derivation from gamma-tocopherol C-methyltransferase would require database lookup. The elimination logic among the four given options does not depend on this.",
    "reason": "A model with general knowledge of enzyme mechanisms can recognize methyltransferase motifs in the sequence and eliminate options A, B, C because those steps involve phosphorylation, oxidation, and condensation respectively—not methyl group transfer. This leaves D as the only mechanistically consistent choice. The reasoning is concrete and does not require memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are all primary amino acid/aromatic biosynthesis steps catalyzed by non-methyltransferase enzymes, making them mechanistically incompatible with the protein's methyltransferase identity. Option D (Alkaloid biosynthesis) is the only option in which N-methyltransferase reactions occur. No other option is defensible."
  },
  "important_caveats": [
    "The methyltransferase motif recognition from sequence alone is a heuristic; the specific assignment to 'alkaloid biosynthesis' (rather than, e.g., tocopherol biosynthesis from which the enzyme family is derived) relies on the elimination logic among the four provided options rather than positive identification of an alkaloid-specific motif.",
    "The UniProt annotation was first published in 2025-06-18 (entry version 36 integrated 2026-01-28), but the underlying experimental evidence dates to 2016 and 2024 publications, so the functional assignment predates the Swiss-Prot entry.",
    "Option D is broad ('Alkaloid biosynthesis') while the specific sub-pathway is ajmaline biosynthesis; this generality is acceptable given the option set."
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

**Accession:** `A0A075D6M1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 36. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
"A0A075D6M1"
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AHH02781.1","source":"EMBL"}],"value":"Gamma-tocopherol-like methyltransferase NNMT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"2.1.1.392"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"Norajmaline N-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38212296","source":"PubMed"}],"value":"RsNNMT"}]}}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38212296","source":"PubMed"}],"value":"Alkaloid biosynthesis; ajmaline biosynthesis"}]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"citation":{"authors":["Cazares-Flores P.","Levac D.","De Luca V."],"citationCrossReferences":[{"database":"PubMed","id":"27122470"},{"database":"DOI","id":"10.1111/tpj.13186"}],"citationType":"journal article","firstPage":"335","id":"27122470","journal":"Plant J.","lastPage":"342","publicationDate":"2016","title":"Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta -methylajmaline biosynthesis belong to a gene family derived from gamma-tocopherol C-methyltransferase.","volume":"87"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D6M1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.783284+00:00.  

```json
{"citation":{"authors":["Guo J.","Gao D.","Lian J.","Qu Y."],"citationCrossReferences":[{"database":"PubMed","id":"38212296"},{"database":"DOI","id":"10.1038/s41467-024-44797-z"}],"citationType":"journal article","firstPage":"457","id":"38212296","journal":"Nat. Commun.","lastPage":"457","publicationDate":"2024","title":"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.","volume":"15"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","TISSUE SPECIFICITY","BIOTECHNOLOGY"]}
```

Source SHA-256: `3bb9ffb2ae03473556ed523492c0744d518e1d741d7bd4b3a3fc9dc695f623a9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
ID   NNMT_RAUSE              Reviewed;         292 AA.
AC   A0A075D6M1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   29-OCT-2014, sequence version 1.
DT   28-JAN-2026, entry version 36.
DE   RecName: Full=Norajmaline N-methyltransferase {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};
DE            Short=RsNNMT {ECO:0000303|PubMed:27122470, ECO:0000303|PubMed:38212296};
DE            EC=2.1.1.392 {ECO:0000269|PubMed:38212296};
DE   AltName: Full=Gamma-tocopherol-like methyltransferase NNMT {ECO:0000312|EMBL:AHH02781.1};
GN   Name=NNMT {ECO:0000303|PubMed:38212296};
GN   Synonyms=Rs9447 {ECO:0000312|EMBL:AHH02781.1};
OS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=4060;
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 27-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND
RP   TISSUE SPECIFICITY.
RX   PubMed=27122470; DOI=10.1111/tpj.13186;
RA   Cazares-Flores P., Levac D., De Luca V.;
RT   "Rauvolfia serpentina N-methyltransferases involved in ajmaline and Nbeta
RT   -methylajmaline biosynthesis belong to a gene family derived from gamma-
RT   tocopherol C-methyltransferase.";
RL   Plant J. 87:335-342(2016).
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 36-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
RN   [3]
RP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE SPECIFICITY, AND
RP   BIOTECHNOLOGY.
RX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;
RA   Guo J., Gao D., Lian J., Qu Y.;
RT   "De novo biosynthesis of antiarrhythmic alkaloid ajmaline.";
RL   Nat. Commun. 15:457-457(2024).
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D6M1?format=txt&versions=36)  
**Locator:** `lines 83-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-01T06:27:15.852655+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.
CC       {ECO:0000269|PubMed:27122470, ECO:0000269|PubMed:38212296}.
```

Source SHA-256: `ea487ae2513c784ecb9c3536d3436f3ff3869372e436c3eb33f2b9b462f39efa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 35. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
