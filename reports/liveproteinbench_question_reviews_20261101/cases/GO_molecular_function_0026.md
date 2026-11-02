# GO_molecular_function_0026

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — alpha-1,6-mannosyltransferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A8C2M425` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

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
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
"A0A8C2M425"
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"GPI mannosyltransferase II"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9NUD9","source":"UniProtKB"}],"value":"GPI-MT-II"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9NUD9","source":"UniProtKB"}],"value":"Phosphatidylinositol-glycan biosynthesis class V protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9NUD9","source":"UniProtKB"}],"value":"PIG-V"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23694781","source":"PubMed"}],"value":"2.4.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9NUD9","source":"UniProtKB"}],"value":"GPI alpha-1,6-mannosyltransferase 2"}}}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23694781","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"23694781","source":"PubMed"}],"value":"Alpha-1,6-mannosyltransferase that catalyzes the transfer of the second mannose, via an alpha-1,6 bond, from a dolichol-phosphate-mannose (Dol-P-Man) to a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H2) intermediate to generate a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) and participates in the seventh step of the glycosylphosphatidylinositol-anchor biosynthesis (PubMed:23694781). May also transfer the second mannose on a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H5), but less effectively (Probable)"}]}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"23694781","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:60489"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"23694781","source":"PubMed"}],"name":"a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:60488"},{"database":"Rhea","id":"RHEA-COMP:19498"},{"database":"Rhea","id":"RHEA-COMP:19501"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57683"},{"database":"ChEBI","id":"CHEBI:58211"},{"database":"ChEBI","id":"CHEBI:143818"},{"database":"ChEBI","id":"CHEBI:144028"}]}}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:57.236271+00:00.  

```json
{"database":"GO","id":"GO:0120563","properties":[{"key":"GoTerm","value":"F:dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity"},{"key":"GoEvidenceType","value":"IEA:Ensembl"}]}
```

Source SHA-256: `4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
ID   PIGV_CRIGR              Reviewed;         494 AA.
AC   A0A8C2M425;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   19-JAN-2022, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=GPI alpha-1,6-mannosyltransferase 2 {ECO:0000250|UniProtKB:Q9NUD9};
DE            EC=2.4.1.- {ECO:0000269|PubMed:23694781};
DE   AltName: Full=GPI mannosyltransferase II;
DE            Short=GPI-MT-II {ECO:0000250|UniProtKB:Q9NUD9};
DE   AltName: Full=Phosphatidylinositol-glycan biosynthesis class V protein {ECO:0000250|UniProtKB:Q9NUD9};
DE            Short=PIG-V {ECO:0000250|UniProtKB:Q9NUD9};
GN   Name=PIGV {ECO:0000303|PubMed:23694781};
OS   Cricetulus griseus (Chinese hamster) (Cricetulus barabensis griseus).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea;
OC   Cricetidae; Cricetinae; Cricetulus.
OX   NCBI_TaxID=10029;
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 36-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
CC   -!- FUNCTION: Alpha-1,6-mannosyltransferase that catalyzes the transfer of
CC       the second mannose, via an alpha-1,6 bond, from a dolichol-phosphate-
CC       mannose (Dol-P-Man) to a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-
CC       glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol
CC       (also termed H2) intermediate to generate a 2-acyl-6-[alpha-D-mannosyl-
CC       (1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-
CC       sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) and participates
CC       in the seventh step of the glycosylphosphatidylinositol-anchor
CC       biosynthesis (PubMed:23694781). May also transfer the second mannose on
CC       a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-
CC       glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol
CC       (also termed H5), but less effectively (Probable).
CC       {ECO:0000269|PubMed:23694781, ECO:0000305|PubMed:23694781}.
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 49-61`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-
CC         (1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-
CC         trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-
CC         [alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-
CC         glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol
CC         + a di-trans,poly-cis-dolichyl phosphate + H(+);
CC         Xref=Rhea:RHEA:60488, Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57683, ChEBI:CHEBI:58211,
CC         ChEBI:CHEBI:143818, ChEBI:CHEBI:144028;
CC         Evidence={ECO:0000269|PubMed:23694781};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:60489;
CC         Evidence={ECO:0000269|PubMed:23694781};
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)  
**Locator:** `lines 107-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:26:00.136470+00:00.  

```text
DR   GO; GO:0000009; F:alpha-1,6-mannosyltransferase activity; IEA:Ensembl.
```

Source SHA-256: `3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 117-125`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000009
name: alpha-1,6-mannosyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of a mannose residue to an oligosaccharide, forming an alpha-(1->6) linkage." [GOC:mcc, PMID:2644248]
synonym: "1,6-alpha-mannosyltransferase activity" EXACT []
xref: Reactome:R-HSA-449718 "Addition of a third mannose to the N-glycan precursor by ALG2"
is_a: GO:0000030 ! mannosyltransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 436201-436210`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0120563
name: dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity
namespace: molecular_function
def: "Catalysis of the transfer of an alpha-D-mannosyl residue from dolichol-P-mannose to Man(1)-GlcN-acyl-PI, forming an alpha-(1->6)-D-mannosyl-D-mannose linkage. This transfers the second mannose to the GPI precursor." [PMID:15623507]
synonym: "glycosylphosphatidylinositol-mannosyltransferase II activity" EXACT []
synonym: "GPI-MT-II activity" EXACT []
is_a: GO:0000009 ! alpha-1,6-mannosyltransferase activity
is_a: GO:0004376 ! GPI mannosyltransferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
