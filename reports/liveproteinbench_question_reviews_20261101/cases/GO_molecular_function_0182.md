# GO_molecular_function_0182

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — phosphatase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASSDLEAATALKVQGNKAFGQHEWPTAVDFYTQAIAKYDREPSFFSNRAQAHIKLEAYGFAIADATKALELDPAYTKAYWRRALANTAILNYKDALRDFKVVAKREPNNRDAKVKLADCEKLVRRMEFEKAIEVGDPPSAFEDLDIDAIAVDDSYDGVRLEKEMTQEFIDDMIERFKNGKKIHRKYAFQIVKAVKDIVYAEPTMVEIGVDQGTKLTVCGDTHGQFFDLLEIFRLNGYPSEKHAYLFNGDFVDRGSWSTEIALLLYAYKWLRPNGIFLNRGNHETDDMNKVYGFEGECKAKYNERMFKVFSESFSALPLATLIGNKYLVLHGGLFSDDNTSLDDIRKLDRHNQRQPGQQGLMMEMLWTDPQTEPGRGPSKRGVGLQFGPDVTKRFCEKNGLEAIIRSHEVRMEGYEVEHDGRCITVFSAPKYCDTTENKGAFINVGPELKLDFQVFEAVPHPDIKPMAYAQNSIMSMM

[Multiple Choices]
A. transmembrane transporter activity
B. mechanosensitive monoatomic ion channel activity
C. peroxidase inhibitor activity
D. phosphatase activity
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

> The supplied sequence exactly matches the UniProt entry for an Aspergillus oryzae serine/threonine-protein phosphatase. The entry records protein dephosphorylation catalytic activity and a phosphatase-activity GO annotation with experimental-assay evidence; the catalytic reaction is linked to a cited publication.

Citations as saved: [C1](#evidence-c1), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a soluble protein without a transmembrane segment and has a phosphatase-like catalytic region, including conserved histidine/aspartate-rich motifs (for example, GDTHG and HGG). These features make phosphatase activity a defensible sequence-based inference and distinguish D from membrane transport or channel activity; peroxidase inhibition is not suggested by the sequence.


**Missing item-specific fact**

> No item-specific fact is essential for selecting the broad phosphatase category among these choices, though identifying the precise protein and its substrate specificity would require additional evidence.


**Reason**

> A characteristic catalytic-region pattern provides a concrete biological basis for selecting phosphatase activity. This is more than identification of the exact sequence or reliance on a predictor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The broad phosphatase category is supported by the sequence and is consistent with the matched entry's catalytic activity. The other options describe functions inconsistent with the apparent soluble enzyme.


### Important caveats

- The reviewer-only database evidence was not available to the model answering the original question.
- The matched entry's current and historical sequence versions are identical, but the author's exact annotation snapshot is unknown.
- The entry's protein-name annotation is partly transferred by similarity; the cited catalytic-activity record and GO annotation provide additional support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble protein without a transmembrane segment and has a phosphatase-like catalytic region, including conserved histidine/aspartate-rich motifs (for example, GDTHG and HGG). These features make phosphatase activity a defensible sequence-based inference and distinguish D from membrane transport or channel activity; peroxidase inhibition is not suggested by the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is essential for selecting the broad phosphatase category among these choices, though identifying the precise protein and its substrate specificity would require additional evidence.",
    "reason": "A characteristic catalytic-region pattern provides a concrete biological basis for selecting phosphatase activity. This is more than identification of the exact sequence or reliance on a predictor."
  },
  "case_id": "GO_molecular_function_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C6",
      "C8",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for an Aspergillus oryzae serine/threonine-protein phosphatase. The entry records protein dephosphorylation catalytic activity and a phosphatase-activity GO annotation with experimental-assay evidence; the catalytic reaction is linked to a cited publication."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the model answering the original question.",
    "The matched entry's current and historical sequence versions are identical, but the author's exact annotation snapshot is unknown.",
    "The entry's protein-name annotation is partly transferred by similarity; the cited catalytic-activity record and GO annotation provide additional support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad phosphatase category is supported by the sequence and is consistent with the matched entry's catalytic activity. The other options describe functions inconsistent with the apparent soluble enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for an Aspergillus oryzae serine/threonine-protein phosphatase. The entry records protein dephosphorylation catalytic activity and a phosphatase-activity GO annotation with experimental-assay evidence; the catalytic reaction is linked to a cited publication.",
    "evidence_ids": ["C1", "C6", "C8", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a soluble protein without a transmembrane segment and has a phosphatase-like catalytic region, including conserved histidine/aspartate-rich motifs (for example, GDTHG and HGG). These features make phosphatase activity a defensible sequence-based inference and distinguish D from membrane transport or channel activity; peroxidase inhibition is not suggested by the sequence.",
    "missing_item_specific_fact": "No item-specific fact is essential for selecting the broad phosphatase category among these choices, though identifying the precise protein and its substrate specificity would require additional evidence.",
    "reason": "A characteristic catalytic-region pattern provides a concrete biological basis for selecting phosphatase activity. This is more than identification of the exact sequence or reliance on a predictor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad phosphatase category is supported by the sequence and is consistent with the matched entry's catalytic activity. The other options describe functions inconsistent with the apparent soluble enzyme."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available to the model answering the original question.",
    "The matched entry's current and historical sequence versions are identical, but the author's exact annotation snapshot is unknown.",
    "The entry's protein-name annotation is partly transferred by similarity; the cited catalytic-activity record and GO annotation provide additional support."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2U919 (PPP5_ASPOR, Serine/threonine-protein phosphatase T) is annotated with GO:0016791 (phosphatase activity) at IDA evidence level from PubMed:17475320 (C8, H7), and with EC 3.1.3.16 catalytic reactions for O-phospho-L-seryl and O-phospho-L-threonyl dephosphorylation (C6, C7, H4, H5). The protein name, function comment, and catalytic activity are all consistent with phosphatase activity. The EC assignment is supported by ECO:0000305 (curator inference from PubMed), and the GO IDA annotation confirms direct experimental assay support.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H4](#evidence-h4), [H5](#evidence-h5), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark PP2C-like catalytic motifs of the PPP5 phosphatase family: a 'GDG' metal-binding motif, the highly conserved 'HGGLFSDD' signature of the PP2C-like catalytic domain, and clustered Asp/His metal-coordinating residues. The N-terminal region displays TPR (tetratricopeptide repeat) architecture (LxxLxxA patterns), which is characteristic of PPP5-family serine/threonine phosphatases. These features are inconsistent with transmembrane transporters (A) or mechanosensitive ion channels (B), which require multiple hydrophobic transmembrane helices absent from this sequence, and with peroxidase inhibitors (C), which require peroxidase-binding structural domains. The presence of a PP2C-like catalytic core with metal-binding residues is a concrete, generalizable biological argument for phosphatase activity.


**Missing item-specific fact**

> None critical. While exact identification of the PPP5 family from sequence requires familiarity with PP2C-like motifs, the motifs themselves (HGGLFSDD, GDG, metal-binding residues) are well-known diagnostic features in protein biochemistry and are present in the supplied sequence.


**Reason**

> A model with general knowledge of protein domain architecture can identify the PP2C-like catalytic motifs and TPR repeats in the sequence, distinguishing phosphatase activity from membrane transport (no TM helices present) and peroxidase inhibition (no peroxidase-binding fold). This constitutes a defensible biological argument from the sequence rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular functions (transport, channel, inhibitor, enzyme catalysis). The sequence lacks transmembrane helices (ruling out A and B), lacks peroxidase-binding structural features (ruling out C), and contains distinctive PP2C-like catalytic motifs supporting D. No other option is defensible.


### Important caveats

- The GO:0016791 annotation is IDA (direct assay) from PubMed:17475320, providing experimental support, while the protein name and function comment are partly based on similarity to P53043 (ECO:0000250).
- The more specific GO term GO:0004722 (protein serine/threonine phosphatase activity) is also annotated (IEA:UniProtKB-EC), but the broader GO:0016791 is the offered option and is correct as a parent term.
- Sequence identification of PPP5-family motifs requires specialized bioinformatics knowledge; while this constitutes reasoning from general biological principles, it is at the boundary of expert pattern recognition.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model; the assessment of reasoning support is based on whether the motifs are identifiable from the sequence itself.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark PP2C-like catalytic motifs of the PPP5 phosphatase family: a 'GDG' metal-binding motif, the highly conserved 'HGGLFSDD' signature of the PP2C-like catalytic domain, and clustered Asp/His metal-coordinating residues. The N-terminal region displays TPR (tetratricopeptide repeat) architecture (LxxLxxA patterns), which is characteristic of PPP5-family serine/threonine phosphatases. These features are inconsistent with transmembrane transporters (A) or mechanosensitive ion channels (B), which require multiple hydrophobic transmembrane helices absent from this sequence, and with peroxidase inhibitors (C), which require peroxidase-binding structural domains. The presence of a PP2C-like catalytic core with metal-binding residues is a concrete, generalizable biological argument for phosphatase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While exact identification of the PPP5 family from sequence requires familiarity with PP2C-like motifs, the motifs themselves (HGGLFSDD, GDG, metal-binding residues) are well-known diagnostic features in protein biochemistry and are present in the supplied sequence.",
    "reason": "A model with general knowledge of protein domain architecture can identify the PP2C-like catalytic motifs and TPR repeats in the sequence, distinguishing phosphatase activity from membrane transport (no TM helices present) and peroxidase inhibition (no peroxidase-binding fold). This constitutes a defensible biological argument from the sequence rather than pure database lookup."
  },
  "case_id": "GO_molecular_function_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H4",
      "H5",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2U919 (PPP5_ASPOR, Serine/threonine-protein phosphatase T) is annotated with GO:0016791 (phosphatase activity) at IDA evidence level from PubMed:17475320 (C8, H7), and with EC 3.1.3.16 catalytic reactions for O-phospho-L-seryl and O-phospho-L-threonyl dephosphorylation (C6, C7, H4, H5). The protein name, function comment, and catalytic activity are all consistent with phosphatase activity. The EC assignment is supported by ECO:0000305 (curator inference from PubMed), and the GO IDA annotation confirms direct experimental assay support."
  },
  "important_caveats": [
    "The GO:0016791 annotation is IDA (direct assay) from PubMed:17475320, providing experimental support, while the protein name and function comment are partly based on similarity to P53043 (ECO:0000250).",
    "The more specific GO term GO:0004722 (protein serine/threonine phosphatase activity) is also annotated (IEA:UniProtKB-EC), but the broader GO:0016791 is the offered option and is correct as a parent term.",
    "Sequence identification of PPP5-family motifs requires specialized bioinformatics knowledge; while this constitutes reasoning from general biological principles, it is at the boundary of expert pattern recognition.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the assessment of reasoning support is based on whether the motifs are identifiable from the sequence itself."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular functions (transport, channel, inhibitor, enzyme catalysis). The sequence lacks transmembrane helices (ruling out A and B), lacks peroxidase-binding structural features (ruling out C), and contains distinctive PP2C-like catalytic motifs supporting D. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2U919 (PPP5_ASPOR, Serine/threonine-protein phosphatase T) is annotated with GO:0016791 (phosphatase activity) at IDA evidence level from PubMed:17475320 (C8, H7), and with EC 3.1.3.16 catalytic reactions for O-phospho-L-seryl and O-phospho-L-threonyl dephosphorylation (C6, C7, H4, H5). The protein name, function comment, and catalytic activity are all consistent with phosphatase activity. The EC assignment is supported by ECO:0000305 (curator inference from PubMed), and the GO IDA annotation confirms direct experimental assay support.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "H4", "H5", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark PP2C-like catalytic motifs of the PPP5 phosphatase family: a 'GDG' metal-binding motif, the highly conserved 'HGGLFSDD' signature of the PP2C-like catalytic domain, and clustered Asp/His metal-coordinating residues. The N-terminal region displays TPR (tetratricopeptide repeat) architecture (LxxLxxA patterns), which is characteristic of PPP5-family serine/threonine phosphatases. These features are inconsistent with transmembrane transporters (A) or mechanosensitive ion channels (B), which require multiple hydrophobic transmembrane helices absent from this sequence, and with peroxidase inhibitors (C), which require peroxidase-binding structural domains. The presence of a PP2C-like catalytic core with metal-binding residues is a concrete, generalizable biological argument for phosphatase activity.",
    "missing_item_specific_fact": "None critical. While exact identification of the PPP5 family from sequence requires familiarity with PP2C-like motifs, the motifs themselves (HGGLFSDD, GDG, metal-binding residues) are well-known diagnostic features in protein biochemistry and are present in the supplied sequence.",
    "reason": "A model with general knowledge of protein domain architecture can identify the PP2C-like catalytic motifs and TPR repeats in the sequence, distinguishing phosphatase activity from membrane transport (no TM helices present) and peroxidase inhibition (no peroxidase-binding fold). This constitutes a defensible biological argument from the sequence rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular functions (transport, channel, inhibitor, enzyme catalysis). The sequence lacks transmembrane helices (ruling out A and B), lacks peroxidase-binding structural features (ruling out C), and contains distinctive PP2C-like catalytic motifs supporting D. No other option is defensible."
  },
  "important_caveats": [
    "The GO:0016791 annotation is IDA (direct assay) from PubMed:17475320, providing experimental support, while the protein name and function comment are partly based on similarity to P53043 (ECO:0000250).",
    "The more specific GO term GO:0004722 (protein serine/threonine phosphatase activity) is also annotated (IEA:UniProtKB-EC), but the broader GO:0016791 is the offered option and is correct as a parent term.",
    "Sequence identification of PPP5-family motifs requires specialized bioinformatics knowledge; while this constitutes reasoning from general biological principles, it is at the boundary of expert pattern recognition.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the assessment of reasoning support is based on whether the motifs are identifiable from the sequence itself."
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

**Accession:** `Q2U919` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 127. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
"Q2U919"
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17475320","source":"PubMed"}],"value":"AoPPT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53043","source":"UniProtKB"}],"value":"Serine/threonine-protein phosphatase T"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53043","source":"UniProtKB"}],"value":"PPT"}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53043","source":"UniProtKB"}],"value":"Protein phosphatase that specifically binds to and dephosphorylates the molecular chaperone Hsp90. Dephosphorylation positively regulates the Hsp90 chaperone machinery"}]}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:47005"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"name":"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:47004"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:61977"}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"17475320","source":"PubMed"}],"id":"GO:0016791","properties":[{"key":"GoTerm","value":"F:phosphatase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"database":"GO","id":"GO:0004722","properties":[{"key":"GoTerm","value":"F:protein serine/threonine phosphatase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-EC"}]}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 47-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:17475320};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000305|PubMed:17475320};
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 55-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:61977; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:17475320};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;
CC         Evidence={ECO:0000305|PubMed:17475320};
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 101-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
DR   GO; GO:0016791; F:phosphatase activity; IDA:UniProtKB.
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 102-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
DR   GO; GO:0004722; F:protein serine/threonine phosphatase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 182. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
