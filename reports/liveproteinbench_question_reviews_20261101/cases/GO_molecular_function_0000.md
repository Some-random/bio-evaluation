# GO_molecular_function_0000

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — serine-type endopeptidase inhibitor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQRNILWISVVAAFGVFHFGECTYQDSGEDSSSMTEESRCDGPPHASRGLMNIPGWFYDGSRDQCRRYHFPDQQFDMAKNKFKTVTECRKSCRSTVPLQCFKKPPQTIRTMGLPVSTYNSTQGECVTIAVRPGQTGPNIFRREVECNETCRDPEYGKCAPLHIVDCGGSTGNHYNLDKQTCEKTTKNKCGPFATLEDCFKRCARYIQRKCNIPLLKSEYCDIVDLRYWYNSESKQCEEIMGCADDVYNFPTAKECWETCSSKEESRCLQPPDLGKLGIGRTRYYYNITSNRCLTTTHVAFWQNTEKKNNFKRRSDCENTCRPKHKDVKKL

[Multiple Choices]
A. tau protein binding
B. UDP-glucuronate decarboxylase activity
C. NADPH dehydrogenase activity
D. serine-type endopeptidase inhibitor activity
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

> The matched protein has a UniProt GO annotation for serine-type endopeptidase inhibitor activity, but that annotation is computational (IEA), not direct experimental evidence for this GO term. The cited experimental function reports inhibition of coagulation-factor activation and notes no inhibition of the amidolytic activity of several tested proteases; this supports an inhibitory anticoagulant role while limiting claims about direct inhibition of those enzymes.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a likely N-terminal secretion signal and repeated cysteine-rich modules consistent with Kunitz domains, which are characteristic of extracellular protease inhibitors. That pattern favors D over the unrelated binding and metabolic-enzyme choices.


**Missing item-specific fact**

> The exact target and mechanism of this particular protein's inhibitory activity are item-specific and would require annotation or experimental information; they are not needed to favor D among these choices.


**Reason**

> The sequence provides a meaningful broad family-level clue that distinguishes the inhibitor option. Identifying the protein or recalling its database entry would add detail, but is not the sole basis for choosing D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only choice aligned with the secreted, cysteine-rich inhibitor-like sequence. The experimental caveat concerns direct amidolytic inhibition of tested proteases, not a competing listed function.


### Important caveats

- The sequence matches the cited UniProt record, but the author’s exact annotation snapshot is unknown.
- The GO annotation is computationally assigned; the cited experimental description supports an anticoagulant inhibitory role but does not establish direct inhibition of the amidolytic activity of the listed proteases.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a likely N-terminal secretion signal and repeated cysteine-rich modules consistent with Kunitz domains, which are characteristic of extracellular protease inhibitors. That pattern favors D over the unrelated binding and metabolic-enzyme choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact target and mechanism of this particular protein's inhibitory activity are item-specific and would require annotation or experimental information; they are not needed to favor D among these choices.",
    "reason": "The sequence provides a meaningful broad family-level clue that distinguishes the inhibitor option. Identifying the protein or recalling its database entry would add detail, but is not the sole basis for choosing D."
  },
  "case_id": "GO_molecular_function_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched protein has a UniProt GO annotation for serine-type endopeptidase inhibitor activity, but that annotation is computational (IEA), not direct experimental evidence for this GO term. The cited experimental function reports inhibition of coagulation-factor activation and notes no inhibition of the amidolytic activity of several tested proteases; this supports an inhibitory anticoagulant role while limiting claims about direct inhibition of those enzymes."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the author’s exact annotation snapshot is unknown.",
    "The GO annotation is computationally assigned; the cited experimental description supports an anticoagulant inhibitory role but does not establish direct inhibition of the amidolytic activity of the listed proteases."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only choice aligned with the secreted, cysteine-rich inhibitor-like sequence. The experimental caveat concerns direct amidolytic inhibition of tested proteases, not a competing listed function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched protein has a UniProt GO annotation for serine-type endopeptidase inhibitor activity, but that annotation is computational (IEA), not direct experimental evidence for this GO term. The cited experimental function reports inhibition of coagulation-factor activation and notes no inhibition of the amidolytic activity of several tested proteases; this supports an inhibitory anticoagulant role while limiting claims about direct inhibition of those enzymes.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a likely N-terminal secretion signal and repeated cysteine-rich modules consistent with Kunitz domains, which are characteristic of extracellular protease inhibitors. That pattern favors D over the unrelated binding and metabolic-enzyme choices.",
    "missing_item_specific_fact": "The exact target and mechanism of this particular protein's inhibitory activity are item-specific and would require annotation or experimental information; they are not needed to favor D among these choices.",
    "reason": "The sequence provides a meaningful broad family-level clue that distinguishes the inhibitor option. Identifying the protein or recalling its database entry would add detail, but is not the sole basis for choosing D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only choice aligned with the secreted, cysteine-rich inhibitor-like sequence. The experimental caveat concerns direct amidolytic inhibition of tested proteases, not a competing listed function."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the author’s exact annotation snapshot is unknown.",
    "The GO annotation is computationally assigned; the cited experimental description supports an anticoagulant inhibitory role but does not establish direct inhibition of the amidolytic activity of the listed proteases."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8MVC4 (Penthalaris, Ixodes scapularis) carries GO:0004867 (serine-type endopeptidase inhibitor activity) annotated via IEA:InterPro (C6) and IEA:UniProtKB-KW (H4). The experimental evidence (ECO:0000269, PubMed:15116248) confirms the protein inhibits serine proteases factor Xa and IXa (C5/H3), consistent with the GO term. The sequence is confirmed matched to the benchmark. The GO assignment is computationally inferred (IEA), but the underlying experimental data directly supports serine-protease inhibition.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple cysteine-rich motifs with spacing (C-x-C...C...C...C) consistent with Kunitz-type domains, preceded by a hydrophobic N-terminal signal peptide indicating secretion. General protein biochemistry knowledge links Kunitz domains to serine protease inhibition. Distractors B (UDP-glucuronate decarboxylase) and C (NADPH dehydrogenase) require catalytic cofactor-binding motifs (Rossmann fold, FAD/NADPH sites, decarboxylase active-site residues) absent from this sequence. Distractor A (tau protein binding) is implausible for a small secreted arthropod protein with no neuronal context.


**Missing item-specific fact**

> None strictly required; however, precise recognition of five tandem Kunitz domains from raw sequence is a specialized domain-detection skill. A model relying solely on generic cysteine-count heuristics might not confidently assign 'serine-type endopeptidase inhibitor' without Kunitz-domain knowledge.


**Reason**

> The sequence visibly displays multiple CXC...C...C...C patterns and a signal peptide, enabling a reasoning chain: cysteine-rich secreted protein → disulfide-stabilized small domains → Kunitz-like → serine protease inhibitor. The three distractors can be eliminated by absence of catalytic machinery (B, C) and biological implausibility (A). This constitutes a defensible biological argument from the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D is consistent with a secreted, cysteine-rich, Kunitz-domain-containing protein. Options B and C require entirely different structural/catalytic architectures absent from the sequence, and option A is a highly specific neuronal interaction incompatible with a tick salivary protein.


### Important caveats

- The GO:0004867 annotation is IEA (Inferred from Electronic Annotation via InterPro/keyword), not a direct experimental GO assignment; however, the underlying experimental data (PubMed:15116248) confirms serine-protease inhibition.
- The protein is a five-Kunitz TFPI; its primary characterized activity is inhibiting factor VIIa–tissue factor complex activation of factors Xa and IXa, which is a nuanced mechanism within the broad GO:0004867 category.
- The sequence provided matches the UniProt precursor (330 AA); the mature protein after signal-peptide removal is shorter.
- Recognition of Kunitz domains from raw sequence is a specialized skill; a model without domain-detection training may rely on memorization of this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple cysteine-rich motifs with spacing (C-x-C...C...C...C) consistent with Kunitz-type domains, preceded by a hydrophobic N-terminal signal peptide indicating secretion. General protein biochemistry knowledge links Kunitz domains to serine protease inhibition. Distractors B (UDP-glucuronate decarboxylase) and C (NADPH dehydrogenase) require catalytic cofactor-binding motifs (Rossmann fold, FAD/NADPH sites, decarboxylase active-site residues) absent from this sequence. Distractor A (tau protein binding) is implausible for a small secreted arthropod protein with no neuronal context.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, precise recognition of five tandem Kunitz domains from raw sequence is a specialized domain-detection skill. A model relying solely on generic cysteine-count heuristics might not confidently assign 'serine-type endopeptidase inhibitor' without Kunitz-domain knowledge.",
    "reason": "The sequence visibly displays multiple CXC...C...C...C patterns and a signal peptide, enabling a reasoning chain: cysteine-rich secreted protein → disulfide-stabilized small domains → Kunitz-like → serine protease inhibitor. The three distractors can be eliminated by absence of catalytic machinery (B, C) and biological implausibility (A). This constitutes a defensible biological argument from the supplied sequence."
  },
  "case_id": "GO_molecular_function_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8MVC4 (Penthalaris, Ixodes scapularis) carries GO:0004867 (serine-type endopeptidase inhibitor activity) annotated via IEA:InterPro (C6) and IEA:UniProtKB-KW (H4). The experimental evidence (ECO:0000269, PubMed:15116248) confirms the protein inhibits serine proteases factor Xa and IXa (C5/H3), consistent with the GO term. The sequence is confirmed matched to the benchmark. The GO assignment is computationally inferred (IEA), but the underlying experimental data directly supports serine-protease inhibition."
  },
  "important_caveats": [
    "The GO:0004867 annotation is IEA (Inferred from Electronic Annotation via InterPro/keyword), not a direct experimental GO assignment; however, the underlying experimental data (PubMed:15116248) confirms serine-protease inhibition.",
    "The protein is a five-Kunitz TFPI; its primary characterized activity is inhibiting factor VIIa–tissue factor complex activation of factors Xa and IXa, which is a nuanced mechanism within the broad GO:0004867 category.",
    "The sequence provided matches the UniProt precursor (330 AA); the mature protein after signal-peptide removal is shorter.",
    "Recognition of Kunitz domains from raw sequence is a specialized skill; a model without domain-detection training may rely on memorization of this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D is consistent with a secreted, cysteine-rich, Kunitz-domain-containing protein. Options B and C require entirely different structural/catalytic architectures absent from the sequence, and option A is a highly specific neuronal interaction incompatible with a tick salivary protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8MVC4 (Penthalaris, Ixodes scapularis) carries GO:0004867 (serine-type endopeptidase inhibitor activity) annotated via IEA:InterPro (C6) and IEA:UniProtKB-KW (H4). The experimental evidence (ECO:0000269, PubMed:15116248) confirms the protein inhibits serine proteases factor Xa and IXa (C5/H3), consistent with the GO term. The sequence is confirmed matched to the benchmark. The GO assignment is computationally inferred (IEA), but the underlying experimental data directly supports serine-protease inhibition.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple cysteine-rich motifs with spacing (C-x-C...C...C...C) consistent with Kunitz-type domains, preceded by a hydrophobic N-terminal signal peptide indicating secretion. General protein biochemistry knowledge links Kunitz domains to serine protease inhibition. Distractors B (UDP-glucuronate decarboxylase) and C (NADPH dehydrogenase) require catalytic cofactor-binding motifs (Rossmann fold, FAD/NADPH sites, decarboxylase active-site residues) absent from this sequence. Distractor A (tau protein binding) is implausible for a small secreted arthropod protein with no neuronal context.",
    "missing_item_specific_fact": "None strictly required; however, precise recognition of five tandem Kunitz domains from raw sequence is a specialized domain-detection skill. A model relying solely on generic cysteine-count heuristics might not confidently assign 'serine-type endopeptidase inhibitor' without Kunitz-domain knowledge.",
    "reason": "The sequence visibly displays multiple CXC...C...C...C patterns and a signal peptide, enabling a reasoning chain: cysteine-rich secreted protein → disulfide-stabilized small domains → Kunitz-like → serine protease inhibitor. The three distractors can be eliminated by absence of catalytic machinery (B, C) and biological implausibility (A). This constitutes a defensible biological argument from the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D is consistent with a secreted, cysteine-rich, Kunitz-domain-containing protein. Options B and C require entirely different structural/catalytic architectures absent from the sequence, and option A is a highly specific neuronal interaction incompatible with a tick salivary protein."
  },
  "important_caveats": [
    "The GO:0004867 annotation is IEA (Inferred from Electronic Annotation via InterPro/keyword), not a direct experimental GO assignment; however, the underlying experimental data (PubMed:15116248) confirms serine-protease inhibition.",
    "The protein is a five-Kunitz TFPI; its primary characterized activity is inhibiting factor VIIa–tissue factor complex activation of factors Xa and IXa, which is a nuanced mechanism within the broad GO:0004867 category.",
    "The sequence provided matches the UniProt precursor (330 AA); the mature protein after signal-peptide removal is shorter.",
    "Recognition of Kunitz domains from raw sequence is a specialized skill; a model without domain-detection training may rely on memorization of this specific protein."
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

**Accession:** `Q8MVC4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8MVC4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:23.101573+00:00.  

```json
"Q8MVC4"
```

Source SHA-256: `422cacae32c00e928adbf4a5309d527434b905851eeaa0c16ad8bfacaca85328`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8MVC4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:23.101573+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"15116248","source":"PubMed"}],"value":"Anticoagulant protein that inhibits the activation of host coagulation factors Xa (F10) and IXa (F9) by the factor VIIa-tissue factor (F7-F3) complex (PubMed:15116248). Does not inhibit the amidolytic activity of thrombin (F2), factor Xa (F10), trypsin and elastase (PubMed:15116248)"}]}
```

Source SHA-256: `422cacae32c00e928adbf4a5309d527434b905851eeaa0c16ad8bfacaca85328`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8MVC4.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:23.101573+00:00.  

```json
{"database":"GO","id":"GO:0004867","properties":[{"key":"GoTerm","value":"F:serine-type endopeptidase inhibitor activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `422cacae32c00e928adbf4a5309d527434b905851eeaa0c16ad8bfacaca85328`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8MVC4?format=txt&versions=74)  
**Locator:** `lines 30-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:32:29.047638+00:00.  

```text
CC   -!- FUNCTION: Anticoagulant protein that inhibits the activation of host
CC       coagulation factors Xa (F10) and IXa (F9) by the factor VIIa-tissue
CC       factor (F7-F3) complex (PubMed:15116248). Does not inhibit the
CC       amidolytic activity of thrombin (F2), factor Xa (F10), trypsin and
CC       elastase (PubMed:15116248). {ECO:0000269|PubMed:15116248}.
```

Source SHA-256: `64b48644632e51cc398a0e6a4a41747feaeeafbddeb8bb3617a19726afe3c707`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8MVC4?format=txt&versions=74)  
**Locator:** `lines 54-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:32:29.047638+00:00.  

```text
DR   GO; GO:0004867; F:serine-type endopeptidase inhibitor activity; IEA:UniProtKB-KW.
```

Source SHA-256: `64b48644632e51cc398a0e6a4a41747feaeeafbddeb8bb3617a19726afe3c707`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 51576-51590`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004867
name: serine-type endopeptidase inhibitor activity
namespace: molecular_function
def: "Binds to and stops, prevents or reduces the activity of a serine-type endopeptidase." [GOC:ai]
synonym: "serine protease inhibitor activity" NARROW []
synonym: "serine proteinase inhibitor activity" NARROW []
synonym: "serpin activity" NARROW []
xref: Reactome:R-HSA-158795 "fibrin multimer, crosslinked:tissue plasminogen activator (one-chain) + plasminogen activator inhibitor 1 -> fibrin multimer, crosslinked:tissue plasminogen activator (one-chain):plasminogen activator inhibitor 1"
xref: Reactome:R-HSA-158800 "fibrin multimer, crosslinked:tissue plasminogen activator (two-chain) + plasminogen activator inhibitor 1 -> fibrin multimer, crosslinked:tissue plasminogen activator (two-chain):plasminogen activator inhibitor 1"
xref: Reactome:R-HSA-158893 "alpha-2-antiplasmin + plasmin -> alpha-2-antiplasmin:plasmin"
xref: Reactome:R-HSA-159001 "urokinase plasminogen activator (two-chain):uPAR + plasminogen activator inhibitor 2 (PAI-2) -> PAI-2:urokinase plasminogen activator (two-chain):uPAR"
xref: Reactome:R-HSA-159005 "urokinase plasminogen activator (two-chain):uPAR + plasminogen activator inhibitor 1 (PAI-1) -> PAI-1:urokinase plasminogen activator (two-chain):uPAR"
is_a: GO:0004866 ! endopeptidase inhibitor activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
