# GO_molecular_function_0124

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKEKGEEKMNDSRKITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRKIERIEKGDSYIPDVSSNVLKDLVQNKQLVVYTPHTGIEEFQNSEYVIVTVPTPINKQKEPDLSALIAASHYIKQNLQAGQTFIFESSTYPGTLEEVIIPIIAQSGKEVGKDYYIGYSPERIDPANQQYTVQTIPKVISGQTERCKQQVQKLYSTIFDTVVPVSSPKVAEMCKLFENIQRLVNISLVNELNILCEKLGIDFREALEAAATKPFGFTPYWPGPGIGGHCIPVDPLYFQWKARQLGQSSQLIEVAHMINEKMPQQIVTQVKELSAPPGTVFLIGIAYKKDVNDLRESPALPIIELLVNEGYKVQYHDPYISSAKIGDKIYDSIPLKKKTLEKADCILIVTDHSNIDWNICKGMKHVIDTRGVLKKVSA

[Multiple Choices]
A. carboxylic ester hydrolase activity
B. oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor
C. metal ion binding
D. transcription coregulator activity
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

> The matched protein has experimentally supported UDP-GlcNAc 6-dehydrogenase activity: its reaction oxidizes a terminal CH-OH group using NAD+, whereas option B specifically describes oxidation of a CH-CH group. UniProt does assign B as an IEA:InterPro annotation, but that computational annotation conflicts with the experimentally documented reaction chemistry.

Citations as saved: [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone may suggest a soluble enzyme, but it does not provide a defensible basis for identifying its specific substrate and reaction or distinguishing the listed catalytic classes.


**Missing item-specific fact**

> The protein's experimentally characterized UDP-GlcNAc oxidation reaction and the resulting CH-OH donor classification are absent from the input.


**Reason**

> Choosing among these precise molecular-function terms requires protein-specific functional knowledge; recognizing the sequence or relying on a database label is not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimentally characterized activity is an NAD-dependent oxidoreductase acting on a CH-OH donor, a class not listed. B is the recorded computational annotation and may be the intended label, but its specified CH-CH chemistry does not match the documented reaction.


### Important caveats

- The matched UniProt record assigns option B with IEA:InterPro evidence; this supports the provenance of the key as an annotation, not its agreement with the experimentally documented reaction.
- The experimental activity evidence applies to the sequence-matched protein, while the exact source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone may suggest a soluble enzyme, but it does not provide a defensible basis for identifying its specific substrate and reaction or distinguishing the listed catalytic classes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally characterized UDP-GlcNAc oxidation reaction and the resulting CH-OH donor classification are absent from the input.",
    "reason": "Choosing among these precise molecular-function terms requires protein-specific functional knowledge; recognizing the sequence or relying on a database label is not reasoning from the supplied input."
  },
  "case_id": "GO_molecular_function_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C6",
      "C8",
      "C9",
      "H4",
      "H6",
      "H7"
    ],
    "judgment": "contradicted",
    "reason": "The matched protein has experimentally supported UDP-GlcNAc 6-dehydrogenase activity: its reaction oxidizes a terminal CH-OH group using NAD+, whereas option B specifically describes oxidation of a CH-CH group. UniProt does assign B as an IEA:InterPro annotation, but that computational annotation conflicts with the experimentally documented reaction chemistry."
  },
  "important_caveats": [
    "The matched UniProt record assigns option B with IEA:InterPro evidence; this supports the provenance of the key as an annotation, not its agreement with the experimentally documented reaction.",
    "The experimental activity evidence applies to the sequence-matched protein, while the exact source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimentally characterized activity is an NAD-dependent oxidoreductase acting on a CH-OH donor, a class not listed. B is the recorded computational annotation and may be the intended label, but its specified CH-CH chemistry does not match the documented reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0124",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The matched protein has experimentally supported UDP-GlcNAc 6-dehydrogenase activity: its reaction oxidizes a terminal CH-OH group using NAD+, whereas option B specifically describes oxidation of a CH-CH group. UniProt does assign B as an IEA:InterPro annotation, but that computational annotation conflicts with the experimentally documented reaction chemistry.",
    "evidence_ids": ["C4", "C6", "C8", "C9", "H4", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone may suggest a soluble enzyme, but it does not provide a defensible basis for identifying its specific substrate and reaction or distinguishing the listed catalytic classes.",
    "missing_item_specific_fact": "The protein's experimentally characterized UDP-GlcNAc oxidation reaction and the resulting CH-OH donor classification are absent from the input.",
    "reason": "Choosing among these precise molecular-function terms requires protein-specific functional knowledge; recognizing the sequence or relying on a database label is not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimentally characterized activity is an NAD-dependent oxidoreductase acting on a CH-OH donor, a class not listed. B is the recorded computational annotation and may be the intended label, but its specified CH-CH chemistry does not match the documented reaction."
  },
  "important_caveats": [
    "The matched UniProt record assigns option B with IEA:InterPro evidence; this supports the provenance of the key as an annotation, not its agreement with the experimentally documented reaction.",
    "The experimental activity evidence applies to the sequence-matched protein, while the exact source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The expected answer (GO:0016628, oxidoreductase acting on the CH-CH group of donors) is contradicted by the experimental evidence. The enzyme is EC 1.1.1.136, UDP-N-acetyl-D-glucosamine 6-dehydrogenase, which catalyzes oxidation of a CH-OH group (the C6 hydroxymethyl of UDP-GlcNAc) to a carboxylate, using NAD+ as acceptor (C5, C6). EC 1.1.1.- belongs to the CH-OH subclass, not the CH-CH subclass (EC 1.3.1.-) that GO:0016628 describes. The experimentally validated GO term is GO:0047004 (UDP-N-acetylglucosamine 6-dehydrogenase activity, EXP evidence, C9/H7), whose correct parent is GO:0016616 (CH-OH group), not GO:0016628 (CH-CH group). The GO:0016628 annotation present in the database (C8/H6) carries only IEA:InterPro evidence and appears to be an erroneous automatic annotation, likely from a generic NAD-binding Rossmann-fold domain match. The experimental data clearly show CH-OH oxidation, not CH-CH dehydrogenation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a canonical Rossmann-fold NAD-binding motif (GLGYVGLPLAIHFAERGYNVVGLDK, residues ~12-35), which is the hallmark of NAD(P)-dependent oxidoreductases. This structural feature allows a model to identify the protein as an NAD-binding dehydrogenase, which uniquely matches option B among the four choices. Options A (carboxylic ester hydrolase), C (metal ion binding), and D (transcription coregulator activity) lack any sequence-level support: there are no serine hydrolase catalytic triads, no dedicated metal-binding motifs as a primary function, and no transcription-factor domains in a 423-residue bacterial enzyme. Thus, the Rossmann fold provides a concrete, sequence-grounded argument to select B over the other three options.


**Missing item-specific fact**

> None needed to distinguish B from A/C/D. However, the specific 'CH-CH group' qualifier within option B is actually incorrect for this enzyme (it should be 'CH-OH group'); no option presents the correct CH-OH variant, so the model cannot detect this error from the choices alone.


**Reason**

> A model recognizing the Rossmann-fold motif can reason that this is an NAD-dependent oxidoreductase and eliminate hydrolase, metal-binding, and transcription-coregulator options. The reasoning is grounded in a visible sequence feature and general enzymology. The incorrect CH-CH qualifier in the expected answer does not prevent selection of B as the best available option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only B describes an oxidoreductase activity, which is the only category consistent with a Rossmann-fold NAD-binding enzyme. A, C, and D are clearly incompatible with the sequence features. Although the 'CH-CH group' qualifier in B is scientifically incorrect (the enzyme acts on CH-OH), no alternative oxidoreductase option is provided, so B remains the single defensible choice.


### Important caveats

- The expected answer GO:0016628 (CH-CH group) is scientifically incorrect for EC 1.1.1.136; the correct parent GO term is GO:0016616 (CH-OH group). The IEA:InterPro annotation in UniProt appears erroneous.
- The experimentally validated annotation (EXP, PubMed:20529859) is GO:0047004 (UDP-N-acetylglucosamine 6-dehydrogenase activity), which is not offered as an option.
- The sequence match to UniProt A7GKX6 is confirmed (SHA-256 match, 423 aa, both current and historical entry version 96).
- The GO:0016628 annotation carries only IEA:InterPro evidence, indicating automatic assignment likely from a domain-level match rather than mechanistic characterization.
- The question is answerable in the sense that B is the best available option, but the benchmark key contains a factual error in the GO qualifier that would mislead a model with accurate enzymology knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a canonical Rossmann-fold NAD-binding motif (GLGYVGLPLAIHFAERGYNVVGLDK, residues ~12-35), which is the hallmark of NAD(P)-dependent oxidoreductases. This structural feature allows a model to identify the protein as an NAD-binding dehydrogenase, which uniquely matches option B among the four choices. Options A (carboxylic ester hydrolase), C (metal ion binding), and D (transcription coregulator activity) lack any sequence-level support: there are no serine hydrolase catalytic triads, no dedicated metal-binding motifs as a primary function, and no transcription-factor domains in a 423-residue bacterial enzyme. Thus, the Rossmann fold provides a concrete, sequence-grounded argument to select B over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None needed to distinguish B from A/C/D. However, the specific 'CH-CH group' qualifier within option B is actually incorrect for this enzyme (it should be 'CH-OH group'); no option presents the correct CH-OH variant, so the model cannot detect this error from the choices alone.",
    "reason": "A model recognizing the Rossmann-fold motif can reason that this is an NAD-dependent oxidoreductase and eliminate hydrolase, metal-binding, and transcription-coregulator options. The reasoning is grounded in a visible sequence feature and general enzymology. The incorrect CH-CH qualifier in the expected answer does not prevent selection of B as the best available option."
  },
  "case_id": "GO_molecular_function_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "C9",
      "H4",
      "H6",
      "H7",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The expected answer (GO:0016628, oxidoreductase acting on the CH-CH group of donors) is contradicted by the experimental evidence. The enzyme is EC 1.1.1.136, UDP-N-acetyl-D-glucosamine 6-dehydrogenase, which catalyzes oxidation of a CH-OH group (the C6 hydroxymethyl of UDP-GlcNAc) to a carboxylate, using NAD+ as acceptor (C5, C6). EC 1.1.1.- belongs to the CH-OH subclass, not the CH-CH subclass (EC 1.3.1.-) that GO:0016628 describes. The experimentally validated GO term is GO:0047004 (UDP-N-acetylglucosamine 6-dehydrogenase activity, EXP evidence, C9/H7), whose correct parent is GO:0016616 (CH-OH group), not GO:0016628 (CH-CH group). The GO:0016628 annotation present in the database (C8/H6) carries only IEA:InterPro evidence and appears to be an erroneous automatic annotation, likely from a generic NAD-binding Rossmann-fold domain match. The experimental data clearly show CH-OH oxidation, not CH-CH dehydrogenation."
  },
  "important_caveats": [
    "The expected answer GO:0016628 (CH-CH group) is scientifically incorrect for EC 1.1.1.136; the correct parent GO term is GO:0016616 (CH-OH group). The IEA:InterPro annotation in UniProt appears erroneous.",
    "The experimentally validated annotation (EXP, PubMed:20529859) is GO:0047004 (UDP-N-acetylglucosamine 6-dehydrogenase activity), which is not offered as an option.",
    "The sequence match to UniProt A7GKX6 is confirmed (SHA-256 match, 423 aa, both current and historical entry version 96).",
    "The GO:0016628 annotation carries only IEA:InterPro evidence, indicating automatic assignment likely from a domain-level match rather than mechanistic characterization.",
    "The question is answerable in the sense that B is the best available option, but the benchmark key contains a factual error in the GO qualifier that would mislead a model with accurate enzymology knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only B describes an oxidoreductase activity, which is the only category consistent with a Rossmann-fold NAD-binding enzyme. A, C, and D are clearly incompatible with the sequence features. Although the 'CH-CH group' qualifier in B is scientifically incorrect (the enzyme acts on CH-OH), no alternative oxidoreductase option is provided, so B remains the single defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0124",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The expected answer (GO:0016628, oxidoreductase acting on the CH-CH group of donors) is contradicted by the experimental evidence. The enzyme is EC 1.1.1.136, UDP-N-acetyl-D-glucosamine 6-dehydrogenase, which catalyzes oxidation of a CH-OH group (the C6 hydroxymethyl of UDP-GlcNAc) to a carboxylate, using NAD+ as acceptor (C5, C6). EC 1.1.1.- belongs to the CH-OH subclass, not the CH-CH subclass (EC 1.3.1.-) that GO:0016628 describes. The experimentally validated GO term is GO:0047004 (UDP-N-acetylglucosamine 6-dehydrogenase activity, EXP evidence, C9/H7), whose correct parent is GO:0016616 (CH-OH group), not GO:0016628 (CH-CH group). The GO:0016628 annotation present in the database (C8/H6) carries only IEA:InterPro evidence and appears to be an erroneous automatic annotation, likely from a generic NAD-binding Rossmann-fold domain match. The experimental data clearly show CH-OH oxidation, not CH-CH dehydrogenation.",
    "evidence_ids": ["C5", "C6", "C8", "C9", "H4", "H6", "H7", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a canonical Rossmann-fold NAD-binding motif (GLGYVGLPLAIHFAERGYNVVGLDK, residues ~12-35), which is the hallmark of NAD(P)-dependent oxidoreductases. This structural feature allows a model to identify the protein as an NAD-binding dehydrogenase, which uniquely matches option B among the four choices. Options A (carboxylic ester hydrolase), C (metal ion binding), and D (transcription coregulator activity) lack any sequence-level support: there are no serine hydrolase catalytic triads, no dedicated metal-binding motifs as a primary function, and no transcription-factor domains in a 423-residue bacterial enzyme. Thus, the Rossmann fold provides a concrete, sequence-grounded argument to select B over the other three options.",
    "missing_item_specific_fact": "None needed to distinguish B from A/C/D. However, the specific 'CH-CH group' qualifier within option B is actually incorrect for this enzyme (it should be 'CH-OH group'); no option presents the correct CH-OH variant, so the model cannot detect this error from the choices alone.",
    "reason": "A model recognizing the Rossmann-fold motif can reason that this is an NAD-dependent oxidoreductase and eliminate hydrolase, metal-binding, and transcription-coregulator options. The reasoning is grounded in a visible sequence feature and general enzymology. The incorrect CH-CH qualifier in the expected answer does not prevent selection of B as the best available option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only B describes an oxidoreductase activity, which is the only category consistent with a Rossmann-fold NAD-binding enzyme. A, C, and D are clearly incompatible with the sequence features. Although the 'CH-CH group' qualifier in B is scientifically incorrect (the enzyme acts on CH-OH), no alternative oxidoreductase option is provided, so B remains the single defensible choice."
  },
  "important_caveats": [
    "The expected answer GO:0016628 (CH-CH group) is scientifically incorrect for EC 1.1.1.136; the correct parent GO term is GO:0016616 (CH-OH group). The IEA:InterPro annotation in UniProt appears erroneous.",
    "The experimentally validated annotation (EXP, PubMed:20529859) is GO:0047004 (UDP-N-acetylglucosamine 6-dehydrogenase activity), which is not offered as an option.",
    "The sequence match to UniProt A7GKX6 is confirmed (SHA-256 match, 423 aa, both current and historical entry version 96).",
    "The GO:0016628 annotation carries only IEA:InterPro evidence, indicating automatic assignment likely from a domain-level match rather than mechanistic characterization.",
    "The question is answerable in the sense that B is the best available option, but the benchmark key contains a factual error in the GO qualifier that would mislead a model with accurate enzymology knowledge."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_definition_difference_traced`.

> C4/C6/C9 and H4/H7 describe UDP-GlcNAc 6-dehydrogenase (EC1.1.1.136); C8/H6 assign the CH-CH donor term via IEA:InterPro.

**Remaining uncertainty:** Oxidation of the terminal alcohol is distinct from the keyed CH-CH donor class. Current EXP and historical IEA evidence classes for the specific dehydrogenase term must remain distinct.

Evidence checked: [C4](#evidence-c4), [C6](#evidence-c6), [C8](#evidence-c8), [C9](#evidence-c9), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A7GKX6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 96. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"value":"1.1.1.136"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-N-acetyl-D-glucosamine 6-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-GlcNAc 6-dehydrogenase"}]}}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"value":"Dehydrogenase involved in the biosynthesis of the nucleotide-sugar UDP-N-acetylxylosamine (UDP-XylNAc) (PubMed:20529859). Catalyzes the conversion of UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-N-acetylglucosaminuronic acid (UDP-GlcNAcA) (PubMed:20529859). Cannot use UDP-glucose, UDP-galactose and UDP-N-acetylgalactosamine as substrates (PubMed:20529859)"}]}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:13326"}}],"reaction":{"ecNumber":"1.1.1.136","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13325"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:65040"}]}}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"database":"GO","id":"GO:0016628","properties":[{"key":"GoTerm","value":"F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"id":"GO:0047004","properties":[{"key":"GoTerm","value":"F:UDP-N-acetylglucosamine 6-dehydrogenase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 40-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-
CC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);
CC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:65040; EC=1.1.1.136;
CC         Evidence={ECO:0000269|PubMed:20529859};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;
CC         Evidence={ECO:0000269|PubMed:20529859};
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 66-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
DR   GO; GO:0016628; F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor; IEA:InterPro.
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 67-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
DR   GO; GO:0047004; F:UDP-N-acetylglucosamine 6-dehydrogenase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 128398-128409`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016628
name: oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor
namespace: molecular_function
def: "Catalysis of an oxidation-reduction (redox) reaction in which a CH-CH group acts as a hydrogen or electron donor and reduces NAD or NADP." [EC:1.3.1.-]
xref: EC:1.3.1.-
xref: Reactome:R-HSA-4755572 "Defective SRD5A3 does not reduce pPNOL to DCHOL"
xref: Reactome:R-HSA-9661726 "An unknown reductase reduces D-UBGN to STBN"
xref: Reactome:R-HSA-9661745 "An unknown BILR reduces BIL to D-UBGN"
is_a: GO:0016627 ! oxidoreductase activity, acting on the CH-CH group of donors
property_value: skos:exactMatch EC:1.3.1.-

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
