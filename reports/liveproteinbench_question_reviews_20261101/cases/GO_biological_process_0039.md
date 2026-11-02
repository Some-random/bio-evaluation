# GO_biological_process_0039

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — triterpenoid biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVLSRLDFPSDFIFGSGTSASQVEGAALEDGKTSTAFEGFLTRMSGNDLSKGVEGYYKYKEDVQLMVQTGLDAYRFSISWSRLIPGGKGPVNPKGLQYYNNFIDELIKNGIQPHVTLLHFDIPDTLMTAYNGLKGQEFVEDFTAFADVCFKEFGDRVLYWTTVNEANNFASLTLDEGNFMPSTEPYIRGHNIILAHASAVKLYREKYKKTQNGFIGLNLYASWYFPETDDEQDSIAAQRAIDFTIGWIMQPLIYGEYPETLKKQVGERLPTFTKEESTFVKNSFDFIGVNCYVGTAVKDDPDSCNSKNKTIITDMSAKLSPKGELGGAYMKGLLEYFKRDYGNPPIYIQENGYWTPRELGVNDASRIEYHTASLASMHDAMKNGANVKGYFQWSFLDLLEVFKYSYGLYHVDLEDPTRERRPKASANWYAEFLKGCATSNGNAKVETPL

[Multiple Choices]
A. mitophagy
B. response to insulin
C. response to bacterium
D. triterpenoid biosynthetic process
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the 449-aa SoGH1 protein from Saponaria officinalis. UniProt records an experimentally supported function in the oleanane-type triterpene saponin biosynthetic pathway and a GO annotation for triterpenoid biosynthetic process with IDA evidence. This supports choice D, though the protein’s described catalytic step is sugar-chain modification of a saponin.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C9](#evidence-c9), [H3](#evidence-h3), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an enzyme, but its sequence alone does not establish that it acts in soapwort saponin biosynthesis rather than another biological process. The choices are distinguishable once that specific pathway role is known.


**Missing item-specific fact**

> The protein-specific finding that SoGH1 participates in triterpene saponin biosynthesis by catalyzing a sugar-chain modification; this comes from the cited functional annotation and study, not from information supplied with the sequence.


**Reason**

> The pathway assignment is supported by reviewer-only experimental annotation, but that external fact was absent from the evaluated input. Recognizing the sequence or its database record would be lookup or memorization, not reasoning from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein-specific pathway evidence supports D. The fact that its stated reaction modifies a saponin’s sugar chain does not make another listed process a comparably supported choice.


### Important caveats

- The cited annotations and study are reviewer-only evidence; they were not provided to the evaluated model.
- The functional evidence supports a role in saponin/triterpenoid biosynthesis, specifically a glycosylation step; it does not imply that SoGH1 synthesizes the triterpenoid core.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but its sequence alone does not establish that it acts in soapwort saponin biosynthesis rather than another biological process. The choices are distinguishable once that specific pathway role is known.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that SoGH1 participates in triterpene saponin biosynthesis by catalyzing a sugar-chain modification; this comes from the cited functional annotation and study, not from information supplied with the sequence.",
    "reason": "The pathway assignment is supported by reviewer-only experimental annotation, but that external fact was absent from the evaluated input. Recognizing the sequence or its database record would be lookup or memorization, not reasoning from the supplied sequence."
  },
  "case_id": "GO_biological_process_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C9",
      "H3",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the 449-aa SoGH1 protein from Saponaria officinalis. UniProt records an experimentally supported function in the oleanane-type triterpene saponin biosynthetic pathway and a GO annotation for triterpenoid biosynthetic process with IDA evidence. This supports choice D, though the protein’s described catalytic step is sugar-chain modification of a saponin."
  },
  "important_caveats": [
    "The cited annotations and study are reviewer-only evidence; they were not provided to the evaluated model.",
    "The functional evidence supports a role in saponin/triterpenoid biosynthesis, specifically a glycosylation step; it does not imply that SoGH1 synthesizes the triterpenoid core."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific pathway evidence supports D. The fact that its stated reaction modifies a saponin’s sugar chain does not make another listed process a comparably supported choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the 449-aa SoGH1 protein from Saponaria officinalis. UniProt records an experimentally supported function in the oleanane-type triterpene saponin biosynthetic pathway and a GO annotation for triterpenoid biosynthetic process with IDA evidence. This supports choice D, though the protein’s described catalytic step is sugar-chain modification of a saponin.",
    "evidence_ids": ["C1", "C5", "C9", "H3", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but its sequence alone does not establish that it acts in soapwort saponin biosynthesis rather than another biological process. The choices are distinguishable once that specific pathway role is known.",
    "missing_item_specific_fact": "The protein-specific finding that SoGH1 participates in triterpene saponin biosynthesis by catalyzing a sugar-chain modification; this comes from the cited functional annotation and study, not from information supplied with the sequence.",
    "reason": "The pathway assignment is supported by reviewer-only experimental annotation, but that external fact was absent from the evaluated input. Recognizing the sequence or its database record would be lookup or memorization, not reasoning from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific pathway evidence supports D. The fact that its stated reaction modifies a saponin’s sugar chain does not make another listed process a comparably supported choice."
  },
  "important_caveats": [
    "The cited annotations and study are reviewer-only evidence; they were not provided to the evaluated model.",
    "The functional evidence supports a role in saponin/triterpenoid biosynthesis, specifically a glycosylation step; it does not imply that SoGH1 synthesizes the triterpenoid core."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1I778 (Glycosyl hydrolase-like protein 1, SoGH1) from Saponaria officinalis is directly annotated with GO:0016104 'triterpenoid biosynthetic process' with IDA (Inferred from Direct Assay) evidence from PubMed:39043959. The FUNCTION comment states it is a 'Component of the oleanane-type triterpene saponins biosynthetic pathway.' The sequence matches exactly (449 AA, SHA256 confirmed). The expected answer D matches the GO annotation precisely.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [H3](#evidence-h3), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could attempt elimination: mitophagy requires mitochondrial-targeted proteins with specific domains (absent), insulin response is primarily animal signaling (inconsistent with a plant enzyme), and 'response to bacterium' implies immune recognition/signaling rather than enzymatic biosynthesis. However, the positive identification of 'triterpenoid biosynthetic process' specifically—rather than 'carbohydrate metabolic process' (also annotated) or 'saponin biosynthetic process' (also annotated)—requires knowing that this glycosyl hydrolase acts in the oleanane-type triterpene/saponin pathway. Additionally, 'response to bacterium' is not trivially eliminable because saponins are defense compounds produced in response to pathogens, blurring the distinction between biosynthesis and response.


**Missing item-specific fact**

> The specific knowledge that this glycosyl hydrolase-like protein (SoGH1) catalyzes quinovose transfer in the oleanane-type triterpene saponin biosynthetic pathway, as established experimentally in PubMed:39043959. Without this, the sequence alone does not distinguish 'triterpenoid biosynthetic process' from other glycosylation or secondary metabolite pathways, nor from 'response to bacterium' given the defense role of saponins.


**Reason**

> While elimination of mitophagy and insulin response is achievable through general reasoning, the specific assignment to 'triterpenoid biosynthetic process' over 'response to bacterium' (saponins are antimicrobial) and over other metabolic processes requires item-specific knowledge of this protein's role in saponin biosynthesis. The sequence provides no clear signal pointing to triterpenoids specifically.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Saponins are well-known antimicrobial defense compounds produced by plants in response to pathogen attack. A model reasoning that this enzyme contributes to 'response to bacterium' (option C) through production of antimicrobial triterpenoid saponins could be defensible, though GO convention places the enzyme under the biosynthetic process rather than the response process. The distinction is subtle and not clearly resolvable from sequence alone.


### Important caveats

- The UniProt entry was first public in June 2025 (PubMed:39043959, Nat. Chem. Biol. 2025), meaning this protein's function was characterized very recently. The GO IDA annotation is from direct experimental evidence.
- The protein is also annotated with GO:0016135 'saponin biosynthetic process' (IDA), which is a more specific term than the answer choice D. The question's option D (triterpenoid biosynthetic process, GO:0016104) is a parent term of saponin biosynthetic process.
- The organism (Saponaria officinalis, a plant) is not stated in the question input, making it harder to rule out animal-specific processes like insulin response from sequence alone.
- The protein name 'Glycosyl hydrolase-like protein 1' and EC 2.4.1.- (glycosyltransferase) suggest enzyme activity but do not specify the triterpenoid pathway without additional context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could attempt elimination: mitophagy requires mitochondrial-targeted proteins with specific domains (absent), insulin response is primarily animal signaling (inconsistent with a plant enzyme), and 'response to bacterium' implies immune recognition/signaling rather than enzymatic biosynthesis. However, the positive identification of 'triterpenoid biosynthetic process' specifically—rather than 'carbohydrate metabolic process' (also annotated) or 'saponin biosynthetic process' (also annotated)—requires knowing that this glycosyl hydrolase acts in the oleanane-type triterpene/saponin pathway. Additionally, 'response to bacterium' is not trivially eliminable because saponins are defense compounds produced in response to pathogens, blurring the distinction between biosynthesis and response.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific knowledge that this glycosyl hydrolase-like protein (SoGH1) catalyzes quinovose transfer in the oleanane-type triterpene saponin biosynthetic pathway, as established experimentally in PubMed:39043959. Without this, the sequence alone does not distinguish 'triterpenoid biosynthetic process' from other glycosylation or secondary metabolite pathways, nor from 'response to bacterium' given the defense role of saponins.",
    "reason": "While elimination of mitophagy and insulin response is achievable through general reasoning, the specific assignment to 'triterpenoid biosynthetic process' over 'response to bacterium' (saponins are antimicrobial) and over other metabolic processes requires item-specific knowledge of this protein's role in saponin biosynthesis. The sequence provides no clear signal pointing to triterpenoids specifically."
  },
  "case_id": "GO_biological_process_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C9",
      "H3",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1I778 (Glycosyl hydrolase-like protein 1, SoGH1) from Saponaria officinalis is directly annotated with GO:0016104 'triterpenoid biosynthetic process' with IDA (Inferred from Direct Assay) evidence from PubMed:39043959. The FUNCTION comment states it is a 'Component of the oleanane-type triterpene saponins biosynthetic pathway.' The sequence matches exactly (449 AA, SHA256 confirmed). The expected answer D matches the GO annotation precisely."
  },
  "important_caveats": [
    "The UniProt entry was first public in June 2025 (PubMed:39043959, Nat. Chem. Biol. 2025), meaning this protein's function was characterized very recently. The GO IDA annotation is from direct experimental evidence.",
    "The protein is also annotated with GO:0016135 'saponin biosynthetic process' (IDA), which is a more specific term than the answer choice D. The question's option D (triterpenoid biosynthetic process, GO:0016104) is a parent term of saponin biosynthetic process.",
    "The organism (Saponaria officinalis, a plant) is not stated in the question input, making it harder to rule out animal-specific processes like insulin response from sequence alone.",
    "The protein name 'Glycosyl hydrolase-like protein 1' and EC 2.4.1.- (glycosyltransferase) suggest enzyme activity but do not specify the triterpenoid pathway without additional context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Saponins are well-known antimicrobial defense compounds produced by plants in response to pathogen attack. A model reasoning that this enzyme contributes to 'response to bacterium' (option C) through production of antimicrobial triterpenoid saponins could be defensible, though GO convention places the enzyme under the biosynthetic process rather than the response process. The distinction is subtle and not clearly resolvable from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1I778 (Glycosyl hydrolase-like protein 1, SoGH1) from Saponaria officinalis is directly annotated with GO:0016104 'triterpenoid biosynthetic process' with IDA (Inferred from Direct Assay) evidence from PubMed:39043959. The FUNCTION comment states it is a 'Component of the oleanane-type triterpene saponins biosynthetic pathway.' The sequence matches exactly (449 AA, SHA256 confirmed). The expected answer D matches the GO annotation precisely.",
    "evidence_ids": ["C5", "C6", "C9", "H3", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could attempt elimination: mitophagy requires mitochondrial-targeted proteins with specific domains (absent), insulin response is primarily animal signaling (inconsistent with a plant enzyme), and 'response to bacterium' implies immune recognition/signaling rather than enzymatic biosynthesis. However, the positive identification of 'triterpenoid biosynthetic process' specifically—rather than 'carbohydrate metabolic process' (also annotated) or 'saponin biosynthetic process' (also annotated)—requires knowing that this glycosyl hydrolase acts in the oleanane-type triterpene/saponin pathway. Additionally, 'response to bacterium' is not trivially eliminable because saponins are defense compounds produced in response to pathogens, blurring the distinction between biosynthesis and response.",
    "missing_item_specific_fact": "The specific knowledge that this glycosyl hydrolase-like protein (SoGH1) catalyzes quinovose transfer in the oleanane-type triterpene saponin biosynthetic pathway, as established experimentally in PubMed:39043959. Without this, the sequence alone does not distinguish 'triterpenoid biosynthetic process' from other glycosylation or secondary metabolite pathways, nor from 'response to bacterium' given the defense role of saponins.",
    "reason": "While elimination of mitophagy and insulin response is achievable through general reasoning, the specific assignment to 'triterpenoid biosynthetic process' over 'response to bacterium' (saponins are antimicrobial) and over other metabolic processes requires item-specific knowledge of this protein's role in saponin biosynthesis. The sequence provides no clear signal pointing to triterpenoids specifically."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Saponins are well-known antimicrobial defense compounds produced by plants in response to pathogen attack. A model reasoning that this enzyme contributes to 'response to bacterium' (option C) through production of antimicrobial triterpenoid saponins could be defensible, though GO convention places the enzyme under the biosynthetic process rather than the response process. The distinction is subtle and not clearly resolvable from sequence alone."
  },
  "important_caveats": [
    "The UniProt entry was first public in June 2025 (PubMed:39043959, Nat. Chem. Biol. 2025), meaning this protein's function was characterized very recently. The GO IDA annotation is from direct experimental evidence.",
    "The protein is also annotated with GO:0016135 'saponin biosynthetic process' (IDA), which is a more specific term than the answer choice D. The question's option D (triterpenoid biosynthetic process, GO:0016104) is a parent term of saponin biosynthetic process.",
    "The organism (Saponaria officinalis, a plant) is not stated in the question input, making it harder to rule out animal-specific processes like insulin response from sequence alone.",
    "The protein name 'Glycosyl hydrolase-like protein 1' and EC 2.4.1.- (glycosyltransferase) suggest enzyme activity but do not specify the triterpenoid pathway without additional context."
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

**Accession:** `A0AAW1I778` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:30.134986+00:00.  

```json
"A0AAW1I778"
```

Source SHA-256: `d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:30.134986+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). Beta-glycosidase that catalyzes the transfer of a modified glucose moiety to QA-triFRXX to produce QA-triF(Q)RXX via the elongation of the C-28 sugar chain with a D-quinovose (PubMed:39043959)"}]}
```

Source SHA-256: `d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:30.134986+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:30.134986+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0016104","properties":[{"key":"GoTerm","value":"P:triterpenoid biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:36.143043+00:00.  

```text
CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.
CC       saponarioside A and saponarioside B) biosynthetic pathway, leading to
CC       the production of natural products with detergent properties used as
CC       traditional sources of soap (PubMed:39043959). Beta-glycosidase that
CC       catalyzes the transfer of a modified glucose moiety to QA-triFRXX to
CC       produce QA-triF(Q)RXX via the elongation of the C-28 sugar chain with a
CC       D-quinovose (PubMed:39043959). {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)  
**Locator:** `lines 41-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:36.143043+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)  
**Locator:** `lines 69-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:36.143043+00:00.  

```text
DR   GO; GO:0016104; P:triterpenoid biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 39. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
