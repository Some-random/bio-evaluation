# catalytic_activity_0119

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: supported

> The exact supplied sequence matches the 299-aa UniProt entry annotated as a bifunctional phosphoglucose/phosphomannose isomerase. That entry assigns the glucose-6-phosphate to fructose-6-phosphate reaction to the protein and cites experimental evidence (ECO:0000269).

Cited evidence: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe different broad activities, but the sequence alone does not provide a clear, general biological argument that identifies this particular protein as catalyzing the glucose-6-phosphate isomerization in D.

**Missing item-specific fact**

> The protein-specific functional identification as phosphoglucose isomerase, or equivalent experimental or database annotation, is needed to select D.

**Reason**

> The supporting functional annotation is reviewer-only and was not supplied in the question. Recognizing the exact sequence or recalling its annotation would be lookup or memorization, not reasoning from the provided input.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed options, D is the reaction supported for this protein. The evidence also assigns the protein a mannose-6-phosphate isomerization activity, but that reaction is not one of the choices.

### Important caveats

- The annotation is linked to a cited 2024 study and carries an experimental evidence code; the primary paper was not independently reviewed here.
- The supplied sequence matches the annotated sequence, but the exact source snapshot used by the question author is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the 299-aa UniProt entry annotated as a bifunctional phosphoglucose/phosphomannose isomerase. That entry assigns the glucose-6-phosphate to fructose-6-phosphate reaction to the protein and cites experimental evidence (ECO:0000269).",
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H4"
    ]
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

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A3MTR6`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 74. The exact author source snapshot remains unknown.

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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 119). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
