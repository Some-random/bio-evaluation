# GO_molecular_function_0122

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key differ; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSIIGSFPPGGPRVEVQETRVQTDRVLTIPNILSMARLAGVPLFLWLILRPEFGGPQSDGWALLVLALSGVSDYLDGKLARRWNQISSLGRLLDPAADRLYILSTLVGLTWREILPLWLTLVLLAREAMLLVMVGILRRHGYPPPQVNFLGKAATFNLMYAFPLLLLSDGSGWIASLAAVFGWAFAGWGTTLYWWAGVLYVVQVRRLVRADVAAD

[Multiple Choices]
A. CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity
B. oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
C. sodium channel inhibitor activity
D. catalytic activity, acting on DNA
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

> The matched protein is experimentally annotated as cardiolipin synthase, transferring a phosphatidyl group to phosphatidylglycerol. Option A instead names the activity using glycerol-3-phosphate as the acceptor, a distinct reaction. A does appear as an InterPro-based computational GO annotation, but that does not establish the exact activity experimentally.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H7](#evidence-h7), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments suggest an integral membrane protein, making a membrane lipid-biosynthesis enzyme more plausible than a DNA-acting enzyme or an NAD(P)-dependent oxidoreductase. That broad clue does not identify the substrate or exact transferase activity.


**Missing item-specific fact**

> The protein-specific functional assignment and reaction, including whether it acts on phosphatidylglycerol or glycerol-3-phosphate, are not supplied in the sequence or prompt.


**Reason**

> Selecting the precise molecular function requires protein-specific annotation or experimental knowledge; the sequence’s membrane character alone cannot establish option A’s exact reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed choice is supported by the supplied sequence features, but option A’s exact acceptor-specific activity is not established by the experimental evidence; the reported cardiolipin synthase activity is absent from the choices.


### Important caveats

- The sequence matches the reviewer-identified UniProt record, but the accession and record were not supplied to the evaluated model.
- The exact GO term in option A is present as an InterPro-based inferred annotation; the cited experimental function describes a distinct reaction.
- The author’s source snapshot is unknown, and absence of evidence for an additional activity does not prove the protein lacks it.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments suggest an integral membrane protein, making a membrane lipid-biosynthesis enzyme more plausible than a DNA-acting enzyme or an NAD(P)-dependent oxidoreductase. That broad clue does not identify the substrate or exact transferase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment and reaction, including whether it acts on phosphatidylglycerol or glycerol-3-phosphate, are not supplied in the sequence or prompt.",
    "reason": "Selecting the precise molecular function requires protein-specific annotation or experimental knowledge; the sequence’s membrane character alone cannot establish option A’s exact reaction."
  },
  "case_id": "GO_molecular_function_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8",
      "H4",
      "H5",
      "H7",
      "GO1"
    ],
    "judgment": "contradicted",
    "reason": "The matched protein is experimentally annotated as cardiolipin synthase, transferring a phosphatidyl group to phosphatidylglycerol. Option A instead names the activity using glycerol-3-phosphate as the acceptor, a distinct reaction. A does appear as an InterPro-based computational GO annotation, but that does not establish the exact activity experimentally."
  },
  "important_caveats": [
    "The sequence matches the reviewer-identified UniProt record, but the accession and record were not supplied to the evaluated model.",
    "The exact GO term in option A is present as an InterPro-based inferred annotation; the cited experimental function describes a distinct reaction.",
    "The author’s source snapshot is unknown, and absence of evidence for an additional activity does not prove the protein lacks it."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed choice is supported by the supplied sequence features, but option A’s exact acceptor-specific activity is not established by the experimental evidence; the reported cardiolipin synthase activity is absent from the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0122",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The matched protein is experimentally annotated as cardiolipin synthase, transferring a phosphatidyl group to phosphatidylglycerol. Option A instead names the activity using glycerol-3-phosphate as the acceptor, a distinct reaction. A does appear as an InterPro-based computational GO annotation, but that does not establish the exact activity experimentally.",
    "evidence_ids": ["C5", "C6", "C8", "H4", "H5", "H7", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments suggest an integral membrane protein, making a membrane lipid-biosynthesis enzyme more plausible than a DNA-acting enzyme or an NAD(P)-dependent oxidoreductase. That broad clue does not identify the substrate or exact transferase activity.",
    "missing_item_specific_fact": "The protein-specific functional assignment and reaction, including whether it acts on phosphatidylglycerol or glycerol-3-phosphate, are not supplied in the sequence or prompt.",
    "reason": "Selecting the precise molecular function requires protein-specific annotation or experimental knowledge; the sequence’s membrane character alone cannot establish option A’s exact reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed choice is supported by the supplied sequence features, but option A’s exact acceptor-specific activity is not established by the experimental evidence; the reported cardiolipin synthase activity is absent from the choices."
  },
  "important_caveats": [
    "The sequence matches the reviewer-identified UniProt record, but the accession and record were not supplied to the evaluated model.",
    "The exact GO term in option A is present as an InterPro-based inferred annotation; the cited experimental function describes a distinct reaction.",
    "The author’s source snapshot is unknown, and absence of evidence for an additional activity does not prove the protein lacks it."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, EC 2.7.8.41) carries GO:0008444 'CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity' as an IEA:InterPro annotation (evidence C8/H7). However, the experimentally determined (IDA) annotation is GO:0043337 'cardiolipin synthase (CMP-forming) activity' (C7/H6), and the described catalytic reaction uses phosphatidylglycerol (not glycerol-3-phosphate) as the phosphatidyl acceptor (C5/H4, C6/H5). GO:0008444 is defined for EC 2.7.8.5 (PGP synthase, glycerol-3-phosphate acceptor). The expected answer is present as a database annotation but is a family-level IEA assignment that is less specific than the experimentally validated term. It is supported in the sense that the annotation exists on this exact sequence, but it represents a broader/less precise classification of the actual activity.

Citations as saved: [C8](#evidence-c8), [H7](#evidence-h7), [C7](#evidence-c7), [H6](#evidence-h6), [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 215-aa sequence exhibits multiple long hydrophobic stretches (e.g., positions ~25-50, ~60-90, ~100-130, ~140-170, ~175-200) consistent with a multi-pass membrane protein, plus conserved 'ARR'/'LRR' motifs characteristic of the CDP-alcohol phosphatidyltransferase (CPTase) superfamily. Option B (oxidoreductase, NAD/NADP-dependent) requires a Rossmann fold and NAD-binding motif (GxGxxG), neither of which is present. Option C (sodium channel inhibitor) typically describes small secreted cysteine-rich toxin peptides, incompatible with a 215-aa polytopic membrane protein lacking disulfide-forming cysteines. Option D (catalytic activity acting on DNA) requires DNA-binding motifs (HTH, zinc finger, etc.) and nuclear/nucleoid localization, inconsistent with a polytopic membrane protein. These eliminations leave A as the only biologically plausible choice.


**Missing item-specific fact**

> None required to distinguish A from B/C/D. However, precisely identifying GO:0008444 (PGP synthase, EC 2.7.8.5) versus GO:0043337 (cardiolipin synthase, EC 2.7.8.41) from sequence alone would require the specific acceptor-substrate discrimination that only experimental data provides; this distinction is moot because GO:0043337 is not among the choices.


**Reason**

> General knowledge of protein fold requirements (Rossmann fold for dehydrogenases, toxin architecture for channel inhibitors, DNA-binding domains for nucleases/polymerases) combined with recognition of the polytopic membrane topology and CPTase-family motifs allows meaningful elimination of B, C, and D without accessing any external database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are structurally and functionally incompatible with a multi-pass membrane protein lacking NAD-binding, toxin, or DNA-binding features. Only A (a membrane-associated phosphatidyltransferase activity) is consistent with the observed sequence architecture. No alternative option is defensible.


### Important caveats

- The expected answer (GO:0008444, EC 2.7.8.5, glycerol-3-phosphate acceptor) is annotated via IEA:InterPro (computational family assignment), whereas the experimentally validated term is GO:0043337 (cardiolipin synthase CMP-forming, EC 2.7.8.41, phosphatidylglycerol acceptor). The expected answer is thus a broader/less precise classification of the protein's true activity.
- The GO:0008444 definition explicitly specifies glycerol-3-phosphate as the phosphatidyl acceptor (RHEA:12593), whereas the protein's confirmed reaction uses phosphatidylglycerol (RHEA:32931). The annotation is family-level and not strictly accurate for the specific catalytic reaction.
- All reviewer evidence is from the current UniProt snapshot (entry version 120, 2026-09-02) and archived version 118; the author's source snapshot date is unknown but the sequence is identical (SHA-256 match).
- The identity origin (accession Q9KZP3) was inferred mechanically from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 215-aa sequence exhibits multiple long hydrophobic stretches (e.g., positions ~25-50, ~60-90, ~100-130, ~140-170, ~175-200) consistent with a multi-pass membrane protein, plus conserved 'ARR'/'LRR' motifs characteristic of the CDP-alcohol phosphatidyltransferase (CPTase) superfamily. Option B (oxidoreductase, NAD/NADP-dependent) requires a Rossmann fold and NAD-binding motif (GxGxxG), neither of which is present. Option C (sodium channel inhibitor) typically describes small secreted cysteine-rich toxin peptides, incompatible with a 215-aa polytopic membrane protein lacking disulfide-forming cysteines. Option D (catalytic activity acting on DNA) requires DNA-binding motifs (HTH, zinc finger, etc.) and nuclear/nucleoid localization, inconsistent with a polytopic membrane protein. These eliminations leave A as the only biologically plausible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required to distinguish A from B/C/D. However, precisely identifying GO:0008444 (PGP synthase, EC 2.7.8.5) versus GO:0043337 (cardiolipin synthase, EC 2.7.8.41) from sequence alone would require the specific acceptor-substrate discrimination that only experimental data provides; this distinction is moot because GO:0043337 is not among the choices.",
    "reason": "General knowledge of protein fold requirements (Rossmann fold for dehydrogenases, toxin architecture for channel inhibitors, DNA-binding domains for nucleases/polymerases) combined with recognition of the polytopic membrane topology and CPTase-family motifs allows meaningful elimination of B, C, and D without accessing any external database entry."
  },
  "case_id": "GO_molecular_function_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H7",
      "C7",
      "H6",
      "C5",
      "H4",
      "C6",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, EC 2.7.8.41) carries GO:0008444 'CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity' as an IEA:InterPro annotation (evidence C8/H7). However, the experimentally determined (IDA) annotation is GO:0043337 'cardiolipin synthase (CMP-forming) activity' (C7/H6), and the described catalytic reaction uses phosphatidylglycerol (not glycerol-3-phosphate) as the phosphatidyl acceptor (C5/H4, C6/H5). GO:0008444 is defined for EC 2.7.8.5 (PGP synthase, glycerol-3-phosphate acceptor). The expected answer is present as a database annotation but is a family-level IEA assignment that is less specific than the experimentally validated term. It is supported in the sense that the annotation exists on this exact sequence, but it represents a broader/less precise classification of the actual activity."
  },
  "important_caveats": [
    "The expected answer (GO:0008444, EC 2.7.8.5, glycerol-3-phosphate acceptor) is annotated via IEA:InterPro (computational family assignment), whereas the experimentally validated term is GO:0043337 (cardiolipin synthase CMP-forming, EC 2.7.8.41, phosphatidylglycerol acceptor). The expected answer is thus a broader/less precise classification of the protein's true activity.",
    "The GO:0008444 definition explicitly specifies glycerol-3-phosphate as the phosphatidyl acceptor (RHEA:12593), whereas the protein's confirmed reaction uses phosphatidylglycerol (RHEA:32931). The annotation is family-level and not strictly accurate for the specific catalytic reaction.",
    "All reviewer evidence is from the current UniProt snapshot (entry version 120, 2026-09-02) and archived version 118; the author's source snapshot date is unknown but the sequence is identical (SHA-256 match).",
    "The identity origin (accession Q9KZP3) was inferred mechanically from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are structurally and functionally incompatible with a multi-pass membrane protein lacking NAD-binding, toxin, or DNA-binding features. Only A (a membrane-associated phosphatidyltransferase activity) is consistent with the observed sequence architecture. No alternative option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9KZP3 (Cardiolipin synthase CMP-forming, EC 2.7.8.41) carries GO:0008444 'CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity' as an IEA:InterPro annotation (evidence C8/H7). However, the experimentally determined (IDA) annotation is GO:0043337 'cardiolipin synthase (CMP-forming) activity' (C7/H6), and the described catalytic reaction uses phosphatidylglycerol (not glycerol-3-phosphate) as the phosphatidyl acceptor (C5/H4, C6/H5). GO:0008444 is defined for EC 2.7.8.5 (PGP synthase, glycerol-3-phosphate acceptor). The expected answer is present as a database annotation but is a family-level IEA assignment that is less specific than the experimentally validated term. It is supported in the sense that the annotation exists on this exact sequence, but it represents a broader/less precise classification of the actual activity.",
    "evidence_ids": ["C8", "H7", "C7", "H6", "C5", "H4", "C6", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 215-aa sequence exhibits multiple long hydrophobic stretches (e.g., positions ~25-50, ~60-90, ~100-130, ~140-170, ~175-200) consistent with a multi-pass membrane protein, plus conserved 'ARR'/'LRR' motifs characteristic of the CDP-alcohol phosphatidyltransferase (CPTase) superfamily. Option B (oxidoreductase, NAD/NADP-dependent) requires a Rossmann fold and NAD-binding motif (GxGxxG), neither of which is present. Option C (sodium channel inhibitor) typically describes small secreted cysteine-rich toxin peptides, incompatible with a 215-aa polytopic membrane protein lacking disulfide-forming cysteines. Option D (catalytic activity acting on DNA) requires DNA-binding motifs (HTH, zinc finger, etc.) and nuclear/nucleoid localization, inconsistent with a polytopic membrane protein. These eliminations leave A as the only biologically plausible choice.",
    "missing_item_specific_fact": "None required to distinguish A from B/C/D. However, precisely identifying GO:0008444 (PGP synthase, EC 2.7.8.5) versus GO:0043337 (cardiolipin synthase, EC 2.7.8.41) from sequence alone would require the specific acceptor-substrate discrimination that only experimental data provides; this distinction is moot because GO:0043337 is not among the choices.",
    "reason": "General knowledge of protein fold requirements (Rossmann fold for dehydrogenases, toxin architecture for channel inhibitors, DNA-binding domains for nucleases/polymerases) combined with recognition of the polytopic membrane topology and CPTase-family motifs allows meaningful elimination of B, C, and D without accessing any external database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are structurally and functionally incompatible with a multi-pass membrane protein lacking NAD-binding, toxin, or DNA-binding features. Only A (a membrane-associated phosphatidyltransferase activity) is consistent with the observed sequence architecture. No alternative option is defensible."
  },
  "important_caveats": [
    "The expected answer (GO:0008444, EC 2.7.8.5, glycerol-3-phosphate acceptor) is annotated via IEA:InterPro (computational family assignment), whereas the experimentally validated term is GO:0043337 (cardiolipin synthase CMP-forming, EC 2.7.8.41, phosphatidylglycerol acceptor). The expected answer is thus a broader/less precise classification of the protein's true activity.",
    "The GO:0008444 definition explicitly specifies glycerol-3-phosphate as the phosphatidyl acceptor (RHEA:12593), whereas the protein's confirmed reaction uses phosphatidylglycerol (RHEA:32931). The annotation is family-level and not strictly accurate for the specific catalytic reaction.",
    "All reviewer evidence is from the current UniProt snapshot (entry version 120, 2026-09-02) and archived version 118; the author's source snapshot date is unknown but the sequence is identical (SHA-256 match).",
    "The identity origin (accession Q9KZP3) was inferred mechanically from dataset metadata and was not provided to the evaluated model."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `reaction_acceptor_difference_traced`.

> C5/C6/H4/H5 describe cardiolipin synthesis using phosphatidylglycerol, whereas GO1 defines the keyed glycerol-3-phosphate acceptor reaction; C8/H7 carry the key computationally.

**Remaining uncertainty:** Preserve the experimentally linked function versus ECO:0000305 reaction and IEA key evidence; another acceptor activity is not exhaustively excluded.

Evidence checked: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H7](#evidence-h7), [GO1](#evidence-go1).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q9KZP3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 118. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"19439403","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"22409773","source":"PubMed"}],"value":"Catalyzes the synthesis of cardiolipin (CL) (diphosphatidylglycerol) by specifically transferring a phosphatidyl group from CDP-diacylglycerol to phosphatidylglycerol (PG)"}]}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.8.41","evidences":[{"evidenceCode":"ECO:0000305","id":"19439403","source":"PubMed"}],"name":"a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:32931"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:58332"},{"database":"ChEBI","id":"CHEBI:60377"},{"database":"ChEBI","id":"CHEBI:62237"},{"database":"ChEBI","id":"CHEBI:64716"}]}}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"19439403","source":"PubMed"}],"id":"GO:0043337","properties":[{"key":"GoTerm","value":"F:cardiolipin synthase (CMP-forming) activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KZP3.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.611577+00:00.  

```json
{"database":"GO","id":"GO:0008444","properties":[{"key":"GoTerm","value":"F:CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `19159a513ac84423a492087d8961c46891339eef5cec5a9d995ec98e1cfe717c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 47-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the synthesis of cardiolipin (CL)
CC       (diphosphatidylglycerol) by specifically transferring a phosphatidyl
CC       group from CDP-diacylglycerol to phosphatidylglycerol (PG).
CC       {ECO:0000269|PubMed:19439403, ECO:0000269|PubMed:22409773}.
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 51-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a CDP-1,2-diacyl-sn-glycerol + a 1,2-diacyl-sn-glycero-3-
CC         phospho-(1'-sn-glycerol) = a cardiolipin + CMP + H(+);
CC         Xref=Rhea:RHEA:32931, ChEBI:CHEBI:15378, ChEBI:CHEBI:58332,
CC         ChEBI:CHEBI:60377, ChEBI:CHEBI:62237, ChEBI:CHEBI:64716; EC=2.7.8.41;
CC         Evidence={ECO:0000305|PubMed:19439403};
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 94-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
DR   GO; GO:0043337; F:cardiolipin synthase (CMP-forming); IDA:UniProtKB.
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KZP3?format=txt&versions=118)  
**Locator:** `lines 95-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 118 / 1.  
**Retrieved:** 2026-11-01T06:28:47.509754+00:00.  

```text
DR   GO; GO:0008444; F:CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity; IEA:InterPro.
```

Source SHA-256: `40068827609c34109c814e2d2c856e36a3bec9b7c2775a90bbcc5f7a21726d79`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 83359-83389`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008444
name: CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity
namespace: molecular_function
def: "Catalysis of the reaction: sn-glycerol 3-phosphate + CDP-diacylglycerol = 3-(3-sn-phosphatidyl)-sn-glycerol 1-phosphate + CMP + H+." [EC:2.7.8.5, RHEA:12593]
synonym: "3-phosphatidyl-1'-glycerol-3'-phosphate synthase activity" RELATED [EC:2.7.8.5]
synonym: "CDP-diacylglycerol:sn-glycerol-3-phosphate 3-phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
synonym: "CDPdiacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
synonym: "CDPdiacylglycerol-sn-glycerol-3-phosphate 3-phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
synonym: "CDPdiacylglycerol:glycerol-3-phosphate phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
synonym: "CDPdiacylglycerol:sn-glycero-3-phosphate phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
synonym: "cytidine 5'-diphospho-1,2-diacyl-sn-glycerol (CDPdiglyceride):sn-glycerol-3-phosphate phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
synonym: "glycerol 3-phosphate phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
synonym: "glycerol phosphate phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
synonym: "glycerophosphate phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
synonym: "PGP synthase activity" RELATED [EC:2.7.8.5]
synonym: "phosphatidylglycerol phosphate synthase activity" RELATED [EC:2.7.8.5]
synonym: "phosphatidylglycerol phosphate synthetase activity" RELATED [EC:2.7.8.5]
synonym: "phosphatidylglycerolphosphate synthase activity" RELATED [EC:2.7.8.5]
synonym: "phosphatidylglycerophosphate synthase activity" RELATED [EC:2.7.8.5]
synonym: "phosphatidylglycerophosphate synthetase activity" RELATED [EC:2.7.8.5]
synonym: "sn-glycerol-3-phosphate phosphatidyltransferase activity" RELATED [EC:2.7.8.5]
xref: EC:2.7.8.5
xref: KEGG_REACTION:R01801
xref: MetaCyc:PHOSPHAGLYPSYN-RXN
xref: Reactome:R-HSA-1482939 "CDP-DAG is converted to PGP by PGS1"
xref: RHEA:12593
is_a: GO:0017169 ! CDP-alcohol phosphatidyltransferase activity
property_value: skos:exactMatch EC:2.7.8.5
property_value: skos:exactMatch RHEA:12593

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 122. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
