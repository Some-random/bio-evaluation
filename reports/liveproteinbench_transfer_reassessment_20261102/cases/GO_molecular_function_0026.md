# GO_molecular_function_0026: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_molecular_function_0026.txt)

**Task:** `GO_molecular_function`  
**Author key, unchanged:** **D** — alpha-1,6-mannosyltransferase activity

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
MWSLDPSQKEVLRFAVSCRILTLMLQALFNIIIPDHHADAFSPPRLASSCSVDQLVEGLLGGLSRWDAEHFLFIAEHGYLYEHNFAFFPGFPLALLMGTELLRPLQGLLSQRSCLLVSVALLNFLFSVLAAVTLHDLGCLVLGCPRQAFYAAMLFCLSPANVFLAAGYSEALFAFLTFSAMGQLERGRSWASGLLFALATGVRSNGLVSVGFLLHAQCRGFFSSLVVLNPLKPLFKLMASLCLSVLTVSLPFALFQYYAYTQFCLPGSAHSVPEPLVQLAVDKGYRITGGNEPPWCSWGLPLVYSYIQDVYWNVGFLRYYELRQVPNFLLATPVAVLVVWAAWTYVTTHPWLCLTLGLRRSKDSKKTLEKPHPGFLSPKVFVYLVHAAGLLLFGSLCMHVQVLTRLLCSSTPVVYWFPAHLLQNQEPLLRSVDTVPEKLLEKNSPPGQKAPRNCIMKLLYNWRACSPVTRCILGYFLTYWLLGLLLHCNFLPWT

[Multiple Choices]
A. 4 iron, 4 sulfur cluster binding
B. Hsp90 protein binding
C. NADPH dehydrogenase (quinone) activity
D. alpha-1,6-mannosyltransferase activity
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

> The reviewer-only UniProt record matches the supplied 494-aa sequence and identifies the protein as GPI alpha-1,6-mannosyltransferase 2. Its functional and catalytic-activity annotations cite experimental evidence (ECO:0000269, PMID:23694781), supporting choice D. The evidence supports the enzyme activity, not merely a computational GO assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and consistent with a polytopic membrane protein, making a membrane-associated glycosylation role plausible; it does not show an obvious iron-sulfur-cluster-binding motif or a recognizable NADPH-binding domain. These clues can make some distractors less plausible but do not identify the alpha-1,6 linkage or its specific substrate.


**Missing item-specific fact**

> The protein-specific identity and experimentally characterized catalytic activity of this sequence as GPI mannosyltransferase II are needed to distinguish D confidently from other membrane-protein functions.


**Reason**

> General sequence features suggest membrane localization but do not establish the precise molecular function or substrate specificity. Selecting D therefore depends on protein-specific annotation, homology recognition, or experimental knowledge not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only evidence supports D for the matched sequence. The sequence alone does not make the precise activity clear, but no alternative choice is comparably supported by the supplied information.


### Important caveats

- The UniProt annotation and its cited experimental evidence are reviewer-only and were absent from the evaluated model input.
- The source record matches the sequence, but the author's exact annotation snapshot is unknown; the matched historical record also supports the function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a polytopic membrane protein, making a membrane-associated glycosylation role plausible; it does not show an obvious iron-sulfur-cluster-binding motif or a recognizable NADPH-binding domain. These clues can make some distractors less plausible but do not identify the alpha-1,6 linkage or its specific substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and experimentally characterized catalytic activity of this sequence as GPI mannosyltransferase II are needed to distinguish D confidently from other membrane-protein functions.",
    "reason": "General sequence features suggest membrane localization but do not establish the precise molecular function or substrate specificity. Selecting D therefore depends on protein-specific annotation, homology recognition, or experimental knowledge not supplied in the question."
  },
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only UniProt record matches the supplied 494-aa sequence and identifies the protein as GPI alpha-1,6-mannosyltransferase 2. Its functional and catalytic-activity annotations cite experimental evidence (ECO:0000269, PMID:23694781), supporting choice D. The evidence supports the enzyme activity, not merely a computational GO assignment."
  },
  "important_caveats": [
    "The UniProt annotation and its cited experimental evidence are reviewer-only and were absent from the evaluated model input.",
    "The source record matches the sequence, but the author's exact annotation snapshot is unknown; the matched historical record also supports the function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D for the matched sequence. The sequence alone does not make the precise activity clear, but no alternative choice is comparably supported by the supplied information."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only UniProt record matches the supplied 494-aa sequence and identifies the protein as GPI alpha-1,6-mannosyltransferase 2. Its functional and catalytic-activity annotations cite experimental evidence (ECO:0000269, PMID:23694781), supporting choice D. The evidence supports the enzyme activity, not merely a computational GO assignment.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a polytopic membrane protein, making a membrane-associated glycosylation role plausible; it does not show an obvious iron-sulfur-cluster-binding motif or a recognizable NADPH-binding domain. These clues can make some distractors less plausible but do not identify the alpha-1,6 linkage or its specific substrate.",
    "missing_item_specific_fact": "The protein-specific identity and experimentally characterized catalytic activity of this sequence as GPI mannosyltransferase II are needed to distinguish D confidently from other membrane-protein functions.",
    "reason": "General sequence features suggest membrane localization but do not establish the precise molecular function or substrate specificity. Selecting D therefore depends on protein-specific annotation, homology recognition, or experimental knowledge not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only evidence supports D for the matched sequence. The sequence alone does not make the precise activity clear, but no alternative choice is comparably supported by the supplied information."
  },
  "important_caveats": [
    "The UniProt annotation and its cited experimental evidence are reviewer-only and were absent from the evaluated model input.",
    "The source record matches the sequence, but the author's exact annotation snapshot is unknown; the matched historical record also supports the function."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A8C2M425 (PIGV_CRIGR, GPI alpha-1,6-mannosyltransferase 2) with exact SHA256 match. The UniProt entry provides experimental evidence (ECO:0000269, PubMed:23694781) for alpha-1,6-mannosyltransferase function, including catalytic activity (RHEA:60488) and GO:0000009 annotation. The recommended name explicitly states 'GPI alpha-1,6-mannosyltransferase 2' and the FUNCTION comment describes alpha-1,6-mannosyltransferase catalysis.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [GO1](#evidence-go1), [GO5](#evidence-go5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a heavily hydrophobic multi-pass transmembrane protein (~10+ TM segments), which is inconsistent with soluble Hsp90 interactors (B) and lacks clustered Cys motifs characteristic of 4Fe-4S cluster binding (A). It also lacks Rossmann-fold NADPH-binding motifs expected for NADPH dehydrogenase (C). This partial elimination of A, B, C is somewhat defensible from general knowledge. However, positively identifying the specific 'alpha-1,6-mannosyltransferase' activity from sequence alone requires recognizing PIGV/GPI-MT-II family-specific motifs or the protein itself.


**Missing item-specific fact**

> Recognition of specific GPI mannosyltransferase II (PIGV) family sequence motifs or the identity of the protein as PIGV/GPI-MT-II is needed to positively assign alpha-1,6-mannosyltransferase activity rather than other membrane-bound glycosyltransferase or transporter functions.


**Reason**

> While general reasoning can weakly eliminate options A, B, and C based on absence of characteristic motifs (Fe-S Cys clusters, Hsp90-binding domains, NADPH Rossmann fold), the positive identification of 'alpha-1,6-mannosyltransferase activity' from a multi-TM membrane protein sequence requires specific family-level knowledge of GPI mannosyltransferases. The membrane-bound architecture is consistent with many protein classes, not uniquely with mannosyltransferases. Selection of D over other membrane protein functions depends on recognizing this specific protein or its family annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are sufficiently distinct in their molecular function classes. A (metal cluster binding), B (protein-protein interaction), C (oxidoreductase), and D (glycosyltransferase) represent different functional categories. The multi-TM membrane architecture of the sequence makes A, B, and C less plausible, leaving D as the most defensible choice among the four, even if positive identification is difficult from sequence alone.


### Important caveats

- The UniProt GO:0000009 annotation carries evidence code IEA:Ensembl (computational transfer), though the underlying function is experimentally supported (ECO:0000269, PubMed:23694781).
- The protein entry was first public in June 2025; the benchmark construction date is unknown, so the annotation may or may not have been available to the author.
- The sequence is from Chinese hamster (Cricetulus griseus), a less commonly studied organism, making memorization of this specific entry less likely than for well-characterized human proteins.
- GO:0120563 (dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity) is the more specific term annotated, and it is_a GO:0000009, making option D a valid parent-level description.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a heavily hydrophobic multi-pass transmembrane protein (~10+ TM segments), which is inconsistent with soluble Hsp90 interactors (B) and lacks clustered Cys motifs characteristic of 4Fe-4S cluster binding (A). It also lacks Rossmann-fold NADPH-binding motifs expected for NADPH dehydrogenase (C). This partial elimination of A, B, C is somewhat defensible from general knowledge. However, positively identifying the specific 'alpha-1,6-mannosyltransferase' activity from sequence alone requires recognizing PIGV/GPI-MT-II family-specific motifs or the protein itself.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Recognition of specific GPI mannosyltransferase II (PIGV) family sequence motifs or the identity of the protein as PIGV/GPI-MT-II is needed to positively assign alpha-1,6-mannosyltransferase activity rather than other membrane-bound glycosyltransferase or transporter functions.",
    "reason": "While general reasoning can weakly eliminate options A, B, and C based on absence of characteristic motifs (Fe-S Cys clusters, Hsp90-binding domains, NADPH Rossmann fold), the positive identification of 'alpha-1,6-mannosyltransferase activity' from a multi-TM membrane protein sequence requires specific family-level knowledge of GPI mannosyltransferases. The membrane-bound architecture is consistent with many protein classes, not uniquely with mannosyltransferases. Selection of D over other membrane protein functions depends on recognizing this specific protein or its family annotation."
  },
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C8",
      "H1",
      "H3",
      "H4",
      "H6",
      "GO1",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A8C2M425 (PIGV_CRIGR, GPI alpha-1,6-mannosyltransferase 2) with exact SHA256 match. The UniProt entry provides experimental evidence (ECO:0000269, PubMed:23694781) for alpha-1,6-mannosyltransferase function, including catalytic activity (RHEA:60488) and GO:0000009 annotation. The recommended name explicitly states 'GPI alpha-1,6-mannosyltransferase 2' and the FUNCTION comment describes alpha-1,6-mannosyltransferase catalysis."
  },
  "important_caveats": [
    "The UniProt GO:0000009 annotation carries evidence code IEA:Ensembl (computational transfer), though the underlying function is experimentally supported (ECO:0000269, PubMed:23694781).",
    "The protein entry was first public in June 2025; the benchmark construction date is unknown, so the annotation may or may not have been available to the author.",
    "The sequence is from Chinese hamster (Cricetulus griseus), a less commonly studied organism, making memorization of this specific entry less likely than for well-characterized human proteins.",
    "GO:0120563 (dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity) is the more specific term annotated, and it is_a GO:0000009, making option D a valid parent-level description."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct in their molecular function classes. A (metal cluster binding), B (protein-protein interaction), C (oxidoreductase), and D (glycosyltransferase) represent different functional categories. The multi-TM membrane architecture of the sequence makes A, B, and C less plausible, leaving D as the most defensible choice among the four, even if positive identification is difficult from sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A8C2M425 (PIGV_CRIGR, GPI alpha-1,6-mannosyltransferase 2) with exact SHA256 match. The UniProt entry provides experimental evidence (ECO:0000269, PubMed:23694781) for alpha-1,6-mannosyltransferase function, including catalytic activity (RHEA:60488) and GO:0000009 annotation. The recommended name explicitly states 'GPI alpha-1,6-mannosyltransferase 2' and the FUNCTION comment describes alpha-1,6-mannosyltransferase catalysis.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C8", "H1", "H3", "H4", "H6", "GO1", "GO5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a heavily hydrophobic multi-pass transmembrane protein (~10+ TM segments), which is inconsistent with soluble Hsp90 interactors (B) and lacks clustered Cys motifs characteristic of 4Fe-4S cluster binding (A). It also lacks Rossmann-fold NADPH-binding motifs expected for NADPH dehydrogenase (C). This partial elimination of A, B, C is somewhat defensible from general knowledge. However, positively identifying the specific 'alpha-1,6-mannosyltransferase' activity from sequence alone requires recognizing PIGV/GPI-MT-II family-specific motifs or the protein itself.",
    "missing_item_specific_fact": "Recognition of specific GPI mannosyltransferase II (PIGV) family sequence motifs or the identity of the protein as PIGV/GPI-MT-II is needed to positively assign alpha-1,6-mannosyltransferase activity rather than other membrane-bound glycosyltransferase or transporter functions.",
    "reason": "While general reasoning can weakly eliminate options A, B, and C based on absence of characteristic motifs (Fe-S Cys clusters, Hsp90-binding domains, NADPH Rossmann fold), the positive identification of 'alpha-1,6-mannosyltransferase activity' from a multi-TM membrane protein sequence requires specific family-level knowledge of GPI mannosyltransferases. The membrane-bound architecture is consistent with many protein classes, not uniquely with mannosyltransferases. Selection of D over other membrane protein functions depends on recognizing this specific protein or its family annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are sufficiently distinct in their molecular function classes. A (metal cluster binding), B (protein-protein interaction), C (oxidoreductase), and D (glycosyltransferase) represent different functional categories. The multi-TM membrane architecture of the sequence makes A, B, and C less plausible, leaving D as the most defensible choice among the four, even if positive identification is difficult from sequence alone."
  },
  "important_caveats": [
    "The UniProt GO:0000009 annotation carries evidence code IEA:Ensembl (computational transfer), though the underlying function is experimentally supported (ECO:0000269, PubMed:23694781).",
    "The protein entry was first public in June 2025; the benchmark construction date is unknown, so the annotation may or may not have been available to the author.",
    "The sequence is from Chinese hamster (Cricetulus griseus), a less commonly studied organism, making memorization of this specific entry less likely than for well-characterized human proteins.",
    "GO:0120563 (dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity) is the more specific term annotated, and it is_a GO:0000009, making option D a valid parent-level description."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt records describe alpha-1,6-mannosyltransferase activity and a catalytic reaction transferring mannose to a GPI precursor. The catalytic activity is linked to experimental evidence (ECO:0000269); the separate GO annotation is computationally assigned.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic and consistent with a multipass membrane protein. Together with transferable knowledge of membrane-embedded GPI mannosyltransferases and their homologs, this favors D, a glycosyltransferase activity, over the iron-sulfur-cluster binding, Hsp90-binding, and NADPH-dehydrogenase alternatives. This is a family-level, probabilistic inference rather than proof of the exact substrate or linkage.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices support a meaningful family/topology-based distinction without requiring the target's database annotation or experimental measurement.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only offered choice consistent with the sequence-based membrane-protein and glycosyltransferase inference; the other options describe distinct activities.


### Important caveats

- The sequence's hydrophobicity alone does not establish alpha-1,6 linkage specificity; that finer functional claim is supported by reviewer-only experimental annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane protein. Together with transferable knowledge of membrane-embedded GPI mannosyltransferases and their homologs, this favors D, a glycosyltransferase activity, over the iron-sulfur-cluster binding, Hsp90-binding, and NADPH-dehydrogenase alternatives. This is a family-level, probabilistic inference rather than proof of the exact substrate or linkage.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support a meaningful family/topology-based distinction without requiring the target's database annotation or experimental measurement."
  },
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records describe alpha-1,6-mannosyltransferase activity and a catalytic reaction transferring mannose to a GPI precursor. The catalytic activity is linked to experimental evidence (ECO:0000269); the separate GO annotation is computationally assigned."
  },
  "important_caveats": [
    "The sequence's hydrophobicity alone does not establish alpha-1,6 linkage specificity; that finer functional claim is supported by reviewer-only experimental annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice consistent with the sequence-based membrane-protein and glycosyltransferase inference; the other options describe distinct activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records describe alpha-1,6-mannosyltransferase activity and a catalytic reaction transferring mannose to a GPI precursor. The catalytic activity is linked to experimental evidence (ECO:0000269); the separate GO annotation is computationally assigned.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane protein. Together with transferable knowledge of membrane-embedded GPI mannosyltransferases and their homologs, this favors D, a glycosyltransferase activity, over the iron-sulfur-cluster binding, Hsp90-binding, and NADPH-dehydrogenase alternatives. This is a family-level, probabilistic inference rather than proof of the exact substrate or linkage.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support a meaningful family/topology-based distinction without requiring the target's database annotation or experimental measurement."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice consistent with the sequence-based membrane-protein and glycosyltransferase inference; the other options describe distinct activities."
  },
  "important_caveats": [
    "The sequence's hydrophobicity alone does not establish alpha-1,6 linkage specificity; that finer functional claim is supported by reviewer-only experimental annotation."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A8C2M425) explicitly annotates the protein as 'GPI alpha-1,6-mannosyltransferase 2' (EC 2.4.1.-) with experimental evidence (PubMed:23694781) for its function as an alpha-1,6-mannosyltransferase catalyzing transfer of mannose via an alpha-1,6 bond in GPI-anchor biosynthesis. GO:0000009 (alpha-1,6-mannosyltransferase activity) is annotated, and the more specific GO:0120563 (dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity) is is_a GO:0000009. The expected answer D matches the annotated molecular function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7), [GO1](#evidence-go1), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 494-aa sequence is dominated by long hydrophobic stretches forming approximately 8-10 transmembrane helices, characteristic of a multi-pass ER membrane protein. Among the four options, only alpha-1,6-mannosyltransferase activity (D) is consistent with a multi-pass membrane glycosyltransferase: GPI mannosyltransferases (PIGV, PIGB, PIGW family) are well-known multi-pass membrane proteins embedded in the ER membrane. In contrast: (A) 4Fe-4S cluster binding proteins are typically soluble and contain specific Cys-rich motifs (e.g., CxxCxxCxxC arrangements) absent here; (B) Hsp90 protein binding involves TPR domains or specific peptide motifs not present in this sequence; (C) NADPH dehydrogenase (quinone) activity requires a Rossmann fold (GxGxxG motif) and is typically soluble. The multi-pass membrane topology alone strongly discriminates D from A, B, and C, which are incompatible with the observed sequence architecture. Additionally, the PIGV/GPI-MT-II family is well-characterized across organisms (human Q9NUD9 is the reference), and its multi-pass membrane architecture is a transferable family-level feature.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the clearly multi-pass transmembrane architecture of the sequence to eliminate the three soluble-protein options (A, B, C) and select the membrane-embedded glycosyltransferase option (D). This relies on general principles: glycosyltransferases in the GPI pathway are membrane proteins, while iron-sulfur cluster binders, Hsp90 interactors, and NADPH dehydrogenases are typically soluble. Family-level knowledge of GPI mannosyltransferases as multi-pass membrane proteins is transferable across organisms.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different protein classes with distinct structural requirements. The multi-pass membrane topology of the sequence uniquely matches a glycosyltransferase among the given choices. No other option is compatible with the observed sequence architecture.


### Important caveats

- The GO annotation for GO:0000009 on this entry is IEA:Ensembl (computational), while the experimental evidence (ECO:0000269, PubMed:23694781) supports the specific GPI mannosyltransferase II activity (GO:0120563), which is_a GO:0000009.
- The sequence is from Cricetulus griseus (Chinese hamster), a homolog of human PIGV (Q9NUD9). The reviewer-only evidence confirms this identity, but the model only sees the sequence.
- The option D uses the general term 'alpha-1,6-mannosyltransferase activity' (GO:0000009) rather than the more specific GPI-specific term (GO:0120563), which is a valid parent term.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 494-aa sequence is dominated by long hydrophobic stretches forming approximately 8-10 transmembrane helices, characteristic of a multi-pass ER membrane protein. Among the four options, only alpha-1,6-mannosyltransferase activity (D) is consistent with a multi-pass membrane glycosyltransferase: GPI mannosyltransferases (PIGV, PIGB, PIGW family) are well-known multi-pass membrane proteins embedded in the ER membrane. In contrast: (A) 4Fe-4S cluster binding proteins are typically soluble and contain specific Cys-rich motifs (e.g., CxxCxxCxxC arrangements) absent here; (B) Hsp90 protein binding involves TPR domains or specific peptide motifs not present in this sequence; (C) NADPH dehydrogenase (quinone) activity requires a Rossmann fold (GxGxxG motif) and is typically soluble. The multi-pass membrane topology alone strongly discriminates D from A, B, and C, which are incompatible with the observed sequence architecture. Additionally, the PIGV/GPI-MT-II family is well-characterized across organisms (human Q9NUD9 is the reference), and its multi-pass membrane architecture is a transferable family-level feature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the clearly multi-pass transmembrane architecture of the sequence to eliminate the three soluble-protein options (A, B, C) and select the membrane-embedded glycosyltransferase option (D). This relies on general principles: glycosyltransferases in the GPI pathway are membrane proteins, while iron-sulfur cluster binders, Hsp90 interactors, and NADPH dehydrogenases are typically soluble. Family-level knowledge of GPI mannosyltransferases as multi-pass membrane proteins is transferable across organisms."
  },
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H1",
      "H3",
      "H4",
      "H6",
      "H7",
      "GO1",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A8C2M425) explicitly annotates the protein as 'GPI alpha-1,6-mannosyltransferase 2' (EC 2.4.1.-) with experimental evidence (PubMed:23694781) for its function as an alpha-1,6-mannosyltransferase catalyzing transfer of mannose via an alpha-1,6 bond in GPI-anchor biosynthesis. GO:0000009 (alpha-1,6-mannosyltransferase activity) is annotated, and the more specific GO:0120563 (dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity) is is_a GO:0000009. The expected answer D matches the annotated molecular function."
  },
  "important_caveats": [
    "The GO annotation for GO:0000009 on this entry is IEA:Ensembl (computational), while the experimental evidence (ECO:0000269, PubMed:23694781) supports the specific GPI mannosyltransferase II activity (GO:0120563), which is_a GO:0000009.",
    "The sequence is from Cricetulus griseus (Chinese hamster), a homolog of human PIGV (Q9NUD9). The reviewer-only evidence confirms this identity, but the model only sees the sequence.",
    "The option D uses the general term 'alpha-1,6-mannosyltransferase activity' (GO:0000009) rather than the more specific GPI-specific term (GO:0120563), which is a valid parent term."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes with distinct structural requirements. The multi-pass membrane topology of the sequence uniquely matches a glycosyltransferase among the given choices. No other option is compatible with the observed sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A8C2M425) explicitly annotates the protein as 'GPI alpha-1,6-mannosyltransferase 2' (EC 2.4.1.-) with experimental evidence (PubMed:23694781) for its function as an alpha-1,6-mannosyltransferase catalyzing transfer of mannose via an alpha-1,6 bond in GPI-anchor biosynthesis. GO:0000009 (alpha-1,6-mannosyltransferase activity) is annotated, and the more specific GO:0120563 (dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity) is is_a GO:0000009. The expected answer D matches the annotated molecular function.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H1", "H3", "H4", "H6", "H7", "GO1", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 494-aa sequence is dominated by long hydrophobic stretches forming approximately 8-10 transmembrane helices, characteristic of a multi-pass ER membrane protein. Among the four options, only alpha-1,6-mannosyltransferase activity (D) is consistent with a multi-pass membrane glycosyltransferase: GPI mannosyltransferases (PIGV, PIGB, PIGW family) are well-known multi-pass membrane proteins embedded in the ER membrane. In contrast: (A) 4Fe-4S cluster binding proteins are typically soluble and contain specific Cys-rich motifs (e.g., CxxCxxCxxC arrangements) absent here; (B) Hsp90 protein binding involves TPR domains or specific peptide motifs not present in this sequence; (C) NADPH dehydrogenase (quinone) activity requires a Rossmann fold (GxGxxG motif) and is typically soluble. The multi-pass membrane topology alone strongly discriminates D from A, B, and C, which are incompatible with the observed sequence architecture. Additionally, the PIGV/GPI-MT-II family is well-characterized across organisms (human Q9NUD9 is the reference), and its multi-pass membrane architecture is a transferable family-level feature.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the clearly multi-pass transmembrane architecture of the sequence to eliminate the three soluble-protein options (A, B, C) and select the membrane-embedded glycosyltransferase option (D). This relies on general principles: glycosyltransferases in the GPI pathway are membrane proteins, while iron-sulfur cluster binders, Hsp90 interactors, and NADPH dehydrogenases are typically soluble. Family-level knowledge of GPI mannosyltransferases as multi-pass membrane proteins is transferable across organisms."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes with distinct structural requirements. The multi-pass membrane topology of the sequence uniquely matches a glycosyltransferase among the given choices. No other option is compatible with the observed sequence architecture."
  },
  "important_caveats": [
    "The GO annotation for GO:0000009 on this entry is IEA:Ensembl (computational), while the experimental evidence (ECO:0000269, PubMed:23694781) supports the specific GPI mannosyltransferase II activity (GO:0120563), which is_a GO:0000009.",
    "The sequence is from Cricetulus griseus (Chinese hamster), a homolog of human PIGV (Q9NUD9). The reviewer-only evidence confirms this identity, but the model only sees the sequence.",
    "The option D uses the general term 'alpha-1,6-mannosyltransferase activity' (GO:0000009) rather than the more specific GPI-specific term (GO:0120563), which is a valid parent term."
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
  "requested_accession": "A0A8C2M425",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "benchmark_sequence_length": 494,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-01-19",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "current_source_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "current_source_sequence_length": 494,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 19,
  "selected_historical_version": {
    "accession": "A0A8C2M425",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PIGV_CRIGR",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "selected_historical_source_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "selected_historical_source_sequence_length": 494,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A8C2M425\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-01-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Chinese hamster\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Cricetidae\",\"Cricetinae\",\"Cricetulus\"],\"scientificName\":\"Cricetulus griseus\",\"synonyms\":[\"Cricetulus barabensis griseus\"],\"taxonId\":10029}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"GPI mannosyltransferase II\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"GPI-MT-II\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"Phosphatidylinositol-glycan biosynthesis class V protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"PIG-V\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"GPI alpha-1,6-mannosyltransferase 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"value\":\"Alpha-1,6-mannosyltransferase that catalyzes the transfer of the second mannose, via an alpha-1,6 bond, from a dolichol-phosphate-mannose (Dol-P-Man) to a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H2) intermediate to generate a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) and participates in the seventh step of the glycosylphosphatidylinositol-anchor biosynthesis (PubMed:23694781). May also transfer the second mannose on a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H5), but less effectively (Probable)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:60489\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"name\":\"a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:60488\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19498\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19501\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58211\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:143818\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:144028\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:60993\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"name\":\"a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-[alpha-D-mannosyl-(1->6)-2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:60992\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19498\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19501\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58211\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:144036\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:144054\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0120563\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:Ensembl\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Hirata T.\",\"Fujita M.\",\"Kanzawa N.\",\"Murakami Y.\",\"Maeda Y.\",\"Kinoshita T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23694781\"},{\"database\":\"DOI\",\"id\":\"10.1093/jb/mvt045\"}],\"citationType\":\"journal article\",\"firstPage\":\"257\",\"id\":\"23694781\",\"journal\":\"J. Biochem.\",\"lastPage\":\"264\",\"publicationDate\":\"2013\",\"title\":\"Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-phosphate mannose availability.\",\"volume\":\"154\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "source_locator": "lines 1-17",
  "excerpt": "ID   PIGV_CRIGR              Reviewed;         494 AA.\nAC   A0A8C2M425;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-JAN-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=GPI alpha-1,6-mannosyltransferase 2 {ECO:0000250|UniProtKB:Q9NUD9};\nDE            EC=2.4.1.- {ECO:0000269|PubMed:23694781};\nDE   AltName: Full=GPI mannosyltransferase II;\nDE            Short=GPI-MT-II {ECO:0000250|UniProtKB:Q9NUD9};\nDE   AltName: Full=Phosphatidylinositol-glycan biosynthesis class V protein {ECO:0000250|UniProtKB:Q9NUD9};\nDE            Short=PIG-V {ECO:0000250|UniProtKB:Q9NUD9};\nGN   Name=PIGV {ECO:0000303|PubMed:23694781};\nOS   Cricetulus griseus (Chinese hamster) (Cricetulus barabensis griseus).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea;\nOC   Cricetidae; Cricetinae; Cricetulus.\nOX   NCBI_TaxID=10029;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "source_locator": "lines 28-35",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=23694781; DOI=10.1093/jb/mvt045;\nRA   Hirata T., Fujita M., Kanzawa N., Murakami Y., Maeda Y., Kinoshita T.;\nRT   \"Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting\nRT   enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-\nRT   phosphate mannose availability.\";\nRL   J. Biochem. 154:257-264(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "source_locator": "lines 36-48",
  "excerpt": "CC   -!- FUNCTION: Alpha-1,6-mannosyltransferase that catalyzes the transfer of\nCC       the second mannose, via an alpha-1,6 bond, from a dolichol-phosphate-\nCC       mannose (Dol-P-Man) to a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-\nCC       glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol\nCC       (also termed H2) intermediate to generate a 2-acyl-6-[alpha-D-mannosyl-\nCC       (1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-\nCC       sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) and participates\nCC       in the seventh step of the glycosylphosphatidylinositol-anchor\nCC       biosynthesis (PubMed:23694781). May also transfer the second mannose on\nCC       a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-\nCC       glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol\nCC       (also termed H5), but less effectively (Probable).\nCC       {ECO:0000269|PubMed:23694781, ECO:0000305|PubMed:23694781}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "source_locator": "lines 49-61",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-\nCC         (1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-\nCC         trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-\nCC         [alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-\nCC         glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol\nCC         + a di-trans,poly-cis-dolichyl phosphate + H(+);\nCC         Xref=Rhea:RHEA:60488, Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57683, ChEBI:CHEBI:58211,\nCC         ChEBI:CHEBI:143818, ChEBI:CHEBI:144028;\nCC         Evidence={ECO:0000269|PubMed:23694781};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:60489;\nCC         Evidence={ECO:0000269|PubMed:23694781};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "source_locator": "lines 62-74",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-\nCC         alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-\nCC         inositol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a\nCC         2-acyl-6-[alpha-D-mannosyl-(1->6)-2-phosphoethanolamine-alpha-D-\nCC         mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-\nCC         phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl phosphate +\nCC         H(+); Xref=Rhea:RHEA:60992, Rhea:RHEA-COMP:19498, Rhea:RHEA-\nCC         COMP:19501, ChEBI:CHEBI:15378, ChEBI:CHEBI:57683, ChEBI:CHEBI:58211,\nCC         ChEBI:CHEBI:144036, ChEBI:CHEBI:144054;\nCC         Evidence={ECO:0000305|PubMed:23694781};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:60993;\nCC         Evidence={ECO:0000305|PubMed:23694781};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "source_locator": "lines 107-107",
  "excerpt": "DR   GO; GO:0000009; F:alpha-1,6-mannosyltransferase activity; IEA:Ensembl.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "source_locator": "lines 108-108",
  "excerpt": "DR   GO; GO:0004376; F:GPI mannosyltransferase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
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
  "source_locator": "lines 117-125",
  "excerpt": "[Term]\nid: GO:0000009\nname: alpha-1,6-mannosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a mannose residue to an oligosaccharide, forming an alpha-(1->6) linkage.\" [GOC:mcc, PMID:2644248]\nsynonym: \"1,6-alpha-mannosyltransferase activity\" EXACT []\nxref: Reactome:R-HSA-449718 \"Addition of a third mannose to the N-glycan precursor by ALG2\"\nis_a: GO:0000030 ! mannosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0000009"
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
  "source_locator": "lines 87356-87384",
  "excerpt": "[Term]\nid: GO:0008753\nname: NADPH dehydrogenase (quinone) activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: NADPH + H+ + a quinone = NADP+ + a quinol.\" [RHEA:46164]\nsynonym: \"NADPH oxidase\" BROAD [EC:1.6.5.10]\nsynonym: \"NADPH:(quinone-acceptor) oxidoreductase\" RELATED [EC:1.6.5.10]\nsynonym: \"reduced nicotinamide adenine dinucleotide phosphate (quinone) dehydrogenase\" RELATED [EC:1.6.5.10]\nxref: EC:1.6.5.10\nxref: KEGG_REACTION:R07359\nxref: MetaCyc:RXN0-271\nxref: MetaCyc:RXN0-7385\nxref: RHEA:46164\nxref: RHEA:61980\nxref: RHEA:63492\nxref: RHEA:83239\nxref: RHEA:83247\nis_a: GO:0003955 ! NAD(P)H dehydrogenase (quinone) activity\nis_a: GO:0003959 ! NADPH dehydrogenase activity\nproperty_value: skos:exactMatch EC:1.6.5.10\nproperty_value: skos:exactMatch KEGG_REACTION:R07359\nproperty_value: skos:exactMatch MetaCyc:RXN0-7385\nproperty_value: skos:exactMatch RHEA:46164\nproperty_value: skos:narrowMatch MetaCyc:RXN0-271\nproperty_value: skos:narrowMatch RHEA:61980\nproperty_value: skos:narrowMatch RHEA:63492\nproperty_value: skos:narrowMatch RHEA:83239\nproperty_value: skos:narrowMatch RHEA:83247\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0008753"
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
  "source_locator": "lines 327906-327919",
  "excerpt": "[Term]\nid: GO:0051539\nname: 4 iron, 4 sulfur cluster binding\nnamespace: molecular_function\ndef: \"Binding to a 4 iron, 4 sulfur (4Fe-4S) cluster; this cluster consists of four iron atoms, with the inorganic sulfur atoms found between the irons and acting as bridging ligands.\" [GOC:ai, PMID:15952888, Wikipedia:Iron-sulfur_cluster]\nsynonym: \"4 Fe 4 S cluster binding\" EXACT []\nsynonym: \"4 iron, 4 sulphur cluster binding\" EXACT []\nsynonym: \"4Fe-4S cluster binding\" EXACT []\nsynonym: \"iron-sulfur cluster 4Fe-4S binding\" EXACT []\nsynonym: \"iron-sulphur cluster 4Fe-4S binding\" EXACT []\nsynonym: \"tetrairon tetrasulfide cluster binding\" EXACT []\nsynonym: \"tetrairon tetrasulphide cluster binding\" EXACT []\nis_a: GO:0051536 ! iron-sulfur cluster binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0051539"
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
  "source_locator": "lines 331451-331459",
  "excerpt": "[Term]\nid: GO:0051879\nname: Hsp90 protein binding\nnamespace: molecular_function\ndef: \"Binding to Hsp90 proteins, any of a group of heat shock proteins around 90kDa in size.\" [GOC:ai]\nsynonym: \"Hsp90 binding\" EXACT []\nsynonym: \"Hsp90 class protein binding\" EXACT []\nis_a: GO:0031072 ! heat shock protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0051879"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 436201-436210",
  "excerpt": "[Term]\nid: GO:0120563\nname: dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of an alpha-D-mannosyl residue from dolichol-P-mannose to Man(1)-GlcN-acyl-PI, forming an alpha-(1->6)-D-mannosyl-D-mannose linkage. This transfers the second mannose to the GPI precursor.\" [PMID:15623507]\nsynonym: \"glycosylphosphatidylinositol-mannosyltransferase II activity\" EXACT []\nsynonym: \"GPI-MT-II activity\" EXACT []\nis_a: GO:0000009 ! alpha-1,6-mannosyltransferase activity\nis_a: GO:0004376 ! GPI mannosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0120563"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
