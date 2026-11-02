# GO_molecular_function_0014

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — isomerase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIRILYLLVKPESMSHEQFRKECVVHFQMSAGMPGLHKYEVRLVAGNPTDTHVPYLDVGRIDAIGECWFASEEQYQVYMESDIRKAWFEHGKYFIGQLKPFVTEELV

[Multiple Choices]
A. sequence-specific DNA binding
B. DNA nuclease activity
C. serine-type endopeptidase activity
D. isomerase activity
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

> The exact sequence matches the annotated 4-carboxymethyl-4-methylbutenolide mutase. Its experimentally supported reaction is an isomerization, so the broader choice D, isomerase activity, is supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a small protein, but its length or general composition does not meaningfully distinguish isomerase activity from the listed DNA-binding or nuclease activities.


**Missing item-specific fact**

> The protein-specific identity or functional annotation linking this sequence to 4-carboxymethyl-4-methylbutenolide mutase activity.


**Reason**

> Choosing D depends on recognizing the sequence through homology or an external annotation; the supplied sequence and choices alone provide no concrete general biological argument that establishes this particular function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimental reaction supports isomerase activity, and none of the other choices is supported by the supplied evidence.


### Important caveats

- The reviewer-only evidence identifies a sequence-matched UniProt record and cites experimental evidence codes and publications; those annotations were not supplied to the evaluated model.
- The cited primary papers were not independently retrieved and comprehensively validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a small protein, but its length or general composition does not meaningfully distinguish isomerase activity from the listed DNA-binding or nuclease activities.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation linking this sequence to 4-carboxymethyl-4-methylbutenolide mutase activity.",
    "reason": "Choosing D depends on recognizing the sequence through homology or an external annotation; the supplied sequence and choices alone provide no concrete general biological argument that establishes this particular function."
  },
  "case_id": "GO_molecular_function_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated 4-carboxymethyl-4-methylbutenolide mutase. Its experimentally supported reaction is an isomerization, so the broader choice D, isomerase activity, is supported."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched UniProt record and cites experimental evidence codes and publications; those annotations were not supplied to the evaluated model.",
    "The cited primary papers were not independently retrieved and comprehensively validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental reaction supports isomerase activity, and none of the other choices is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated 4-carboxymethyl-4-methylbutenolide mutase. Its experimentally supported reaction is an isomerization, so the broader choice D, isomerase activity, is supported.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a small protein, but its length or general composition does not meaningfully distinguish isomerase activity from the listed DNA-binding or nuclease activities.",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation linking this sequence to 4-carboxymethyl-4-methylbutenolide mutase activity.",
    "reason": "Choosing D depends on recognizing the sequence through homology or an external annotation; the supplied sequence and choices alone provide no concrete general biological argument that establishes this particular function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental reaction supports isomerase activity, and none of the other choices is supported by the supplied evidence."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched UniProt record and cites experimental evidence codes and publications; those annotations were not supplied to the evaluated model.",
    "The cited primary papers were not independently retrieved and comprehensively validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt C5MR76 (sequence matched, 107 aa) annotates this protein as 4-methylmuconolactone methylisomerase / 4-carboxymethyl-4-methylbutenolide mutase (EC 5.4.99.14), with experimental evidence (ECO:0000269, PubMed:19801657 crystal structure and catalytic characterization). The GO annotation GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity) is_a GO:0016866 (intramolecular transferase activity) is_a GO:0016853 (isomerase activity). EC class 5 is Isomerases. The function comment explicitly states 'Isomerase involved in the degradation of 4-methylsalicylate and 5-methylsalicylate.' The author key D (isomerase activity) is the correct parent GO term.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO3](#evidence-go3), [GO4](#evidence-go4), [GO6](#evidence-go6), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could attempt elimination: the 107-aa sequence lacks recognizable DNA-binding motifs (helix-turn-helix, zinc finger, etc.) to rule out A; lacks nuclease catalytic residues/motifs to rule out B; and lacks a canonical Ser-His-Asp catalytic triad in a serine-protease fold to rule out C. However, this negative elimination does not positively confirm isomerase activity. The sequence contains Cys, His, and Tyr residues (active-site residues His-26, Tyr-39, His-52, Cys-67 per the crystal structure paper), but these are not a recognized isomerase signature motif. There is no well-known, generalizable sequence motif in this 107-aa protein that positively identifies it as an isomerase rather than some other small metabolic enzyme.


**Missing item-specific fact**

> The specific identity of this protein as 4-methylmuconolactone methylisomerase (EC 5.4.99.14), a member of a specialized bacterial lactone-mutase family involved in methylsalicylate degradation, is required to positively assign isomerase activity. Without recognizing the sequence or knowing this enzyme family, the sequence alone does not provide a positive, generalizable argument for isomerase over other possible small-enzyme functions.


**Reason**

> The sequence provides no recognizable isomerase fold signature or catalytic mechanism motif that would allow general biological reasoning to positively identify isomerase activity. While elimination of A, B, and C via absence of their characteristic motifs is partially defensible, the positive assignment to D requires item-specific knowledge of this particular protein family or its database annotation. Recognizing the exact sequence and recalling its UniProt entry does not constitute reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the four choices, A (sequence-specific DNA binding), B (DNA nuclease activity), and C (serine-type endopeptidase activity) can each be reasonably excluded from the sequence by absence of their defining structural/functional motifs. D (isomerase activity) is the only remaining option and is confirmed by the database annotation. No other option is defensible for this protein.


### Important caveats

- The evaluated model receives only the 107-aa sequence and four choices; all UniProt/GO annotations are reviewer-only and were not in the model input.
- The GO term in the answer key is the broad parent term GO:0016853 (isomerase activity), not the specific GO:0047469; the ontology path confirms the parent-child relationship.
- The protein's crystal structure (PDB 3HDS, 3HF5, 3HFK) and mutagenesis data (PubMed:19801657) provide experimental (ECO:0000269) support for the isomerase function, not merely computational annotation.
- The sequence is short (107 aa) and lacks widely recognized motif signatures, making de novo functional assignment from sequence alone very difficult without family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could attempt elimination: the 107-aa sequence lacks recognizable DNA-binding motifs (helix-turn-helix, zinc finger, etc.) to rule out A; lacks nuclease catalytic residues/motifs to rule out B; and lacks a canonical Ser-His-Asp catalytic triad in a serine-protease fold to rule out C. However, this negative elimination does not positively confirm isomerase activity. The sequence contains Cys, His, and Tyr residues (active-site residues His-26, Tyr-39, His-52, Cys-67 per the crystal structure paper), but these are not a recognized isomerase signature motif. There is no well-known, generalizable sequence motif in this 107-aa protein that positively identifies it as an isomerase rather than some other small metabolic enzyme.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as 4-methylmuconolactone methylisomerase (EC 5.4.99.14), a member of a specialized bacterial lactone-mutase family involved in methylsalicylate degradation, is required to positively assign isomerase activity. Without recognizing the sequence or knowing this enzyme family, the sequence alone does not provide a positive, generalizable argument for isomerase over other possible small-enzyme functions.",
    "reason": "The sequence provides no recognizable isomerase fold signature or catalytic mechanism motif that would allow general biological reasoning to positively identify isomerase activity. While elimination of A, B, and C via absence of their characteristic motifs is partially defensible, the positive assignment to D requires item-specific knowledge of this particular protein family or its database annotation. Recognizing the exact sequence and recalling its UniProt entry does not constitute reasoning."
  },
  "case_id": "GO_molecular_function_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "GO3",
      "GO4",
      "GO6",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt C5MR76 (sequence matched, 107 aa) annotates this protein as 4-methylmuconolactone methylisomerase / 4-carboxymethyl-4-methylbutenolide mutase (EC 5.4.99.14), with experimental evidence (ECO:0000269, PubMed:19801657 crystal structure and catalytic characterization). The GO annotation GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity) is_a GO:0016866 (intramolecular transferase activity) is_a GO:0016853 (isomerase activity). EC class 5 is Isomerases. The function comment explicitly states 'Isomerase involved in the degradation of 4-methylsalicylate and 5-methylsalicylate.' The author key D (isomerase activity) is the correct parent GO term."
  },
  "important_caveats": [
    "The evaluated model receives only the 107-aa sequence and four choices; all UniProt/GO annotations are reviewer-only and were not in the model input.",
    "The GO term in the answer key is the broad parent term GO:0016853 (isomerase activity), not the specific GO:0047469; the ontology path confirms the parent-child relationship.",
    "The protein's crystal structure (PDB 3HDS, 3HF5, 3HFK) and mutagenesis data (PubMed:19801657) provide experimental (ECO:0000269) support for the isomerase function, not merely computational annotation.",
    "The sequence is short (107 aa) and lacks widely recognized motif signatures, making de novo functional assignment from sequence alone very difficult without family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four choices, A (sequence-specific DNA binding), B (DNA nuclease activity), and C (serine-type endopeptidase activity) can each be reasonably excluded from the sequence by absence of their defining structural/functional motifs. D (isomerase activity) is the only remaining option and is confirmed by the database annotation. No other option is defensible for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt C5MR76 (sequence matched, 107 aa) annotates this protein as 4-methylmuconolactone methylisomerase / 4-carboxymethyl-4-methylbutenolide mutase (EC 5.4.99.14), with experimental evidence (ECO:0000269, PubMed:19801657 crystal structure and catalytic characterization). The GO annotation GO:0047469 (4-carboxymethyl-4-methylbutenolide mutase activity) is_a GO:0016866 (intramolecular transferase activity) is_a GO:0016853 (isomerase activity). EC class 5 is Isomerases. The function comment explicitly states 'Isomerase involved in the degradation of 4-methylsalicylate and 5-methylsalicylate.' The author key D (isomerase activity) is the correct parent GO term.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "GO3", "GO4", "GO6", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could attempt elimination: the 107-aa sequence lacks recognizable DNA-binding motifs (helix-turn-helix, zinc finger, etc.) to rule out A; lacks nuclease catalytic residues/motifs to rule out B; and lacks a canonical Ser-His-Asp catalytic triad in a serine-protease fold to rule out C. However, this negative elimination does not positively confirm isomerase activity. The sequence contains Cys, His, and Tyr residues (active-site residues His-26, Tyr-39, His-52, Cys-67 per the crystal structure paper), but these are not a recognized isomerase signature motif. There is no well-known, generalizable sequence motif in this 107-aa protein that positively identifies it as an isomerase rather than some other small metabolic enzyme.",
    "missing_item_specific_fact": "The specific identity of this protein as 4-methylmuconolactone methylisomerase (EC 5.4.99.14), a member of a specialized bacterial lactone-mutase family involved in methylsalicylate degradation, is required to positively assign isomerase activity. Without recognizing the sequence or knowing this enzyme family, the sequence alone does not provide a positive, generalizable argument for isomerase over other possible small-enzyme functions.",
    "reason": "The sequence provides no recognizable isomerase fold signature or catalytic mechanism motif that would allow general biological reasoning to positively identify isomerase activity. While elimination of A, B, and C via absence of their characteristic motifs is partially defensible, the positive assignment to D requires item-specific knowledge of this particular protein family or its database annotation. Recognizing the exact sequence and recalling its UniProt entry does not constitute reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four choices, A (sequence-specific DNA binding), B (DNA nuclease activity), and C (serine-type endopeptidase activity) can each be reasonably excluded from the sequence by absence of their defining structural/functional motifs. D (isomerase activity) is the only remaining option and is confirmed by the database annotation. No other option is defensible for this protein."
  },
  "important_caveats": [
    "The evaluated model receives only the 107-aa sequence and four choices; all UniProt/GO annotations are reviewer-only and were not in the model input.",
    "The GO term in the answer key is the broad parent term GO:0016853 (isomerase activity), not the specific GO:0047469; the ontology path confirms the parent-child relationship.",
    "The protein's crystal structure (PDB 3HDS, 3HF5, 3HFK) and mutagenesis data (PubMed:19801657) provide experimental (ECO:0000269) support for the isomerase function, not merely computational annotation.",
    "The sequence is short (107 aa) and lacks widely recognized motif signatures, making de novo functional assignment from sequence alone very difficult without family-level knowledge."
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

**Accession:** `C5MR76` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 66. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"19801657","source":"PubMed"}],"value":"4-methylmuconolactone methylisomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"19801657","source":"PubMed"}],"value":"MLMI"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"}],"value":"5.4.99.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"4-carboxymethyl-4-methylbutenolide mutase"}}}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"20061479","source":"PubMed"}],"value":"Isomerase involved in the degradation of 4-methylsalicylate and 5-methylsalicylate (PubMed:20061479). Catalyzes the isomerization of the dead-end metabolite 4-methylmuconolactone (4-ML) to 3-methylmuconolactone (3-ML), which can then be further degraded through a modified 3-oxoadipate pathway (PubMed:19801657). Can also use 1-methylbislactone but not 3-methyl-cis,cis-muconate (PubMed:19801657)"}]}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"19801657","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:19238"}}],"reaction":{"ecNumber":"5.4.99.14","evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"}],"name":"4-methylmuconolactone = 3-methylmuconolactone","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19237"},{"database":"ChEBI","id":"CHEBI:57883"},{"database":"ChEBI","id":"CHEBI:57888"}]}}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C5MR76.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:31.044476+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"19801657","source":"PubMed"}],"id":"GO:0047469","properties":[{"key":"GoTerm","value":"F:4-carboxymethyl-4-methylbutenolide mutase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `3d67557ecf827cb87e773519386698ecac17ac2714ab4e9390e7fdb2b8e1ed32`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 56-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
CC   -!- FUNCTION: Isomerase involved in the degradation of 4-methylsalicylate
CC       and 5-methylsalicylate (PubMed:20061479). Catalyzes the isomerization
CC       of the dead-end metabolite 4-methylmuconolactone (4-ML) to 3-
CC       methylmuconolactone (3-ML), which can then be further degraded through
CC       a modified 3-oxoadipate pathway (PubMed:19801657). Can also use 1-
CC       methylbislactone but not 3-methyl-cis,cis-muconate (PubMed:19801657).
CC       {ECO:0000269|PubMed:19801657, ECO:0000269|PubMed:20061479}.
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 63-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-methylmuconolactone = 3-methylmuconolactone;
CC         Xref=Rhea:RHEA:19237, ChEBI:CHEBI:57883, ChEBI:CHEBI:57888;
CC         EC=5.4.99.14; Evidence={ECO:0000269|PubMed:19801657};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:19238;
CC         Evidence={ECO:0000305|PubMed:19801657};
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C5MR76?format=txt&versions=66)  
**Locator:** `lines 104-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 1.  
**Retrieved:** 2026-11-02T04:27:34.227817+00:00.  

```text
DR   GO; GO:0047469; F:4-carboxymethyl-4-methylbutenolide mutase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `813b0f1c8060cf8b4b09f12d8d6ff0f15ff7f1c1b402841ea0a11592eb3069aa`.

### Evidence GO3

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

### Evidence GO4

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

### Evidence GO6

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
