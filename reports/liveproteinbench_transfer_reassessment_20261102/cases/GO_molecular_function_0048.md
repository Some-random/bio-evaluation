# GO_molecular_function_0048: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0048.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **C** — chorismate synthase activity

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSFGESHGKAIGCVIDGFLPNVEINFDLIQRQLNRRRPNQSKLTSNRNEPDKLIVLSGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGEVTPGGSRAQEGTSFEKDACHRSGHLSNLSGYPSNGSGNPPNGSDHPSNRSGNPPNRSDPRVDESTRETSPPSGEKLLVTTSNNCGGILAGITTGNNIVFRSAIKPVSSIQIEKETCNFFGEKCKLKVTGMHDCCILPRLPPIIEASTSIVIGDMILRQVAKYGHSKLPSVGSLSRSTRE

[Multiple Choices]
A. ATP hydrolysis activity
B. heme oxygenase (decyclizing) activity
C. chorismate synthase activity
D. single-stranded DNA binding
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the Plasmodium vivax protein annotated as chorismate synthase. UniProt records the EPSP-to-chorismate reaction with experimental evidence (ECO:0000269, citing PMID 31381947), supporting choice C. The entry also describes a second, flavin-reductase activity, which is not among the choices.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a clear, general biological clue that identifies chorismate synthase activity over the other offered functions; distinguishing these choices requires recognizing the protein family or knowing a protein-specific functional annotation.


**Missing item-specific fact**

> That this particular 547-aa Plasmodium vivax protein is a bifunctional chorismate synthase/flavin reductase.


**Reason**

> Reviewer-only annotation and experimental evidence support the key, but those facts are not supplied to the evaluated model. Exact-sequence recognition or recalled database annotation would be lookup or memorization, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein has an additional flavin-reductase activity, but that activity is not offered. Among the listed options, the evidence supports chorismate synthase activity.


### Important caveats

- The experimental support is represented by UniProt evidence citing PMID 31381947; the primary paper was not independently reviewed here.
- The GO annotation itself is electronically inferred from the EC number, so it should be distinguished from the cited experimental functional annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a clear, general biological clue that identifies chorismate synthase activity over the other offered functions; distinguishing these choices requires recognizing the protein family or knowing a protein-specific functional annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular 547-aa Plasmodium vivax protein is a bifunctional chorismate synthase/flavin reductase.",
    "reason": "Reviewer-only annotation and experimental evidence support the key, but those facts are not supplied to the evaluated model. Exact-sequence recognition or recalled database annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Plasmodium vivax protein annotated as chorismate synthase. UniProt records the EPSP-to-chorismate reaction with experimental evidence (ECO:0000269, citing PMID 31381947), supporting choice C. The entry also describes a second, flavin-reductase activity, which is not among the choices."
  },
  "important_caveats": [
    "The experimental support is represented by UniProt evidence citing PMID 31381947; the primary paper was not independently reviewed here.",
    "The GO annotation itself is electronically inferred from the EC number, so it should be distinguished from the cited experimental functional annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has an additional flavin-reductase activity, but that activity is not offered. Among the listed options, the evidence supports chorismate synthase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the Plasmodium vivax protein annotated as chorismate synthase. UniProt records the EPSP-to-chorismate reaction with experimental evidence (ECO:0000269, citing PMID 31381947), supporting choice C. The entry also describes a second, flavin-reductase activity, which is not among the choices.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a clear, general biological clue that identifies chorismate synthase activity over the other offered functions; distinguishing these choices requires recognizing the protein family or knowing a protein-specific functional annotation.",
    "missing_item_specific_fact": "That this particular 547-aa Plasmodium vivax protein is a bifunctional chorismate synthase/flavin reductase.",
    "reason": "Reviewer-only annotation and experimental evidence support the key, but those facts are not supplied to the evaluated model. Exact-sequence recognition or recalled database annotation would be lookup or memorization, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein has an additional flavin-reductase activity, but that activity is not offered. Among the listed options, the evidence supports chorismate synthase activity."
  },
  "important_caveats": [
    "The experimental support is represented by UniProt evidence citing PMID 31381947; the primary paper was not independently reviewed here.",
    "The GO annotation itself is electronically inferred from the EC number, so it should be distinguished from the cited experimental functional annotation."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A5K264 (AROC_PLAVS), a Plasmodium vivax protein explicitly named 'Chorismate synthase' with EC 4.2.3.5 (catalysis of EPSP → chorismate + phosphate). The function is supported by experimental evidence (ECO:0000269, PubMed:31381947, Khera et al. 2019). GO:0004107 'chorismate synthase activity' is annotated. The sequence match is confirmed (SHA-256 identical, 547 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C11](#evidence-c11), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could attempt elimination: (A) no Walker A (GxxxxGK&#91;S/T&#93;) or Walker B motifs visible → unlikely ATPase; (B) no conserved heme-coordinating His cluster in the characteristic HO-1/HO-2 pattern → unlikely heme oxygenase; (D) no OB-fold or RPA-like ssDNA-binding motifs → unlikely ssDNA binding. The sequence does contain FMN-binding-like motifs (e.g., the GSGFDGTYMLGSDHNDLFGTLD region), consistent with the FMN cofactor used by chorismate synthase. However, positively identifying 'chorismate synthase' specifically (as opposed to other FMN-binding or flavin reductase proteins) from raw sequence requires recognizing its particular structural motifs or knowing the database entry.


**Missing item-specific fact**

> Recognition that this 547-aa sequence corresponds to the bifunctional chorismate synthase/flavin reductase of Plasmodium vivax, or identification of the specific conserved catalytic residues (e.g., the FMN-binding arginines, the catalytic Arg/His triad) that distinguish chorismate synthase from other FMN-binding proteins. The sequence alone does not contain a universally recognized 'chorismate synthase signature' analogous to, say, a kinase catalytic loop.


**Reason**

> While elimination of options A, B, and D is partially feasible through absence of characteristic motifs, the positive identification of chorismate synthase from this sequence requires specialized knowledge of its conserved structural motifs or direct database lookup. The FMN-binding region is consistent with but not diagnostic of chorismate synthase among all FMN-binding proteins. The question is not purely lookup (elimination helps), but the final positive identification depends on an item-specific annotation or specialized motif recognition not derivable from general biology alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only chorismate synthase activity is supported by the UniProt annotation. The bifunctional flavin reductase (NADPH) activity (GO:0052873) is not among the options, so it does not create ambiguity. The other three options (ATP hydrolysis, heme oxygenase, ssDNA binding) have no supporting evidence for this sequence.


### Important caveats

- The protein is bifunctional (chorismate synthase EC 4.2.3.5 AND flavin reductase EC 1.5.1.38). The question asks for 'primary molecular function' and only chorismate synthase is offered as an option, avoiding ambiguity.
- The GO annotation for chorismate synthase activity uses evidence code IEA:UniProtKB-EC (inferred from EC number), while the experimental evidence (ECO:0000269) supports the catalytic activity directly from PubMed:31381947.
- The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. The sequence itself dates to 2011.
- The identity of the protein (Plasmodium vivax chorismate synthase) was not provided to the evaluated model; only the raw sequence and four options were given.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could attempt elimination: (A) no Walker A (GxxxxGK[S/T]) or Walker B motifs visible → unlikely ATPase; (B) no conserved heme-coordinating His cluster in the characteristic HO-1/HO-2 pattern → unlikely heme oxygenase; (D) no OB-fold or RPA-like ssDNA-binding motifs → unlikely ssDNA binding. The sequence does contain FMN-binding-like motifs (e.g., the GSGFDGTYMLGSDHNDLFGTLD region), consistent with the FMN cofactor used by chorismate synthase. However, positively identifying 'chorismate synthase' specifically (as opposed to other FMN-binding or flavin reductase proteins) from raw sequence requires recognizing its particular structural motifs or knowing the database entry.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition that this 547-aa sequence corresponds to the bifunctional chorismate synthase/flavin reductase of Plasmodium vivax, or identification of the specific conserved catalytic residues (e.g., the FMN-binding arginines, the catalytic Arg/His triad) that distinguish chorismate synthase from other FMN-binding proteins. The sequence alone does not contain a universally recognized 'chorismate synthase signature' analogous to, say, a kinase catalytic loop.",
    "reason": "While elimination of options A, B, and D is partially feasible through absence of characteristic motifs, the positive identification of chorismate synthase from this sequence requires specialized knowledge of its conserved structural motifs or direct database lookup. The FMN-binding region is consistent with but not diagnostic of chorismate synthase among all FMN-binding proteins. The question is not purely lookup (elimination helps), but the final positive identification depends on an item-specific annotation or specialized motif recognition not derivable from general biology alone."
  },
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C11",
      "H1",
      "H3",
      "H4",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A5K264 (AROC_PLAVS), a Plasmodium vivax protein explicitly named 'Chorismate synthase' with EC 4.2.3.5 (catalysis of EPSP → chorismate + phosphate). The function is supported by experimental evidence (ECO:0000269, PubMed:31381947, Khera et al. 2019). GO:0004107 'chorismate synthase activity' is annotated. The sequence match is confirmed (SHA-256 identical, 547 aa)."
  },
  "important_caveats": [
    "The protein is bifunctional (chorismate synthase EC 4.2.3.5 AND flavin reductase EC 1.5.1.38). The question asks for 'primary molecular function' and only chorismate synthase is offered as an option, avoiding ambiguity.",
    "The GO annotation for chorismate synthase activity uses evidence code IEA:UniProtKB-EC (inferred from EC number), while the experimental evidence (ECO:0000269) supports the catalytic activity directly from PubMed:31381947.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. The sequence itself dates to 2011.",
    "The identity of the protein (Plasmodium vivax chorismate synthase) was not provided to the evaluated model; only the raw sequence and four options were given."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only chorismate synthase activity is supported by the UniProt annotation. The bifunctional flavin reductase (NADPH) activity (GO:0052873) is not among the options, so it does not create ambiguity. The other three options (ATP hydrolysis, heme oxygenase, ssDNA binding) have no supporting evidence for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A5K264 (AROC_PLAVS), a Plasmodium vivax protein explicitly named 'Chorismate synthase' with EC 4.2.3.5 (catalysis of EPSP → chorismate + phosphate). The function is supported by experimental evidence (ECO:0000269, PubMed:31381947, Khera et al. 2019). GO:0004107 'chorismate synthase activity' is annotated. The sequence match is confirmed (SHA-256 identical, 547 aa).",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C11", "H1", "H3", "H4", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could attempt elimination: (A) no Walker A (GxxxxGK[S/T]) or Walker B motifs visible → unlikely ATPase; (B) no conserved heme-coordinating His cluster in the characteristic HO-1/HO-2 pattern → unlikely heme oxygenase; (D) no OB-fold or RPA-like ssDNA-binding motifs → unlikely ssDNA binding. The sequence does contain FMN-binding-like motifs (e.g., the GSGFDGTYMLGSDHNDLFGTLD region), consistent with the FMN cofactor used by chorismate synthase. However, positively identifying 'chorismate synthase' specifically (as opposed to other FMN-binding or flavin reductase proteins) from raw sequence requires recognizing its particular structural motifs or knowing the database entry.",
    "missing_item_specific_fact": "Recognition that this 547-aa sequence corresponds to the bifunctional chorismate synthase/flavin reductase of Plasmodium vivax, or identification of the specific conserved catalytic residues (e.g., the FMN-binding arginines, the catalytic Arg/His triad) that distinguish chorismate synthase from other FMN-binding proteins. The sequence alone does not contain a universally recognized 'chorismate synthase signature' analogous to, say, a kinase catalytic loop.",
    "reason": "While elimination of options A, B, and D is partially feasible through absence of characteristic motifs, the positive identification of chorismate synthase from this sequence requires specialized knowledge of its conserved structural motifs or direct database lookup. The FMN-binding region is consistent with but not diagnostic of chorismate synthase among all FMN-binding proteins. The question is not purely lookup (elimination helps), but the final positive identification depends on an item-specific annotation or specialized motif recognition not derivable from general biology alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only chorismate synthase activity is supported by the UniProt annotation. The bifunctional flavin reductase (NADPH) activity (GO:0052873) is not among the options, so it does not create ambiguity. The other three options (ATP hydrolysis, heme oxygenase, ssDNA binding) have no supporting evidence for this sequence."
  },
  "important_caveats": [
    "The protein is bifunctional (chorismate synthase EC 4.2.3.5 AND flavin reductase EC 1.5.1.38). The question asks for 'primary molecular function' and only chorismate synthase is offered as an option, avoiding ambiguity.",
    "The GO annotation for chorismate synthase activity uses evidence code IEA:UniProtKB-EC (inferred from EC number), while the experimental evidence (ECO:0000269) supports the catalytic activity directly from PubMed:31381947.",
    "The UniProt entry was first publicly released 2025-06-18; the benchmark construction date is unknown. The sequence itself dates to 2011.",
    "The identity of the protein (Plasmodium vivax chorismate synthase) was not provided to the evaluated model; only the raw sequence and four options were given."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record identifies the protein as a chorismate synthase and reports EPSP-to-chorismate catalysis with experimental evidence (ECO:0000269). This supports choice C. The protein is also reported to have flavin reductase activity, which is not among the options.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize the sequence as belonging to the chorismate synthase family by comparison with transferable sequence patterns and family knowledge. Chorismate synthases are enzymes in the shikimate pathway that form chorismate from EPSP; that family-level inference distinguishes C from ATP hydrolysis, heme oxygenase activity, and single-stranded DNA binding. The sequence is a long globular enzyme rather than an obvious DNA-binding protein or membrane-associated heme oxygenase, and it lacks an obvious ATPase signature. These features support the family inference but are not, by themselves, proof of function.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices include a specific enzyme activity that can be distinguished through transferable family recognition and sequence comparison with related proteins. The inference need not establish every activity of this bifunctional protein to select C among these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source reports a second activity, flavin reductase, but that is not one of the offered choices. Among the listed options, chorismate synthase activity is supported.


### Important caveats

- The source records match the supplied sequence, but the author's exact source snapshot is unknown.
- The experimental evidence supports chorismate synthase activity; the sequence-based inference is probabilistic rather than a direct activity measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as belonging to the chorismate synthase family by comparison with transferable sequence patterns and family knowledge. Chorismate synthases are enzymes in the shikimate pathway that form chorismate from EPSP; that family-level inference distinguishes C from ATP hydrolysis, heme oxygenase activity, and single-stranded DNA binding. The sequence is a long globular enzyme rather than an obvious DNA-binding protein or membrane-associated heme oxygenase, and it lacks an obvious ATPase signature. These features support the family inference but are not, by themselves, proof of function.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices include a specific enzyme activity that can be distinguished through transferable family recognition and sequence comparison with related proteins. The inference need not establish every activity of this bifunctional protein to select C among these alternatives."
  },
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as a chorismate synthase and reports EPSP-to-chorismate catalysis with experimental evidence (ECO:0000269). This supports choice C. The protein is also reported to have flavin reductase activity, which is not among the options."
  },
  "important_caveats": [
    "The source records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence supports chorismate synthase activity; the sequence-based inference is probabilistic rather than a direct activity measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source reports a second activity, flavin reductase, but that is not one of the offered choices. Among the listed options, chorismate synthase activity is supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as a chorismate synthase and reports EPSP-to-chorismate catalysis with experimental evidence (ECO:0000269). This supports choice C. The protein is also reported to have flavin reductase activity, which is not among the options.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as belonging to the chorismate synthase family by comparison with transferable sequence patterns and family knowledge. Chorismate synthases are enzymes in the shikimate pathway that form chorismate from EPSP; that family-level inference distinguishes C from ATP hydrolysis, heme oxygenase activity, and single-stranded DNA binding. The sequence is a long globular enzyme rather than an obvious DNA-binding protein or membrane-associated heme oxygenase, and it lacks an obvious ATPase signature. These features support the family inference but are not, by themselves, proof of function.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices include a specific enzyme activity that can be distinguished through transferable family recognition and sequence comparison with related proteins. The inference need not establish every activity of this bifunctional protein to select C among these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source reports a second activity, flavin reductase, but that is not one of the offered choices. Among the listed options, chorismate synthase activity is supported."
  },
  "important_caveats": [
    "The source records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence supports chorismate synthase activity; the sequence-based inference is probabilistic rather than a direct activity measurement."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A5K264 (AROC_PLAVS) is experimentally characterized (ECO:0000269, PubMed:31381947) as a bifunctional chorismate synthase (EC 4.2.3.5) and flavin reductase (EC 1.5.1.38). The GO annotation GO:0004107 (chorismate synthase activity) is assigned via UniProtKB-EC, and the underlying EC assignment derives from experimental evidence. The catalytic activity EPSP → chorismate + phosphate is confirmed by the reference. The sequence matches exactly (sha256 identical). Choice C is the primary recommended function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [C11](#evidence-c11), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conserved 'GFDEN' motif (appearing as 'SGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGE'), which is a family-level signature of chorismate synthases (known from E. coli AroC, yeast, and other organisms). The second occurrence 'GIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGE' resembles the FMN-binding architecture characteristic of the chorismate synthase fold. The protein length (547 aa) is consistent with eukaryotic chorismate synthases. Multiple clustered arginines (RRR, RGR) are consistent with the poly-arginine catalytic site of chorismate synthase. Against the distractors: (A) no Walker A (GxxxxGK&#91;T/S&#93;) or Walker B motifs are present, ruling out ATP hydrolysis; (B) heme oxygenases are ~260-290 aa with a conserved RxxxH heme-binding motif absent here, and the 547-aa length is inconsistent; (D) no OB-fold, RRM, or zinc-finger patterns characteristic of ssDNA-binding proteins are present. The GFDEN motif plus FMN-binding architecture are transferable family features that positively identify chorismate synthase and exclude the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the GFDEN motif and FMN-binding architecture from other chorismate synthases (E. coli, yeast, other eukaryotes) can positively identify the protein family and exclude the three distractors based on absence of their characteristic motifs (Walker A/B, heme-binding RxxxH, OB-fold/RRM). This is legitimate family-level inference from conserved sequence features shared across the chorismate synthase protein family.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct molecular functions with clearly different structural and sequence signatures. Only chorismate synthase matches the observed GFDEN motif and FMN-binding architecture. The protein's bifunctionality (also flavin reductase) does not create ambiguity because flavin reductase is not among the offered choices.


### Important caveats

- The protein is bifunctional (chorismate synthase AND flavin reductase per PubMed:31381947), but flavin reductase activity is not among the four choices, so this does not affect the answer.
- The GO annotation for chorismate synthase activity is IEA (Inferred from Electronic Annotation via UniProtKB-EC), but the underlying EC 4.2.3.5 assignment is supported by experimental evidence (ECO:0000269).
- The GFDEN motif, while strongly associated with chorismate synthase family members, should be considered in context with the overall FMN-binding architecture and protein length for confident family assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved 'GFDEN' motif (appearing as 'SGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGE'), which is a family-level signature of chorismate synthases (known from E. coli AroC, yeast, and other organisms). The second occurrence 'GIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGE' resembles the FMN-binding architecture characteristic of the chorismate synthase fold. The protein length (547 aa) is consistent with eukaryotic chorismate synthases. Multiple clustered arginines (RRR, RGR) are consistent with the poly-arginine catalytic site of chorismate synthase. Against the distractors: (A) no Walker A (GxxxxGK[T/S]) or Walker B motifs are present, ruling out ATP hydrolysis; (B) heme oxygenases are ~260-290 aa with a conserved RxxxH heme-binding motif absent here, and the 547-aa length is inconsistent; (D) no OB-fold, RRM, or zinc-finger patterns characteristic of ssDNA-binding proteins are present. The GFDEN motif plus FMN-binding architecture are transferable family features that positively identify chorismate synthase and exclude the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the GFDEN motif and FMN-binding architecture from other chorismate synthases (E. coli, yeast, other eukaryotes) can positively identify the protein family and exclude the three distractors based on absence of their characteristic motifs (Walker A/B, heme-binding RxxxH, OB-fold/RRM). This is legitimate family-level inference from conserved sequence features shared across the chorismate synthase protein family."
  },
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "C11",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A5K264 (AROC_PLAVS) is experimentally characterized (ECO:0000269, PubMed:31381947) as a bifunctional chorismate synthase (EC 4.2.3.5) and flavin reductase (EC 1.5.1.38). The GO annotation GO:0004107 (chorismate synthase activity) is assigned via UniProtKB-EC, and the underlying EC assignment derives from experimental evidence. The catalytic activity EPSP → chorismate + phosphate is confirmed by the reference. The sequence matches exactly (sha256 identical). Choice C is the primary recommended function."
  },
  "important_caveats": [
    "The protein is bifunctional (chorismate synthase AND flavin reductase per PubMed:31381947), but flavin reductase activity is not among the four choices, so this does not affect the answer.",
    "The GO annotation for chorismate synthase activity is IEA (Inferred from Electronic Annotation via UniProtKB-EC), but the underlying EC 4.2.3.5 assignment is supported by experimental evidence (ECO:0000269).",
    "The GFDEN motif, while strongly associated with chorismate synthase family members, should be considered in context with the overall FMN-binding architecture and protein length for confident family assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct molecular functions with clearly different structural and sequence signatures. Only chorismate synthase matches the observed GFDEN motif and FMN-binding architecture. The protein's bifunctionality (also flavin reductase) does not create ambiguity because flavin reductase is not among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A5K264 (AROC_PLAVS) is experimentally characterized (ECO:0000269, PubMed:31381947) as a bifunctional chorismate synthase (EC 4.2.3.5) and flavin reductase (EC 1.5.1.38). The GO annotation GO:0004107 (chorismate synthase activity) is assigned via UniProtKB-EC, and the underlying EC assignment derives from experimental evidence. The catalytic activity EPSP → chorismate + phosphate is confirmed by the reference. The sequence matches exactly (sha256 identical). Choice C is the primary recommended function.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "C11", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conserved 'GFDEN' motif (appearing as 'SGFDENKTLGTPITFLINNEDVIKKNYSSFIDIPRPGHGDYTYFKKYNVKNKSGSSRFSGRETATRVAAGACIEQWLHTFYNCTIVCYVHSVGNIKLPEQVSKDFERNPPSRDLVDAHGAVKYHQGRGTFTDFFGNVYNANGEFLRGGEAAPEGATPADGTPTDGNPTDDPLANARERLSDPGECTLLQTRCPHPLTAVKICSYILKLKKAGDSIGGVATCIAHNVPVGIGEPIFEKMEAELGKIILSIPAVKGIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGE'), which is a family-level signature of chorismate synthases (known from E. coli AroC, yeast, and other organisms). The second occurrence 'GIEFGSGFDGTYMLGSDHNDLFGTLDVPEEGPCQRGWTLTDALDSKRGE' resembles the FMN-binding architecture characteristic of the chorismate synthase fold. The protein length (547 aa) is consistent with eukaryotic chorismate synthases. Multiple clustered arginines (RRR, RGR) are consistent with the poly-arginine catalytic site of chorismate synthase. Against the distractors: (A) no Walker A (GxxxxGK[T/S]) or Walker B motifs are present, ruling out ATP hydrolysis; (B) heme oxygenases are ~260-290 aa with a conserved RxxxH heme-binding motif absent here, and the 547-aa length is inconsistent; (D) no OB-fold, RRM, or zinc-finger patterns characteristic of ssDNA-binding proteins are present. The GFDEN motif plus FMN-binding architecture are transferable family features that positively identify chorismate synthase and exclude the other three options.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the GFDEN motif and FMN-binding architecture from other chorismate synthases (E. coli, yeast, other eukaryotes) can positively identify the protein family and exclude the three distractors based on absence of their characteristic motifs (Walker A/B, heme-binding RxxxH, OB-fold/RRM). This is legitimate family-level inference from conserved sequence features shared across the chorismate synthase protein family."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct molecular functions with clearly different structural and sequence signatures. Only chorismate synthase matches the observed GFDEN motif and FMN-binding architecture. The protein's bifunctionality (also flavin reductase) does not create ambiguity because flavin reductase is not among the offered choices."
  },
  "important_caveats": [
    "The protein is bifunctional (chorismate synthase AND flavin reductase per PubMed:31381947), but flavin reductase activity is not among the four choices, so this does not affect the answer.",
    "The GO annotation for chorismate synthase activity is IEA (Inferred from Electronic Annotation via UniProtKB-EC), but the underlying EC 4.2.3.5 assignment is supported by experimental evidence (ECO:0000269).",
    "The GFDEN motif, while strongly associated with chorismate synthase family members, should be considered in context with the overall FMN-binding architecture and protein length for confident family assignment."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A5K264",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "dd6cd0d6b670d3bec55a95f172073170bd0c4383312200bc83dee06a611f059e",
  "benchmark_sequence_length": 547,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 65,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-02-08",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "current_source_sequence_sha256": "dd6cd0d6b670d3bec55a95f172073170bd0c4383312200bc83dee06a611f059e",
  "current_source_sequence_length": 547,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 64,
  "selected_historical_version": {
    "accession": "A5K264",
    "database": "Swiss-Prot",
    "entryVersion": 64,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "AROC_PLAVS",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "selected_historical_source_sequence_sha256": "dd6cd0d6b670d3bec55a95f172073170bd0c4383312200bc83dee06a611f059e",
  "selected_historical_source_sequence_length": 547,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 64,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A5K264\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":65,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-02-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008333\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Plasmodium\"],\"scientificName\":\"Plasmodium vivax (strain Salvador I)\",\"taxonId\":126793}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.38\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Chorismate synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Bifunctional chorismate synthase and flavin reductase (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate 3-phosphate (EPSP) to form chorismate (PubMed:31381947). Acts also as a flavin reductase (FR) able to generate reduced flavin mononucleotide in the presence of NADPH (PubMed:31381947)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:21021\"}}],\"reaction\":{\"ecNumber\":\"4.2.3.5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"name\":\"5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21020\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57701\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:21626\"}}],\"reaction\":{\"ecNumber\":\"1.5.1.38\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"name\":\"FMNH2 + NADP(+) = FMN + NADPH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21624\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004107\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:chorismate synthase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-EC\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0010181\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:FMN binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0052873\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:FMN reductase (NADPH) activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-EC\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A5K264.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A5K264.json",
  "source_sha256": "d58af6bd4484c5c3f24d6df9b8a86368b29010264a29037f28d736c22aba6d5e",
  "retrieved_utc": "2026-11-02T04:27:01.460415+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Khera H.K.\",\"Singh S.K.\",\"Singh S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31381947\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2019.111202\"}],\"citationType\":\"journal article\",\"firstPage\":\"111202\",\"id\":\"31381947\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"111202\",\"publicationDate\":\"2019\",\"title\":\"Chorismate synthase from malaria parasites is bifunctional enzyme.\",\"volume\":\"233\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   AROC_PLAVS              Reviewed;         547 AA.\nAC   A5K264;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-FEB-2011, sequence version 1.\nDT   28-JAN-2026, entry version 64.\nDE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:31381947};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:31381947};\nGN   Name=CS {ECO:0000305}; ORFNames=PVX_114265 {ECO:0000312|EMBL:EDL46514.1};\nOS   Plasmodium vivax (strain Salvador I).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).\nOX   NCBI_TaxID=126793 {ECO:0000312|Proteomes:UP000008333};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 64,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "source_locator": "lines 29-34",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;\nRA   Khera H.K., Singh S.K., Singh S.;\nRT   \"Chorismate synthase from malaria parasites is bifunctional enzyme.\";\nRL   Mol. Biochem. Parasitol. 233:111202-111202(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 64,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "source_locator": "lines 35-39",
  "excerpt": "CC   -!- FUNCTION: Bifunctional chorismate synthase and flavin reductase\nCC       (PubMed:31381947). Catalyzes the conversion of 5-enolpyruvylshikimate\nCC       3-phosphate (EPSP) to form chorismate (PubMed:31381947). Acts also as a\nCC       flavin reductase (FR) able to generate reduced flavin mononucleotide in\nCC       the presence of NADPH (PubMed:31381947). {ECO:0000269|PubMed:31381947}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 64,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "source_locator": "lines 40-46",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate +\nCC         phosphate; Xref=Rhea:RHEA:21020, ChEBI:CHEBI:29748,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57701; EC=4.2.3.5;\nCC         Evidence={ECO:0000269|PubMed:31381947};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:21021;\nCC         Evidence={ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 64,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "source_locator": "lines 47-53",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=FMNH2 + NADP(+) = FMN + NADPH + 2 H(+); Xref=Rhea:RHEA:21624,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57618, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:58349; EC=1.5.1.38;\nCC         Evidence={ECO:0000305|PubMed:31381947};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:21626;\nCC         Evidence={ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 64,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "source_locator": "lines 80-80",
  "excerpt": "DR   GO; GO:0004107; F:chorismate synthase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 64,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "source_locator": "lines 81-81",
  "excerpt": "DR   GO; GO:0010181; F:FMN binding; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 64,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A5K264?format=txt&versions=64",
  "source_sha256": "6e2964cdb968286a7cc2f7c98521da2e5af1f80b98dc4f616e38657c099ee036",
  "retrieved_utc": "2026-11-02T04:27:05.947967+00:00",
  "source_locator": "lines 82-82",
  "excerpt": "DR   GO; GO:0052873; F:FMN reductase (NADPH) activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 64,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 27998-28008",
  "excerpt": "[Term]\nid: GO:0003697\nname: single-stranded DNA binding\nnamespace: molecular_function\nalt_id: GO:0003698\nalt_id: GO:0003699\ndef: \"Binding to single-stranded DNA.\" [GOC:elh, GOC:vw, PMID:22976174]\ncomment: Note that this term is restricted to those cases where the binding is to a single-stranded DNA molecule, not to one of the stands of double-stranded DNA.\nsynonym: \"ssDNA binding\" EXACT [GOC:mah]\nis_a: GO:0003677 ! DNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0003697"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 35553-35568",
  "excerpt": "[Term]\nid: GO:0004107\nname: chorismate synthase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 5-O-(1-carboxyvinyl)-3-phosphoshikimate = chorismate + phosphate.\" [EC:4.2.3.5, RHEA:21020]\nsynonym: \"5-enolpyruvylshikimate-3-phosphate phospholyase activity\" RELATED [EC:4.2.3.5]\nsynonym: \"5-O-(1-carboxyvinyl)-3-phosphoshikimate phosphate-lyase (chorismate-forming)\" RELATED [EC:4.2.3.5]\nsynonym: \"5-O-(1-carboxyvinyl)-3-phosphoshikimate phosphate-lyase activity\" RELATED [EC:4.2.3.5]\nxref: EC:4.2.3.5\nxref: KEGG_REACTION:R01714\nxref: MetaCyc:CHORISMATE-SYNTHASE-RXN\nxref: RHEA:21020\nis_a: GO:0016838 ! carbon-oxygen lyase activity, acting on phosphates\nproperty_value: skos:exactMatch EC:4.2.3.5\nproperty_value: skos:exactMatch RHEA:21020\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004107"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 41241-41260",
  "excerpt": "[Term]\nid: GO:0004392\nname: heme oxygenase (decyclizing) activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: heme b + 3 O2 + 3 reduced [NADPH-hemoprotein reductase] = biliverdin + CO + Fe2+ + H+ + 3 H2O + 3 oxidized [NADPH-hemoprotein reductase].\" [RHEA:21764]\nsynonym: \"haem oxidase activity\" RELATED [EC:1.14.14.18]\nsynonym: \"haem oxygenase (decyclizing) activity\" EXACT []\nsynonym: \"haem oxygenase activity\" RELATED [EC:1.14.14.18]\nsynonym: \"heme oxidase activity\" RELATED [EC:1.14.14.18]\nsynonym: \"heme oxygenase activity\" RELATED [EC:1.14.14.18]\nsynonym: \"heme,hydrogen-donor:oxygen oxidoreductase (alpha-methene-oxidizing, hydroxylating)\" RELATED [EC:1.14.14.18]\nsynonym: \"ORP33 proteins\" RELATED [EC:1.14.14.18]\nxref: EC:1.14.14.18\nxref: MetaCyc:HEME-OXYGENASE-DECYCLIZING-RXN\nxref: Reactome:R-HSA-189398 \"HMOX1 dimer, HMOX2 cleave heme\"\nxref: RHEA:21764\nis_a: GO:0016712 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, reduced flavin or flavoprotein as one donor, and incorporation of one atom of oxygen\nproperty_value: skos:exactMatch EC:1.14.14.18\nproperty_value: skos:exactMatch RHEA:21764\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0004392"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 131251-131292",
  "excerpt": "[Term]\nid: GO:0016887\nname: ATP hydrolysis activity\nnamespace: molecular_function\nalt_id: GO:0004002\nalt_id: GO:0042623\ndef: \"Catalysis of the reaction: ATP + H2O = ADP + H+ phosphate. ATP hydrolysis is used in some reactions as an energy source, for example to catalyze a reaction or drive transport against a concentration gradient.\" [RHEA:13065]\ncomment: Note that this term is meant to specifically represent the ATPase activity of proteins using ATP as a source of energy to drive a reaction. If possible, gene products should also be annotated to a child of 'ATP-dependent activity ; GO:0140657', to capture their overall function.\nsynonym: \"adenosine 5'-triphosphatase activity\" EXACT []\nsynonym: \"adenosine triphosphatase activity\" EXACT []\nsynonym: \"adenosinetriphosphatase activity\" EXACT []\nsynonym: \"ATP hydrolase activity\" EXACT []\nsynonym: \"ATP monophosphatase activity\" RELATED []\nsynonym: \"ATP phosphohydrolase activity\" EXACT []\nxref: Reactome:R-HSA-159101 \"NXF1:NXT1 (TAP:p15) binds capped mRNA:CBC:EJC:TREX (minus DDX39B)\"\nxref: Reactome:R-HSA-3371422 \"ATP hydrolysis by HSP70\"\nxref: Reactome:R-HSA-416985 \"Trafficking of GluR2-containing AMPA receptors to synapse\"\nxref: Reactome:R-HSA-5618093 \"ATP hydrolysis by HSP90\"\nxref: Reactome:R-HSA-5654989 \"SPRTN:VCP-mediated release of POLH from monoUb:K164-PCNA\"\nxref: Reactome:R-HSA-5694425 \"NSF ATPase activity dissociates cis-SNARE\"\nxref: Reactome:R-HSA-6809015 \"NSF ATPase activity dissociates cis-SNARE at cis-Golgi\"\nxref: Reactome:R-HSA-6811422 \"NSF ATPase activity dissociates cis-SNARE at the ER\"\nxref: Reactome:R-HSA-6814670 \"ATP hydrolysis by RHOBTB3 promotes PLIN3 dissociation\"\nxref: Reactome:R-HSA-6814678 \"ATP hydrolysis by NSF disassembles the cis-SNARE at the TGN\"\nxref: Reactome:R-HSA-6814683 \"NSF-dependent ATP hydrolysis disassembles the cis-SNARE at the TGN\"\nxref: Reactome:R-HSA-8847638 \"ATP hydrolysis by NSF disassembles the cis-SNARE at the Golgi membrane\"\nxref: Reactome:R-HSA-8868658 \"HSPA8-mediated ATP hydrolysis promotes vesicle uncoating\"\nxref: Reactome:R-HSA-8939203 \"HSP90-dependent ATP hydrolysis promotes release of ESR:ESTG from chaperone complex\"\nxref: Reactome:R-HSA-9038161 \"Progesterone stimulation promotes PGR:P4 binding to ESR1:ESTG\"\nxref: Reactome:R-HSA-917693 \"ESCRT Disassembly\"\nxref: Reactome:R-HSA-9609860 \"Tail-anchored protein:SGTA:BAG6:GET4:UBL4A:ASNA1:ATP dissociates and ASNA1 hydrolyzes ATP yielding Tail-anchored protein:ASNA1:ADP\"\nxref: Reactome:R-HSA-9668415 \"VPS4 mediates disassembly of ESCRTIII subunits to promote sealing of holes in the nuclear envelope\"\nxref: Reactome:R-HSA-9706399 \"RHOBTB3 hydrolyzes ATP\"\nxref: Reactome:R-HSA-9749350 \"ATP-dependent release of CDT1 from the OCCM complex\"\nxref: Reactome:R-HSA-9948300 \"RQT complex:K63polyUb-80S ribosome dissociates yielding K63polyUb-40S subunit and 60S subunit:peptidyl-tRNA with nascent peptide\"\nxref: Reactome:R-HSA-9949632 \"VCP hexamer extracts K48 polyubiquitinated alanine-tailed nascent peptide from VCP hexamer:UFD1:NPLOC4:LTN1:NEMF:TCF25:60S ribosome subunit:K48polyUb-nascent peptide\"\nxref: Reactome:R-HSA-9955731 \"ABCE1:PELO:80S Ribosome:non-stop mRNA:peptidyl-tRNA with elongating peptide dissociates yielding ABCE1:40S ribosomal subunit, PELO, and 60S ribosomal subunit:peptidyl-tRNA with nascent peptide\"\nxref: RHEA:13065\nis_a: GO:0017111 ! ribonucleoside triphosphate phosphatase activity\nrelationship: part_of GO:0140657 ! ATP-dependent activity\nproperty_value: skos:exactMatch RHEA:13065\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0016887"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
