# pathway_0027

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFSNLHLPLNPIDKVNQPPVYYLQVQDGLIICSGLCWTTAYILYIRQAYRDKSYGMPLVCLCANIAWEFLFGAAIPESAAQVVSFFPWFVIDIGIVYTTWKFGREQWKHAPLVAQNLGWILLGGIAGMLVMFWAFLKTYDNRYEAGFYLAWTDQIIVSTTSVAQLMSRNNTSGHSWGIWFTRWIGSVFAELIFVWRYWNYPESYPVAATHVTIFLFIVTEVADLTYPFVYASLDKKEKKKLK

[Multiple Choices]
A. Secondary metabolite biosynthesis
B. fatty acid beta-oxidation. .
C. Carbohydrate degradation
D. iron-sulfur cluster biosynthesis. .
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

> The exact sequence matches a UniProt entry annotated as the Pyr4-family terpene cyclase mfmH, with its pathway listed as secondary metabolite biosynthesis (terpenoid biosynthesis). The annotation cites a publication and carries experimental evidence code ECO:0000269; the cited study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic, but that feature does not meaningfully identify secondary-metabolite biosynthesis or distinguish it from the listed alternatives.


**Missing item-specific fact**

> The protein-specific identification and functional/pathway evidence linking this sequence to the mfmH terpene-cyclase role.


**Reason**

> The pathway annotation supports the key, but that annotation and its cited functional evidence are absent from the question. Recognizing the exact sequence from an external database would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence does not establish a competing pathway, and the sequence-matched annotation supports A. The input’s lack of sufficient discrimination is a lookup-dependence issue rather than evidence that multiple options are equally correct.


### Important caveats

- Reviewer-only database evidence was not available to the evaluated model.
- The historical UniProt record matches the sequence, but the author's exact source snapshot is unknown; the cited primary study was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic, but that feature does not meaningfully identify secondary-metabolite biosynthesis or distinguish it from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional/pathway evidence linking this sequence to the mfmH terpene-cyclase role.",
    "reason": "The pathway annotation supports the key, but that annotation and its cited functional evidence are absent from the question. Recognizing the exact sequence from an external database would be lookup, not reasoning from the supplied input."
  },
  "case_id": "pathway_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as the Pyr4-family terpene cyclase mfmH, with its pathway listed as secondary metabolite biosynthesis (terpenoid biosynthesis). The annotation cites a publication and carries experimental evidence code ECO:0000269; the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The historical UniProt record matches the sequence, but the author's exact source snapshot is unknown; the cited primary study was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not establish a competing pathway, and the sequence-matched annotation supports A. The input’s lack of sufficient discrimination is a lookup-dependence issue rather than evidence that multiple options are equally correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as the Pyr4-family terpene cyclase mfmH, with its pathway listed as secondary metabolite biosynthesis (terpenoid biosynthesis). The annotation cites a publication and carries experimental evidence code ECO:0000269; the cited study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic, but that feature does not meaningfully identify secondary-metabolite biosynthesis or distinguish it from the listed alternatives.",
    "missing_item_specific_fact": "The protein-specific identification and functional/pathway evidence linking this sequence to the mfmH terpene-cyclase role.",
    "reason": "The pathway annotation supports the key, but that annotation and its cited functional evidence are absent from the question. Recognizing the exact sequence from an external database would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not establish a competing pathway, and the sequence-matched annotation supports A. The input’s lack of sufficient discrimination is a lookup-dependence issue rather than evidence that multiple options are equally correct."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The historical UniProt record matches the sequence, but the author's exact source snapshot is unknown; the cited primary study was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DY23 (Pyr4-family terpene cyclase mfmH from Annulohypoxylon moriforme) is annotated with the pathway 'Secondary metabolite biosynthesis; terpenoid biosynthesis' backed by ECO:0000269 (direct assay) evidence from PubMed:38404388 (Yan & Matsuda, Chem. Sci. 2024). The protein is part of the 11'-O-desmethylfendlerol biosynthesis cluster and has EC 4.2.3.- (terpene cyclase). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed). Choice A is directly supported by experimental annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits multiple long hydrophobic stretches (e.g., 'LIICSGLCWTTAYILY', 'GWILLGGIAGMLVMFWAFLK', 'GIWFTRWIGSVFAELIFVWRYWNYPESYPVAATHVTIFLFIVTEVADLTYPFVYASLDK') indicating a multi-transmembrane membrane-bound protein of ~242 aa. Fatty acid beta-oxidation enzymes (acyl-CoA dehydrogenases, enoyl-CoA hydratases, thiolases) are predominantly soluble with characteristic FAD/NAD-binding Rossmann folds absent here. Carbohydrate-degrading enzymes (glycosidases, cellulases) require specific catalytic motifs (e.g., DxDxDxK, E-D-E) not present. Iron-sulfur cluster biosynthetic machinery (e.g., NifU/SufU scaffolds, cysteine desulfurases) features distinctive C-x-x-C or C-x3-C Fe-S binding motifs and different architectures. By elimination of these three well-characterized pathway enzyme classes, and recognizing that small membrane-bound proteins with multiple TM helices in fungi are commonly terpene cyclases or polyketide-synthase-associated enzymes involved in secondary metabolite biosynthesis, Choice A is the most defensible answer.


**Missing item-specific fact**

> Positive identification of the Pyr4-family terpene cyclase fold (a non-canonical, membrane-bound terpene cyclase family distinct from the classical DDxxD/NDxxD soluble terpene cyclases) would require specific knowledge of this recently characterized family. However, this is not strictly necessary to select A by elimination of the other three options.


**Reason**

> The membrane-bound architecture with multiple TM helices, the relatively small size (~242 aa), and the clear absence of diagnostic motifs for beta-oxidation, glycosidase, or Fe-S cluster machinery provide a general biological elimination argument that meaningfully distinguishes A from B, C, and D. The positive identification as a terpene cyclase adds specificity but the elimination reasoning alone is sufficient to arrive at A.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (B, C, D) correspond to pathway enzyme classes with well-known, distinctive structural and sequence features that are clearly absent from this membrane-bound, multi-TM protein. No reasonable biological argument supports selecting B, C, or D over A.


### Important caveats

- The Pyr4-family terpene cyclase classification is a relatively recent (2024) characterization; a model without knowledge of this specific family would rely primarily on elimination rather than positive identification.
- The organism (Annulohypoxylon moriforme, a filamentous fungus) is not provided in the question input; fungal origin strengthens the secondary-metabolite-gene-cluster association but is not given.
- The UniProt annotation carries ECO:0000269 (direct assay), indicating experimental validation of the pathway assignment, not mere computational inference.
- The entry was first released in April 2025; if the benchmark was constructed before that date, the annotation may not have been available at construction time (though the sequence itself was in the dataset).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits multiple long hydrophobic stretches (e.g., 'LIICSGLCWTTAYILY', 'GWILLGGIAGMLVMFWAFLK', 'GIWFTRWIGSVFAELIFVWRYWNYPESYPVAATHVTIFLFIVTEVADLTYPFVYASLDK') indicating a multi-transmembrane membrane-bound protein of ~242 aa. Fatty acid beta-oxidation enzymes (acyl-CoA dehydrogenases, enoyl-CoA hydratases, thiolases) are predominantly soluble with characteristic FAD/NAD-binding Rossmann folds absent here. Carbohydrate-degrading enzymes (glycosidases, cellulases) require specific catalytic motifs (e.g., DxDxDxK, E-D-E) not present. Iron-sulfur cluster biosynthetic machinery (e.g., NifU/SufU scaffolds, cysteine desulfurases) features distinctive C-x-x-C or C-x3-C Fe-S binding motifs and different architectures. By elimination of these three well-characterized pathway enzyme classes, and recognizing that small membrane-bound proteins with multiple TM helices in fungi are commonly terpene cyclases or polyketide-synthase-associated enzymes involved in secondary metabolite biosynthesis, Choice A is the most defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of the Pyr4-family terpene cyclase fold (a non-canonical, membrane-bound terpene cyclase family distinct from the classical DDxxD/NDxxD soluble terpene cyclases) would require specific knowledge of this recently characterized family. However, this is not strictly necessary to select A by elimination of the other three options.",
    "reason": "The membrane-bound architecture with multiple TM helices, the relatively small size (~242 aa), and the clear absence of diagnostic motifs for beta-oxidation, glycosidase, or Fe-S cluster machinery provide a general biological elimination argument that meaningfully distinguishes A from B, C, and D. The positive identification as a terpene cyclase adds specificity but the elimination reasoning alone is sufficient to arrive at A."
  },
  "case_id": "pathway_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DY23 (Pyr4-family terpene cyclase mfmH from Annulohypoxylon moriforme) is annotated with the pathway 'Secondary metabolite biosynthesis; terpenoid biosynthesis' backed by ECO:0000269 (direct assay) evidence from PubMed:38404388 (Yan & Matsuda, Chem. Sci. 2024). The protein is part of the 11'-O-desmethylfendlerol biosynthesis cluster and has EC 4.2.3.- (terpene cyclase). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed). Choice A is directly supported by experimental annotation."
  },
  "important_caveats": [
    "The Pyr4-family terpene cyclase classification is a relatively recent (2024) characterization; a model without knowledge of this specific family would rely primarily on elimination rather than positive identification.",
    "The organism (Annulohypoxylon moriforme, a filamentous fungus) is not provided in the question input; fungal origin strengthens the secondary-metabolite-gene-cluster association but is not given.",
    "The UniProt annotation carries ECO:0000269 (direct assay), indicating experimental validation of the pathway assignment, not mere computational inference.",
    "The entry was first released in April 2025; if the benchmark was constructed before that date, the annotation may not have been available at construction time (though the sequence itself was in the dataset)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B, C, D) correspond to pathway enzyme classes with well-known, distinctive structural and sequence features that are clearly absent from this membrane-bound, multi-TM protein. No reasonable biological argument supports selecting B, C, or D over A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DY23 (Pyr4-family terpene cyclase mfmH from Annulohypoxylon moriforme) is annotated with the pathway 'Secondary metabolite biosynthesis; terpenoid biosynthesis' backed by ECO:0000269 (direct assay) evidence from PubMed:38404388 (Yan & Matsuda, Chem. Sci. 2024). The protein is part of the 11'-O-desmethylfendlerol biosynthesis cluster and has EC 4.2.3.- (terpene cyclase). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed). Choice A is directly supported by experimental annotation.",
    "evidence_ids": ["C5", "C6", "H3", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits multiple long hydrophobic stretches (e.g., 'LIICSGLCWTTAYILY', 'GWILLGGIAGMLVMFWAFLK', 'GIWFTRWIGSVFAELIFVWRYWNYPESYPVAATHVTIFLFIVTEVADLTYPFVYASLDK') indicating a multi-transmembrane membrane-bound protein of ~242 aa. Fatty acid beta-oxidation enzymes (acyl-CoA dehydrogenases, enoyl-CoA hydratases, thiolases) are predominantly soluble with characteristic FAD/NAD-binding Rossmann folds absent here. Carbohydrate-degrading enzymes (glycosidases, cellulases) require specific catalytic motifs (e.g., DxDxDxK, E-D-E) not present. Iron-sulfur cluster biosynthetic machinery (e.g., NifU/SufU scaffolds, cysteine desulfurases) features distinctive C-x-x-C or C-x3-C Fe-S binding motifs and different architectures. By elimination of these three well-characterized pathway enzyme classes, and recognizing that small membrane-bound proteins with multiple TM helices in fungi are commonly terpene cyclases or polyketide-synthase-associated enzymes involved in secondary metabolite biosynthesis, Choice A is the most defensible answer.",
    "missing_item_specific_fact": "Positive identification of the Pyr4-family terpene cyclase fold (a non-canonical, membrane-bound terpene cyclase family distinct from the classical DDxxD/NDxxD soluble terpene cyclases) would require specific knowledge of this recently characterized family. However, this is not strictly necessary to select A by elimination of the other three options.",
    "reason": "The membrane-bound architecture with multiple TM helices, the relatively small size (~242 aa), and the clear absence of diagnostic motifs for beta-oxidation, glycosidase, or Fe-S cluster machinery provide a general biological elimination argument that meaningfully distinguishes A from B, C, and D. The positive identification as a terpene cyclase adds specificity but the elimination reasoning alone is sufficient to arrive at A."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (B, C, D) correspond to pathway enzyme classes with well-known, distinctive structural and sequence features that are clearly absent from this membrane-bound, multi-TM protein. No reasonable biological argument supports selecting B, C, or D over A."
  },
  "important_caveats": [
    "The Pyr4-family terpene cyclase classification is a relatively recent (2024) characterization; a model without knowledge of this specific family would rely primarily on elimination rather than positive identification.",
    "The organism (Annulohypoxylon moriforme, a filamentous fungus) is not provided in the question input; fungal origin strengthens the secondary-metabolite-gene-cluster association but is not given.",
    "The UniProt annotation carries ECO:0000269 (direct assay), indicating experimental validation of the pathway assignment, not mere computational inference.",
    "The entry was first released in April 2025; if the benchmark was constructed before that date, the annotation may not have been available at construction time (though the sequence itself was in the dataset)."
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

**Accession:** `P0DY23` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38404388","source":"PubMed"}],"value":"11'-O-desmethylfendlerol biosynthesis cluster protein H"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38404388","source":"PubMed"}],"value":"4.2.3.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38404388","source":"PubMed"}],"value":"Pyr4-family terpene cyclase mfmH"}}}
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38404388","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY23.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:06.355655+00:00.  

```json
{"citation":{"authors":["Yan D.","Matsuda Y."],"citationCrossReferences":[{"database":"PubMed","id":"38404388"},{"database":"DOI","id":"10.1039/d3sc06001b"}],"citationType":"journal article","firstPage":"3011","id":"38404388","journal":"Chem. Sci.","lastPage":"3017","publicationDate":"2024","title":"Global genome mining-driven discovery of an unusual biosynthetic logic for fungal polyketide-terpenoid hybrids.","volume":"15"},"referenceComments":[{"type":"STRAIN","value":"CBS 123579"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `6af7a985bb93d19c99b5af4867a56ec8d88ffbb618fc982eb2bddb21ed56136c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:08.630908+00:00.  

```text
ID   MFMH_ANNMO              Reviewed;         242 AA.
AC   P0DY23;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   09-APR-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=Pyr4-family terpene cyclase mfmH {ECO:0000303|PubMed:38404388};
DE            EC=4.2.3.- {ECO:0000269|PubMed:38404388};
DE   AltName: Full=11'-O-desmethylfendlerol biosynthesis cluster protein H {ECO:0000303|PubMed:38404388};
GN   Name=mfmH {ECO:0000303|PubMed:38404388}; ORFNames=F4805DRAFT_30178;
OS   Annulohypoxylon moriforme (Filamentous fungus) (Hypoxylon moriforme).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Xylariomycetidae; Xylariales; Hypoxylaceae; Annulohypoxylon.
OX   NCBI_TaxID=326622;
```

Source SHA-256: `3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)  
**Locator:** `lines 28-35`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:08.630908+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RC   STRAIN=CBS 123579;
RX   PubMed=38404388; DOI=10.1039/d3sc06001b;
RA   Yan D., Matsuda Y.;
RT   "Global genome mining-driven discovery of an unusual biosynthetic logic for
RT   fungal polyketide-terpenoid hybrids.";
RL   Chem. Sci. 15:3011-3017(2024).
```

Source SHA-256: `3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY23?format=txt&versions=3)  
**Locator:** `lines 55-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:08.630908+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:38404388}.
```

Source SHA-256: `3fa07f60335a414512ee3950d17eeba0727ca5a77e80ddc7a1d8da8b59a78b2d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
