# pathway_0002

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDMNTFPANTYCDSIVRFLDAIEYHDDNLTHDERVEGLRHVHSRTAQYFTEPLPRKVLKDVAPRRIAAVTRTISHFIVYCWSKLPREAQVDVSIYLSIINVLDDEISSEPSTQMATFWTDLVQGKQQKHPFWVLFNSHLPRLLRHYDSFCSFNIMRCTFDYFEGCWIEQHNFQGYPGADCYPLFLRRLNCLGGAVAGTIFPAAKFDEQKLFAEISCVMAQIDGPVALVNDLFSFYKEYDQDEANLVTNWCTVDGITMDQALTRLTDDTIHACVRILEILKDKDPDMLATIRGFIHGYVTWHICDFRYRLREIYDREDLGGSSAKFRDYFDTAINVGWVDVEEWTCQVQGFEVDGPVPKGSEIQAYRTNAFGFSVDTRRPHNMDYVGSSIISMFEWVTGYLKGKSR

[Multiple Choices]
A. L-methionine biosynthesis via de novo pathway
B. Secondary metabolite biosynthesis
C. L-methionine biosynthesis via de novo pathway. .
D. NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1. .
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

> The exact sequence matches a UniProt entry annotated as terpene cyclase pbrA, with a pathway annotation of secondary metabolite biosynthesis; the annotation cites experimental evidence (ECO:0000269) and a publication. This supports choice B, though the cited primary study was not independently reviewed here.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5), [C4](#evidence-c4), [H2](#evidence-h2), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices provide no clear, general biological feature that identifies this particular enzyme's pathway. Its pathway assignment depends on knowing its specific function as a terpene cyclase in aspterric acid biosynthesis.


**Missing item-specific fact**

> The protein-specific functional assignment linking this sequence to terpene and secondary-metabolite biosynthesis.


**Reason**

> The pathway annotation supports the key, but that annotation is reviewer-only. Without it, recognizing or inferring this particular protein's function requires an external protein-specific fact; broad sequence reasoning does not meaningfully distinguish the listed pathways.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice B is distinct from the other pathway options. A and C are duplicate versions of the same methionine-pathway answer, but neither is supported as an alternative to B by the supplied evidence.


### Important caveats

- The sequence match is exact, but the author's source snapshot is unknown.
- The UniProt pathway annotation cites experimental evidence, but the cited paper was not independently validated in the supplied reviewer evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices provide no clear, general biological feature that identifies this particular enzyme's pathway. Its pathway assignment depends on knowing its specific function as a terpene cyclase in aspterric acid biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment linking this sequence to terpene and secondary-metabolite biosynthesis.",
    "reason": "The pathway annotation supports the key, but that annotation is reviewer-only. Without it, recognizing or inferring this particular protein's function requires an external protein-specific fact; broad sequence reasoning does not meaningfully distinguish the listed pathways."
  },
  "case_id": "pathway_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5",
      "C4",
      "H2",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as terpene cyclase pbrA, with a pathway annotation of secondary metabolite biosynthesis; the annotation cites experimental evidence (ECO:0000269) and a publication. This supports choice B, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact, but the author's source snapshot is unknown.",
    "The UniProt pathway annotation cites experimental evidence, but the cited paper was not independently validated in the supplied reviewer evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B is distinct from the other pathway options. A and C are duplicate versions of the same methionine-pathway answer, but neither is supported as an alternative to B by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as terpene cyclase pbrA, with a pathway annotation of secondary metabolite biosynthesis; the annotation cites experimental evidence (ECO:0000269) and a publication. This supports choice B, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["H3", "C5", "C4", "H2", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices provide no clear, general biological feature that identifies this particular enzyme's pathway. Its pathway assignment depends on knowing its specific function as a terpene cyclase in aspterric acid biosynthesis.",
    "missing_item_specific_fact": "The protein-specific functional assignment linking this sequence to terpene and secondary-metabolite biosynthesis.",
    "reason": "The pathway annotation supports the key, but that annotation is reviewer-only. Without it, recognizing or inferring this particular protein's function requires an external protein-specific fact; broad sequence reasoning does not meaningfully distinguish the listed pathways."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice B is distinct from the other pathway options. A and C are duplicate versions of the same methionine-pathway answer, but neither is supported as an alternative to B by the supplied evidence."
  },
  "important_caveats": [
    "The sequence match is exact, but the author's source snapshot is unknown.",
    "The UniProt pathway annotation cites experimental evidence, but the cited paper was not independently validated in the supplied reviewer evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0F7TWX5 (sequence matched) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39511739). The protein is a terpene cyclase (EC 4.2.3.-) involved in aspterric acid biosynthesis, a secondary metabolite. Choice B directly matches the database annotation.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H3](#evidence-h3), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the DDxxD aspartate-rich motif (e.g., 'DGITMDQALTRLTDDTIHACVRILEILKDKDPDMLATIRGF' and 'DVEEWTCQVQGFEVDGPVPKGSEIQAYRTNAFGFSVDTRRPHNMDYVGSSIISMFEWVTGYLKGKSR'), which is the hallmark structural signature of terpene cyclases/synthases. Recognizing this motif leads to the conclusion that the protein catalyzes cyclization of isoprenoid substrates, a reaction central to terpenoid biosynthesis, which is a subclass of secondary metabolite biosynthesis. The distractors (methionine biosynthesis enzymes such as homoserine dehydrogenase or methionine synthase; NAD+ biosynthesis enzymes such as NAD synthetase) belong to entirely different enzyme classes lacking DDxxD motifs and operating on amino acid or nucleotide substrates.


**Missing item-specific fact**

> None strictly required; the DDxxD motif is general biochemical knowledge about terpene cyclase structural biology. However, confidently identifying this specific sequence as a fungal terpene cyclase (as opposed to, say, a prenyltransferase that also uses DDxxD) adds some specificity beyond the motif alone.


**Reason**

> A knowledgeable biochemist can identify the DDxxD motif in the sequence, recognize it as diagnostic of terpene cyclases, and connect terpene cyclases to secondary metabolite (terpenoid) biosynthesis. The distractors involve primary metabolic enzymes (methionine synthase, NAD synthetase) with no structural or functional overlap with terpene cyclases, making them distinguishable through general enzymology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are near-duplicates (both 'L-methionine biosynthesis via de novo pathway', C with an extra period), but both are clearly incorrect and do not compete with B. Option D (NAD+ biosynthesis) is unrelated. Only B is defensible given the terpene cyclase identity.


### Important caveats

- Options A and C are functionally identical, suggesting a formatting error in the benchmark construction; this does not affect the correct answer but indicates poor distractor design.
- The pathway annotation 'Secondary metabolite biosynthesis; terpenoid biosynthesis' is broad. A more specific answer (e.g., 'aspterric acid biosynthesis' or 'sesquiterpene biosynthesis') would be more informative, but B is the correct level of granularity among the choices provided.
- The evidence code ECO:0000269 indicates direct experimental evidence from the cited 2024 paper (Zhou et al., J. Agric. Food Chem.), not merely computational inference.
- The DDxxD motif argument is valid but requires the evaluator to recognize a specific structural signature; a model without terpene-cyclase motif knowledge would struggle to distinguish B from the distractors purely from sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the DDxxD aspartate-rich motif (e.g., 'DGITMDQALTRLTDDTIHACVRILEILKDKDPDMLATIRGF' and 'DVEEWTCQVQGFEVDGPVPKGSEIQAYRTNAFGFSVDTRRPHNMDYVGSSIISMFEWVTGYLKGKSR'), which is the hallmark structural signature of terpene cyclases/synthases. Recognizing this motif leads to the conclusion that the protein catalyzes cyclization of isoprenoid substrates, a reaction central to terpenoid biosynthesis, which is a subclass of secondary metabolite biosynthesis. The distractors (methionine biosynthesis enzymes such as homoserine dehydrogenase or methionine synthase; NAD+ biosynthesis enzymes such as NAD synthetase) belong to entirely different enzyme classes lacking DDxxD motifs and operating on amino acid or nucleotide substrates.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; the DDxxD motif is general biochemical knowledge about terpene cyclase structural biology. However, confidently identifying this specific sequence as a fungal terpene cyclase (as opposed to, say, a prenyltransferase that also uses DDxxD) adds some specificity beyond the motif alone.",
    "reason": "A knowledgeable biochemist can identify the DDxxD motif in the sequence, recognize it as diagnostic of terpene cyclases, and connect terpene cyclases to secondary metabolite (terpenoid) biosynthesis. The distractors involve primary metabolic enzymes (methionine synthase, NAD synthetase) with no structural or functional overlap with terpene cyclases, making them distinguishable through general enzymology knowledge."
  },
  "case_id": "pathway_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H3",
      "H1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWX5 (sequence matched) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39511739). The protein is a terpene cyclase (EC 4.2.3.-) involved in aspterric acid biosynthesis, a secondary metabolite. Choice B directly matches the database annotation."
  },
  "important_caveats": [
    "Options A and C are functionally identical, suggesting a formatting error in the benchmark construction; this does not affect the correct answer but indicates poor distractor design.",
    "The pathway annotation 'Secondary metabolite biosynthesis; terpenoid biosynthesis' is broad. A more specific answer (e.g., 'aspterric acid biosynthesis' or 'sesquiterpene biosynthesis') would be more informative, but B is the correct level of granularity among the choices provided.",
    "The evidence code ECO:0000269 indicates direct experimental evidence from the cited 2024 paper (Zhou et al., J. Agric. Food Chem.), not merely computational inference.",
    "The DDxxD motif argument is valid but requires the evaluator to recognize a specific structural signature; a model without terpene-cyclase motif knowledge would struggle to distinguish B from the distractors purely from sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are near-duplicates (both 'L-methionine biosynthesis via de novo pathway', C with an extra period), but both are clearly incorrect and do not compete with B. Option D (NAD+ biosynthesis) is unrelated. Only B is defensible given the terpene cyclase identity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWX5 (sequence matched) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39511739). The protein is a terpene cyclase (EC 4.2.3.-) involved in aspterric acid biosynthesis, a secondary metabolite. Choice B directly matches the database annotation.",
    "evidence_ids": ["C5", "C4", "H3", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the DDxxD aspartate-rich motif (e.g., 'DGITMDQALTRLTDDTIHACVRILEILKDKDPDMLATIRGF' and 'DVEEWTCQVQGFEVDGPVPKGSEIQAYRTNAFGFSVDTRRPHNMDYVGSSIISMFEWVTGYLKGKSR'), which is the hallmark structural signature of terpene cyclases/synthases. Recognizing this motif leads to the conclusion that the protein catalyzes cyclization of isoprenoid substrates, a reaction central to terpenoid biosynthesis, which is a subclass of secondary metabolite biosynthesis. The distractors (methionine biosynthesis enzymes such as homoserine dehydrogenase or methionine synthase; NAD+ biosynthesis enzymes such as NAD synthetase) belong to entirely different enzyme classes lacking DDxxD motifs and operating on amino acid or nucleotide substrates.",
    "missing_item_specific_fact": "None strictly required; the DDxxD motif is general biochemical knowledge about terpene cyclase structural biology. However, confidently identifying this specific sequence as a fungal terpene cyclase (as opposed to, say, a prenyltransferase that also uses DDxxD) adds some specificity beyond the motif alone.",
    "reason": "A knowledgeable biochemist can identify the DDxxD motif in the sequence, recognize it as diagnostic of terpene cyclases, and connect terpene cyclases to secondary metabolite (terpenoid) biosynthesis. The distractors involve primary metabolic enzymes (methionine synthase, NAD synthetase) with no structural or functional overlap with terpene cyclases, making them distinguishable through general enzymology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are near-duplicates (both 'L-methionine biosynthesis via de novo pathway', C with an extra period), but both are clearly incorrect and do not compete with B. Option D (NAD+ biosynthesis) is unrelated. Only B is defensible given the terpene cyclase identity."
  },
  "important_caveats": [
    "Options A and C are functionally identical, suggesting a formatting error in the benchmark construction; this does not affect the correct answer but indicates poor distractor design.",
    "The pathway annotation 'Secondary metabolite biosynthesis; terpenoid biosynthesis' is broad. A more specific answer (e.g., 'aspterric acid biosynthesis' or 'sesquiterpene biosynthesis') would be more informative, but B is the correct level of granularity among the choices provided.",
    "The evidence code ECO:0000269 indicates direct experimental evidence from the cited 2024 paper (Zhou et al., J. Agric. Food Chem.), not merely computational inference.",
    "The DDxxD motif argument is valid but requires the evaluator to recognize a specific structural signature; a model without terpene-cyclase motif knowledge would struggle to distinguish B from the distractors purely from sequence."
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

**Accession:** `A0A0F7TWX5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39511739","source":"PubMed"}],"value":"4.2.3.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Terpene cyclase pbrA"}}}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39511739","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"citation":{"authors":["Zhou Z.","Zhang Y.","Wu Q.","Hou X.","Zhang B."],"citationCrossReferences":[{"database":"PubMed","id":"39511739"},{"database":"DOI","id":"10.1021/acs.jafc.4c08468"}],"citationType":"journal article","firstPage":"25755","id":"39511739","journal":"J. Agric. Food Chem.","lastPage":"25766","publicationDate":"2024","title":"Yeast synthesis and herbicidal activity evaluation of aspterric acid.","volume":"72"},"referenceNumber":2,"referencePositions":["FUNCTION","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
ID   PBRA_PENBI              Reviewed;         405 AA.
AC   A0A0F7TWX5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   22-JUL-2015, sequence version 1.
DT   28-JAN-2026, entry version 30.
DE   RecName: Full=Terpene cyclase pbrA {ECO:0000303|PubMed:39511739};
DE            EC=4.2.3.- {ECO:0000305|PubMed:39511739};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein A {ECO:0000303|PubMed:39511739};
GN   Name=pbrA {ECO:0000303|PubMed:39511739}; ORFNames=PMG11_09714;
OS   Penicillium brasilianum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.
OX   NCBI_TaxID=104259;
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 22-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
RN   [2]
RP   FUNCTION, PATHWAY, AND BIOTECHNOLOGY.
RX   PubMed=39511739; DOI=10.1021/acs.jafc.4c08468;
RA   Zhou Z., Zhang Y., Wu Q., Hou X., Zhang B.;
RT   "Yeast synthesis and herbicidal activity evaluation of aspterric acid.";
RL   J. Agric. Food Chem. 72:25755-25766(2024).
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 40-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39511739}.
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
