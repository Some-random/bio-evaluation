# GO_molecular_function_0078

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — protein serine/threonine phosphatase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRTCGTSSEGQDECCLYGLSAMQGWRISMEDAHAAVLDLQAKSTGGSEKPTDPDKRLAFFGVYDGHGGDKVALFAGENVHKIVAKQEAFAKGDIEQALKDGFLATDRAILEDPKYEEEVSGCTAAVSVISKNKIWVANAGDSRSVLGVKGRAKPLSFDHKPQNEGEKARISAAGGFVDFGRVNGNLALSRAIGDFEFKKSPELSPEQQIVTAYPDVTVHEVTDDDEFLVIACDGIWDCQSSQSVVEFVRRGIAAKQELYRICENMMDNCLASNSETGGVGCDNMTMIIIGLLNGKTKEEWYNQISERVANGDGPCAPPEYGKSEFRGPGIRNQFEETPDNYDLENDRSRGFSVRSGRIILLGDGTELIPEQNDEELFDQREENRDVTNHLQHDKAEETSTAANLSESPSSANKNSSGSGTEATEKSASS

[Multiple Choices]
A. protein serine/threonine phosphatase activity
B. NAD+ synthase (glutamine-hydrolyzing) activity
C. glycosyltransferase activity
D. structural molecule activity
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

> The exact sequence matches the 429-aa UniProt entry for a PP2C homolog. Its annotated catalytic activity is EC 3.1.3.16, which covers serine/threonine protein phosphatase activity; the record also reports dephosphorylation of sakA with a literature evidence code. The catalytic annotation includes computational ProRule evidence, so it should not be mistaken for a direct enzyme assay.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains an Asp/His-rich motif such as DGHGGD and other conserved-looking acidic motifs consistent with a metal-dependent PP2C phosphatase domain. That provides a meaningful family-level basis for choosing phosphatase activity over NAD+ synthesis, glycosyl transfer, or structural activity.


**Missing item-specific fact**

> The exact protein identity and its experimentally reported substrate are not supplied; those would be needed to establish the specific annotation independently of sequence-based family inference.


**Reason**

> The choices are broad enough that recognizable PP2C-family sequence features meaningfully distinguish A. The reviewer-only database annotation supports the key but is not necessary to make that family-level inference from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is comparably supported by the sequence features; the options represent distinct functional classes.


### Important caveats

- The exact sequence match and protein-specific database annotation are reviewer-only evidence, not information given to the evaluated model.
- The catalytic activity annotation includes computational and similarity-based evidence; the cited literature annotation reports sakA dephosphorylation, but the excerpts do not independently establish a purified-enzyme assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains an Asp/His-rich motif such as DGHGGD and other conserved-looking acidic motifs consistent with a metal-dependent PP2C phosphatase domain. That provides a meaningful family-level basis for choosing phosphatase activity over NAD+ synthesis, glycosyl transfer, or structural activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein identity and its experimentally reported substrate are not supplied; those would be needed to establish the specific annotation independently of sequence-based family inference.",
    "reason": "The choices are broad enough that recognizable PP2C-family sequence features meaningfully distinguish A. The reviewer-only database annotation supports the key but is not necessary to make that family-level inference from the input."
  },
  "case_id": "GO_molecular_function_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C9",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the 429-aa UniProt entry for a PP2C homolog. Its annotated catalytic activity is EC 3.1.3.16, which covers serine/threonine protein phosphatase activity; the record also reports dephosphorylation of sakA with a literature evidence code. The catalytic annotation includes computational ProRule evidence, so it should not be mistaken for a direct enzyme assay."
  },
  "important_caveats": [
    "The exact sequence match and protein-specific database annotation are reviewer-only evidence, not information given to the evaluated model.",
    "The catalytic activity annotation includes computational and similarity-based evidence; the cited literature annotation reports sakA dephosphorylation, but the excerpts do not independently establish a purified-enzyme assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence features; the options represent distinct functional classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the 429-aa UniProt entry for a PP2C homolog. Its annotated catalytic activity is EC 3.1.3.16, which covers serine/threonine protein phosphatase activity; the record also reports dephosphorylation of sakA with a literature evidence code. The catalytic annotation includes computational ProRule evidence, so it should not be mistaken for a direct enzyme assay.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C9", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains an Asp/His-rich motif such as DGHGGD and other conserved-looking acidic motifs consistent with a metal-dependent PP2C phosphatase domain. That provides a meaningful family-level basis for choosing phosphatase activity over NAD+ synthesis, glycosyl transfer, or structural activity.",
    "missing_item_specific_fact": "The exact protein identity and its experimentally reported substrate are not supplied; those would be needed to establish the specific annotation independently of sequence-based family inference.",
    "reason": "The choices are broad enough that recognizable PP2C-family sequence features meaningfully distinguish A. The reviewer-only database annotation supports the key but is not necessary to make that family-level inference from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence features; the options represent distinct functional classes."
  },
  "important_caveats": [
    "The exact sequence match and protein-specific database annotation are reviewer-only evidence, not information given to the evaluated model.",
    "The catalytic activity annotation includes computational and similarity-based evidence; the cited literature annotation reports sakA dephosphorylation, but the excerpts do not independently establish a purified-enzyme assay."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WTH5 (PP2C2_ASPFU) is annotated as 'Protein phosphatase 2C homolog 2' with EC 3.1.3.16. The catalytic activity comments explicitly describe dephosphorylation of O-phospho-L-seryl-&#91;protein&#93; and O-phospho-L-threonyl-&#91;protein&#93;, matching GO:0004722 (protein serine/threonine phosphatase activity). GO:0004722 lists 'protein phosphatase type 2C activity' as a NARROW synonym. Experimental evidence (PubMed:25597841) demonstrates dephosphorylation of sakA. The sequence matches the UniProt entry exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H7](#evidence-h7), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains multiple well-characterized PP2C-family catalytic motifs: the DxHG motif ('DGHGG' at ~residue 60), the PP2C signature 'GDSRS' (~residue 130), 'GDFEF' (~residue 195), the catalytic 'GIRNQ' region (~residue 280), and 'GRIILLGDG' (~residue 300). These motifs are hallmarks of the PP2C (protein phosphatase 2C) family, which catalyzes Mg2+-dependent hydrolysis of phosphoserine/phosphothreonine from proteins. A knowledgeable bioinformatician can identify these motifs in the raw sequence and infer serine/threonine phosphatase activity without database lookup. None of the distractor options (NAD+ synthase, glycosyltransferase, structural molecule) have corresponding motifs in the sequence.


**Missing item-specific fact**

> None strictly required. Recognition of PP2C-family motifs and their functional implication is general protein-family knowledge. However, a model without specific PP2C motif training might struggle to distinguish this from other phosphatase families or unrelated activities purely from sequence.


**Reason**

> The PP2C signature motifs (DxHG, GDSRS, GDFEF, GIRNQ, GRIILLGDG) are well-documented in the literature and are present in the supplied sequence. Identifying these motifs and linking them to serine/threonine phosphatase activity constitutes a concrete biological argument from the sequence itself. The distractors lack any corresponding motifs. This is protein-family-level inference rather than item-specific database memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PP2C motifs unambiguously point to serine/threonine phosphatase activity. NAD+ synthase (glutamine amidotransferase domain), glycosyltransferase (PSPG or similar donor-binding motifs), and structural molecule activity (repetitive/coiled-coil architecture) have no supporting features in this sequence.


### Important caveats

- The GO annotation for GO:0004722 uses evidence codes ISS (Inferred from Sequence Similarity to P39966) and IBA (Inferred by Biological Aspect), not direct experimental assay on this exact protein. However, the function comment includes experimental evidence (PubMed:25597841) showing dephosphorylation of sakA.
- The EC number assignment relies partly on PROSITE-ProRule (ECO:0000255) and similarity to P39966 (ECO:0000250), i.e., computational inference, though the PROSITE rule is a well-validated family signature.
- Recognition of PP2C motifs is specialized but falls within general protein-family knowledge expected of a bioinformatician; it does not require memorizing the specific UniProt entry for Q4WTH5.
- The sequence-match between the benchmark input and UniProt Q4WTH5 is exact (SHA-256 confirmed), so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains multiple well-characterized PP2C-family catalytic motifs: the DxHG motif ('DGHGG' at ~residue 60), the PP2C signature 'GDSRS' (~residue 130), 'GDFEF' (~residue 195), the catalytic 'GIRNQ' region (~residue 280), and 'GRIILLGDG' (~residue 300). These motifs are hallmarks of the PP2C (protein phosphatase 2C) family, which catalyzes Mg2+-dependent hydrolysis of phosphoserine/phosphothreonine from proteins. A knowledgeable bioinformatician can identify these motifs in the raw sequence and infer serine/threonine phosphatase activity without database lookup. None of the distractor options (NAD+ synthase, glycosyltransferase, structural molecule) have corresponding motifs in the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Recognition of PP2C-family motifs and their functional implication is general protein-family knowledge. However, a model without specific PP2C motif training might struggle to distinguish this from other phosphatase families or unrelated activities purely from sequence.",
    "reason": "The PP2C signature motifs (DxHG, GDSRS, GDFEF, GIRNQ, GRIILLGDG) are well-documented in the literature and are present in the supplied sequence. Identifying these motifs and linking them to serine/threonine phosphatase activity constitutes a concrete biological argument from the sequence itself. The distractors lack any corresponding motifs. This is protein-family-level inference rather than item-specific database memorization."
  },
  "case_id": "GO_molecular_function_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C9",
      "H3",
      "H4",
      "H5",
      "H7",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WTH5 (PP2C2_ASPFU) is annotated as 'Protein phosphatase 2C homolog 2' with EC 3.1.3.16. The catalytic activity comments explicitly describe dephosphorylation of O-phospho-L-seryl-[protein] and O-phospho-L-threonyl-[protein], matching GO:0004722 (protein serine/threonine phosphatase activity). GO:0004722 lists 'protein phosphatase type 2C activity' as a NARROW synonym. Experimental evidence (PubMed:25597841) demonstrates dephosphorylation of sakA. The sequence matches the UniProt entry exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The GO annotation for GO:0004722 uses evidence codes ISS (Inferred from Sequence Similarity to P39966) and IBA (Inferred by Biological Aspect), not direct experimental assay on this exact protein. However, the function comment includes experimental evidence (PubMed:25597841) showing dephosphorylation of sakA.",
    "The EC number assignment relies partly on PROSITE-ProRule (ECO:0000255) and similarity to P39966 (ECO:0000250), i.e., computational inference, though the PROSITE rule is a well-validated family signature.",
    "Recognition of PP2C motifs is specialized but falls within general protein-family knowledge expected of a bioinformatician; it does not require memorizing the specific UniProt entry for Q4WTH5.",
    "The sequence-match between the benchmark input and UniProt Q4WTH5 is exact (SHA-256 confirmed), so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP2C motifs unambiguously point to serine/threonine phosphatase activity. NAD+ synthase (glutamine amidotransferase domain), glycosyltransferase (PSPG or similar donor-binding motifs), and structural molecule activity (repetitive/coiled-coil architecture) have no supporting features in this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WTH5 (PP2C2_ASPFU) is annotated as 'Protein phosphatase 2C homolog 2' with EC 3.1.3.16. The catalytic activity comments explicitly describe dephosphorylation of O-phospho-L-seryl-[protein] and O-phospho-L-threonyl-[protein], matching GO:0004722 (protein serine/threonine phosphatase activity). GO:0004722 lists 'protein phosphatase type 2C activity' as a NARROW synonym. Experimental evidence (PubMed:25597841) demonstrates dephosphorylation of sakA. The sequence matches the UniProt entry exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C9", "H3", "H4", "H5", "H7", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains multiple well-characterized PP2C-family catalytic motifs: the DxHG motif ('DGHGG' at ~residue 60), the PP2C signature 'GDSRS' (~residue 130), 'GDFEF' (~residue 195), the catalytic 'GIRNQ' region (~residue 280), and 'GRIILLGDG' (~residue 300). These motifs are hallmarks of the PP2C (protein phosphatase 2C) family, which catalyzes Mg2+-dependent hydrolysis of phosphoserine/phosphothreonine from proteins. A knowledgeable bioinformatician can identify these motifs in the raw sequence and infer serine/threonine phosphatase activity without database lookup. None of the distractor options (NAD+ synthase, glycosyltransferase, structural molecule) have corresponding motifs in the sequence.",
    "missing_item_specific_fact": "None strictly required. Recognition of PP2C-family motifs and their functional implication is general protein-family knowledge. However, a model without specific PP2C motif training might struggle to distinguish this from other phosphatase families or unrelated activities purely from sequence.",
    "reason": "The PP2C signature motifs (DxHG, GDSRS, GDFEF, GIRNQ, GRIILLGDG) are well-documented in the literature and are present in the supplied sequence. Identifying these motifs and linking them to serine/threonine phosphatase activity constitutes a concrete biological argument from the sequence itself. The distractors lack any corresponding motifs. This is protein-family-level inference rather than item-specific database memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP2C motifs unambiguously point to serine/threonine phosphatase activity. NAD+ synthase (glutamine amidotransferase domain), glycosyltransferase (PSPG or similar donor-binding motifs), and structural molecule activity (repetitive/coiled-coil architecture) have no supporting features in this sequence."
  },
  "important_caveats": [
    "The GO annotation for GO:0004722 uses evidence codes ISS (Inferred from Sequence Similarity to P39966) and IBA (Inferred by Biological Aspect), not direct experimental assay on this exact protein. However, the function comment includes experimental evidence (PubMed:25597841) showing dephosphorylation of sakA.",
    "The EC number assignment relies partly on PROSITE-ProRule (ECO:0000255) and similarity to P39966 (ECO:0000250), i.e., computational inference, though the PROSITE rule is a well-validated family signature.",
    "Recognition of PP2C motifs is specialized but falls within general protein-family knowledge expected of a bioinformatician; it does not require memorizing the specific UniProt entry for Q4WTH5.",
    "The sequence-match between the benchmark input and UniProt Q4WTH5 is exact (SHA-256 confirmed), so the annotation applies directly to the supplied sequence."
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

**Accession:** `Q4WTH5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 119. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
"Q4WTH5"
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein phosphatase 2C homolog 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PP2C-2"}]}}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"25597841","source":"PubMed"}],"value":"Dephosphorylating regulator for many key proteins (By similarity). Dephosphorylates sakA, to negatively regulate the stress-activated p38MAPK cascade (PubMed:25597841)"}]}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01082","source":"PROSITE-ProRule"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:47005"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"name":"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:47004"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:61977"}]}}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WTH5.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:22.256463+00:00.  

```json
{"database":"GO","id":"GO:0004722","properties":[{"key":"GoTerm","value":"F:protein serine/threonine phosphatase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `f938bc341dcec6cecae47c9a46d2d7980c3f17520ab8f34ad6cb3420e7aa9484`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 51-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
CC   -!- FUNCTION: Dephosphorylating regulator for many key proteins (By
CC       similarity). Dephosphorylates sakA, to negatively regulate the stress-
CC       activated p38MAPK cascade (PubMed:25597841).
CC       {ECO:0000250|UniProtKB:P39966, ECO:0000269|PubMed:25597841}.
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 55-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16; Evidence={ECO:0000255|PROSITE-
CC         ProRule:PRU01082};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000305};
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 63-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:61977; EC=3.1.3.16;
CC         Evidence={ECO:0000250|UniProtKB:P39966};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;
CC         Evidence={ECO:0000250|UniProtKB:P39966};
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WTH5?format=txt&versions=119)  
**Locator:** `lines 115-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 1.  
**Retrieved:** 2026-11-01T06:28:37.090130+00:00.  

```text
DR   GO; GO:0004722; F:protein serine/threonine phosphatase activity; IBA:GO_Central.
```

Source SHA-256: `1422e4910ae5e5e06e93f448659a88f79da1861e03cba96d2a96852792edfd48`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 48538-48627`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004722
name: protein serine/threonine phosphatase activity
namespace: molecular_function
alt_id: GO:0000158
alt_id: GO:0000163
alt_id: GO:0004724
alt_id: GO:0008598
alt_id: GO:0008600
alt_id: GO:0015071
alt_id: GO:0030357
alt_id: GO:0030358
alt_id: GO:0030360
alt_id: GO:0030361
alt_id: GO:0106306
alt_id: GO:0106307
def: "Catalysis of the reaction: protein serine phosphate + H2O = protein serine + phosphate, and protein threonine phosphate + H2O = protein threonine + phosphate." [GOC:bf]
synonym: "magnesium-dependent protein serine/threonine phosphatase activity" RELATED []
synonym: "phosphatase I" NARROW []
synonym: "phosphatase II" NARROW []
synonym: "phosphatase III" NARROW []
synonym: "protein phosphatase type 1 activity" NARROW []
synonym: "protein phosphatase type 2A activity" NARROW []
synonym: "protein phosphatase type 2B activity" NARROW []
synonym: "protein phosphatase type 2C activity" NARROW []
synonym: "protein phosphatase-1" NARROW [EC:3.1.3.16]
synonym: "protein phosphatase-2A" NARROW [EC:3.1.3.16]
synonym: "protein phosphatase-2B" NARROW [EC:3.1.3.16]
synonym: "protein phosphatase-2C" NARROW [EC:3.1.3.16]
synonym: "protein serine phosphatase activity" NARROW []
synonym: "protein threonine phosphatase activity" NARROW []
synonym: "serine/threonine specific protein phosphatase activity" EXACT []
xref: EC:3.1.3.16
xref: MetaCyc:3.1.3.16-RXN
xref: Reactome:R-HSA-1295632 "PPA2A dephosphorylates SPRY2"
xref: Reactome:R-HSA-163568 "phosphorylated perilipin + H2O -> perilipin + orthophosphate"
xref: Reactome:R-HSA-163689 "PP2A complex dephosphorylates pChREBP (MLXIPL)"
xref: Reactome:R-HSA-163750 "PP2A complex dephosphorylates pPFKFB1"
xref: Reactome:R-HSA-1638821 "PP2A-B56 dephosphorylates centromeric cohesin"
xref: Reactome:R-HSA-199425 "PHLPP dephosphorylates S473 in AKT"
xref: Reactome:R-HSA-199959 "ERKs are inactivated by protein phosphatase 2A"
xref: Reactome:R-HSA-201787 "PPP3 complex dephosphorylates DARPP-32 on Thr34"
xref: Reactome:R-HSA-201790 "DARPP-32 is dephosphorylated on Thr75 by PP2A"
xref: Reactome:R-HSA-209055 "PPM1A dephosphorylates nuclear SMAD2/3"
xref: Reactome:R-HSA-2187401 "MTMR4 dephosphorylates SMAD2/3"
xref: Reactome:R-HSA-2995388 "PP2A dephosphorylates BANF1"
xref: Reactome:R-HSA-3002811 "Myosin phosphatase dephosphorylates PLK1"
xref: Reactome:R-HSA-3601585 "PP2A dephosphorylates AXIN, APC and CTNNB1 in the destruction complex"
xref: Reactome:R-HSA-380949 "AMPK is dephosphorylated"
xref: Reactome:R-HSA-4088141 "PP2A-PPP2R2A dephosphorylates FOXM1"
xref: Reactome:R-HSA-429730 "PPM1L dephosphorylates multiphospho-CERT1-2"
xref: Reactome:R-HSA-4419948 "CTDNEP1:CNEP1R1 dephosphorylates LPIN"
xref: Reactome:R-HSA-5672957 "PP2A dephosphorylates KSR1"
xref: Reactome:R-HSA-5672961 "PP2A dephosphorylates inactive RAFs"
xref: Reactome:R-HSA-5675431 "PP2A dephosphorylates RAF1"
xref: Reactome:R-HSA-5675433 "PP5 dephosphorylates RAF1 S338"
xref: Reactome:R-HSA-5679206 "MTMR14, MTMR3 dephosphorylate PI3P"
xref: Reactome:R-HSA-5683405 "PPP5C dephosphorylates TP53BP1"
xref: Reactome:R-HSA-5687758 "PPP4C:PPP4R2 dephosphorylates RPA2"
xref: Reactome:R-HSA-5692754 "CDC14A,B dephosphorylate p-3S,T MAPK6"
xref: Reactome:R-HSA-5694421 "PP6 dephosphorylates SEC24"
xref: Reactome:R-HSA-6792863 "PP2A-PP2R5C dephosphorylates MDM2"
xref: Reactome:R-HSA-6811504 "AKT1 dephosphorylation by PP2A-B56-beta,gamma"
xref: Reactome:R-HSA-74948 "PP2A dephosphorylates p-RHO to RHO"
xref: Reactome:R-HSA-8948139 "p-S13-FUNDC1 is dephosphorylated by PGAM5"
xref: Reactome:R-HSA-9619430 "PPM1E dephosphorylates CAMK4"
xref: Reactome:R-HSA-9619449 "PPM1F dephosphorylates p-T286-CaMKII"
xref: Reactome:R-HSA-9619467 "PPM1F dephosphorylates CAMK1"
xref: Reactome:R-HSA-9658445 "MRAS:SHOC2:PPP1CC dephosphorylates inactive RAFs"
xref: Reactome:R-HSA-9660536 "SHOC2 M173I disrupts the SHOC2:MRAS:PP1 complex"
xref: Reactome:R-HSA-9660538 "Mutant MRAS:SHOC2:PPP1CC complexes dephosphorylate inactive RAFs"
xref: Reactome:R-HSA-9686524 "PP6-PPP6R3 dephosphorylates TERF2"
xref: Reactome:R-HSA-9831948 "P:PP1 dephosphorylates M2-1"
xref: Reactome:R-HSA-9853385 "PPP1CC dephosphorylates PLK1"
xref: Reactome:R-HSA-9861725 "PGAM5 dodecamer dephosphorylates p-S336-ME1"
xref: Reactome:R-HSA-9865226 "PP2A dephosphorylates serine-127 of YAP1"
xref: Reactome:R-HSA-9865238 "PP2A dephosphorylates serine-715 of PDE4D5 in p-S715-PDE4D5:integrin alpha5:integrin beta1:fibronectin"
xref: Reactome:R-HSA-9912527 "H139Hfs13* PPM1K does not dephosphorylate BCKDH"
xref: Reactome:R-HSA-9970190 "PP1 dephosphorylates RNA Pol II"
xref: RHEA:12849
xref: RHEA:20629
xref: RHEA:47004
xref: RHEA:53988
is_a: GO:0004721 ! phosphoprotein phosphatase activity
property_value: skos:exactMatch EC:3.1.3.16
property_value: skos:narrowMatch RHEA:12849
property_value: skos:narrowMatch RHEA:20629
property_value: skos:narrowMatch RHEA:47004
property_value: skos:narrowMatch RHEA:53988

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
