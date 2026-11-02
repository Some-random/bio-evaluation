# pathway_0100

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGASTFSQSFAEGYAAWALMLPALVGCALLIYRAFFAIRYPANLPLAGEPDGKRTFSWRTRWRYYIDCEALYKETYDNYTKHGKTVLLPGLGFRHDIVLPQSAMRDIMARPEKELSHADAVLELVQLKYSLGHEKYKADPWPCMLVKSDINSKLEAVCDGMNEELKYAFDKYVGCDTESWKEVDLLETIRMIIMAAASRFTVGFPLCRSEAYLRACWKVNDGIMMNGGLTGATPRLLRPIVGPLVTMKLRQSIEQVKKHVEPIYRQRVQALSQQNSAEKPASDETQDLFQQMLRYAQRERPGELHDLPSMCRRLCFANFAAVHQTTLLVTNMVLNIVSSDPQHNTISVLRDEVKDVIGPDSNAKWTKYKVAQMIKSDSVARETMRLYSNTNRGVFRKVLVEGIKTEDGIELPKGAYVSFLGRPLQCDPETFEDPFEYNPFRFSRIREQAPRDTKGRSSASHLSFVSTSPEHLPFGHGGHSCPGRFLVDFEVKMIVAYLLMNYDVEFPAEYKGQRPANRWMAEALMPPSGARIRIKRRS

[Multiple Choices]
A. Secondary metabolite biosynthesis
B. IMP biosynthesis via de novo pathway
C. (S)-3-hydroxy-3-methylglutaryl-CoA from 3-isovaleryl-CoA: step 3/3. .
D. peptidoglycan degradation. .
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

> The exact 538-aa sequence matches the UniProt entry for Aspergillus terreus cytochrome P450 monooxygenase AstC, annotated to secondary-metabolite and terpenoid biosynthesis. The pathway annotation carries experimental evidence codes, though it is database evidence rather than an independently reviewed assessment here.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the N-terminal hydrophobic region and conserved heme-thiolate P450 features expected of a fungal cytochrome P450 monooxygenase. Among these choices, secondary-metabolite biosynthesis is a defensible broad pathway fit; the alternatives describe unrelated purine, isovalerate-derived, or peptidoglycan processes.


**Missing item-specific fact**

> The exact AstC identity and its experimentally characterized role in aspterric-acid biosynthesis are not supplied; those facts would be needed to establish the specific pathway independently of the broad sequence-based inference.


**Reason**

> The sequence and answer choices offer a meaningful biological basis for preferring the broad secondary-metabolism category, even though they do not establish AstC's specific pathway role without protein-specific information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are sufficiently distinct that the fungal P450 sequence supports A over the unrelated pathway options.


### Important caveats

- Reviewer-only database annotations support the key but were not available to the evaluated model.
- The matched sequence and historical UniProt entry support annotation applicability; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the N-terminal hydrophobic region and conserved heme-thiolate P450 features expected of a fungal cytochrome P450 monooxygenase. Among these choices, secondary-metabolite biosynthesis is a defensible broad pathway fit; the alternatives describe unrelated purine, isovalerate-derived, or peptidoglycan processes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact AstC identity and its experimentally characterized role in aspterric-acid biosynthesis are not supplied; those facts would be needed to establish the specific pathway independently of the broad sequence-based inference.",
    "reason": "The sequence and answer choices offer a meaningful biological basis for preferring the broad secondary-metabolism category, even though they do not establish AstC's specific pathway role without protein-specific information."
  },
  "case_id": "pathway_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 538-aa sequence matches the UniProt entry for Aspergillus terreus cytochrome P450 monooxygenase AstC, annotated to secondary-metabolite and terpenoid biosynthesis. The pathway annotation carries experimental evidence codes, though it is database evidence rather than an independently reviewed assessment here."
  },
  "important_caveats": [
    "Reviewer-only database annotations support the key but were not available to the evaluated model.",
    "The matched sequence and historical UniProt entry support annotation applicability; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are sufficiently distinct that the fungal P450 sequence supports A over the unrelated pathway options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 538-aa sequence matches the UniProt entry for Aspergillus terreus cytochrome P450 monooxygenase AstC, annotated to secondary-metabolite and terpenoid biosynthesis. The pathway annotation carries experimental evidence codes, though it is database evidence rather than an independently reviewed assessment here.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the N-terminal hydrophobic region and conserved heme-thiolate P450 features expected of a fungal cytochrome P450 monooxygenase. Among these choices, secondary-metabolite biosynthesis is a defensible broad pathway fit; the alternatives describe unrelated purine, isovalerate-derived, or peptidoglycan processes.",
    "missing_item_specific_fact": "The exact AstC identity and its experimentally characterized role in aspterric-acid biosynthesis are not supplied; those facts would be needed to establish the specific pathway independently of the broad sequence-based inference.",
    "reason": "The sequence and answer choices offer a meaningful biological basis for preferring the broad secondary-metabolism category, even though they do not establish AstC's specific pathway role without protein-specific information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are sufficiently distinct that the fungal P450 sequence supports A over the unrelated pathway options."
  },
  "important_caveats": [
    "Reviewer-only database annotations support the key but were not available to the evaluated model.",
    "The matched sequence and historical UniProt entry support annotation applicability; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q0CPG6 (ASTC_ASPTN) for this exact sequence (538 aa, matched) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with ECO:0000269 (experimental evidence) supported by two publications (PubMed:29995859, PubMed:39511739). The protein is a cytochrome P450 monooxygenase astC involved in aspterric acid biosynthesis in Aspergillus terreus, which falls squarely under secondary metabolite biosynthesis.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains the canonical P450 heme-binding motif FGHGGHSCPGRF (FxxGxxxCxG), identifying the protein as a cytochrome P450 monooxygenase. This immediately eliminates B (IMP/purine biosynthesis does not employ P450 enzymes) and D (peptidoglycan degradation is a bacterial process absent in fungi). Option C describes a specific step in leucine biosynthesis (3-methylcrotonyl-CoA → HMG-CoA) that is catalyzed by carboxylase/ligase enzymes, not P450s. The remaining option A is consistent with the well-established biological principle that fungal P450s are disproportionately dedicated to secondary metabolite (terpenoid, polyketide, etc.) biosynthesis rather than primary metabolism.


**Missing item-specific fact**

> The specific identity of aspterric acid and its terpenoid classification requires knowledge of this particular biosynthetic cluster, but the question only asks for the broad pathway category, which is inferable from P450 identification plus fungal context.


**Reason**

> The sequence provides a recognizable P450 heme-binding motif, enabling elimination of three options through general pathway biochemistry. The positive identification of 'secondary metabolite biosynthesis' follows from the well-known dominance of P450 involvement in fungal secondary metabolism, a general biological principle rather than a protein-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly incompatible with a fungal cytochrome P450: B involves purine biosynthesis (no P450), C is a leucine biosynthesis step (no P450), and D is a bacterial cell-wall process. Only A is consistent with a fungal P450.


### Important caveats

- The P450 heme-binding motif identification relies on recognizing FGHGGHSCPGRF in the C-terminal region; a model unfamiliar with P450 motifs might not extract this signal.
- The 'fungal P450s → secondary metabolism' heuristic is a strong general principle but not an absolute rule; some fungal P450s participate in primary metabolism (e.g., ergosterol synthesis). However, none of the other options correspond to primary metabolic P450 pathways.
- The UniProt annotation is backed by experimental evidence (ECO:0000269) from a 2018 Nature paper and a 2024 J. Agric. Food Chem. paper, lending strong support to the pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains the canonical P450 heme-binding motif FGHGGHSCPGRF (FxxGxxxCxG), identifying the protein as a cytochrome P450 monooxygenase. This immediately eliminates B (IMP/purine biosynthesis does not employ P450 enzymes) and D (peptidoglycan degradation is a bacterial process absent in fungi). Option C describes a specific step in leucine biosynthesis (3-methylcrotonyl-CoA → HMG-CoA) that is catalyzed by carboxylase/ligase enzymes, not P450s. The remaining option A is consistent with the well-established biological principle that fungal P450s are disproportionately dedicated to secondary metabolite (terpenoid, polyketide, etc.) biosynthesis rather than primary metabolism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identity of aspterric acid and its terpenoid classification requires knowledge of this particular biosynthetic cluster, but the question only asks for the broad pathway category, which is inferable from P450 identification plus fungal context.",
    "reason": "The sequence provides a recognizable P450 heme-binding motif, enabling elimination of three options through general pathway biochemistry. The positive identification of 'secondary metabolite biosynthesis' follows from the well-known dominance of P450 involvement in fungal secondary metabolism, a general biological principle rather than a protein-specific lookup."
  },
  "case_id": "pathway_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG6 (ASTC_ASPTN) for this exact sequence (538 aa, matched) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with ECO:0000269 (experimental evidence) supported by two publications (PubMed:29995859, PubMed:39511739). The protein is a cytochrome P450 monooxygenase astC involved in aspterric acid biosynthesis in Aspergillus terreus, which falls squarely under secondary metabolite biosynthesis."
  },
  "important_caveats": [
    "The P450 heme-binding motif identification relies on recognizing FGHGGHSCPGRF in the C-terminal region; a model unfamiliar with P450 motifs might not extract this signal.",
    "The 'fungal P450s → secondary metabolism' heuristic is a strong general principle but not an absolute rule; some fungal P450s participate in primary metabolism (e.g., ergosterol synthesis). However, none of the other options correspond to primary metabolic P450 pathways.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from a 2018 Nature paper and a 2024 J. Agric. Food Chem. paper, lending strong support to the pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a fungal cytochrome P450: B involves purine biosynthesis (no P450), C is a leucine biosynthesis step (no P450), and D is a bacterial cell-wall process. Only A is consistent with a fungal P450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG6 (ASTC_ASPTN) for this exact sequence (538 aa, matched) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with ECO:0000269 (experimental evidence) supported by two publications (PubMed:29995859, PubMed:39511739). The protein is a cytochrome P450 monooxygenase astC involved in aspterric acid biosynthesis in Aspergillus terreus, which falls squarely under secondary metabolite biosynthesis.",
    "evidence_ids": ["C5", "H4", "C4", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains the canonical P450 heme-binding motif FGHGGHSCPGRF (FxxGxxxCxG), identifying the protein as a cytochrome P450 monooxygenase. This immediately eliminates B (IMP/purine biosynthesis does not employ P450 enzymes) and D (peptidoglycan degradation is a bacterial process absent in fungi). Option C describes a specific step in leucine biosynthesis (3-methylcrotonyl-CoA → HMG-CoA) that is catalyzed by carboxylase/ligase enzymes, not P450s. The remaining option A is consistent with the well-established biological principle that fungal P450s are disproportionately dedicated to secondary metabolite (terpenoid, polyketide, etc.) biosynthesis rather than primary metabolism.",
    "missing_item_specific_fact": "The specific identity of aspterric acid and its terpenoid classification requires knowledge of this particular biosynthetic cluster, but the question only asks for the broad pathway category, which is inferable from P450 identification plus fungal context.",
    "reason": "The sequence provides a recognizable P450 heme-binding motif, enabling elimination of three options through general pathway biochemistry. The positive identification of 'secondary metabolite biosynthesis' follows from the well-known dominance of P450 involvement in fungal secondary metabolism, a general biological principle rather than a protein-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly incompatible with a fungal cytochrome P450: B involves purine biosynthesis (no P450), C is a leucine biosynthesis step (no P450), and D is a bacterial cell-wall process. Only A is consistent with a fungal P450."
  },
  "important_caveats": [
    "The P450 heme-binding motif identification relies on recognizing FGHGGHSCPGRF in the C-terminal region; a model unfamiliar with P450 motifs might not extract this signal.",
    "The 'fungal P450s → secondary metabolism' heuristic is a strong general principle but not an absolute rule; some fungal P450s participate in primary metabolism (e.g., ergosterol synthesis). However, none of the other options correspond to primary metabolic P450 pathways.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from a 2018 Nature paper and a 2024 J. Agric. Food Chem. paper, lending strong support to the pathway assignment."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
"Q0CPG6"
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"lineage":["Eukaryota","Fungi","Dikarya","Ascomycota","Pezizomycotina","Eurotiomycetes","Eurotiomycetidae","Eurotiales","Aspergillaceae","Aspergillus","Circumdati"],"scientificName":"Aspergillus terreus (strain NIH 2624 / FGSC A1156)","taxonId":341663}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein C"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"}],"value":"1.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29995859","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase astC"}}}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"29995859","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39511739","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:22.231293+00:00.  

```json
{"citation":{"authors":["Yan Y.","Liu Q.","Zang X.","Yuan S.","Bat-Erdene U.","Nguyen C.","Gan J.","Zhou J.","Jacobsen S.E.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"29995859"},{"database":"DOI","id":"10.1038/s41586-018-0319-4"}],"citationType":"journal article","firstPage":"415","id":"29995859","journal":"Nature","lastPage":"418","publicationDate":"2018","title":"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.","volume":"559"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `5cce9b434216d52e19bdca420e1e007eb4141638d98f34365df82078180206fe`.

### Evidence C7

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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 100. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
