# pathway_0177

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSQPEFTRSIVGASFLLPVINGAMHIPPAVSATRVTLEDNQPRDAPILVLLFALSVLIDVMDKAADLPRQTRKTWLMTIVVFASPFVVLAVYGTMHCGLLALLRLLGVPLLAVVHAMPLIPVYSWKTGSISTVKLKYFLGPFKSLFGATCIGLMDVTAVVLYLRGTMLHPENASSAGHFRVLMYTITYDFLWESICDVRDIQEDEQNNITTLATAFGVRPTLIFLGGSTMMGDLSITLLGGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART

[Multiple Choices]
A. Metabolic intermediate biosynthesis
B. Secondary metabolite biosynthesis
C. peptidoglycan degradation. .
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

> The exact-matching UniProt record annotates this protein to secondary metabolite biosynthesis, specifically terpenoid biosynthesis, and identifies it as prenyltransferase vviA. The pathway annotation is attributed to a publication with experimental evidence code ECO:0000269; the primary paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and appears to contain multiple membrane-spanning regions, but that does not identify its specific substrate, enzymatic function, or pathway among the choices.


**Missing item-specific fact**

> The protein-specific identification as prenyltransferase vviA and its role in terpenoid/secondary-metabolite biosynthesis.


**Reason**

> The supplied sequence and choices do not provide a defensible way to distinguish the specific secondary-metabolite pathway from broader metabolic biosynthesis. The answer depends on protein-specific functional annotation or equivalent external evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The choices provide no sequence-based discriminator between broad metabolic intermediate biosynthesis and the more specific secondary-metabolite biosynthesis. These descriptions can also overlap; the protein-specific annotation resolves the intended choice as B.


### Important caveats

- The reviewer-only record matches the supplied sequence, including the historical record available by the stated cutoff.
- The cited database annotation attributes experimental evidence to a publication, but that primary publication was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and appears to contain multiple membrane-spanning regions, but that does not identify its specific substrate, enzymatic function, or pathway among the choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as prenyltransferase vviA and its role in terpenoid/secondary-metabolite biosynthesis.",
    "reason": "The supplied sequence and choices do not provide a defensible way to distinguish the specific secondary-metabolite pathway from broader metabolic biosynthesis. The answer depends on protein-specific functional annotation or equivalent external evidence."
  },
  "case_id": "pathway_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates this protein to secondary metabolite biosynthesis, specifically terpenoid biosynthesis, and identifies it as prenyltransferase vviA. The pathway annotation is attributed to a publication with experimental evidence code ECO:0000269; the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence, including the historical record available by the stated cutoff.",
    "The cited database annotation attributes experimental evidence to a publication, but that primary publication was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The choices provide no sequence-based discriminator between broad metabolic intermediate biosynthesis and the more specific secondary-metabolite biosynthesis. These descriptions can also overlap; the protein-specific annotation resolves the intended choice as B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching UniProt record annotates this protein to secondary metabolite biosynthesis, specifically terpenoid biosynthesis, and identifies it as prenyltransferase vviA. The pathway annotation is attributed to a publication with experimental evidence code ECO:0000269; the primary paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and appears to contain multiple membrane-spanning regions, but that does not identify its specific substrate, enzymatic function, or pathway among the choices.",
    "missing_item_specific_fact": "The protein-specific identification as prenyltransferase vviA and its role in terpenoid/secondary-metabolite biosynthesis.",
    "reason": "The supplied sequence and choices do not provide a defensible way to distinguish the specific secondary-metabolite pathway from broader metabolic biosynthesis. The answer depends on protein-specific functional annotation or equivalent external evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The choices provide no sequence-based discriminator between broad metabolic intermediate biosynthesis and the more specific secondary-metabolite biosynthesis. These descriptions can also overlap; the protein-specific annotation resolves the intended choice as B."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence, including the historical record available by the stated cutoff.",
    "The cited database annotation attributes experimental evidence to a publication, but that primary publication was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A6A6H402 (Prenyltransferase vviA / Sporulositol A biosynthesis cluster protein A) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39310987, a 2024 Org. Lett. paper on cyclo-farnesyl diphosphate-dependent prenylation in fungi). The sequence matches exactly (293 AA, SHA-256 confirmed). The protein catalyzes prenylation in sporulositol A biosynthesis, a fungal secondary metabolite. The expected answer B is directly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could argue that fungal membrane-bound prenyltransferases with multiple TM domains are predominantly involved in secondary metabolite (terpenoid) biosynthesis rather than primary metabolic intermediate production. Options C (peptidoglycan degradation) and D (histidine biosynthesis) are readily excluded for a eukaryotic membrane protein. However, the critical A-vs-B distinction ('metabolic intermediate biosynthesis' vs. 'secondary metabolite biosynthesis') hinges on whether the prenylated product is a primary or secondary metabolite, which is not determinable from sequence features alone.


**Missing item-specific fact**

> The specific substrate and product identity of this enzyme (cyclo-farnesyl diphosphate-dependent prenylation producing sporulositol A, a secondary metabolite) is required to definitively assign the pathway as 'secondary metabolite biosynthesis' rather than the more generic 'metabolic intermediate biosynthesis.' Prenyltransferases can function in both primary (e.g., ubiquinone biosynthesis) and secondary metabolism, and the sequence alone does not encode which class of product is formed.


**Reason**

> While a knowledgeable model might narrow choices by recognizing prenyltransferase motifs and fungal membrane-protein architecture, the decisive distinction between option A (metabolic intermediate biosynthesis) and option B (secondary metabolite biosynthesis) depends on knowing this particular enzyme's role in sporulositol A biosynthesis—a specific experimental finding from PubMed:39310987. No general sequence heuristic reliably separates primary from secondary metabolite prenylation in fungi.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Prenyltransferases produce intermediates in isoprenoid pathways, which could be described as 'metabolic intermediate biosynthesis' (option A) in a broad sense. The classification as 'secondary metabolite biosynthesis' (option B) reflects the specific downstream product (sporulositol A) rather than a property uniquely readable from the enzyme's sequence. Without the specific substrate/product annotation, both A and B have some plausibility, though B is the more precise UniProt-assigned pathway.


### Important caveats

- The organism (Viridothelium virens, a lichen-forming fungus) is not stated in the question; the model must infer eukaryotic/fungal origin from sequence features alone.
- The pathway annotation is based on a single 2024 experimental study (PubMed:39310987); the EC number remains 2.5.1.- (unassigned subclass), indicating incomplete mechanistic characterization.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must work from sequence and general knowledge only.
- Option C (peptidoglycan degradation) is trivially wrong for a fungal protein, and option D (histidine biosynthesis) is inconsistent with the membrane-protein architecture, but these easy eliminations do not resolve the A-vs-B ambiguity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could argue that fungal membrane-bound prenyltransferases with multiple TM domains are predominantly involved in secondary metabolite (terpenoid) biosynthesis rather than primary metabolic intermediate production. Options C (peptidoglycan degradation) and D (histidine biosynthesis) are readily excluded for a eukaryotic membrane protein. However, the critical A-vs-B distinction ('metabolic intermediate biosynthesis' vs. 'secondary metabolite biosynthesis') hinges on whether the prenylated product is a primary or secondary metabolite, which is not determinable from sequence features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate and product identity of this enzyme (cyclo-farnesyl diphosphate-dependent prenylation producing sporulositol A, a secondary metabolite) is required to definitively assign the pathway as 'secondary metabolite biosynthesis' rather than the more generic 'metabolic intermediate biosynthesis.' Prenyltransferases can function in both primary (e.g., ubiquinone biosynthesis) and secondary metabolism, and the sequence alone does not encode which class of product is formed.",
    "reason": "While a knowledgeable model might narrow choices by recognizing prenyltransferase motifs and fungal membrane-protein architecture, the decisive distinction between option A (metabolic intermediate biosynthesis) and option B (secondary metabolite biosynthesis) depends on knowing this particular enzyme's role in sporulositol A biosynthesis—a specific experimental finding from PubMed:39310987. No general sequence heuristic reliably separates primary from secondary metabolite prenylation in fungi."
  },
  "case_id": "pathway_0177",
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
    "reason": "UniProt entry A0A6A6H402 (Prenyltransferase vviA / Sporulositol A biosynthesis cluster protein A) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39310987, a 2024 Org. Lett. paper on cyclo-farnesyl diphosphate-dependent prenylation in fungi). The sequence matches exactly (293 AA, SHA-256 confirmed). The protein catalyzes prenylation in sporulositol A biosynthesis, a fungal secondary metabolite. The expected answer B is directly supported."
  },
  "important_caveats": [
    "The organism (Viridothelium virens, a lichen-forming fungus) is not stated in the question; the model must infer eukaryotic/fungal origin from sequence features alone.",
    "The pathway annotation is based on a single 2024 experimental study (PubMed:39310987); the EC number remains 2.5.1.- (unassigned subclass), indicating incomplete mechanistic characterization.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must work from sequence and general knowledge only.",
    "Option C (peptidoglycan degradation) is trivially wrong for a fungal protein, and option D (histidine biosynthesis) is inconsistent with the membrane-protein architecture, but these easy eliminations do not resolve the A-vs-B ambiguity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Prenyltransferases produce intermediates in isoprenoid pathways, which could be described as 'metabolic intermediate biosynthesis' (option A) in a broad sense. The classification as 'secondary metabolite biosynthesis' (option B) reflects the specific downstream product (sporulositol A) rather than a property uniquely readable from the enzyme's sequence. Without the specific substrate/product annotation, both A and B have some plausibility, though B is the more precise UniProt-assigned pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A6A6H402 (Prenyltransferase vviA / Sporulositol A biosynthesis cluster protein A) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39310987, a 2024 Org. Lett. paper on cyclo-farnesyl diphosphate-dependent prenylation in fungi). The sequence matches exactly (293 AA, SHA-256 confirmed). The protein catalyzes prenylation in sporulositol A biosynthesis, a fungal secondary metabolite. The expected answer B is directly supported.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could argue that fungal membrane-bound prenyltransferases with multiple TM domains are predominantly involved in secondary metabolite (terpenoid) biosynthesis rather than primary metabolic intermediate production. Options C (peptidoglycan degradation) and D (histidine biosynthesis) are readily excluded for a eukaryotic membrane protein. However, the critical A-vs-B distinction ('metabolic intermediate biosynthesis' vs. 'secondary metabolite biosynthesis') hinges on whether the prenylated product is a primary or secondary metabolite, which is not determinable from sequence features alone.",
    "missing_item_specific_fact": "The specific substrate and product identity of this enzyme (cyclo-farnesyl diphosphate-dependent prenylation producing sporulositol A, a secondary metabolite) is required to definitively assign the pathway as 'secondary metabolite biosynthesis' rather than the more generic 'metabolic intermediate biosynthesis.' Prenyltransferases can function in both primary (e.g., ubiquinone biosynthesis) and secondary metabolism, and the sequence alone does not encode which class of product is formed.",
    "reason": "While a knowledgeable model might narrow choices by recognizing prenyltransferase motifs and fungal membrane-protein architecture, the decisive distinction between option A (metabolic intermediate biosynthesis) and option B (secondary metabolite biosynthesis) depends on knowing this particular enzyme's role in sporulositol A biosynthesis—a specific experimental finding from PubMed:39310987. No general sequence heuristic reliably separates primary from secondary metabolite prenylation in fungi."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Prenyltransferases produce intermediates in isoprenoid pathways, which could be described as 'metabolic intermediate biosynthesis' (option A) in a broad sense. The classification as 'secondary metabolite biosynthesis' (option B) reflects the specific downstream product (sporulositol A) rather than a property uniquely readable from the enzyme's sequence. Without the specific substrate/product annotation, both A and B have some plausibility, though B is the more precise UniProt-assigned pathway."
  },
  "important_caveats": [
    "The organism (Viridothelium virens, a lichen-forming fungus) is not stated in the question; the model must infer eukaryotic/fungal origin from sequence features alone.",
    "The pathway annotation is based on a single 2024 experimental study (PubMed:39310987); the EC number remains 2.5.1.- (unassigned subclass), indicating incomplete mechanistic characterization.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must work from sequence and general knowledge only.",
    "Option C (peptidoglycan degradation) is trivially wrong for a fungal protein, and option D (histidine biosynthesis) is inconsistent with the membrane-protein architecture, but these easy eliminations do not resolve the A-vs-B ambiguity."
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

**Accession:** `A0A6A6H402` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39310987","source":"PubMed"}],"value":"Sporulositol A biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39310987","source":"PubMed"}],"value":"2.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39310987","source":"PubMed"}],"value":"Prenyltransferase vviA"}}}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39310987","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.724960+00:00.  

```json
{"citation":{"authors":["Tang Y.J.","Zou Y."],"citationCrossReferences":[{"database":"PubMed","id":"39310987"},{"database":"DOI","id":"10.1021/acs.orglett.4c03154"}],"citationType":"journal article","firstPage":"8366","id":"39310987","journal":"Org. Lett.","lastPage":"8370","publicationDate":"2024","title":"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.","volume":"26"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","PATHWAY","MUTAGENESIS OF LEU-17; ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND THR-277"]}
```

Source SHA-256: `b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
ID   VVIA_VIRVR              Reviewed;         293 AA.
AC   A0A6A6H402;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   17-JUN-2020, sequence version 1.
DT   28-JAN-2026, entry version 12.
DE   RecName: Full=Prenyltransferase vviA {ECO:0000303|PubMed:39310987};
DE            EC=2.5.1.- {ECO:0000269|PubMed:39310987};
DE   AltName: Full=Sporulositol A biosynthesis cluster protein A {ECO:0000303|PubMed:39310987};
GN   Name=vviA {ECO:0000303|PubMed:39310987}; ORFNames=EV356DRAFT_253807;
OS   Viridothelium virens (Speckled blister lichen) (Trypethelium virens).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetes incertae sedis; Trypetheliales; Trypetheliaceae;
OC   Viridothelium.
OX   NCBI_TaxID=1048519;
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 29-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, PATHWAY, AND MUTAGENESIS OF LEU-17;
RP   ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND
RP   THR-277.
RX   PubMed=39310987; DOI=10.1021/acs.orglett.4c03154;
RA   Tang Y.J., Zou Y.;
RT   "Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.";
RL   Org. Lett. 26:8366-8370(2024).
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)  
**Locator:** `lines 58-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-02T04:25:34.642719+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39310987}.
```

Source SHA-256: `f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 177. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
