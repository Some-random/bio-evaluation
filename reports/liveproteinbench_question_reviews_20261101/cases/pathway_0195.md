# pathway_0195

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
METVQSSSSAELLRAQTHFSTQLFSFQNYASLKCALHLGIPDAIKQHGKPMNLSELTSALPIKPSKAPYIHRLMRMLVKAGYFAQENECFDLTPIGLLLLKDDPINIRALVLLELHPALLLPWIALSEWFQNDDATPFVTAHGKSFWDYTSRDPEFRKLFDEAMAGDSELISKVLVTEFKYVFEGLKSLVDVGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEGVVELEKNAGNEYAGLENLDMEMLVLYNSKERTKKEWAKLFSDAGFSDYKFIPALDSWCIIELTP

[Multiple Choices]
A. Cell wall biogenesis
B. Lipid metabolism. .
C. Alkaloid biosynthesis. .
D. L-leucine degradation
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

> The supplied sequence exactly matches the UniProt sequence for CiOMT, annotated as cephaeline/emetine O-methyltransferase in alkaloid biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269), though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may be compatible with an enzyme such as an O-methyltransferase, but that general inference does not establish which pathway it serves. The alkaloid-pathway assignment depends on identifying this specific enzyme and its substrates.


**Missing item-specific fact**

> The protein's identity as CiOMT and its experimentally annotated role in cephaeline/emetine biosynthesis are not supplied in the question.


**Reason**

> The sequence and choices alone do not meaningfully distinguish alkaloid biosynthesis from other possible pathways for a methyltransferase; an item-specific functional annotation or equivalent knowledge is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the sequence-matched functional annotation, alkaloid biosynthesis is the supported pathway choice; the other options are not supported for this protein.


### Important caveats

- Reviewer-only database evidence was not available to the evaluated model.
- The exact author source snapshot is unknown, although a historical UniProt record with a matching sequence also carries the alkaloid-biosynthesis annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may be compatible with an enzyme such as an O-methyltransferase, but that general inference does not establish which pathway it serves. The alkaloid-pathway assignment depends on identifying this specific enzyme and its substrates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as CiOMT and its experimentally annotated role in cephaeline/emetine biosynthesis are not supplied in the question.",
    "reason": "The sequence and choices alone do not meaningfully distinguish alkaloid biosynthesis from other possible pathways for a methyltransferase; an item-specific functional annotation or equivalent knowledge is needed."
  },
  "case_id": "pathway_0195",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for CiOMT, annotated as cephaeline/emetine O-methyltransferase in alkaloid biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269), though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The exact author source snapshot is unknown, although a historical UniProt record with a matching sequence also carries the alkaloid-biosynthesis annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the sequence-matched functional annotation, alkaloid biosynthesis is the supported pathway choice; the other options are not supported for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0195",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence for CiOMT, annotated as cephaeline/emetine O-methyltransferase in alkaloid biosynthesis. The pathway annotation cites experimental evidence (ECO:0000269), though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may be compatible with an enzyme such as an O-methyltransferase, but that general inference does not establish which pathway it serves. The alkaloid-pathway assignment depends on identifying this specific enzyme and its substrates.",
    "missing_item_specific_fact": "The protein's identity as CiOMT and its experimentally annotated role in cephaeline/emetine biosynthesis are not supplied in the question.",
    "reason": "The sequence and choices alone do not meaningfully distinguish alkaloid biosynthesis from other possible pathways for a methyltransferase; an item-specific functional annotation or equivalent knowledge is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the sequence-matched functional annotation, alkaloid biosynthesis is the supported pathway choice; the other options are not supported for this protein."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The exact author source snapshot is unknown, although a historical UniProt record with a matching sequence also carries the alkaloid-biosynthesis annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E7FL15 (CIOMT_CARIP) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 (PubMed:21228475). The protein is a Cephaeline 6'-O-methyltransferase (EC 2.1.1.396) involved in emetine/cephaeline biosynthesis in Carapichea ipecacuanha. The sequence matches exactly (350 AA, SHA256 confirmed). The annotation is experimentally supported, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'GGGNG' motif (residues ~168-172: 'VGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEG') characteristic of SAM-dependent O-methyltransferases. In plants, O-methyltransferases with this domain architecture are overwhelmingly associated with secondary metabolism, particularly alkaloid biosynthesis (e.g., berberine, morphine, emetine pathways), rather than cell wall biogenesis, lipid metabolism, or amino acid degradation. A biologist recognizing the plant OMT fold can reasonably infer alkaloid biosynthesis as the most probable pathway among the four choices.


**Missing item-specific fact**

> The specific substrate (cephaeline/7'-O-demethylcephaeline) and organism (Carapichea ipecacuanha, ipecac) are not provided in the input. However, the general biological argument that plant SAM-dependent OMTs predominantly function in alkaloid/secondary metabolite biosynthesis is sufficient to distinguish C from the other three options without memorizing this protein's annotation.


**Reason**

> The GGGNG SAM-binding motif identifies the protein as a methyltransferase. Among the four pathway options, alkaloid biosynthesis is the most biologically coherent assignment for a plant O-methyltransferase. Cell wall biogenesis (A) and L-leucine degradation (D) are implausible for an OMT. Lipid metabolism (B) is possible but far less common for plant OMTs with this domain architecture. The reasoning chain (plant OMT → secondary metabolism → alkaloid biosynthesis) is a defensible general biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (cell wall biogenesis) and D (L-leucine degradation) are clearly implausible for an O-methyltransferase. Option B (lipid metabolism) is a weak distractor since some methyltransferases participate in lipid modification, but plant OMTs with the GGGNG/SAM-binding fold are predominantly in alkaloid and phenylpropanoid pathways. Option C is the most defensible choice.


### Important caveats

- The reviewer-only UniProt annotation confirms the answer experimentally (ECO:0000269), but this information was not available to the evaluated model.
- The reasoning argument (plant OMT → alkaloid biosynthesis) is a general statistical tendency in plant secondary metabolism, not a deterministic rule. A small number of plant OMTs participate in other pathways.
- The specific identification as an emetine/cephaeline biosynthesis enzyme requires knowledge of the organism or substrate, but the question asks for the pathway category, which is reasonably inferable from the enzyme class and kingdom.
- The identity of the protein (E7FL15) was inferred mechanically from dataset metadata and was not provided to the model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'GGGNG' motif (residues ~168-172: 'VGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEG') characteristic of SAM-dependent O-methyltransferases. In plants, O-methyltransferases with this domain architecture are overwhelmingly associated with secondary metabolism, particularly alkaloid biosynthesis (e.g., berberine, morphine, emetine pathways), rather than cell wall biogenesis, lipid metabolism, or amino acid degradation. A biologist recognizing the plant OMT fold can reasonably infer alkaloid biosynthesis as the most probable pathway among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate (cephaeline/7'-O-demethylcephaeline) and organism (Carapichea ipecacuanha, ipecac) are not provided in the input. However, the general biological argument that plant SAM-dependent OMTs predominantly function in alkaloid/secondary metabolite biosynthesis is sufficient to distinguish C from the other three options without memorizing this protein's annotation.",
    "reason": "The GGGNG SAM-binding motif identifies the protein as a methyltransferase. Among the four pathway options, alkaloid biosynthesis is the most biologically coherent assignment for a plant O-methyltransferase. Cell wall biogenesis (A) and L-leucine degradation (D) are implausible for an OMT. Lipid metabolism (B) is possible but far less common for plant OMTs with this domain architecture. The reasoning chain (plant OMT → secondary metabolism → alkaloid biosynthesis) is a defensible general biological argument."
  },
  "case_id": "pathway_0195",
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
    "reason": "UniProt entry E7FL15 (CIOMT_CARIP) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 (PubMed:21228475). The protein is a Cephaeline 6'-O-methyltransferase (EC 2.1.1.396) involved in emetine/cephaeline biosynthesis in Carapichea ipecacuanha. The sequence matches exactly (350 AA, SHA256 confirmed). The annotation is experimentally supported, not merely computational."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation confirms the answer experimentally (ECO:0000269), but this information was not available to the evaluated model.",
    "The reasoning argument (plant OMT → alkaloid biosynthesis) is a general statistical tendency in plant secondary metabolism, not a deterministic rule. A small number of plant OMTs participate in other pathways.",
    "The specific identification as an emetine/cephaeline biosynthesis enzyme requires knowledge of the organism or substrate, but the question asks for the pathway category, which is reasonably inferable from the enzyme class and kingdom.",
    "The identity of the protein (E7FL15) was inferred mechanically from dataset metadata and was not provided to the model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (cell wall biogenesis) and D (L-leucine degradation) are clearly implausible for an O-methyltransferase. Option B (lipid metabolism) is a weak distractor since some methyltransferases participate in lipid modification, but plant OMTs with the GGGNG/SAM-binding fold are predominantly in alkaloid and phenylpropanoid pathways. Option C is the most defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0195",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E7FL15 (CIOMT_CARIP) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence code ECO:0000269 (PubMed:21228475). The protein is a Cephaeline 6'-O-methyltransferase (EC 2.1.1.396) involved in emetine/cephaeline biosynthesis in Carapichea ipecacuanha. The sequence matches exactly (350 AA, SHA256 confirmed). The annotation is experimentally supported, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'GGGNG' motif (residues ~168-172: 'VGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEG') characteristic of SAM-dependent O-methyltransferases. In plants, O-methyltransferases with this domain architecture are overwhelmingly associated with secondary metabolism, particularly alkaloid biosynthesis (e.g., berberine, morphine, emetine pathways), rather than cell wall biogenesis, lipid metabolism, or amino acid degradation. A biologist recognizing the plant OMT fold can reasonably infer alkaloid biosynthesis as the most probable pathway among the four choices.",
    "missing_item_specific_fact": "The specific substrate (cephaeline/7'-O-demethylcephaeline) and organism (Carapichea ipecacuanha, ipecac) are not provided in the input. However, the general biological argument that plant SAM-dependent OMTs predominantly function in alkaloid/secondary metabolite biosynthesis is sufficient to distinguish C from the other three options without memorizing this protein's annotation.",
    "reason": "The GGGNG SAM-binding motif identifies the protein as a methyltransferase. Among the four pathway options, alkaloid biosynthesis is the most biologically coherent assignment for a plant O-methyltransferase. Cell wall biogenesis (A) and L-leucine degradation (D) are implausible for an OMT. Lipid metabolism (B) is possible but far less common for plant OMTs with this domain architecture. The reasoning chain (plant OMT → secondary metabolism → alkaloid biosynthesis) is a defensible general biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (cell wall biogenesis) and D (L-leucine degradation) are clearly implausible for an O-methyltransferase. Option B (lipid metabolism) is a weak distractor since some methyltransferases participate in lipid modification, but plant OMTs with the GGGNG/SAM-binding fold are predominantly in alkaloid and phenylpropanoid pathways. Option C is the most defensible choice."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation confirms the answer experimentally (ECO:0000269), but this information was not available to the evaluated model.",
    "The reasoning argument (plant OMT → alkaloid biosynthesis) is a general statistical tendency in plant secondary metabolism, not a deterministic rule. A small number of plant OMTs participate in other pathways.",
    "The specific identification as an emetine/cephaeline biosynthesis enzyme requires knowledge of the organism or substrate, but the question asks for the pathway category, which is reasonably inferable from the enzyme class and kingdom.",
    "The identity of the protein (E7FL15) was inferred mechanically from dataset metadata and was not provided to the model."
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

**Accession:** `E7FL15` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:03.494312+00:00.  

```json
"E7FL15"
```

Source SHA-256: `609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:03.494312+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21228475","source":"PubMed"}],"value":"2.1.1.395"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"7'-O-demethylcephaeline 7'-O-methyltransferase CiOMT"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"Cephaeline synthase CiOMT"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"},{"evidenceCode":"ECO:0000312","id":"BAJ72588.1","source":"EMBL"}],"value":"7'-O-demethylcephaeline/cephaeline O-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ72588.1","source":"EMBL"}],"value":"7'OMT"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"CiOMT"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21228475","source":"PubMed"}],"value":"2.1.1.396"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"Cephaeline 6'-O-methyltransferase CiOMT"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"21228475","source":"PubMed"}],"value":"Emetine synthase CiOMT"}]}}
```

Source SHA-256: `609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:03.494312+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21228475","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:03.494312+00:00.  

```json
{"citation":{"authors":["Cheong B.E.","Takemura T.","Yoshimatsu K.","Sato F."],"citationCrossReferences":[{"database":"PubMed","id":"21228475"},{"database":"DOI","id":"10.1271/bbb.100605"}],"citationType":"journal article","firstPage":"107","id":"21228475","journal":"Biosci. Biotechnol. Biochem.","lastPage":"113","publicationDate":"2011","title":"Molecular cloning of an O-methyltransferase from adventitious roots of Carapichea ipecacuanha.","volume":"75"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ72588.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Root"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION"]}
```

Source SHA-256: `609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)  
**Locator:** `lines 1-21`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:05.930954+00:00.  

```text
ID   CIOMT_CARIP             Reviewed;         350 AA.
AC   E7FL15;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-APR-2011, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Cephaeline 6'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};
DE            Short=Emetine synthase CiOMT {ECO:0000303|PubMed:21228475};
DE            EC=2.1.1.396 {ECO:0000269|PubMed:21228475};
DE   AltName: Full=7'-O-demethylcephaeline 7'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};
DE            Short=Cephaeline synthase CiOMT {ECO:0000303|PubMed:21228475};
DE            EC=2.1.1.395 {ECO:0000269|PubMed:21228475};
DE   AltName: Full=7'-O-demethylcephaeline/cephaeline O-methyltransferase {ECO:0000303|PubMed:21228475, ECO:0000312|EMBL:BAJ72588.1};
DE            Short=7'OMT {ECO:0000312|EMBL:BAJ72588.1};
DE            Short=CiOMT {ECO:0000303|PubMed:21228475};
GN   Name=OMT {ECO:0000303|PubMed:21228475};
OS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;
OC   Carapichea.
OX   NCBI_TaxID=77880;
```

Source SHA-256: `aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)  
**Locator:** `lines 22-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:05.930954+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAJ72588.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.
RC   TISSUE=Root;
RX   PubMed=21228475; DOI=10.1271/bbb.100605;
RA   Cheong B.E., Takemura T., Yoshimatsu K., Sato F.;
RT   "Molecular cloning of an O-methyltransferase from adventitious roots of
RT   Carapichea ipecacuanha.";
RL   Biosci. Biotechnol. Biochem. 75:107-113(2011).
```

Source SHA-256: `aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)  
**Locator:** `lines 66-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:28:05.930954+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:21228475}.
```

Source SHA-256: `aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 195. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
