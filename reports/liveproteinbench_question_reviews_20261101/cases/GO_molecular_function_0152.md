# GO_molecular_function_0152

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — S-adenosylmethionine-dependent methyltransferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAENQEALAEFYDKGVGVWDNLSREHMHFGYYAPGATATIGGHRASLVRLIDEALCFAEFPDDPEKKPRNMLDVGCGIGGTCLHVAKKYDIQCKGINISPEQVKIAQGLAAAQGLESKVSFDVGDALDMPYPDGAFDLVLSIHCIEHLQDKEKFIREMVRVAASGATIIILSHVHRDLSPSEQSLKPQEERVLRKIGSSVQAWFCPLSNYVSLLAPLPVEVIKIADWSRNIDPSSRLMLKVAFSVKGIVSNLMKGVQGWTAIKNVLPMKLLHKALHDGLVKFVVLTCRKSN

[Multiple Choices]
A. 2-oxoglutarate-dependent dioxygenase activity
B. phosphopantothenoylcysteine decarboxylase activity
C. S-adenosylmethionine-dependent methyltransferase activity
D. tRNA (guanine(18)-2'-O)-methyltransferase activity
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

> The supplied sequence exactly matches the cited UniProt entry for Rauvolfia serpentina ajmaline N-methyltransferase. The entry reports experimentally supported methylation using S-adenosyl-L-methionine, which supports choice C; its GO annotation for that activity is computationally assigned by InterPro.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may be compatible with a methyltransferase, but the input supplies no organism, substrate, or other context that identifies its particular activity. Sequence-based general knowledge does not establish that this protein methylates ajmaline rather than performing one of the other listed functions.


**Missing item-specific fact**

> The protein-specific identification and functional annotation as an S-adenosylmethionine-dependent ajmaline N-methyltransferase.


**Reason**

> The correct choice is supported by reviewer-only evidence for the exact sequence, but that evidence is absent from the evaluated input. Recognizing the sequence or relying on a predictor would not make the distinction reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports C for this protein. Although option C is broad, the sequence-specific evidence identifies an activity matching it, not the specific tRNA methyltransferase activity in D.


### Important caveats

- The cited functional and catalytic annotations are linked to a publication with experimental evidence; the GO term itself is marked IEA:InterPro.
- The exact author data-source snapshot is unknown, though the sequence matches both current and archived UniProt records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may be compatible with a methyltransferase, but the input supplies no organism, substrate, or other context that identifies its particular activity. Sequence-based general knowledge does not establish that this protein methylates ajmaline rather than performing one of the other listed functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional annotation as an S-adenosylmethionine-dependent ajmaline N-methyltransferase.",
    "reason": "The correct choice is supported by reviewer-only evidence for the exact sequence, but that evidence is absent from the evaluated input. Recognizing the sequence or relying on a predictor would not make the distinction reasoning-supported."
  },
  "case_id": "GO_molecular_function_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited UniProt entry for Rauvolfia serpentina ajmaline N-methyltransferase. The entry reports experimentally supported methylation using S-adenosyl-L-methionine, which supports choice C; its GO annotation for that activity is computationally assigned by InterPro."
  },
  "important_caveats": [
    "The cited functional and catalytic annotations are linked to a publication with experimental evidence; the GO term itself is marked IEA:InterPro.",
    "The exact author data-source snapshot is unknown, though the sequence matches both current and archived UniProt records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C for this protein. Although option C is broad, the sequence-specific evidence identifies an activity matching it, not the specific tRNA methyltransferase activity in D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited UniProt entry for Rauvolfia serpentina ajmaline N-methyltransferase. The entry reports experimentally supported methylation using S-adenosyl-L-methionine, which supports choice C; its GO annotation for that activity is computationally assigned by InterPro.",
    "evidence_ids": ["C1", "C5", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may be compatible with a methyltransferase, but the input supplies no organism, substrate, or other context that identifies its particular activity. Sequence-based general knowledge does not establish that this protein methylates ajmaline rather than performing one of the other listed functions.",
    "missing_item_specific_fact": "The protein-specific identification and functional annotation as an S-adenosylmethionine-dependent ajmaline N-methyltransferase.",
    "reason": "The correct choice is supported by reviewer-only evidence for the exact sequence, but that evidence is absent from the evaluated input. Recognizing the sequence or relying on a predictor would not make the distinction reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports C for this protein. Although option C is broad, the sequence-specific evidence identifies an activity matching it, not the specific tRNA methyltransferase activity in D."
  },
  "important_caveats": [
    "The cited functional and catalytic annotations are linked to a publication with experimental evidence; the GO term itself is marked IEA:InterPro.",
    "The exact author data-source snapshot is unknown, though the sequence matches both current and archived UniProt records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A075D654 (sequence matched, 291 aa) identifies this protein as Ajmaline N-methyltransferase (EC 2.1.1.393) from Rauvolfia serpentina. Experimental evidence (ECO:0000269, PubMed:27122470) confirms the catalytic reaction: ajmaline + S-adenosyl-L-methionine → 4-methylajmaline + S-adenosyl-L-homocysteine + H(+). This is unambiguously an S-adenosylmethionine-dependent methyltransferase reaction. GO:0008757 (S-adenosylmethionine-dependent methyltransferase activity) is annotated to this entry. The answer C is well-supported by experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of class I SAM-dependent methyltransferases: a GxGxG Rossmann-fold motif (GCGIGGT at ~residues 78-84) and a DWS motif (IADWS at ~residues 228-232). These are textbook signatures of the Rossmann-fold methyltransferase superfamily that uses SAM as methyl donor, directly supporting option C. Option A (2-oxoglutarate-dependent dioxygenase) requires a different fold (cupin/β-barrel) and Fe(II)/2-oxoglutarate-binding motifs (HxD/E...H) absent here. Option B (phosphopantothenoylcysteine decarboxylase) is a flavin-dependent decarboxylase with no SAM-binding architecture. Option D (tRNA guanine(18)-2'-O-methyltransferase, Trm13) uses a class III methyltransferase fold (not Rossmann) and would be expected to contain tRNA-recognition elements; the observed Rossmann-fold architecture with DWS motif is inconsistent with a tRNA 2'-O-methyltransferase. Thus, general knowledge of methyltransferase fold classification meaningfully distinguishes C from the other options.


**Missing item-specific fact**

> The exact substrate identity (ajmaline alkaloid) cannot be determined from sequence alone, but the question only requires identifying the general molecular function category (SAM-dependent methyltransferase), which the fold motifs support.


**Reason**

> The GxGxG and DWS motifs are well-established, general biochemical signatures of class I SAM-dependent methyltransferases. Their presence rules out dioxygenase (A) and decarboxylase (B) activities. The Rossmann-fold architecture is inconsistent with the class III fold of Trm13-type tRNA 2'-O-methyltransferases (D). This provides a concrete, general biological argument to select C without needing to recognize the exact protein or recall a specific database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are clearly incompatible with the observed methyltransferase fold motifs. Option D (tRNA 2'-O-methyltransferase) uses a fundamentally different structural fold (class III) and is inconsistent with the Rossmann-fold architecture evident in the sequence. Option C is the only defensible choice given the sequence features. While C is a broad category that technically encompasses D's parent, the fold evidence argues specifically against D, leaving C as the uniquely supported answer.


### Important caveats

- The GO:0008757 annotation in UniProt carries IEA:InterPro evidence code (computational inference from domain match), while the underlying enzymatic activity is experimentally confirmed (ECO:0000269, PubMed:27122470). The answer is supported at the experimental level.
- The distinction between C and D relies on fold-class knowledge (class I Rossmann vs. class III for Trm13); a model lacking this structural biology knowledge might find C and D both plausible as 'methyltransferase' answers.
- The sequence-match is confirmed (291 aa, SHA256 matched in both current and historical entry versions).
- The identity of the protein as Ajmaline N-methyltransferase specifically (vs. another SAM-dependent methyltransferase) would require substrate-level information not derivable from sequence alone, but this level of specificity is not required by the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of class I SAM-dependent methyltransferases: a GxGxG Rossmann-fold motif (GCGIGGT at ~residues 78-84) and a DWS motif (IADWS at ~residues 228-232). These are textbook signatures of the Rossmann-fold methyltransferase superfamily that uses SAM as methyl donor, directly supporting option C. Option A (2-oxoglutarate-dependent dioxygenase) requires a different fold (cupin/β-barrel) and Fe(II)/2-oxoglutarate-binding motifs (HxD/E...H) absent here. Option B (phosphopantothenoylcysteine decarboxylase) is a flavin-dependent decarboxylase with no SAM-binding architecture. Option D (tRNA guanine(18)-2'-O-methyltransferase, Trm13) uses a class III methyltransferase fold (not Rossmann) and would be expected to contain tRNA-recognition elements; the observed Rossmann-fold architecture with DWS motif is inconsistent with a tRNA 2'-O-methyltransferase. Thus, general knowledge of methyltransferase fold classification meaningfully distinguishes C from the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact substrate identity (ajmaline alkaloid) cannot be determined from sequence alone, but the question only requires identifying the general molecular function category (SAM-dependent methyltransferase), which the fold motifs support.",
    "reason": "The GxGxG and DWS motifs are well-established, general biochemical signatures of class I SAM-dependent methyltransferases. Their presence rules out dioxygenase (A) and decarboxylase (B) activities. The Rossmann-fold architecture is inconsistent with the class III fold of Trm13-type tRNA 2'-O-methyltransferases (D). This provides a concrete, general biological argument to select C without needing to recognize the exact protein or recall a specific database annotation."
  },
  "case_id": "GO_molecular_function_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A075D654 (sequence matched, 291 aa) identifies this protein as Ajmaline N-methyltransferase (EC 2.1.1.393) from Rauvolfia serpentina. Experimental evidence (ECO:0000269, PubMed:27122470) confirms the catalytic reaction: ajmaline + S-adenosyl-L-methionine → 4-methylajmaline + S-adenosyl-L-homocysteine + H(+). This is unambiguously an S-adenosylmethionine-dependent methyltransferase reaction. GO:0008757 (S-adenosylmethionine-dependent methyltransferase activity) is annotated to this entry. The answer C is well-supported by experimental evidence."
  },
  "important_caveats": [
    "The GO:0008757 annotation in UniProt carries IEA:InterPro evidence code (computational inference from domain match), while the underlying enzymatic activity is experimentally confirmed (ECO:0000269, PubMed:27122470). The answer is supported at the experimental level.",
    "The distinction between C and D relies on fold-class knowledge (class I Rossmann vs. class III for Trm13); a model lacking this structural biology knowledge might find C and D both plausible as 'methyltransferase' answers.",
    "The sequence-match is confirmed (291 aa, SHA256 matched in both current and historical entry versions).",
    "The identity of the protein as Ajmaline N-methyltransferase specifically (vs. another SAM-dependent methyltransferase) would require substrate-level information not derivable from sequence alone, but this level of specificity is not required by the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly incompatible with the observed methyltransferase fold motifs. Option D (tRNA 2'-O-methyltransferase) uses a fundamentally different structural fold (class III) and is inconsistent with the Rossmann-fold architecture evident in the sequence. Option C is the only defensible choice given the sequence features. While C is a broad category that technically encompasses D's parent, the fold evidence argues specifically against D, leaving C as the uniquely supported answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A075D654 (sequence matched, 291 aa) identifies this protein as Ajmaline N-methyltransferase (EC 2.1.1.393) from Rauvolfia serpentina. Experimental evidence (ECO:0000269, PubMed:27122470) confirms the catalytic reaction: ajmaline + S-adenosyl-L-methionine → 4-methylajmaline + S-adenosyl-L-homocysteine + H(+). This is unambiguously an S-adenosylmethionine-dependent methyltransferase reaction. GO:0008757 (S-adenosylmethionine-dependent methyltransferase activity) is annotated to this entry. The answer C is well-supported by experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H3", "H4", "H5", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of class I SAM-dependent methyltransferases: a GxGxG Rossmann-fold motif (GCGIGGT at ~residues 78-84) and a DWS motif (IADWS at ~residues 228-232). These are textbook signatures of the Rossmann-fold methyltransferase superfamily that uses SAM as methyl donor, directly supporting option C. Option A (2-oxoglutarate-dependent dioxygenase) requires a different fold (cupin/β-barrel) and Fe(II)/2-oxoglutarate-binding motifs (HxD/E...H) absent here. Option B (phosphopantothenoylcysteine decarboxylase) is a flavin-dependent decarboxylase with no SAM-binding architecture. Option D (tRNA guanine(18)-2'-O-methyltransferase, Trm13) uses a class III methyltransferase fold (not Rossmann) and would be expected to contain tRNA-recognition elements; the observed Rossmann-fold architecture with DWS motif is inconsistent with a tRNA 2'-O-methyltransferase. Thus, general knowledge of methyltransferase fold classification meaningfully distinguishes C from the other options.",
    "missing_item_specific_fact": "The exact substrate identity (ajmaline alkaloid) cannot be determined from sequence alone, but the question only requires identifying the general molecular function category (SAM-dependent methyltransferase), which the fold motifs support.",
    "reason": "The GxGxG and DWS motifs are well-established, general biochemical signatures of class I SAM-dependent methyltransferases. Their presence rules out dioxygenase (A) and decarboxylase (B) activities. The Rossmann-fold architecture is inconsistent with the class III fold of Trm13-type tRNA 2'-O-methyltransferases (D). This provides a concrete, general biological argument to select C without needing to recognize the exact protein or recall a specific database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly incompatible with the observed methyltransferase fold motifs. Option D (tRNA 2'-O-methyltransferase) uses a fundamentally different structural fold (class III) and is inconsistent with the Rossmann-fold architecture evident in the sequence. Option C is the only defensible choice given the sequence features. While C is a broad category that technically encompasses D's parent, the fold evidence argues specifically against D, leaving C as the uniquely supported answer."
  },
  "important_caveats": [
    "The GO:0008757 annotation in UniProt carries IEA:InterPro evidence code (computational inference from domain match), while the underlying enzymatic activity is experimentally confirmed (ECO:0000269, PubMed:27122470). The answer is supported at the experimental level.",
    "The distinction between C and D relies on fold-class knowledge (class I Rossmann vs. class III for Trm13); a model lacking this structural biology knowledge might find C and D both plausible as 'methyltransferase' answers.",
    "The sequence-match is confirmed (291 aa, SHA256 matched in both current and historical entry versions).",
    "The identity of the protein as Ajmaline N-methyltransferase specifically (vs. another SAM-dependent methyltransferase) would require substrate-level information not derivable from sequence alone, but this level of specificity is not required by the question."
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

**Accession:** `A0A075D654` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 32. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
"A0A075D654"
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AHH02777.1","source":"EMBL"}],"value":"Gamma-tocopherol-like methyltransferase ANMT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"value":"2.1.1.393"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"}],"value":"Ajmaline N-methyltransferase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"27122470","source":"PubMed"}],"value":"RsANMT"}]}}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"value":"N-methyltransferase involved in the biosynthesis of ajmaline-type monoterpenoid indole alkaloids (MIAs) natural products, important plant-derived pharmaceuticals used in the therapy of heart disorders (PubMed:27122470). Catalyzes the indole N-methylation of ajmaline to produce 4-methylajmaline (PubMed:27122470). Also able, with a lower efficiency, to mediate the conversion of norajmaline to 4-methylnorajmaline (PubMed:27122470)"}]}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79632"}}],"reaction":{"ecNumber":"2.1.1.393","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"name":"ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79631"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:58567"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:230509"}]}}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79628"}}],"reaction":{"ecNumber":"2.1.1.393","evidences":[{"evidenceCode":"ECO:0000269","id":"27122470","source":"PubMed"}],"name":"norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79627"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:77618"},{"database":"ChEBI","id":"CHEBI:230510"}]}}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A075D654.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:36.410454+00:00.  

```json
{"database":"GO","id":"GO:0008757","properties":[{"key":"GoTerm","value":"F:S-adenosylmethionine-dependent methyltransferase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `124df2385940e2e796356809e8af1e8fa6c895c01f7e6fd2fc1c87d9a5dbcf22`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 35-41`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
CC   -!- FUNCTION: N-methyltransferase involved in the biosynthesis of ajmaline-
CC       type monoterpenoid indole alkaloids (MIAs) natural products, important
CC       plant-derived pharmaceuticals used in the therapy of heart disorders
CC       (PubMed:27122470). Catalyzes the indole N-methylation of ajmaline to
CC       produce 4-methylajmaline (PubMed:27122470). Also able, with a lower
CC       efficiency, to mediate the conversion of norajmaline to 4-
CC       methylnorajmaline (PubMed:27122470). {ECO:0000269|PubMed:27122470}.
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-
CC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:79631,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58567,
CC         ChEBI:CHEBI:59789, ChEBI:CHEBI:230509; EC=2.1.1.393;
CC         Evidence={ECO:0000269|PubMed:27122470};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79632;
CC         Evidence={ECO:0000269|PubMed:27122470};
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 50-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline +
CC         S-adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:79627,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:77618, ChEBI:CHEBI:230510; EC=2.1.1.393;
CC         Evidence={ECO:0000269|PubMed:27122470};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79628;
CC         Evidence={ECO:0000269|PubMed:27122470};
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A075D654?format=txt&versions=32)  
**Locator:** `lines 93-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:15.419855+00:00.  

```text
DR   GO; GO:0008757; F:S-adenosylmethionine-dependent methyltransferase activity; IEA:InterPro.
```

Source SHA-256: `15b1ec6a186650c4d2bc97d8a1e63645a9b1f63fb122c34f7abac877a8922eb4`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 87421-87429`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008757
name: S-adenosylmethionine-dependent methyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a methyl group from S-adenosyl-L-methionine to a substrate." [GOC:mah]
synonym: "S-adenosyl methionine-dependent methyltransferase activity" EXACT []
synonym: "SAM-dependent methyltransferase activity" EXACT []
is_a: GO:0008168 ! methyltransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 152. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
