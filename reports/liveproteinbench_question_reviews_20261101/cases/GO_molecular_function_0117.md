# GO_molecular_function_0117

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — pyridoxal phosphate binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGSLDIKQESSPLMTNPLDSEEFRRQGYMVIDFLAEYYKNIQKFPVRSQVEPGYLRKRLPESAPYEPESIETILKDVHDDIVPGLTHWQSPNYYAYFPSSGSTAGLLGETLAAGFNVVGFNWISSPASTELESIVMDWLAEMLNLPKSFTFSGDGGGVMMGTTCEAILTTITAARDRILDRIGREHINKLVVYGSDQTHCSFFKSAKIAGISPNNFRQVKTSRVNAFSMRPDALRAAIQADVDAGLVPFFLCTTVGTTSTAAVDPVALLCEVAKDYGMWVHIDAAYAGNACICPEFRHMINGVENADSFSFNAHKWFLTTLDCCCLWVKDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQITLSRRFRSLKMWLVLRSYGVDYLRNFLRSHVDMAAYFEQLVRMDGRFEVVVPRSFALVCFRLSASAVIQRLYDSCHRHGHGQKFLEEETLNDVNAELLESVNSAGQIYMTHSLVDGVYMLRFAVGATLTQTHHVTYAWKQVQDHASAVLARRINSICNC

[Multiple Choices]
A. pyridoxal phosphate binding
B. exo-alpha-sialidase activity
C. histone H3K18 acetyltransferase activity
D. actinin binding
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

> The exact sequence matches a plant aromatic amino acid decarboxylase. UniProt assigns pyridoxal phosphate binding by computational InterPro evidence, and experimentally supported decarboxylase activity is consistent with a PLP-dependent enzyme. The binding annotation is computational, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C9](#evidence-c9), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Knowing that aromatic amino acid decarboxylases commonly use PLP would favor A, but the input gives no explicit family or cofactor annotation, and the sequence alone does not provide an evident, readily interpretable cue establishing that identity.


**Missing item-specific fact**

> That this specific sequence is an aromatic amino acid decarboxylase with a computational PLP-binding annotation.


**Reason**

> Distinguishing A requires recognizing the specific enzyme family or obtaining its protein-specific annotation; the broad relationship between decarboxylation and PLP does not itself establish the identity from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports A; the other choices describe unrelated activities, with no supplied evidence supporting them.


### Important caveats

- The PLP-binding GO annotation is computational (IEA:InterPro), whereas the cited decarboxylase activities have experimental evidence.
- The sequence match and historical record support applicability to this protein, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Knowing that aromatic amino acid decarboxylases commonly use PLP would favor A, but the input gives no explicit family or cofactor annotation, and the sequence alone does not provide an evident, readily interpretable cue establishing that identity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this specific sequence is an aromatic amino acid decarboxylase with a computational PLP-binding annotation.",
    "reason": "Distinguishing A requires recognizing the specific enzyme family or obtaining its protein-specific annotation; the broad relationship between decarboxylation and PLP does not itself establish the identity from the supplied input."
  },
  "case_id": "GO_molecular_function_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "C9",
      "H4",
      "H5",
      "H6",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a plant aromatic amino acid decarboxylase. UniProt assigns pyridoxal phosphate binding by computational InterPro evidence, and experimentally supported decarboxylase activity is consistent with a PLP-dependent enzyme. The binding annotation is computational, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The PLP-binding GO annotation is computational (IEA:InterPro), whereas the cited decarboxylase activities have experimental evidence.",
    "The sequence match and historical record support applicability to this protein, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports A; the other choices describe unrelated activities, with no supplied evidence supporting them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a plant aromatic amino acid decarboxylase. UniProt assigns pyridoxal phosphate binding by computational InterPro evidence, and experimentally supported decarboxylase activity is consistent with a PLP-dependent enzyme. The binding annotation is computational, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "C9", "H4", "H5", "H6", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Knowing that aromatic amino acid decarboxylases commonly use PLP would favor A, but the input gives no explicit family or cofactor annotation, and the sequence alone does not provide an evident, readily interpretable cue establishing that identity.",
    "missing_item_specific_fact": "That this specific sequence is an aromatic amino acid decarboxylase with a computational PLP-binding annotation.",
    "reason": "Distinguishing A requires recognizing the specific enzyme family or obtaining its protein-specific annotation; the broad relationship between decarboxylation and PLP does not itself establish the identity from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports A; the other choices describe unrelated activities, with no supplied evidence supporting them."
  },
  "important_caveats": [
    "The PLP-binding GO annotation is computational (IEA:InterPro), whereas the cited decarboxylase activities have experimental evidence.",
    "The sequence match and historical record support applicability to this protein, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (UniProt A0AA51Z3J4, LwTyDC2 from Lophophora williamsii) is an aromatic amino acid decarboxylase (EC 4.1.1.25/4.1.1.28). GO:0030170 (pyridoxal phosphate binding) is annotated in the UniProt entry with IEA:InterPro evidence (C9, H8). While the evidence code is computational (InterPro domain match) rather than direct experimental, PLP-dependence is a well-established biochemical property of aromatic amino acid decarboxylases (group III PLP enzymes), where PLP is covalently bound to a catalytic lysine. The annotation is scientifically correct for this enzyme class. Among the four options, A is the only one biochemically associated with this protein.

Citations as saved: [C9](#evidence-c9), [H8](#evidence-h8), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable motifs of PLP-dependent aromatic amino acid decarboxylases (group III): the 'GSDQ' motif (residues ~230-235: 'GSDQTHCSFF'), the conserved 'GGG' motif, and the overall two-domain architecture typical of aromatic amino acid decarboxylases. A biochemist familiar with PLP-dependent enzyme families can identify these motifs and know that PLP is the essential cofactor for amino acid decarboxylases (forming a Schiff base with a catalytic lysine). The three distractors (exo-alpha-sialidase = glycosidase EC 3.2.1.18, histone H3K18 acetyltransferase = transferase, actinin binding = protein-protein interaction) are completely incompatible with the sequence features of a PLP-dependent enzyme. The reasoning chain—recognize PLP motifs → know PLP is the cofactor → select PLP binding—is general biochemistry knowledge.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify PLP-binding sequence motifs (GSDQ, GGG, conserved catalytic lysine context) and apply general knowledge that aromatic amino acid decarboxylases are PLP-dependent. This does not require memorizing a specific database entry for this particular protein. The distractors are from entirely unrelated enzyme classes and are eliminable by sequence-feature reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A is biochemically consistent with a PLP-dependent aromatic amino acid decarboxylase. Options B (glycosidase), C (acetyltransferase), and D (protein-protein binding) are incompatible with the sequence architecture and motifs. No ambiguity exists among the choices.


### Important caveats

- The GO annotation for PLP binding (GO:0030170) carries IEA:InterPro evidence, i.e., it is computationally inferred from domain matching rather than directly experimentally demonstrated for this specific protein. However, PLP-dependence is a defining biochemical property of the enzyme class.
- The 'primary molecular function' phrasing in the system prompt could arguably point toward the catalytic activity (tyrosine/L-dopa decarboxylase activity, GO:0004837/GO:0036468) rather than cofactor binding. However, since the catalytic activity terms are not among the options, PLP binding is the only correct choice.
- The UniProt entry was first released 2025-06-18, relatively recent. The historical entry version 9 (2026-01-28) confirms the same annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable motifs of PLP-dependent aromatic amino acid decarboxylases (group III): the 'GSDQ' motif (residues ~230-235: 'GSDQTHCSFF'), the conserved 'GGG' motif, and the overall two-domain architecture typical of aromatic amino acid decarboxylases. A biochemist familiar with PLP-dependent enzyme families can identify these motifs and know that PLP is the essential cofactor for amino acid decarboxylases (forming a Schiff base with a catalytic lysine). The three distractors (exo-alpha-sialidase = glycosidase EC 3.2.1.18, histone H3K18 acetyltransferase = transferase, actinin binding = protein-protein interaction) are completely incompatible with the sequence features of a PLP-dependent enzyme. The reasoning chain—recognize PLP motifs → know PLP is the cofactor → select PLP binding—is general biochemistry knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify PLP-binding sequence motifs (GSDQ, GGG, conserved catalytic lysine context) and apply general knowledge that aromatic amino acid decarboxylases are PLP-dependent. This does not require memorizing a specific database entry for this particular protein. The distractors are from entirely unrelated enzyme classes and are eliminable by sequence-feature reasoning."
  },
  "case_id": "GO_molecular_function_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C9",
      "H8",
      "C4",
      "C5",
      "C6",
      "C7",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein (UniProt A0AA51Z3J4, LwTyDC2 from Lophophora williamsii) is an aromatic amino acid decarboxylase (EC 4.1.1.25/4.1.1.28). GO:0030170 (pyridoxal phosphate binding) is annotated in the UniProt entry with IEA:InterPro evidence (C9, H8). While the evidence code is computational (InterPro domain match) rather than direct experimental, PLP-dependence is a well-established biochemical property of aromatic amino acid decarboxylases (group III PLP enzymes), where PLP is covalently bound to a catalytic lysine. The annotation is scientifically correct for this enzyme class. Among the four options, A is the only one biochemically associated with this protein."
  },
  "important_caveats": [
    "The GO annotation for PLP binding (GO:0030170) carries IEA:InterPro evidence, i.e., it is computationally inferred from domain matching rather than directly experimentally demonstrated for this specific protein. However, PLP-dependence is a defining biochemical property of the enzyme class.",
    "The 'primary molecular function' phrasing in the system prompt could arguably point toward the catalytic activity (tyrosine/L-dopa decarboxylase activity, GO:0004837/GO:0036468) rather than cofactor binding. However, since the catalytic activity terms are not among the options, PLP binding is the only correct choice.",
    "The UniProt entry was first released 2025-06-18, relatively recent. The historical entry version 9 (2026-01-28) confirms the same annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A is biochemically consistent with a PLP-dependent aromatic amino acid decarboxylase. Options B (glycosidase), C (acetyltransferase), and D (protein-protein binding) are incompatible with the sequence architecture and motifs. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (UniProt A0AA51Z3J4, LwTyDC2 from Lophophora williamsii) is an aromatic amino acid decarboxylase (EC 4.1.1.25/4.1.1.28). GO:0030170 (pyridoxal phosphate binding) is annotated in the UniProt entry with IEA:InterPro evidence (C9, H8). While the evidence code is computational (InterPro domain match) rather than direct experimental, PLP-dependence is a well-established biochemical property of aromatic amino acid decarboxylases (group III PLP enzymes), where PLP is covalently bound to a catalytic lysine. The annotation is scientifically correct for this enzyme class. Among the four options, A is the only one biochemically associated with this protein.",
    "evidence_ids": ["C9", "H8", "C4", "C5", "C6", "C7", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable motifs of PLP-dependent aromatic amino acid decarboxylases (group III): the 'GSDQ' motif (residues ~230-235: 'GSDQTHCSFF'), the conserved 'GGG' motif, and the overall two-domain architecture typical of aromatic amino acid decarboxylases. A biochemist familiar with PLP-dependent enzyme families can identify these motifs and know that PLP is the essential cofactor for amino acid decarboxylases (forming a Schiff base with a catalytic lysine). The three distractors (exo-alpha-sialidase = glycosidase EC 3.2.1.18, histone H3K18 acetyltransferase = transferase, actinin binding = protein-protein interaction) are completely incompatible with the sequence features of a PLP-dependent enzyme. The reasoning chain—recognize PLP motifs → know PLP is the cofactor → select PLP binding—is general biochemistry knowledge.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify PLP-binding sequence motifs (GSDQ, GGG, conserved catalytic lysine context) and apply general knowledge that aromatic amino acid decarboxylases are PLP-dependent. This does not require memorizing a specific database entry for this particular protein. The distractors are from entirely unrelated enzyme classes and are eliminable by sequence-feature reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A is biochemically consistent with a PLP-dependent aromatic amino acid decarboxylase. Options B (glycosidase), C (acetyltransferase), and D (protein-protein binding) are incompatible with the sequence architecture and motifs. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The GO annotation for PLP binding (GO:0030170) carries IEA:InterPro evidence, i.e., it is computationally inferred from domain matching rather than directly experimentally demonstrated for this specific protein. However, PLP-dependence is a defining biochemical property of the enzyme class.",
    "The 'primary molecular function' phrasing in the system prompt could arguably point toward the catalytic activity (tyrosine/L-dopa decarboxylase activity, GO:0004837/GO:0036468) rather than cofactor binding. However, since the catalytic activity terms are not among the options, PLP binding is the only correct choice.",
    "The UniProt entry was first released 2025-06-18, relatively recent. The historical entry version 9 (2026-01-28) confirms the same annotations."
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

**Accession:** `A0AA51Z3J4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 9. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
"A0AA51Z3J4"
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37675639","source":"PubMed"}],"value":"Aromatic amino acid decarboxylase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"37675639","source":"PubMed"}],"value":"LwTyDC1"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"value":"4.1.1.25"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"value":"4.1.1.28"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38835170","source":"PubMed"}],"value":"L-tyrosine/L-DOPA decarboxylase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38835170","source":"PubMed"}],"value":"LwTyDC2"}]}}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"value":"Aromatic amino acid decarboxylase participating in the biosynthesis of natural products derived from phenylethylamine, including mescaline, a natural hallucinogen potentially used in psychotherapeutic treatments (PubMed:37675639, PubMed:38835170). Catalyzes the decarboxylation of L-tyrosine and L-DOPA (PubMed:37675639, PubMed:38835170)"}]}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:14346"}}],"reaction":{"ecNumber":"4.1.1.25","evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"name":"L-tyrosine + H(+) = tyramine + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14345"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:58315"},{"database":"ChEBI","id":"CHEBI:327995"}]}}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:12273"}}],"reaction":{"ecNumber":"4.1.1.28","evidences":[{"evidenceCode":"ECO:0000269","id":"37675639","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38835170","source":"PubMed"}],"name":"L-dopa + H(+) = dopamine + CO2","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:12272"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:57504"},{"database":"ChEBI","id":"CHEBI:59905"}]}}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:23.611761+00:00.  

```json
{"database":"GO","id":"GO:0030170","properties":[{"key":"GoTerm","value":"F:pyridoxal phosphate binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 39-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
CC   -!- FUNCTION: Aromatic amino acid decarboxylase participating in the
CC       biosynthesis of natural products derived from phenylethylamine,
CC       including mescaline, a natural hallucinogen potentially used in
CC       psychotherapeutic treatments (PubMed:37675639, PubMed:38835170).
CC       Catalyzes the decarboxylation of L-tyrosine and L-DOPA
CC       (PubMed:37675639, PubMed:38835170). {ECO:0000269|PubMed:37675639,
CC       ECO:0000269|PubMed:38835170}.
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 46-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-tyrosine + H(+) = tyramine + CO2; Xref=Rhea:RHEA:14345,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:58315,
CC         ChEBI:CHEBI:327995; EC=4.1.1.25;
CC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14346;
CC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 53-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-dopa + H(+) = dopamine + CO2; Xref=Rhea:RHEA:12272,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57504,
CC         ChEBI:CHEBI:59905; EC=4.1.1.28;
CC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:12273;
CC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)  
**Locator:** `lines 90-90`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 9 / 2.  
**Retrieved:** 2026-11-02T04:26:27.253771+00:00.  

```text
DR   GO; GO:0030170; F:pyridoxal phosphate binding; IEA:InterPro.
```

Source SHA-256: `19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 163502-163510`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0030170
name: pyridoxal phosphate binding
namespace: molecular_function
def: "Binding to pyridoxal 5' phosphate, 3-hydroxy-5-(hydroxymethyl)-2-methyl4-pyridine carboxaldehyde 5' phosphate, the biologically active form of vitamin B6." [GOC:mah, ISBN:0198506732]
subset: goslim_metagenomics
is_a: GO:0043168 ! anion binding
is_a: GO:0070279 ! vitamin B6 binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
