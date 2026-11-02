# GO_molecular_function_0020

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — polynucleotide 5&#x27;-phosphatase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATPKSFRDNLAEILKTHDFRTVELEFRLGFQAPGEFITNINKHVWTTAKEKLGTPAQELVMVDKYIRSTPGESSRYVVFPDGQGYWEHKKKVAKETTTGGKYGVRSAFSLERRENGKPPVSFRMQRTKYRTTFVKGPWKIDFTRVESIPATDRDCESTYEIEVELYDMFYLFEKELDIIIQEGNKLVQSIVM

[Multiple Choices]
A. peptidyl-arginine 3-dioxygenase activity
B. ubiquitin-like protein transferase activity
C. polynucleotide 5'-phosphatase activity
D. aspartic-type endopeptidase activity
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

> The supplied sequence exactly matches the PBCV-1 protein annotated as an RNA triphosphatase. Its cited experimentally supported activity is removing the gamma-phosphate from nascent mRNA, and the more specific mRNA 5′-triphosphate monophosphatase activity is a descendant of option C in GO. Thus C is supported, although it is broader than the specific activity.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO2](#evidence-go2), [GO5](#evidence-go5), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options describe distinct activities, but the supplied sequence and prompt provide no organism, protein context, or clearly diagnostic functional motif that meaningfully identifies this particular RNA triphosphatase. The broad fact that proteins can be enzymes does not distinguish these options.


**Missing item-specific fact**

> One needs the protein-specific identification or functional annotation establishing that this sequence is the PBCV-1 mRNA-capping RNA triphosphatase, including its experimentally characterized phosphate-removal activity.


**Reason**

> Choosing C depends on an item-specific protein-function fact absent from the model input; sequence recognition or recalling a database entry would be lookup or memorization, not reasoning from the supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The specific mRNA 5′-triphosphate monophosphatase activity is represented as a child of the broader polynucleotide 5′-phosphatase term, making C the matching listed option.


### Important caveats

- The reviewer-only sequence-matched record identifies the protein as PBCV-1 5′RNA triphosphatase A449R; that identity was not supplied to the evaluated model.
- The record attributes the activity to experimental evidence from a cited publication, but the primary paper was not independently retrieved or validated here.
- The exact author data and ontology snapshots are unknown; historical and current annotations support the same broad option.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options describe distinct activities, but the supplied sequence and prompt provide no organism, protein context, or clearly diagnostic functional motif that meaningfully identifies this particular RNA triphosphatase. The broad fact that proteins can be enzymes does not distinguish these options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "One needs the protein-specific identification or functional annotation establishing that this sequence is the PBCV-1 mRNA-capping RNA triphosphatase, including its experimentally characterized phosphate-removal activity.",
    "reason": "Choosing C depends on an item-specific protein-function fact absent from the model input; sequence recognition or recalling a database entry would be lookup or memorization, not reasoning from the supplied context."
  },
  "case_id": "GO_molecular_function_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C7",
      "GO2",
      "GO5",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the PBCV-1 protein annotated as an RNA triphosphatase. Its cited experimentally supported activity is removing the gamma-phosphate from nascent mRNA, and the more specific mRNA 5′-triphosphate monophosphatase activity is a descendant of option C in GO. Thus C is supported, although it is broader than the specific activity."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record identifies the protein as PBCV-1 5′RNA triphosphatase A449R; that identity was not supplied to the evaluated model.",
    "The record attributes the activity to experimental evidence from a cited publication, but the primary paper was not independently retrieved or validated here.",
    "The exact author data and ontology snapshots are unknown; historical and current annotations support the same broad option."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The specific mRNA 5′-triphosphate monophosphatase activity is represented as a child of the broader polynucleotide 5′-phosphatase term, making C the matching listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the PBCV-1 protein annotated as an RNA triphosphatase. Its cited experimentally supported activity is removing the gamma-phosphate from nascent mRNA, and the more specific mRNA 5′-triphosphate monophosphatase activity is a descendant of option C in GO. Thus C is supported, although it is broader than the specific activity.",
    "evidence_ids": ["C1", "C5", "C6", "C7", "GO2", "GO5", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options describe distinct activities, but the supplied sequence and prompt provide no organism, protein context, or clearly diagnostic functional motif that meaningfully identifies this particular RNA triphosphatase. The broad fact that proteins can be enzymes does not distinguish these options.",
    "missing_item_specific_fact": "One needs the protein-specific identification or functional annotation establishing that this sequence is the PBCV-1 mRNA-capping RNA triphosphatase, including its experimentally characterized phosphate-removal activity.",
    "reason": "Choosing C depends on an item-specific protein-function fact absent from the model input; sequence recognition or recalling a database entry would be lookup or memorization, not reasoning from the supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The specific mRNA 5′-triphosphate monophosphatase activity is represented as a child of the broader polynucleotide 5′-phosphatase term, making C the matching listed option."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record identifies the protein as PBCV-1 5′RNA triphosphatase A449R; that identity was not supplied to the evaluated model.",
    "The record attributes the activity to experimental evidence from a cited publication, but the primary paper was not independently retrieved or validated here.",
    "The exact author data and ontology snapshots are unknown; historical and current annotations support the same broad option."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q98500 (PBCV-1 5'RNA triphosphatase A449R, EC 3.6.1.74) is directly annotated with GO:0004651 (polynucleotide 5'-phosphatase activity) via IEA:InterPro (evidence H6). The more specific EXP annotation GO:0140818 (mRNA 5'-triphosphate monophosphatase activity) is_a GO:0004651 (evidence GO5). The protein catalyzes removal of gamma-phosphate from the 5'-triphosphate end of nascent mRNA (evidence C5/C6/H3/H4), which is a subtype of polynucleotide 5'-phosphatase activity. The sequence matches (193 aa, sha256 confirmed). GO:0004651 is a valid parent term encompassing this protein's catalytic function.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO2](#evidence-go2), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three of four options can be eliminated by absence of well-defined catalytic motifs: (1) Aspartic-type endopeptidase (D) requires the D-x-T-G-S (or D-T-G) catalytic dyad motif, which is absent from this sequence. (2) Ubiquitin-like protein transferase (B) requires a catalytic cysteine (E2) or specific E1/E3 catalytic architecture with conserved Cys/Lys residues in defined structural context; no such architecture is present. (3) Peptidyl-arginine 3-dioxygenase (A) requires the 2-oxoglutarate/Fe(II) facial triad (H-x-D/E...H) for iron coordination, which is absent. This leaves C (polynucleotide 5'-phosphatase) as the only remaining option, consistent with the small viral protein's role in nucleotide/nucleic acid metabolism.


**Missing item-specific fact**

> Positive identification of phosphatase activity from sequence alone requires recognizing the specific RNA triphosphatase fold (not a universally-recognized linear motif like D-T-G-S). However, elimination of the three clearly incompatible enzyme classes provides sufficient grounds to select C.


**Reason**

> The three distractors represent enzyme classes with well-characterized, structurally obligatory catalytic motifs (aspartic protease dyad, ubiquitin-transferase catalytic Cys, 2-OG dioxygenase facial triad) whose absence is verifiable from the sequence. This elimination constitutes meaningful biological reasoning. The remaining option C is a phosphatase acting on nucleic acids, consistent with a small viral protein involved in mRNA processing.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe fundamentally different enzyme classes (dioxygenase, transferase, protease) with well-defined structural requirements absent from this sequence. Only C (phosphatase acting on polynucleotides) is consistent with the protein's composition and the absence of other catalytic architectures. The GO hierarchy also confirms GO:0004651 as a valid parent of the protein's specific function.


### Important caveats

- The protein's most specific annotation is GO:0140818 (mRNA 5'-triphosphate monophosphatase activity, EXP:UniProtKB), which is a child of the answer GO:0004651. The question asks for 'primary molecular function' and GO:0004651 is a valid broader parent term.
- The GO:0004651 annotation is IEA:InterPro (computational inference), while the more specific GO:0140818 is EXP (experimental, PubMed:11160672). The answer relies on the parent term being valid, which is confirmed by the ontology is_a relationship.
- Elimination-based reasoning supports the answer, but positive identification of phosphatase activity from this 193-aa sequence without fold recognition is non-trivial. The reasoning strength depends on the evaluator accepting motif-absence arguments for the three distractors.
- The protein is from a giant dsDNA virus (PBCV-1); its involvement in mRNA capping (removing 5'-gamma-phosphate) is experimentally characterized but not obvious from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three of four options can be eliminated by absence of well-defined catalytic motifs: (1) Aspartic-type endopeptidase (D) requires the D-x-T-G-S (or D-T-G) catalytic dyad motif, which is absent from this sequence. (2) Ubiquitin-like protein transferase (B) requires a catalytic cysteine (E2) or specific E1/E3 catalytic architecture with conserved Cys/Lys residues in defined structural context; no such architecture is present. (3) Peptidyl-arginine 3-dioxygenase (A) requires the 2-oxoglutarate/Fe(II) facial triad (H-x-D/E...H) for iron coordination, which is absent. This leaves C (polynucleotide 5'-phosphatase) as the only remaining option, consistent with the small viral protein's role in nucleotide/nucleic acid metabolism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of phosphatase activity from sequence alone requires recognizing the specific RNA triphosphatase fold (not a universally-recognized linear motif like D-T-G-S). However, elimination of the three clearly incompatible enzyme classes provides sufficient grounds to select C.",
    "reason": "The three distractors represent enzyme classes with well-characterized, structurally obligatory catalytic motifs (aspartic protease dyad, ubiquitin-transferase catalytic Cys, 2-OG dioxygenase facial triad) whose absence is verifiable from the sequence. This elimination constitutes meaningful biological reasoning. The remaining option C is a phosphatase acting on nucleic acids, consistent with a small viral protein involved in mRNA processing."
  },
  "case_id": "GO_molecular_function_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO2",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "UniProt Q98500 (PBCV-1 5'RNA triphosphatase A449R, EC 3.6.1.74) is directly annotated with GO:0004651 (polynucleotide 5'-phosphatase activity) via IEA:InterPro (evidence H6). The more specific EXP annotation GO:0140818 (mRNA 5'-triphosphate monophosphatase activity) is_a GO:0004651 (evidence GO5). The protein catalyzes removal of gamma-phosphate from the 5'-triphosphate end of nascent mRNA (evidence C5/C6/H3/H4), which is a subtype of polynucleotide 5'-phosphatase activity. The sequence matches (193 aa, sha256 confirmed). GO:0004651 is a valid parent term encompassing this protein's catalytic function."
  },
  "important_caveats": [
    "The protein's most specific annotation is GO:0140818 (mRNA 5'-triphosphate monophosphatase activity, EXP:UniProtKB), which is a child of the answer GO:0004651. The question asks for 'primary molecular function' and GO:0004651 is a valid broader parent term.",
    "The GO:0004651 annotation is IEA:InterPro (computational inference), while the more specific GO:0140818 is EXP (experimental, PubMed:11160672). The answer relies on the parent term being valid, which is confirmed by the ontology is_a relationship.",
    "Elimination-based reasoning supports the answer, but positive identification of phosphatase activity from this 193-aa sequence without fold recognition is non-trivial. The reasoning strength depends on the evaluator accepting motif-absence arguments for the three distractors.",
    "The protein is from a giant dsDNA virus (PBCV-1); its involvement in mRNA capping (removing 5'-gamma-phosphate) is experimentally characterized but not obvious from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe fundamentally different enzyme classes (dioxygenase, transferase, protease) with well-defined structural requirements absent from this sequence. Only C (phosphatase acting on polynucleotides) is consistent with the protein's composition and the absence of other catalytic architectures. The GO hierarchy also confirms GO:0004651 as a valid parent of the protein's specific function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q98500 (PBCV-1 5'RNA triphosphatase A449R, EC 3.6.1.74) is directly annotated with GO:0004651 (polynucleotide 5'-phosphatase activity) via IEA:InterPro (evidence H6). The more specific EXP annotation GO:0140818 (mRNA 5'-triphosphate monophosphatase activity) is_a GO:0004651 (evidence GO5). The protein catalyzes removal of gamma-phosphate from the 5'-triphosphate end of nascent mRNA (evidence C5/C6/H3/H4), which is a subtype of polynucleotide 5'-phosphatase activity. The sequence matches (193 aa, sha256 confirmed). GO:0004651 is a valid parent term encompassing this protein's catalytic function.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "C8", "H3", "H4", "H5", "H6", "GO2", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three of four options can be eliminated by absence of well-defined catalytic motifs: (1) Aspartic-type endopeptidase (D) requires the D-x-T-G-S (or D-T-G) catalytic dyad motif, which is absent from this sequence. (2) Ubiquitin-like protein transferase (B) requires a catalytic cysteine (E2) or specific E1/E3 catalytic architecture with conserved Cys/Lys residues in defined structural context; no such architecture is present. (3) Peptidyl-arginine 3-dioxygenase (A) requires the 2-oxoglutarate/Fe(II) facial triad (H-x-D/E...H) for iron coordination, which is absent. This leaves C (polynucleotide 5'-phosphatase) as the only remaining option, consistent with the small viral protein's role in nucleotide/nucleic acid metabolism.",
    "missing_item_specific_fact": "Positive identification of phosphatase activity from sequence alone requires recognizing the specific RNA triphosphatase fold (not a universally-recognized linear motif like D-T-G-S). However, elimination of the three clearly incompatible enzyme classes provides sufficient grounds to select C.",
    "reason": "The three distractors represent enzyme classes with well-characterized, structurally obligatory catalytic motifs (aspartic protease dyad, ubiquitin-transferase catalytic Cys, 2-OG dioxygenase facial triad) whose absence is verifiable from the sequence. This elimination constitutes meaningful biological reasoning. The remaining option C is a phosphatase acting on nucleic acids, consistent with a small viral protein involved in mRNA processing."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe fundamentally different enzyme classes (dioxygenase, transferase, protease) with well-defined structural requirements absent from this sequence. Only C (phosphatase acting on polynucleotides) is consistent with the protein's composition and the absence of other catalytic architectures. The GO hierarchy also confirms GO:0004651 as a valid parent of the protein's specific function."
  },
  "important_caveats": [
    "The protein's most specific annotation is GO:0140818 (mRNA 5'-triphosphate monophosphatase activity, EXP:UniProtKB), which is a child of the answer GO:0004651. The question asks for 'primary molecular function' and GO:0004651 is a valid broader parent term.",
    "The GO:0004651 annotation is IEA:InterPro (computational inference), while the more specific GO:0140818 is EXP (experimental, PubMed:11160672). The answer relies on the parent term being valid, which is confirmed by the ontology is_a relationship.",
    "Elimination-based reasoning supports the answer, but positive identification of phosphatase activity from this 193-aa sequence without fold recognition is non-trivial. The reasoning strength depends on the evaluator accepting motif-absence arguments for the three distractors.",
    "The protein is from a giant dsDNA virus (PBCV-1); its involvement in mRNA capping (removing 5'-gamma-phosphate) is experimentally characterized but not obvious from sequence alone."
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

**Accession:** `Q98500` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 85. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
"Q98500"
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"value":"3.6.1.74"}],"fullName":{"value":"5'RNA triphosphatase A449R"}}}
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11160672","source":"PubMed"}],"value":"Catalyzes the first stes of cap formation: by removing the gamma-phosphate from the 5'-triphosphate end of nascent mRNA to yield a diphosphate end"}]}
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"11160672","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:67005"}}],"reaction":{"ecNumber":"3.6.1.74","evidences":[{"evidenceCode":"ECO:0000269","id":"11160672","source":"PubMed"}],"name":"a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:67004"},{"database":"Rhea","id":"RHEA-COMP:17164"},{"database":"Rhea","id":"RHEA-COMP:17165"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:167616"},{"database":"ChEBI","id":"CHEBI:167618"}]}}
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"11160672","source":"PubMed"}],"id":"GO:0140818","properties":[{"key":"GoTerm","value":"F:mRNA 5'-triphosphate monophosphatase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:37.911424+00:00.  

```json
{"citation":{"authors":["Ho C.K.","Gong C.","Shuman S."],"citationCrossReferences":[{"database":"PubMed","id":"11160672"},{"database":"DOI","id":"10.1128/jvi.75.4.1744-1750.2001"}],"citationType":"journal article","firstPage":"1744","id":"11160672","journal":"J. Virol.","lastPage":"1750","publicationDate":"2001","title":"RNA triphosphatase component of the mRNA capping apparatus of Paramecium bursaria Chlorella virus 1.","volume":"75"},"referenceNumber":2,"referencePositions":["FUNCTION","CHARACTERIZATION OF TRIPHOSPHATASE ACTIVITY","MUTAGENESIS OF GLU-26"]}
```

Source SHA-256: `6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)  
**Locator:** `lines 29-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:32:39.788206+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the first stes of cap formation: by removing the
CC       gamma-phosphate from the 5'-triphosphate end of nascent mRNA to yield a
CC       diphosphate end. {ECO:0000269|PubMed:11160672}.
```

Source SHA-256: `18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)  
**Locator:** `lines 32-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:32:39.788206+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end
CC         diphospho-ribonucleoside in mRNA + phosphate + H(+);
CC         Xref=Rhea:RHEA:67004, Rhea:RHEA-COMP:17164, Rhea:RHEA-COMP:17165,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:167616, ChEBI:CHEBI:167618; EC=3.6.1.74;
CC         Evidence={ECO:0000269|PubMed:11160672};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:67005;
CC         Evidence={ECO:0000269|PubMed:11160672};
```

Source SHA-256: `18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)  
**Locator:** `lines 56-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:32:39.788206+00:00.  

```text
DR   GO; GO:0140818; F:mRNA 5'-triphosphate monophosphatase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)  
**Locator:** `lines 57-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 85 / 1.  
**Retrieved:** 2026-11-02T04:32:39.788206+00:00.  

```text
DR   GO; GO:0004651; F:polynucleotide 5'-phosphatase activity; IEA:InterPro.
```

Source SHA-256: `18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 46274-46292`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004651
name: polynucleotide 5'-phosphatase activity
namespace: molecular_function
def: "Catalysis of the reaction: a 5'-phosphopolynucleotide + H2O = a polynucleotide + phosphate." [EC:3.1.3.33]
synonym: "5'-polynucleotidase activity" RELATED [EC:3.1.3.33]
synonym: "polynucleotide 5'-phosphohydrolase activity" RELATED [EC:3.1.3.33]
synonym: "polynucleotide 5'-triphosphatase activity" RELATED [EC:3.1.3.33]
xref: EC:3.1.3.33
xref: MetaCyc:RXN-21861
xref: Reactome:R-HSA-77078 "Hydrolysis of the 5'-end of the nascent transcript by the capping enzyme"
xref: Reactome:R-HSA-9923980 "NS3 cleaves triphosphate moiety of genomic +ssRNA"
xref: RHEA:67772
xref: RHEA:67776
is_a: GO:0016791 ! phosphatase activity
property_value: skos:exactMatch EC:3.1.3.33
property_value: skos:narrowMatch RHEA:67772
property_value: skos:narrowMatch RHEA:67776

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 443789-443809`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0140818
name: mRNA 5'-triphosphate monophosphatase activity
namespace: molecular_function
def: "A 5'-end triphospho-[mRNA] + H2O = a 5'-end diphospho-[mRNA] + H+ + phosphate." [PMID:9473487]
synonym: "mRNA 5'-phosphatase activity" EXACT []
xref: EC:3.6.1.74
xref: MetaCyc:POLYNUCLEOTIDE-5-PHOSPHATASE-RXN
xref: RHEA:11008
xref: RHEA:60828
xref: RHEA:60832
xref: RHEA:67004
is_a: GO:0004651 ! polynucleotide 5'-phosphatase activity
is_a: GO:0016462 ! pyrophosphatase activity
is_a: GO:0140098 ! catalytic activity, acting on RNA
property_value: skos:exactMatch EC:3.6.1.74
property_value: skos:exactMatch RHEA:67004
property_value: skos:narrowMatch RHEA:11008
property_value: skos:narrowMatch RHEA:60828
property_value: skos:narrowMatch RHEA:60832

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
