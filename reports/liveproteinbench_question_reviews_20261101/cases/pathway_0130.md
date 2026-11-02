# pathway_0130

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. ubiquinone biosynthesis. .
B. peptidoglycan degradation. .
C. Amino-acid biosynthesis
D. L-valine biosynthesis
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

> The sequence-matched UniProt record identifies the protein as dihydroxy-acid dehydratase and annotates it in amino-acid biosynthesis, including both isoleucine and valine biosynthesis. This supports the keyed broad category C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If the protein is identified as dihydroxy-acid dehydratase, its role in branched-chain amino-acid biosynthesis is biologically coherent; however, that protein-specific identification is not supplied in the question.


**Missing item-specific fact**

> The protein's identity and pathway annotation, including its roles in both isoleucine and valine biosynthesis.


**Reason**

> The sequence and choices alone do not provide a clear basis to identify this particular enzyme or distinguish the broad amino-acid biosynthesis choice from the more specific valine pathway choice. Doing so depends on protein-specific information absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The matched record annotates the enzyme in both broad amino-acid biosynthesis and L-valine biosynthesis. C is supported as the umbrella category, while D is also a documented pathway for this protein; the question does not define how to choose between broad and specific pathway labels.


### Important caveats

- The sequence match and pathway annotations are reviewer-only evidence, not information supplied to the evaluated model.
- The cited annotation evidence is linked to a publication, but the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If the protein is identified as dihydroxy-acid dehydratase, its role in branched-chain amino-acid biosynthesis is biologically coherent; however, that protein-specific identification is not supplied in the question.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and pathway annotation, including its roles in both isoleucine and valine biosynthesis.",
    "reason": "The sequence and choices alone do not provide a clear basis to identify this particular enzyme or distinguish the broad amino-acid biosynthesis choice from the more specific valine pathway choice. Doing so depends on protein-specific information absent from the input."
  },
  "case_id": "pathway_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as dihydroxy-acid dehydratase and annotates it in amino-acid biosynthesis, including both isoleucine and valine biosynthesis. This supports the keyed broad category C."
  },
  "important_caveats": [
    "The sequence match and pathway annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The cited annotation evidence is linked to a publication, but the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The matched record annotates the enzyme in both broad amino-acid biosynthesis and L-valine biosynthesis. C is supported as the umbrella category, while D is also a documented pathway for this protein; the question does not define how to choose between broad and specific pathway labels."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as dihydroxy-acid dehydratase and annotates it in amino-acid biosynthesis, including both isoleucine and valine biosynthesis. This supports the keyed broad category C.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If the protein is identified as dihydroxy-acid dehydratase, its role in branched-chain amino-acid biosynthesis is biologically coherent; however, that protein-specific identification is not supplied in the question.",
    "missing_item_specific_fact": "The protein's identity and pathway annotation, including its roles in both isoleucine and valine biosynthesis.",
    "reason": "The sequence and choices alone do not provide a clear basis to identify this particular enzyme or distinguish the broad amino-acid biosynthesis choice from the more specific valine pathway choice. Doing so depends on protein-specific information absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The matched record annotates the enzyme in both broad amino-acid biosynthesis and L-valine biosynthesis. C is supported as the umbrella category, while D is also a documented pathway for this protein; the question does not define how to choose between broad and specific pathway labels."
  },
  "important_caveats": [
    "The sequence match and pathway annotations are reviewer-only evidence, not information supplied to the evaluated model.",
    "The cited annotation evidence is linked to a publication, but the primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q0CPG9, ASTD_ASPTN) annotates this protein (Dihydroxy-acid dehydratase astD, EC 4.2.1.9) under two pathway comments: 'Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4' and 'Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4'. Both share the umbrella term 'Amino-acid biosynthesis', making choice C a supported and arguably more complete answer than the narrower D, since the protein participates in two distinct branched-chain amino acid biosynthesis routes. The annotation is backed by experimental evidence (ECO:0000269, PubMed:29995859, Nature 2018).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could partially reason: (1) eliminate B (peptidoglycan degradation) because the sequence composition and context suggest a eukaryotic/fungal protein, and peptidoglycan is a bacterial cell-wall polymer; (2) if one recognized conserved &#91;2Fe-2S&#93; cluster-binding cysteine motifs characteristic of the DHAD family, one could infer branched-chain amino acid biosynthesis. However, identifying this specific 598-aa fungal sequence as DHAD from sequence features alone is extremely difficult without database comparison, and the critical C-vs-D distinction requires knowing that this particular protein is annotated in BOTH isoleucine and valine biosynthesis (making the broader 'Amino-acid biosynthesis' the more appropriate 'primary' label).


**Missing item-specific fact**

> The specific annotation that this protein (astD) participates in both L-isoleucine AND L-valine biosynthesis pathways, which is what makes the broader category (C) preferable to the narrower sub-pathway (D). Additionally, recognizing the sequence as DHAD requires either motif-level expertise or a database hit.


**Reason**

> While one can eliminate B by general biological reasoning (eukaryote vs peptidoglycan), distinguishing among A, C, and D requires identifying the protein as a DHAD-family enzyme and knowing its dual pathway annotation. This identification is not achievable through general biological reasoning from the raw sequence alone; it depends on protein-specific database annotation or memorized knowledge of this particular enzyme's function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The UniProt entry explicitly annotates this protein in BOTH 'Amino-acid biosynthesis; L-valine biosynthesis' and 'Amino-acid biosynthesis; L-isoleucine biosynthesis'. Choice D (L-valine biosynthesis) is a directly annotated sub-pathway and is therefore also defensible. The author's preference for C (the broader umbrella) over D is reasonable because the protein spans two amino acid biosynthesis routes, but the question wording ('primary metabolic or signaling pathway') does not clearly mandate the broadest category. A model selecting D could argue it is naming a specific annotated pathway for this protein.


### Important caveats

- The protein is specifically astD, part of the aspterric acid biosynthesis gene cluster in Aspergillus terreus (PubMed:29995859, Nature 2018). Its DHAD activity is in the context of a natural-product herbicide biosynthetic cluster, not merely housekeeping amino acid biosynthesis. The pathway annotation reflects its enzymatic step within branched-chain amino acid metabolism.
- The C-vs-D ambiguity is structurally inherent: the UniProt entry lists both pathways with equal evidence codes (ECO:0000269). Neither is annotated as 'primary' over the other.
- The sequence-match is confirmed (SHA-256 match between benchmark sequence and UniProt Q0CPG9), so the annotation applies directly to the supplied sequence.
- The identity of the protein (accession Q0CPG9) was inferred by the reviewer from dataset metadata, not from the model input. The evaluated model sees only the raw sequence and the four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could partially reason: (1) eliminate B (peptidoglycan degradation) because the sequence composition and context suggest a eukaryotic/fungal protein, and peptidoglycan is a bacterial cell-wall polymer; (2) if one recognized conserved [2Fe-2S] cluster-binding cysteine motifs characteristic of the DHAD family, one could infer branched-chain amino acid biosynthesis. However, identifying this specific 598-aa fungal sequence as DHAD from sequence features alone is extremely difficult without database comparison, and the critical C-vs-D distinction requires knowing that this particular protein is annotated in BOTH isoleucine and valine biosynthesis (making the broader 'Amino-acid biosynthesis' the more appropriate 'primary' label).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation that this protein (astD) participates in both L-isoleucine AND L-valine biosynthesis pathways, which is what makes the broader category (C) preferable to the narrower sub-pathway (D). Additionally, recognizing the sequence as DHAD requires either motif-level expertise or a database hit.",
    "reason": "While one can eliminate B by general biological reasoning (eukaryote vs peptidoglycan), distinguishing among A, C, and D requires identifying the protein as a DHAD-family enzyme and knowing its dual pathway annotation. This identification is not achievable through general biological reasoning from the raw sequence alone; it depends on protein-specific database annotation or memorized knowledge of this particular enzyme's function."
  },
  "case_id": "pathway_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q0CPG9, ASTD_ASPTN) annotates this protein (Dihydroxy-acid dehydratase astD, EC 4.2.1.9) under two pathway comments: 'Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4' and 'Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4'. Both share the umbrella term 'Amino-acid biosynthesis', making choice C a supported and arguably more complete answer than the narrower D, since the protein participates in two distinct branched-chain amino acid biosynthesis routes. The annotation is backed by experimental evidence (ECO:0000269, PubMed:29995859, Nature 2018)."
  },
  "important_caveats": [
    "The protein is specifically astD, part of the aspterric acid biosynthesis gene cluster in Aspergillus terreus (PubMed:29995859, Nature 2018). Its DHAD activity is in the context of a natural-product herbicide biosynthetic cluster, not merely housekeeping amino acid biosynthesis. The pathway annotation reflects its enzymatic step within branched-chain amino acid metabolism.",
    "The C-vs-D ambiguity is structurally inherent: the UniProt entry lists both pathways with equal evidence codes (ECO:0000269). Neither is annotated as 'primary' over the other.",
    "The sequence-match is confirmed (SHA-256 match between benchmark sequence and UniProt Q0CPG9), so the annotation applies directly to the supplied sequence.",
    "The identity of the protein (accession Q0CPG9) was inferred by the reviewer from dataset metadata, not from the model input. The evaluated model sees only the raw sequence and the four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The UniProt entry explicitly annotates this protein in BOTH 'Amino-acid biosynthesis; L-valine biosynthesis' and 'Amino-acid biosynthesis; L-isoleucine biosynthesis'. Choice D (L-valine biosynthesis) is a directly annotated sub-pathway and is therefore also defensible. The author's preference for C (the broader umbrella) over D is reasonable because the protein spans two amino acid biosynthesis routes, but the question wording ('primary metabolic or signaling pathway') does not clearly mandate the broadest category. A model selecting D could argue it is naming a specific annotated pathway for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q0CPG9, ASTD_ASPTN) annotates this protein (Dihydroxy-acid dehydratase astD, EC 4.2.1.9) under two pathway comments: 'Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4' and 'Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4'. Both share the umbrella term 'Amino-acid biosynthesis', making choice C a supported and arguably more complete answer than the narrower D, since the protein participates in two distinct branched-chain amino acid biosynthesis routes. The annotation is backed by experimental evidence (ECO:0000269, PubMed:29995859, Nature 2018).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could partially reason: (1) eliminate B (peptidoglycan degradation) because the sequence composition and context suggest a eukaryotic/fungal protein, and peptidoglycan is a bacterial cell-wall polymer; (2) if one recognized conserved [2Fe-2S] cluster-binding cysteine motifs characteristic of the DHAD family, one could infer branched-chain amino acid biosynthesis. However, identifying this specific 598-aa fungal sequence as DHAD from sequence features alone is extremely difficult without database comparison, and the critical C-vs-D distinction requires knowing that this particular protein is annotated in BOTH isoleucine and valine biosynthesis (making the broader 'Amino-acid biosynthesis' the more appropriate 'primary' label).",
    "missing_item_specific_fact": "The specific annotation that this protein (astD) participates in both L-isoleucine AND L-valine biosynthesis pathways, which is what makes the broader category (C) preferable to the narrower sub-pathway (D). Additionally, recognizing the sequence as DHAD requires either motif-level expertise or a database hit.",
    "reason": "While one can eliminate B by general biological reasoning (eukaryote vs peptidoglycan), distinguishing among A, C, and D requires identifying the protein as a DHAD-family enzyme and knowing its dual pathway annotation. This identification is not achievable through general biological reasoning from the raw sequence alone; it depends on protein-specific database annotation or memorized knowledge of this particular enzyme's function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The UniProt entry explicitly annotates this protein in BOTH 'Amino-acid biosynthesis; L-valine biosynthesis' and 'Amino-acid biosynthesis; L-isoleucine biosynthesis'. Choice D (L-valine biosynthesis) is a directly annotated sub-pathway and is therefore also defensible. The author's preference for C (the broader umbrella) over D is reasonable because the protein spans two amino acid biosynthesis routes, but the question wording ('primary metabolic or signaling pathway') does not clearly mandate the broadest category. A model selecting D could argue it is naming a specific annotated pathway for this protein."
  },
  "important_caveats": [
    "The protein is specifically astD, part of the aspterric acid biosynthesis gene cluster in Aspergillus terreus (PubMed:29995859, Nature 2018). Its DHAD activity is in the context of a natural-product herbicide biosynthetic cluster, not merely housekeeping amino acid biosynthesis. The pathway annotation reflects its enzymatic step within branched-chain amino acid metabolism.",
    "The C-vs-D ambiguity is structurally inherent: the UniProt entry lists both pathways with equal evidence codes (ECO:0000269). Neither is annotated as 'primary' over the other.",
    "The sequence-match is confirmed (SHA-256 match between benchmark sequence and UniProt Q0CPG9), so the annotation applies directly to the supplied sequence.",
    "The identity of the protein (accession Q0CPG9) was inferred by the reviewer from dataset metadata, not from the model input. The evaluated model sees only the raw sequence and the four choices."
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

**Accession:** `Q0CPG9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 90. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein D"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"4.2.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Dihydroxy-acid dehydratase astD, mitochondrial"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"DHAD astD"}]}}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/comments/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4"}]}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/comments/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4"}]}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:26.147110+00:00.  

```json
{"citation":{"authors":["Yan Y.","Liu Q.","Zang X.","Yuan S.","Bat-Erdene U.","Nguyen C.","Gan J.","Zhou J.","Jacobsen S.E.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"29995859"},{"database":"DOI","id":"10.1038/s41586-018-0319-4"}],"citationType":"journal article","firstPage":"415","id":"29995859","journal":"Nature","lastPage":"418","publicationDate":"2018","title":"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.","volume":"559"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","DOMAIN","ACTIVITY REGULATION","PATHWAY"]}
```

Source SHA-256: `0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 77-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-isoleucine biosynthesis; L-
CC       isoleucine from 2-oxobutanoate: step 3/4.
CC       {ECO:0000269|PubMed:29995859}.
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)  
**Locator:** `lines 80-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 90 / 1.  
**Retrieved:** 2026-11-02T04:30:28.917378+00:00.  

```text
CC   -!- PATHWAY: Amino-acid biosynthesis; L-valine biosynthesis; L-valine from
CC       pyruvate: step 3/4. {ECO:0000269|PubMed:29995859}.
```

Source SHA-256: `9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
