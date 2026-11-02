# GO_cellular_component_0177

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — endoplasmic reticulum

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMKINLYKLLCFICVIFLLHKNVVRSGDNMKYNDMKGLDDLSKLNDDQVKDILGLKIDGAKERIEKLFHLIDKNNDKEITEEELNTWSSFLKNEIFLKQVQAEMGQIDSDKDGFISLNELNDAFAQNLDAKEVEKHSEGLLKRFQIVDKDKDGKLSINEVGLLIDPMKDEELKELEINEILEHHDVNKDGKISLDEFKQTRSDESSGVKKDDEMALDDFNFFDANKDGFIDKEEIIKVYFDPAHESGAINVNEIKENIFEGKKITYDLWNEKALKIAVTSLTDYGDVIRYPEDFKLDIGKNVILPTARSRAFEDDDMDADNTEDDKDEADDASQQKSPAIDEL

[Multiple Choices]
A. heterotrimeric G-protein complex
B. endoplasmic reticulum
C. extracellular region
D. microtubule associated complex
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches the Plasmodium falciparum protein whose UniProt annotation places it in the endoplasmic reticulum. The annotation cites experimental evidence, including GO:0005783 with IDA evidence and multiple cited localization studies.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with entry into the secretory pathway, making ER localization plausible. But that signal alone does not distinguish an ER-resident protein from one ultimately localized extracellularly.


**Missing item-specific fact**

> Whether this particular protein is retained in the ER rather than secreted, as established by its protein-specific localization evidence.


**Reason**

> The sequence offers a broad secretory-pathway clue, but the choice between ER and extracellular region depends on item-specific localization evidence not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> From the sequence alone, the N-terminal hydrophobic region supports secretory-pathway targeting but does not resolve ER residence versus extracellular localization. The reviewer-only evidence supports B.


### Important caveats

- The sequence match establishes that the cited annotations concern this sequence; it does not mean those annotations were available to the evaluated model.
- The evidence includes database annotation and cited experimental localization evidence; the primary papers were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with entry into the secretory pathway, making ER localization plausible. But that signal alone does not distinguish an ER-resident protein from one ultimately localized extracellularly.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular protein is retained in the ER rather than secreted, as established by its protein-specific localization evidence.",
    "reason": "The sequence offers a broad secretory-pathway clue, but the choice between ER and extracellular region depends on item-specific localization evidence not supplied in the question."
  },
  "case_id": "GO_cellular_component_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium falciparum protein whose UniProt annotation places it in the endoplasmic reticulum. The annotation cites experimental evidence, including GO:0005783 with IDA evidence and multiple cited localization studies."
  },
  "important_caveats": [
    "The sequence match establishes that the cited annotations concern this sequence; it does not mean those annotations were available to the evaluated model.",
    "The evidence includes database annotation and cited experimental localization evidence; the primary papers were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "From the sequence alone, the N-terminal hydrophobic region supports secretory-pathway targeting but does not resolve ER residence versus extracellular localization. The reviewer-only evidence supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium falciparum protein whose UniProt annotation places it in the endoplasmic reticulum. The annotation cites experimental evidence, including GO:0005783 with IDA evidence and multiple cited localization studies.",
    "evidence_ids": ["C5", "C6", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with entry into the secretory pathway, making ER localization plausible. But that signal alone does not distinguish an ER-resident protein from one ultimately localized extracellularly.",
    "missing_item_specific_fact": "Whether this particular protein is retained in the ER rather than secreted, as established by its protein-specific localization evidence.",
    "reason": "The sequence offers a broad secretory-pathway clue, but the choice between ER and extracellular region depends on item-specific localization evidence not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "From the sequence alone, the N-terminal hydrophobic region supports secretory-pathway targeting but does not resolve ER residence versus extracellular localization. The reviewer-only evidence supports B."
  },
  "important_caveats": [
    "The sequence match establishes that the cited annotations concern this sequence; it does not mean those annotations were available to the evaluated model.",
    "The evidence includes database annotation and cited experimental localization evidence; the primary papers were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IIR7 (PFERC_PLAF7) is annotated as 'Endoplasmic reticulum-resident calcium binding protein' (PfERC) with subcellular location 'Endoplasmic reticulum' supported by four independent experimental studies (PubMed:9364972, 9497061, 23061985, 32098818), all with ECO:0000269 (direct assay) evidence. GO:0005783 (endoplasmic reticulum) is annotated with IDA:GeneDB evidence. The sequence matches the canonical entry exactly (SHA-256 match confirmed in both current and historical snapshots).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch (MMKINLYKLLCFICVIFLLHKNV) is recognizable as a signal peptide, directing the protein into the secretory pathway (ER). Multiple EF-hand calcium-binding motifs (repeated DxxxD...E...D...K patterns) and highly acidic character are identifiable. This narrows the plausible options to B (ER) or C (extracellular region), since both involve the secretory pathway. However, the mature sequence lacks a canonical KDEL/HDEL ER-retention signal and lacks a transmembrane domain, so the default sequence-based prediction from a signal peptide alone would favor secretion (C) over ER residency (B). Distinguishing ER-resident from secreted requires knowing this specific protein belongs to the CREC family of ER calcium-binding proteins, which is protein-specific knowledge not derivable from general sequence heuristics.


**Missing item-specific fact**

> The absence of a visible ER-retention signal (KDEL/HDEL) in the C-terminus of this precursor sequence means that experimental determination (immunofluorescence, subcellular fractionation, mass spectrometry of ER fractions) was required to establish ER residency rather than secretion. The CREC-family membership and ER-residency of PfERC is a protein-specific fact established by direct assay in four publications.


**Reason**

> While the signal peptide and EF-hand motifs provide general biological grounds to eliminate options A (no GTPase/helical-bundle G-protein motifs) and D (no tubulin-binding motifs), the critical distinction between B (endoplasmic reticulum) and C (extracellular region) cannot be resolved from the sequence alone. A signal peptide without a retention signal typically predicts secretion. The actual ER residency was established experimentally and is not inferable from general biological reasoning about the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Given a signal peptide directing into the secretory pathway but no visible ER-retention motif (KDEL/HDEL) and no transmembrane anchor, both 'endoplasmic reticulum' and 'extracellular region' are plausible predictions from sequence alone. The default prediction for a soluble protein with a signal peptide and no retention signal would be secretion (C). The correct answer (B) depends on protein-specific experimental knowledge.


### Important caveats

- The UniProt entry flags the protein as a 'Precursor,' meaning the mature form may differ from the supplied sequence; the retention signal (if any) may be in a region not obvious in the full precursor.
- The EF-hand motifs are identifiable by general knowledge, but the CREC-family ER-residency classification is a specific annotation not derivable from sequence heuristics alone.
- All supporting evidence is experimental (ECO:0000269, direct assay) from four independent publications, providing strong confidence in the annotation.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q8IIR7, validating that annotations apply to this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MMKINLYKLLCFICVIFLLHKNV) is recognizable as a signal peptide, directing the protein into the secretory pathway (ER). Multiple EF-hand calcium-binding motifs (repeated DxxxD...E...D...K patterns) and highly acidic character are identifiable. This narrows the plausible options to B (ER) or C (extracellular region), since both involve the secretory pathway. However, the mature sequence lacks a canonical KDEL/HDEL ER-retention signal and lacks a transmembrane domain, so the default sequence-based prediction from a signal peptide alone would favor secretion (C) over ER residency (B). Distinguishing ER-resident from secreted requires knowing this specific protein belongs to the CREC family of ER calcium-binding proteins, which is protein-specific knowledge not derivable from general sequence heuristics.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The absence of a visible ER-retention signal (KDEL/HDEL) in the C-terminus of this precursor sequence means that experimental determination (immunofluorescence, subcellular fractionation, mass spectrometry of ER fractions) was required to establish ER residency rather than secretion. The CREC-family membership and ER-residency of PfERC is a protein-specific fact established by direct assay in four publications.",
    "reason": "While the signal peptide and EF-hand motifs provide general biological grounds to eliminate options A (no GTPase/helical-bundle G-protein motifs) and D (no tubulin-binding motifs), the critical distinction between B (endoplasmic reticulum) and C (extracellular region) cannot be resolved from the sequence alone. A signal peptide without a retention signal typically predicts secretion. The actual ER residency was established experimentally and is not inferable from general biological reasoning about the supplied sequence."
  },
  "case_id": "GO_cellular_component_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IIR7 (PFERC_PLAF7) is annotated as 'Endoplasmic reticulum-resident calcium binding protein' (PfERC) with subcellular location 'Endoplasmic reticulum' supported by four independent experimental studies (PubMed:9364972, 9497061, 23061985, 32098818), all with ECO:0000269 (direct assay) evidence. GO:0005783 (endoplasmic reticulum) is annotated with IDA:GeneDB evidence. The sequence matches the canonical entry exactly (SHA-256 match confirmed in both current and historical snapshots)."
  },
  "important_caveats": [
    "The UniProt entry flags the protein as a 'Precursor,' meaning the mature form may differ from the supplied sequence; the retention signal (if any) may be in a region not obvious in the full precursor.",
    "The EF-hand motifs are identifiable by general knowledge, but the CREC-family ER-residency classification is a specific annotation not derivable from sequence heuristics alone.",
    "All supporting evidence is experimental (ECO:0000269, direct assay) from four independent publications, providing strong confidence in the annotation.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q8IIR7, validating that annotations apply to this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Given a signal peptide directing into the secretory pathway but no visible ER-retention motif (KDEL/HDEL) and no transmembrane anchor, both 'endoplasmic reticulum' and 'extracellular region' are plausible predictions from sequence alone. The default prediction for a soluble protein with a signal peptide and no retention signal would be secretion (C). The correct answer (B) depends on protein-specific experimental knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IIR7 (PFERC_PLAF7) is annotated as 'Endoplasmic reticulum-resident calcium binding protein' (PfERC) with subcellular location 'Endoplasmic reticulum' supported by four independent experimental studies (PubMed:9364972, 9497061, 23061985, 32098818), all with ECO:0000269 (direct assay) evidence. GO:0005783 (endoplasmic reticulum) is annotated with IDA:GeneDB evidence. The sequence matches the canonical entry exactly (SHA-256 match confirmed in both current and historical snapshots).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "C10", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MMKINLYKLLCFICVIFLLHKNV) is recognizable as a signal peptide, directing the protein into the secretory pathway (ER). Multiple EF-hand calcium-binding motifs (repeated DxxxD...E...D...K patterns) and highly acidic character are identifiable. This narrows the plausible options to B (ER) or C (extracellular region), since both involve the secretory pathway. However, the mature sequence lacks a canonical KDEL/HDEL ER-retention signal and lacks a transmembrane domain, so the default sequence-based prediction from a signal peptide alone would favor secretion (C) over ER residency (B). Distinguishing ER-resident from secreted requires knowing this specific protein belongs to the CREC family of ER calcium-binding proteins, which is protein-specific knowledge not derivable from general sequence heuristics.",
    "missing_item_specific_fact": "The absence of a visible ER-retention signal (KDEL/HDEL) in the C-terminus of this precursor sequence means that experimental determination (immunofluorescence, subcellular fractionation, mass spectrometry of ER fractions) was required to establish ER residency rather than secretion. The CREC-family membership and ER-residency of PfERC is a protein-specific fact established by direct assay in four publications.",
    "reason": "While the signal peptide and EF-hand motifs provide general biological grounds to eliminate options A (no GTPase/helical-bundle G-protein motifs) and D (no tubulin-binding motifs), the critical distinction between B (endoplasmic reticulum) and C (extracellular region) cannot be resolved from the sequence alone. A signal peptide without a retention signal typically predicts secretion. The actual ER residency was established experimentally and is not inferable from general biological reasoning about the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Given a signal peptide directing into the secretory pathway but no visible ER-retention motif (KDEL/HDEL) and no transmembrane anchor, both 'endoplasmic reticulum' and 'extracellular region' are plausible predictions from sequence alone. The default prediction for a soluble protein with a signal peptide and no retention signal would be secretion (C). The correct answer (B) depends on protein-specific experimental knowledge."
  },
  "important_caveats": [
    "The UniProt entry flags the protein as a 'Precursor,' meaning the mature form may differ from the supplied sequence; the retention signal (if any) may be in a region not obvious in the full precursor.",
    "The EF-hand motifs are identifiable by general knowledge, but the CREC-family ER-residency classification is a specific annotation not derivable from sequence heuristics alone.",
    "All supporting evidence is experimental (ECO:0000269, direct assay) from four independent publications, providing strong confidence in the annotation.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q8IIR7, validating that annotations apply to this exact protein."
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

**Accession:** `Q8IIR7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 146. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.166389+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"9497061","source":"PubMed"}],"value":"Pf39"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"9364972","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9497061","source":"PubMed"}],"value":"Pfs40"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23061985","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"32098818","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9364972","source":"PubMed"}],"value":"Endoplasmic reticulum-resident calcium binding protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"23061985","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"32098818","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"9364972","source":"PubMed"}],"value":"PfERC"}]}}
```

Source SHA-256: `bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.166389+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"23061985","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32098818","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9364972","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9497061","source":"PubMed"}],"id":"SL-0095","value":"Endoplasmic reticulum"}}]}
```

Source SHA-256: `bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.166389+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"9364972","source":"PubMed"}],"id":"GO:0005783","properties":[{"key":"GoTerm","value":"C:endoplasmic reticulum"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.166389+00:00.  

```json
{"citation":{"authors":["La Greca N.","Hibbs A.R.","Riffkin C.","Foley M.","Tilley L."],"citationCrossReferences":[{"database":"PubMed","id":"9364972"},{"database":"DOI","id":"10.1016/s0166-6851(97)00134-5"}],"citationType":"journal article","firstPage":"283","id":"9364972","journal":"Mol. Biochem. Parasitol.","lastPage":"293","publicationDate":"1997","title":"Identification of an endoplasmic reticulum-resident calcium-binding protein with multiple EF-hand motifs in asexual stages of Plasmodium falciparum.","volume":"89"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"9364972","source":"PubMed"}],"type":"STRAIN","value":"D10"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"9364972","source":"PubMed"}],"type":"STRAIN","value":"FCR3"}],"referenceNumber":2,"referencePositions":["PROTEIN SEQUENCE OF 238-249","FUNCTION","SUBCELLULAR LOCATION","DEVELOPMENTAL STAGE"]}
```

Source SHA-256: `bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.166389+00:00.  

```json
{"citation":{"authors":["Templeton T.J.","Fujioka H.","Aikawa M.","Parker K.C.","Kaslow D.C."],"citationCrossReferences":[{"database":"PubMed","id":"9497061"},{"database":"DOI","id":"10.1016/s0166-6851(97)00164-3"}],"citationType":"journal article","firstPage":"359","id":"9497061","journal":"Mol. Biochem. Parasitol.","lastPage":"365","publicationDate":"1997","title":"Plasmodium falciparum Pfs40, renamed Pf39, is localized to an intracellular membrane-bound compartment and is not sexual stage-specific.","volume":"90"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["SUBCELLULAR LOCATION","DEVELOPMENTAL STAGE"]}
```

Source SHA-256: `bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.166389+00:00.  

```json
{"citation":{"authors":["Morita M.","Sanai H.","Hiramoto A.","Sato A.","Hiraoka O.","Sakura T.","Kaneko O.","Masuyama A.","Nojima M.","Wataya Y.","Kim H.S."],"citationCrossReferences":[{"database":"PubMed","id":"23061985"},{"database":"DOI","id":"10.1021/pr3005315"}],"citationType":"journal article","firstPage":"5704","id":"23061985","journal":"J. Proteome Res.","lastPage":"5711","publicationDate":"2012","title":"Plasmodium falciparum endoplasmic reticulum-resident calcium binding protein is a possible target of synthetic antimalarial endoperoxides, N-89 and N-251.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"23061985","source":"PubMed"}],"type":"STRAIN","value":"FCR3"}],"referenceNumber":4,"referencePositions":["IDENTIFICATION BY MASS SPECTROMETRY","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:13.166389+00:00.  

```json
{"citation":{"authors":["Fierro M.A.","Asady B.","Brooks C.F.","Cobb D.W.","Villegas A.","Moreno S.N.J.","Muralidharan V."],"citationCrossReferences":[{"database":"PubMed","id":"32098818"},{"database":"DOI","id":"10.1128/mbio.03078-19"}],"citationType":"journal article","firstPage":"0","id":"32098818","journal":"MBio","lastPage":"0","publicationDate":"2020","title":"An Endoplasmic Reticulum CREC Family Protein Regulates the Egress Proteolytic Cascade in Malaria Parasites.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)  
**Locator:** `lines 77-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 146 / 1.  
**Retrieved:** 2026-11-02T04:32:17.560132+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Endoplasmic reticulum
CC       {ECO:0000269|PubMed:23061985, ECO:0000269|PubMed:32098818,
CC       ECO:0000269|PubMed:9364972, ECO:0000269|PubMed:9497061}.
```

Source SHA-256: `6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)  
**Locator:** `lines 126-126`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 146 / 1.  
**Retrieved:** 2026-11-02T04:32:17.560132+00:00.  

```text
DR   GO; GO:0005783; C:endoplasmic reticulum; IDA:GeneDB.
```

Source SHA-256: `6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 177. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
