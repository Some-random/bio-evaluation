# GO_biological_process_0055: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_biological_process_0055.txt)

**Task:** `GO_biological_process`  
**Author key, unchanged:** **D** — microtubule cytoskeleton organization

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MERSGGNGAGARAGAPSEGAAKGSSLLSAKSTEGATGRFSQSTPRPTGMDGFLKSDERQRLAKERREEREKCLAAREQQILEKQKRAKLQYEKQIEERWRKLEEQRQREDQKRAAVEEKRKQKLREEEERLEAMMRRSLERTQQLELKKKCSWAGSAASGPGGRDGESENTPPLPLTLAASIPPSDTGTATAAAESTNACDKLSTSTMNLPKQTEPPMSKHLSSSIVAISYSPDRALRSPLKSSYKSSPTRTTEKKKNTLLSGVGDAGKGAMTGGEPSQMEKVKKGRGATSVSSGGLGSPLRRCEPPENISKRSSSPVKSKVTAKTYPQSPKTVKPTYIGSPVKYYFPPTPSEETLKKKAEKEKSNKEKEGATGRQTTVLPREETLEKPMADKDATEKYVADKHATEKHSATGGKAEHSAGKSTAGTTDAGEAAKILAEKRRQARLQKEQEEQERLEKEEQERLEKEELKRKAEEERLRIEKQEEEKKQQEEEEKRKAEEKAKEKAEEELLSKEEQEKEKQEKEKKEKAMIEKQIQAEKEAAEAKAQDAAKQMRLEREQIMLQIEQERLERKKRIDEIMKRTRKSDASLEVKKEDPKVEIQPLPDVENKIKPVVPNKIEINVLNTCQKVNVSERAAPETFPQDIFSNGLKPVGGPVHPDVLDGKSNSLDDSTEEVQSMDVSPVSKEELISIPEFSPVSEMIPGMSLDQNGTGNARALQDILDFTGPPAFPKKSSENLSLDDCNKNLIEGFNSPGQETTLNTFC

[Multiple Choices]
A. venom-mediated fibrinolysis
B. positive regulation of transcription elongation by RNA polymerase II
C. amino acid activation for nonribosomal peptide biosynthetic process
D. microtubule cytoskeleton organization
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the rat MAP7D2 entry, which is annotated to microtubule cytoskeleton organization with IMP evidence (inference from mutant phenotype). Its described microtubule-stabilizing function is consistent with that process.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is rich in charged, likely coiled-coil regions, which may suggest a structural or interaction-focused protein, but this does not establish microtubule organization as its biological process or reliably distinguish it from other choices such as transcription regulation.


**Missing item-specific fact**

> The protein-specific identification and functional evidence that this sequence is MAP7D2, a microtubule-stabilizing protein involved in microtubule cytoskeleton organization.


**Reason**

> That functional assignment is supported by reviewer-only database and literature-linked evidence, but it is not supplied in the question. Recognizing the exact protein or consulting its annotation would be needed for a reliable choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports D; the sequence alone makes the answer difficult to infer, but does not make another listed process comparably supported.


### Important caveats

- The current and historical database records match the supplied sequence, but the author's exact source snapshot is unknown.
- The GO annotation uses IMP evidence; the cited primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is rich in charged, likely coiled-coil regions, which may suggest a structural or interaction-focused protein, but this does not establish microtubule organization as its biological process or reliably distinguish it from other choices such as transcription regulation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional evidence that this sequence is MAP7D2, a microtubule-stabilizing protein involved in microtubule cytoskeleton organization.",
    "reason": "That functional assignment is supported by reviewer-only database and literature-linked evidence, but it is not supplied in the question. Recognizing the exact protein or consulting its annotation would be needed for a reliable choice."
  },
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rat MAP7D2 entry, which is annotated to microtubule cytoskeleton organization with IMP evidence (inference from mutant phenotype). Its described microtubule-stabilizing function is consistent with that process."
  },
  "important_caveats": [
    "The current and historical database records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation uses IMP evidence; the cited primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D; the sequence alone makes the answer difficult to infer, but does not make another listed process comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rat MAP7D2 entry, which is annotated to microtubule cytoskeleton organization with IMP evidence (inference from mutant phenotype). Its described microtubule-stabilizing function is consistent with that process.",
    "evidence_ids": ["C1", "C5", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is rich in charged, likely coiled-coil regions, which may suggest a structural or interaction-focused protein, but this does not establish microtubule organization as its biological process or reliably distinguish it from other choices such as transcription regulation.",
    "missing_item_specific_fact": "The protein-specific identification and functional evidence that this sequence is MAP7D2, a microtubule-stabilizing protein involved in microtubule cytoskeleton organization.",
    "reason": "That functional assignment is supported by reviewer-only database and literature-linked evidence, but it is not supplied in the question. Recognizing the exact protein or consulting its annotation would be needed for a reliable choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D; the sequence alone makes the answer difficult to infer, but does not make another listed process comparably supported."
  },
  "important_caveats": [
    "The current and historical database records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation uses IMP evidence; the cited primary study was not independently reviewed here."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry D4A4L4 (MAP7D2, Rat) carries GO:0000226 'microtubule cytoskeleton organization' with IMP evidence (PubMed:35470240). The function comment explicitly states 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' and describes kinesin-1 cofactor activity on microtubules. The protein is named 'MAP7 domain-containing protein 2,' where MAP7 is a well-characterized microtubule-associated protein family. The sequence matches exactly (SHA-256 confirmed). The GO term text matches option D verbatim.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H3](#evidence-h3), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A and C can be eliminated with high confidence through general biology: (1) 'venom-mediated fibrinolysis' requires a secreted venom protease (serine or metalloprotease motif), which is absent from this 763-aa rat brain protein; (2) 'amino acid activation for nonribosomal peptide biosynthetic process' is exclusively a bacterial/fungal NRPS enzymatic process (requires adenylation, thiolation, condensation domains) and is incompatible with a mammalian protein. Between the remaining B and D: the sequence is a large, highly charged, intrinsically disordered protein with alternating acidic/basic stretches (E/K/R-rich) and lacks any domain architecture typical of transcription elongation regulators (no PWWP, bromodomain, TFIIS-like motifs, or specific protein-protein interaction modules). This charged, repetitive, disordered architecture is characteristic of microtubule-associated proteins (MAPs), whose microtubule-binding regions are typically unstructured and electrostatic. Thus general protein-architecture reasoning favors D over B.


**Missing item-specific fact**

> Specific recognition of the MAP7 domain signature (a ~200-300 aa microtubule-binding domain) from the sequence alone would require prior knowledge of this domain family. However, this is not strictly necessary given the strong elimination of A and C and the architectural argument favoring D over B.


**Reason**

> The four options span radically different biological contexts (venom, transcription, bacterial NRPS, cytoskeleton), allowing a model to eliminate A and C through organism/domain logic and to favor D over B through protein-architecture reasoning (large disordered charged protein without transcription-specific domains). While precise MAP7 domain identification adds confidence, the reasoning path to D does not depend solely on memorizing this protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are essentially impossible for a rat protein (wrong organism context, wrong domain architecture). Option B is disfavored by the absence of transcription-regulatory domains and the presence of MAP-like architecture. Only D is consistent with the sequence features and the protein's identity.


### Important caveats

- The GO:0000226 annotation is supported by IMP evidence (PubMed:35470240, 2022), while the 'axon development' annotation (GO:0061564) is from PubMed:30784582 (2019). Both are experimental (IMP), not purely computational.
- The MAP7 domain in this sequence is not a universally recognized motif like a kinase or zinc finger; a model relying solely on de novo domain recognition might find B vs D less clear-cut than the elimination of A and C.
- The protein was first publicly released in UniProt in April 2025; the author's source snapshot is unknown but the sequence matches the current and archived (v89) entries.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning assessment above considers only what a model could infer from the sequence and general biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A and C can be eliminated with high confidence through general biology: (1) 'venom-mediated fibrinolysis' requires a secreted venom protease (serine or metalloprotease motif), which is absent from this 763-aa rat brain protein; (2) 'amino acid activation for nonribosomal peptide biosynthetic process' is exclusively a bacterial/fungal NRPS enzymatic process (requires adenylation, thiolation, condensation domains) and is incompatible with a mammalian protein. Between the remaining B and D: the sequence is a large, highly charged, intrinsically disordered protein with alternating acidic/basic stretches (E/K/R-rich) and lacks any domain architecture typical of transcription elongation regulators (no PWWP, bromodomain, TFIIS-like motifs, or specific protein-protein interaction modules). This charged, repetitive, disordered architecture is characteristic of microtubule-associated proteins (MAPs), whose microtubule-binding regions are typically unstructured and electrostatic. Thus general protein-architecture reasoning favors D over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Specific recognition of the MAP7 domain signature (a ~200-300 aa microtubule-binding domain) from the sequence alone would require prior knowledge of this domain family. However, this is not strictly necessary given the strong elimination of A and C and the architectural argument favoring D over B.",
    "reason": "The four options span radically different biological contexts (venom, transcription, bacterial NRPS, cytoskeleton), allowing a model to eliminate A and C through organism/domain logic and to favor D over B through protein-architecture reasoning (large disordered charged protein without transcription-specific domains). While precise MAP7 domain identification adds confidence, the reasoning path to D does not depend solely on memorizing this protein's annotation."
  },
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "C9",
      "H3",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry D4A4L4 (MAP7D2, Rat) carries GO:0000226 'microtubule cytoskeleton organization' with IMP evidence (PubMed:35470240). The function comment explicitly states 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' and describes kinesin-1 cofactor activity on microtubules. The protein is named 'MAP7 domain-containing protein 2,' where MAP7 is a well-characterized microtubule-associated protein family. The sequence matches exactly (SHA-256 confirmed). The GO term text matches option D verbatim."
  },
  "important_caveats": [
    "The GO:0000226 annotation is supported by IMP evidence (PubMed:35470240, 2022), while the 'axon development' annotation (GO:0061564) is from PubMed:30784582 (2019). Both are experimental (IMP), not purely computational.",
    "The MAP7 domain in this sequence is not a universally recognized motif like a kinase or zinc finger; a model relying solely on de novo domain recognition might find B vs D less clear-cut than the elimination of A and C.",
    "The protein was first publicly released in UniProt in April 2025; the author's source snapshot is unknown but the sequence matches the current and archived (v89) entries.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning assessment above considers only what a model could infer from the sequence and general biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are essentially impossible for a rat protein (wrong organism context, wrong domain architecture). Option B is disfavored by the absence of transcription-regulatory domains and the presence of MAP-like architecture. Only D is consistent with the sequence features and the protein's identity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry D4A4L4 (MAP7D2, Rat) carries GO:0000226 'microtubule cytoskeleton organization' with IMP evidence (PubMed:35470240). The function comment explicitly states 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' and describes kinesin-1 cofactor activity on microtubules. The protein is named 'MAP7 domain-containing protein 2,' where MAP7 is a well-characterized microtubule-associated protein family. The sequence matches exactly (SHA-256 confirmed). The GO term text matches option D verbatim.",
    "evidence_ids": ["C5", "C7", "C9", "H3", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A and C can be eliminated with high confidence through general biology: (1) 'venom-mediated fibrinolysis' requires a secreted venom protease (serine or metalloprotease motif), which is absent from this 763-aa rat brain protein; (2) 'amino acid activation for nonribosomal peptide biosynthetic process' is exclusively a bacterial/fungal NRPS enzymatic process (requires adenylation, thiolation, condensation domains) and is incompatible with a mammalian protein. Between the remaining B and D: the sequence is a large, highly charged, intrinsically disordered protein with alternating acidic/basic stretches (E/K/R-rich) and lacks any domain architecture typical of transcription elongation regulators (no PWWP, bromodomain, TFIIS-like motifs, or specific protein-protein interaction modules). This charged, repetitive, disordered architecture is characteristic of microtubule-associated proteins (MAPs), whose microtubule-binding regions are typically unstructured and electrostatic. Thus general protein-architecture reasoning favors D over B.",
    "missing_item_specific_fact": "Specific recognition of the MAP7 domain signature (a ~200-300 aa microtubule-binding domain) from the sequence alone would require prior knowledge of this domain family. However, this is not strictly necessary given the strong elimination of A and C and the architectural argument favoring D over B.",
    "reason": "The four options span radically different biological contexts (venom, transcription, bacterial NRPS, cytoskeleton), allowing a model to eliminate A and C through organism/domain logic and to favor D over B through protein-architecture reasoning (large disordered charged protein without transcription-specific domains). While precise MAP7 domain identification adds confidence, the reasoning path to D does not depend solely on memorizing this protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are essentially impossible for a rat protein (wrong organism context, wrong domain architecture). Option B is disfavored by the absence of transcription-regulatory domains and the presence of MAP-like architecture. Only D is consistent with the sequence features and the protein's identity."
  },
  "important_caveats": [
    "The GO:0000226 annotation is supported by IMP evidence (PubMed:35470240, 2022), while the 'axon development' annotation (GO:0061564) is from PubMed:30784582 (2019). Both are experimental (IMP), not purely computational.",
    "The MAP7 domain in this sequence is not a universally recognized motif like a kinase or zinc finger; a model relying solely on de novo domain recognition might find B vs D less clear-cut than the elimination of A and C.",
    "The protein was first publicly released in UniProt in April 2025; the author's source snapshot is unknown but the sequence matches the current and archived (v89) entries.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model; the reasoning assessment above considers only what a model could infer from the sequence and general biology."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the UniProt record, which describes a microtubule-stabilizing protein and annotates microtubule cytoskeleton organization with IMP evidence. This supports D, while noting that the GO annotation is an inference from mutant phenotype rather than a direct assay of every aspect of the process.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a long, highly charged protein with extensive coiled-coil-like and low-complexity regions, not an obvious catalytic enzyme. That architecture is consistent with a cytoskeletal-associated structural or regulatory protein and unlike the enzymes implied by venom-mediated fibrinolysis or nonribosomal amino acid activation. Transferable knowledge of MAP7-family proteins as microtubule-associated proteins makes microtubule cytoskeleton organization the best fit among the offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable family/architecture knowledge provide a meaningful basis for choosing D over these alternatives, even though they do not independently establish the exact GO annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the microtubule-related process is distinctly better supported by the sequence architecture and family-level inference.


### Important caveats

- Reviewer-only source evidence confirms the key but was not available as an input to the evaluated model.
- The sequence-based family and function inference is probabilistic; the sequence alone does not prove a particular GO annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long, highly charged protein with extensive coiled-coil-like and low-complexity regions, not an obvious catalytic enzyme. That architecture is consistent with a cytoskeletal-associated structural or regulatory protein and unlike the enzymes implied by venom-mediated fibrinolysis or nonribosomal amino acid activation. Transferable knowledge of MAP7-family proteins as microtubule-associated proteins makes microtubule cytoskeleton organization the best fit among the offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable family/architecture knowledge provide a meaningful basis for choosing D over these alternatives, even though they do not independently establish the exact GO annotation."
  },
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, which describes a microtubule-stabilizing protein and annotates microtubule cytoskeleton organization with IMP evidence. This supports D, while noting that the GO annotation is an inference from mutant phenotype rather than a direct assay of every aspect of the process."
  },
  "important_caveats": [
    "Reviewer-only source evidence confirms the key but was not available as an input to the evaluated model.",
    "The sequence-based family and function inference is probabilistic; the sequence alone does not prove a particular GO annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the microtubule-related process is distinctly better supported by the sequence architecture and family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, which describes a microtubule-stabilizing protein and annotates microtubule cytoskeleton organization with IMP evidence. This supports D, while noting that the GO annotation is an inference from mutant phenotype rather than a direct assay of every aspect of the process.",
    "evidence_ids": ["C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a long, highly charged protein with extensive coiled-coil-like and low-complexity regions, not an obvious catalytic enzyme. That architecture is consistent with a cytoskeletal-associated structural or regulatory protein and unlike the enzymes implied by venom-mediated fibrinolysis or nonribosomal amino acid activation. Transferable knowledge of MAP7-family proteins as microtubule-associated proteins makes microtubule cytoskeleton organization the best fit among the offered choices.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable family/architecture knowledge provide a meaningful basis for choosing D over these alternatives, even though they do not independently establish the exact GO annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the microtubule-related process is distinctly better supported by the sequence architecture and family-level inference."
  },
  "important_caveats": [
    "Reviewer-only source evidence confirms the key but was not available as an input to the evaluated model.",
    "The sequence-based family and function inference is probabilistic; the sequence alone does not prove a particular GO annotation."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry D4A4L4 (MAP7D2_RAT) explicitly annotates GO:0000226 'microtubule cytoskeleton organization' with IMP:UniProtKB evidence code (PubMed:35470240). The FUNCTION comment describes it as a 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' and a 'critical cofactor for kinesin transport.' The GO term matches option D exactly. The evidence is from a mutant phenotype study (IMP), providing experimental support.

Citations as saved: [C7](#evidence-c7), [C5](#evidence-c5), [C9](#evidence-c9), [H5](#evidence-h5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~200 residues display an extended coiled-coil domain with the classic heptad repeat pattern (hydrophobic residues at a/d positions, charged residues at e/g positions): 'ERQRLAKERREEREKCLAAREQQILEKQKRAKLQYEKQIEERWRKLEEQRQREDQKRAAVEEKRKQKLREEEERLEAMMRRSLERTQQLELKKK'. This architecture—an unusually long coiled-coil (~200+ aa) followed by multiple proline/serine-rich disordered regions and a C-terminal domain—is the hallmark of the MAP7 protein family (MAP7, MAP7D1, MAP7D2, E-MAP-115). All known members of this family are microtubule-associated proteins. This family-level recognition allows elimination of: (A) venom fibrinolysis requires a small secreted serine protease with catalytic triad—absent here; (C) NRPS amino acid activation requires adenylation domain motifs (PP-binding, specific catalytic residues)—absent; (B) transcription elongation factors with coiled-coils typically have short dimerization coiled-coils (30-50 aa), not the extended ~200-residue structural coiled-coil seen here, and lack the disordered MAP-linker architecture. The MAP7 coiled-coil domain is a well-characterized family signature in structural biology databases, providing transferable knowledge from multiple family members to identify this protein as a microtubule-associated protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The extended coiled-coil domain with MAP7-family heptad pattern, combined with the overall multi-domain architecture (long CC + disordered linkers + C-terminal region), is a recognizable family-level signature. Knowledge of the MAP7 family (MAP7, MAP7D1, MAP7D2) and their shared microtubule-binding function provides a concrete transferable basis to select D over the other three options, which require entirely different sequence architectures.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different protein classes (venom protease, transcription factor, NRPS enzyme, structural MAP). The extended coiled-coil architecture uniquely points to the MAP family among these choices. No other option is defensible given the sequence features.


### Important caveats

- The protein also carries GO:0061564 'axon development' (IMP), which is not among the options but is a more specific annotation. The question asks for the 'primary biological process' and GO:0000226 is a valid parent-level term.
- The coiled-coil domain recognition relies on pattern matching to the MAP7 family signature; without explicit domain annotation in the input, this requires trained pattern recognition of heptad repeats.
- The sequence is from Rattus norvegicus (rat) per UniProt, but organism identity was not provided to the model and is not needed for the family-level inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~200 residues display an extended coiled-coil domain with the classic heptad repeat pattern (hydrophobic residues at a/d positions, charged residues at e/g positions): 'ERQRLAKERREEREKCLAAREQQILEKQKRAKLQYEKQIEERWRKLEEQRQREDQKRAAVEEKRKQKLREEEERLEAMMRRSLERTQQLELKKK'. This architecture—an unusually long coiled-coil (~200+ aa) followed by multiple proline/serine-rich disordered regions and a C-terminal domain—is the hallmark of the MAP7 protein family (MAP7, MAP7D1, MAP7D2, E-MAP-115). All known members of this family are microtubule-associated proteins. This family-level recognition allows elimination of: (A) venom fibrinolysis requires a small secreted serine protease with catalytic triad—absent here; (C) NRPS amino acid activation requires adenylation domain motifs (PP-binding, specific catalytic residues)—absent; (B) transcription elongation factors with coiled-coils typically have short dimerization coiled-coils (30-50 aa), not the extended ~200-residue structural coiled-coil seen here, and lack the disordered MAP-linker architecture. The MAP7 coiled-coil domain is a well-characterized family signature in structural biology databases, providing transferable knowledge from multiple family members to identify this protein as a microtubule-associated protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The extended coiled-coil domain with MAP7-family heptad pattern, combined with the overall multi-domain architecture (long CC + disordered linkers + C-terminal region), is a recognizable family-level signature. Knowledge of the MAP7 family (MAP7, MAP7D1, MAP7D2) and their shared microtubule-binding function provides a concrete transferable basis to select D over the other three options, which require entirely different sequence architectures."
  },
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C5",
      "C9",
      "H5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry D4A4L4 (MAP7D2_RAT) explicitly annotates GO:0000226 'microtubule cytoskeleton organization' with IMP:UniProtKB evidence code (PubMed:35470240). The FUNCTION comment describes it as a 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' and a 'critical cofactor for kinesin transport.' The GO term matches option D exactly. The evidence is from a mutant phenotype study (IMP), providing experimental support."
  },
  "important_caveats": [
    "The protein also carries GO:0061564 'axon development' (IMP), which is not among the options but is a more specific annotation. The question asks for the 'primary biological process' and GO:0000226 is a valid parent-level term.",
    "The coiled-coil domain recognition relies on pattern matching to the MAP7 family signature; without explicit domain annotation in the input, this requires trained pattern recognition of heptad repeats.",
    "The sequence is from Rattus norvegicus (rat) per UniProt, but organism identity was not provided to the model and is not needed for the family-level inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes (venom protease, transcription factor, NRPS enzyme, structural MAP). The extended coiled-coil architecture uniquely points to the MAP family among these choices. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry D4A4L4 (MAP7D2_RAT) explicitly annotates GO:0000226 'microtubule cytoskeleton organization' with IMP:UniProtKB evidence code (PubMed:35470240). The FUNCTION comment describes it as a 'Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth' and a 'critical cofactor for kinesin transport.' The GO term matches option D exactly. The evidence is from a mutant phenotype study (IMP), providing experimental support.",
    "evidence_ids": ["C7", "C5", "C9", "H5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~200 residues display an extended coiled-coil domain with the classic heptad repeat pattern (hydrophobic residues at a/d positions, charged residues at e/g positions): 'ERQRLAKERREEREKCLAAREQQILEKQKRAKLQYEKQIEERWRKLEEQRQREDQKRAAVEEKRKQKLREEEERLEAMMRRSLERTQQLELKKK'. This architecture—an unusually long coiled-coil (~200+ aa) followed by multiple proline/serine-rich disordered regions and a C-terminal domain—is the hallmark of the MAP7 protein family (MAP7, MAP7D1, MAP7D2, E-MAP-115). All known members of this family are microtubule-associated proteins. This family-level recognition allows elimination of: (A) venom fibrinolysis requires a small secreted serine protease with catalytic triad—absent here; (C) NRPS amino acid activation requires adenylation domain motifs (PP-binding, specific catalytic residues)—absent; (B) transcription elongation factors with coiled-coils typically have short dimerization coiled-coils (30-50 aa), not the extended ~200-residue structural coiled-coil seen here, and lack the disordered MAP-linker architecture. The MAP7 coiled-coil domain is a well-characterized family signature in structural biology databases, providing transferable knowledge from multiple family members to identify this protein as a microtubule-associated protein.",
    "missing_item_specific_fact": "",
    "reason": "The extended coiled-coil domain with MAP7-family heptad pattern, combined with the overall multi-domain architecture (long CC + disordered linkers + C-terminal region), is a recognizable family-level signature. Knowledge of the MAP7 family (MAP7, MAP7D1, MAP7D2) and their shared microtubule-binding function provides a concrete transferable basis to select D over the other three options, which require entirely different sequence architectures."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes (venom protease, transcription factor, NRPS enzyme, structural MAP). The extended coiled-coil architecture uniquely points to the MAP family among these choices. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The protein also carries GO:0061564 'axon development' (IMP), which is not among the options but is a more specific annotation. The question asks for the 'primary biological process' and GO:0000226 is a valid parent-level term.",
    "The coiled-coil domain recognition relies on pattern matching to the MAP7 family signature; without explicit domain annotation in the input, this requires trained pattern recognition of heptad repeats.",
    "The sequence is from Rattus norvegicus (rat) per UniProt, but organism identity was not provided to the model and is not needed for the family-level inference."
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
  "requested_accession": "D4A4L4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "9f83a28f18a3ddef374f5b11aa7538748ba9db51c5a423b7b6975f09f4db2855",
  "benchmark_sequence_length": 763,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 90,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2022-05-25",
    "sequenceVersion": 4
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "current_source_sequence_sha256": "9f83a28f18a3ddef374f5b11aa7538748ba9db51c5a423b7b6975f09f4db2855",
  "current_source_sequence_length": 763,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 89,
  "selected_historical_version": {
    "accession": "D4A4L4",
    "database": "Swiss-Prot",
    "entryVersion": 89,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MA7D2_RAT",
    "sequenceVersion": 4
  },
  "selected_historical_record_sha256": "86c6555798622b5baa0bd1337356f1304f14355ea4b631126a5d35b217aec7c9",
  "selected_historical_source_sequence_sha256": "9f83a28f18a3ddef374f5b11aa7538748ba9db51c5a423b7b6975f09f4db2855",
  "selected_historical_source_sequence_length": 763,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 89,
      "exact_sequence_comparison": "matched",
      "sequence_version": 4
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4A4L4.json",
  "source_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "retrieved_utc": "2026-11-02T04:27:48.272925+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"D4A4L4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4A4L4.json",
  "source_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "retrieved_utc": "2026-11-02T04:27:48.272925+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":90,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2022-05-25\",\"sequenceVersion\":4}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4A4L4.json",
  "source_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "retrieved_utc": "2026-11-02T04:27:48.272925+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Rat\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4A4L4.json",
  "source_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "retrieved_utc": "2026-11-02T04:27:48.272925+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.1\",\"source\":\"Reference\"}],\"value\":\"Brain-enriched E-MAP-115-like protein\"}}],\"recommendedName\":{\"fullName\":{\"value\":\"MAP7 domain-containing protein 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4A4L4.json",
  "source_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "retrieved_utc": "2026-11-02T04:27:48.272925+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A2AG50\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30784582\",\"source\":\"PubMed\"}],\"value\":\"Microtubule-stabilizing protein involved in the control of cell motility and neurite outgrowth (By similarity). Acts as a critical cofactor for kinesin transport; in the proximal axon regulates kinesin-1 family members, KIF5A, KIF5B and KIF5C recruitment to microtubules and contributes to kinesin-1-mediated transport in the axons (PubMed:30784582)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4A4L4.json",
  "source_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "retrieved_utc": "2026-11-02T04:27:48.272925+00:00",
  "json_pointer": "/uniProtKBCrossReferences/39",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"30784582\",\"source\":\"PubMed\"}],\"id\":\"GO:0061564\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:axon development\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4A4L4.json",
  "source_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "retrieved_utc": "2026-11-02T04:27:48.272925+00:00",
  "json_pointer": "/uniProtKBCrossReferences/40",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"35470240\",\"source\":\"PubMed\"}],\"id\":\"GO:0000226\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:microtubule cytoskeleton organization\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4A4L4.json",
  "source_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "retrieved_utc": "2026-11-02T04:27:48.272925+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Pan X.\",\"Cao Y.\",\"Stucchi R.\",\"Hooikaas P.J.\",\"Portegies S.\",\"Will L.\",\"Martin M.\",\"Akhmanova A.\",\"Harterink M.\",\"Hoogenraad C.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30784582\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.celrep.2019.01.084\"}],\"citationType\":\"journal article\",\"firstPage\":\"1988\",\"id\":\"30784582\",\"journal\":\"Cell Rep.\",\"lastPage\":\"1999.e6\",\"publicationDate\":\"2019\",\"title\":\"MAP7D2 Localizes to the Proximal Axon and Locally Promotes Kinesin-1-Mediated Cargo Transport into the Axon.\",\"volume\":\"26\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4A4L4.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/D4A4L4.json",
  "source_sha256": "0d37ad5d40219180e220dafa1510690a87aca9ddbb94e64922e34175051fa1e2",
  "retrieved_utc": "2026-11-02T04:27:48.272925+00:00",
  "json_pointer": "/references/4",
  "excerpt": "{\"citation\":{\"authors\":[\"Kikuchi K.\",\"Sakamoto Y.\",\"Uezu A.\",\"Yamamoto H.\",\"Ishiguro K.I.\",\"Shimamura K.\",\"Saito T.\",\"Hisanaga S.I.\",\"Nakanishi H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35470240\"},{\"database\":\"DOI\",\"id\":\"10.26508/lsa.202201390\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"35470240\",\"journal\":\"Life. Sci Alliance\",\"lastPage\":\"0\",\"publicationDate\":\"2022\",\"title\":\"Map7D2 and Map7D1 facilitate microtubule stabilization through distinct mechanisms in neuronal cells.\",\"volume\":\"5\"},\"referenceNumber\":5,\"referencePositions\":[\"TISSUE SPECIFICITY\",\"SUBCELLULAR LOCATION\",\"INTERACTION WITH MICROTUBULES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89",
  "source_sha256": "86c6555798622b5baa0bd1337356f1304f14355ea4b631126a5d35b217aec7c9",
  "retrieved_utc": "2026-11-02T04:27:53.462029+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   MA7D2_RAT               Reviewed;         763 AA.\nAC   D4A4L4; W0T3G7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-MAY-2022, sequence version 4.\nDT   28-JAN-2026, entry version 89.\nDE   RecName: Full=MAP7 domain-containing protein 2;\nDE   AltName: Full=Brain-enriched E-MAP-115-like protein {ECO:0000303|Ref.1};\nGN   Name=Map7d2; Synonyms=Brelin {ECO:0000303|Ref.1}, Mtap7d2;\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89",
  "source_sha256": "86c6555798622b5baa0bd1337356f1304f14355ea4b631126a5d35b217aec7c9",
  "retrieved_utc": "2026-11-02T04:27:53.462029+00:00",
  "source_locator": "lines 76-83",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND SUBUNIT.\nRX   PubMed=30784582; DOI=10.1016/j.celrep.2019.01.084;\nRA   Pan X., Cao Y., Stucchi R., Hooikaas P.J., Portegies S., Will L.,\nRA   Martin M., Akhmanova A., Harterink M., Hoogenraad C.C.;\nRT   \"MAP7D2 Localizes to the Proximal Axon and Locally Promotes Kinesin-1-\nRT   Mediated Cargo Transport into the Axon.\";\nRL   Cell Rep. 26:1988-1999.e6(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89",
  "source_sha256": "86c6555798622b5baa0bd1337356f1304f14355ea4b631126a5d35b217aec7c9",
  "retrieved_utc": "2026-11-02T04:27:53.462029+00:00",
  "source_locator": "lines 93-99",
  "excerpt": "CC   -!- FUNCTION: Microtubule-stabilizing protein involved in the control of\nCC       cell motility and neurite outgrowth (By similarity). Acts as a critical\nCC       cofactor for kinesin transport; in the proximal axon regulates kinesin-\nCC       1 family members, KIF5A, KIF5B and KIF5C recruitment to microtubules\nCC       and contributes to kinesin-1-mediated transport in the axons\nCC       (PubMed:30784582). {ECO:0000250|UniProtKB:A2AG50,\nCC       ECO:0000269|PubMed:30784582}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89",
  "source_sha256": "86c6555798622b5baa0bd1337356f1304f14355ea4b631126a5d35b217aec7c9",
  "retrieved_utc": "2026-11-02T04:27:53.462029+00:00",
  "source_locator": "lines 151-151",
  "excerpt": "DR   GO; GO:0061564; P:axon development; IMP:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 4,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/D4A4L4?format=txt&versions=89",
  "source_sha256": "86c6555798622b5baa0bd1337356f1304f14355ea4b631126a5d35b217aec7c9",
  "retrieved_utc": "2026-11-02T04:27:53.462029+00:00",
  "source_locator": "lines 152-152",
  "excerpt": "DR   GO; GO:0000226; P:microtubule cytoskeleton organization; IMP:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 4,
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
  "source_locator": "lines 2328-2338",
  "excerpt": "[Term]\nid: GO:0000226\nname: microtubule cytoskeleton organization\nnamespace: biological_process\ndef: \"A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of cytoskeletal structures comprising microtubules and their associated proteins.\" [GOC:mah]\nsubset: goslim_pombe\nsynonym: \"microtubule cytoskeleton organisation\" EXACT [GOC:mah]\nsynonym: \"microtubule cytoskeleton organization and biogenesis\" RELATED [GOC:mah]\nis_a: GO:0007010 ! cytoskeleton organization\nis_a: GO:0007017 ! microtubule-based process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0000226"
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
  "source_locator": "lines 192437-192450",
  "excerpt": "[Term]\nid: GO:0032968\nname: positive regulation of transcription elongation by RNA polymerase II\nnamespace: biological_process\nalt_id: GO:0090040\ndef: \"Any process that activates or increases the frequency, rate or extent of transcription elongation, the extension of an RNA molecule after transcription initiation and promoter clearance by the addition of ribonucleotides, catalyzed by RNA polymerase II.\" [GOC:mah, GOC:txnOH]\nsynonym: \"positive regulation of gene-specific transcription elongation from RNA polymerase II promoter\" RELATED []\nsynonym: \"positive regulation of RNA elongation from RNA polymerase II promoter\" EXACT []\nsynonym: \"positive regulation of transcription elongation from RNA polymerase II promoter\" EXACT []\nis_a: GO:0032786 ! positive regulation of DNA-templated transcription, elongation\nis_a: GO:0034243 ! regulation of transcription elongation by RNA polymerase II\nis_a: GO:0045944 ! positive regulation of transcription by RNA polymerase II\nrelationship: positively_regulates GO:0006368 ! transcription elongation by RNA polymerase II\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0032968"
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
  "source_locator": "lines 243406-243414",
  "excerpt": "[Term]\nid: GO:0043041\nname: amino acid activation for nonribosomal peptide biosynthetic process\nnamespace: biological_process\ndef: \"Activation of an amino acid for incorporation into a peptide by a nonribosomal process.\" [GOC:jl]\nsynonym: \"nonribosomal amino acid activation\" RELATED []\nis_a: GO:0043038 ! amino acid activation\nrelationship: part_of GO:0019184 ! nonribosomal peptide biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0043041"
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
  "source_locator": "lines 257660-257669",
  "excerpt": "[Term]\nid: GO:0044484\nname: venom-mediated fibrinolysis\nnamespace: biological_process\ndef: \"A process in which an organism causes fibrinolysis in another organism via the action of a venom. Fibrinolysis is a process that solubilizes fibrin in the blood, chiefly by the proteolytic action of plasmin.\" [GOC:fj, GOC:jl, PMID:17433397, PMID:17544404]\nsynonym: \"envenomation resulting in fibrinolysis\" EXACT []\nsynonym: \"envenomation resulting in fibrinolysis in another organism\" EXACT []\nsynonym: \"envenomation resulting in fibrinolysis in other organism\" EXACT []\nis_a: GO:0044483 ! venom-mediated perturbation of hemostasis\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0044484"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
