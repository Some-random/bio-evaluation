# GO_molecular_function_0022

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — ubiquitin-protein transferase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPVILNFSSERVLSESELEALRHVGRVSQSEQLVVRGRTMRLHHISFMDSFSVEPVSGGLLDRLSARGHRLLAENLEIQLNRGHTFLQAFRLYMEQSRATPCTRQNVSSAIQNKINSHAFTVSHQDFSCHEQHLNCPITLCIPETGVFVRNAKNSEICSLYDHNALTELIRRNAPHPLSREPFVPEMIVSKDECHFNLIEQYFCILATQNICTRI

[Multiple Choices]
A. phosphopantothenoylcysteine decarboxylase activity
B. amidophosphoribosyltransferase activity
C. nucleic acid binding
D. ubiquitin-protein transferase activity
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

> The supplied sequence exactly matches the recorded 215-aa E. coli O157:H7 NleG8 protein. Its UniProt entry identifies it as an E3 ubiquitin-protein ligase and records experimental evidence for ubiquitin transfer activity, supporting choice D. The evidence is an annotation citing a publication, not an independently reviewed primary-paper result here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a sufficiently specific, general biological argument to identify this particular protein’s ubiquitin-transfer activity. The alternatives name distinct functions, but recognizing which one applies requires protein-specific functional knowledge.


**Missing item-specific fact**

> That this sequence is NleG8, an E3 ubiquitin-protein ligase with experimentally supported ubiquitin-transfer activity.


**Reason**

> The sequence is the only biological input, and no organism or protein annotation is given. The decisive NleG8 identity and its experimental functional characterization are external, item-specific facts; reviewer-only database evidence cannot make the question reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched functional evidence supports D, and the listed alternatives describe different activities. No competing option is comparably supported by the supplied evidence.


### Important caveats

- The exact author source snapshot is unknown, although the sequence matches both the current and checked historical UniProt records.
- The reviewer-only experimental evidence supports the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific, general biological argument to identify this particular protein’s ubiquitin-transfer activity. The alternatives name distinct functions, but recognizing which one applies requires protein-specific functional knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence is NleG8, an E3 ubiquitin-protein ligase with experimentally supported ubiquitin-transfer activity.",
    "reason": "The sequence is the only biological input, and no organism or protein annotation is given. The decisive NleG8 identity and its experimental functional characterization are external, item-specific facts; reviewer-only database evidence cannot make the question reasoning-supported."
  },
  "case_id": "GO_molecular_function_0022",
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
    "reason": "The supplied sequence exactly matches the recorded 215-aa E. coli O157:H7 NleG8 protein. Its UniProt entry identifies it as an E3 ubiquitin-protein ligase and records experimental evidence for ubiquitin transfer activity, supporting choice D. The evidence is an annotation citing a publication, not an independently reviewed primary-paper result here."
  },
  "important_caveats": [
    "The exact author source snapshot is unknown, although the sequence matches both the current and checked historical UniProt records.",
    "The reviewer-only experimental evidence supports the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched functional evidence supports D, and the listed alternatives describe different activities. No competing option is comparably supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the recorded 215-aa E. coli O157:H7 NleG8 protein. Its UniProt entry identifies it as an E3 ubiquitin-protein ligase and records experimental evidence for ubiquitin transfer activity, supporting choice D. The evidence is an annotation citing a publication, not an independently reviewed primary-paper result here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific, general biological argument to identify this particular protein’s ubiquitin-transfer activity. The alternatives name distinct functions, but recognizing which one applies requires protein-specific functional knowledge.",
    "missing_item_specific_fact": "That this sequence is NleG8, an E3 ubiquitin-protein ligase with experimentally supported ubiquitin-transfer activity.",
    "reason": "The sequence is the only biological input, and no organism or protein annotation is given. The decisive NleG8 identity and its experimental functional characterization are external, item-specific facts; reviewer-only database evidence cannot make the question reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched functional evidence supports D, and the listed alternatives describe different activities. No competing option is comparably supported by the supplied evidence."
  },
  "important_caveats": [
    "The exact author source snapshot is unknown, although the sequence matches both the current and checked historical UniProt records.",
    "The reviewer-only experimental evidence supports the key but was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8XAN6 (NleG8, E. coli O157:H7) is annotated as 'E3 ubiquitin-protein ligase NleG' with EC 2.3.2.27, supported by experimental evidence (ECO:0000269, PubMed:36511702). The GO annotation GO:0061630 (ubiquitin protein ligase activity) is is_a GO:0004842 (ubiquitin-protein transferase activity), which matches option D exactly. The catalytic activity reaction (C6/H4) confirms ubiquitin transferase function. Sequence match is confirmed (SHA256 identical, 215 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO4](#evidence-go4), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the 215-aa sequence contains a compact cysteine-rich motif (…DECHFNLIEQYFCILATQNICTRI) with Cys residues spaced at intervals consistent with a U-box domain (a modified RING-finger fold). U-box domains are well-established structural hallmarks of E3 ubiquitin-protein ligases. The small protein size (~215 aa), bacterial origin, and absence of catalytic residues characteristic of phosphopantothenoylcysteine decarboxylase (FMN-dependent decarboxylase) or amidophosphoribosyltransferase (large glutamine amidotransferase) further disfavor options A and B. Option C (nucleic acid binding) lacks any recognizable DNA/RNA-binding motif (e.g., helix-turn-helix, zinc finger with specific spacing, or arginine-rich patch). Thus, the Cys-rich C-terminal signature pointing to a U-box/E3 ligase fold provides a concrete structural-biology argument distinguishing D.


**Missing item-specific fact**

> Precise confirmation that this specific Cys pattern is a bona fide U-box (rather than a generic Cys-rich or zinc-binding motif) would benefit from the crystal structure (PDB 6XNJ, residues 206–215 in complex with GOPC), but the sequence-level Cys spacing is a legitimate and commonly used heuristic in structural biology.


**Reason**

> A biologist examining the sequence can note the C-terminal cysteine-rich compact region, recognize it as consistent with a U-box/RING-like fold, and connect that fold to E3 ubiquitin ligase activity. The other options require specific catalytic architectures (FMN-binding pocket for PPCDC, glutamine amidotransferase domain for PRPP amidotransferase) that are absent from the sequence. This constitutes a defensible biological reasoning chain, though U-box recognition from raw sequence is non-trivial and benefits from structural-biology expertise.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C (nucleic acid binding) is extremely broad but no recognizable nucleic-acid-binding motif is present. Options A and B require specific enzymatic active-site architectures not evident in the sequence. The Cys-rich C-terminal region uniquely points toward D among the four choices.


### Important caveats

- The UniProt entry was first publicly released 2025-06-18; the benchmark's exact author source snapshot is unknown. However, the sequence version 1 dates to 2002-03-01 and is unchanged, so the sequence itself was available long before the functional annotation.
- The GO annotation evidence code is EXP (experimental, PubMed:36511702, 2023), meaning the E3 ligase activity was established experimentally, not merely by computational inference.
- U-box domain identification from sequence alone is a heuristic; the definitive confirmation came from X-ray crystallography (PDB 6XNJ, residues 206–215). A model relying solely on sequence would be applying a well-known but imperfect structural motif prediction.
- The reviewer-only evidence was absent from the evaluated model input; the model must rely on the raw sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the 215-aa sequence contains a compact cysteine-rich motif (…DECHFNLIEQYFCILATQNICTRI) with Cys residues spaced at intervals consistent with a U-box domain (a modified RING-finger fold). U-box domains are well-established structural hallmarks of E3 ubiquitin-protein ligases. The small protein size (~215 aa), bacterial origin, and absence of catalytic residues characteristic of phosphopantothenoylcysteine decarboxylase (FMN-dependent decarboxylase) or amidophosphoribosyltransferase (large glutamine amidotransferase) further disfavor options A and B. Option C (nucleic acid binding) lacks any recognizable DNA/RNA-binding motif (e.g., helix-turn-helix, zinc finger with specific spacing, or arginine-rich patch). Thus, the Cys-rich C-terminal signature pointing to a U-box/E3 ligase fold provides a concrete structural-biology argument distinguishing D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise confirmation that this specific Cys pattern is a bona fide U-box (rather than a generic Cys-rich or zinc-binding motif) would benefit from the crystal structure (PDB 6XNJ, residues 206–215 in complex with GOPC), but the sequence-level Cys spacing is a legitimate and commonly used heuristic in structural biology.",
    "reason": "A biologist examining the sequence can note the C-terminal cysteine-rich compact region, recognize it as consistent with a U-box/RING-like fold, and connect that fold to E3 ubiquitin ligase activity. The other options require specific catalytic architectures (FMN-binding pocket for PPCDC, glutamine amidotransferase domain for PRPP amidotransferase) that are absent from the sequence. This constitutes a defensible biological reasoning chain, though U-box recognition from raw sequence is non-trivial and benefits from structural-biology expertise."
  },
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "H5",
      "GO4",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8XAN6 (NleG8, E. coli O157:H7) is annotated as 'E3 ubiquitin-protein ligase NleG' with EC 2.3.2.27, supported by experimental evidence (ECO:0000269, PubMed:36511702). The GO annotation GO:0061630 (ubiquitin protein ligase activity) is is_a GO:0004842 (ubiquitin-protein transferase activity), which matches option D exactly. The catalytic activity reaction (C6/H4) confirms ubiquitin transferase function. Sequence match is confirmed (SHA256 identical, 215 aa)."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released 2025-06-18; the benchmark's exact author source snapshot is unknown. However, the sequence version 1 dates to 2002-03-01 and is unchanged, so the sequence itself was available long before the functional annotation.",
    "The GO annotation evidence code is EXP (experimental, PubMed:36511702, 2023), meaning the E3 ligase activity was established experimentally, not merely by computational inference.",
    "U-box domain identification from sequence alone is a heuristic; the definitive confirmation came from X-ray crystallography (PDB 6XNJ, residues 206–215). A model relying solely on sequence would be applying a well-known but imperfect structural motif prediction.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on the raw sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (nucleic acid binding) is extremely broad but no recognizable nucleic-acid-binding motif is present. Options A and B require specific enzymatic active-site architectures not evident in the sequence. The Cys-rich C-terminal region uniquely points toward D among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8XAN6 (NleG8, E. coli O157:H7) is annotated as 'E3 ubiquitin-protein ligase NleG' with EC 2.3.2.27, supported by experimental evidence (ECO:0000269, PubMed:36511702). The GO annotation GO:0061630 (ubiquitin protein ligase activity) is is_a GO:0004842 (ubiquitin-protein transferase activity), which matches option D exactly. The catalytic activity reaction (C6/H4) confirms ubiquitin transferase function. Sequence match is confirmed (SHA256 identical, 215 aa).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4", "H5", "GO4", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the 215-aa sequence contains a compact cysteine-rich motif (…DECHFNLIEQYFCILATQNICTRI) with Cys residues spaced at intervals consistent with a U-box domain (a modified RING-finger fold). U-box domains are well-established structural hallmarks of E3 ubiquitin-protein ligases. The small protein size (~215 aa), bacterial origin, and absence of catalytic residues characteristic of phosphopantothenoylcysteine decarboxylase (FMN-dependent decarboxylase) or amidophosphoribosyltransferase (large glutamine amidotransferase) further disfavor options A and B. Option C (nucleic acid binding) lacks any recognizable DNA/RNA-binding motif (e.g., helix-turn-helix, zinc finger with specific spacing, or arginine-rich patch). Thus, the Cys-rich C-terminal signature pointing to a U-box/E3 ligase fold provides a concrete structural-biology argument distinguishing D.",
    "missing_item_specific_fact": "Precise confirmation that this specific Cys pattern is a bona fide U-box (rather than a generic Cys-rich or zinc-binding motif) would benefit from the crystal structure (PDB 6XNJ, residues 206–215 in complex with GOPC), but the sequence-level Cys spacing is a legitimate and commonly used heuristic in structural biology.",
    "reason": "A biologist examining the sequence can note the C-terminal cysteine-rich compact region, recognize it as consistent with a U-box/RING-like fold, and connect that fold to E3 ubiquitin ligase activity. The other options require specific catalytic architectures (FMN-binding pocket for PPCDC, glutamine amidotransferase domain for PRPP amidotransferase) that are absent from the sequence. This constitutes a defensible biological reasoning chain, though U-box recognition from raw sequence is non-trivial and benefits from structural-biology expertise."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (nucleic acid binding) is extremely broad but no recognizable nucleic-acid-binding motif is present. Options A and B require specific enzymatic active-site architectures not evident in the sequence. The Cys-rich C-terminal region uniquely points toward D among the four choices."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released 2025-06-18; the benchmark's exact author source snapshot is unknown. However, the sequence version 1 dates to 2002-03-01 and is unchanged, so the sequence itself was available long before the functional annotation.",
    "The GO annotation evidence code is EXP (experimental, PubMed:36511702, 2023), meaning the E3 ligase activity was established experimentally, not merely by computational inference.",
    "U-box domain identification from sequence alone is a heuristic; the definitive confirmation came from X-ray crystallography (PDB 6XNJ, residues 206–215). A model relying solely on sequence would be applying a well-known but imperfect structural motif prediction.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely on the raw sequence and general biological knowledge."
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

**Accession:** `Q8XAN6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 129. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.588356+00:00.  

```json
"Q8XAN6"
```

Source SHA-256: `791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.588356+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36511702","source":"PubMed"}],"value":"2.3.2.27"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"E3 ubiquitin-protein ligase NleG"}}}
```

Source SHA-256: `791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.588356+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36511702","source":"PubMed"}],"value":"Effector proteins function to alter host cell physiology and promote bacterial survival in host tissues. This protein is an E3 ubiquitin-protein ligase that probably interferes with the host's ubiquitination pathway and targets host proteins for proteasomal degradation. Can ubiquitinate ubiquitin, giving rise to polyubiquitin chains (in vitro) (PubMed:36511702). Does not complement an nleG8 deletion in C.rodentium (PubMed:36511702)"}]}
```

Source SHA-256: `791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.588356+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.3.2.27","evidences":[{"evidenceCode":"ECO:0000269","id":"36511702","source":"PubMed"}],"name":"S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine."}}
```

Source SHA-256: `791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.588356+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"36511702","source":"PubMed"}],"id":"GO:0061630","properties":[{"key":"GoTerm","value":"F:ubiquitin protein ligase activity"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 129 / 1.  
**Retrieved:** 2026-11-01T06:28:42.292045+00:00.  

```text
ID   NLEG8_ECO57             Reviewed;         215 AA.
AC   Q8XAN6; A0A0H3JIV3; A0A6M0JK84; Q7AEM3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAR-2002, sequence version 1.
DT   28-JAN-2026, entry version 129.
DE   RecName: Full=E3 ubiquitin-protein ligase NleG {ECO:0000305};
DE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};
GN   Name=nleG8 {ECO:0000303|PubMed:36511702};
GN   Synonyms=nleG {ECO:0000312|EMBL:BAB35247.1};
GN   ORFNames=ECs_1824 {ECO:0000312|EMBL:BAB35247.1};
OS   Escherichia coli O157:H7.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Enterobacteriaceae; Escherichia.
OX   NCBI_TaxID=83334;
```

Source SHA-256: `6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)  
**Locator:** `lines 42-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 129 / 1.  
**Retrieved:** 2026-11-01T06:28:42.292045+00:00.  

```text
CC   -!- FUNCTION: Effector proteins function to alter host cell physiology and
CC       promote bacterial survival in host tissues. This protein is an E3
CC       ubiquitin-protein ligase that probably interferes with the host's
CC       ubiquitination pathway and targets host proteins for proteasomal
CC       degradation. Can ubiquitinate ubiquitin, giving rise to polyubiquitin
CC       chains (in vitro) (PubMed:36511702). Does not complement an nleG8
CC       deletion in C.rodentium (PubMed:36511702).
CC       {ECO:0000269|PubMed:36511702}.
```

Source SHA-256: `6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)  
**Locator:** `lines 50-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 129 / 1.  
**Retrieved:** 2026-11-01T06:28:42.292045+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine +
CC         [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-
CC         cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.;
CC         EC=2.3.2.27; Evidence={ECO:0000269|PubMed:36511702};
```

Source SHA-256: `6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)  
**Locator:** `lines 86-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 129 / 1.  
**Retrieved:** 2026-11-01T06:28:42.292045+00:00.  

```text
DR   GO; GO:0061630; F:ubiquitin protein ligase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 51005-51151`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004842
name: ubiquitin-protein transferase activity
namespace: molecular_function
alt_id: GO:0004840
alt_id: GO:0004841
def: "Catalysis of the transfer of ubiquitin from one protein to another via the reaction X-Ub + Y = Y-Ub + X, where both X-Ub and Y-Ub are covalent linkages." [GOC:BioGRID, GOC:jh2, PMID:9635407]
synonym: "E2" BROAD []
synonym: "E3" BROAD []
synonym: "ubiquitin conjugating enzyme activity" NARROW []
synonym: "ubiquitin ligase activity" NARROW []
synonym: "ubiquitin protein ligase activity" NARROW []
synonym: "ubiquitin protein-ligase activity" NARROW []
synonym: "ubiquitin-conjugating enzyme activity" NARROW []
xref: KEGG_REACTION:R03876
xref: Reactome:R-HSA-1234163 "Cytosolic VBC complex ubiquitinylates hydroxyprolyl-HIF-alpha"
xref: Reactome:R-HSA-1234172 "Nuclear VBC complex ubiquitinylates HIF-alpha"
xref: Reactome:R-HSA-1253282 "ERBB4 ubiquitination by WWP1/ITCH"
xref: Reactome:R-HSA-1358789 "Self-ubiquitination of RNF41"
xref: Reactome:R-HSA-1358790 "RNF41 ubiquitinates ERBB3"
xref: Reactome:R-HSA-1358792 "RNF41 ubiquitinates activated ERBB3"
xref: Reactome:R-HSA-1363331 "Ubiquitination of p130 (RBL2) by SCF (Skp2)"
xref: Reactome:R-HSA-168915 "K63-linked ubiquitination of RIP1 bound to the activated TLR complex"
xref: Reactome:R-HSA-173542 "SMURF2 ubiquitinates SMAD2"
xref: Reactome:R-HSA-173545 "Ubiquitin-dependent degradation of the SMAD complex terminates TGF-beta signaling"
xref: Reactome:R-HSA-174057 "Multiubiquitination of APC/C-associated Cdh1"
xref: Reactome:R-HSA-174104 "Ubiquitination of Cyclin A by APC/C:Cdc20 complex"
xref: Reactome:R-HSA-174144 "Ubiquitination of Securin by phospho-APC/C:Cdc20 complex"
xref: Reactome:R-HSA-174159 "Ubiquitination of Emi1 by SCF-beta-TrCP"
xref: Reactome:R-HSA-174195 "Ubiquitination of cell cycle proteins targeted by the APC/C:Cdh1complex"
xref: Reactome:R-HSA-174227 "Ubiquitination of Cyclin B by phospho-APC/C:Cdc20 complex"
xref: Reactome:R-HSA-179417 "Multiubiquitination of Nek2A"
xref: Reactome:R-HSA-180540 "Multi-ubiquitination of APOBEC3G"
xref: Reactome:R-HSA-180597 "Ubiquitination of CD4 by Vpu:CD4:beta-TrCP:SKP1 complex"
xref: Reactome:R-HSA-182986 "CBL-mediated ubiquitination of CIN85"
xref: Reactome:R-HSA-182993 "Ubiquitination of stimulated EGFR (CBL)"
xref: Reactome:R-HSA-183051 "CBL ubiquitinates Sprouty"
xref: Reactome:R-HSA-183084 "CBL escapes CDC42-mediated inhibition by down-regulating the adaptor molecule Beta-Pix"
xref: Reactome:R-HSA-183089 "CBL binds and ubiquitinates phosphorylated Sprouty"
xref: Reactome:R-HSA-1852623 "Ubiquitination of NICD1 by FBWX7"
xref: Reactome:R-HSA-187575 "Ubiquitination of phospho-p27/p21"
xref: Reactome:R-HSA-1912357 "ITCH ubiquitinates DTX"
xref: Reactome:R-HSA-1912386 "Ubiquitination of NOTCH1 by ITCH in the absence of ligand"
xref: Reactome:R-HSA-1918092 "CHIP (STUB1) mediates ubiquitination of ERBB2"
xref: Reactome:R-HSA-1918095 "CUL5 mediates ubiquitination of ERBB2"
xref: Reactome:R-HSA-1977296 "NEDD4 ubiquitinates ERBB4jmAcyt1s80 dimer"
xref: Reactome:R-HSA-1980074 "Ubiquitination of DLL/JAG ligands upon binding to NOTCH1"
xref: Reactome:R-HSA-1980118 "ARRB mediates NOTCH1 ubiquitination"
xref: Reactome:R-HSA-201425 "Ubiquitin-dependent degradation of the Smad complex terminates BMP2 signalling"
xref: Reactome:R-HSA-202453 "Auto-ubiquitination of TRAF6"
xref: Reactome:R-HSA-202534 "Ubiquitination of NEMO by TRAF6"
xref: Reactome:R-HSA-205118 "TRAF6 polyubiquitinates NRIF"
xref: Reactome:R-HSA-209063 "Beta-TrCP ubiquitinates NFKB p50:p65:phospho IKBA complex"
xref: Reactome:R-HSA-211734 "Ubiquitination of PAK-2p34"
xref: Reactome:R-HSA-2169050 "SMURFs/NEDD4L ubiquitinate phosphorylated TGFBR1 and SMAD7"
xref: Reactome:R-HSA-2172172 "Ubiquitination of DLL/JAG ligands upon binding to NOTCH2"
xref: Reactome:R-HSA-2179276 "SMURF2 monoubiquitinates SMAD3"
xref: Reactome:R-HSA-2186747 "Ubiquitination of SKI/SKIL by RNF111/SMURF2"
xref: Reactome:R-HSA-2186785 "RNF111 ubiquitinates SMAD7"
xref: Reactome:R-HSA-2187368 "STUB1 (CHIP) ubiquitinates SMAD3"
xref: Reactome:R-HSA-2213017 "Auto-ubiquitination of TRAF3"
xref: Reactome:R-HSA-264444 "Autoubiquitination of phospho-COP1(Ser-387 )"
xref: Reactome:R-HSA-2682349 "RAF1:SGK:TSC22D3:WPP ubiquitinates SCNN channels"
xref: Reactome:R-HSA-2730904 "Auto-ubiquitination of TRAF6"
xref: Reactome:R-HSA-2737728 "Ubiquitination of DLL/JAG ligands upon binding to NOTCH1 HD domain mutants"
xref: Reactome:R-HSA-2769007 "Ubiquitination of DLL/JAG ligands upon binding to NOTCH1 PEST domain mutants"
xref: Reactome:R-HSA-2900765 "Ubiquitination of DLL/JAG ligands upon binding to NOTCH1 HD+PEST domain mutants"
xref: Reactome:R-HSA-3000335 "SCF-beta-TrCp1/2 ubiquitinates phosphorylated BORA"
xref: Reactome:R-HSA-3134804 "STING ubiquitination by TRIM32 or TRIM56"
xref: Reactome:R-HSA-3134946 "DDX41 ubiquitination by TRIM21"
xref: Reactome:R-HSA-3249386 "DTX4 ubiquitinates p-S172-TBK1 within NLRP4:DTX4:dsDNA:ZBP1:TBK1"
xref: Reactome:R-HSA-3780995 "NHLRC1 mediated ubiquitination of EPM2A (laforin) and PPP1RC3 (PTG) associated with glycogen-GYG2"
xref: Reactome:R-HSA-3781009 "NHLRC1 mediated ubiquitination of EPM2A and PPP1RC3 associated with glycogen-GYG1"
xref: Reactome:R-HSA-3788724 "Cdh1:APC/C ubiquitinates EHMT1 and EHMT2"
xref: Reactome:R-HSA-3797226 "Defective NHLRC1 does not ubiquitinate EPM2A (laforin) and PPP1R3C (PTG) (type 2B disease)"
xref: Reactome:R-HSA-4332236 "CBL neddylates TGFBR2"
xref: Reactome:R-HSA-446877 "TRAF6 is K63 poly-ubiquitinated"
xref: Reactome:R-HSA-450358 "Activated TRAF6 synthesizes unanchored polyubiquitin chains upon TLR stimulation"
xref: Reactome:R-HSA-451418 "Pellino ubiquitinates IRAK1"
xref: Reactome:R-HSA-5357757 "BIRC(cIAP1/2) ubiquitinates RIPK1"
xref: Reactome:R-HSA-5362412 "SYVN1 ubiquitinates Hh C-terminal fragments"
xref: Reactome:R-HSA-5483238 "Hh processing variants are ubiquitinated"
xref: Reactome:R-HSA-5607725 "SCF-beta-TRCP ubiquitinates p-7S-p100:RELB in active NIK:p-176,S180-IKKA dimer:p-7S-p100:SCF-beta-TRCP"
xref: Reactome:R-HSA-5607728 "beta-TRCP ubiquitinates IkB-alpha in p-S32,33-IkB-alpha:NF-kB complex"
xref: Reactome:R-HSA-5607756 "TRAF6 oligomer autoubiquitinates"
xref: Reactome:R-HSA-5607757 "K63polyUb-TRAF6 ubiquitinates TAK1"
xref: Reactome:R-HSA-5610742 "SCF(beta-TrCP) ubiquitinates p-GLI1"
xref: Reactome:R-HSA-5610745 "SCF(beta-TrCP) ubiquitinates p-GLI2"
xref: Reactome:R-HSA-5610746 "SCF(beta-TrCP) ubiquitinates p-GLI3"
xref: Reactome:R-HSA-5652009 "RAD18:UBE2B or RBX1:CUL4:DDB1:DTL monoubiquitinates PCNA"
xref: Reactome:R-HSA-5655170 "RCHY1 monoubiquitinates POLH"
xref: Reactome:R-HSA-5660753 "SIAH1:UBE2L6:Ubiquitin ubiquitinates SNCA"
xref: Reactome:R-HSA-5667107 "SIAH1, SIAH2 ubiquitinate SNCAIP"
xref: Reactome:R-HSA-5667111 "PARK2 K63-Ubiquitinates SNCAIP"
xref: Reactome:R-HSA-5668454 "K63polyUb-cIAP1,2 ubiquitinates TRAF3"
xref: Reactome:R-HSA-5668534 "cIAP1,2 ubiquitinates NIK in cIAP1,2:TRAF2::TRAF3:NIK"
xref: Reactome:R-HSA-5675470 "BIRC2/3 (cIAP1/2) is autoubiquitinated"
xref: Reactome:R-HSA-5684250 "SCF betaTrCP ubiquitinates NFKB p105 within p-S927, S932-NFkB p105:TPL2:ABIN2"
xref: Reactome:R-HSA-5691108 "SKP1:FBXL5:CUL1:NEDD8 ubiquitinylates IREB2"
xref: Reactome:R-HSA-5693108 "TNFAIP3 (A20) ubiquitinates RIPK1 with K48-linked Ub chains"
xref: Reactome:R-HSA-68712 "The geminin component of geminin:Cdt1 complexes is ubiquitinated, releasing Cdt1"
xref: Reactome:R-HSA-69598 "Ubiquitination of phosphorylated CDC25A"
xref: Reactome:R-HSA-741386 "RIP2 induces K63-linked ubiquitination of NEMO"
xref: Reactome:R-HSA-75824 "Ubiquitination of Cyclin D1"
xref: Reactome:R-HSA-870449 "TRIM33 monoubiquitinates SMAD4"
xref: Reactome:R-HSA-8948709 "DTX4 ubiquitinates p-S172-TBK1 within NLRP4:DTX4:STING:TBK1:IRF3"
xref: Reactome:R-HSA-8956106 "VHL:EloB,C:NEDD8-CUL2:RBX1 complex ubiquitinylates HIF-alpha"
xref: Reactome:R-HSA-9013069 "Ubiquitination of DLL/JAG ligands upon binding to NOTCH3"
xref: Reactome:R-HSA-9013974 "Auto-ubiquitination of TRAF3 within activated TLR3 complex"
xref: Reactome:R-HSA-9014342 "K63-linked ubiquitination of RIP1 bound to the activated TLR complex"
xref: Reactome:R-HSA-918224 "DDX58 is K63 polyubiquitinated"
xref: Reactome:R-HSA-936412 "RNF125 mediated ubiquitination of DDX58, IFIH1 and MAVS"
xref: Reactome:R-HSA-936942 "Auto ubiquitination of oligo-TRAF6 bound to p-IRAK2"
xref: Reactome:R-HSA-936986 "Activated TRAF6 synthesizes unanchored polyubiquitin chains"
xref: Reactome:R-HSA-9628444 "Activated TRAF6 synthesizes unanchored polyubiquitin chains upon TLR3 stimulation"
xref: Reactome:R-HSA-9645394 "Activated TRAF6 synthesizes unanchored polyubiquitin chains upon ALPK1:ADP-heptose stimulation"
xref: Reactome:R-HSA-9645414 "Auto ubiquitination of TRAF6 bound to ALPK1:ADP-heptose:TIFA oligomer"
xref: Reactome:R-HSA-9688831 "STUB1 ubiquitinates RIPK3 at K55, K363"
xref: Reactome:R-HSA-9701000 "BRCA1:BARD1 heterodimer autoubiquitinates"
xref: Reactome:R-HSA-9750946 "TRAF2,6 ubiquitinates NLRC5"
xref: Reactome:R-HSA-975118 "TRAF6 ubiquitinqtes IRF7 within the activated TLR7/8 or 9 complex"
xref: Reactome:R-HSA-975147 "Auto ubiquitination of oligo-TRAF6 bound to p-IRAK2 at endosome membrane"
xref: Reactome:R-HSA-9758604 "Ubiquitination of IKBKG by TRAF6"
xref: Reactome:R-HSA-9766227 "MDM2 mediates CDH1 ubiquitination"
xref: Reactome:R-HSA-9793444 "ITCH polyubiquitinates MLKL at K50"
xref: Reactome:R-HSA-9793485 "PRKN polyubiquitinates RIPK3"
xref: Reactome:R-HSA-9793679 "LUBAC ubiquitinates RIPK1 at K627"
xref: Reactome:R-HSA-9796346 "MIB2 ubiquitinates RIPK1 at K377, K604, K634"
xref: Reactome:R-HSA-9796387 "STUB1 ubiquitinates RIPK1 at K571, K604, K627"
xref: Reactome:R-HSA-9796626 "MIB2 ubiquitinates CFLAR"
xref: Reactome:R-HSA-9815507 "MIB2 ubiquitinates CYLD at K338, K530"
xref: Reactome:R-HSA-9817362 "SPATA2:CYLD-bound LUBAC ubiquitinates RIPK1 at K627 within the TNFR1 signaling complex"
xref: Reactome:R-HSA-983140 "Transfer of Ub from E2 to substrate and release of E2"
xref: Reactome:R-HSA-983153 "E1 mediated ubiquitin activation"
xref: Reactome:R-HSA-983156 "Polyubiquitination of substrate"
xref: Reactome:R-HSA-9833155 "Ubiquitination of STAT2"
xref: Reactome:R-HSA-9834070 "PRKN ubiquitinates MOM substrates"
xref: Reactome:R-HSA-9861563 "CTLH E3 ligase ubiquitinates LDHA"
xref: Reactome:R-HSA-9861640 "CTLH E3 ligase ubiquitinates PKM-1"
xref: Reactome:R-HSA-9929350 "Ubiquitination of CD274 by BTRC-SCF E3-ligase complex"
xref: Reactome:R-HSA-9934753 "CBLL1 ubiquitinates CDH1"
xref: Reactome:R-HSA-9948301 "ZNF598 K63 polyubiquitinates RPS10 (eS10) and RPS20 (uS10) of the 40S ribosomal subunit"
xref: Reactome:R-HSA-9954721 "NEDD8-K699-CUL2:ELOB:ELOC:RBX1:KLHDC10 K48 polyubiquitinates alanine-tailed nascent peptide"
xref: Reactome:R-HSA-9955146 "S.flexneri ipaH9.8 ubiquitinates GBPs"
xref: Reactome:R-HSA-9970191 "RBBP6 activates CPSF complex"
is_a: GO:0019787 ! ubiquitin-like protein transferase activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 358126-358254`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0061630
name: ubiquitin protein ligase activity
namespace: molecular_function
alt_id: GO:0090302
alt_id: GO:0090622
alt_id: GO:1904264
alt_id: GO:1904822
def: "Catalysis of the transfer of ubiquitin to a substrate protein via the reaction X-ubiquitin + S = X + S-ubiquitin, where X is either an E2 or E3 enzyme, the X-ubiquitin linkage is a thioester bond, and the S-ubiquitin linkage is an amide bond: an isopeptide bond between the C-terminal glycine of ubiquitin and the epsilon-amino group of lysine residues in the substrate or, in the linear extension of ubiquitin chains, a peptide bond the between the C-terminal glycine and N-terminal methionine of ubiquitin residues." [GOC:BioGRID, GOC:dph, GOC:mah, GOC:tb, PMID:22863777]
comment: This enzyme catalyzes a transferase reaction.
synonym: "E3" BROAD [GOC:dph]
synonym: "ER-associated E3 ligase" RELATED [PMID:24019521]
synonym: "protein ubiquitination activity" EXACT [GOC:dph]
synonym: "ubiquitin ligase activity" EXACT [GOC:dph]
xref: EC:2.3.2.26
xref: EC:2.3.2.27
xref: EC:2.3.2.31
xref: EC:2.3.2.33
xref: EC:2.3.2.36
xref: Reactome:R-HSA-1225956 "Inefficient ubiquitination of ligand-responsive p-6Y-EGFR mutants by p-Y371-CBL"
xref: Reactome:R-HSA-1504190 "DVL is ubiquitinated by CUL3:KLHL12:RBX1"
xref: Reactome:R-HSA-183036 "Ubiquitination of stimulated EGFR (CBL:GRB2)"
xref: Reactome:R-HSA-201445 "Ubiquitin-dependent degradation controls basal levels of R-Smad1/5/8"
xref: Reactome:R-HSA-3322429 "XIAP monoubiquinates TLE"
xref: Reactome:R-HSA-3640861 "RNF146 ubiquitinates ADP-ribosylated AXIN"
xref: Reactome:R-HSA-4608852 "SMURF1/2 ubiquitinates PRICKLE1"
xref: Reactome:R-HSA-4641129 "AXIN is ubiquitinated by SMURF2"
xref: Reactome:R-HSA-4641159 "DVL1 is ubiquitinated by HECW1"
xref: Reactome:R-HSA-4641246 "ZNRF3 autoubiquitinates to promote its internalization"
xref: Reactome:R-HSA-4641253 "ZNRF3 ubiquitinates FZD to promote its downregulation"
xref: Reactome:R-HSA-5246693 "APC is K63-polyubiquitinated"
xref: Reactome:R-HSA-5610737 "NUMB:ITCH bind and ubiquitnate GLI1"
xref: Reactome:R-HSA-5632648 "SMURF1/2 ubiquitinates PTCH1"
xref: Reactome:R-HSA-5635856 "SPOP:CUL3:RBX1 ubiquitinates GLI2,3"
xref: Reactome:R-HSA-5635864 "NUMB:ITCH ubiquitinates GLI1"
xref: Reactome:R-HSA-5654672 "CBL ubiquitinates FRS2 and FGFR1"
xref: Reactome:R-HSA-5654677 "CBL ubiquitinates FRS2 and FGFR2"
xref: Reactome:R-HSA-5654679 "CBL ubiquitinates FRS2 and FGFR3"
xref: Reactome:R-HSA-5654684 "CBL ubiquitinates FRS2 and FGFR4"
xref: Reactome:R-HSA-5658424 "KBTBD7:CUL3:RBX1 ubiquitinates NF1"
xref: Reactome:R-HSA-5674022 "BRAP autoubiquitinates"
xref: Reactome:R-HSA-5682858 "RNF8 and RNF168 ubiquitinate H2AFX"
xref: Reactome:R-HSA-5684071 "RNF4 ubiquitinates MDC1"
xref: Reactome:R-HSA-5687081 "MAPK6 is ubiquitinated at the N-terminal"
xref: Reactome:R-HSA-5689111 "PARK2 autoubiquitinates"
xref: Reactome:R-HSA-5690827 "TNFAIP3 (A20) ubiquitinates RIPK1"
xref: Reactome:R-HSA-6781867 "ERCC8:DDB1:CUL4:RBX1 ubiquitinates ERCC6 and RNA Pol II"
xref: Reactome:R-HSA-6782943 "UV-DDB ubiquitinates XPC"
xref: Reactome:R-HSA-6785361 "Monoubiquitination of FANCD2:FANCI"
xref: Reactome:R-HSA-6790487 "RNF111 ubiquitinates SUMOylated XPC"
xref: Reactome:R-HSA-6798373 "MDM2 ubiquitinates DYRK2"
xref: Reactome:R-HSA-6804253 "MDM2 ubiquitinates JMY"
xref: Reactome:R-HSA-6804441 "RNF34 or RFFL ubiquitinates phosphorylated TP53"
xref: Reactome:R-HSA-6804724 "MDM2 ubiquitinates phosphorylated MDM4"
xref: Reactome:R-HSA-6804879 "MDM2 ubiquitinates TP53"
xref: Reactome:R-HSA-6804942 "MDM2 homodimers auto-ubiquitinate"
xref: Reactome:R-HSA-6807106 "PTEN undergoes monoubiquitination"
xref: Reactome:R-HSA-6807134 "NEDD4, WWP2, CHIP and XIAP polyubiquitinate PTEN"
xref: Reactome:R-HSA-68946 "Phosphorylated Orc1 is ubiquitinated while still associated with chromatin"
xref: Reactome:R-HSA-69015 "Cytoplasmic phosphorylated Cdc6 is ubiquitinated by the anaphase-promoting complex"
xref: Reactome:R-HSA-8848829 "CBL autoubiquitinates"
xref: Reactome:R-HSA-8851011 "TRIM27 polyubiquitinates PTEN"
xref: Reactome:R-HSA-8854041 "SCF-FBXL7 ubiquitinates AURKA"
xref: Reactome:R-HSA-8854051 "SCF-FBXL18 ubiquitinates FBXL7"
xref: Reactome:R-HSA-8854628 "MYLIP dimer ubiquitinates VLDLR on Lys-839"
xref: Reactome:R-HSA-8866546 "RNF5 and RNF185 ubiquitinate misfolded CFTR"
xref: Reactome:R-HSA-8866856 "RNF5 and RNF185 ubiquitinate CFTR F508del"
xref: Reactome:R-HSA-8867288 "OS9:SEL1:ERAD E3 ligase:DERL2 ubiquitinates unfolded protein:(GlcNAc)2 (Man)9-5"
xref: Reactome:R-HSA-8875183 "CBL monoubiquitinates activated MET"
xref: Reactome:R-HSA-8875431 "LRIG1 undergoes ubiquitination"
xref: Reactome:R-HSA-8876258 "CBL monoubiquitinates InlB-bound MET"
xref: Reactome:R-HSA-8877003 "CBLL1 ubiqutinates the InlA-bound CDH1 complex"
xref: Reactome:R-HSA-8938773 "RNF144A polyubiquitinates PRKDC"
xref: Reactome:R-HSA-8938815 "RNF152 polyubiquitinates RRAGA"
xref: Reactome:R-HSA-8939335 "RNF181 polyubiquinates BCL10"
xref: Reactome:R-HSA-8939706 "SCF(SKP2) polyubiquitinates RUNX2"
xref: Reactome:R-HSA-8942101 "RNF20:RNF40 monoubiquitinates Histone H2B"
xref: Reactome:R-HSA-8943003 "SHPRH polyubiquitinates monoubiquitinated PCNA"
xref: Reactome:R-HSA-8943040 "HLTF polyubiquitinates monoubiquitinated PCNA"
xref: Reactome:R-HSA-8943080 "TMEM129 polyubiquitinates HLA (MHC class I heavy chain) bound to cytomegalovirus US11"
xref: Reactome:R-HSA-8948775 "MKRN1 polyubiquitinates PTEN"
xref: Reactome:R-HSA-8948832 "RNF146 polyubiquitinates PARylated PTEN"
xref: Reactome:R-HSA-8952382 "MDM2 polyubiquitinates RUNX3"
xref: Reactome:R-HSA-8952419 "SMURFs ubiquitinate RUNX3"
xref: Reactome:R-HSA-8953946 "PEX2:PEX10:PEX12 monoubiquitinates PEX5S,L at cysteine-11"
xref: Reactome:R-HSA-8956026 "CUL9:RBX1 ubiquitinates BIRC5"
xref: Reactome:R-HSA-8956684 "ITCH polyubiquitinates TP73"
xref: Reactome:R-HSA-9008076 "WWP1 polyubiquitinates RUNX2"
xref: Reactome:R-HSA-9009308 "STUB1 polyubiquitinates RUNX2"
xref: Reactome:R-HSA-9009403 "SMURF1 polyubiquitinates RUNX2"
xref: Reactome:R-HSA-9011300 "ZSWIM8 ubiquitinates ROBO3.1"
xref: Reactome:R-HSA-9021523 "WWP2 ubiquitinates NOTCH3"
xref: Reactome:R-HSA-9033485 "PEX2:PEX10:PEX12 monoubiquitinates PEX5L at cysteine-11"
xref: Reactome:R-HSA-934604 "Phosphorylated SPRY2 is ubiquitinated by CBL"
xref: Reactome:R-HSA-936462 "PIN1 mediated IRF3 degradation"
xref: Reactome:R-HSA-936475 "Negative regulation of DDX58/IFIH1 signaling by RNF216"
xref: Reactome:R-HSA-9604629 "FBXW7 promotes ubiquitination of p-NICD4"
xref: Reactome:R-HSA-9685195 "SARS-CoV-1 9b recruits ITCH to MAVS"
xref: Reactome:R-HSA-9686920 "PELI1 ubiquitinates RIPK3 at K363"
xref: Reactome:R-HSA-9686969 "APC/C:Cdh1 polyubiquitinates SKP2"
xref: Reactome:R-HSA-9705738 "SOCS1,3 ubiquitinates CSF3R in SOCS1,3:p-4Y-CSF3R:CSF3 dimer:LYN:p-Y-JAK1:p-JAK2:p-SYK:p-HCK:p-TYK2:CUL5:ELOB:ELOC:RNF7"
xref: Reactome:R-HSA-9706354 "Ubiquitination of FLT3"
xref: Reactome:R-HSA-9706356 "CBL mutants don't ubiquitinate FLT3"
xref: Reactome:R-HSA-9708517 "FBXL17 ubiquitinates BACH1 (in BACH1:FBXL17:SCF (SKP2))"
xref: Reactome:R-HSA-9733316 "p-Y-CBL autoubiquitinates and multiubiquitinates p-Y561-CSF1R in CSF1 dimer:p-Y561-CSF1R dimer:p-Y-CBL"
xref: Reactome:R-HSA-9755304 "MUL1 ubiquitinates UBXN7"
xref: Reactome:R-HSA-9755505 "KEAP1:NEDD8-CUL3:RBX1 complex ubiquitinates NFE2L2"
xref: Reactome:R-HSA-9759154 "TRIM21 ubiquitinates SQSTM1"
xref: Reactome:R-HSA-9759172 "KEAP1:CUL3:RBX1 ubiquitinates p-S349 SQSTM1 oligomer"
xref: Reactome:R-HSA-9762091 "NFE2L2 is ubiquitinated by BTRC:SKP1:CUL1:RBX1"
xref: Reactome:R-HSA-9766645 "CUL3:RBX1 ubiquitinates KEAP1"
xref: Reactome:R-HSA-990526 "Recruitment of ITCH and K48 ubiquitination of MAVS"
xref: Reactome:R-HSA-9929490 "CD274 ubiquitination by SPOP:CUL3:RBX1 complex"
xref: Reactome:R-HSA-9931298 "Ubiquitination of CD274 by ERAD complex"
xref: Reactome:R-HSA-9931430 "MIB2-mediated K63-ubiquitination of CD274"
xref: Reactome:R-HSA-9932510 "BTRC:CUL1:SKP1:RBX1 (SCF-beta-TrCP1) ubiquitinylates phosphorylated PER1,2,3"
xref: Reactome:R-HSA-9932512 "FBXL3:CUL1:SKP1:RBX1 ubiquitinylates phosphorylated CRY1,2"
xref: Reactome:R-HSA-9945766 "NS3 is ubiquitinated"
xref: Reactome:R-HSA-9946390 "NS1 dimer is ubiquitinated"
xref: Reactome:R-HSA-9948362 "LTN1 K48 polyubiquitinates the nascent peptide in NEMF:60S ribosomal subunit:peptidyl-tRNA with nascent peptide"
xref: Reactome:R-HSA-9954737 "RCHY1 K48 polyubiquitinates alanine-tailed nascent peptide"
is_a: GO:0004842 ! ubiquitin-protein transferase activity
is_a: GO:0061659 ! ubiquitin-like protein ligase activity
property_value: skos:narrowMatch EC:2.3.2.26
property_value: skos:narrowMatch EC:2.3.2.27
property_value: skos:narrowMatch EC:2.3.2.31
property_value: skos:narrowMatch EC:2.3.2.33
property_value: skos:narrowMatch EC:2.3.2.36

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
