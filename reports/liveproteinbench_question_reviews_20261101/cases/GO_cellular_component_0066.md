# GO_cellular_component_0066

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — cytoplasm

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGVEEADKLKQLGNAAFSERKWHLAIDMYTKAIELTKTPTLFCNRALAELRAELPGAALADADAALGIEPTFAKAYYHKASAYLSLGKHKQALTNYKKVVDLAPQNSDAQAKVEFCKKEIRRINFENAIMTPDEAPLSQTIKLGSVRADYDGPRIENETVTVEFVEAMKEHFRLEKLIDRHDVIFILLEVQKILKKCPNFVSINVPVGEEITVCGDTHGQYYDLLNIFKLNGNPLETNRYLFNGDFVDRGSYSFENIMTLFAYKVLYPDHFFLSRGNHEGVSMNRMYGFEGEVTQKYNSEMFRLFTEVFNSLPIGHIINNEVFVVHGGLYSSDKVTLDDLQHPNRFRDIPESGLICESLWSDPQPMPGRAPSKRGVSCLSFGPDVTETFLNNNNLKLLVRSHEVKDEGYEIEHGGKCITVFSAPNYCDQMGNKGAFIRFTGGDMKPRFTTFTHVPHPGKRPMHYATGFGLF

[Multiple Choices]
A. transcription factor TFIID complex
B. mitochondrial matrix
C. SAGA complex
D. cytoplasm
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

> The sequence matches the Trypanosoma brucei serine/threonine-protein phosphatase T entry. Its annotation reports predominantly cytosolic localization, with GO cytoplasm supported by an IDA annotation citing PubMed:11290414. This supports D, while also recording nuclear localization in some cells.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has no obvious transmembrane segment or strong mitochondrial targeting presequence, which makes a soluble cytoplasmic protein plausible and weakens the mitochondrial-matrix choice. That does not establish its predominant localization or distinguish cytoplasm from possible nuclear localization.


**Missing item-specific fact**

> The protein-specific localization evidence that this phosphatase is predominantly cytosolic; this is not stated in the input.


**Reason**

> General sequence features can rule against some options, but selecting cytoplasm as the primary location relies on the protein-specific localization result, not a decisive argument available from the sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports cytoplasm as the primary location. Although the protein is also reported in the nucleus in some cells, nucleus is not an option, and the nuclear complex choices do not establish membership in those complexes.


### Important caveats

- The localization annotation is experimental-evidence-coded and cites PubMed:11290414; the supplied excerpts do not independently validate the underlying study.
- The matched sequence is from Trypanosoma brucei brucei strain 927/4 GUTat10.1, while the cited study annotation specifies strain LUMP 1026.
- Cytosol is included within the broader GO term cytoplasm.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has no obvious transmembrane segment or strong mitochondrial targeting presequence, which makes a soluble cytoplasmic protein plausible and weakens the mitochondrial-matrix choice. That does not establish its predominant localization or distinguish cytoplasm from possible nuclear localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization evidence that this phosphatase is predominantly cytosolic; this is not stated in the input.",
    "reason": "General sequence features can rule against some options, but selecting cytoplasm as the primary location relies on the protein-specific localization result, not a decisive argument available from the sequence and choices."
  },
  "case_id": "GO_cellular_component_0066",
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
    "reason": "The sequence matches the Trypanosoma brucei serine/threonine-protein phosphatase T entry. Its annotation reports predominantly cytosolic localization, with GO cytoplasm supported by an IDA annotation citing PubMed:11290414. This supports D, while also recording nuclear localization in some cells."
  },
  "important_caveats": [
    "The localization annotation is experimental-evidence-coded and cites PubMed:11290414; the supplied excerpts do not independently validate the underlying study.",
    "The matched sequence is from Trypanosoma brucei brucei strain 927/4 GUTat10.1, while the cited study annotation specifies strain LUMP 1026.",
    "Cytosol is included within the broader GO term cytoplasm."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports cytoplasm as the primary location. Although the protein is also reported in the nucleus in some cells, nucleus is not an option, and the nuclear complex choices do not establish membership in those complexes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the Trypanosoma brucei serine/threonine-protein phosphatase T entry. Its annotation reports predominantly cytosolic localization, with GO cytoplasm supported by an IDA annotation citing PubMed:11290414. This supports D, while also recording nuclear localization in some cells.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has no obvious transmembrane segment or strong mitochondrial targeting presequence, which makes a soluble cytoplasmic protein plausible and weakens the mitochondrial-matrix choice. That does not establish its predominant localization or distinguish cytoplasm from possible nuclear localization.",
    "missing_item_specific_fact": "The protein-specific localization evidence that this phosphatase is predominantly cytosolic; this is not stated in the input.",
    "reason": "General sequence features can rule against some options, but selecting cytoplasm as the primary location relies on the protein-specific localization result, not a decisive argument available from the sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports cytoplasm as the primary location. Although the protein is also reported in the nucleus in some cells, nucleus is not an option, and the nuclear complex choices do not establish membership in those complexes."
  },
  "important_caveats": [
    "The localization annotation is experimental-evidence-coded and cites PubMed:11290414; the supplied excerpts do not independently validate the underlying study.",
    "The matched sequence is from Trypanosoma brucei brucei strain 927/4 GUTat10.1, while the cited study annotation specifies strain LUMP 1026.",
    "Cytosol is included within the broader GO term cytoplasm."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q388N2 (TbPP5, Serine/threonine-protein phosphatase T from Trypanosoma brucei) carries experimental (ECO:0000269, PubMed:11290414) subcellular localization annotation stating 'Predominantly present in the cytosol and localizes densely to the area near the nucleus.' GO annotations include GO:0005737 (cytoplasm, IDA) and GO:0005829 (cytosol, IDA), with cytosol being part_of cytoplasm. The primary location is cytoplasm, matching option D. Options A (TFIID complex) and C (SAGA complex) are nuclear transcription coactivator complexes with no relation to a PP5-type phosphatase; option B (mitochondrial matrix) is unsupported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical PP1/PP5-family catalytic motifs (GDxHG: 'GDTHGQ'; GDxVDRG: 'GDFVDRGS'; HGG: 'HGGKCITV') and a C-terminal tetratricopeptide repeat (TPR) domain characteristic of PP5-type phosphatases. PP5 family members are well-established cytoplasmic enzymes: the TPR domain mediates constitutive binding to Hsp90, sequestering the phosphatase in the cytosol until stress-induced dissociation. No N-terminal mitochondrial targeting presequence (amphipathic, positively charged helix) is present, ruling out mitochondrial matrix (B). A serine/threonine phosphatase is not a structural component of the multi-subunit TFIID (A) or SAGA (C) transcription complexes. The 'primary' qualifier in the question aligns with the known predominant cytoplasmic localization of PP5.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the PP5 catalytic architecture (conserved GD motifs, HGG motif, TPR domain) can invoke general PP5-family biology—cytoplasmic Hsp90-bound phosphatase—to select cytoplasm. The distractors are eliminated by general reasoning: no mitochondrial targeting signal excludes B; a phosphatase is not a subunit of TFIID or SAGA complexes, excluding A and C. The distinction from nucleus is handled by the 'primary' qualifier and the well-known Hsp90 sequestration mechanism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry also annotates nucleus (GO:0005634), the question asks for the 'primary' cellular component, and the experimental annotation explicitly states 'predominantly present in the cytosol.' The PP5 TPR-Hsp90 mechanism provides a clear biological rationale for cytoplasm as the primary compartment. The other options (A, B, C) are not defensible for a PP5-type phosphatase.


### Important caveats

- The UniProt entry also annotates nucleus (GO:0005634, IDA) as a secondary location; the 'primary' qualifier in the question resolves this in favor of cytoplasm.
- Sequence identity was confirmed as Q388N2 (matched, 472 aa) via reviewer-only accession inference from dataset metadata; the evaluated model did not receive this accession.
- The PP5 family assignment is based on recognizable catalytic and TPR motifs; the model need not know the exact Trypanosoma protein to apply general PP5 biology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical PP1/PP5-family catalytic motifs (GDxHG: 'GDTHGQ'; GDxVDRG: 'GDFVDRGS'; HGG: 'HGGKCITV') and a C-terminal tetratricopeptide repeat (TPR) domain characteristic of PP5-type phosphatases. PP5 family members are well-established cytoplasmic enzymes: the TPR domain mediates constitutive binding to Hsp90, sequestering the phosphatase in the cytosol until stress-induced dissociation. No N-terminal mitochondrial targeting presequence (amphipathic, positively charged helix) is present, ruling out mitochondrial matrix (B). A serine/threonine phosphatase is not a structural component of the multi-subunit TFIID (A) or SAGA (C) transcription complexes. The 'primary' qualifier in the question aligns with the known predominant cytoplasmic localization of PP5.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the PP5 catalytic architecture (conserved GD motifs, HGG motif, TPR domain) can invoke general PP5-family biology—cytoplasmic Hsp90-bound phosphatase—to select cytoplasm. The distractors are eliminated by general reasoning: no mitochondrial targeting signal excludes B; a phosphatase is not a subunit of TFIID or SAGA complexes, excluding A and C. The distinction from nucleus is handled by the 'primary' qualifier and the well-known Hsp90 sequestration mechanism."
  },
  "case_id": "GO_cellular_component_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q388N2 (TbPP5, Serine/threonine-protein phosphatase T from Trypanosoma brucei) carries experimental (ECO:0000269, PubMed:11290414) subcellular localization annotation stating 'Predominantly present in the cytosol and localizes densely to the area near the nucleus.' GO annotations include GO:0005737 (cytoplasm, IDA) and GO:0005829 (cytosol, IDA), with cytosol being part_of cytoplasm. The primary location is cytoplasm, matching option D. Options A (TFIID complex) and C (SAGA complex) are nuclear transcription coactivator complexes with no relation to a PP5-type phosphatase; option B (mitochondrial matrix) is unsupported."
  },
  "important_caveats": [
    "The UniProt entry also annotates nucleus (GO:0005634, IDA) as a secondary location; the 'primary' qualifier in the question resolves this in favor of cytoplasm.",
    "Sequence identity was confirmed as Q388N2 (matched, 472 aa) via reviewer-only accession inference from dataset metadata; the evaluated model did not receive this accession.",
    "The PP5 family assignment is based on recognizable catalytic and TPR motifs; the model need not know the exact Trypanosoma protein to apply general PP5 biology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry also annotates nucleus (GO:0005634), the question asks for the 'primary' cellular component, and the experimental annotation explicitly states 'predominantly present in the cytosol.' The PP5 TPR-Hsp90 mechanism provides a clear biological rationale for cytoplasm as the primary compartment. The other options (A, B, C) are not defensible for a PP5-type phosphatase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q388N2 (TbPP5, Serine/threonine-protein phosphatase T from Trypanosoma brucei) carries experimental (ECO:0000269, PubMed:11290414) subcellular localization annotation stating 'Predominantly present in the cytosol and localizes densely to the area near the nucleus.' GO annotations include GO:0005737 (cytoplasm, IDA) and GO:0005829 (cytosol, IDA), with cytosol being part_of cytoplasm. The primary location is cytoplasm, matching option D. Options A (TFIID complex) and C (SAGA complex) are nuclear transcription coactivator complexes with no relation to a PP5-type phosphatase; option B (mitochondrial matrix) is unsupported.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical PP1/PP5-family catalytic motifs (GDxHG: 'GDTHGQ'; GDxVDRG: 'GDFVDRGS'; HGG: 'HGGKCITV') and a C-terminal tetratricopeptide repeat (TPR) domain characteristic of PP5-type phosphatases. PP5 family members are well-established cytoplasmic enzymes: the TPR domain mediates constitutive binding to Hsp90, sequestering the phosphatase in the cytosol until stress-induced dissociation. No N-terminal mitochondrial targeting presequence (amphipathic, positively charged helix) is present, ruling out mitochondrial matrix (B). A serine/threonine phosphatase is not a structural component of the multi-subunit TFIID (A) or SAGA (C) transcription complexes. The 'primary' qualifier in the question aligns with the known predominant cytoplasmic localization of PP5.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the PP5 catalytic architecture (conserved GD motifs, HGG motif, TPR domain) can invoke general PP5-family biology—cytoplasmic Hsp90-bound phosphatase—to select cytoplasm. The distractors are eliminated by general reasoning: no mitochondrial targeting signal excludes B; a phosphatase is not a subunit of TFIID or SAGA complexes, excluding A and C. The distinction from nucleus is handled by the 'primary' qualifier and the well-known Hsp90 sequestration mechanism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry also annotates nucleus (GO:0005634), the question asks for the 'primary' cellular component, and the experimental annotation explicitly states 'predominantly present in the cytosol.' The PP5 TPR-Hsp90 mechanism provides a clear biological rationale for cytoplasm as the primary compartment. The other options (A, B, C) are not defensible for a PP5-type phosphatase."
  },
  "important_caveats": [
    "The UniProt entry also annotates nucleus (GO:0005634, IDA) as a secondary location; the 'primary' qualifier in the question resolves this in favor of cytoplasm.",
    "Sequence identity was confirmed as Q388N2 (matched, 472 aa) via reviewer-only accession inference from dataset metadata; the evaluated model did not receive this accession.",
    "The PP5 family assignment is based on recognizable catalytic and TPR motifs; the model need not know the exact Trypanosoma protein to apply general PP5 biology."
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

**Accession:** `Q388N2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
"Q388N2"
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11290414","source":"PubMed"}],"value":"TbPP5"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Serine/threonine-protein phosphatase T"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PPT"}]}}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/comments/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11290414","source":"PubMed"}],"value":"Predominantly present in the cytosol and localizes densely to the area near the nucleus (PubMed:11290414). Also present in the nucleus of some cells (PubMed:11290414)"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"11290414","source":"PubMed"}],"id":"SL-0091","value":"Cytoplasm, cytosol"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"11290414","source":"PubMed"}],"id":"SL-0191","value":"Nucleus"}}]}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"11290414","source":"PubMed"}],"id":"GO:0005737","properties":[{"key":"GoTerm","value":"C:cytoplasm"},{"key":"GoEvidenceType","value":"IDA:GeneDB"}]}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"11290414","source":"PubMed"}],"id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 80-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:11290414}.
CC       Nucleus {ECO:0000269|PubMed:11290414}. Note=Predominantly present in
CC       the cytosol and localizes densely to the area near the nucleus
CC       (PubMed:11290414). Also present in the nucleus of some cells
CC       (PubMed:11290414). {ECO:0000269|PubMed:11290414}.
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 110-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
DR   GO; GO:0005737; C:cytoplasm; IDA:GeneDB.
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 111-111`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; IDA:UniProtKB.
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 66. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
