# GO_molecular_function_0087

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — isomerase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIRLLYLLVKPAGMSDETFRAECLRHYEMSHDVPGLHKYEVRLVAEQPTDTHVPFFDIGHVDAIGECWFKDDAAYATYMASDIRKAWFEHGKTFIGQLKPFRTAPVAGDEPAS

[Multiple Choices]
A. S-adenosyl-L-methionine binding
B. isomerase activity
C. carbohydrate binding
D. rRNA binding
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry for a 4-carboxymethyl-4-methylbutenolide mutase. The entry reports experimentally supported isomerization activity, and the specific mutase activity is a subtype of isomerase activity, matching choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [GO2](#evidence-go2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No clear sequence feature or supplied biological context distinguishes this specific isomerase from the listed binding functions. Recognizing the exact protein or relying on its annotated function would require protein-specific knowledge.


**Missing item-specific fact**

> The protein-specific identity and evidence that this sequence catalyzes an isomerization reaction.


**Reason**

> The key is supported by external, sequence-matched annotation and cited experimental evidence, but those facts are absent from the question input. The short sequence and choices alone do not provide a defensible distinguishing argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports isomerase activity; none of the other choices is indicated as a function of this protein.


### Important caveats

- The matched database entry and literature citations support the answer, but reviewer-only sources were not available to the evaluated model.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No clear sequence feature or supplied biological context distinguishes this specific isomerase from the listed binding functions. Recognizing the exact protein or relying on its annotated function would require protein-specific knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and evidence that this sequence catalyzes an isomerization reaction.",
    "reason": "The key is supported by external, sequence-matched annotation and cited experimental evidence, but those facts are absent from the question input. The short sequence and choices alone do not provide a defensible distinguishing argument."
  },
  "case_id": "GO_molecular_function_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "GO2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for a 4-carboxymethyl-4-methylbutenolide mutase. The entry reports experimentally supported isomerization activity, and the specific mutase activity is a subtype of isomerase activity, matching choice B."
  },
  "important_caveats": [
    "The matched database entry and literature citations support the answer, but reviewer-only sources were not available to the evaluated model.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports isomerase activity; none of the other choices is indicated as a function of this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for a 4-carboxymethyl-4-methylbutenolide mutase. The entry reports experimentally supported isomerization activity, and the specific mutase activity is a subtype of isomerase activity, matching choice B.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "GO1", "GO2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No clear sequence feature or supplied biological context distinguishes this specific isomerase from the listed binding functions. Recognizing the exact protein or relying on its annotated function would require protein-specific knowledge.",
    "missing_item_specific_fact": "The protein-specific identity and evidence that this sequence catalyzes an isomerization reaction.",
    "reason": "The key is supported by external, sequence-matched annotation and cited experimental evidence, but those facts are absent from the question input. The short sequence and choices alone do not provide a defensible distinguishing argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports isomerase activity; none of the other choices is indicated as a function of this protein."
  },
  "important_caveats": [
    "The matched database entry and literature citations support the answer, but reviewer-only sources were not available to the evaluated model.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (UniProt O51799, MMLI_CUPPJ) is experimentally characterized (ECO:0000269, PubMed:2241929 and PubMed:9461415) as EC 5.4.99.14, a mutase catalyzing 4-methylmuconolactone → 3-methylmuconolactone. Its GO annotation GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity) is is_a GO:0016866 (intramolecular transferase/mutase activity) which is is_a GO:0016853 (isomerase activity, EC class 5). The expected answer 'isomerase activity' is the correct parent GO term for this enzyme's molecular function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO5](#evidence-go5), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly argue by elimination that the 113-aa sequence lacks canonical SAM-binding motifs (e.g., CX3CX2C for radical SAM enzymes), lacks RNA-binding domains (RGG, KH, RRM), and lacks lectin/carbohydrate-binding folds, leaving 'isomerase activity' as the only catalytic option. However, this negative reasoning does not positively identify the enzyme as an isomerase specifically rather than any other enzyme class, and the sequence does not contain a universally recognized 'isomerase signature.'


**Missing item-specific fact**

> The specific identification of this 113-aa sequence as 4-methylmuconolactone methylisomerase (EC 5.4.99.14), a mutase within EC class 5 (isomerases), requires recognizing the protein sequence or its database annotation. No general sequence heuristic reliably assigns 'isomerase activity' to this particular fold without prior knowledge of the MMLI protein or its structural family.


**Reason**

> The sequence is short (113 aa) and does not display a universally recognized catalytic motif specific to isomerases. While the absence of binding-domain hallmarks weakly disfavors options A, C, and D, the positive assignment to 'isomerase activity' over any other enzyme class depends on recognizing this specific protein or its annotation, making the question lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GO ontology path unambiguously places the protein's function (GO:0047469) under isomerase activity (GO:0016853). The other three options (SAM binding, carbohydrate binding, rRNA binding) have no annotation or experimental support for this protein. No alternative option is defensible.


### Important caveats

- The expected answer 'isomerase activity' (GO:0016853) is a parent term; the precise annotation is GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity), which is a specific mutase. The broad term 'isomerase activity' is correct but imprecise.
- The evidence codes for the functional annotation are ECO:0000269 (experimental evidence from PubMed), confirming the isomerase activity is experimentally established, not merely computational.
- The sequence match is confirmed (SHA-256 identical between benchmark and UniProt entry, both 113 aa).
- The GO annotation in the current entry (C7) uses EXP:UniProtKB evidence, while the historical entry (H6) shows IEA:UniProtKB-EC for the same GO term, indicating the evidence code was upgraded over time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly argue by elimination that the 113-aa sequence lacks canonical SAM-binding motifs (e.g., CX3CX2C for radical SAM enzymes), lacks RNA-binding domains (RGG, KH, RRM), and lacks lectin/carbohydrate-binding folds, leaving 'isomerase activity' as the only catalytic option. However, this negative reasoning does not positively identify the enzyme as an isomerase specifically rather than any other enzyme class, and the sequence does not contain a universally recognized 'isomerase signature.'",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this 113-aa sequence as 4-methylmuconolactone methylisomerase (EC 5.4.99.14), a mutase within EC class 5 (isomerases), requires recognizing the protein sequence or its database annotation. No general sequence heuristic reliably assigns 'isomerase activity' to this particular fold without prior knowledge of the MMLI protein or its structural family.",
    "reason": "The sequence is short (113 aa) and does not display a universally recognized catalytic motif specific to isomerases. While the absence of binding-domain hallmarks weakly disfavors options A, C, and D, the positive assignment to 'isomerase activity' over any other enzyme class depends on recognizing this specific protein or its annotation, making the question lookup-dependent."
  },
  "case_id": "GO_molecular_function_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "GO1",
      "GO2",
      "GO5",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The protein (UniProt O51799, MMLI_CUPPJ) is experimentally characterized (ECO:0000269, PubMed:2241929 and PubMed:9461415) as EC 5.4.99.14, a mutase catalyzing 4-methylmuconolactone → 3-methylmuconolactone. Its GO annotation GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity) is is_a GO:0016866 (intramolecular transferase/mutase activity) which is is_a GO:0016853 (isomerase activity, EC class 5). The expected answer 'isomerase activity' is the correct parent GO term for this enzyme's molecular function."
  },
  "important_caveats": [
    "The expected answer 'isomerase activity' (GO:0016853) is a parent term; the precise annotation is GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity), which is a specific mutase. The broad term 'isomerase activity' is correct but imprecise.",
    "The evidence codes for the functional annotation are ECO:0000269 (experimental evidence from PubMed), confirming the isomerase activity is experimentally established, not merely computational.",
    "The sequence match is confirmed (SHA-256 identical between benchmark and UniProt entry, both 113 aa).",
    "The GO annotation in the current entry (C7) uses EXP:UniProtKB evidence, while the historical entry (H6) shows IEA:UniProtKB-EC for the same GO term, indicating the evidence code was upgraded over time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GO ontology path unambiguously places the protein's function (GO:0047469) under isomerase activity (GO:0016853). The other three options (SAM binding, carbohydrate binding, rRNA binding) have no annotation or experimental support for this protein. No alternative option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (UniProt O51799, MMLI_CUPPJ) is experimentally characterized (ECO:0000269, PubMed:2241929 and PubMed:9461415) as EC 5.4.99.14, a mutase catalyzing 4-methylmuconolactone → 3-methylmuconolactone. Its GO annotation GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity) is is_a GO:0016866 (intramolecular transferase/mutase activity) which is is_a GO:0016853 (isomerase activity, EC class 5). The expected answer 'isomerase activity' is the correct parent GO term for this enzyme's molecular function.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "GO1", "GO2", "GO5", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly argue by elimination that the 113-aa sequence lacks canonical SAM-binding motifs (e.g., CX3CX2C for radical SAM enzymes), lacks RNA-binding domains (RGG, KH, RRM), and lacks lectin/carbohydrate-binding folds, leaving 'isomerase activity' as the only catalytic option. However, this negative reasoning does not positively identify the enzyme as an isomerase specifically rather than any other enzyme class, and the sequence does not contain a universally recognized 'isomerase signature.'",
    "missing_item_specific_fact": "The specific identification of this 113-aa sequence as 4-methylmuconolactone methylisomerase (EC 5.4.99.14), a mutase within EC class 5 (isomerases), requires recognizing the protein sequence or its database annotation. No general sequence heuristic reliably assigns 'isomerase activity' to this particular fold without prior knowledge of the MMLI protein or its structural family.",
    "reason": "The sequence is short (113 aa) and does not display a universally recognized catalytic motif specific to isomerases. While the absence of binding-domain hallmarks weakly disfavors options A, C, and D, the positive assignment to 'isomerase activity' over any other enzyme class depends on recognizing this specific protein or its annotation, making the question lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GO ontology path unambiguously places the protein's function (GO:0047469) under isomerase activity (GO:0016853). The other three options (SAM binding, carbohydrate binding, rRNA binding) have no annotation or experimental support for this protein. No alternative option is defensible."
  },
  "important_caveats": [
    "The expected answer 'isomerase activity' (GO:0016853) is a parent term; the precise annotation is GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity), which is a specific mutase. The broad term 'isomerase activity' is correct but imprecise.",
    "The evidence codes for the functional annotation are ECO:0000269 (experimental evidence from PubMed), confirming the isomerase activity is experimentally established, not merely computational.",
    "The sequence match is confirmed (SHA-256 identical between benchmark and UniProt entry, both 113 aa).",
    "The GO annotation in the current entry (C7) uses EXP:UniProtKB evidence, while the historical entry (H6) shows IEA:UniProtKB-EC for the same GO term, indicating the evidence code was upgraded over time."
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

**Accession:** `O51799` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 65. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
"O51799"
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"2241929","source":"PubMed"}],"value":"4-carboxymethyl-4-methylbut-2-en-4-olide isomerase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"2241929","source":"PubMed"}],"value":"4-methyl-2-enelactone isomerase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9461415","source":"PubMed"}],"value":"4-methylmuconolactone methylisomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"9461415","source":"PubMed"}],"value":"MLMI"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"value":"5.4.99.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4-carboxymethyl-4-methylbutenolide mutase"}}}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"value":"Isomerase involved in the degradation of 4-methylcatechol (PubMed:2241929). Catalyzes the isomerization of the dead-end metabolite 4-methylmuconolactone (4-ML) to 3-methylmuconolactone (3-ML), which can then be further degraded through a modified 3-oxoadipate pathway (PubMed:2241929, PubMed:9461415). Can also use 1-methylbislactone, but not the isomeric methyl-substituted 4-carboxymethylbut-2-en-4-olides (PubMed:2241929)"}]}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19238"}}],"reaction":{"ecNumber":"5.4.99.14","evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"name":"4-methylmuconolactone = 3-methylmuconolactone","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19237"},{"database":"ChEBI","id":"CHEBI:57883"},{"database":"ChEBI","id":"CHEBI:57888"}]}}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O51799.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.163444+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"2241929","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9461415","source":"PubMed"}],"id":"GO:0047469","properties":[{"key":"GoTerm","value":"F:4-carboxymethyl-4-methylbutenolide mutase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `b70c681e56806aa898c9fb39f2f630921678c753acd190c1b04d04bedc7c3968`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)  
**Locator:** `lines 56-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-01T06:28:15.847605+00:00.  

```text
CC   -!- FUNCTION: Isomerase involved in the degradation of 4-methylcatechol
CC       (PubMed:2241929). Catalyzes the isomerization of the dead-end
CC       metabolite 4-methylmuconolactone (4-ML) to 3-methylmuconolactone (3-
CC       ML), which can then be further degraded through a modified 3-oxoadipate
CC       pathway (PubMed:2241929, PubMed:9461415). Can also use 1-
CC       methylbislactone, but not the isomeric methyl-substituted 4-
CC       carboxymethylbut-2-en-4-olides (PubMed:2241929).
CC       {ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415}.
```

Source SHA-256: `1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)  
**Locator:** `lines 64-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-01T06:28:15.847605+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-methylmuconolactone = 3-methylmuconolactone;
CC         Xref=Rhea:RHEA:19237, ChEBI:CHEBI:57883, ChEBI:CHEBI:57888;
CC         EC=5.4.99.14; Evidence={ECO:0000269|PubMed:2241929,
CC         ECO:0000269|PubMed:9461415};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19238;
CC         Evidence={ECO:0000269|PubMed:2241929, ECO:0000269|PubMed:9461415};
```

Source SHA-256: `1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O51799?format=txt&versions=65)  
**Locator:** `lines 101-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-01T06:28:15.847605+00:00.  

```text
DR   GO; GO:0047469; F:4-carboxymethyl-4-methylbutenolide mutase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `1fb5ec02f51833bc2a3a34baeeee4fa6645485da2ba66876fa2f98e7c8ee89ac`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 130892-130912`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016853
name: isomerase activity
namespace: molecular_function
def: "Catalysis of the geometric or structural changes within one molecule. Isomerase is the systematic name for any enzyme of EC class 5." [ISBN:0198506732]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_prokaryote
subset: goslim_yeast
synonym: "other isomerase activity" NARROW []
xref: EC:5.-.-.-
xref: Reactome:R-HSA-2161666 "PGA2 is isomerised to PGC2"
xref: Reactome:R-HSA-2161735 "PGC2 is isomerised to PGB2"
xref: Reactome:R-HSA-6787623 "GFUS dimer epimerises GDP-DHDMan to GDP-KDGal"
is_a: GO:0003824 ! catalytic activity
property_value: skos:exactMatch EC:5.-.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 131035-131045`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016866
name: intramolecular transferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a functional group from one position to another within a single molecule." [GOC:mah]
synonym: "intramolecular transferase activity, transferring other groups" NARROW []
synonym: "mutase activity" EXACT []
xref: EC:5.4.-.-
is_a: GO:0016853 ! isomerase activity
property_value: skos:exactMatch EC:5.4.-.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 290813-290830`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0047469
name: 4-carboxymethyl-4-methylbutenolide mutase activity
namespace: molecular_function
def: "Catalysis of the reaction: 4-carboxymethyl-4-methylbut-2-en-1,4-olide = 4-carboxymethyl-3-methylbut-2-en-1,4-olide." [EC:5.4.99.14, RHEA:19237]
synonym: "4-carboxymethyl-4-methylbut-2-en-1,4-olide methylmutase activity" RELATED [EC:5.4.99.14]
synonym: "4-methyl-2-enelactone isomerase activity" RELATED [EC:5.4.99.14]
synonym: "4-methyl-2-enelactone methyl-isomerase activity" RELATED [EC:5.4.99.14]
synonym: "4-methyl-3-enelactone methyl isomerase activity" RELATED [EC:5.4.99.14]
synonym: "4-methylmuconolactone methylisomerase activity" RELATED [EC:5.4.99.14]
xref: EC:5.4.99.14
xref: KEGG_REACTION:R04510
xref: MetaCyc:5.4.99.14-RXN
xref: RHEA:19237
is_a: GO:0016866 ! intramolecular transferase activity
property_value: skos:exactMatch EC:5.4.99.14
property_value: skos:exactMatch RHEA:19237

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
