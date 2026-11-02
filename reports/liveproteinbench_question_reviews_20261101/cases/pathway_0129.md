# pathway_0129

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPESYSNFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLHDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHVDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. L-homoserine from L-aspartate: step 1/3. .
B. tetrahydrofolate biosynthesis
C. coenzyme A biosynthesis
D. Alkaloid biosynthesis. .
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

> The exact sequence matches UniProt entry B6ZKM4, which annotates it as an ipecac alkaloid beta-glucosidase and assigns it to alkaloid biosynthesis. The pathway annotation is attributed to a publication reporting function and pathway evidence, supporting choice D.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support general enzyme-family inference, but it does not provide a concrete biological basis to distinguish alkaloid biosynthesis from the other listed pathways.


**Missing item-specific fact**

> The protein-specific finding that this enzyme is an ipecac alkaloid beta-glucosidase involved in alkaloid biosynthesis.


**Reason**

> Selecting D depends on a specific functional/pathway annotation or experimental result not supplied in the question; recognizing the sequence or recalling its entry would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available sequence-matched annotation supports D, and no evidence here supports another listed pathway.


### Important caveats

- The supporting annotation is attributed to a published study, but the primary paper was not independently retrieved or validated here.
- The reviewer-only database evidence was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support general enzyme-family inference, but it does not provide a concrete biological basis to distinguish alkaloid biosynthesis from the other listed pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that this enzyme is an ipecac alkaloid beta-glucosidase involved in alkaloid biosynthesis.",
    "reason": "Selecting D depends on a specific functional/pathway annotation or experimental result not supplied in the question; recognizing the sequence or recalling its entry would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "pathway_0129",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry B6ZKM4, which annotates it as an ipecac alkaloid beta-glucosidase and assigns it to alkaloid biosynthesis. The pathway annotation is attributed to a publication reporting function and pathway evidence, supporting choice D."
  },
  "important_caveats": [
    "The supporting annotation is attributed to a published study, but the primary paper was not independently retrieved or validated here.",
    "The reviewer-only database evidence was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence-matched annotation supports D, and no evidence here supports another listed pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry B6ZKM4, which annotates it as an ipecac alkaloid beta-glucosidase and assigns it to alkaloid biosynthesis. The pathway annotation is attributed to a publication reporting function and pathway evidence, supporting choice D.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support general enzyme-family inference, but it does not provide a concrete biological basis to distinguish alkaloid biosynthesis from the other listed pathways.",
    "missing_item_specific_fact": "The protein-specific finding that this enzyme is an ipecac alkaloid beta-glucosidase involved in alkaloid biosynthesis.",
    "reason": "Selecting D depends on a specific functional/pathway annotation or experimental result not supplied in the question; recognizing the sequence or recalling its entry would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence-matched annotation supports D, and no evidence here supports another listed pathway."
  },
  "important_caveats": [
    "The supporting annotation is attributed to a published study, but the primary paper was not independently retrieved or validated here.",
    "The reviewer-only database evidence was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B6ZKM4 (sequence SHA256 matched) is annotated as 'Ipecac alkaloid beta-glucosidase 2' (EC 3.2.1.-) from Carapichea ipecacuanha. The pathway annotation 'Alkaloid biosynthesis' carries evidence code ECO:0000269 (inferred from direct assay), referencing Nomura et al. 2008 JBC (PMID 18927081), which experimentally characterized this beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis. The expected answer D is directly supported by experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of glycosyl hydrolase family 1 (GH1) beta-glucosidases (e.g., WDTFTHTHPE, NEPESYSNFF, HWDVPQ catalytic region). Recognizing the protein as a beta-glucosidase allows elimination of the other options: (A) L-homoserine from L-aspartate step 1/3 requires aspartate kinase (a kinase, not a glycosidase); (B) tetrahydrofolate biosynthesis involves GTP cyclohydrolase, dihydroneopterin aldolase, HPPK, and DHPS (none are glycosidases); (C) coenzyme A biosynthesis involves pantothenate kinase, phosphopantothenate synthetase, and CoA synthetase (none are glycosidases). Plant beta-glucosidases are well-known to participate in secondary metabolite/alkaloid biosynthesis by cleaving sugar moieties from glycosylated alkaloid precursors, making D the only pathway consistent with a glycosidase enzyme.


**Missing item-specific fact**

> None strictly required. The elimination logic (glycosidase ≠ kinase/cyclohydrolase/synthetase) is general biochemistry. The specific substrate identity (ipecac alkaloid glucoside) is an additional confirmatory detail but not needed to distinguish among the four options.


**Reason**

> A model that recognizes GH1 beta-glucosidase family motifs can eliminate options A, B, and C on the basis that those pathways do not involve glycosidase-type enzymes. Plant beta-glucosidases are commonly associated with secondary metabolite and alkaloid pathways, making D the only defensible choice without needing to recall this specific protein's UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically distinct enzyme classes (kinase, cyclohydrolase/synthetase, kinase/synthetase, glycosidase). A correctly identified beta-glucosidase unambiguously points to D among these choices. No other option involves a glycosidase step.


### Important caveats

- The reviewer-only evidence confirms the pathway annotation is experimentally supported (ECO:0000269), not merely computational inference.
- The reasoning argument depends on recognizing GH1 motifs in the sequence; if a model fails to identify the protein as a glycosidase, the elimination logic collapses.
- The specific assignment to 'alkaloid' biosynthesis (vs. other glycosidase-involving pathways like flavonoid metabolism) is not fully derivable from sequence alone, but among the four given options, only D involves a glycosidase, so the elimination is unambiguous.
- The protein is from Carapichea ipecacuanha (Ipecac), a plant well-known for terpenoid-isoquinoline alkaloids (emetine, cephaeline), which provides additional biological context but is not stated in the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of glycosyl hydrolase family 1 (GH1) beta-glucosidases (e.g., WDTFTHTHPE, NEPESYSNFF, HWDVPQ catalytic region). Recognizing the protein as a beta-glucosidase allows elimination of the other options: (A) L-homoserine from L-aspartate step 1/3 requires aspartate kinase (a kinase, not a glycosidase); (B) tetrahydrofolate biosynthesis involves GTP cyclohydrolase, dihydroneopterin aldolase, HPPK, and DHPS (none are glycosidases); (C) coenzyme A biosynthesis involves pantothenate kinase, phosphopantothenate synthetase, and CoA synthetase (none are glycosidases). Plant beta-glucosidases are well-known to participate in secondary metabolite/alkaloid biosynthesis by cleaving sugar moieties from glycosylated alkaloid precursors, making D the only pathway consistent with a glycosidase enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The elimination logic (glycosidase ≠ kinase/cyclohydrolase/synthetase) is general biochemistry. The specific substrate identity (ipecac alkaloid glucoside) is an additional confirmatory detail but not needed to distinguish among the four options.",
    "reason": "A model that recognizes GH1 beta-glucosidase family motifs can eliminate options A, B, and C on the basis that those pathways do not involve glycosidase-type enzymes. Plant beta-glucosidases are commonly associated with secondary metabolite and alkaloid pathways, making D the only defensible choice without needing to recall this specific protein's UniProt annotation."
  },
  "case_id": "pathway_0129",
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
    "reason": "UniProt entry B6ZKM4 (sequence SHA256 matched) is annotated as 'Ipecac alkaloid beta-glucosidase 2' (EC 3.2.1.-) from Carapichea ipecacuanha. The pathway annotation 'Alkaloid biosynthesis' carries evidence code ECO:0000269 (inferred from direct assay), referencing Nomura et al. 2008 JBC (PMID 18927081), which experimentally characterized this beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis. The expected answer D is directly supported by experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the pathway annotation is experimentally supported (ECO:0000269), not merely computational inference.",
    "The reasoning argument depends on recognizing GH1 motifs in the sequence; if a model fails to identify the protein as a glycosidase, the elimination logic collapses.",
    "The specific assignment to 'alkaloid' biosynthesis (vs. other glycosidase-involving pathways like flavonoid metabolism) is not fully derivable from sequence alone, but among the four given options, only D involves a glycosidase, so the elimination is unambiguous.",
    "The protein is from Carapichea ipecacuanha (Ipecac), a plant well-known for terpenoid-isoquinoline alkaloids (emetine, cephaeline), which provides additional biological context but is not stated in the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct enzyme classes (kinase, cyclohydrolase/synthetase, kinase/synthetase, glycosidase). A correctly identified beta-glucosidase unambiguously points to D among these choices. No other option involves a glycosidase step."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0129",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B6ZKM4 (sequence SHA256 matched) is annotated as 'Ipecac alkaloid beta-glucosidase 2' (EC 3.2.1.-) from Carapichea ipecacuanha. The pathway annotation 'Alkaloid biosynthesis' carries evidence code ECO:0000269 (inferred from direct assay), referencing Nomura et al. 2008 JBC (PMID 18927081), which experimentally characterized this beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis. The expected answer D is directly supported by experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of glycosyl hydrolase family 1 (GH1) beta-glucosidases (e.g., WDTFTHTHPE, NEPESYSNFF, HWDVPQ catalytic region). Recognizing the protein as a beta-glucosidase allows elimination of the other options: (A) L-homoserine from L-aspartate step 1/3 requires aspartate kinase (a kinase, not a glycosidase); (B) tetrahydrofolate biosynthesis involves GTP cyclohydrolase, dihydroneopterin aldolase, HPPK, and DHPS (none are glycosidases); (C) coenzyme A biosynthesis involves pantothenate kinase, phosphopantothenate synthetase, and CoA synthetase (none are glycosidases). Plant beta-glucosidases are well-known to participate in secondary metabolite/alkaloid biosynthesis by cleaving sugar moieties from glycosylated alkaloid precursors, making D the only pathway consistent with a glycosidase enzyme.",
    "missing_item_specific_fact": "None strictly required. The elimination logic (glycosidase ≠ kinase/cyclohydrolase/synthetase) is general biochemistry. The specific substrate identity (ipecac alkaloid glucoside) is an additional confirmatory detail but not needed to distinguish among the four options.",
    "reason": "A model that recognizes GH1 beta-glucosidase family motifs can eliminate options A, B, and C on the basis that those pathways do not involve glycosidase-type enzymes. Plant beta-glucosidases are commonly associated with secondary metabolite and alkaloid pathways, making D the only defensible choice without needing to recall this specific protein's UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct enzyme classes (kinase, cyclohydrolase/synthetase, kinase/synthetase, glycosidase). A correctly identified beta-glucosidase unambiguously points to D among these choices. No other option involves a glycosidase step."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the pathway annotation is experimentally supported (ECO:0000269), not merely computational inference.",
    "The reasoning argument depends on recognizing GH1 motifs in the sequence; if a model fails to identify the protein as a glycosidase, the elimination logic collapses.",
    "The specific assignment to 'alkaloid' biosynthesis (vs. other glycosidase-involving pathways like flavonoid metabolism) is not fully derivable from sequence alone, but among the four given options, only D involves a glycosidase, so the elimination is unambiguous.",
    "The protein is from Carapichea ipecacuanha (Ipecac), a plant well-known for terpenoid-isoquinoline alkaloids (emetine, cephaeline), which provides additional biological context but is not stated in the question."
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

**Accession:** `B6ZKM4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 44. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.131375+00:00.  

```json
"B6ZKM4"
```

Source SHA-256: `354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.131375+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"3.2.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Ipecac alkaloid beta-glucosidase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"IpeGLU2"}]}}
```

Source SHA-256: `354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.131375+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.131375+00:00.  

```json
{"citation":{"authors":["Nomura T.","Quesada A.L.","Kutchan T.M."],"citationCrossReferences":[{"database":"PubMed","id":"18927081"},{"database":"DOI","id":"10.1074/jbc.m806953200"}],"citationType":"journal article","firstPage":"34650","id":"18927081","journal":"J. Biol. Chem.","lastPage":"34659","publicationDate":"2008","title":"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.","volume":"283"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAH02545.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Root"},{"type":"TISSUE","value":"Shoot"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `354892c453442df6b8a8703ec4aa29037694a198fcc3f4c682270abff718a772`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-01T06:27:55.242337+00:00.  

```text
ID   GLU2_CARIP              Reviewed;         543 AA.
AC   B6ZKM4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-FEB-2009, sequence version 1.
DT   28-JAN-2026, entry version 44.
DE   RecName: Full=Ipecac alkaloid beta-glucosidase 2 {ECO:0000303|PubMed:18927081};
DE            Short=IpeGLU2 {ECO:0000303|PubMed:18927081};
DE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};
GN   Name=GLU2 {ECO:0000303|PubMed:18927081};
OS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;
OC   Carapichea.
OX   NCBI_TaxID=77880;
```

Source SHA-256: `dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)  
**Locator:** `lines 16-23`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-01T06:27:55.242337+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAH02545.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RC   TISSUE=Root, and Shoot;
RX   PubMed=18927081; DOI=10.1074/jbc.m806953200;
RA   Nomura T., Quesada A.L., Kutchan T.M.;
RT   "The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis
RT   in Psychotria ipecacuanha.";
RL   J. Biol. Chem. 283:34650-34659(2008).
```

Source SHA-256: `dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM4?format=txt&versions=44)  
**Locator:** `lines 41-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 44 / 1.  
**Retrieved:** 2026-11-01T06:27:55.242337+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:18927081}.
```

Source SHA-256: `dba9b28a9f04f15e6605a1a0435dd29c1c58104dd69f5c4d39df880ddc9b47b1`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 129. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
