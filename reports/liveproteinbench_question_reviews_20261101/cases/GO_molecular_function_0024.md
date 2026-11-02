# GO_molecular_function_0024

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — cysteine-type endopeptidase inhibitor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAFFKSAVFLVCVVLAAAGSASRSKRALVGGWKTQDPTNPKFENLAHYAVSTQVEGREYYDTVLELLEVQTQIVAGVNYKLKFTTTQSTCKIETGVEYSKELCQPKTNKVEAVCTSIIYTVPWQNIKRVLSYHCDAPNDV

[Multiple Choices]
A. 3'-phosphoadenosine 5'-phosphosulfate binding
B. single-stranded DNA endodeoxyribonuclease activity
C. cysteine-type endopeptidase inhibitor activity
D. cysteine desulfurase activity
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

> The supplied sequence exactly matches the protein annotated as mialostatin. UniProt reports inhibition of cysteine proteinases with experimental evidence, supporting choice C; the GO cross-reference is also to the matching inhibitor-activity term.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a signal peptide, and the small mature protein is compatible with a secreted inhibitor. These clues do not establish its specific molecular activity over the alternatives.


**Missing item-specific fact**

> The protein-specific identification as mialostatin and its experimentally reported inhibition of cysteine proteinases are not provided in the question.


**Reason**

> Choosing C is supported by matched sequence-specific annotation and experimental reports, not by a decisive argument from the supplied sequence alone. Recognizing the exact protein or retrieving its functional annotation would be needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence-specific functional evidence supports C; no alternative listed activity is supported by the supplied evidence.


### Important caveats

- The UniProt functional annotation cites experimental evidence (ECO:0000269); the GO cross-reference itself is computationally assigned.
- The sequence match is exact in both current and historical UniProt records, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and the small mature protein is compatible with a secreted inhibitor. These clues do not establish its specific molecular activity over the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as mialostatin and its experimentally reported inhibition of cysteine proteinases are not provided in the question.",
    "reason": "Choosing C is supported by matched sequence-specific annotation and experimental reports, not by a decisive argument from the supplied sequence alone. Recognizing the exact protein or retrieving its functional annotation would be needed."
  },
  "case_id": "GO_molecular_function_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the protein annotated as mialostatin. UniProt reports inhibition of cysteine proteinases with experimental evidence, supporting choice C; the GO cross-reference is also to the matching inhibitor-activity term."
  },
  "important_caveats": [
    "The UniProt functional annotation cites experimental evidence (ECO:0000269); the GO cross-reference itself is computationally assigned.",
    "The sequence match is exact in both current and historical UniProt records, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence-specific functional evidence supports C; no alternative listed activity is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the protein annotated as mialostatin. UniProt reports inhibition of cysteine proteinases with experimental evidence, supporting choice C; the GO cross-reference is also to the matching inhibitor-activity term.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and the small mature protein is compatible with a secreted inhibitor. These clues do not establish its specific molecular activity over the alternatives.",
    "missing_item_specific_fact": "The protein-specific identification as mialostatin and its experimentally reported inhibition of cysteine proteinases are not provided in the question.",
    "reason": "Choosing C is supported by matched sequence-specific annotation and experimental reports, not by a decisive argument from the supplied sequence alone. Recognizing the exact protein or retrieving its functional annotation would be needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence-specific functional evidence supports C; no alternative listed activity is supported by the supplied evidence."
  },
  "important_caveats": [
    "The UniProt functional annotation cites experimental evidence (ECO:0000269); the GO cross-reference itself is computationally assigned.",
    "The sequence match is exact in both current and historical UniProt records, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry V5H924 (Mialostatin, Ixodes ricinus) carries a FUNCTION comment with direct experimental evidence (ECO:0000269, PubMed:34065290 and 38444844) stating it is an 'Inhibitor of cysteine proteinases' that inhibits cathepsin L1, L3, B, C and host cathepsins B, C, H, K, L, S. X-ray crystallography at 1.55 Å (PDB 6ZTK) and mass spectrometry further support the annotation. The GO term GO:0004869 (cysteine-type endopeptidase inhibitor activity) is assigned. The sequence matches exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The mature protein (~120 aa after signal peptide cleavage) displays the three canonical cystatin family motifs: (1) an N-terminal glycine-rich region 'ALVGGW' (conserved Gly), (2) a QxVxG motif in 'EQTQIVAG' (Q-I-V-A-G), and (3) the highly conserved Pro-Trp motif in 'TVPWQ'. Combined with the small secreted architecture (signal peptide, ~140 aa precursor) and multiple cysteines (4 in mature form, consistent with Type 2 cystatin disulfide bonding), these features are diagnostic of the cystatin family and its molecular function as a cysteine-type endopeptidase inhibitor. The other options are excluded by size and motif absence: cysteine desulfurases are ~400 aa PLP-dependent enzymes; ssDNA endonucleases require nuclease catalytic motifs; PAPS-binding proteins require PSAP or similar motifs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The cystatin QxVxG and PW motifs are well-established, textbook-level protein biochemistry features. A biologist familiar with protease inhibitor families could identify the cystatin fold from these motifs in the sequence without needing to look up this specific protein's database entry. The reasoning chain (signal peptide → small secreted protein → PW + QxVxG motifs → cystatin → cysteine protease inhibitor) is a valid general-knowledge inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three canonical cystatin motifs (QxVxG, PW, N-terminal Gly) together with the small secreted architecture and disulfide-forming cysteines uniquely point to option C. The other options require entirely different structural and catalytic features (PLP cofactor for desulfurase, nuclease motifs for ssDNA endonuclease, PSAP domain for PAPS binding) that are absent from this 140-aa sequence.


### Important caveats

- The GO annotation in UniProt is IEA (inferred from electronic annotation via InterPro/UniProtKB keyword), but the underlying FUNCTION comment is backed by direct experimental evidence (ECO:0000269) from two independent studies.
- The QxVxG motif match ('QIVAG') is slightly degenerate compared to the canonical 'QxVxG' consensus, though the PW motif is unambiguous.
- The protein is a tick-derived cystatin (Mialostatin); recognizing it as a cystatin does not require knowing the specific organism or protein name, only the conserved family motifs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The mature protein (~120 aa after signal peptide cleavage) displays the three canonical cystatin family motifs: (1) an N-terminal glycine-rich region 'ALVGGW' (conserved Gly), (2) a QxVxG motif in 'EQTQIVAG' (Q-I-V-A-G), and (3) the highly conserved Pro-Trp motif in 'TVPWQ'. Combined with the small secreted architecture (signal peptide, ~140 aa precursor) and multiple cysteines (4 in mature form, consistent with Type 2 cystatin disulfide bonding), these features are diagnostic of the cystatin family and its molecular function as a cysteine-type endopeptidase inhibitor. The other options are excluded by size and motif absence: cysteine desulfurases are ~400 aa PLP-dependent enzymes; ssDNA endonucleases require nuclease catalytic motifs; PAPS-binding proteins require PSAP or similar motifs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The cystatin QxVxG and PW motifs are well-established, textbook-level protein biochemistry features. A biologist familiar with protease inhibitor families could identify the cystatin fold from these motifs in the sequence without needing to look up this specific protein's database entry. The reasoning chain (signal peptide → small secreted protein → PW + QxVxG motifs → cystatin → cysteine protease inhibitor) is a valid general-knowledge inference."
  },
  "case_id": "GO_molecular_function_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry V5H924 (Mialostatin, Ixodes ricinus) carries a FUNCTION comment with direct experimental evidence (ECO:0000269, PubMed:34065290 and 38444844) stating it is an 'Inhibitor of cysteine proteinases' that inhibits cathepsin L1, L3, B, C and host cathepsins B, C, H, K, L, S. X-ray crystallography at 1.55 Å (PDB 6ZTK) and mass spectrometry further support the annotation. The GO term GO:0004869 (cysteine-type endopeptidase inhibitor activity) is assigned. The sequence matches exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA (inferred from electronic annotation via InterPro/UniProtKB keyword), but the underlying FUNCTION comment is backed by direct experimental evidence (ECO:0000269) from two independent studies.",
    "The QxVxG motif match ('QIVAG') is slightly degenerate compared to the canonical 'QxVxG' consensus, though the PW motif is unambiguous.",
    "The protein is a tick-derived cystatin (Mialostatin); recognizing it as a cystatin does not require knowing the specific organism or protein name, only the conserved family motifs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three canonical cystatin motifs (QxVxG, PW, N-terminal Gly) together with the small secreted architecture and disulfide-forming cysteines uniquely point to option C. The other options require entirely different structural and catalytic features (PLP cofactor for desulfurase, nuclease motifs for ssDNA endonuclease, PSAP domain for PAPS binding) that are absent from this 140-aa sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry V5H924 (Mialostatin, Ixodes ricinus) carries a FUNCTION comment with direct experimental evidence (ECO:0000269, PubMed:34065290 and 38444844) stating it is an 'Inhibitor of cysteine proteinases' that inhibits cathepsin L1, L3, B, C and host cathepsins B, C, H, K, L, S. X-ray crystallography at 1.55 Å (PDB 6ZTK) and mass spectrometry further support the annotation. The GO term GO:0004869 (cysteine-type endopeptidase inhibitor activity) is assigned. The sequence matches exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The mature protein (~120 aa after signal peptide cleavage) displays the three canonical cystatin family motifs: (1) an N-terminal glycine-rich region 'ALVGGW' (conserved Gly), (2) a QxVxG motif in 'EQTQIVAG' (Q-I-V-A-G), and (3) the highly conserved Pro-Trp motif in 'TVPWQ'. Combined with the small secreted architecture (signal peptide, ~140 aa precursor) and multiple cysteines (4 in mature form, consistent with Type 2 cystatin disulfide bonding), these features are diagnostic of the cystatin family and its molecular function as a cysteine-type endopeptidase inhibitor. The other options are excluded by size and motif absence: cysteine desulfurases are ~400 aa PLP-dependent enzymes; ssDNA endonucleases require nuclease catalytic motifs; PAPS-binding proteins require PSAP or similar motifs.",
    "missing_item_specific_fact": "",
    "reason": "The cystatin QxVxG and PW motifs are well-established, textbook-level protein biochemistry features. A biologist familiar with protease inhibitor families could identify the cystatin fold from these motifs in the sequence without needing to look up this specific protein's database entry. The reasoning chain (signal peptide → small secreted protein → PW + QxVxG motifs → cystatin → cysteine protease inhibitor) is a valid general-knowledge inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three canonical cystatin motifs (QxVxG, PW, N-terminal Gly) together with the small secreted architecture and disulfide-forming cysteines uniquely point to option C. The other options require entirely different structural and catalytic features (PLP cofactor for desulfurase, nuclease motifs for ssDNA endonuclease, PSAP domain for PAPS binding) that are absent from this 140-aa sequence."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA (inferred from electronic annotation via InterPro/UniProtKB keyword), but the underlying FUNCTION comment is backed by direct experimental evidence (ECO:0000269) from two independent studies.",
    "The QxVxG motif match ('QIVAG') is slightly degenerate compared to the canonical 'QxVxG' consensus, though the PW motif is unambiguous.",
    "The protein is a tick-derived cystatin (Mialostatin); recognizing it as a cystatin does not require knowing the specific organism or protein name, only the conserved family motifs."
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

**Accession:** `V5H924` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 33. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V5H924.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:03.811258+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34065290","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38444844","source":"PubMed"}],"value":"Mialostatin"}}}
```

Source SHA-256: `67ce73be04e5e21e9a9bef22a442c902d04b23a06bed3a61d9770ed95a4c54e2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V5H924.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:03.811258+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34065290","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38444844","source":"PubMed"}],"value":"Inhibitor of cysteine proteinases (PubMed:34065290, PubMed:38444844). Inhibits several endogenous midgut digestive cysteine proteases, such as cathepsin L1, L3, B and C, but not aspartic protease cathepsin D1 and cysteine protease legumain (PubMed:34065290). Inhibits proteolysis of blood proteins catalyzed by tick gut cysteine cathepsins (PubMed:34065290). Inhibits host cathepsin B (CSTB), C (CTSC), H (CTSH), K (CTSK), L (CTSL) and S (CTSS) (PubMed:34065290, PubMed:38444844)"}]}
```

Source SHA-256: `67ce73be04e5e21e9a9bef22a442c902d04b23a06bed3a61d9770ed95a4c54e2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V5H924.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:03.811258+00:00.  

```json
{"database":"GO","id":"GO:0004869","properties":[{"key":"GoTerm","value":"F:cysteine-type endopeptidase inhibitor activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `67ce73be04e5e21e9a9bef22a442c902d04b23a06bed3a61d9770ed95a4c54e2`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/V5H924.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:03.811258+00:00.  

```json
{"citation":{"authors":["Kotal J.","Busa M.","Urbanova V.","Rezacova P.","Chmelar J.","Langhansova H.","Sojka D.","Mares M.","Kotsyfakis M."],"citationCrossReferences":[{"database":"PubMed","id":"34065290"},{"database":"DOI","id":"10.3390/ijms22105371"}],"citationType":"journal article","firstPage":"0","id":"34065290","journal":"Int. J. Mol. Sci.","lastPage":"0","publicationDate":"2021","title":"Mialostatin, a Novel Midgut Cystatin from <i>Ixodes ricinus</i> Ticks: Crystal Structure and Regulation of Host Blood Digestion.","volume":"22"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6ZTK","source":"PDB"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.55 ANGSTROMS) OF 9-140","IDENTIFICATION BY MASS SPECTROMETRY","FUNCTION","SUBCELLULAR LOCATION","TISSUE SPECIFICITY","INDUCTION BY BLOOD FEEDING","DISULFIDE BONDS"]}
```

Source SHA-256: `67ce73be04e5e21e9a9bef22a442c902d04b23a06bed3a61d9770ed95a4c54e2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V5H924?format=txt&versions=33)  
**Locator:** `lines 39-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:34:08.928179+00:00.  

```text
CC   -!- FUNCTION: Inhibitor of cysteine proteinases (PubMed:34065290,
CC       PubMed:38444844). Inhibits several endogenous midgut digestive cysteine
CC       proteases, such as cathepsin L1, L3, B and C, but not aspartic protease
CC       cathepsin D1 and cysteine protease legumain (PubMed:34065290). Inhibits
CC       proteolysis of blood proteins catalyzed by tick gut cysteine cathepsins
CC       (PubMed:34065290). Inhibits host cathepsin B (CSTB), C (CTSC), H
CC       (CTSH), K (CTSK), L (CTSL) and S (CTSS) (PubMed:34065290,
CC       PubMed:38444844). {ECO:0000269|PubMed:34065290,
CC       ECO:0000269|PubMed:38444844}.
```

Source SHA-256: `d09a9d61de00fa8fb5a39d6875fda110f9b83db00fab10f3412c0d727c5635ab`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/V5H924?format=txt&versions=33)  
**Locator:** `lines 70-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 33 / 1.  
**Retrieved:** 2026-11-02T04:34:08.928179+00:00.  

```text
DR   GO; GO:0004869; F:cysteine-type endopeptidase inhibitor activity; IEA:UniProtKB-KW.
```

Source SHA-256: `d09a9d61de00fa8fb5a39d6875fda110f9b83db00fab10f3412c0d727c5635ab`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
