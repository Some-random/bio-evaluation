# GO_molecular_function_0180

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — serine-type peptidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTHRRLLWALCVAALLGVVAAQAGDQQQMQPNEADALRKKWSAVEVVRDLGHIKKDLAKMIELEGAGALSQDELYFYYFRMHDFDNNNKLDGQEMMAAMFHTNHHEEDDEHDGKVPLIIPEQDIASYVDSVLRADKNQDGFISYPELRTSDLTNQI

[Multiple Choices]
A. structural constituent of virion
B. serine-type peptidase activity
C. cellulose synthase (UDP-forming) activity
D. cardiolipin synthase activity
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

> The supplied sequence exactly matches the archived UniProt sequence for longistatin, and that archived entry annotates serine-type peptidase activity with IDA evidence. The entry also reports hydrolysis of serine-protease-specific substrates, supporting choice B for this protein.

Citations as saved: [H8](#evidence-h8), [H10](#evidence-h10), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secretory signal, but the sequence alone does not establish that this unusual protein has serine-type peptidase activity. The other options look poorly matched to a short secreted tick protein, yet that does not specifically demonstrate B.


**Missing item-specific fact**

> The protein-specific experimental finding that longistatin hydrolyzes serine-protease-specific substrates, or an equivalent annotation identifying its serine-type peptidase activity.


**Reason**

> The decisive evidence is experimental characterization of this particular protein, not a general sequence feature that meaningfully distinguishes B from all alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, the sequence-matched experimental annotation supports B; no supplied evidence supports another listed activity.


### Important caveats

- The archived annotation is sequence-matched and records experimental evidence, but the exact source snapshot used by the question author is unknown.
- Longistatin has other reported functions, including calcium binding, which is not among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretory signal, but the sequence alone does not establish that this unusual protein has serine-type peptidase activity. The other options look poorly matched to a short secreted tick protein, yet that does not specifically demonstrate B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental finding that longistatin hydrolyzes serine-protease-specific substrates, or an equivalent annotation identifying its serine-type peptidase activity.",
    "reason": "The decisive evidence is experimental characterization of this particular protein, not a general sequence feature that meaningfully distinguishes B from all alternatives."
  },
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "H8",
      "H10",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived UniProt sequence for longistatin, and that archived entry annotates serine-type peptidase activity with IDA evidence. The entry also reports hydrolysis of serine-protease-specific substrates, supporting choice B for this protein."
  },
  "important_caveats": [
    "The archived annotation is sequence-matched and records experimental evidence, but the exact source snapshot used by the question author is unknown.",
    "Longistatin has other reported functions, including calcium binding, which is not among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the sequence-matched experimental annotation supports B; no supplied evidence supports another listed activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the archived UniProt sequence for longistatin, and that archived entry annotates serine-type peptidase activity with IDA evidence. The entry also reports hydrolysis of serine-protease-specific substrates, supporting choice B for this protein.",
    "evidence_ids": ["H8", "H10", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretory signal, but the sequence alone does not establish that this unusual protein has serine-type peptidase activity. The other options look poorly matched to a short secreted tick protein, yet that does not specifically demonstrate B.",
    "missing_item_specific_fact": "The protein-specific experimental finding that longistatin hydrolyzes serine-protease-specific substrates, or an equivalent annotation identifying its serine-type peptidase activity.",
    "reason": "The decisive evidence is experimental characterization of this particular protein, not a general sequence feature that meaningfully distinguishes B from all alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the sequence-matched experimental annotation supports B; no supplied evidence supports another listed activity."
  },
  "important_caveats": [
    "The archived annotation is sequence-matched and records experimental evidence, but the exact source snapshot used by the question author is unknown.",
    "Longistatin has other reported functions, including calcium binding, which is not among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry D4QD81 (Longistatin) is annotated with GO:0008236 (serine-type peptidase activity) via IDA (Inferred by Direct Assay) evidence, supported by experimental studies (PubMed:22206819, PubMed:23296609). The EC number 3.4.21.- (serine-type peptidase class) is assigned with experimental evidence. The function comment explicitly states it 'Hydrolyzes serine protease-specific substrates' and the reference title confirms it is 'an unconventional serine protease.' The sequence matches exactly (SHA256 confirmed). The GO annotation is backed by direct assay evidence, not mere computational prediction.

Citations as saved: [C7](#evidence-c7), [H10](#evidence-h10), [C4](#evidence-c4), [C5](#evidence-c5), [H8](#evidence-h8), [C11](#evidence-c11), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The three distractors can be eliminated by general biological knowledge about protein size, topology, and domain architecture: (1) Cellulose synthase (UDP-forming) is EC 2.4.1.12, a large multi-pass membrane enzyme typically 800+ residues—impossible for a 156-aa secreted protein with a signal peptide. (2) Cardiolipin synthase is a phosphatidyltransferase, also a membrane-bound enzyme of comparable size—again incompatible with a small secreted protein. (3) Structural constituent of virion applies to viral capsid/matrix proteins; this sequence contains a eukaryotic signal peptide and EF-hand calcium-binding motifs, not viral structural protein features. By elimination, a small secreted protein with enzymatic activity is most consistent with a peptidase. However, the positive identification of 'serine-type' specifically (vs. other protease classes) is NOT derivable from sequence motifs—this protein is explicitly described as 'unconventional' and lacks the canonical GDSGGP catalytic triad motif.


**Missing item-specific fact**

> The specific experimental finding that this unconventional tick salivary protein, despite lacking canonical serine protease motifs, possesses serine-type peptidase activity was established by direct assay (PubMed:22206819) and cannot be inferred from sequence alone.


**Reason**

> The distractors are eliminable through general biological reasoning about protein size, membrane topology, and domain architecture. A 156-aa protein with a signal peptide and EF-hand domains cannot be a cellulose synthase, cardiolipin synthase, or viral structural protein. This leaves a peptidase as the only plausible enzymatic function among the choices. However, the positive assignment of 'serine-type' specifically relies on experimental characterization of this particular protein's unconventional catalytic mechanism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly incompatible with a 156-aa secreted protein (both are large membrane enzymes). Option A applies to viral structural proteins, while this sequence has eukaryotic secretory features. Only B remains viable by elimination. The GO annotation also includes calcium ion binding (GO:0005509), but that is not among the choices, so no ambiguity arises from the provided options.


### Important caveats

- The protein is explicitly described as an 'unconventional serine protease'—it lacks the canonical serine protease catalytic triad sequence motifs visible in the primary structure. The serine-type peptidase classification was established experimentally, not by sequence homology.
- The most prominent sequence features are EF-hand calcium-binding domains, which would more naturally suggest 'calcium ion binding' (GO:0005509, also annotated) as the primary molecular function. The peptidase activity is a secondary, experimentally-discovered function.
- The GO annotation for serine-type peptidase activity uses IDA (direct assay) evidence codes (ECO:0000314), confirming experimental basis rather than computational inference.
- The answer is reachable by elimination of clearly incompatible distractors, but positive identification of 'serine-type peptidase' from sequence alone would not be possible for this unconventional protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The three distractors can be eliminated by general biological knowledge about protein size, topology, and domain architecture: (1) Cellulose synthase (UDP-forming) is EC 2.4.1.12, a large multi-pass membrane enzyme typically 800+ residues—impossible for a 156-aa secreted protein with a signal peptide. (2) Cardiolipin synthase is a phosphatidyltransferase, also a membrane-bound enzyme of comparable size—again incompatible with a small secreted protein. (3) Structural constituent of virion applies to viral capsid/matrix proteins; this sequence contains a eukaryotic signal peptide and EF-hand calcium-binding motifs, not viral structural protein features. By elimination, a small secreted protein with enzymatic activity is most consistent with a peptidase. However, the positive identification of 'serine-type' specifically (vs. other protease classes) is NOT derivable from sequence motifs—this protein is explicitly described as 'unconventional' and lacks the canonical GDSGGP catalytic triad motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific experimental finding that this unconventional tick salivary protein, despite lacking canonical serine protease motifs, possesses serine-type peptidase activity was established by direct assay (PubMed:22206819) and cannot be inferred from sequence alone.",
    "reason": "The distractors are eliminable through general biological reasoning about protein size, membrane topology, and domain architecture. A 156-aa protein with a signal peptide and EF-hand domains cannot be a cellulose synthase, cardiolipin synthase, or viral structural protein. This leaves a peptidase as the only plausible enzymatic function among the choices. However, the positive assignment of 'serine-type' specifically relies on experimental characterization of this particular protein's unconventional catalytic mechanism."
  },
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H10",
      "C4",
      "C5",
      "H8",
      "C11",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry D4QD81 (Longistatin) is annotated with GO:0008236 (serine-type peptidase activity) via IDA (Inferred by Direct Assay) evidence, supported by experimental studies (PubMed:22206819, PubMed:23296609). The EC number 3.4.21.- (serine-type peptidase class) is assigned with experimental evidence. The function comment explicitly states it 'Hydrolyzes serine protease-specific substrates' and the reference title confirms it is 'an unconventional serine protease.' The sequence matches exactly (SHA256 confirmed). The GO annotation is backed by direct assay evidence, not mere computational prediction."
  },
  "important_caveats": [
    "The protein is explicitly described as an 'unconventional serine protease'—it lacks the canonical serine protease catalytic triad sequence motifs visible in the primary structure. The serine-type peptidase classification was established experimentally, not by sequence homology.",
    "The most prominent sequence features are EF-hand calcium-binding domains, which would more naturally suggest 'calcium ion binding' (GO:0005509, also annotated) as the primary molecular function. The peptidase activity is a secondary, experimentally-discovered function.",
    "The GO annotation for serine-type peptidase activity uses IDA (direct assay) evidence codes (ECO:0000314), confirming experimental basis rather than computational inference.",
    "The answer is reachable by elimination of clearly incompatible distractors, but positive identification of 'serine-type peptidase' from sequence alone would not be possible for this unconventional protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with a 156-aa secreted protein (both are large membrane enzymes). Option A applies to viral structural proteins, while this sequence has eukaryotic secretory features. Only B remains viable by elimination. The GO annotation also includes calcium ion binding (GO:0005509), but that is not among the choices, so no ambiguity arises from the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry D4QD81 (Longistatin) is annotated with GO:0008236 (serine-type peptidase activity) via IDA (Inferred by Direct Assay) evidence, supported by experimental studies (PubMed:22206819, PubMed:23296609). The EC number 3.4.21.- (serine-type peptidase class) is assigned with experimental evidence. The function comment explicitly states it 'Hydrolyzes serine protease-specific substrates' and the reference title confirms it is 'an unconventional serine protease.' The sequence matches exactly (SHA256 confirmed). The GO annotation is backed by direct assay evidence, not mere computational prediction.",
    "evidence_ids": ["C7", "H10", "C4", "C5", "H8", "C11", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The three distractors can be eliminated by general biological knowledge about protein size, topology, and domain architecture: (1) Cellulose synthase (UDP-forming) is EC 2.4.1.12, a large multi-pass membrane enzyme typically 800+ residues—impossible for a 156-aa secreted protein with a signal peptide. (2) Cardiolipin synthase is a phosphatidyltransferase, also a membrane-bound enzyme of comparable size—again incompatible with a small secreted protein. (3) Structural constituent of virion applies to viral capsid/matrix proteins; this sequence contains a eukaryotic signal peptide and EF-hand calcium-binding motifs, not viral structural protein features. By elimination, a small secreted protein with enzymatic activity is most consistent with a peptidase. However, the positive identification of 'serine-type' specifically (vs. other protease classes) is NOT derivable from sequence motifs—this protein is explicitly described as 'unconventional' and lacks the canonical GDSGGP catalytic triad motif.",
    "missing_item_specific_fact": "The specific experimental finding that this unconventional tick salivary protein, despite lacking canonical serine protease motifs, possesses serine-type peptidase activity was established by direct assay (PubMed:22206819) and cannot be inferred from sequence alone.",
    "reason": "The distractors are eliminable through general biological reasoning about protein size, membrane topology, and domain architecture. A 156-aa protein with a signal peptide and EF-hand domains cannot be a cellulose synthase, cardiolipin synthase, or viral structural protein. This leaves a peptidase as the only plausible enzymatic function among the choices. However, the positive assignment of 'serine-type' specifically relies on experimental characterization of this particular protein's unconventional catalytic mechanism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with a 156-aa secreted protein (both are large membrane enzymes). Option A applies to viral structural proteins, while this sequence has eukaryotic secretory features. Only B remains viable by elimination. The GO annotation also includes calcium ion binding (GO:0005509), but that is not among the choices, so no ambiguity arises from the provided options."
  },
  "important_caveats": [
    "The protein is explicitly described as an 'unconventional serine protease'—it lacks the canonical serine protease catalytic triad sequence motifs visible in the primary structure. The serine-type peptidase classification was established experimentally, not by sequence homology.",
    "The most prominent sequence features are EF-hand calcium-binding domains, which would more naturally suggest 'calcium ion binding' (GO:0005509, also annotated) as the primary molecular function. The peptidase activity is a secondary, experimentally-discovered function.",
    "The GO annotation for serine-type peptidase activity uses IDA (direct assay) evidence codes (ECO:0000314), confirming experimental basis rather than computational inference.",
    "The answer is reachable by elimination of clearly incompatible distractors, but positive identification of 'serine-type peptidase' from sequence alone would not be possible for this unconventional protein."
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

**Accession:** `D4QD81` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.409363+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22206819","source":"PubMed"}],"value":"3.4.21.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"19968997","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"21423674","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"21925150","source":"PubMed"}],"value":"Longistatin"}}}
```

Source SHA-256: `27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.409363+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"19968997","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21423674","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21925150","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"22206819","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"23296609","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"25401185","source":"PubMed"}],"value":"Anticoagulant and fibrinolytic protease that modulates blood feeding of ticks on vertebrate hosts (PubMed:21423674). Degrades host fibrinogen and delays fibrin clot formation (PubMed:21423674). Promotes lysis of fibrin clots in the host by activating host plasminogen in the presence of soluble fibrin (PubMed:21423674, PubMed:21925150). Binds Ca(2+) (PubMed:19968997, PubMed:23296609). Hydrolyzes serine protease-specific substrates (PubMed:22206819). Required for the formation of a blood pool, an accumulation of blood and tissue fluid developed at the tick's feeding site (PubMed:21423674). Blocks activation of host AGER/RAGE (PubMed:25401185). Reduces AGER/RAGE-dependent production of reactive oxygen species (ROS) in human endothelial cells (PubMed:25401185). Prevents AGER/RAGE-dependent activation of NF-kappa-B and suppresses expression of adhesion molecules, such as VCAM1, ICAM1 and SELE, and secretion of cytokines, such as CSF3/GCSF and TGF-beta, in human endothelial cells (PubMed:25401185). Suppresses RAGE/AGER-mediated migration of mouse peritoneal resident cells (PubMed:25401185). Reduces AGER/RAGE-mediated inflammation in mice tissues (PubMed:25401185)"}]}
```

Source SHA-256: `27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.409363+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"22206819","source":"PubMed"}],"id":"GO:0008236","properties":[{"key":"GoTerm","value":"F:serine-type peptidase activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D4QD81.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.409363+00:00.  

```json
{"citation":{"authors":["Anisuzzaman X.","Islam M.K.","Alim M.A.","Miyoshi T.","Hatta T.","Yamaji K.","Matsumoto Y.","Fujisaki K.","Tsuji N."],"citationCrossReferences":[{"database":"PubMed","id":"22206819"},{"database":"DOI","id":"10.1016/j.molbiopara.2011.12.002"}],"citationType":"journal article","firstPage":"45","id":"22206819","journal":"Mol. Biochem. Parasitol.","lastPage":"53","publicationDate":"2012","title":"Longistatin is an unconventional serine protease and induces protective immunity against tick infestation.","volume":"182"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","TISSUE SPECIFICITY"]}
```

Source SHA-256: `27d5a24c10550956afab284439c23ad93d6c94ed57b9a87ce791ea4e4597d0dd`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)  
**Locator:** `lines 41-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:28:00.036900+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, AND TISSUE SPECIFICITY.
RX   PubMed=22206819; DOI=10.1016/j.molbiopara.2011.12.002;
RA   Anisuzzaman X., Islam M.K., Alim M.A., Miyoshi T., Hatta T., Yamaji K.,
RA   Matsumoto Y., Fujisaki K., Tsuji N.;
RT   "Longistatin is an unconventional serine protease and induces protective
RT   immunity against tick infestation.";
RL   Mol. Biochem. Parasitol. 182:45-53(2012).
```

Source SHA-256: `33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)  
**Locator:** `lines 66-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:28:00.036900+00:00.  

```text
CC   -!- FUNCTION: Anticoagulant and fibrinolytic protease that modulates blood
CC       feeding of ticks on vertebrate hosts (PubMed:21423674). Degrades host
CC       fibrinogen and delays fibrin clot formation (PubMed:21423674). Promotes
CC       lysis of fibrin clots in the host by activating host plasminogen in the
CC       presence of soluble fibrin (PubMed:21423674, PubMed:21925150). Binds
CC       Ca(2+) (PubMed:19968997, PubMed:23296609). Hydrolyzes serine protease-
CC       specific substrates (PubMed:22206819). Required for the formation of a
CC       blood pool, an accumulation of blood and tissue fluid developed at the
CC       tick's feeding site (PubMed:21423674). Blocks activation of host
CC       AGER/RAGE (PubMed:25401185). Reduces AGER/RAGE-dependent production of
CC       reactive oxygen species (ROS) in human endothelial cells
CC       (PubMed:25401185). Prevents AGER/RAGE-dependent activation of NF-kappa-
CC       B and suppresses expression of adhesion molecules, such as VCAM1, ICAM1
CC       and SELE, and secretion of cytokines, such as CSF3/GCSF and TGF-beta,
CC       in human endothelial cells (PubMed:25401185). Suppresses RAGE/AGER-
CC       mediated migration of mouse peritoneal resident cells
CC       (PubMed:25401185). Reduces AGER/RAGE-mediated inflammation in mice
CC       tissues (PubMed:25401185). {ECO:0000269|PubMed:19968997,
CC       ECO:0000269|PubMed:21423674, ECO:0000269|PubMed:21925150,
CC       ECO:0000269|PubMed:22206819, ECO:0000269|PubMed:23296609,
CC       ECO:0000269|PubMed:25401185}.
```

Source SHA-256: `33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D4QD81?format=txt&versions=31)  
**Locator:** `lines 141-141`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-01T06:28:00.036900+00:00.  

```text
DR   GO; GO:0008236; F:serine-type peptidase activity; IDA:UniProtKB.
```

Source SHA-256: `33d72b54de397540314c319d5d65281dcef13ef22f478476c602e399ba6c861a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 180. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
