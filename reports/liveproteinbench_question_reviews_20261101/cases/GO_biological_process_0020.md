# GO_biological_process_0020

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — secondary metabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGASTFSQSFAEGYAAWALMLPALVGCALLIYRAFFAIRYPANLPLAGEPDGKRTFSWRTRWRYYIDCEALYKETYDNYTKHGKTVLLPGLGFRHDIVLPQSAMRDIMARPEKELSHADAVLELVQLKYSLGHEKYKADPWPCMLVKSDINSKLEAVCDGMNEELKYAFDKYVGCDTESWKEVDLLETIRMIIMAAASRFTVGFPLCRSEAYLRACWKVNDGIMMNGGLTGATPRLLRPIVGPLVTMKLRQSIEQVKKHVEPIYRQRVQALSQQNSAEKPASDETQDLFQQMLRYAQRERPGELHDLPSMCRRLCFANFAAVHQTTLLVTNMVLNIVSSDPQHNTISVLRDEVKDVIGPDSNAKWTKYKVAQMIKSDSVARETMRLYSNTNRGVFRKVLVEGIKTEDGIELPKGAYVSFLGRPLQCDPETFEDPFEYNPFRFSRIREQAPRDTKGRSSASHLSFVSTSPEHLPFGHGGHSCPGRFLVDFEVKMIVAYLLMNYDVEFPAEYKGQRPANRWMAEALMPPSGARIRIKRRS

[Multiple Choices]
A. response to cold
B. chaperone-mediated protein folding
C. surfactant secretion
D. secondary metabolic process
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as fungal cytochrome P450 AstC in a pathway for biosynthesis of aspterric acid, a secondary metabolite. UniProt cites literature with experimental evidence for its function and pathway; its GO annotation for secondary metabolic process is separately marked IEA, so that GO annotation is computational rather than direct experimental evidence.

Citations as saved: [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a membrane-associated cytochrome P450, which makes a metabolic enzyme more plausible than a chaperone or surfactant-secretion protein. But P450 family identity alone does not establish that this particular enzyme participates in secondary metabolism.


**Missing item-specific fact**

> The protein-specific identification as AstC and its role in aspterric-acid biosynthesis, established by annotation and cited experimental literature, are absent from the supplied input.


**Reason**

> The sequence offers family-level clues, but determining the asked biological process requires the item-specific pathway assignment. Recognizing or retrieving this exact protein's annotation would supply that fact; it is not entailed by the sequence features alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports D for this sequence; it provides no comparable support for A, B, or C. The limitation is that the sequence-only input does not establish the protein-specific pathway.


### Important caveats

- The sequence matches the current and archived UniProt sequence, but the author's exact annotation snapshot is unknown.
- The GO secondary-metabolic-process annotation is IEA; the cited functional and pathway annotations carry experimental-evidence codes, but the primary papers were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a membrane-associated cytochrome P450, which makes a metabolic enzyme more plausible than a chaperone or surfactant-secretion protein. But P450 family identity alone does not establish that this particular enzyme participates in secondary metabolism.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as AstC and its role in aspterric-acid biosynthesis, established by annotation and cited experimental literature, are absent from the supplied input.",
    "reason": "The sequence offers family-level clues, but determining the asked biological process requires the item-specific pathway assignment. Recognizing or retrieving this exact protein's annotation would supply that fact; it is not entailed by the sequence features alone."
  },
  "case_id": "GO_biological_process_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H5",
      "H6",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as fungal cytochrome P450 AstC in a pathway for biosynthesis of aspterric acid, a secondary metabolite. UniProt cites literature with experimental evidence for its function and pathway; its GO annotation for secondary metabolic process is separately marked IEA, so that GO annotation is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The sequence matches the current and archived UniProt sequence, but the author's exact annotation snapshot is unknown.",
    "The GO secondary-metabolic-process annotation is IEA; the cited functional and pathway annotations carry experimental-evidence codes, but the primary papers were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D for this sequence; it provides no comparable support for A, B, or C. The limitation is that the sequence-only input does not establish the protein-specific pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as fungal cytochrome P450 AstC in a pathway for biosynthesis of aspterric acid, a secondary metabolite. UniProt cites literature with experimental evidence for its function and pathway; its GO annotation for secondary metabolic process is separately marked IEA, so that GO annotation is computational rather than direct experimental evidence.",
    "evidence_ids": ["H4", "H5", "H6", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a membrane-associated cytochrome P450, which makes a metabolic enzyme more plausible than a chaperone or surfactant-secretion protein. But P450 family identity alone does not establish that this particular enzyme participates in secondary metabolism.",
    "missing_item_specific_fact": "The protein-specific identification as AstC and its role in aspterric-acid biosynthesis, established by annotation and cited experimental literature, are absent from the supplied input.",
    "reason": "The sequence offers family-level clues, but determining the asked biological process requires the item-specific pathway assignment. Recognizing or retrieving this exact protein's annotation would supply that fact; it is not entailed by the sequence features alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D for this sequence; it provides no comparable support for A, B, or C. The limitation is that the sequence-only input does not establish the protein-specific pathway."
  },
  "important_caveats": [
    "The sequence matches the current and archived UniProt sequence, but the author's exact annotation snapshot is unknown.",
    "The GO secondary-metabolic-process annotation is IEA; the cited functional and pathway annotations carry experimental-evidence codes, but the primary papers were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q0CPG6, AstC) is a cytochrome P450 monooxygenase experimentally characterized (ECO:0000269, PubMed:29995859 and 39511739) as part of the aspterric acid (sesquiterpenoid) biosynthesis gene cluster. UniProt explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (C6/H5), and the GO term GO:0019748 'secondary metabolic process' is assigned (C7/H6). The underlying experimental evidence confirms the protein catalyzes a step in secondary metabolite production, directly supporting choice D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [C9](#evidence-c9), [C10](#evidence-c10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable cytochrome P450 heme-binding motif (FGHGGHSCPGRF region with the axial-ligand cysteine), identifying the protein as a P450 monooxygenase—an oxidative enzyme catalyzing metabolic transformations. Among the four choices, A (response to cold), B (chaperone-mediated protein folding), and C (surfactant secretion) describe processes fundamentally incompatible with a P450 enzyme's catalytic function. Only D (secondary metabolic process) describes an enzymatic metabolic role consistent with a P450. Thus, identifying the protein class from the heme-binding signature and applying general knowledge that P450s are oxidative metabolic enzymes eliminates A, B, and C, leaving D.


**Missing item-specific fact**

> The specific assignment to 'secondary' (rather than primary) metabolism requires knowing the substrate is a sesquiterpenoid (aspterric acid), which is not determinable from sequence alone. However, since D is the only metabolic option among the choices, this distinction does not affect answer selection.


**Reason**

> A model can identify the P450 heme-binding motif in the sequence, recognize the protein as an oxidative enzyme, and eliminate the three non-enzymatic/non-metabolic distractors (cold response, chaperone, surfactant secretion) using general biological knowledge. The remaining option D is the only one describing an enzymatic metabolic process. The specific 'secondary' qualifier is not independently derivable but is irrelevant when the other three choices are categorically incompatible with a P450.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C describe processes (cold sensing, protein folding assistance, surfactant release) that are mechanistically incompatible with a cytochrome P450 monooxygenase. Only D describes a metabolic enzymatic role. No other option is defensible for a P450 enzyme.


### Important caveats

- The GO:0019748 annotation carries evidence code IEA:UniProtKB-ARBA (computational transfer), though the underlying pathway assignment is experimentally supported (ECO:0000269).
- The specific 'secondary' vs. 'primary' metabolic distinction cannot be determined from sequence alone; the answer is selected by elimination of clearly incompatible options rather than positive identification of the sesquiterpenoid pathway.
- The reviewer identified the accession Q0CPG6 from dataset metadata; this accession was not provided to the evaluated model.
- The P450 heme-binding motif (FGHGGHSCPGRF) is identifiable in the sequence, enabling protein-class recognition without database lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif (FGHGGHSCPGRF region with the axial-ligand cysteine), identifying the protein as a P450 monooxygenase—an oxidative enzyme catalyzing metabolic transformations. Among the four choices, A (response to cold), B (chaperone-mediated protein folding), and C (surfactant secretion) describe processes fundamentally incompatible with a P450 enzyme's catalytic function. Only D (secondary metabolic process) describes an enzymatic metabolic role consistent with a P450. Thus, identifying the protein class from the heme-binding signature and applying general knowledge that P450s are oxidative metabolic enzymes eliminates A, B, and C, leaving D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific assignment to 'secondary' (rather than primary) metabolism requires knowing the substrate is a sesquiterpenoid (aspterric acid), which is not determinable from sequence alone. However, since D is the only metabolic option among the choices, this distinction does not affect answer selection.",
    "reason": "A model can identify the P450 heme-binding motif in the sequence, recognize the protein as an oxidative enzyme, and eliminate the three non-enzymatic/non-metabolic distractors (cold response, chaperone, surfactant secretion) using general biological knowledge. The remaining option D is the only one describing an enzymatic metabolic process. The specific 'secondary' qualifier is not independently derivable but is irrelevant when the other three choices are categorically incompatible with a P450."
  },
  "case_id": "GO_biological_process_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6",
      "C9",
      "C10"
    ],
    "judgment": "supported",
    "reason": "The protein (Q0CPG6, AstC) is a cytochrome P450 monooxygenase experimentally characterized (ECO:0000269, PubMed:29995859 and 39511739) as part of the aspterric acid (sesquiterpenoid) biosynthesis gene cluster. UniProt explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (C6/H5), and the GO term GO:0019748 'secondary metabolic process' is assigned (C7/H6). The underlying experimental evidence confirms the protein catalyzes a step in secondary metabolite production, directly supporting choice D."
  },
  "important_caveats": [
    "The GO:0019748 annotation carries evidence code IEA:UniProtKB-ARBA (computational transfer), though the underlying pathway assignment is experimentally supported (ECO:0000269).",
    "The specific 'secondary' vs. 'primary' metabolic distinction cannot be determined from sequence alone; the answer is selected by elimination of clearly incompatible options rather than positive identification of the sesquiterpenoid pathway.",
    "The reviewer identified the accession Q0CPG6 from dataset metadata; this accession was not provided to the evaluated model.",
    "The P450 heme-binding motif (FGHGGHSCPGRF) is identifiable in the sequence, enabling protein-class recognition without database lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe processes (cold sensing, protein folding assistance, surfactant release) that are mechanistically incompatible with a cytochrome P450 monooxygenase. Only D describes a metabolic enzymatic role. No other option is defensible for a P450 enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q0CPG6, AstC) is a cytochrome P450 monooxygenase experimentally characterized (ECO:0000269, PubMed:29995859 and 39511739) as part of the aspterric acid (sesquiterpenoid) biosynthesis gene cluster. UniProt explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (C6/H5), and the GO term GO:0019748 'secondary metabolic process' is assigned (C7/H6). The underlying experimental evidence confirms the protein catalyzes a step in secondary metabolite production, directly supporting choice D.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "H6", "C9", "C10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif (FGHGGHSCPGRF region with the axial-ligand cysteine), identifying the protein as a P450 monooxygenase—an oxidative enzyme catalyzing metabolic transformations. Among the four choices, A (response to cold), B (chaperone-mediated protein folding), and C (surfactant secretion) describe processes fundamentally incompatible with a P450 enzyme's catalytic function. Only D (secondary metabolic process) describes an enzymatic metabolic role consistent with a P450. Thus, identifying the protein class from the heme-binding signature and applying general knowledge that P450s are oxidative metabolic enzymes eliminates A, B, and C, leaving D.",
    "missing_item_specific_fact": "The specific assignment to 'secondary' (rather than primary) metabolism requires knowing the substrate is a sesquiterpenoid (aspterric acid), which is not determinable from sequence alone. However, since D is the only metabolic option among the choices, this distinction does not affect answer selection.",
    "reason": "A model can identify the P450 heme-binding motif in the sequence, recognize the protein as an oxidative enzyme, and eliminate the three non-enzymatic/non-metabolic distractors (cold response, chaperone, surfactant secretion) using general biological knowledge. The remaining option D is the only one describing an enzymatic metabolic process. The specific 'secondary' qualifier is not independently derivable but is irrelevant when the other three choices are categorically incompatible with a P450."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C describe processes (cold sensing, protein folding assistance, surfactant release) that are mechanistically incompatible with a cytochrome P450 monooxygenase. Only D describes a metabolic enzymatic role. No other option is defensible for a P450 enzyme."
  },
  "important_caveats": [
    "The GO:0019748 annotation carries evidence code IEA:UniProtKB-ARBA (computational transfer), though the underlying pathway assignment is experimentally supported (ECO:0000269).",
    "The specific 'secondary' vs. 'primary' metabolic distinction cannot be determined from sequence alone; the answer is selected by elimination of clearly incompatible options rather than positive identification of the sesquiterpenoid pathway.",
    "The reviewer identified the accession Q0CPG6 from dataset metadata; this accession was not provided to the evaluated model.",
    "The P450 heme-binding motif (FGHGGHSCPGRF) is identifiable in the sequence, enabling protein-class recognition without database lookup."
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

**Accession:** `Q0CPG6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 96. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39511739","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase; part of the gene cluster that mediates the biosynthesis of the sesquiterpenoid aspterric acid (AA), an inhibitor of dihydroxy-acid dehydratase (DHAD) effective as an herbicide (PubMed:29995859, PubMed:39511739). AstC catalyzes the third and last step within the pathway and converts the alpha-epoxy carboxylate intermediate produced by the cytochrome P450 monooxygenase astC from (-)daucane into the tricyclic aspterric acid (PubMed:29995859)"}]}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39511739","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"database":"GO","id":"GO:0019748","properties":[{"key":"GoTerm","value":"P:secondary metabolic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-ARBA"}]}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"citation":{"authors":["Yan Y.","Liu Q.","Zang X.","Yuan S.","Bat-Erdene U.","Nguyen C.","Gan J.","Zhou J.","Jacobsen S.E.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"29995859"},{"database":"DOI","id":"10.1038/s41586-018-0319-4"}],"citationType":"journal article","firstPage":"415","id":"29995859","journal":"Nature","lastPage":"418","publicationDate":"2018","title":"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.","volume":"559"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"citation":{"authors":["Zhou Z.","Zhang Y.","Wu Q.","Hou X.","Zhang B."],"citationCrossReferences":[{"database":"PubMed","id":"39511739"},{"database":"DOI","id":"10.1021/acs.jafc.4c08468"}],"citationType":"journal article","firstPage":"25755","id":"39511739","journal":"J. Agric. Food Chem.","lastPage":"25766","publicationDate":"2024","title":"Yeast synthesis and herbicidal activity evaluation of aspterric acid.","volume":"72"},"referenceNumber":3,"referencePositions":["FUNCTION","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)  
**Locator:** `lines 41-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:30:24.324806+00:00.  

```text
CC   -!- FUNCTION: Cytochrome P450 monooxygenase; part of the gene cluster that
CC       mediates the biosynthesis of the sesquiterpenoid aspterric acid (AA),
CC       an inhibitor of dihydroxy-acid dehydratase (DHAD) effective as an
CC       herbicide (PubMed:29995859, PubMed:39511739). AstC catalyzes the third
CC       and last step within the pathway and converts the alpha-epoxy
CC       carboxylate intermediate produced by the cytochrome P450 monooxygenase
CC       astC from (-)daucane into the tricyclic aspterric acid
CC       (PubMed:29995859). {ECO:0000269|PubMed:29995859,
CC       ECO:0000269|PubMed:39511739}.
```

Source SHA-256: `482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)  
**Locator:** `lines 63-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:30:24.324806+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:29995859, ECO:0000269|PubMed:39511739}.
```

Source SHA-256: `482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG6?format=txt&versions=96)  
**Locator:** `lines 95-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:30:24.324806+00:00.  

```text
DR   GO; GO:0019748; P:secondary metabolic process; IEA:UniProtKB-ARBA.
```

Source SHA-256: `482e2797ef6a132bf6ecea28c3af021dd91a0c76f43ab91eddc89822a20eafbd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
