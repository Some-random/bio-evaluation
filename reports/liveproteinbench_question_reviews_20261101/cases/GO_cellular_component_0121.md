# GO_cellular_component_0121

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MALKLVYGVFTLALLGISSVNADCSLKIPESVENEKTPVIMVRKSLKTFEYDLFQPTGEVTNFPERTELLLACTGAQNYFKNGEESVTLMCHNNEFDDGQGNGLDLFTCVKTPTAELRKTKERCSLGDLYVYDVVFRISEEELVGPVYDICYNEYSQKPAYSRNIINGAAVNYRVPESETDLTVSLAKDFTTRDVNNYFKLENQKQRFQGYTIDGKPLVDDKNFFAPGQLAPDTSMITPADKLSTYDYANIVPQYKTVYDGNVWRVENITRDLAVNRQAKFEVYTGGYERLTALHNGKEEEIFLSAKKYVHEIPKYIYKFVVDKENDAGIVFFTLNNPHVKNVKGTEFCKNQCEEANVLDSNFKDWTQGYTFCCTWNNVKDYVRALPQDIEINNLLKFN

[Multiple Choices]
A. egg chorion
B. nucleus
C. mitochondrial [2Fe-2S] assembly complex
D. ADA complex
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

### Expected-answer support: contradicted

> The exact-matching historical record describes the protein as secreted and has an extracellular-region annotation with IDA evidence. Its nucleus annotation is only IEA:TreeGrafter, a computational inference, so the evidence does not support nucleus as the primary location.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a signal peptide and secretion, which argues against nuclear, mitochondrial-complex, or ADA-complex residence. But secretion does not establish that the protein is an egg-chorion component.


**Missing item-specific fact**

> The protein-specific fact that this sequence is the tsetse salivary protein Tsal1, reported as secreted; no listed option is extracellular or secreted.


**Reason**

> Sequence features suggest secretion, but do not identify an egg-chorion role or support any listed intracellular complex. Distinguishing a listed choice would require protein-specific information absent from the prompt.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports secretion/extracellular location, which is not among the choices. The sequence’s signal-peptide-like region does not make egg chorion a defensible specific assignment.


### Important caveats

- The sequence matches the cited UniProt record, but the accession was inferred from reviewer-only metadata and was not supplied to the evaluated model.
- The extracellular IDA annotation cites a publication; the primary paper was not independently reviewed here.
- The record also contains a nuclear annotation, but it is computationally inferred and does not outweigh the cited secreted/extracellular evidence for the primary-location claim.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a signal peptide and secretion, which argues against nuclear, mitochondrial-complex, or ADA-complex residence. But secretion does not establish that the protein is an egg-chorion component.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is the tsetse salivary protein Tsal1, reported as secreted; no listed option is extracellular or secreted.",
    "reason": "Sequence features suggest secretion, but do not identify an egg-chorion role or support any listed intracellular complex. Distinguishing a listed choice would require protein-specific information absent from the prompt."
  },
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The exact-matching historical record describes the protein as secreted and has an extracellular-region annotation with IDA evidence. Its nucleus annotation is only IEA:TreeGrafter, a computational inference, so the evidence does not support nucleus as the primary location."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the accession was inferred from reviewer-only metadata and was not supplied to the evaluated model.",
    "The extracellular IDA annotation cites a publication; the primary paper was not independently reviewed here.",
    "The record also contains a nuclear annotation, but it is computationally inferred and does not outweigh the cited secreted/extracellular evidence for the primary-location claim."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports secretion/extracellular location, which is not among the choices. The sequence’s signal-peptide-like region does not make egg chorion a defensible specific assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The exact-matching historical record describes the protein as secreted and has an extracellular-region annotation with IDA evidence. Its nucleus annotation is only IEA:TreeGrafter, a computational inference, so the evidence does not support nucleus as the primary location.",
    "evidence_ids": ["H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a signal peptide and secretion, which argues against nuclear, mitochondrial-complex, or ADA-complex residence. But secretion does not establish that the protein is an egg-chorion component.",
    "missing_item_specific_fact": "The protein-specific fact that this sequence is the tsetse salivary protein Tsal1, reported as secreted; no listed option is extracellular or secreted.",
    "reason": "Sequence features suggest secretion, but do not identify an egg-chorion role or support any listed intracellular complex. Distinguishing a listed choice would require protein-specific information absent from the prompt."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports secretion/extracellular location, which is not among the choices. The sequence’s signal-peptide-like region does not make egg chorion a defensible specific assignment."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the accession was inferred from reviewer-only metadata and was not supplied to the evaluated model.",
    "The extracellular IDA annotation cites a publication; the primary paper was not independently reviewed here.",
    "The record also contains a nuclear annotation, but it is computationally inferred and does not outweigh the cited secreted/extracellular evidence for the primary-location claim."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein D3TS87 is 'Salivary protein Tsal1' from Glossina morsitans morsitans. UniProt explicitly annotates its subcellular location as 'Secreted' with experimental evidence (ECO:0000305|PubMed:23110062), and the GO annotation for extracellular region (GO:0005576) carries an IDA:UniProtKB evidence code. The 'nucleus' annotation (GO:0005634) is only IEA:TreeGrafter — a purely computational homology-based prediction. The N-terminal sequence MALKLVYGVFTLALLGISSVNAD is a classic hydrophobic signal peptide consistent with the secretory pathway, not nuclear import. The author's key of 'nucleus' is contradicted by the experimental subcellular location annotation and the protein's identity as a secreted salivary gland protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch (MALKLVYGVFTLALLGISSVNAD) is a canonical signal peptide indicating entry into the secretory pathway, which would lead a reasoning model to conclude the protein is secreted/extracellular. However, 'extracellular region' or 'secreted' is not among the four options. No biological reasoning from the sequence supports 'nucleus' — the protein lacks a nuclear localization signal, and the signal peptide argues against nuclear retention. The author's selection of 'nucleus' appears to rest on the mere presence of a GO:0005634 IEA:TreeGrafter annotation in the database, without regard to evidence strength.


**Missing item-specific fact**

> The correct cellular component (extracellular region / secreted) is absent from the option set. The author's key was apparently derived from a weak computational annotation (IEA:TreeGrafter) rather than the experimentally supported location, making the 'correct' answer identifiable only by knowing which specific GO term was recorded in the database entry, not by reasoning from the sequence.


**Reason**

> No sequence-based reasoning distinguishes 'nucleus' from the other three options for a protein with a clear signal peptide. The author's answer depends on selecting a specific database annotation (GO:0005634, IEA:TreeGrafter) while ignoring the stronger experimental annotation (GO:0005576, IDA:UniProtKB) and the 'Secreted' subcellular location comment. This is a lookup of a particular annotation rather than a reasoning task.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the four options (egg chorion, nucleus, mitochondrial &#91;2Fe-2S&#93; assembly complex, ADA complex) correctly describe the location of a secreted salivary gland protein. The correct answer — extracellular region or secreted — is absent from the choices. The question is defective because no option is scientifically correct, and the author's key ('nucleus') is contradicted by experimental evidence. All four options are equally wrong for this protein, though 'nucleus' is the most directly contradicted by the IDA-level annotation.


### Important caveats

- The 'nucleus' GO annotation exists in the database but is IEA:TreeGrafter (computational prediction by homology), not experimental. The experimentally supported location is 'Secreted' (IDA-level evidence).
- The protein's actual function (high-affinity nucleic acid binding with residual nuclease activity) occurs extracellularly in saliva during tsetse fly feeding, not in the nucleus.
- The correct cellular component (extracellular region, GO:0005576) is not offered as an option, making the question fundamentally flawed regardless of which option is designated as correct.
- The identity of the protein (D3TS87, Tsal1) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MALKLVYGVFTLALLGISSVNAD) is a canonical signal peptide indicating entry into the secretory pathway, which would lead a reasoning model to conclude the protein is secreted/extracellular. However, 'extracellular region' or 'secreted' is not among the four options. No biological reasoning from the sequence supports 'nucleus' — the protein lacks a nuclear localization signal, and the signal peptide argues against nuclear retention. The author's selection of 'nucleus' appears to rest on the mere presence of a GO:0005634 IEA:TreeGrafter annotation in the database, without regard to evidence strength.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The correct cellular component (extracellular region / secreted) is absent from the option set. The author's key was apparently derived from a weak computational annotation (IEA:TreeGrafter) rather than the experimentally supported location, making the 'correct' answer identifiable only by knowing which specific GO term was recorded in the database entry, not by reasoning from the sequence.",
    "reason": "No sequence-based reasoning distinguishes 'nucleus' from the other three options for a protein with a clear signal peptide. The author's answer depends on selecting a specific database annotation (GO:0005634, IEA:TreeGrafter) while ignoring the stronger experimental annotation (GO:0005576, IDA:UniProtKB) and the 'Secreted' subcellular location comment. This is a lookup of a particular annotation rather than a reasoning task."
  },
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The protein D3TS87 is 'Salivary protein Tsal1' from Glossina morsitans morsitans. UniProt explicitly annotates its subcellular location as 'Secreted' with experimental evidence (ECO:0000305|PubMed:23110062), and the GO annotation for extracellular region (GO:0005576) carries an IDA:UniProtKB evidence code. The 'nucleus' annotation (GO:0005634) is only IEA:TreeGrafter — a purely computational homology-based prediction. The N-terminal sequence MALKLVYGVFTLALLGISSVNAD is a classic hydrophobic signal peptide consistent with the secretory pathway, not nuclear import. The author's key of 'nucleus' is contradicted by the experimental subcellular location annotation and the protein's identity as a secreted salivary gland protein."
  },
  "important_caveats": [
    "The 'nucleus' GO annotation exists in the database but is IEA:TreeGrafter (computational prediction by homology), not experimental. The experimentally supported location is 'Secreted' (IDA-level evidence).",
    "The protein's actual function (high-affinity nucleic acid binding with residual nuclease activity) occurs extracellularly in saliva during tsetse fly feeding, not in the nucleus.",
    "The correct cellular component (extracellular region, GO:0005576) is not offered as an option, making the question fundamentally flawed regardless of which option is designated as correct.",
    "The identity of the protein (D3TS87, Tsal1) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options (egg chorion, nucleus, mitochondrial [2Fe-2S] assembly complex, ADA complex) correctly describe the location of a secreted salivary gland protein. The correct answer — extracellular region or secreted — is absent from the choices. The question is defective because no option is scientifically correct, and the author's key ('nucleus') is contradicted by experimental evidence. All four options are equally wrong for this protein, though 'nucleus' is the most directly contradicted by the IDA-level annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0121",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein D3TS87 is 'Salivary protein Tsal1' from Glossina morsitans morsitans. UniProt explicitly annotates its subcellular location as 'Secreted' with experimental evidence (ECO:0000305|PubMed:23110062), and the GO annotation for extracellular region (GO:0005576) carries an IDA:UniProtKB evidence code. The 'nucleus' annotation (GO:0005634) is only IEA:TreeGrafter — a purely computational homology-based prediction. The N-terminal sequence MALKLVYGVFTLALLGISSVNAD is a classic hydrophobic signal peptide consistent with the secretory pathway, not nuclear import. The author's key of 'nucleus' is contradicted by the experimental subcellular location annotation and the protein's identity as a secreted salivary gland protein.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MALKLVYGVFTLALLGISSVNAD) is a canonical signal peptide indicating entry into the secretory pathway, which would lead a reasoning model to conclude the protein is secreted/extracellular. However, 'extracellular region' or 'secreted' is not among the four options. No biological reasoning from the sequence supports 'nucleus' — the protein lacks a nuclear localization signal, and the signal peptide argues against nuclear retention. The author's selection of 'nucleus' appears to rest on the mere presence of a GO:0005634 IEA:TreeGrafter annotation in the database, without regard to evidence strength.",
    "missing_item_specific_fact": "The correct cellular component (extracellular region / secreted) is absent from the option set. The author's key was apparently derived from a weak computational annotation (IEA:TreeGrafter) rather than the experimentally supported location, making the 'correct' answer identifiable only by knowing which specific GO term was recorded in the database entry, not by reasoning from the sequence.",
    "reason": "No sequence-based reasoning distinguishes 'nucleus' from the other three options for a protein with a clear signal peptide. The author's answer depends on selecting a specific database annotation (GO:0005634, IEA:TreeGrafter) while ignoring the stronger experimental annotation (GO:0005576, IDA:UniProtKB) and the 'Secreted' subcellular location comment. This is a lookup of a particular annotation rather than a reasoning task."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options (egg chorion, nucleus, mitochondrial [2Fe-2S] assembly complex, ADA complex) correctly describe the location of a secreted salivary gland protein. The correct answer — extracellular region or secreted — is absent from the choices. The question is defective because no option is scientifically correct, and the author's key ('nucleus') is contradicted by experimental evidence. All four options are equally wrong for this protein, though 'nucleus' is the most directly contradicted by the IDA-level annotation."
  },
  "important_caveats": [
    "The 'nucleus' GO annotation exists in the database but is IEA:TreeGrafter (computational prediction by homology), not experimental. The experimentally supported location is 'Secreted' (IDA-level evidence).",
    "The protein's actual function (high-affinity nucleic acid binding with residual nuclease activity) occurs extracellularly in saliva during tsetse fly feeding, not in the nucleus.",
    "The correct cellular component (extracellular region, GO:0005576) is not offered as an option, making the question fundamentally flawed regardless of which option is designated as correct.",
    "The identity of the protein (D3TS87, Tsal1) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `historical_location_conflict_traced`.

> The exact-sequence historical source H3 says secreted, H4 assigns extracellular region IDA, and H6 assigns nucleus IEA:TreeGrafter.

**Remaining uncertainty:** The claim is anchored in the exact-match historical source; preserve current-source availability/match limitations and unknown author snapshot.

Evidence checked: [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `D3TS87` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.191362+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23110062","source":"PubMed"}],"value":"3.1.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Salivary protein Tsal1"}}}
```

Source SHA-256: `3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.191362+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"23110062","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}}]}
```

Source SHA-256: `3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.191362+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"23110062","source":"PubMed"}],"id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.191362+00:00.  

```json
{"database":"GO","id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)  
**Locator:** `lines 62-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-01T06:27:59.125691+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:23110062}.
```

Source SHA-256: `fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)  
**Locator:** `lines 79-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-01T06:27:59.125691+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IDA:UniProtKB.
```

Source SHA-256: `fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)  
**Locator:** `lines 81-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-01T06:27:59.125691+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; IEA:TreeGrafter.
```

Source SHA-256: `fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 121. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
