# GO_molecular_function_0108

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — sequence-specific DNA binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNEALDDIDRILVRELAADGRATLSELATRAGLSVSAVQSRVRRLESRGVVQGYSARINPEAVGHLLSAFVAITPLDPSQPDDAPARLEHIEEVESCYSVAGEESYVLLVRVASARALEDLLQRIRTTANVRTRSTIILNTFYSDRQHIP

[Multiple Choices]
A. hydrolase activity
B. nicotinamide phosphoribosyltransferase activity
C. sequence-specific DNA binding
D. tau protein binding
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

> The exact sequence match is annotated as sequence-specific DNA binding (C6); the annotation is IBA, a computational inference. Separately, the entry’s function statement says the protein directly binds target-gene promoter regions and cites experimental evidence (C5).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 150-residue bacterial sequence has a compact, strongly helical N-terminal region with basic residues, consistent with a helix-turn-helix DNA-binding region in a small bacterial regulator. It also lacks an evident catalytic signature; the much more specific enzyme option and tau-protein binding are less plausible.


**Missing item-specific fact**

> No particular database annotation is essential to make the choice, although identifying the protein family confidently would benefit from sequence-homology or domain evidence not supplied explicitly.


**Reason**

> The sequence offers a defensible regulator/HTH-based argument that distinguishes DNA binding from the listed alternatives, though it is an inference rather than proof of the exact molecular function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Sequence-specific DNA binding is the only option with a plausible fit to the sequence’s compact bacterial regulator-like architecture; the alternatives are not comparably supported.


### Important caveats

- The GO sequence-specific DNA-binding annotation cited here is IBA, not itself direct experimental evidence.
- The experimental support cited in the entry concerns direct promoter binding and transcriptional regulation; the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 150-residue bacterial sequence has a compact, strongly helical N-terminal region with basic residues, consistent with a helix-turn-helix DNA-binding region in a small bacterial regulator. It also lacks an evident catalytic signature; the much more specific enzyme option and tau-protein binding are less plausible.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No particular database annotation is essential to make the choice, although identifying the protein family confidently would benefit from sequence-homology or domain evidence not supplied explicitly.",
    "reason": "The sequence offers a defensible regulator/HTH-based argument that distinguishes DNA binding from the listed alternatives, though it is an inference rather than proof of the exact molecular function."
  },
  "case_id": "GO_molecular_function_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as sequence-specific DNA binding (C6); the annotation is IBA, a computational inference. Separately, the entry’s function statement says the protein directly binds target-gene promoter regions and cites experimental evidence (C5)."
  },
  "important_caveats": [
    "The GO sequence-specific DNA-binding annotation cited here is IBA, not itself direct experimental evidence.",
    "The experimental support cited in the entry concerns direct promoter binding and transcriptional regulation; the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Sequence-specific DNA binding is the only option with a plausible fit to the sequence’s compact bacterial regulator-like architecture; the alternatives are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as sequence-specific DNA binding (C6); the annotation is IBA, a computational inference. Separately, the entry’s function statement says the protein directly binds target-gene promoter regions and cites experimental evidence (C5).",
    "evidence_ids": ["C1", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 150-residue bacterial sequence has a compact, strongly helical N-terminal region with basic residues, consistent with a helix-turn-helix DNA-binding region in a small bacterial regulator. It also lacks an evident catalytic signature; the much more specific enzyme option and tau-protein binding are less plausible.",
    "missing_item_specific_fact": "No particular database annotation is essential to make the choice, although identifying the protein family confidently would benefit from sequence-homology or domain evidence not supplied explicitly.",
    "reason": "The sequence offers a defensible regulator/HTH-based argument that distinguishes DNA binding from the listed alternatives, though it is an inference rather than proof of the exact molecular function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Sequence-specific DNA binding is the only option with a plausible fit to the sequence’s compact bacterial regulator-like architecture; the alternatives are not comparably supported."
  },
  "important_caveats": [
    "The GO sequence-specific DNA-binding annotation cited here is IBA, not itself direct experimental evidence.",
    "The experimental support cited in the entry concerns direct promoter binding and transcriptional regulation; the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is UniProt I6YBQ3 (LRPA_MYCTU), an HTH-type transcriptional regulator LrpA from Mycobacterium tuberculosis. The FUNCTION comment (ECO:0000269, direct assay evidence from PubMed:18042675, 18930129, 26789099) states it 'Acts by binding directly to the promoter region of the target genes.' Multiple crystal structures (PDB: 2IVM, 2VBW–2VC1, 2QZ8) confirm the DNA-binding HTH domain. The GO annotation GO:0043565 (sequence-specific DNA binding) is present, though with IBA:GO_Central (inferred by biological aspect). The direct experimental evidence from crystal structures and DNA-binding assays supports the expected answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [C10](#evidence-c10), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 150-aa protein lacks any recognizable catalytic motifs (no Ser-His-Asp triad, no metalloprotease motifs, no transferase signatures), which argues against hydrolase (A) and nicotinamide phosphoribosyltransferase (B). The amino acid composition (high Ala, Glu, Arg, Leu; absence of eukaryotic-specific features) is consistent with a bacterial protein, making tau protein binding (D, a eukaryotic neuronal interaction) implausible. The C-terminal region ('RLEHIEEVESCYSVAGEESYVLLVRVASARALEDLLQRIRTTANVRTRSTIILNTFYSDRQHIP') exhibits the characteristic spacing of hydrophobic helical segments with basic residues (Arg, Glu) positioned for nucleic-acid contact, consistent with a helix-turn-helix (HTH) DNA-binding domain found in small bacterial transcriptional regulators. The small size (150 aa) is typical of DNA-binding regulatory proteins rather than enzymes.


**Missing item-specific fact**

> Definitive confirmation that this specific 150-aa sequence is LrpA (Rv3291c) requires database lookup. However, the elimination of alternatives through general biological reasoning (no catalytic motifs, bacterial context excludes tau binding, HTH-like helical architecture) provides meaningful grounds to select C without exact sequence identification.


**Reason**

> General biological knowledge allows meaningful discrimination: (1) absence of catalytic motifs eliminates hydrolase and transferase; (2) bacterial amino-acid composition makes eukaryotic tau binding implausible; (3) the small size and helical architecture with basic residues are consistent with a DNA-binding transcriptional regulator. While precise HTH motif identification from sequence alone is non-trivial, the elimination approach provides defensible grounds for selecting C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors are well-separated: hydrolase and nicotinamide phosphoribosyltransferase require specific catalytic motifs absent from the sequence; tau protein binding is a eukaryotic-specific interaction implausible for a bacterial protein. Only C is consistent with the observed sequence features.


### Important caveats

- The GO:0043565 annotation uses evidence code IBA:GO_Central (computational inference by biological aspect), not direct experimental annotation. However, the FUNCTION comment and crystal structures provide direct experimental support for DNA binding.
- Identifying the HTH motif purely from a 150-aa sequence without secondary-structure prediction tools is non-trivial; the reasoning relies on elimination of alternatives and general architectural expectations rather than definitive motif recognition.
- The sequence-match is confirmed (SHA256 match between benchmark and UniProt entry I6YBQ3, sequence version 1, 150 aa).
- The author source snapshot is unknown; the historical entry version 79 (2026-01-28) already contains the relevant annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 150-aa protein lacks any recognizable catalytic motifs (no Ser-His-Asp triad, no metalloprotease motifs, no transferase signatures), which argues against hydrolase (A) and nicotinamide phosphoribosyltransferase (B). The amino acid composition (high Ala, Glu, Arg, Leu; absence of eukaryotic-specific features) is consistent with a bacterial protein, making tau protein binding (D, a eukaryotic neuronal interaction) implausible. The C-terminal region ('RLEHIEEVESCYSVAGEESYVLLVRVASARALEDLLQRIRTTANVRTRSTIILNTFYSDRQHIP') exhibits the characteristic spacing of hydrophobic helical segments with basic residues (Arg, Glu) positioned for nucleic-acid contact, consistent with a helix-turn-helix (HTH) DNA-binding domain found in small bacterial transcriptional regulators. The small size (150 aa) is typical of DNA-binding regulatory proteins rather than enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Definitive confirmation that this specific 150-aa sequence is LrpA (Rv3291c) requires database lookup. However, the elimination of alternatives through general biological reasoning (no catalytic motifs, bacterial context excludes tau binding, HTH-like helical architecture) provides meaningful grounds to select C without exact sequence identification.",
    "reason": "General biological knowledge allows meaningful discrimination: (1) absence of catalytic motifs eliminates hydrolase and transferase; (2) bacterial amino-acid composition makes eukaryotic tau binding implausible; (3) the small size and helical architecture with basic residues are consistent with a DNA-binding transcriptional regulator. While precise HTH motif identification from sequence alone is non-trivial, the elimination approach provides defensible grounds for selecting C."
  },
  "case_id": "GO_molecular_function_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "C10",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The protein is UniProt I6YBQ3 (LRPA_MYCTU), an HTH-type transcriptional regulator LrpA from Mycobacterium tuberculosis. The FUNCTION comment (ECO:0000269, direct assay evidence from PubMed:18042675, 18930129, 26789099) states it 'Acts by binding directly to the promoter region of the target genes.' Multiple crystal structures (PDB: 2IVM, 2VBW–2VC1, 2QZ8) confirm the DNA-binding HTH domain. The GO annotation GO:0043565 (sequence-specific DNA binding) is present, though with IBA:GO_Central (inferred by biological aspect). The direct experimental evidence from crystal structures and DNA-binding assays supports the expected answer."
  },
  "important_caveats": [
    "The GO:0043565 annotation uses evidence code IBA:GO_Central (computational inference by biological aspect), not direct experimental annotation. However, the FUNCTION comment and crystal structures provide direct experimental support for DNA binding.",
    "Identifying the HTH motif purely from a 150-aa sequence without secondary-structure prediction tools is non-trivial; the reasoning relies on elimination of alternatives and general architectural expectations rather than definitive motif recognition.",
    "The sequence-match is confirmed (SHA256 match between benchmark and UniProt entry I6YBQ3, sequence version 1, 150 aa).",
    "The author source snapshot is unknown; the historical entry version 79 (2026-01-28) already contains the relevant annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors are well-separated: hydrolase and nicotinamide phosphoribosyltransferase require specific catalytic motifs absent from the sequence; tau protein binding is a eukaryotic-specific interaction implausible for a bacterial protein. Only C is consistent with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is UniProt I6YBQ3 (LRPA_MYCTU), an HTH-type transcriptional regulator LrpA from Mycobacterium tuberculosis. The FUNCTION comment (ECO:0000269, direct assay evidence from PubMed:18042675, 18930129, 26789099) states it 'Acts by binding directly to the promoter region of the target genes.' Multiple crystal structures (PDB: 2IVM, 2VBW–2VC1, 2QZ8) confirm the DNA-binding HTH domain. The GO annotation GO:0043565 (sequence-specific DNA binding) is present, though with IBA:GO_Central (inferred by biological aspect). The direct experimental evidence from crystal structures and DNA-binding assays supports the expected answer.",
    "evidence_ids": ["C4", "C5", "C6", "C9", "C10", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 150-aa protein lacks any recognizable catalytic motifs (no Ser-His-Asp triad, no metalloprotease motifs, no transferase signatures), which argues against hydrolase (A) and nicotinamide phosphoribosyltransferase (B). The amino acid composition (high Ala, Glu, Arg, Leu; absence of eukaryotic-specific features) is consistent with a bacterial protein, making tau protein binding (D, a eukaryotic neuronal interaction) implausible. The C-terminal region ('RLEHIEEVESCYSVAGEESYVLLVRVASARALEDLLQRIRTTANVRTRSTIILNTFYSDRQHIP') exhibits the characteristic spacing of hydrophobic helical segments with basic residues (Arg, Glu) positioned for nucleic-acid contact, consistent with a helix-turn-helix (HTH) DNA-binding domain found in small bacterial transcriptional regulators. The small size (150 aa) is typical of DNA-binding regulatory proteins rather than enzymes.",
    "missing_item_specific_fact": "Definitive confirmation that this specific 150-aa sequence is LrpA (Rv3291c) requires database lookup. However, the elimination of alternatives through general biological reasoning (no catalytic motifs, bacterial context excludes tau binding, HTH-like helical architecture) provides meaningful grounds to select C without exact sequence identification.",
    "reason": "General biological knowledge allows meaningful discrimination: (1) absence of catalytic motifs eliminates hydrolase and transferase; (2) bacterial amino-acid composition makes eukaryotic tau binding implausible; (3) the small size and helical architecture with basic residues are consistent with a DNA-binding transcriptional regulator. While precise HTH motif identification from sequence alone is non-trivial, the elimination approach provides defensible grounds for selecting C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors are well-separated: hydrolase and nicotinamide phosphoribosyltransferase require specific catalytic motifs absent from the sequence; tau protein binding is a eukaryotic-specific interaction implausible for a bacterial protein. Only C is consistent with the observed sequence features."
  },
  "important_caveats": [
    "The GO:0043565 annotation uses evidence code IBA:GO_Central (computational inference by biological aspect), not direct experimental annotation. However, the FUNCTION comment and crystal structures provide direct experimental support for DNA binding.",
    "Identifying the HTH motif purely from a 150-aa sequence without secondary-structure prediction tools is non-trivial; the reasoning relies on elimination of alternatives and general architectural expectations rather than definitive motif recognition.",
    "The sequence-match is confirmed (SHA256 match between benchmark and UniProt entry I6YBQ3, sequence version 1, 150 aa).",
    "The author source snapshot is unknown; the historical entry version 79 (2026-01-28) already contains the relevant annotations."
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

**Accession:** `I6YBQ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 79. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I6YBQ3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.289633+00:00.  

```json
"I6YBQ3"
```

Source SHA-256: `3978e04c41379d89d9a497b2d685cf726895877f193db390290b68c748badf35`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I6YBQ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.289633+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17962306","source":"PubMed"}],"value":"Feast/famine regulatory protein Rv3291c"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17962306","source":"PubMed"}],"value":"MtbLrp"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26789099","source":"PubMed"}],"value":"MtbLrpA"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HTH-type transcriptional regulator LrpA"}}}
```

Source SHA-256: `3978e04c41379d89d9a497b2d685cf726895877f193db390290b68c748badf35`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I6YBQ3.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.289633+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18042675","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"18930129","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26789099","source":"PubMed"}],"value":"Transcriptional regulator that probably plays an important role in M.tuberculosis persistence (PubMed:18042675, PubMed:18930129, PubMed:26789099). Regulates the expression of several genes, including lat, rsmG, whiB2, lsr2 and Rv2011c (PubMed:18042675, PubMed:26789099). Acts by binding directly to the promoter region of the target genes (PubMed:18042675, PubMed:26789099)"}]}
```

Source SHA-256: `3978e04c41379d89d9a497b2d685cf726895877f193db390290b68c748badf35`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I6YBQ3.json)  
**Locator:** `/uniProtKBCrossReferences/43`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.289633+00:00.  

```json
{"database":"GO","id":"GO:0043565","properties":[{"key":"GoTerm","value":"F:sequence-specific DNA binding"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `3978e04c41379d89d9a497b2d685cf726895877f193db390290b68c748badf35`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I6YBQ3.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.289633+00:00.  

```json
{"citation":{"authors":["Shrivastava T.","Ramachandran R."],"citationCrossReferences":[{"database":"PubMed","id":"17962306"},{"database":"DOI","id":"10.1093/nar/gkm850"}],"citationType":"journal article","firstPage":"7324","id":"17962306","journal":"Nucleic Acids Res.","lastPage":"7335","publicationDate":"2007","title":"Mechanistic insights from the crystal structures of a feast/famine regulatory protein from Mycobacterium tuberculosis H37Rv.","volume":"35"},"evidences":[{"evidenceCode":"ECO:0007744","id":"2IVM","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VBW","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VBX","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VBY","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VBZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VC0","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VC1","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"H37Rv"}],"referenceNumber":7,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) OF APOPROTEIN AND IN COMPLEXES WITH HISTIDINE; LEUCINE; METHIONINE; PHENYLALANINE; TRYPTOPHAN AND TYROSINE","ACTIVITY REGULATION","SUBUNIT","DOMAIN"]}
```

Source SHA-256: `3978e04c41379d89d9a497b2d685cf726895877f193db390290b68c748badf35`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I6YBQ3.json)  
**Locator:** `/references/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.289633+00:00.  

```json
{"citation":{"authors":["Reddy M.C.","Gokulan K.","Jacobs W.R.","Ioerger T.R.","Sacchettini J.C."],"citationCrossReferences":[{"database":"PubMed","id":"18042675"},{"database":"DOI","id":"10.1110/ps.073192208"}],"citationType":"journal article","firstPage":"159","id":"18042675","journal":"Protein Sci.","lastPage":"170","publicationDate":"2008","title":"Crystal structure of Mycobacterium tuberculosis LrpA, a leucine-responsive global regulator associated with starvation response.","volume":"17"},"evidences":[{"evidenceCode":"ECO:0007744","id":"2QZ8","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"H37Rv"}],"referenceNumber":8,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.16 ANGSTROMS) OF 5-150 OF MUTANT MET-108","FUNCTION","DNA-BINDING","ACTIVITY REGULATION","SUBUNIT","DOMAIN"]}
```

Source SHA-256: `3978e04c41379d89d9a497b2d685cf726895877f193db390290b68c748badf35`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I6YBQ3?format=txt&versions=79)  
**Locator:** `lines 104-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:11.636802+00:00.  

```text
CC   -!- FUNCTION: Transcriptional regulator that probably plays an important
CC       role in M.tuberculosis persistence (PubMed:18042675, PubMed:18930129,
CC       PubMed:26789099). Regulates the expression of several genes, including
CC       lat, rsmG, whiB2, lsr2 and Rv2011c (PubMed:18042675, PubMed:26789099).
CC       Acts by binding directly to the promoter region of the target genes
CC       (PubMed:18042675, PubMed:26789099). {ECO:0000269|PubMed:18042675,
CC       ECO:0000269|PubMed:18930129, ECO:0000269|PubMed:26789099}.
```

Source SHA-256: `0d8bb5d3f126c254cc07f1a917b843bb272ed6b3990eb34e792e13bcb3ee45b0`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I6YBQ3?format=txt&versions=79)  
**Locator:** `lines 194-194`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:11.636802+00:00.  

```text
DR   GO; GO:0043565; F:sequence-specific DNA binding; IBA:GO_Central.
```

Source SHA-256: `0d8bb5d3f126c254cc07f1a917b843bb272ed6b3990eb34e792e13bcb3ee45b0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
