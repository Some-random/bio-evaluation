# pathway_0094

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGRNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAINSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPESYSNFFGVAYDTPPKAHALKASRLLVPTTVARPSKPVRVFASTADPGTTTADQVYKVGHNLLLAHAAAIQVYRDKFQNTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQLLGPRLREFTPDQKKLLIGSYDYVGVNYYTATYVSSAQPPHDKKKAVFHTDGNFYTTDSKDGVLIGPLAGPAWLNIVPEGIYHVLQDIKENYEDPVIYITENGVYEVNDTAKTLSEARVDTTRLHYLQDHLSKVLEARHQGVRVQGYLVWSLMDNWELRAGYTSRFGLIHIDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKARPQEDDGAFDTPRKRLRKY

[Multiple Choices]
A. Alkaloid biosynthesis. .
B. O-acetyl-L-homoserine from L-homoserine: step 1/1. .
C. L-threonine from L-aspartate: step 5/5. .
D. Lipid metabolism. .
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

> The supplied sequence exactly matches the reviewed UniProt sequence for IpeGLU1, annotated to alkaloid biosynthesis with experimental evidence code ECO:0000269 citing PubMed 18927081. The archived entry also records this pathway annotation. This supports choice A for this protein, though the cited paper was not independently assessed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The input gives only a sequence and choices; it provides no biological source or functional context that reliably distinguishes these pathways. A broad sequence-based enzyme-family inference would not by itself establish this protein’s specific pathway.


**Missing item-specific fact**

> The needed fact is that this exact protein is IpeGLU1, an ipecoside beta-D-glucosidase associated with alkaloid biosynthesis; that protein-specific functional/pathway annotation is absent from the model input.


**Reason**

> Selecting A depends on identifying the specific protein or obtaining its functional annotation, not on a concrete pathway-discriminating argument supplied by the sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports A for the sequence-matched protein. The other choices describe distinct pathways or reactions, and no evidence here supports them for this protein.


### Important caveats

- Reviewer-only accession and annotation evidence were not supplied to the evaluated model.
- The current and archived UniProt records match the sequence, but the author's exact source snapshot is unknown.
- The pathway evidence is an annotated, experimentally coded record citing a paper; that paper was not independently retrieved or validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The input gives only a sequence and choices; it provides no biological source or functional context that reliably distinguishes these pathways. A broad sequence-based enzyme-family inference would not by itself establish this protein’s specific pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The needed fact is that this exact protein is IpeGLU1, an ipecoside beta-D-glucosidase associated with alkaloid biosynthesis; that protein-specific functional/pathway annotation is absent from the model input.",
    "reason": "Selecting A depends on identifying the specific protein or obtaining its functional annotation, not on a concrete pathway-discriminating argument supplied by the sequence and choices."
  },
  "case_id": "pathway_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence for IpeGLU1, annotated to alkaloid biosynthesis with experimental evidence code ECO:0000269 citing PubMed 18927081. The archived entry also records this pathway annotation. This supports choice A for this protein, though the cited paper was not independently assessed here."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model.",
    "The current and archived UniProt records match the sequence, but the author's exact source snapshot is unknown.",
    "The pathway evidence is an annotated, experimentally coded record citing a paper; that paper was not independently retrieved or validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports A for the sequence-matched protein. The other choices describe distinct pathways or reactions, and no evidence here supports them for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence for IpeGLU1, annotated to alkaloid biosynthesis with experimental evidence code ECO:0000269 citing PubMed 18927081. The archived entry also records this pathway annotation. This supports choice A for this protein, though the cited paper was not independently assessed here.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The input gives only a sequence and choices; it provides no biological source or functional context that reliably distinguishes these pathways. A broad sequence-based enzyme-family inference would not by itself establish this protein’s specific pathway.",
    "missing_item_specific_fact": "The needed fact is that this exact protein is IpeGLU1, an ipecoside beta-D-glucosidase associated with alkaloid biosynthesis; that protein-specific functional/pathway annotation is absent from the model input.",
    "reason": "Selecting A depends on identifying the specific protein or obtaining its functional annotation, not on a concrete pathway-discriminating argument supplied by the sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports A for the sequence-matched protein. The other choices describe distinct pathways or reactions, and no evidence here supports them for this protein."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model.",
    "The current and archived UniProt records match the sequence, but the author's exact source snapshot is unknown.",
    "The pathway evidence is an annotated, experimentally coded record citing a paper; that paper was not independently retrieved or validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B6ZKM3 (GLU1_CARIP) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:18927081). The protein is Ipecoside beta-D-glucosidase IpeGLU1 (EC 3.2.1.220) from Carapichea ipecacuanha, characterized in a 2008 JBC paper on terpenoid-isoquinoline alkaloid biosynthesis. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed). The annotation is experimentally supported, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is recognizable as a plant beta-glucosidase (GH1 family) from conserved motifs and overall composition, which eliminates options B and C (amino acid biosynthesis steps not catalyzed by glucosidases). However, distinguishing 'Alkaloid biosynthesis' (A) from 'Lipid metabolism' (D) requires knowing that this specific enzyme hydrolyzes ipecoside/strictosidine (terpenoid-isoquinoline alkaloid glycosides) rather than glucosylceramides or other lipid-linked glycosides. Plant beta-glucosidases participate in both alkaloid and lipid pathways, and general sequence features do not resolve substrate specificity at this level.


**Missing item-specific fact**

> The specific substrate identity (ipecoside, a terpenoid-isoquinoline alkaloid glycoside) and the organism context (Carapichea ipecacuanha, an ipecac plant known for alkaloid biosynthesis) are required to assign this beta-glucosidase to alkaloid biosynthesis rather than lipid metabolism. This is an item-specific experimental characterization (PubMed:18927081) not derivable from sequence alone.


**Reason**

> While a model can identify the enzyme as a plant beta-glucosidase from sequence features and eliminate B and C, the choice between A and D depends on the specific substrate (ipecoside vs. lipid glycosides), which is an experimentally determined fact about this particular protein. General biological knowledge about beta-glucosidase families does not resolve this distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Without knowing the specific substrate, a plant beta-glucosidase could plausibly be assigned to either alkaloid biosynthesis or lipid metabolism. Both pathways involve beta-glucosidases in plants. The sequence alone does not contain information sufficient to exclude D (Lipid metabolism) with high confidence. Options B and C are clearly eliminable as they describe amino acid biosynthesis steps not catalyzed by glucosidases.


### Important caveats

- The UniProt pathway annotation carries experimental evidence (ECO:0000269) from the 2008 Nomura et al. paper, lending strong support to the key.
- The entry was first released in Swiss-Prot on 2025-06-18; the author's source snapshot is unknown but the sequence has been unchanged since 2009.
- The reviewer identified the accession via dataset metadata not available to the evaluated model.
- The question format asks for 'primary pathway' which is a broad category; 'Alkaloid biosynthesis' is the UniProt-level pathway label, which is appropriate for this task format.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is recognizable as a plant beta-glucosidase (GH1 family) from conserved motifs and overall composition, which eliminates options B and C (amino acid biosynthesis steps not catalyzed by glucosidases). However, distinguishing 'Alkaloid biosynthesis' (A) from 'Lipid metabolism' (D) requires knowing that this specific enzyme hydrolyzes ipecoside/strictosidine (terpenoid-isoquinoline alkaloid glycosides) rather than glucosylceramides or other lipid-linked glycosides. Plant beta-glucosidases participate in both alkaloid and lipid pathways, and general sequence features do not resolve substrate specificity at this level.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (ipecoside, a terpenoid-isoquinoline alkaloid glycoside) and the organism context (Carapichea ipecacuanha, an ipecac plant known for alkaloid biosynthesis) are required to assign this beta-glucosidase to alkaloid biosynthesis rather than lipid metabolism. This is an item-specific experimental characterization (PubMed:18927081) not derivable from sequence alone.",
    "reason": "While a model can identify the enzyme as a plant beta-glucosidase from sequence features and eliminate B and C, the choice between A and D depends on the specific substrate (ipecoside vs. lipid glycosides), which is an experimentally determined fact about this particular protein. General biological knowledge about beta-glucosidase families does not resolve this distinction."
  },
  "case_id": "pathway_0094",
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
    "reason": "The UniProt entry B6ZKM3 (GLU1_CARIP) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:18927081). The protein is Ipecoside beta-D-glucosidase IpeGLU1 (EC 3.2.1.220) from Carapichea ipecacuanha, characterized in a 2008 JBC paper on terpenoid-isoquinoline alkaloid biosynthesis. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed). The annotation is experimentally supported, not merely computational."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries experimental evidence (ECO:0000269) from the 2008 Nomura et al. paper, lending strong support to the key.",
    "The entry was first released in Swiss-Prot on 2025-06-18; the author's source snapshot is unknown but the sequence has been unchanged since 2009.",
    "The reviewer identified the accession via dataset metadata not available to the evaluated model.",
    "The question format asks for 'primary pathway' which is a broad category; 'Alkaloid biosynthesis' is the UniProt-level pathway label, which is appropriate for this task format."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Without knowing the specific substrate, a plant beta-glucosidase could plausibly be assigned to either alkaloid biosynthesis or lipid metabolism. Both pathways involve beta-glucosidases in plants. The sequence alone does not contain information sufficient to exclude D (Lipid metabolism) with high confidence. Options B and C are clearly eliminable as they describe amino acid biosynthesis steps not catalyzed by glucosidases."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKM3 (GLU1_CARIP) explicitly annotates the pathway as 'Alkaloid biosynthesis' with experimental evidence (ECO:0000269, PubMed:18927081). The protein is Ipecoside beta-D-glucosidase IpeGLU1 (EC 3.2.1.220) from Carapichea ipecacuanha, characterized in a 2008 JBC paper on terpenoid-isoquinoline alkaloid biosynthesis. The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed). The annotation is experimentally supported, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is recognizable as a plant beta-glucosidase (GH1 family) from conserved motifs and overall composition, which eliminates options B and C (amino acid biosynthesis steps not catalyzed by glucosidases). However, distinguishing 'Alkaloid biosynthesis' (A) from 'Lipid metabolism' (D) requires knowing that this specific enzyme hydrolyzes ipecoside/strictosidine (terpenoid-isoquinoline alkaloid glycosides) rather than glucosylceramides or other lipid-linked glycosides. Plant beta-glucosidases participate in both alkaloid and lipid pathways, and general sequence features do not resolve substrate specificity at this level.",
    "missing_item_specific_fact": "The specific substrate identity (ipecoside, a terpenoid-isoquinoline alkaloid glycoside) and the organism context (Carapichea ipecacuanha, an ipecac plant known for alkaloid biosynthesis) are required to assign this beta-glucosidase to alkaloid biosynthesis rather than lipid metabolism. This is an item-specific experimental characterization (PubMed:18927081) not derivable from sequence alone.",
    "reason": "While a model can identify the enzyme as a plant beta-glucosidase from sequence features and eliminate B and C, the choice between A and D depends on the specific substrate (ipecoside vs. lipid glycosides), which is an experimentally determined fact about this particular protein. General biological knowledge about beta-glucosidase families does not resolve this distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Without knowing the specific substrate, a plant beta-glucosidase could plausibly be assigned to either alkaloid biosynthesis or lipid metabolism. Both pathways involve beta-glucosidases in plants. The sequence alone does not contain information sufficient to exclude D (Lipid metabolism) with high confidence. Options B and C are clearly eliminable as they describe amino acid biosynthesis steps not catalyzed by glucosidases."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries experimental evidence (ECO:0000269) from the 2008 Nomura et al. paper, lending strong support to the key.",
    "The entry was first released in Swiss-Prot on 2025-06-18; the author's source snapshot is unknown but the sequence has been unchanged since 2009.",
    "The reviewer identified the accession via dataset metadata not available to the evaluated model.",
    "The question format asks for 'primary pathway' which is a broad category; 'Alkaloid biosynthesis' is the UniProt-level pathway label, which is appropriate for this task format."
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

**Accession:** `B6ZKM3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
"B6ZKM3"
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Ipecac alkaloid beta-glucosidase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"},{"evidenceCode":"ECO:0000312","id":"BAH02544.1","source":"EMBL"}],"value":"IpeGLU1"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"3.2.1.105"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Strictosidine beta-glucosidase IpeGLU1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"3.2.1.220"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"18927081","source":"PubMed"}],"value":"Ipecoside beta-D-glucosidase IpeGLU1"}}}
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/comments/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18927081","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKM3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:01.419788+00:00.  

```json
{"citation":{"authors":["Nomura T.","Quesada A.L.","Kutchan T.M."],"citationCrossReferences":[{"database":"PubMed","id":"18927081"},{"database":"DOI","id":"10.1074/jbc.m806953200"}],"citationType":"journal article","firstPage":"34650","id":"18927081","journal":"J. Biol. Chem.","lastPage":"34659","publicationDate":"2008","title":"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.","volume":"283"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAH02544.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Root"},{"type":"TISSUE","value":"Shoot"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION"]}
```

Source SHA-256: `b4dc990c5f2650c1e16f2454dc482e32dd840c6fdb37b2ea511a19a97fd3b4b4`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:27:52.619495+00:00.  

```text
ID   GLU1_CARIP              Reviewed;         543 AA.
AC   B6ZKM3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   10-FEB-2009, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Ipecoside beta-D-glucosidase IpeGLU1 {ECO:0000303|PubMed:18927081};
DE            EC=3.2.1.220 {ECO:0000269|PubMed:18927081};
DE   AltName: Full=Ipecac alkaloid beta-glucosidase 1 {ECO:0000303|PubMed:18927081};
DE            Short=IpeGLU1 {ECO:0000303|PubMed:18927081, ECO:0000312|EMBL:BAH02544.1};
DE   AltName: Full=Strictosidine beta-glucosidase IpeGLU1 {ECO:0000303|PubMed:18927081};
DE            EC=3.2.1.105 {ECO:0000269|PubMed:18927081};
GN   Name=GLU1 {ECO:0000303|PubMed:18927081};
OS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;
OC   Carapichea.
OX   NCBI_TaxID=77880;
```

Source SHA-256: `90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)  
**Locator:** `lines 19-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:27:52.619495+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAH02544.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.
RC   TISSUE=Root, and Shoot;
RX   PubMed=18927081; DOI=10.1074/jbc.m806953200;
RA   Nomura T., Quesada A.L., Kutchan T.M.;
RT   "The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis
RT   in Psychotria ipecacuanha.";
RL   J. Biol. Chem. 283:34650-34659(2008).
```

Source SHA-256: `90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKM3?format=txt&versions=51)  
**Locator:** `lines 175-175`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-01T06:27:52.619495+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:18927081}.
```

Source SHA-256: `90ae349be568c2efc5445de22d0fd39250b75a79ab4620dfe4d50cedde82d831`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
