# catalytic_activity_0101

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — (13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSASGKEKPLKDVPGSYGVPVVGALKDRLDFYWFQGEVEFYKSRMEKNQSTVFRVNFPPGPPGFPEGHGIVLLDQVSYSVLLDNAKVDKRDTLIGSYMPDLAFTGGYRTLPYLDTAEEKHTTYKSLMFEILHESAQRFGPELSSAFDRTAQEWEAKIAKDGSVESLSTAGNMVIQFLYKTITHQDPMATMGDDPHSVYMAWTGVQFAGIAYTNLPHITEELLMHSFQLPFFPIKKKYEQIVEFFRSAGSGLLDLAVTKYGLDREEALHNLVFSFGINTRLGLLKMFPPILFFIARAGAEFQARLKQEIRGRMKKREDAASIQALGDLKLVKATVLEVFRLMPSIFVAFGRARQDLEVESHDARYKIKKGELLGTHQYFVMRDPVVFKDPHSFVPDRFMGSEGAALLPHIVWSNGRETDSPTPTNKQCPGKNQAELIAVQFIAEMFLRYDSWEVTQESSVSATKLDVHLCKLVKRS

[Multiple Choices]
A. an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)
B. 2 L-tryptophan = cyclo(L-Trp-L-Trp) + 2 H2O
C. (13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O
D. 2 oxidized [4Fe-4S]-[ferredoxin] + taurine + H2O = aminoacetaldehyde + 2 reduced [4Fe-4S]-[ferredoxin] + sulfite + 3 H(+)
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

> The supplied sequence exactly matches the UniProt entry annotated as CYP74M1, and that entry assigns the reaction in choice C with experimental-evidence code ECO:0000269 linked to PubMed 26776054. The archived annotation also contains the same reaction.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options describe distinct enzyme activities, and sequence analysis might suggest a broad protein family, but the input gives no organism, enzyme name, or demonstrated substrate specificity that establishes this exact hydroperoxide-to-etheroleate reaction.


**Missing item-specific fact**

> The protein-specific functional assignment and evidence that this enzyme catalyzes the reaction in choice C.


**Reason**

> Distinguishing the precise reaction requires an item-specific functional annotation or experimental fact not provided in the question. Identifying the exact sequence from memory would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify substantially different reactions; the reviewer-only annotation supports choice C for the sequence-matched protein.


### Important caveats

- The evidence is a UniProt annotation linked to a publication; the primary paper was not independently reviewed here.
- The sequence matches both the current and checked historical UniProt record, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options describe distinct enzyme activities, and sequence analysis might suggest a broad protein family, but the input gives no organism, enzyme name, or demonstrated substrate specificity that establishes this exact hydroperoxide-to-etheroleate reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment and evidence that this enzyme catalyzes the reaction in choice C.",
    "reason": "Distinguishing the precise reaction requires an item-specific functional annotation or experimental fact not provided in the question. Identifying the exact sequence from memory would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "catalytic_activity_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as CYP74M1, and that entry assigns the reaction in choice C with experimental-evidence code ECO:0000269 linked to PubMed 26776054. The archived annotation also contains the same reaction."
  },
  "important_caveats": [
    "The evidence is a UniProt annotation linked to a publication; the primary paper was not independently reviewed here.",
    "The sequence matches both the current and checked historical UniProt record, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify substantially different reactions; the reviewer-only annotation supports choice C for the sequence-matched protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as CYP74M1, and that entry assigns the reaction in choice C with experimental-evidence code ECO:0000269 linked to PubMed 26776054. The archived annotation also contains the same reaction.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options describe distinct enzyme activities, and sequence analysis might suggest a broad protein family, but the input gives no organism, enzyme name, or demonstrated substrate specificity that establishes this exact hydroperoxide-to-etheroleate reaction.",
    "missing_item_specific_fact": "The protein-specific functional assignment and evidence that this enzyme catalyzes the reaction in choice C.",
    "reason": "Distinguishing the precise reaction requires an item-specific functional annotation or experimental fact not provided in the question. Identifying the exact sequence from memory would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify substantially different reactions; the reviewer-only annotation supports choice C for the sequence-matched protein."
  },
  "important_caveats": [
    "The evidence is a UniProt annotation linked to a publication; the primary paper was not independently reviewed here.",
    "The sequence matches both the current and checked historical UniProt record, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry D8S724 (C74M1_SELML, sequence matched at 475 aa) explicitly annotates the catalytic activity as '(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O' (EC 4.2.1.183), with experimental evidence code ECO:0000269 from PubMed:26776054 (Gorina et al., 2016, Biochim. Biophys. Acta). The protein is named 'Divinyl ether synthase CYP74M1' / 'Etheroleic acid synthase CYP74M1'. Choice C matches this reaction verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 475-aa sequence exhibits cytochrome P450 architecture (N-terminal signal peptide, substrate-binding domain, heme-binding region with a variant FGxxRxx motif typical of the CYP74 subfamily, and C-terminal membrane anchor). P450s catalyze oxidative reactions on diverse substrates. Among the four choices, only C describes a P450-type reaction (dehydration of a fatty acid hydroperoxide by a heme-thiolate enzyme). Choice A is a dolichol-linked mannosyltransferase (GT-B fold), B is a cyclodipeptide synthase (fold-type II thioesterase), and D is an Fe-S cluster–dependent dioxygenase (taurine dioxygenase). None of these share a P450 fold or mechanism. Recognizing the P450 scaffold and eliminating mechanistically incompatible choices constitutes valid biological reasoning.


**Missing item-specific fact**

> Specific subfamily assignment within CYP74 (e.g., CYP74M1 vs CYP74A/B/C/D) would require exact sequence identity or phylogenetic analysis, but this is unnecessary because all distractors belong to entirely unrelated enzyme classes.


**Reason**

> A model with general P450 knowledge can identify the heme-thiolate enzyme fold from sequence features (length, domain organization, conserved P450 motifs including the slightly divergent heme-binding region of CYP74s) and then eliminate A, B, and D on mechanistic grounds (glycosyltransferase, thioesterase, Fe-S dioxygenase are incompatible with a P450). Only C is a P450-catalyzed transformation. No protein-specific database lookup is required to reach the correct answer given these distractors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, B, and D describe reactions catalyzed by glycosyltransferases, cyclodipeptide synthases, and Fe-S cluster enzymes respectively—none of which share a P450 fold or mechanism. Only C is mechanistically consistent with a cytochrome P450. The distractors are from sufficiently different enzyme classes that no ambiguity arises.


### Important caveats

- The heme-binding motif in CYP74 enzymes is slightly divergent from canonical P450s (FGxGxRxCxG spacing varies), which may modestly increase recognition difficulty but does not preclude identification.
- Distinguishing CYP74M1 (divinyl ether synthase) from other CYP74 subfamilies (allene oxide synthase, hydroperoxide lyase, etc.) from sequence alone would be difficult; however, the given distractors do not include other CYP74 reactions, so subfamily resolution is unnecessary.
- The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:26776054), confirming the reaction was experimentally characterized rather than inferred by similarity.
- Reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the reasoning path relies solely on sequence features and general enzymology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 475-aa sequence exhibits cytochrome P450 architecture (N-terminal signal peptide, substrate-binding domain, heme-binding region with a variant FGxxRxx motif typical of the CYP74 subfamily, and C-terminal membrane anchor). P450s catalyze oxidative reactions on diverse substrates. Among the four choices, only C describes a P450-type reaction (dehydration of a fatty acid hydroperoxide by a heme-thiolate enzyme). Choice A is a dolichol-linked mannosyltransferase (GT-B fold), B is a cyclodipeptide synthase (fold-type II thioesterase), and D is an Fe-S cluster–dependent dioxygenase (taurine dioxygenase). None of these share a P450 fold or mechanism. Recognizing the P450 scaffold and eliminating mechanistically incompatible choices constitutes valid biological reasoning.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Specific subfamily assignment within CYP74 (e.g., CYP74M1 vs CYP74A/B/C/D) would require exact sequence identity or phylogenetic analysis, but this is unnecessary because all distractors belong to entirely unrelated enzyme classes.",
    "reason": "A model with general P450 knowledge can identify the heme-thiolate enzyme fold from sequence features (length, domain organization, conserved P450 motifs including the slightly divergent heme-binding region of CYP74s) and then eliminate A, B, and D on mechanistic grounds (glycosyltransferase, thioesterase, Fe-S dioxygenase are incompatible with a P450). Only C is a P450-catalyzed transformation. No protein-specific database lookup is required to reach the correct answer given these distractors."
  },
  "case_id": "catalytic_activity_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry D8S724 (C74M1_SELML, sequence matched at 475 aa) explicitly annotates the catalytic activity as '(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O' (EC 4.2.1.183), with experimental evidence code ECO:0000269 from PubMed:26776054 (Gorina et al., 2016, Biochim. Biophys. Acta). The protein is named 'Divinyl ether synthase CYP74M1' / 'Etheroleic acid synthase CYP74M1'. Choice C matches this reaction verbatim."
  },
  "important_caveats": [
    "The heme-binding motif in CYP74 enzymes is slightly divergent from canonical P450s (FGxGxRxCxG spacing varies), which may modestly increase recognition difficulty but does not preclude identification.",
    "Distinguishing CYP74M1 (divinyl ether synthase) from other CYP74 subfamilies (allene oxide synthase, hydroperoxide lyase, etc.) from sequence alone would be difficult; however, the given distractors do not include other CYP74 reactions, so subfamily resolution is unnecessary.",
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:26776054), confirming the reaction was experimentally characterized rather than inferred by similarity.",
    "Reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the reasoning path relies solely on sequence features and general enzymology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, B, and D describe reactions catalyzed by glycosyltransferases, cyclodipeptide synthases, and Fe-S cluster enzymes respectively—none of which share a P450 fold or mechanism. Only C is mechanistically consistent with a cytochrome P450. The distractors are from sufficiently different enzyme classes that no ambiguity arises."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry D8S724 (C74M1_SELML, sequence matched at 475 aa) explicitly annotates the catalytic activity as '(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O' (EC 4.2.1.183), with experimental evidence code ECO:0000269 from PubMed:26776054 (Gorina et al., 2016, Biochim. Biophys. Acta). The protein is named 'Divinyl ether synthase CYP74M1' / 'Etheroleic acid synthase CYP74M1'. Choice C matches this reaction verbatim.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 475-aa sequence exhibits cytochrome P450 architecture (N-terminal signal peptide, substrate-binding domain, heme-binding region with a variant FGxxRxx motif typical of the CYP74 subfamily, and C-terminal membrane anchor). P450s catalyze oxidative reactions on diverse substrates. Among the four choices, only C describes a P450-type reaction (dehydration of a fatty acid hydroperoxide by a heme-thiolate enzyme). Choice A is a dolichol-linked mannosyltransferase (GT-B fold), B is a cyclodipeptide synthase (fold-type II thioesterase), and D is an Fe-S cluster–dependent dioxygenase (taurine dioxygenase). None of these share a P450 fold or mechanism. Recognizing the P450 scaffold and eliminating mechanistically incompatible choices constitutes valid biological reasoning.",
    "missing_item_specific_fact": "Specific subfamily assignment within CYP74 (e.g., CYP74M1 vs CYP74A/B/C/D) would require exact sequence identity or phylogenetic analysis, but this is unnecessary because all distractors belong to entirely unrelated enzyme classes.",
    "reason": "A model with general P450 knowledge can identify the heme-thiolate enzyme fold from sequence features (length, domain organization, conserved P450 motifs including the slightly divergent heme-binding region of CYP74s) and then eliminate A, B, and D on mechanistic grounds (glycosyltransferase, thioesterase, Fe-S dioxygenase are incompatible with a P450). Only C is a P450-catalyzed transformation. No protein-specific database lookup is required to reach the correct answer given these distractors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, B, and D describe reactions catalyzed by glycosyltransferases, cyclodipeptide synthases, and Fe-S cluster enzymes respectively—none of which share a P450 fold or mechanism. Only C is mechanistically consistent with a cytochrome P450. The distractors are from sufficiently different enzyme classes that no ambiguity arises."
  },
  "important_caveats": [
    "The heme-binding motif in CYP74 enzymes is slightly divergent from canonical P450s (FGxGxRxCxG spacing varies), which may modestly increase recognition difficulty but does not preclude identification.",
    "Distinguishing CYP74M1 (divinyl ether synthase) from other CYP74 subfamilies (allene oxide synthase, hydroperoxide lyase, etc.) from sequence alone would be difficult; however, the given distractors do not include other CYP74 reactions, so subfamily resolution is unnecessary.",
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed:26776054), confirming the reaction was experimentally characterized rather than inferred by similarity.",
    "Reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the reasoning path relies solely on sequence features and general enzymology."
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

**Accession:** `D8S724` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 64. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:52.483973+00:00.  

```json
"D8S724"
```

Source SHA-256: `ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:52.483973+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"value":"4.2.1.183"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"26776054","source":"PubMed"}],"value":"Etheroleic acid synthase CYP74M1"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26776054","source":"PubMed"}],"value":"Divinyl ether synthase CYP74M1"}}}
```

Source SHA-256: `ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D8S724.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:52.483973+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"26776054","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79276"}}],"reaction":{"ecNumber":"4.2.1.183","evidences":[{"evidenceCode":"ECO:0000269","id":"26776054","source":"PubMed"}],"name":"(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79275"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:57466"},{"database":"ChEBI","id":"CHEBI:229759"}]}}
```

Source SHA-256: `ce7aa6baed98798a69728414276bfd9599ab5c6274d1a0a96fd5c9206a1de059`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:54.936001+00:00.  

```text
DE   RecName: Full=Divinyl ether synthase CYP74M1 {ECO:0000303|PubMed:26776054};
DE   AltName: Full=Etheroleic acid synthase CYP74M1 {ECO:0000305|PubMed:26776054};
DE            EC=4.2.1.183 {ECO:0000269|PubMed:26776054};
```

Source SHA-256: `1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D8S724?format=txt&versions=64)  
**Locator:** `lines 56-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 64 / 1.  
**Retrieved:** 2026-11-02T04:27:54.936001+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate +
CC         H2O; Xref=Rhea:RHEA:79275, ChEBI:CHEBI:15377, ChEBI:CHEBI:57466,
CC         ChEBI:CHEBI:229759; EC=4.2.1.183;
CC         Evidence={ECO:0000269|PubMed:26776054};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79276;
CC         Evidence={ECO:0000305|PubMed:26776054};
```

Source SHA-256: `1097bd32dc09d094cd22c43824a76d7061c1b33dcc4a0916c1eedb76de7e938c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 101. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
