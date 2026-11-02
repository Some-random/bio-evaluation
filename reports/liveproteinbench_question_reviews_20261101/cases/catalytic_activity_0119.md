# catalytic_activity_0119

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLNDYLQWEKFILRGVEFPTRYRVDGDEVEITPSSRLYVSGMGGSGVVGDLIRDFSIVWNWDVEVTVVKDYFLRARDGLLIAVSYSGNTVETLYSVEYAKKRRIPTVAITTGGKLAQMGVPTIIIPKASAPRAALPQMLTAALHVVRKVYGIPIEIPEALEPPNDPLIHKLMEDFQKRPTIVAPETMRGVAYRVKNEFNENAKIEPSVEILPEAHHNWIEGSERPIVALTSPHIPREHQERVKATLEILGGTLYVVEMSTRGVLTFLREVGVASIKLAESRGVNPLATPRIEALKRRLQ

[Multiple Choices]
A. L-lysine(in) = L-lysine(out)
B. cyclo(N(8)-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-Trp) + AH2 + O2 = okaramine C + A + H2O
C. a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)
D. alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the 299-aa UniProt entry annotated as a bifunctional phosphoglucose/phosphomannose isomerase. That entry assigns the glucose-6-phosphate to fructose-6-phosphate reaction to the protein and cites experimental evidence (ECO:0000269).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe different broad activities, but the sequence alone does not provide a clear, general biological argument that identifies this particular protein as catalyzing the glucose-6-phosphate isomerization in D.


**Missing item-specific fact**

> The protein-specific functional identification as phosphoglucose isomerase, or equivalent experimental or database annotation, is needed to select D.


**Reason**

> The supporting functional annotation is reviewer-only and was not supplied in the question. Recognizing the exact sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, D is the reaction supported for this protein. The evidence also assigns the protein a mannose-6-phosphate isomerization activity, but that reaction is not one of the choices.


### Important caveats

- The annotation is linked to a cited 2024 study and carries an experimental evidence code; the primary paper was not independently reviewed here.
- The supplied sequence matches the annotated sequence, but the exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe different broad activities, but the sequence alone does not provide a clear, general biological argument that identifies this particular protein as catalyzing the glucose-6-phosphate isomerization in D.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification as phosphoglucose isomerase, or equivalent experimental or database annotation, is needed to select D.",
    "reason": "The supporting functional annotation is reviewer-only and was not supplied in the question. Recognizing the exact sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "catalytic_activity_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the 299-aa UniProt entry annotated as a bifunctional phosphoglucose/phosphomannose isomerase. That entry assigns the glucose-6-phosphate to fructose-6-phosphate reaction to the protein and cites experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The annotation is linked to a cited 2024 study and carries an experimental evidence code; the primary paper was not independently reviewed here.",
    "The supplied sequence matches the annotated sequence, but the exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, D is the reaction supported for this protein. The evidence also assigns the protein a mannose-6-phosphate isomerization activity, but that reaction is not one of the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the 299-aa UniProt entry annotated as a bifunctional phosphoglucose/phosphomannose isomerase. That entry assigns the glucose-6-phosphate to fructose-6-phosphate reaction to the protein and cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe different broad activities, but the sequence alone does not provide a clear, general biological argument that identifies this particular protein as catalyzing the glucose-6-phosphate isomerization in D.",
    "missing_item_specific_fact": "The protein-specific functional identification as phosphoglucose isomerase, or equivalent experimental or database annotation, is needed to select D.",
    "reason": "The supporting functional annotation is reviewer-only and was not supplied in the question. Recognizing the exact sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, D is the reaction supported for this protein. The evidence also assigns the protein a mannose-6-phosphate isomerization activity, but that reaction is not one of the choices."
  },
  "important_caveats": [
    "The annotation is linked to a cited 2024 study and carries an experimental evidence code; the primary paper was not independently reviewed here.",
    "The supplied sequence matches the annotated sequence, but the exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A3MTR6 (sequence SHA256 matched, 299 aa) is annotated as Bifunctional phosphoglucose/phosphomannose isomerase (EC 5.3.1.8 and 5.3.1.9) with experimental evidence (ECO:0000269, PubMed:39208883). The catalytic activity for EC 5.3.1.9 is explicitly listed as 'alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate', matching Choice D exactly. The second activity (mannose-6-phosphate isomerase) is not among the answer choices, so D is the uniquely correct option provided.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'SGMGGSGVVGDL' motif near residues 35-47, which is a hallmark signature of the phosphoglucose isomerase (PGI) family within the TIM-barrel superfamily. Additional conserved PGI motifs ('GGKLAQMG', 'GGTLYVVEMSTRG') are present. The ~300-residue length is consistent with archaeal/bacterial PGI (eukaryotic PGI is ~550 aa). These sequence features allow identification of PGI activity (EC 5.3.1.9) without needing to recall a specific UniProt entry. Among the four choices, only D corresponds to a PGI-catalyzed isomerization; A is a transporter, B is a P450-type oxidation, and C is a glycoside hydrolase reaction—none match TIM-barrel isomerase motifs.


**Missing item-specific fact**

> None critical. The bifunctional PMI activity (EC 5.3.1.8) of this particular archaeal enzyme is an item-specific fact, but it does not affect answer selection because the PMI reaction is not among the choices.


**Reason**

> The GMGGSG motif is a well-known PGI family signature taught in enzymology and biochemistry. Recognizing it as indicative of phosphoglucose isomerase activity constitutes general biological knowledge about enzyme-family sequence signatures, not recall of a specific database annotation. The distractors (transporter, P450, glycosidase) are clearly incompatible with the observed TIM-barrel PGI motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the enzyme is bifunctional (also catalyzes D-mannose 6-phosphate = D-fructose 6-phosphate), that alternative reaction is not offered as a choice. Among A-D, only D matches the identified PGI activity. No other option is defensible given the sequence motifs.


### Important caveats

- The protein is bifunctional (PGI + PMI); the question implicitly selects the PGI activity as the 'answer' because only that reaction appears among the choices.
- The UniProt annotation carries experimental evidence (ECO:0000269) from a 2024 structural/functional study (PubMed:39208883), strengthening the annotation's reliability.
- The 'GGSG' PGI motif recognition, while part of standard enzymology, still requires familiarity with prokaryotic PGI sequence signatures; this is specialized but general family-level knowledge rather than a single-entry lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'SGMGGSGVVGDL' motif near residues 35-47, which is a hallmark signature of the phosphoglucose isomerase (PGI) family within the TIM-barrel superfamily. Additional conserved PGI motifs ('GGKLAQMG', 'GGTLYVVEMSTRG') are present. The ~300-residue length is consistent with archaeal/bacterial PGI (eukaryotic PGI is ~550 aa). These sequence features allow identification of PGI activity (EC 5.3.1.9) without needing to recall a specific UniProt entry. Among the four choices, only D corresponds to a PGI-catalyzed isomerization; A is a transporter, B is a P450-type oxidation, and C is a glycoside hydrolase reaction—none match TIM-barrel isomerase motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The bifunctional PMI activity (EC 5.3.1.8) of this particular archaeal enzyme is an item-specific fact, but it does not affect answer selection because the PMI reaction is not among the choices.",
    "reason": "The GMGGSG motif is a well-known PGI family signature taught in enzymology and biochemistry. Recognizing it as indicative of phosphoglucose isomerase activity constitutes general biological knowledge about enzyme-family sequence signatures, not recall of a specific database annotation. The distractors (transporter, P450, glycosidase) are clearly incompatible with the observed TIM-barrel PGI motifs."
  },
  "case_id": "catalytic_activity_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A3MTR6 (sequence SHA256 matched, 299 aa) is annotated as Bifunctional phosphoglucose/phosphomannose isomerase (EC 5.3.1.8 and 5.3.1.9) with experimental evidence (ECO:0000269, PubMed:39208883). The catalytic activity for EC 5.3.1.9 is explicitly listed as 'alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate', matching Choice D exactly. The second activity (mannose-6-phosphate isomerase) is not among the answer choices, so D is the uniquely correct option provided."
  },
  "important_caveats": [
    "The protein is bifunctional (PGI + PMI); the question implicitly selects the PGI activity as the 'answer' because only that reaction appears among the choices.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2024 structural/functional study (PubMed:39208883), strengthening the annotation's reliability.",
    "The 'GGSG' PGI motif recognition, while part of standard enzymology, still requires familiarity with prokaryotic PGI sequence signatures; this is specialized but general family-level knowledge rather than a single-entry lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the enzyme is bifunctional (also catalyzes D-mannose 6-phosphate = D-fructose 6-phosphate), that alternative reaction is not offered as a choice. Among A-D, only D matches the identified PGI activity. No other option is defensible given the sequence motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A3MTR6 (sequence SHA256 matched, 299 aa) is annotated as Bifunctional phosphoglucose/phosphomannose isomerase (EC 5.3.1.8 and 5.3.1.9) with experimental evidence (ECO:0000269, PubMed:39208883). The catalytic activity for EC 5.3.1.9 is explicitly listed as 'alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate', matching Choice D exactly. The second activity (mannose-6-phosphate isomerase) is not among the answer choices, so D is the uniquely correct option provided.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'SGMGGSGVVGDL' motif near residues 35-47, which is a hallmark signature of the phosphoglucose isomerase (PGI) family within the TIM-barrel superfamily. Additional conserved PGI motifs ('GGKLAQMG', 'GGTLYVVEMSTRG') are present. The ~300-residue length is consistent with archaeal/bacterial PGI (eukaryotic PGI is ~550 aa). These sequence features allow identification of PGI activity (EC 5.3.1.9) without needing to recall a specific UniProt entry. Among the four choices, only D corresponds to a PGI-catalyzed isomerization; A is a transporter, B is a P450-type oxidation, and C is a glycoside hydrolase reaction—none match TIM-barrel isomerase motifs.",
    "missing_item_specific_fact": "None critical. The bifunctional PMI activity (EC 5.3.1.8) of this particular archaeal enzyme is an item-specific fact, but it does not affect answer selection because the PMI reaction is not among the choices.",
    "reason": "The GMGGSG motif is a well-known PGI family signature taught in enzymology and biochemistry. Recognizing it as indicative of phosphoglucose isomerase activity constitutes general biological knowledge about enzyme-family sequence signatures, not recall of a specific database annotation. The distractors (transporter, P450, glycosidase) are clearly incompatible with the observed TIM-barrel PGI motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the enzyme is bifunctional (also catalyzes D-mannose 6-phosphate = D-fructose 6-phosphate), that alternative reaction is not offered as a choice. Among A-D, only D matches the identified PGI activity. No other option is defensible given the sequence motifs."
  },
  "important_caveats": [
    "The protein is bifunctional (PGI + PMI); the question implicitly selects the PGI activity as the 'answer' because only that reaction appears among the choices.",
    "The UniProt annotation carries experimental evidence (ECO:0000269) from a 2024 structural/functional study (PubMed:39208883), strengthening the annotation's reliability.",
    "The 'GGSG' PGI motif recognition, while part of standard enzymology, still requires familiarity with prokaryotic PGI sequence signatures; this is specialized but general family-level knowledge rather than a single-entry lookup."
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

**Accession:** `A3MTR6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
"A3MTR6"
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39208883","source":"PubMed"}],"value":"Glucose-6-phosphate isomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"GPI"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Mannose-6-phosphate isomerase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"5.3.1.8"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"5.3.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39208883","source":"PubMed"}],"value":"Bifunctional phosphoglucose/phosphomannose isomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Bifunctional PGI/PMI"}]}}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.3.1.9","evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"name":"alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:11816"},{"database":"ChEBI","id":"CHEBI:57634"},{"database":"ChEBI","id":"CHEBI:58225"}]}}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"citation":{"authors":["Maqsood A.","Shakir N.A.","Aslam M.","Rahman M.","Rashid N."],"citationCrossReferences":[{"database":"PubMed","id":"39208883"},{"database":"DOI","id":"10.1016/j.ijbiomac.2024.135127"}],"citationType":"journal article","firstPage":"135127","id":"39208883","journal":"Int. J. Biol. Macromol.","lastPage":"135127","publicationDate":"2024","title":"Structural and functional investigations of Pcal_0606, a bifunctional phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.","volume":"279"},"referenceComments":[{"type":"STRAIN","value":"DSM 21063 / JCM 11548 / VA1"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)  
**Locator:** `lines 6-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:27:04.156488+00:00.  

```text
DE   RecName: Full=Bifunctional phosphoglucose/phosphomannose isomerase {ECO:0000303|PubMed:39208883};
DE            Short=Bifunctional PGI/PMI {ECO:0000305};
DE            EC=5.3.1.8 {ECO:0000269|PubMed:39208883};
DE            EC=5.3.1.9 {ECO:0000269|PubMed:39208883};
DE   AltName: Full=Glucose-6-phosphate isomerase {ECO:0000303|PubMed:39208883};
DE            Short=GPI {ECO:0000305};
DE   AltName: Full=Mannose-6-phosphate isomerase {ECO:0000305};
```

Source SHA-256: `9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)  
**Locator:** `lines 44-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:27:04.156488+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate;
CC         Xref=Rhea:RHEA:11816, ChEBI:CHEBI:57634, ChEBI:CHEBI:58225;
CC         EC=5.3.1.9; Evidence={ECO:0000269|PubMed:39208883};
```

Source SHA-256: `9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
