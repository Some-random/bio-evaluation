# EC_number_0007

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 4.4.1.11

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIAVNSRNSLNADMTSLHPETLMVHGGMKGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHTLKDGDSAVYQRLWQPGVARFETALAGLEHAEEAVAFATGMAAMTAALLAAVSAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEADIASAIQDDTGLVIVETPANPSLDLVDLDSVVSAAGNVPVLVDNTFCTPVLQQPISHGAALVLHSATKYLGGHGDAMGGIIATNADWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLDAHPAISVVHYPGLKGQDPRGLLGRQMSGGGAMIAMELAGGFDAARSFVEHCNLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLADDLIAALDASRAAA

[Multiple Choices]
A. 4.3.1.24
B. 1.6.5.2
C. 3.2.2.5
D. 4.4.1.11
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt sequence annotated as L-methionine gamma-lyase, EC 4.4.1.11, with cited experimental evidence. Thus D is supported among the listed choices. The record also annotates homocysteine desulfhydrase activity as EC 4.4.1.2.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features might suggest a PLP-dependent enzyme and help separate it from the oxidoreductase and hydrolase choices, but they do not establish the precise substrate-specific EC activity asked for.


**Missing item-specific fact**

> The protein-specific catalytic activity and substrate specificity—particularly methionine gamma-lyase activity—are not provided in the question and require an annotation, homology-based identification, or experimental evidence.


**Reason**

> Selecting the exact complete EC number depends on protein-specific functional information absent from the input; recalling the exact protein or its database entry would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, only D matches the supported annotation. However, the protein is also annotated with EC 4.4.1.2 activity, which is not offered, so the wording could suggest a single EC even though the record reports more than one catalytic activity.


### Important caveats

- The reviewer-only sequence match supports applicability of the cited annotations, but those annotations were not available to the evaluated model.
- The cited database annotations associate both reactions with experimental evidence codes; the primary papers were not independently reviewed here.
- The evidence establishes support for D without implying that EC 4.4.1.11 is the protein's only annotated activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features might suggest a PLP-dependent enzyme and help separate it from the oxidoreductase and hydrolase choices, but they do not establish the precise substrate-specific EC activity asked for.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity and substrate specificity—particularly methionine gamma-lyase activity—are not provided in the question and require an annotation, homology-based identification, or experimental evidence.",
    "reason": "Selecting the exact complete EC number depends on protein-specific functional information absent from the input; recalling the exact protein or its database entry would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "EC_number_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as L-methionine gamma-lyase, EC 4.4.1.11, with cited experimental evidence. Thus D is supported among the listed choices. The record also annotates homocysteine desulfhydrase activity as EC 4.4.1.2."
  },
  "important_caveats": [
    "The reviewer-only sequence match supports applicability of the cited annotations, but those annotations were not available to the evaluated model.",
    "The cited database annotations associate both reactions with experimental evidence codes; the primary papers were not independently reviewed here.",
    "The evidence establishes support for D without implying that EC 4.4.1.11 is the protein's only annotated activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, only D matches the supported annotation. However, the protein is also annotated with EC 4.4.1.2 activity, which is not offered, so the wording could suggest a single EC even though the record reports more than one catalytic activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as L-methionine gamma-lyase, EC 4.4.1.11, with cited experimental evidence. Thus D is supported among the listed choices. The record also annotates homocysteine desulfhydrase activity as EC 4.4.1.2.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features might suggest a PLP-dependent enzyme and help separate it from the oxidoreductase and hydrolase choices, but they do not establish the precise substrate-specific EC activity asked for.",
    "missing_item_specific_fact": "The protein-specific catalytic activity and substrate specificity—particularly methionine gamma-lyase activity—are not provided in the question and require an annotation, homology-based identification, or experimental evidence.",
    "reason": "Selecting the exact complete EC number depends on protein-specific functional information absent from the input; recalling the exact protein or its database entry would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, only D matches the supported annotation. However, the protein is also annotated with EC 4.4.1.2 activity, which is not offered, so the wording could suggest a single EC even though the record reports more than one catalytic activity."
  },
  "important_caveats": [
    "The reviewer-only sequence match supports applicability of the cited annotations, but those annotations were not available to the evaluated model.",
    "The cited database annotations associate both reactions with experimental evidence codes; the primary papers were not independently reviewed here.",
    "The evidence establishes support for D without implying that EC 4.4.1.11 is the protein's only annotated activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A2H1K3G9 (MEGL_BREAU, L-methionine gamma-lyase from Brevibacterium aurantiacum) is annotated with EC 4.4.1.11 as the recommended name, supported by experimental evidence (ECO:0000269) from PubMed:30940696 and PubMed:9726878. The catalytic reaction L-methionine + H2O → methanethiol + 2-oxobutanoate + NH4+ is confirmed with Rhea cross-references. The benchmark sequence matches the UniProt sequence exactly (406 aa, SHA256 match). The alternative EC 4.4.1.2 (homocysteine desulfhydrase) is listed as a secondary activity but the primary/recommended EC is 4.4.1.11.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence (~406 aa) exhibits hallmarks of the aspartate aminotransferase/PLP-dependent superfamily fold (conserved lysine for PLP Schiff-base formation, characteristic domain architecture with N-terminal and C-terminal lobes, conserved motif patterns). This fold is incompatible with EC 1.6.5.2 (NADH:ubiquinone oxidoreductase, a large membrane-associated oxidoreductase with FMN/NADH-binding domains) and EC 3.2.2.5 (nucleosidase, a glycosyl hydrolase with completely different fold). Among the remaining lyase options, the aminotransferase-fold PLP enzymes that catalyze β-elimination on sulfur-containing amino acids (C-S lyases, EC 4.4.1.x) have distinct active-site residue configurations compared to C-N bond-cleaving hydro-lyases (EC 4.3.1.x). The sequence's overall architecture and residue conservation pattern aligns with C-S lyase members of the aminotransferase superfamily rather than C-N lyases.


**Missing item-specific fact**

> The precise assignment to EC 4.4.1.11 (methionine gamma-lyase) versus other C-S lyases in the same fold (e.g., cystathionine beta-lyase EC 4.4.1.8) requires knowledge of specific substrate-binding residues. However, no other C-S lyase EC number is offered as a distractor, so the fold-level argument suffices to select among the given choices.


**Reason**

> The aminotransferase/PLP fold identification provides a concrete biological argument to eliminate the oxidoreductase (1.6.5.2) and hydrolase (3.2.2.5) options. The distinction between C-S lyases (4.4.1.x) and C-N lyases (4.3.1.x) within the same fold is a matter of general enzymology regarding active-site geometry and catalytic residue arrangement. While the final precise EC assignment has some specificity component, the provided choices are sufficiently separated by fold class to allow meaningful reasoning-based discrimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC classes (oxidoreductase, hydrolase, lyase) and two lyase subclasses (C-S vs C-N). The fold analysis clearly eliminates 1.6.5.2 and 3.2.2.5. EC 4.3.1.24 is an obscure or possibly deprecated C-N hydro-lyase entry that does not match the observed aminotransferase-fold C-S lyase architecture. No other C-S lyase EC number is offered, so 4.4.1.11 is the uniquely defensible choice among the given options.


### Important caveats

- The enzyme also catalyzes EC 4.4.1.2 (homocysteine desulfhydrase) as a secondary activity, but this EC number is not among the choices.
- The UniProt annotation is experimentally supported (ECO:0000269) from two independent publications, not merely computational prediction.
- The identity of the protein as MEGL_BREAU was established via reviewer-only metadata; the evaluated model only sees the raw sequence.
- EC 4.3.1.24 may be a non-standard or deleted EC number, which would make it an easier distractor to eliminate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence (~406 aa) exhibits hallmarks of the aspartate aminotransferase/PLP-dependent superfamily fold (conserved lysine for PLP Schiff-base formation, characteristic domain architecture with N-terminal and C-terminal lobes, conserved motif patterns). This fold is incompatible with EC 1.6.5.2 (NADH:ubiquinone oxidoreductase, a large membrane-associated oxidoreductase with FMN/NADH-binding domains) and EC 3.2.2.5 (nucleosidase, a glycosyl hydrolase with completely different fold). Among the remaining lyase options, the aminotransferase-fold PLP enzymes that catalyze β-elimination on sulfur-containing amino acids (C-S lyases, EC 4.4.1.x) have distinct active-site residue configurations compared to C-N bond-cleaving hydro-lyases (EC 4.3.1.x). The sequence's overall architecture and residue conservation pattern aligns with C-S lyase members of the aminotransferase superfamily rather than C-N lyases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise assignment to EC 4.4.1.11 (methionine gamma-lyase) versus other C-S lyases in the same fold (e.g., cystathionine beta-lyase EC 4.4.1.8) requires knowledge of specific substrate-binding residues. However, no other C-S lyase EC number is offered as a distractor, so the fold-level argument suffices to select among the given choices.",
    "reason": "The aminotransferase/PLP fold identification provides a concrete biological argument to eliminate the oxidoreductase (1.6.5.2) and hydrolase (3.2.2.5) options. The distinction between C-S lyases (4.4.1.x) and C-N lyases (4.3.1.x) within the same fold is a matter of general enzymology regarding active-site geometry and catalytic residue arrangement. While the final precise EC assignment has some specificity component, the provided choices are sufficiently separated by fold class to allow meaningful reasoning-based discrimination."
  },
  "case_id": "EC_number_0007",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A2H1K3G9 (MEGL_BREAU, L-methionine gamma-lyase from Brevibacterium aurantiacum) is annotated with EC 4.4.1.11 as the recommended name, supported by experimental evidence (ECO:0000269) from PubMed:30940696 and PubMed:9726878. The catalytic reaction L-methionine + H2O → methanethiol + 2-oxobutanoate + NH4+ is confirmed with Rhea cross-references. The benchmark sequence matches the UniProt sequence exactly (406 aa, SHA256 match). The alternative EC 4.4.1.2 (homocysteine desulfhydrase) is listed as a secondary activity but the primary/recommended EC is 4.4.1.11."
  },
  "important_caveats": [
    "The enzyme also catalyzes EC 4.4.1.2 (homocysteine desulfhydrase) as a secondary activity, but this EC number is not among the choices.",
    "The UniProt annotation is experimentally supported (ECO:0000269) from two independent publications, not merely computational prediction.",
    "The identity of the protein as MEGL_BREAU was established via reviewer-only metadata; the evaluated model only sees the raw sequence.",
    "EC 4.3.1.24 may be a non-standard or deleted EC number, which would make it an easier distractor to eliminate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (oxidoreductase, hydrolase, lyase) and two lyase subclasses (C-S vs C-N). The fold analysis clearly eliminates 1.6.5.2 and 3.2.2.5. EC 4.3.1.24 is an obscure or possibly deprecated C-N hydro-lyase entry that does not match the observed aminotransferase-fold C-S lyase architecture. No other C-S lyase EC number is offered, so 4.4.1.11 is the uniquely defensible choice among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0007",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A2H1K3G9 (MEGL_BREAU, L-methionine gamma-lyase from Brevibacterium aurantiacum) is annotated with EC 4.4.1.11 as the recommended name, supported by experimental evidence (ECO:0000269) from PubMed:30940696 and PubMed:9726878. The catalytic reaction L-methionine + H2O → methanethiol + 2-oxobutanoate + NH4+ is confirmed with Rhea cross-references. The benchmark sequence matches the UniProt sequence exactly (406 aa, SHA256 match). The alternative EC 4.4.1.2 (homocysteine desulfhydrase) is listed as a secondary activity but the primary/recommended EC is 4.4.1.11.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H1", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence (~406 aa) exhibits hallmarks of the aspartate aminotransferase/PLP-dependent superfamily fold (conserved lysine for PLP Schiff-base formation, characteristic domain architecture with N-terminal and C-terminal lobes, conserved motif patterns). This fold is incompatible with EC 1.6.5.2 (NADH:ubiquinone oxidoreductase, a large membrane-associated oxidoreductase with FMN/NADH-binding domains) and EC 3.2.2.5 (nucleosidase, a glycosyl hydrolase with completely different fold). Among the remaining lyase options, the aminotransferase-fold PLP enzymes that catalyze β-elimination on sulfur-containing amino acids (C-S lyases, EC 4.4.1.x) have distinct active-site residue configurations compared to C-N bond-cleaving hydro-lyases (EC 4.3.1.x). The sequence's overall architecture and residue conservation pattern aligns with C-S lyase members of the aminotransferase superfamily rather than C-N lyases.",
    "missing_item_specific_fact": "The precise assignment to EC 4.4.1.11 (methionine gamma-lyase) versus other C-S lyases in the same fold (e.g., cystathionine beta-lyase EC 4.4.1.8) requires knowledge of specific substrate-binding residues. However, no other C-S lyase EC number is offered as a distractor, so the fold-level argument suffices to select among the given choices.",
    "reason": "The aminotransferase/PLP fold identification provides a concrete biological argument to eliminate the oxidoreductase (1.6.5.2) and hydrolase (3.2.2.5) options. The distinction between C-S lyases (4.4.1.x) and C-N lyases (4.3.1.x) within the same fold is a matter of general enzymology regarding active-site geometry and catalytic residue arrangement. While the final precise EC assignment has some specificity component, the provided choices are sufficiently separated by fold class to allow meaningful reasoning-based discrimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC classes (oxidoreductase, hydrolase, lyase) and two lyase subclasses (C-S vs C-N). The fold analysis clearly eliminates 1.6.5.2 and 3.2.2.5. EC 4.3.1.24 is an obscure or possibly deprecated C-N hydro-lyase entry that does not match the observed aminotransferase-fold C-S lyase architecture. No other C-S lyase EC number is offered, so 4.4.1.11 is the uniquely defensible choice among the given options."
  },
  "important_caveats": [
    "The enzyme also catalyzes EC 4.4.1.2 (homocysteine desulfhydrase) as a secondary activity, but this EC number is not among the choices.",
    "The UniProt annotation is experimentally supported (ECO:0000269) from two independent publications, not merely computational prediction.",
    "The identity of the protein as MEGL_BREAU was established via reviewer-only metadata; the evaluated model only sees the raw sequence.",
    "EC 4.3.1.24 may be a non-standard or deleted EC number, which would make it an easier distractor to eliminate."
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

**Accession:** `A0A2H1K3G9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
"A0A2H1K3G9"
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"}],"value":"4.4.1.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30940696","source":"PubMed"}],"value":"Homocysteine desulfhydrase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30940696","source":"PubMed"}],"value":"MGL-BL929"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"}],"value":"4.4.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9726878","source":"PubMed"}],"value":"L-methionine gamma-lyase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9726878","source":"PubMed"}],"value":"MGL"}]}}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23801"}}],"reaction":{"ecNumber":"4.4.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"}],"name":"L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23800"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:16007"},{"database":"ChEBI","id":"CHEBI:16763"},{"database":"ChEBI","id":"CHEBI:28938"},{"database":"ChEBI","id":"CHEBI:57844"}]}}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"30940696","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:14502"}}],"reaction":{"ecNumber":"4.4.1.2","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"}],"name":"L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide + NH4(+) + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14501"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16763"},{"database":"ChEBI","id":"CHEBI:28938"},{"database":"ChEBI","id":"CHEBI:29919"},{"database":"ChEBI","id":"CHEBI:58199"}]}}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"citation":{"authors":["Dias B.","Weimer B."],"citationCrossReferences":[{"database":"PubMed","id":"9726878"},{"database":"DOI","id":"10.1128/aem.64.9.3327-3331.1998"}],"citationType":"journal article","firstPage":"3327","id":"9726878","journal":"Appl. Environ. Microbiol.","lastPage":"3331","publicationDate":"1998","title":"Purification and characterization of L-methionine gamma-lyase from brevibacterium linens BL2.","volume":"64"},"referenceComments":[{"type":"STRAIN","value":"BL2"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBSTRATE SPECIFICITY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION","SUBUNIT"]}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"citation":{"authors":["Machover D.","Rossi L.","Hamelin J.","Desterke C.","Goldschmidt E.","Chadefaux-Vekemans B.","Bonnarme P.","Briozzo P.","Kopecny D.","Pierige F.","Magnani M.","Mollicone R.","Haghighi-Rad F.","Gaston-Mathe Y.","Dairou J.","Boucheix C.","Saffroy R."],"citationCrossReferences":[{"database":"PubMed","id":"30940696"},{"database":"DOI","id":"10.1124/jpet.119.256537"}],"citationType":"journal article","firstPage":"489","id":"30940696","journal":"J. Pharmacol. Exp. Ther.","lastPage":"502","publicationDate":"2019","title":"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for Sustained L-Methionine Elimination.","volume":"369"},"referenceComments":[{"type":"STRAIN","value":"ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB 8546 / KC"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBSTRATE SPECIFICITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","BIOTECHNOLOGY"]}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 1-19`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
ID   MEGL_BREAU              Reviewed;         406 AA.
AC   A0A2H1K3G9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   31-JAN-2018, sequence version 1.
DT   28-JAN-2026, entry version 32.
DE   RecName: Full=L-methionine gamma-lyase {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};
DE            Short=MGL {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};
DE            EC=4.4.1.11 {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};
DE   AltName: Full=Homocysteine desulfhydrase {ECO:0000303|PubMed:30940696};
DE            EC=4.4.1.2 {ECO:0000269|PubMed:30940696};
DE   AltName: Full=MGL-BL929 {ECO:0000303|PubMed:30940696};
GN   ORFNames=BAUR9175_03070 {ECO:0000312|EMBL:SMX94104.1},
GN   BAUR920_03040 {ECO:0000312|EMBL:SMX97377.1},
GN   BAURA63_02933 {ECO:0000312|EMBL:SMX94451.1},
GN   BAURA86_00394 {ECO:0000312|EMBL:SMX72154.1};
OS   Brevibacterium aurantiacum.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales;
OC   Brevibacteriaceae; Brevibacterium.
OX   NCBI_TaxID=273384;
```

Source SHA-256: `9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 6-11`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
DE   RecName: Full=L-methionine gamma-lyase {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};
DE            Short=MGL {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};
DE            EC=4.4.1.11 {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};
DE   AltName: Full=Homocysteine desulfhydrase {ECO:0000303|PubMed:30940696};
DE            EC=4.4.1.2 {ECO:0000269|PubMed:30940696};
DE   AltName: Full=MGL-BL929 {ECO:0000303|PubMed:30940696};
```

Source SHA-256: `9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 60-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+);
CC         Xref=Rhea:RHEA:23800, ChEBI:CHEBI:15377, ChEBI:CHEBI:16007,
CC         ChEBI:CHEBI:16763, ChEBI:CHEBI:28938, ChEBI:CHEBI:57844; EC=4.4.1.11;
CC         Evidence={ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23801;
CC         Evidence={ECO:0000269|PubMed:30940696};
```

Source SHA-256: `9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 67-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide +
CC         NH4(+) + H(+); Xref=Rhea:RHEA:14501, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16763, ChEBI:CHEBI:28938,
CC         ChEBI:CHEBI:29919, ChEBI:CHEBI:58199; EC=4.4.1.2;
CC         Evidence={ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14502;
CC         Evidence={ECO:0000305|PubMed:30940696};
```

Source SHA-256: `9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 7. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
