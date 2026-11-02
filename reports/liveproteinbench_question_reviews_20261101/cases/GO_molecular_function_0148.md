# GO_molecular_function_0148

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — ABC-type transporter activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTAYALTDSWTMTRRELARWARQPVQLVVNLVFPVMLLLMFGYLIGGGRGVNGEYRDYLIPGMLALTMAFGLEGTMIAVTRDLDKGVIDRFRSMPMADGAVLVGRSAADMLQSAMALVVLIGVGAALGWRVHGGPVAFLGAVGLLLLFRFAMLWIGIYLALVAGKPEMVQAVQILVWPIGFLSNALALPDTMPGWLGTVVEWNPMSHTATAVRDLFGTPGAESGHVGAALVWPLALLAVFFPLAVRRFGRLSR

[Multiple Choices]
A. ABC-type transporter activity
B. tubulin deacetylase activity
C. structural constituent of vitelline membrane
D. RNA binding
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches UniProt P0DXU8, annotated as the DrrB3 ABC-transporter permease. UniProt describes it as part of the DrrA3B3 complex involved in daunorubicin efflux, with substrate translocation attributed to this protein as probable. The ABC-type transporter GO annotation is computational (IEA:InterPro); the functional annotation also cites a publication with experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic regions strongly suggest an integral membrane protein and make the soluble deacetylase and typical RNA-binding alternatives less plausible. However, that architecture alone does not identify it specifically as an ABC-transporter permease.


**Missing item-specific fact**

> The protein-specific identity and evidence that this membrane protein is DrrB3, a permease component of the daunorubicin-efflux ABC transporter complex.


**Reason**

> The sequence supports a membrane-protein inference, but does not by itself establish ABC-transporter function; choosing A specifically relies on the protein-specific annotation or equivalent external evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is supported by the matching protein-specific annotation and cited functional evidence; the other listed choices are not comparably supported.


### Important caveats

- The sequence match and UniProt identity are reviewer-only evidence, not information supplied to the evaluated model.
- The ABC-type transporter GO annotation is IEA:InterPro; the cited literature-backed annotation supports complex-level efflux, while translocation by DrrB3 itself is qualified as probable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic regions strongly suggest an integral membrane protein and make the soluble deacetylase and typical RNA-binding alternatives less plausible. However, that architecture alone does not identify it specifically as an ABC-transporter permease.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and evidence that this membrane protein is DrrB3, a permease component of the daunorubicin-efflux ABC transporter complex.",
    "reason": "The sequence supports a membrane-protein inference, but does not by itself establish ABC-transporter function; choosing A specifically relies on the protein-specific annotation or equivalent external evidence."
  },
  "case_id": "GO_molecular_function_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt P0DXU8, annotated as the DrrB3 ABC-transporter permease. UniProt describes it as part of the DrrA3B3 complex involved in daunorubicin efflux, with substrate translocation attributed to this protein as probable. The ABC-type transporter GO annotation is computational (IEA:InterPro); the functional annotation also cites a publication with experimental evidence."
  },
  "important_caveats": [
    "The sequence match and UniProt identity are reviewer-only evidence, not information supplied to the evaluated model.",
    "The ABC-type transporter GO annotation is IEA:InterPro; the cited literature-backed annotation supports complex-level efflux, while translocation by DrrB3 itself is qualified as probable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported by the matching protein-specific annotation and cited functional evidence; the other listed choices are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt P0DXU8, annotated as the DrrB3 ABC-transporter permease. UniProt describes it as part of the DrrA3B3 complex involved in daunorubicin efflux, with substrate translocation attributed to this protein as probable. The ABC-type transporter GO annotation is computational (IEA:InterPro); the functional annotation also cites a publication with experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic regions strongly suggest an integral membrane protein and make the soluble deacetylase and typical RNA-binding alternatives less plausible. However, that architecture alone does not identify it specifically as an ABC-transporter permease.",
    "missing_item_specific_fact": "The protein-specific identity and evidence that this membrane protein is DrrB3, a permease component of the daunorubicin-efflux ABC transporter complex.",
    "reason": "The sequence supports a membrane-protein inference, but does not by itself establish ABC-transporter function; choosing A specifically relies on the protein-specific annotation or equivalent external evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported by the matching protein-specific annotation and cited functional evidence; the other listed choices are not comparably supported."
  },
  "important_caveats": [
    "The sequence match and UniProt identity are reviewer-only evidence, not information supplied to the evaluated model.",
    "The ABC-type transporter GO annotation is IEA:InterPro; the cited literature-backed annotation supports complex-level efflux, while translocation by DrrB3 itself is qualified as probable."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXU8 (sequence matched exactly) annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB3' with GO:0140359 'ABC-type transporter activity' (IEA:InterPro). The FUNCTION comment (C5) cites experimental evidence (ECO:0000269, PubMed:39375957) confirming its role in the ABC transporter complex DrrA3B3 for daunorubicin efflux. The 253-aa polytopic membrane topology is consistent with an ABC permease component.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is unmistakably a polytopic membrane protein (≥10 hydrophobic segments spanning ~20 residues each) from a bacterium. Option C (structural constituent of vitelline membrane, GO:0008316) is a Drosophila egg-shell term incompatible with a bacterial membrane protein. Option B (tubulin deacetylase, GO:0042903) requires catalytic zinc/hydrolase machinery absent here. Option D (RNA binding, GO:0003723) is incompatible with a polytopic transmembrane topology lacking RRM, KH, or other RNA-binding motifs. Only option A (ABC-type transporter activity) describes a polytopic membrane transporter, and ABC permease subunits are characteristically 200-300 aa with 10-12 TM helices, matching the observed topology. General knowledge of protein classes suffices to eliminate B, C, and D.


**Missing item-specific fact**

> Precise ABC permease signature motifs (e.g., EAA/ER motifs, specific TM helix packing) would strengthen the positive identification of 'ABC-type' over other transporter families, but since ABC-type is the only transporter option among the four choices, elimination of the three non-transporter distractors is sufficient.


**Reason**

> The polytopic membrane topology and bacterial origin allow a knowledgeable model to eliminate the three non-transporter options through general biological reasoning, leaving ABC-type transporter activity as the only viable choice. The question does not require memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (tubulin deacetylase, vitelline membrane structural constituent, RNA binding) are all clearly incompatible with a 253-aa bacterial polytopic membrane protein. No ambiguity exists among the options.


### Important caveats

- The GO annotation GO:0140359 carries evidence code IEA:InterPro (computational inference), while the functional role in daunorubicin efflux is supported by experimental evidence (PubMed:39375957). The ABC-type classification itself rests on domain architecture recognition rather than direct biochemical reconstitution of ATP-driven transport.
- The UniProt entry was first released 2025-02-05; the benchmark's exact construction date is unknown, though the sequence matches across checked versions.
- The reviewer-only accession was inferred from dataset image-path metadata and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is unmistakably a polytopic membrane protein (≥10 hydrophobic segments spanning ~20 residues each) from a bacterium. Option C (structural constituent of vitelline membrane, GO:0008316) is a Drosophila egg-shell term incompatible with a bacterial membrane protein. Option B (tubulin deacetylase, GO:0042903) requires catalytic zinc/hydrolase machinery absent here. Option D (RNA binding, GO:0003723) is incompatible with a polytopic transmembrane topology lacking RRM, KH, or other RNA-binding motifs. Only option A (ABC-type transporter activity) describes a polytopic membrane transporter, and ABC permease subunits are characteristically 200-300 aa with 10-12 TM helices, matching the observed topology. General knowledge of protein classes suffices to eliminate B, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise ABC permease signature motifs (e.g., EAA/ER motifs, specific TM helix packing) would strengthen the positive identification of 'ABC-type' over other transporter families, but since ABC-type is the only transporter option among the four choices, elimination of the three non-transporter distractors is sufficient.",
    "reason": "The polytopic membrane topology and bacterial origin allow a knowledgeable model to eliminate the three non-transporter options through general biological reasoning, leaving ABC-type transporter activity as the only viable choice. The question does not require memorizing this specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXU8 (sequence matched exactly) annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB3' with GO:0140359 'ABC-type transporter activity' (IEA:InterPro). The FUNCTION comment (C5) cites experimental evidence (ECO:0000269, PubMed:39375957) confirming its role in the ABC transporter complex DrrA3B3 for daunorubicin efflux. The 253-aa polytopic membrane topology is consistent with an ABC permease component."
  },
  "important_caveats": [
    "The GO annotation GO:0140359 carries evidence code IEA:InterPro (computational inference), while the functional role in daunorubicin efflux is supported by experimental evidence (PubMed:39375957). The ABC-type classification itself rests on domain architecture recognition rather than direct biochemical reconstitution of ATP-driven transport.",
    "The UniProt entry was first released 2025-02-05; the benchmark's exact construction date is unknown, though the sequence matches across checked versions.",
    "The reviewer-only accession was inferred from dataset image-path metadata and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (tubulin deacetylase, vitelline membrane structural constituent, RNA binding) are all clearly incompatible with a 253-aa bacterial polytopic membrane protein. No ambiguity exists among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXU8 (sequence matched exactly) annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB3' with GO:0140359 'ABC-type transporter activity' (IEA:InterPro). The FUNCTION comment (C5) cites experimental evidence (ECO:0000269, PubMed:39375957) confirming its role in the ABC transporter complex DrrA3B3 for daunorubicin efflux. The 253-aa polytopic membrane topology is consistent with an ABC permease component.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is unmistakably a polytopic membrane protein (≥10 hydrophobic segments spanning ~20 residues each) from a bacterium. Option C (structural constituent of vitelline membrane, GO:0008316) is a Drosophila egg-shell term incompatible with a bacterial membrane protein. Option B (tubulin deacetylase, GO:0042903) requires catalytic zinc/hydrolase machinery absent here. Option D (RNA binding, GO:0003723) is incompatible with a polytopic transmembrane topology lacking RRM, KH, or other RNA-binding motifs. Only option A (ABC-type transporter activity) describes a polytopic membrane transporter, and ABC permease subunits are characteristically 200-300 aa with 10-12 TM helices, matching the observed topology. General knowledge of protein classes suffices to eliminate B, C, and D.",
    "missing_item_specific_fact": "Precise ABC permease signature motifs (e.g., EAA/ER motifs, specific TM helix packing) would strengthen the positive identification of 'ABC-type' over other transporter families, but since ABC-type is the only transporter option among the four choices, elimination of the three non-transporter distractors is sufficient.",
    "reason": "The polytopic membrane topology and bacterial origin allow a knowledgeable model to eliminate the three non-transporter options through general biological reasoning, leaving ABC-type transporter activity as the only viable choice. The question does not require memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (tubulin deacetylase, vitelline membrane structural constituent, RNA binding) are all clearly incompatible with a 253-aa bacterial polytopic membrane protein. No ambiguity exists among the options."
  },
  "important_caveats": [
    "The GO annotation GO:0140359 carries evidence code IEA:InterPro (computational inference), while the functional role in daunorubicin efflux is supported by experimental evidence (PubMed:39375957). The ABC-type classification itself rests on domain architecture recognition rather than direct biochemical reconstitution of ATP-driven transport.",
    "The UniProt entry was first released 2025-02-05; the benchmark's exact construction date is unknown, though the sequence matches across checked versions.",
    "The reviewer-only accession was inferred from dataset image-path metadata and was not available to the evaluated model."
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

**Accession:** `P0DXU8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Daunorubicin resistance ABC transporter permease protein DrrB3"}}}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39375957","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Part of the ABC transporter complex DrrA3B3 involved in daunorubicin efflux (PubMed:39375957). Responsible for the translocation of the substrate across the membrane (Probable). Confers self-resistance to daunorubicin, an antibiotic produced by S.coeruleorubidus (PubMed:39375957). The efficiency of DrrA3B3 to export daunorubicin is probably lower than that of DrrA1B1 or DrrA2B2 (PubMed:39375957)"}]}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"database":"GO","id":"GO:0140359","properties":[{"key":"GoTerm","value":"F:ABC-type transporter activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.602104+00:00.  

```json
{"citation":{"authors":["Dong J.","Ning J.","Tian Y.","Li H.","Chen H.","Guan W."],"citationCrossReferences":[{"database":"PubMed","id":"39375957"},{"database":"DOI","id":"10.1111/1751-7915.70023"}],"citationType":"journal article","firstPage":"e70023","id":"39375957","journal":"Microb. Biotechnol.","lastPage":"e70023","publicationDate":"2024","title":"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.","volume":"17"},"referenceNumber":2,"referencePositions":["FUNCTION IN DAUNORUBICIN EFFLUX","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-01T06:28:21.104799+00:00.  

```text
ID   DRRB3_STRC4             Reviewed;         253 AA.
AC   P0DXU8;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB3 {ECO:0000305};
GN   Name=drrB3 {ECO:0000303|PubMed:39375957};
GN   ORFNames=R5U08_20730 {ECO:0000312|EMBL:WOT36400.1};
OS   Streptomyces coeruleorubidus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=116188;
```

Source SHA-256: `eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)  
**Locator:** `lines 25-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-01T06:28:21.104799+00:00.  

```text
CC   -!- FUNCTION: Part of the ABC transporter complex DrrA3B3 involved in
CC       daunorubicin efflux (PubMed:39375957). Responsible for the
CC       translocation of the substrate across the membrane (Probable). Confers
CC       self-resistance to daunorubicin, an antibiotic produced by
CC       S.coeruleorubidus (PubMed:39375957). The efficiency of DrrA3B3 to
CC       export daunorubicin is probably lower than that of DrrA1B1 or DrrA2B2
CC       (PubMed:39375957). {ECO:0000269|PubMed:39375957, ECO:0000305}.
```

Source SHA-256: `eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)  
**Locator:** `lines 56-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-01T06:28:21.104799+00:00.  

```text
DR   GO; GO:0140359; F:ABC-type transporter activity; IEA:InterPro.
```

Source SHA-256: `eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 439730-439752`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0140359
name: ABC-type transporter activity
namespace: molecular_function
def: "Primary active transporter characterized by two nucleotide-binding domains and two transmembrane domains. Uses the energy generated from ATP hydrolysis to drive the transport of a substance across a membrane." [PMID:26517899]
synonym: "ABC transporter" EXACT []
synonym: "ABC-type efflux permease activity" EXACT []
synonym: "ABC-type efflux porter activity" EXACT []
synonym: "ABC-type transmembrane transporter activity" EXACT []
synonym: "ABC-type uptake permease activity" EXACT []
synonym: "ATP binding cassette transporter" EXACT []
synonym: "ATP-binding cassette (ABC) transporter activity" EXACT []
synonym: "ATP-binding cassette transporter" EXACT []
xref: Reactome:R-HSA-266070 "LTC4 is exported from the cytosol by ABCC1"
xref: Reactome:R-HSA-429157 "ABCC4 accumulation of dense granule contents"
xref: Reactome:R-HSA-5362459 "VCP-catalyzed ATP hydrolysis promotes the translocation of Hh-C into the cytosol"
xref: Reactome:R-HSA-5387389 "Hh processing variants are translocated to the cytosol in a VCP-dependent manner"
xref: Reactome:R-HSA-9661405 "ABCC1 transports BIL from cytosol to extracellular region (blood)"
xref: Reactome:R-HSA-9750656 "ABCC2, ABCC3 transport salicylate metabolites from cytosol to extracellular region of hepatic cells"
xref: TC:3.A.1
xref: Wikipedia:ATP-binding_cassette_transporter
is_a: GO:0042626 ! ATPase-coupled transmembrane transporter activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 148. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
