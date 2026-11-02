# catalytic_activity_0078

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGQTLSEPVVEKTSEKGEDDRLIYGVSAMQGWRISMEDAHTAELNLPPPDNDTKTHPDRLSFFGVFDGHGGDKVALFAGENIHNIVFKQESFKSGDYAQGLKDGFLATDRAILNDPKYEEEVSGCTACVTLIAGNKLYVANAGDSRSVLGIKGRAKPLSNDHKPQLETEKNRITAAGGFVDFGRVNGNLALSRAIGDFEFKKSAELSPENQIVTAFPDVEVHELTEEDEFLVIACDGIWDCQSSQAVVEFVRRGIAAKQDLDKICENMMDNCLASNSETGGVGCDNMTMVIIGFLHGKTKEEWYDEIAKRVANGDGPCAPPEYAEFRGPGVHHNYEDSDSGYDVDADSGGKFSLAGSRGRIIFLGDGTEVLTGSDDTEMFDNADEDKDLASQVPKSSGKTDAKEETEAKPAPEAESSKPADGSEKKQDEKTPEESKKD

[Multiple Choices]
A. Cd(2+)(in) = Cd(2+)(out)
B. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
C. 2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol
D. a quinone + NADH + H(+) = a quinol + NAD(+)
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

> The exact supplied sequence matches the UniProt entry annotated as a protein phosphatase 2C homolog, and that entry lists option B as a catalytic reaction. The reaction annotation is supported by a computational PROSITE-ProRule inference, rather than direct experimental evidence in the supplied reviewer excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs consistent with a metal-dependent PP2C-family phosphatase catalytic domain. That supports protein dephosphorylation and distinguishes B from the ion-transport, cardiolipin-synthesis, and NADH:quinone-reduction alternatives.


**Missing item-specific fact**

> No item-specific fact is necessary to distinguish the broad reaction class among these choices, although the precise annotation for this protein is not provided in the question.


**Reason**

> The sequence and options offer a meaningful family-level biological basis for selecting a protein phosphatase reaction; this does not establish the activity by experiment or independently verify every substrate detail.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices represent distinct reaction classes, and the sequence’s phosphatase-family features support B over the alternatives.


### Important caveats

- The exact sequence match and database reaction annotation are reviewer-only evidence, not information supplied to the evaluated model.
- The cited serine-phosphatase reaction is annotated computationally; the entry also lists threonine dephosphorylation by similarity to another protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs consistent with a metal-dependent PP2C-family phosphatase catalytic domain. That supports protein dephosphorylation and distinguishes B from the ion-transport, cardiolipin-synthesis, and NADH:quinone-reduction alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is necessary to distinguish the broad reaction class among these choices, although the precise annotation for this protein is not provided in the question.",
    "reason": "The sequence and options offer a meaningful family-level biological basis for selecting a protein phosphatase reaction; this does not establish the activity by experiment or independently verify every substrate detail."
  },
  "case_id": "catalytic_activity_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as a protein phosphatase 2C homolog, and that entry lists option B as a catalytic reaction. The reaction annotation is supported by a computational PROSITE-ProRule inference, rather than direct experimental evidence in the supplied reviewer excerpts."
  },
  "important_caveats": [
    "The exact sequence match and database reaction annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The cited serine-phosphatase reaction is annotated computationally; the entry also lists threonine dephosphorylation by similarity to another protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices represent distinct reaction classes, and the sequence’s phosphatase-family features support B over the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as a protein phosphatase 2C homolog, and that entry lists option B as a catalytic reaction. The reaction annotation is supported by a computational PROSITE-ProRule inference, rather than direct experimental evidence in the supplied reviewer excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs consistent with a metal-dependent PP2C-family phosphatase catalytic domain. That supports protein dephosphorylation and distinguishes B from the ion-transport, cardiolipin-synthesis, and NADH:quinone-reduction alternatives.",
    "missing_item_specific_fact": "No item-specific fact is necessary to distinguish the broad reaction class among these choices, although the precise annotation for this protein is not provided in the question.",
    "reason": "The sequence and options offer a meaningful family-level biological basis for selecting a protein phosphatase reaction; this does not establish the activity by experiment or independently verify every substrate detail."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices represent distinct reaction classes, and the sequence’s phosphatase-family features support B over the alternatives."
  },
  "important_caveats": [
    "The exact sequence match and database reaction annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The cited serine-phosphatase reaction is annotated computationally; the entry also lists threonine dephosphorylation by similarity to another protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry G0RT93 (PP2C2_HYPJQ) annotates this protein as 'Protein phosphatase 2C homolog 2' with EC 3.1.3.16, and the catalytic activity is explicitly stated as 'O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate' (RHEA:20629), matching option B verbatim. The sequence matches the benchmark sequence exactly (SHA-256 identical, 438 aa). The EC assignment carries evidence codes ECO:0000255 (PROSITE-ProRule PRU01082) and ECO:0000250 (similarity to P39966), indicating family-based computational inference rather than a direct experimental assay on this specific protein, but PP2C serine/threonine phosphatase activity is an extensively characterized family function. The gene name PTC2 and its study in the unfolded protein response pathway (PubMed:15480788) provide additional functional context.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple well-established PP2C family signature motifs: 'GVSAM' near the N-terminus, 'FDGHGGD' (the canonical PP2C metal-binding motif), 'GDSRSVLGIKG', 'GDFEFKK', 'GCDGIWDC', 'GCDNMTMVIIGFLHG', and 'GRIIFLGDGTEVL'. These are textbook PROSITE PP2C identifiers. Recognizing these motifs identifies the protein as a member of the protein phosphatase 2C family, whose established biochemical function is hydrolysis of phosphoserine/phosphothreonine residues from proteins. Among the four choices, only B describes a phosphatase reaction; A is a metal-ion transporter, C is a cardiolipin synthase (lipid transferase), and D is an NADH:quinone oxidoreductase (oxidoreductase). None of these alternative enzyme classes share PP2C sequence motifs, so identifying the PP2C fold and motifs suffices to eliminate A, C, and D and select B.


**Missing item-specific fact**

> None required beyond general knowledge of PP2C family sequence signatures and their well-characterized phosphatase function.


**Reason**

> A model with knowledge of enzyme-family sequence motifs can identify the PP2C signature elements in the supplied sequence and deduce the phosphatase function. The distractors belong to entirely different enzyme classes (transporter, lipid synthase, oxidoreductase) with no sequence resemblance to PP2C motifs. This constitutes a concrete biological argument from the supplied sequence rather than reliance on a single protein-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span four distinct enzyme classes (transporter, phosphatase, lipid transferase, oxidoreductase). The PP2C motifs in the sequence unambiguously point to the phosphatase option B. Although PP2C enzymes can also dephosphorylate threonine residues (as noted in the UniProt entry for a second reaction), no threonine-specific option is offered, and option B is the only phosphatase reaction listed.


### Important caveats

- The EC 3.1.3.16 annotation for G0RT93 is based on PROSITE-ProRule pattern matching (ECO:0000255) and similarity transfer from P39966 (ECO:0000250), not a direct enzymatic assay on this specific Trichoderma protein. However, PP2C serine/threonine phosphatase activity is an exceptionally well-characterized family function.
- The UniProt entry was first released in February 2025; the author's data-construction date and exact source snapshot are unknown, though the sequence has been stable since 2011.
- The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence-motif recognition and general enzyme-family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple well-established PP2C family signature motifs: 'GVSAM' near the N-terminus, 'FDGHGGD' (the canonical PP2C metal-binding motif), 'GDSRSVLGIKG', 'GDFEFKK', 'GCDGIWDC', 'GCDNMTMVIIGFLHG', and 'GRIIFLGDGTEVL'. These are textbook PROSITE PP2C identifiers. Recognizing these motifs identifies the protein as a member of the protein phosphatase 2C family, whose established biochemical function is hydrolysis of phosphoserine/phosphothreonine residues from proteins. Among the four choices, only B describes a phosphatase reaction; A is a metal-ion transporter, C is a cardiolipin synthase (lipid transferase), and D is an NADH:quinone oxidoreductase (oxidoreductase). None of these alternative enzyme classes share PP2C sequence motifs, so identifying the PP2C fold and motifs suffices to eliminate A, C, and D and select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required beyond general knowledge of PP2C family sequence signatures and their well-characterized phosphatase function.",
    "reason": "A model with knowledge of enzyme-family sequence motifs can identify the PP2C signature elements in the supplied sequence and deduce the phosphatase function. The distractors belong to entirely different enzyme classes (transporter, lipid synthase, oxidoreductase) with no sequence resemblance to PP2C motifs. This constitutes a concrete biological argument from the supplied sequence rather than reliance on a single protein-specific database lookup."
  },
  "case_id": "catalytic_activity_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry G0RT93 (PP2C2_HYPJQ) annotates this protein as 'Protein phosphatase 2C homolog 2' with EC 3.1.3.16, and the catalytic activity is explicitly stated as 'O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate' (RHEA:20629), matching option B verbatim. The sequence matches the benchmark sequence exactly (SHA-256 identical, 438 aa). The EC assignment carries evidence codes ECO:0000255 (PROSITE-ProRule PRU01082) and ECO:0000250 (similarity to P39966), indicating family-based computational inference rather than a direct experimental assay on this specific protein, but PP2C serine/threonine phosphatase activity is an extensively characterized family function. The gene name PTC2 and its study in the unfolded protein response pathway (PubMed:15480788) provide additional functional context."
  },
  "important_caveats": [
    "The EC 3.1.3.16 annotation for G0RT93 is based on PROSITE-ProRule pattern matching (ECO:0000255) and similarity transfer from P39966 (ECO:0000250), not a direct enzymatic assay on this specific Trichoderma protein. However, PP2C serine/threonine phosphatase activity is an exceptionally well-characterized family function.",
    "The UniProt entry was first released in February 2025; the author's data-construction date and exact source snapshot are unknown, though the sequence has been stable since 2011.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence-motif recognition and general enzyme-family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct enzyme classes (transporter, phosphatase, lipid transferase, oxidoreductase). The PP2C motifs in the sequence unambiguously point to the phosphatase option B. Although PP2C enzymes can also dephosphorylate threonine residues (as noted in the UniProt entry for a second reaction), no threonine-specific option is offered, and option B is the only phosphatase reaction listed."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry G0RT93 (PP2C2_HYPJQ) annotates this protein as 'Protein phosphatase 2C homolog 2' with EC 3.1.3.16, and the catalytic activity is explicitly stated as 'O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate' (RHEA:20629), matching option B verbatim. The sequence matches the benchmark sequence exactly (SHA-256 identical, 438 aa). The EC assignment carries evidence codes ECO:0000255 (PROSITE-ProRule PRU01082) and ECO:0000250 (similarity to P39966), indicating family-based computational inference rather than a direct experimental assay on this specific protein, but PP2C serine/threonine phosphatase activity is an extensively characterized family function. The gene name PTC2 and its study in the unfolded protein response pathway (PubMed:15480788) provide additional functional context.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple well-established PP2C family signature motifs: 'GVSAM' near the N-terminus, 'FDGHGGD' (the canonical PP2C metal-binding motif), 'GDSRSVLGIKG', 'GDFEFKK', 'GCDGIWDC', 'GCDNMTMVIIGFLHG', and 'GRIIFLGDGTEVL'. These are textbook PROSITE PP2C identifiers. Recognizing these motifs identifies the protein as a member of the protein phosphatase 2C family, whose established biochemical function is hydrolysis of phosphoserine/phosphothreonine residues from proteins. Among the four choices, only B describes a phosphatase reaction; A is a metal-ion transporter, C is a cardiolipin synthase (lipid transferase), and D is an NADH:quinone oxidoreductase (oxidoreductase). None of these alternative enzyme classes share PP2C sequence motifs, so identifying the PP2C fold and motifs suffices to eliminate A, C, and D and select B.",
    "missing_item_specific_fact": "None required beyond general knowledge of PP2C family sequence signatures and their well-characterized phosphatase function.",
    "reason": "A model with knowledge of enzyme-family sequence motifs can identify the PP2C signature elements in the supplied sequence and deduce the phosphatase function. The distractors belong to entirely different enzyme classes (transporter, lipid synthase, oxidoreductase) with no sequence resemblance to PP2C motifs. This constitutes a concrete biological argument from the supplied sequence rather than reliance on a single protein-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct enzyme classes (transporter, phosphatase, lipid transferase, oxidoreductase). The PP2C motifs in the sequence unambiguously point to the phosphatase option B. Although PP2C enzymes can also dephosphorylate threonine residues (as noted in the UniProt entry for a second reaction), no threonine-specific option is offered, and option B is the only phosphatase reaction listed."
  },
  "important_caveats": [
    "The EC 3.1.3.16 annotation for G0RT93 is based on PROSITE-ProRule pattern matching (ECO:0000255) and similarity transfer from P39966 (ECO:0000250), not a direct enzymatic assay on this specific Trichoderma protein. However, PP2C serine/threonine phosphatase activity is an exceptionally well-characterized family function.",
    "The UniProt entry was first released in February 2025; the author's data-construction date and exact source snapshot are unknown, though the sequence has been stable since 2011.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence-motif recognition and general enzyme-family knowledge."
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

**Accession:** `G0RT93` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 60. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.800559+00:00.  

```json
"G0RT93"
```

Source SHA-256: `b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.800559+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P39966","source":"UniProtKB"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Protein phosphatase 2C homolog 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PP2C-2"}]}}
```

Source SHA-256: `b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:20.800559+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01082","source":"PROSITE-ProRule"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-02T04:28:22.841847+00:00.  

```text
DE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000305};
DE            Short=PP2C-2 {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000250|UniProtKB:P39966};
```

Source SHA-256: `83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)  
**Locator:** `lines 15-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-02T04:28:22.841847+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:AAP92916.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], AND FUNCTION.
RC   STRAIN=QM6a {ECO:0000303|PubMed:15480788};
RX   PubMed=15480788; DOI=10.1007/s00438-004-1070-0;
RA   Valkonen M., Penttila M., Saloheimo M.;
RT   "The ire1 and ptc2 genes involved in the unfolded protein response pathway
RT   in the filamentous fungus Trichoderma reesei.";
RL   Mol. Genet. Genomics 272:443-451(2004).
```

Source SHA-256: `83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 60 / 1.  
**Retrieved:** 2026-11-02T04:28:22.841847+00:00.  

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

Source SHA-256: `83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
