# GO_molecular_function_0154

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — cystathionine gamma-lyase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIAVNSRNSLNADMTSLHPETLMVHGGMKGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHTLKDGDSAVYQRLWQPGVARFETALAGLEHAEEAVAFATGMAAMTAALLAAVSAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEADIASAIQDDTGLVIVETPANPSLDLVDLDSVVSAAGNVPVLVDNTFCTPVLQQPISHGAALVLHSATKYLGGHGDAMGGIIATNADWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLDAHPAISVVHYPGLKGQDPRGLLGRQMSGGGAMIAMELAGGFDAARSFVEHCNLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLADDLIAALDASRAAA

[Multiple Choices]
A. S-adenosyl-L-methionine binding
B. ubiquitin protein ligase activity
C. amidophosphoribosyltransferase activity
D. cystathionine gamma-lyase activity
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

### Expected-answer support: contradicted

> The sequence-matched protein is experimentally annotated as an L-methionine gamma-lyase, and the cited functional evidence says it has no activity toward L-cystathionine. The D-term assignment is only computational (IEA:TreeGrafter), so it does not outweigh that evidence. The experimentally supported primary activity is not among the choices.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [C10](#evidence-c10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a PLP-dependent enzyme, but that broad family-level clue does not distinguish cystathionine gamma-lyase activity from related gamma-lyase activities with different substrate specificity.


**Missing item-specific fact**

> Whether this particular protein catalyzes a reaction on L-cystathionine; the cited experiments report that it does not and identify methionine gamma-lyase activity instead.


**Reason**

> The sequence and choices do not provide a reliable basis for resolving this specific substrate preference. The needed distinction depends on protein-specific functional characterization or an external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimental evidence supports methionine gamma-lyase activity, which is not listed. None of the offered options is supported as the protein's primary activity by the supplied sequence alone; D is contradicted by the cited substrate-specificity evidence.


### Important caveats

- The reviewer-only database record matches the supplied sequence; that record and its annotations were not provided to the evaluated model.
- The cystathionine gamma-lyase annotation is computational, whereas the methionine gamma-lyase and lack-of-cystathionine-activity evidence is linked to experimental literature.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent enzyme, but that broad family-level clue does not distinguish cystathionine gamma-lyase activity from related gamma-lyase activities with different substrate specificity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular protein catalyzes a reaction on L-cystathionine; the cited experiments report that it does not and identify methionine gamma-lyase activity instead.",
    "reason": "The sequence and choices do not provide a reliable basis for resolving this specific substrate preference. The needed distinction depends on protein-specific functional characterization or an external annotation."
  },
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "C10"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched protein is experimentally annotated as an L-methionine gamma-lyase, and the cited functional evidence says it has no activity toward L-cystathionine. The D-term assignment is only computational (IEA:TreeGrafter), so it does not outweigh that evidence. The experimentally supported primary activity is not among the choices."
  },
  "important_caveats": [
    "The reviewer-only database record matches the supplied sequence; that record and its annotations were not provided to the evaluated model.",
    "The cystathionine gamma-lyase annotation is computational, whereas the methionine gamma-lyase and lack-of-cystathionine-activity evidence is linked to experimental literature."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental evidence supports methionine gamma-lyase activity, which is not listed. None of the offered options is supported as the protein's primary activity by the supplied sequence alone; D is contradicted by the cited substrate-specificity evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched protein is experimentally annotated as an L-methionine gamma-lyase, and the cited functional evidence says it has no activity toward L-cystathionine. The D-term assignment is only computational (IEA:TreeGrafter), so it does not outweigh that evidence. The experimentally supported primary activity is not among the choices.",
    "evidence_ids": ["C5", "C8", "C10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent enzyme, but that broad family-level clue does not distinguish cystathionine gamma-lyase activity from related gamma-lyase activities with different substrate specificity.",
    "missing_item_specific_fact": "Whether this particular protein catalyzes a reaction on L-cystathionine; the cited experiments report that it does not and identify methionine gamma-lyase activity instead.",
    "reason": "The sequence and choices do not provide a reliable basis for resolving this specific substrate preference. The needed distinction depends on protein-specific functional characterization or an external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental evidence supports methionine gamma-lyase activity, which is not listed. None of the offered options is supported as the protein's primary activity by the supplied sequence alone; D is contradicted by the cited substrate-specificity evidence."
  },
  "important_caveats": [
    "The reviewer-only database record matches the supplied sequence; that record and its annotations were not provided to the evaluated model.",
    "The cystathionine gamma-lyase annotation is computational, whereas the methionine gamma-lyase and lack-of-cystathionine-activity evidence is linked to experimental literature."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein (UniProt A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum) is experimentally confirmed (ECO:0000269, PubMed:9726878 and PubMed:30940696) to catalyze alpha,gamma-elimination of L-methionine (EC 4.4.1.11) and L-homocysteine (EC 4.4.1.2), but the FUNCTION comment explicitly states it 'has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine.' The GO:0004123 (cystathionine gamma-lyase activity) annotation is solely IEA:TreeGrafter (computational homology inference) and is directly contradicted by experimental substrate-specificity data. The correct primary molecular function is methionine gamma-lyase activity (GO:0018826, EXP) or homocysteine desulfhydrase activity (GO:0047982, EXP), neither of which is offered as a choice.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs characteristic of the Cys/Met metabolism PLP-dependent enzyme family (e.g., the conserved PLP-binding lysine region, the 'GGMKGL' and 'ETALAGLE' segments typical of this superfamily). A knowledgeable biologist can identify this as a pyridoxal-phosphate-dependent gamma-lyase acting on sulfur amino acids. Among the four choices: A (SAM binding) is a binding function, B (ubiquitin ligase) is a transferase/ligase, C (amidophosphoribosyltransferase) is a transferase — none are lyases. Only D (cystathionine gamma-lyase) is a PLP-dependent carbon-sulfur lyase on a sulfur amino acid, matching the mechanistic class identifiable from sequence.


**Missing item-specific fact**

> The precise substrate specificity (methionine vs. cystathionine vs. homocysteine) cannot be unambiguously determined from sequence alone. The correct substrate is L-methionine, not L-cystathionine, but the option 'methionine gamma-lyase activity' is not offered.


**Reason**

> A model can reason from sequence motifs to identify the mechanistic class (PLP-dependent gamma-lyase on sulfur amino acids) and select D by elimination of the three mechanistically unrelated options. However, the precise substrate assignment (cystathionine vs. methionine) would require specific knowledge, and the 'correct' answer is actually experimentally contradicted.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four provided choices, only D falls within the correct mechanistic class (PLP-dependent carbon-sulfur lyase). A, B, and C are mechanistically unrelated (binding, ubiquitin ligase, amidotransferase). However, the question is fundamentally flawed because the experimentally correct answer (methionine gamma-lyase activity / homocysteine desulfhydrase activity) is not among the options, and the offered 'correct' answer (cystathionine gamma-lyase) is explicitly contradicted by experimental data.


### Important caveats

- The expected answer D is contradicted by experimental evidence: the protein has NO activity toward L-cystathionine (PubMed:9726878, PubMed:30940696). The GO:0004123 annotation is IEA:TreeGrafter only.
- The protein's true primary molecular function is L-methionine gamma-lyase activity (GO:0018826, EXP) and homocysteine desulfhydrase activity (GO:0047982, EXP). Neither is offered as a choice.
- The benchmark appears to have selected the GO:0004123 annotation from the database without recognizing it as a low-confidence computational inference contradicted by experimental data.
- The question is answerable by elimination (D is the only lyase option), but the 'correct' answer is scientifically inaccurate for this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs characteristic of the Cys/Met metabolism PLP-dependent enzyme family (e.g., the conserved PLP-binding lysine region, the 'GGMKGL' and 'ETALAGLE' segments typical of this superfamily). A knowledgeable biologist can identify this as a pyridoxal-phosphate-dependent gamma-lyase acting on sulfur amino acids. Among the four choices: A (SAM binding) is a binding function, B (ubiquitin ligase) is a transferase/ligase, C (amidophosphoribosyltransferase) is a transferase — none are lyases. Only D (cystathionine gamma-lyase) is a PLP-dependent carbon-sulfur lyase on a sulfur amino acid, matching the mechanistic class identifiable from sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise substrate specificity (methionine vs. cystathionine vs. homocysteine) cannot be unambiguously determined from sequence alone. The correct substrate is L-methionine, not L-cystathionine, but the option 'methionine gamma-lyase activity' is not offered.",
    "reason": "A model can reason from sequence motifs to identify the mechanistic class (PLP-dependent gamma-lyase on sulfur amino acids) and select D by elimination of the three mechanistically unrelated options. However, the precise substrate assignment (cystathionine vs. methionine) would require specific knowledge, and the 'correct' answer is actually experimentally contradicted."
  },
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "contradicted",
    "reason": "The protein (UniProt A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum) is experimentally confirmed (ECO:0000269, PubMed:9726878 and PubMed:30940696) to catalyze alpha,gamma-elimination of L-methionine (EC 4.4.1.11) and L-homocysteine (EC 4.4.1.2), but the FUNCTION comment explicitly states it 'has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine.' The GO:0004123 (cystathionine gamma-lyase activity) annotation is solely IEA:TreeGrafter (computational homology inference) and is directly contradicted by experimental substrate-specificity data. The correct primary molecular function is methionine gamma-lyase activity (GO:0018826, EXP) or homocysteine desulfhydrase activity (GO:0047982, EXP), neither of which is offered as a choice."
  },
  "important_caveats": [
    "The expected answer D is contradicted by experimental evidence: the protein has NO activity toward L-cystathionine (PubMed:9726878, PubMed:30940696). The GO:0004123 annotation is IEA:TreeGrafter only.",
    "The protein's true primary molecular function is L-methionine gamma-lyase activity (GO:0018826, EXP) and homocysteine desulfhydrase activity (GO:0047982, EXP). Neither is offered as a choice.",
    "The benchmark appears to have selected the GO:0004123 annotation from the database without recognizing it as a low-confidence computational inference contradicted by experimental data.",
    "The question is answerable by elimination (D is the only lyase option), but the 'correct' answer is scientifically inaccurate for this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, only D falls within the correct mechanistic class (PLP-dependent carbon-sulfur lyase). A, B, and C are mechanistically unrelated (binding, ubiquitin ligase, amidotransferase). However, the question is fundamentally flawed because the experimentally correct answer (methionine gamma-lyase activity / homocysteine desulfhydrase activity) is not among the options, and the offered 'correct' answer (cystathionine gamma-lyase) is explicitly contradicted by experimental data."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0154",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein (UniProt A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum) is experimentally confirmed (ECO:0000269, PubMed:9726878 and PubMed:30940696) to catalyze alpha,gamma-elimination of L-methionine (EC 4.4.1.11) and L-homocysteine (EC 4.4.1.2), but the FUNCTION comment explicitly states it 'has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine.' The GO:0004123 (cystathionine gamma-lyase activity) annotation is solely IEA:TreeGrafter (computational homology inference) and is directly contradicted by experimental substrate-specificity data. The correct primary molecular function is methionine gamma-lyase activity (GO:0018826, EXP) or homocysteine desulfhydrase activity (GO:0047982, EXP), neither of which is offered as a choice.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs characteristic of the Cys/Met metabolism PLP-dependent enzyme family (e.g., the conserved PLP-binding lysine region, the 'GGMKGL' and 'ETALAGLE' segments typical of this superfamily). A knowledgeable biologist can identify this as a pyridoxal-phosphate-dependent gamma-lyase acting on sulfur amino acids. Among the four choices: A (SAM binding) is a binding function, B (ubiquitin ligase) is a transferase/ligase, C (amidophosphoribosyltransferase) is a transferase — none are lyases. Only D (cystathionine gamma-lyase) is a PLP-dependent carbon-sulfur lyase on a sulfur amino acid, matching the mechanistic class identifiable from sequence.",
    "missing_item_specific_fact": "The precise substrate specificity (methionine vs. cystathionine vs. homocysteine) cannot be unambiguously determined from sequence alone. The correct substrate is L-methionine, not L-cystathionine, but the option 'methionine gamma-lyase activity' is not offered.",
    "reason": "A model can reason from sequence motifs to identify the mechanistic class (PLP-dependent gamma-lyase on sulfur amino acids) and select D by elimination of the three mechanistically unrelated options. However, the precise substrate assignment (cystathionine vs. methionine) would require specific knowledge, and the 'correct' answer is actually experimentally contradicted."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, only D falls within the correct mechanistic class (PLP-dependent carbon-sulfur lyase). A, B, and C are mechanistically unrelated (binding, ubiquitin ligase, amidotransferase). However, the question is fundamentally flawed because the experimentally correct answer (methionine gamma-lyase activity / homocysteine desulfhydrase activity) is not among the options, and the offered 'correct' answer (cystathionine gamma-lyase) is explicitly contradicted by experimental data."
  },
  "important_caveats": [
    "The expected answer D is contradicted by experimental evidence: the protein has NO activity toward L-cystathionine (PubMed:9726878, PubMed:30940696). The GO:0004123 annotation is IEA:TreeGrafter only.",
    "The protein's true primary molecular function is L-methionine gamma-lyase activity (GO:0018826, EXP) and homocysteine desulfhydrase activity (GO:0047982, EXP). Neither is offered as a choice.",
    "The benchmark appears to have selected the GO:0004123 annotation from the database without recognizing it as a low-confidence computational inference contradicted by experimental data.",
    "The question is answerable by elimination (D is the only lyase option), but the 'correct' answer is scientifically inaccurate for this specific protein."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `explicit_negative_substrate_evidence_traced`.

> C5 explicitly reports no activity toward L-cystathionine, while describing L-methionine gamma-lyase activity. C8 still assigns the keyed cystathionine gamma-lyase term via IEA:TreeGrafter; C10 assigns methionine gamma-lyase with EXP evidence. The negative-substrate statement is genuinely present and applies to the exact matched sequence.

**Remaining uncertainty:** The cited primary papers and assay conditions were not independently reviewed. This source trace preserves, rather than replaces, the model contradiction judgment.

Evidence checked: [C5](#evidence-c5), [C8](#evidence-c8), [C10](#evidence-c10).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A2H1K3G9` (recovered from dataset image-path metadata, not original question text).  
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

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"9726878","source":"PubMed"}],"value":"Catalyzes the alpha,gamma-elimination of L-methionine to produce methanethiol, 2-oxobutanoate and ammonia (PubMed:30940696, PubMed:9726878). May be responsible for the production of methanethiol associated with desirable Cheddar-type sulfur notes during cheese ripening (Probable). Is also able to catalyze the alpha,gamma-elimination of L-homocysteine and DL-selenomethionine, but has no activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine and D-methionine (PubMed:30940696, PubMed:9726878)"}]}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:23801"}}],"reaction":{"ecNumber":"4.4.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"}],"name":"L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:23800"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:16007"},{"database":"ChEBI","id":"CHEBI:16763"},{"database":"ChEBI","id":"CHEBI:28938"},{"database":"ChEBI","id":"CHEBI:57844"}]}}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"30940696","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:14502"}}],"reaction":{"ecNumber":"4.4.1.2","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"}],"name":"L-homocysteine + H2O = 2-oxobutanoate + hydrogen sulfide + NH4(+) + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14501"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16763"},{"database":"ChEBI","id":"CHEBI:28938"},{"database":"ChEBI","id":"CHEBI:29919"},{"database":"ChEBI","id":"CHEBI:58199"}]}}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"database":"GO","id":"GO:0004123","properties":[{"key":"GoTerm","value":"F:cystathionine gamma-lyase activity"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"}],"id":"GO:0047982","properties":[{"key":"GoTerm","value":"F:homocysteine desulfhydrase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.554855+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"30940696","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9726878","source":"PubMed"}],"id":"GO:0018826","properties":[{"key":"GoTerm","value":"F:methionine gamma-lyase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 50-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the alpha,gamma-elimination of L-methionine to
CC       produce methanethiol, 2-oxobutanoate and ammonia (PubMed:30940696,
CC       PubMed:9726878). May be responsible for the production of methanethiol
CC       associated with desirable Cheddar-type sulfur notes during cheese
CC       ripening (Probable). Is also able to catalyze the alpha,gamma-
CC       elimination of L-homocysteine and DL-selenomethionine, but has no
CC       activity toward L-cysteine, L-cystathionine, S-adenosyl-L-homocysteine
CC       and D-methionine (PubMed:30940696, PubMed:9726878).
CC       {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878,
CC       ECO:0000305|PubMed:9726878}.
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

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 124-124`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
DR   GO; GO:0004123; F:cystathionine gamma-lyase activity; IEA:TreeGrafter.
```

Source SHA-256: `9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 125-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
DR   GO; GO:0047982; F:homocysteine desulfhydrase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)  
**Locator:** `lines 126-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 32 / 1.  
**Retrieved:** 2026-11-01T06:27:25.782043+00:00.  

```text
DR   GO; GO:0018826; F:methionine gamma-lyase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 154. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
