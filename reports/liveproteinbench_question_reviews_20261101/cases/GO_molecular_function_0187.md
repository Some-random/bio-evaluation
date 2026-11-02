# GO_molecular_function_0187

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — UDP-glucosyltransferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGTKELHIVMYPWLAFGHFIPYLHLSNKLAQKGHKITFLLPHRAKLQLDSQNLYPSLITLVPITVPQVDTLPLGAESTADIPLSQHGDLSIAMDRTRPEIESILSKLDPKPDLIFFDMAQWVPVIASKLGIKSVSYNIVCAISLDLVRDWYKKDDGSNVPSWTLKHDKSSHFGENISILERALIALGTPDAIGIRSCREIEGEYCDSIAERFKKPVLLSGTTLPEPSDDPLDPKWVKWLGKFEEGSVIFCCLGSQHVLDKPQLQELALGLEMTGLPFFLAIKPPLGYATLDEVLPEGFSERVRDRGVAHGGWVQQPQMLAHPSVGCFLCHCGSSSMWEALVSDTQLVLFPQIPDQALNAVLMADKLKVGVKVEREDDGGVSKEVWSRAIKSVMDKESEIAAEVKKNHTKWRDMLINEEFVNGYIDSFIKDLQDLVEK

[Multiple Choices]
A. UDP-glucosyltransferase activity
B. promoter-specific chromatin binding
C. calmodulin binding
D. URM1 activating enzyme activity
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

> The matched sequence is experimentally annotated as transferring xylose from UDP-xylose, not a glucosyl group from UDP-glucose, which is the defining activity of option A. A computational InterPro annotation assigns that GO term, but it conflicts with the reported catalytic reaction.

Citations as saved: [C6](#evidence-c6), [C7](#evidence-c7), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a plant glycosyltransferase, which makes A more plausible than the chromatin-, calmodulin-, or URM1-related alternatives.


**Missing item-specific fact**

> The enzyme's donor-substrate specificity: the reported activity uses UDP-xylose rather than UDP-glucose.


**Reason**

> Sequence-family recognition can suggest glycosyltransferase activity, but it does not establish the specific sugar transferred. Distinguishing the stated glucosyltransferase activity from the enzyme's reported xylosyltransferase activity requires protein-specific functional information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative listed option fits the reported catalytic activity. A is the closest broad class, but its wording specifies glucosyl transfer and therefore does not accurately describe the reported UDP-xylose reaction.


### Important caveats

- The matched sequence has a computational InterPro annotation for UDP-glucosyltransferase activity and an experimental annotation for the broader UDP-glycosyltransferase activity.
- The reported experimental catalytic reaction is specifically xylose transfer; the available evidence does not establish that the enzyme also catalyzes glucosyl transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a plant glycosyltransferase, which makes A more plausible than the chromatin-, calmodulin-, or URM1-related alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's donor-substrate specificity: the reported activity uses UDP-xylose rather than UDP-glucose.",
    "reason": "Sequence-family recognition can suggest glycosyltransferase activity, but it does not establish the specific sugar transferred. Distinguishing the stated glucosyltransferase activity from the enzyme's reported xylosyltransferase activity requires protein-specific functional information."
  },
  "case_id": "GO_molecular_function_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C7",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The matched sequence is experimentally annotated as transferring xylose from UDP-xylose, not a glucosyl group from UDP-glucose, which is the defining activity of option A. A computational InterPro annotation assigns that GO term, but it conflicts with the reported catalytic reaction."
  },
  "important_caveats": [
    "The matched sequence has a computational InterPro annotation for UDP-glucosyltransferase activity and an experimental annotation for the broader UDP-glycosyltransferase activity.",
    "The reported experimental catalytic reaction is specifically xylose transfer; the available evidence does not establish that the enzyme also catalyzes glucosyl transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative listed option fits the reported catalytic activity. A is the closest broad class, but its wording specifies glucosyl transfer and therefore does not accurately describe the reported UDP-xylose reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0187",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The matched sequence is experimentally annotated as transferring xylose from UDP-xylose, not a glucosyl group from UDP-glucose, which is the defining activity of option A. A computational InterPro annotation assigns that GO term, but it conflicts with the reported catalytic reaction.",
    "evidence_ids": ["C6", "C7", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a plant glycosyltransferase, which makes A more plausible than the chromatin-, calmodulin-, or URM1-related alternatives.",
    "missing_item_specific_fact": "The enzyme's donor-substrate specificity: the reported activity uses UDP-xylose rather than UDP-glucose.",
    "reason": "Sequence-family recognition can suggest glycosyltransferase activity, but it does not establish the specific sugar transferred. Distinguishing the stated glucosyltransferase activity from the enzyme's reported xylosyltransferase activity requires protein-specific functional information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative listed option fits the reported catalytic activity. A is the closest broad class, but its wording specifies glucosyl transfer and therefore does not accurately describe the reported UDP-xylose reaction."
  },
  "important_caveats": [
    "The matched sequence has a computational InterPro annotation for UDP-glucosyltransferase activity and an experimental annotation for the broader UDP-glycosyltransferase activity.",
    "The reported experimental catalytic reaction is specifically xylose transfer; the available evidence does not establish that the enzyme also catalyzes glucosyl transfer."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAW1MQS1 annotates GO:0035251 (UDP-glucosyltransferase activity) via IEA:InterPro (C7/H5), and the broader parent GO:0008194 (UDP-glycosyltransferase activity) via IDA:UniProtKB (C8/H6). The protein is named 'UDP-glucosyl transferase 79L3' (EC 2.4.2.-) and its function comment confirms glycosyltransferase activity in saponin biosynthesis. Note: the experimentally verified catalytic reaction (C6/H4) transfers D-xylose from UDP-xylose, not glucose from UDP-glucose, so the specific term GO:0035251 reflects family-level InterPro inference rather than direct substrate evidence. Nevertheless, the annotation is present and the answer is supported within the provided options.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 437-aa plant protein can be distinguished from the other options through general structural and functional reasoning: (1) Option B (promoter-specific chromatin binding) requires DNA-binding domains (zinc fingers, homeodomains, bHLH) absent from this sequence; (2) Option D (URM1 activating enzyme activity) is a small E1-like adenylation enzyme (~170 aa in yeast UBA4), incompatible with a 437-aa plant protein lacking E1 adenylation motifs; (3) Option C (calmodulin binding) is a secondary protein-protein interaction, not a primary molecular function for a large plant enzyme. The remaining option A (UDP-glucosyltransferase) is consistent with the sequence length, plant origin, and the presence of UGT-family fold features (e.g., conserved 'WVQQ' and 'CCLGSQ' motifs in the C-terminal region characteristic of plant UGT PSPG domains). Elimination of the three structurally incompatible distractors leaves A as the only viable choice.


**Missing item-specific fact**

> None critical. Positive confirmation of the exact UGT family (79L3) and substrate specificity (xylose vs glucose) requires specialized domain knowledge, but the four-option format allows elimination reasoning without this.


**Reason**

> The distractors represent fundamentally different molecular function classes (chromatin binding, protein-protein interaction, E1 enzyme) that are structurally incompatible with a 437-aa plant enzyme sequence. A biologist can eliminate B, C, and D based on general knowledge of domain architecture and enzyme size, leaving A as the only plausible option. The UGT fold recognition adds confidence but is not strictly necessary given the elimination logic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative option is defensible. The actual catalytic reaction involves UDP-xylose (not UDP-glucose), making 'UDP-glucosyltransferase' slightly imprecise, but the broader experimentally-verified term 'UDP-glycosyltransferase activity' (GO:0008194) is not among the choices. Among the four provided options, only A is compatible with the protein's identity. B, C, and D are structurally and functionally incompatible with this sequence.


### Important caveats

- The specific GO term GO:0035251 (UDP-glucosyltransferase) is annotated via IEA:InterPro (family-level inference), while the experimentally verified activity (IDA) is the broader GO:0008194 (UDP-glycosyltransferase). The actual reaction uses UDP-xylose, not UDP-glucose.
- The protein was characterized in a 2025 Nature Chemical Biology paper (PubMed:39043959) and integrated into Swiss-Prot in January 2026, making this a very recent annotation.
- The protein name 'UDP-glucosyl transferase 79L3' follows UGT family nomenclature (UGT79L3) and does not imply glucose is the transferred sugar; plant UGTs named by family number often transfer various sugars.
- The UGT fold recognition (PSPG motif, ~400-500 aa plant glycosyltransferases) is specialized but not obscure for plant biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 437-aa plant protein can be distinguished from the other options through general structural and functional reasoning: (1) Option B (promoter-specific chromatin binding) requires DNA-binding domains (zinc fingers, homeodomains, bHLH) absent from this sequence; (2) Option D (URM1 activating enzyme activity) is a small E1-like adenylation enzyme (~170 aa in yeast UBA4), incompatible with a 437-aa plant protein lacking E1 adenylation motifs; (3) Option C (calmodulin binding) is a secondary protein-protein interaction, not a primary molecular function for a large plant enzyme. The remaining option A (UDP-glucosyltransferase) is consistent with the sequence length, plant origin, and the presence of UGT-family fold features (e.g., conserved 'WVQQ' and 'CCLGSQ' motifs in the C-terminal region characteristic of plant UGT PSPG domains). Elimination of the three structurally incompatible distractors leaves A as the only viable choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Positive confirmation of the exact UGT family (79L3) and substrate specificity (xylose vs glucose) requires specialized domain knowledge, but the four-option format allows elimination reasoning without this.",
    "reason": "The distractors represent fundamentally different molecular function classes (chromatin binding, protein-protein interaction, E1 enzyme) that are structurally incompatible with a 437-aa plant enzyme sequence. A biologist can eliminate B, C, and D based on general knowledge of domain architecture and enzyme size, leaving A as the only plausible option. The UGT fold recognition adds confidence but is not strictly necessary given the elimination logic."
  },
  "case_id": "GO_molecular_function_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1MQS1 annotates GO:0035251 (UDP-glucosyltransferase activity) via IEA:InterPro (C7/H5), and the broader parent GO:0008194 (UDP-glycosyltransferase activity) via IDA:UniProtKB (C8/H6). The protein is named 'UDP-glucosyl transferase 79L3' (EC 2.4.2.-) and its function comment confirms glycosyltransferase activity in saponin biosynthesis. Note: the experimentally verified catalytic reaction (C6/H4) transfers D-xylose from UDP-xylose, not glucose from UDP-glucose, so the specific term GO:0035251 reflects family-level InterPro inference rather than direct substrate evidence. Nevertheless, the annotation is present and the answer is supported within the provided options."
  },
  "important_caveats": [
    "The specific GO term GO:0035251 (UDP-glucosyltransferase) is annotated via IEA:InterPro (family-level inference), while the experimentally verified activity (IDA) is the broader GO:0008194 (UDP-glycosyltransferase). The actual reaction uses UDP-xylose, not UDP-glucose.",
    "The protein was characterized in a 2025 Nature Chemical Biology paper (PubMed:39043959) and integrated into Swiss-Prot in January 2026, making this a very recent annotation.",
    "The protein name 'UDP-glucosyl transferase 79L3' follows UGT family nomenclature (UGT79L3) and does not imply glucose is the transferred sugar; plant UGTs named by family number often transfer various sugars.",
    "The UGT fold recognition (PSPG motif, ~400-500 aa plant glycosyltransferases) is specialized but not obscure for plant biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative option is defensible. The actual catalytic reaction involves UDP-xylose (not UDP-glucose), making 'UDP-glucosyltransferase' slightly imprecise, but the broader experimentally-verified term 'UDP-glycosyltransferase activity' (GO:0008194) is not among the choices. Among the four provided options, only A is compatible with the protein's identity. B, C, and D are structurally and functionally incompatible with this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"GO_molecular_function_0187","expected_answer_check":{"judgment":"supported","reason":"UniProt entry A0AAW1MQS1 annotates GO:0035251 (UDP-glucosyltransferase activity) via IEA:InterPro (C7/H5), and the broader parent GO:0008194 (UDP-glycosyltransferase activity) via IDA:UniProtKB (C8/H6). The protein is named 'UDP-glucosyl transferase 79L3' (EC 2.4.2.-) and its function comment confirms glycosyltransferase activity in saponin biosynthesis. Note: the experimentally verified catalytic reaction (C6/H4) transfers D-xylose from UDP-xylose, not glucose from UDP-glucose, so the specific term GO:0035251 reflects family-level InterPro inference rather than direct substrate evidence. Nevertheless, the annotation is present and the answer is supported within the provided options.","evidence_ids":["C4","C5","C6","C7","C8","H1","H3","H4","H5","H6"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The 437-aa plant protein can be distinguished from the other options through general structural and functional reasoning: (1) Option B (promoter-specific chromatin binding) requires DNA-binding domains (zinc fingers, homeodomains, bHLH) absent from this sequence; (2) Option D (URM1 activating enzyme activity) is a small E1-like adenylation enzyme (~170 aa in yeast UBA4), incompatible with a 437-aa plant protein lacking E1 adenylation motifs; (3) Option C (calmodulin binding) is a secondary protein-protein interaction, not a primary molecular function for a large plant enzyme. The remaining option A (UDP-glucosyltransferase) is consistent with the sequence length, plant origin, and the presence of UGT-family fold features (e.g., conserved 'WVQQ' and 'CCLGSQ' motifs in the C-terminal region characteristic of plant UGT PSPG domains). Elimination of the three structurally incompatible distractors leaves A as the only viable choice.","missing_item_specific_fact":"None critical. Positive confirmation of the exact UGT family (79L3) and substrate specificity (xylose vs glucose) requires specialized domain knowledge, but the four-option format allows elimination reasoning without this.","reason":"The distractors represent fundamentally different molecular function classes (chromatin binding, protein-protein interaction, E1 enzyme) that are structurally incompatible with a 437-aa plant enzyme sequence. A biologist can eliminate B, C, and D based on general knowledge of domain architecture and enzyme size, leaving A as the only plausible option. The UGT fold recognition adds confidence but is not strictly necessary given the elimination logic."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"No alternative option is defensible. The actual catalytic reaction involves UDP-xylose (not UDP-glucose), making 'UDP-glucosyltransferase' slightly imprecise, but the broader experimentally-verified term 'UDP-glycosyltransferase activity' (GO:0008194) is not among the choices. Among the four provided options, only A is compatible with the protein's identity. B, C, and D are structurally and functionally incompatible with this sequence."},"important_caveats":["The specific GO term GO:0035251 (UDP-glucosyltransferase) is annotated via IEA:InterPro (family-level inference), while the experimentally verified activity (IDA) is the broader GO:0008194 (UDP-glycosyltransferase). The actual reaction uses UDP-xylose, not UDP-glucose.","The protein was characterized in a 2025 Nature Chemical Biology paper (PubMed:39043959) and integrated into Swiss-Prot in January 2026, making this a very recent annotation.","The protein name 'UDP-glucosyl transferase 79L3' follows UGT family nomenclature (UGT79L3) and does not imply glucose is the transferred sugar; plant UGTs named by family number often transfer various sugars.","The UGT fold recognition (PSPG motif, ~400-500 aa plant glycosyltransferases) is specialized but not obscure for plant biochemistry."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_donor_difference_traced`.

> C6 transfers xylose from UDP-xylose; GO2 defines glucosyl transfer from UDP-glucose; C7 assigns the key via IEA:InterPro.

**Remaining uncertainty:** The donor distinction is literal, but the supplied reaction does not exhaustively exclude use of a second sugar donor.

Evidence checked: [C6](#evidence-c6), [C7](#evidence-c7), [GO2](#evidence-go2).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0AAW1MQS1` (recovered from dataset image-path metadata, not original question text).  
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

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:42.921794+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"2.4.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"UDP-glucosyl transferase 79L3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoUGT79L3"}]}}
```

Source SHA-256: `38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:42.921794+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). A glycosyltransferase that mediates the conversion of QA-triFR to QA-triFRX via the elongation of the C-28 sugar chain with a D-xylose (PubMed:39043959)"}]}
```

Source SHA-256: `38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:42.921794+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:85056"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"name":"3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-quillaic acid alpha-L-Rha-(1->2)-beta-D-Fuc ester + UDP-alpha-D-xylose = 3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-quillaic acid beta-D-Xyl-(1->4)-alpha-L-Rha-(1->2)-beta-D-Fuc ester + UDP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:85055"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57632"},{"database":"ChEBI","id":"CHEBI:58223"},{"database":"ChEBI","id":"CHEBI:234167"},{"database":"ChEBI","id":"CHEBI:234168"}]}}
```

Source SHA-256: `38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:42.921794+00:00.  

```json
{"database":"GO","id":"GO:0035251","properties":[{"key":"GoTerm","value":"F:UDP-glucosyltransferase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:42.921794+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0008194","properties":[{"key":"GoTerm","value":"F:UDP-glycosyltransferase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:44.890470+00:00.  

```text
ID   GT793_SAPOF             Reviewed;         437 AA.
AC   A0AAW1MQS1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=UDP-glucosyl transferase 79L3 {ECO:0000303|PubMed:39043959};
DE            Short=SoUGT79L3 {ECO:0000303|PubMed:39043959};
DE            EC=2.4.2.- {ECO:0000269|PubMed:39043959};
GN   Name=UGT79L3 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11006237m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_02G054000 {ECO:0000312|EMBL:KAK9748391.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)  
**Locator:** `lines 34-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:44.890470+00:00.  

```text
CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.
CC       saponarioside A and saponarioside B) biosynthetic pathway, leading to
CC       the production of natural products with detergent properties used as
CC       traditional sources of soap (PubMed:39043959). A glycosyltransferase
CC       that mediates the conversion of QA-triFR to QA-triFRX via the
CC       elongation of the C-28 sugar chain with a D-xylose (PubMed:39043959).
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)  
**Locator:** `lines 41-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:44.890470+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-
CC         quillaic acid alpha-L-Rha-(1->2)-beta-D-Fuc ester + UDP-alpha-D-
CC         xylose = 3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-
CC         quillaic acid beta-D-Xyl-(1->4)-alpha-L-Rha-(1->2)-beta-D-Fuc ester +
CC         UDP + H(+); Xref=Rhea:RHEA:85055, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57632, ChEBI:CHEBI:58223, ChEBI:CHEBI:234167,
CC         ChEBI:CHEBI:234168; Evidence={ECO:0000269|PubMed:39043959};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:85056;
CC         Evidence={ECO:0000269|PubMed:39043959};
```

Source SHA-256: `c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)  
**Locator:** `lines 73-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:44.890470+00:00.  

```text
DR   GO; GO:0035251; F:UDP-glucosyltransferase activity; IEA:InterPro.
```

Source SHA-256: `c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:44.890470+00:00.  

```text
DR   GO; GO:0008194; F:UDP-glycosyltransferase activity; IDA:UniProtKB.
```

Source SHA-256: `c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 216295-216303`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0035251
name: UDP-glucosyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a glucosyl group from UDP-glucose to an acceptor molecule." [PMID:19858195]
xref: Reactome:R-HSA-1912353 "Glucosylation of Pre-NOTCH by POGLUT1"
is_a: GO:0008194 ! UDP-glycosyltransferase activity
is_a: GO:0046527 ! glucosyltransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 187. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
