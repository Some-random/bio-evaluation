# cofactor_0119

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGNRGVVYLGPGKVEVQNIPYPKMQDPQGRQIDHGVILRVVSTNICGSDQHMVRGRTTAPEGLVLGHEITGEVVEIGRGVETMKIGDLVSVPFNVACGHCRTCKEQHTGVCLTVNPARAGGAYGYVDMGGWVGGQAEYVLVPYADFNLLKLPNREAAMEKIRDLTCLSDILPTGYHGAVTAGVGPGSTVYIAGAGPVGLAAAASARLLGAAVVIVGDVNPTRLAHAKKQGFEIADLSKDTPLHEQIAALLGEPEVDCAVDAVGFEARGHGHSGSQQEAPATVLNSLMGITRVAGKIGIPGLYVTEDPGAVDAAAKHGALSIRFGLGWAKSHSFHTGQTPVMKYNRQLMQAIMWDRIKIADIVGVEVITLDDAPKGYGEFDAGVPKKFVIDPHNLFRAA

[Multiple Choices]
A. Fe(2+)
B. cob(II)alamin
C. [2Fe-2S] cluster
D. Zn(2+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the UniProt entry for this protein. That entry annotates Zn(2+) as a cofactor, reports two Zn(2+) ions per subunit, and cites experimental evidence; a cited crystal structure is described as containing zinc.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a conspicuous Cys/His-rich segment (…ACGHCRTCKEQHTGVCL…), a plausible metal-binding motif that favors Zn(2+) among the listed choices over cob(II)alamin or a &#91;2Fe-2S&#93; cluster. This is a meaningful sequence-based clue, though not experimental proof.


**Missing item-specific fact**

> No additional item-specific fact is required for a defensible motif-based choice; experimental confirmation that this protein binds zinc is external to the question.


**Reason**

> The sequence provides a concrete metal-binding clue that distinguishes the choices, while the reviewer-only experimental annotation independently supports the key. The experimental evidence itself was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Cys/His-rich motif favors zinc among these options; the reviewer-only evidence also specifically supports Zn(2+).


### Important caveats

- The sequence motif is suggestive rather than conclusive on its own.
- The database annotation cites experimental evidence, but the cited primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a conspicuous Cys/His-rich segment (…ACGHCRTCKEQHTGVCL…), a plausible metal-binding motif that favors Zn(2+) among the listed choices over cob(II)alamin or a [2Fe-2S] cluster. This is a meaningful sequence-based clue, though not experimental proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional item-specific fact is required for a defensible motif-based choice; experimental confirmation that this protein binds zinc is external to the question.",
    "reason": "The sequence provides a concrete metal-binding clue that distinguishes the choices, while the reviewer-only experimental annotation independently supports the key. The experimental evidence itself was not supplied to the evaluated model."
  },
  "case_id": "cofactor_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein. That entry annotates Zn(2+) as a cofactor, reports two Zn(2+) ions per subunit, and cites experimental evidence; a cited crystal structure is described as containing zinc."
  },
  "important_caveats": [
    "The sequence motif is suggestive rather than conclusive on its own.",
    "The database annotation cites experimental evidence, but the cited primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys/His-rich motif favors zinc among these options; the reviewer-only evidence also specifically supports Zn(2+)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for this protein. That entry annotates Zn(2+) as a cofactor, reports two Zn(2+) ions per subunit, and cites experimental evidence; a cited crystal structure is described as containing zinc.",
    "evidence_ids": ["C1", "C5", "C7", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a conspicuous Cys/His-rich segment (…ACGHCRTCKEQHTGVCL…), a plausible metal-binding motif that favors Zn(2+) among the listed choices over cob(II)alamin or a [2Fe-2S] cluster. This is a meaningful sequence-based clue, though not experimental proof.",
    "missing_item_specific_fact": "No additional item-specific fact is required for a defensible motif-based choice; experimental confirmation that this protein binds zinc is external to the question.",
    "reason": "The sequence provides a concrete metal-binding clue that distinguishes the choices, while the reviewer-only experimental annotation independently supports the key. The experimental evidence itself was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys/His-rich motif favors zinc among these options; the reviewer-only evidence also specifically supports Zn(2+)."
  },
  "important_caveats": [
    "The sequence motif is suggestive rather than conclusive on its own.",
    "The database annotation cites experimental evidence, but the cited primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXZ0 (Glutathione-independent formaldehyde dehydrogenase, EC 1.2.1.46, Pseudomonas aeruginosa LESB58) annotates Zn(2+) as the cofactor with experimental evidence code ECO:0000269 (direct assay, PubMed:23989142). The X-ray crystallography reference (PDB 4JLW, 2.70 Å) confirms the protein in complex with NAD and zinc. The annotation states 'Binds 2 Zn(2+) ions per subunit.' Sequence match is exact (399 AA, SHA256 matched in both current and historical records).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Rossmann-fold-like nucleotide-binding motif (GPGSTVYIAGAGPVGL, with GxGxxG spacing) indicating an NAD(P)-dependent dehydrogenase. Aldehyde dehydrogenases classically require Zn(2+) as a catalytic metal. The sequence also contains Cys/His clusters (e.g., 'ACGHCRTCKEQHTG' and 'GHGHSG') consistent with Zn coordination by Cys/His ligands. Distractors can be argued against: &#91;2Fe-2S&#93; requires a tight Cys4 (or 3Cys+1His) motif in specific spacing not clearly present; cob(II)alamin is restricted to radical SAM mutases and isomutases, not dehydrogenases; Fe(2+) is more typical of oxygenases/dioxygenases than NAD-dependent dehydrogenases.


**Missing item-specific fact**

> Precise identification of this protein as a formaldehyde dehydrogenase (vs. another dehydrogenase subtype) from sequence alone is non-trivial without database lookup, though the general 'dehydrogenase → Zn2+' heuristic applies broadly.


**Reason**

> A model with general biochemistry knowledge can identify dehydrogenase features (Rossmann fold, Cys/His metal-binding clusters) and apply the well-established rule that aldehyde/alcohol dehydrogenases use Zn2+. The distractors are eliminable by enzyme-class logic (cob(II)alamin for mutases, &#91;2Fe-2S&#93; for ferredoxins with specific Cys4 motifs, Fe2+ for oxygenases). The reasoning chain is not airtight but provides meaningful grounds to prefer D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the protein also binds NAD+ (a co-substrate/cofactor), NAD+ is not among the choices. Among the four options, Zn(2+) is the only metal cofactor consistent with a dehydrogenase bearing Cys/His clusters and lacking Fe-S or B12 signatures. No other option is defensible given the enzyme class.


### Important caveats

- The UniProt entry was first public on 2025-04-09; the author's source snapshot date is unknown but the sequence matches exactly.
- The crystallography evidence (PDB 4JLW) shows zinc in the structure but the paper title emphasizes NAD+ binding; zinc coordination is confirmed by the cofactor annotation and structural reference.
- The reasoning pathway (dehydrogenase → Zn2+) is a general heuristic that does not guarantee Zn2+ for every dehydrogenase (e.g., some use FAD or no metal), but it is the strongest prior among the given choices.
- The protein is 'glutathione-independent' FALDH, a distinct family from the classic ALDH superfamily; its zinc-binding mechanism may differ from canonical ALDH zinc coordination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold-like nucleotide-binding motif (GPGSTVYIAGAGPVGL, with GxGxxG spacing) indicating an NAD(P)-dependent dehydrogenase. Aldehyde dehydrogenases classically require Zn(2+) as a catalytic metal. The sequence also contains Cys/His clusters (e.g., 'ACGHCRTCKEQHTG' and 'GHGHSG') consistent with Zn coordination by Cys/His ligands. Distractors can be argued against: [2Fe-2S] requires a tight Cys4 (or 3Cys+1His) motif in specific spacing not clearly present; cob(II)alamin is restricted to radical SAM mutases and isomutases, not dehydrogenases; Fe(2+) is more typical of oxygenases/dioxygenases than NAD-dependent dehydrogenases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of this protein as a formaldehyde dehydrogenase (vs. another dehydrogenase subtype) from sequence alone is non-trivial without database lookup, though the general 'dehydrogenase → Zn2+' heuristic applies broadly.",
    "reason": "A model with general biochemistry knowledge can identify dehydrogenase features (Rossmann fold, Cys/His metal-binding clusters) and apply the well-established rule that aldehyde/alcohol dehydrogenases use Zn2+. The distractors are eliminable by enzyme-class logic (cob(II)alamin for mutases, [2Fe-2S] for ferredoxins with specific Cys4 motifs, Fe2+ for oxygenases). The reasoning chain is not airtight but provides meaningful grounds to prefer D."
  },
  "case_id": "cofactor_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXZ0 (Glutathione-independent formaldehyde dehydrogenase, EC 1.2.1.46, Pseudomonas aeruginosa LESB58) annotates Zn(2+) as the cofactor with experimental evidence code ECO:0000269 (direct assay, PubMed:23989142). The X-ray crystallography reference (PDB 4JLW, 2.70 Å) confirms the protein in complex with NAD and zinc. The annotation states 'Binds 2 Zn(2+) ions per subunit.' Sequence match is exact (399 AA, SHA256 matched in both current and historical records)."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-04-09; the author's source snapshot date is unknown but the sequence matches exactly.",
    "The crystallography evidence (PDB 4JLW) shows zinc in the structure but the paper title emphasizes NAD+ binding; zinc coordination is confirmed by the cofactor annotation and structural reference.",
    "The reasoning pathway (dehydrogenase → Zn2+) is a general heuristic that does not guarantee Zn2+ for every dehydrogenase (e.g., some use FAD or no metal), but it is the strongest prior among the given choices.",
    "The protein is 'glutathione-independent' FALDH, a distinct family from the classic ALDH superfamily; its zinc-binding mechanism may differ from canonical ALDH zinc coordination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the protein also binds NAD+ (a co-substrate/cofactor), NAD+ is not among the choices. Among the four options, Zn(2+) is the only metal cofactor consistent with a dehydrogenase bearing Cys/His clusters and lacking Fe-S or B12 signatures. No other option is defensible given the enzyme class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXZ0 (Glutathione-independent formaldehyde dehydrogenase, EC 1.2.1.46, Pseudomonas aeruginosa LESB58) annotates Zn(2+) as the cofactor with experimental evidence code ECO:0000269 (direct assay, PubMed:23989142). The X-ray crystallography reference (PDB 4JLW, 2.70 Å) confirms the protein in complex with NAD and zinc. The annotation states 'Binds 2 Zn(2+) ions per subunit.' Sequence match is exact (399 AA, SHA256 matched in both current and historical records).",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold-like nucleotide-binding motif (GPGSTVYIAGAGPVGL, with GxGxxG spacing) indicating an NAD(P)-dependent dehydrogenase. Aldehyde dehydrogenases classically require Zn(2+) as a catalytic metal. The sequence also contains Cys/His clusters (e.g., 'ACGHCRTCKEQHTG' and 'GHGHSG') consistent with Zn coordination by Cys/His ligands. Distractors can be argued against: [2Fe-2S] requires a tight Cys4 (or 3Cys+1His) motif in specific spacing not clearly present; cob(II)alamin is restricted to radical SAM mutases and isomutases, not dehydrogenases; Fe(2+) is more typical of oxygenases/dioxygenases than NAD-dependent dehydrogenases.",
    "missing_item_specific_fact": "Precise identification of this protein as a formaldehyde dehydrogenase (vs. another dehydrogenase subtype) from sequence alone is non-trivial without database lookup, though the general 'dehydrogenase → Zn2+' heuristic applies broadly.",
    "reason": "A model with general biochemistry knowledge can identify dehydrogenase features (Rossmann fold, Cys/His metal-binding clusters) and apply the well-established rule that aldehyde/alcohol dehydrogenases use Zn2+. The distractors are eliminable by enzyme-class logic (cob(II)alamin for mutases, [2Fe-2S] for ferredoxins with specific Cys4 motifs, Fe2+ for oxygenases). The reasoning chain is not airtight but provides meaningful grounds to prefer D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the protein also binds NAD+ (a co-substrate/cofactor), NAD+ is not among the choices. Among the four options, Zn(2+) is the only metal cofactor consistent with a dehydrogenase bearing Cys/His clusters and lacking Fe-S or B12 signatures. No other option is defensible given the enzyme class."
  },
  "important_caveats": [
    "The UniProt entry was first public on 2025-04-09; the author's source snapshot date is unknown but the sequence matches exactly.",
    "The crystallography evidence (PDB 4JLW) shows zinc in the structure but the paper title emphasizes NAD+ binding; zinc coordination is confirmed by the cofactor annotation and structural reference.",
    "The reasoning pathway (dehydrogenase → Zn2+) is a general heuristic that does not guarantee Zn2+ for every dehydrogenase (e.g., some use FAD or no metal), but it is the strongest prior among the given choices.",
    "The protein is 'glutathione-independent' FALDH, a distinct family from the classic ALDH superfamily; its zinc-binding mechanism may differ from canonical ALDH zinc coordination."
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

**Accession:** `P0DXZ0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.597114+00:00.  

```json
"P0DXZ0"
```

Source SHA-256: `8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.597114+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23989142","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24125754","source":"PubMed"}],"value":"1.2.1.46"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24125754","source":"PubMed"}],"value":"Glutathione-independent formaldehyde dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"FALDH"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"24125754","source":"PubMed"}],"value":"FDH"}]}}
```

Source SHA-256: `8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.597114+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000269","id":"23989142","source":"PubMed"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23989142","source":"PubMed"}],"value":"Binds 2 Zn(2+) ions per subunit."}]}}
```

Source SHA-256: `8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ0.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:58.597114+00:00.  

```json
{"citation":{"authors":["Liao Y.","Chen S.","Wang D.","Zhang W.","Wang S.","Ding J.","Wang Y.","Cai L.","Ran X.","Wang X.","Zhu H."],"citationCrossReferences":[{"database":"PubMed","id":"23989142"},{"database":"DOI","id":"10.1107/s174430911302160x"}],"citationType":"journal article","firstPage":"967","id":"23989142","journal":"Acta Crystallogr. F","lastPage":"972","publicationDate":"2013","title":"Structure of formaldehyde dehydrogenase from Pseudomonas aeruginosa: the binary complex with the cofactor NAD+.","volume":"69"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4JLW","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"LESB58"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) IN COMPLEX WITH NAD AND ZINC","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `8358bc7929b955de7e67b1043a04f43bee60b90cfc3761b786b255991af12c1a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)  
**Locator:** `lines 37-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:03.050160+00:00.  

```text
RN   [3] {ECO:0007744|PDB:4JLW}
RP   X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) IN COMPLEX WITH NAD AND ZINC,
RP   CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.
RC   STRAIN=LESB58;
RX   PubMed=23989142; DOI=10.1107/s174430911302160x;
RA   Liao Y., Chen S., Wang D., Zhang W., Wang S., Ding J., Wang Y., Cai L.,
RA   Ran X., Wang X., Zhu H.;
RT   "Structure of formaldehyde dehydrogenase from Pseudomonas aeruginosa: the
RT   binary complex with the cofactor NAD+.";
RL   Acta Crystallogr. F 69:967-972(2013).
```

Source SHA-256: `f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ0?format=txt&versions=3)  
**Locator:** `lines 62-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:30:03.050160+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000269|PubMed:23989142};
CC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000269|PubMed:23989142};
```

Source SHA-256: `f1ef75a29e458d74a2ad18ea0e1fb01729078531d96bb65f57b769518e4c742e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
