# GO_cellular_component_0134

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — endoplasmic reticulum

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVSTNAGGIASKQASSMAPNPGKATILALGHAFPQQLVMQDYVVDGFMRNTNCDDPELKEKLTRLCKTTTVKTRYVVMSEEILKSYPELAQEGQPTMKQRLDISNKAVTQMATEASLACVRSWGGALSEITHLVYVSSSEARFPGGDLHLARALGLSPDVRRVMLAFTGCSGGVAGLRVAKGLAESCPGARVLLATSETTIVGFRPPSPDRPYDLVGVALFGDGAGAAVVGADPTPVERPLFELHSALQRFLPDTDKTIDGRLTEEGIKFQLGRELPHIIEANVEAFCQKLMQEHPQAADKLTYGDMFWAVHPGGPAILTKMEGRLGLDGGKLRASRSALRDFGNASSNTIVYVLENMVEETRQRREEAAEEEDCEWGLILAFGPGITFEGILARNLQARARARD

[Multiple Choices]
A. actin cytoskeleton
B. site of double-strand break
C. endoplasmic reticulum
D. vesicle
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

> The supplied sequence exactly matches the rice protein entry Q8H305. Its archived UniProt record annotates it to the endoplasmic reticulum with ECO:0000269 evidence, and records a GO cellular-component annotation with IDA evidence. This supports choice C, though the cited primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble enzyme and lacks an obvious conventional transmembrane segment or N-terminal secretion signal, but those features do not distinguish ER localization from other listed locations.


**Missing item-specific fact**

> The protein-specific experimental localization of this rice polyketide synthase to the endoplasmic reticulum.


**Reason**

> The matching annotation supports the key, but that protein-specific localization fact is absent from the question. General sequence reasoning does not establish the precise compartment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only sequence-matched annotation supports the endoplasmic reticulum choice; the input alone does not provide enough evidence to establish another option.


### Important caveats

- The UniProt annotation cites experimental evidence, but the cited primary study was not independently validated here.
- The author’s exact source snapshot is unknown, although the historical record available by the repository cutoff contains the same localization annotation and matching sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme and lacks an obvious conventional transmembrane segment or N-terminal secretion signal, but those features do not distinguish ER localization from other listed locations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental localization of this rice polyketide synthase to the endoplasmic reticulum.",
    "reason": "The matching annotation supports the key, but that protein-specific localization fact is absent from the question. General sequence reasoning does not establish the precise compartment."
  },
  "case_id": "GO_cellular_component_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rice protein entry Q8H305. Its archived UniProt record annotates it to the endoplasmic reticulum with ECO:0000269 evidence, and records a GO cellular-component annotation with IDA evidence. This supports choice C, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the cited primary study was not independently validated here.",
    "The author’s exact source snapshot is unknown, although the historical record available by the repository cutoff contains the same localization annotation and matching sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports the endoplasmic reticulum choice; the input alone does not provide enough evidence to establish another option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the rice protein entry Q8H305. Its archived UniProt record annotates it to the endoplasmic reticulum with ECO:0000269 evidence, and records a GO cellular-component annotation with IDA evidence. This supports choice C, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme and lacks an obvious conventional transmembrane segment or N-terminal secretion signal, but those features do not distinguish ER localization from other listed locations.",
    "missing_item_specific_fact": "The protein-specific experimental localization of this rice polyketide synthase to the endoplasmic reticulum.",
    "reason": "The matching annotation supports the key, but that protein-specific localization fact is absent from the question. General sequence reasoning does not establish the precise compartment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only sequence-matched annotation supports the endoplasmic reticulum choice; the input alone does not provide enough evidence to establish another option."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the cited primary study was not independently validated here.",
    "The author’s exact source snapshot is unknown, although the historical record available by the repository cutoff contains the same localization annotation and matching sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8H305 (PKS10_ORYSJ, OsPKS2/OsPKS10, a Type III polyketide synthase from rice) carries an explicit experimental subcellular localization annotation: 'Endoplasmic reticulum {ECO:0000269|PubMed:29411094}' (evidence C5, H5), corresponding to GO:0005783 with IDA evidence code (C6, H6). The reference (Zou et al. 2018, Plant Cell Rep.) reports SUBCELLULAR LOCATION as a primary finding, indicating direct experimental determination (e.g., fluorescent protein tagging). The benchmark sequence matches the UniProt entry exactly (405 AA, SHA256 confirmed). The expected answer 'endoplasmic reticulum' is directly supported by experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6), [C9](#evidence-c9), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains type III polyketide synthase (chalcone synthase family) motifs (e.g., GCSGGVAGLRVAKG, GPG near C-terminus), which are classically cytoplasmic soluble enzymes in plants. None of the four options is 'cytoplasm/cytosol.' One can eliminate actin cytoskeleton (no actin-binding domains) and site of double-strand break (no DNA repair motifs) by general knowledge. However, distinguishing ER from vesicle among the remaining two membrane-compartment options requires knowing that pollen exine/Ubisch body lipid biosynthesis occurs at the ER—a functional-context fact not encoded in the sequence. The sequence lacks any obvious ER-targeting signal peptide, transmembrane anchor, or KDEL/HDEL retrieval motif that would predict ER localization from sequence alone.


**Missing item-specific fact**

> The experimentally determined ER localization of OsPKS2/PKS10 (Q8H305), established by fluorescent-protein co-localization in the 2018 Zou et al. study, is a protein-specific finding. Type III PKS enzymes are canonically cytoplasmic; this particular enzyme's ER association is a non-obvious, experimentally discovered property not inferable from sequence features.


**Reason**

> The sequence is a typical type III PKS with no visible ER-targeting signals, TM domains, or retrieval motifs. Eliminating options A and B is straightforward, but choosing C (ER) over D (vesicle) requires the specific experimental finding that this OsPKS localizes to the ER during pollen wall biosynthesis—a fact absent from the sequence and not predictable by general enzymology or sequence heuristics.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (actin cytoskeleton) and B (site of double-strand break) are clearly inappropriate for a polyketide synthase with no cytoskeletal or DNA-repair domains. Between C (ER) and D (vesicle), the ER is the experimentally verified location, and a lipid-biosynthesis enzyme is more logically associated with the ER (site of lipid synthesis) than with a generic vesicle. While the sequence alone does not strongly favor ER over vesicle, the ER is the only option with direct experimental support.


### Important caveats

- The ER localization of OsPKS2 is experimentally determined (ECO:0000269, IDA) but is a surprising finding for a type III PKS, which are typically cytoplasmic. This makes the question less amenable to sequence-based reasoning.
- The UniProt entry was first public in April 2025; the benchmark construction date is unknown, but the sequence and annotation are consistent across historical and current snapshots.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely solely on the 405-aa sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains type III polyketide synthase (chalcone synthase family) motifs (e.g., GCSGGVAGLRVAKG, GPG near C-terminus), which are classically cytoplasmic soluble enzymes in plants. None of the four options is 'cytoplasm/cytosol.' One can eliminate actin cytoskeleton (no actin-binding domains) and site of double-strand break (no DNA repair motifs) by general knowledge. However, distinguishing ER from vesicle among the remaining two membrane-compartment options requires knowing that pollen exine/Ubisch body lipid biosynthesis occurs at the ER—a functional-context fact not encoded in the sequence. The sequence lacks any obvious ER-targeting signal peptide, transmembrane anchor, or KDEL/HDEL retrieval motif that would predict ER localization from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimentally determined ER localization of OsPKS2/PKS10 (Q8H305), established by fluorescent-protein co-localization in the 2018 Zou et al. study, is a protein-specific finding. Type III PKS enzymes are canonically cytoplasmic; this particular enzyme's ER association is a non-obvious, experimentally discovered property not inferable from sequence features.",
    "reason": "The sequence is a typical type III PKS with no visible ER-targeting signals, TM domains, or retrieval motifs. Eliminating options A and B is straightforward, but choosing C (ER) over D (vesicle) requires the specific experimental finding that this OsPKS localizes to the ER during pollen wall biosynthesis—a fact absent from the sequence and not predictable by general enzymology or sequence heuristics."
  },
  "case_id": "GO_cellular_component_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6",
      "C9",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8H305 (PKS10_ORYSJ, OsPKS2/OsPKS10, a Type III polyketide synthase from rice) carries an explicit experimental subcellular localization annotation: 'Endoplasmic reticulum {ECO:0000269|PubMed:29411094}' (evidence C5, H5), corresponding to GO:0005783 with IDA evidence code (C6, H6). The reference (Zou et al. 2018, Plant Cell Rep.) reports SUBCELLULAR LOCATION as a primary finding, indicating direct experimental determination (e.g., fluorescent protein tagging). The benchmark sequence matches the UniProt entry exactly (405 AA, SHA256 confirmed). The expected answer 'endoplasmic reticulum' is directly supported by experimental evidence."
  },
  "important_caveats": [
    "The ER localization of OsPKS2 is experimentally determined (ECO:0000269, IDA) but is a surprising finding for a type III PKS, which are typically cytoplasmic. This makes the question less amenable to sequence-based reasoning.",
    "The UniProt entry was first public in April 2025; the benchmark construction date is unknown, but the sequence and annotation are consistent across historical and current snapshots.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely solely on the 405-aa sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (actin cytoskeleton) and B (site of double-strand break) are clearly inappropriate for a polyketide synthase with no cytoskeletal or DNA-repair domains. Between C (ER) and D (vesicle), the ER is the experimentally verified location, and a lipid-biosynthesis enzyme is more logically associated with the ER (site of lipid synthesis) than with a generic vesicle. While the sequence alone does not strongly favor ER over vesicle, the ER is the only option with direct experimental support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"GO_cellular_component_0134","expected_answer_check":{"judgment":"supported","reason":"UniProt entry Q8H305 (PKS10_ORYSJ, OsPKS2/OsPKS10, a Type III polyketide synthase from rice) carries an explicit experimental subcellular localization annotation: 'Endoplasmic reticulum {ECO:0000269|PubMed:29411094}' (evidence C5, H5), corresponding to GO:0005783 with IDA evidence code (C6, H6). The reference (Zou et al. 2018, Plant Cell Rep.) reports SUBCELLULAR LOCATION as a primary finding, indicating direct experimental determination (e.g., fluorescent protein tagging). The benchmark sequence matches the UniProt entry exactly (405 AA, SHA256 confirmed). The expected answer 'endoplasmic reticulum' is directly supported by experimental evidence.","evidence_ids":["C5","C6","H5","H6","C9","H4"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"The sequence contains type III polyketide synthase (chalcone synthase family) motifs (e.g., GCSGGVAGLRVAKG, GPG near C-terminus), which are classically cytoplasmic soluble enzymes in plants. None of the four options is 'cytoplasm/cytosol.' One can eliminate actin cytoskeleton (no actin-binding domains) and site of double-strand break (no DNA repair motifs) by general knowledge. However, distinguishing ER from vesicle among the remaining two membrane-compartment options requires knowing that pollen exine/Ubisch body lipid biosynthesis occurs at the ER—a functional-context fact not encoded in the sequence. The sequence lacks any obvious ER-targeting signal peptide, transmembrane anchor, or KDEL/HDEL retrieval motif that would predict ER localization from sequence alone.","missing_item_specific_fact":"The experimentally determined ER localization of OsPKS2/PKS10 (Q8H305), established by fluorescent-protein co-localization in the 2018 Zou et al. study, is a protein-specific finding. Type III PKS enzymes are canonically cytoplasmic; this particular enzyme's ER association is a non-obvious, experimentally discovered property not inferable from sequence features.","reason":"The sequence is a typical type III PKS with no visible ER-targeting signals, TM domains, or retrieval motifs. Eliminating options A and B is straightforward, but choosing C (ER) over D (vesicle) requires the specific experimental finding that this OsPKS localizes to the ER during pollen wall biosynthesis—a fact absent from the sequence and not predictable by general enzymology or sequence heuristics."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"Options A (actin cytoskeleton) and B (site of double-strand break) are clearly inappropriate for a polyketide synthase with no cytoskeletal or DNA-repair domains. Between C (ER) and D (vesicle), the ER is the experimentally verified location, and a lipid-biosynthesis enzyme is more logically associated with the ER (site of lipid synthesis) than with a generic vesicle. While the sequence alone does not strongly favor ER over vesicle, the ER is the only option with direct experimental support."},"important_caveats":["The ER localization of OsPKS2 is experimentally determined (ECO:0000269, IDA) but is a surprising finding for a type III PKS, which are typically cytoplasmic. This makes the question less amenable to sequence-based reasoning.","The UniProt entry was first public in April 2025; the benchmark construction date is unknown, but the sequence and annotation are consistent across historical and current snapshots.","The reviewer-only evidence confirms the key but was not available to the evaluated model; the model must rely solely on the 405-aa sequence and general biological knowledge."]}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q8H305` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 131. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:57.631660+00:00.  

```json
"Q8H305"
```

Source SHA-256: `725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:57.631660+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"29411094","source":"PubMed"}],"id":"SL-0095","value":"Endoplasmic reticulum"}}]}
```

Source SHA-256: `725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)  
**Locator:** `/uniProtKBCrossReferences/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:57.631660+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"29411094","source":"PubMed"}],"id":"GO:0005783","properties":[{"key":"GoTerm","value":"C:endoplasmic reticulum"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:57.631660+00:00.  

```json
{"citation":{"authors":["Zou T.","Liu M.","Xiao Q.","Wang T.","Chen D.","Luo T.","Yuan G.","Li Q.","Zhu J.","Liang Y.","Deng Q.","Wang S.","Zheng A.","Wang L.","Li P.","Li S."],"citationCrossReferences":[{"database":"PubMed","id":"29411094"},{"database":"DOI","id":"10.1007/s00299-018-2265-x"}],"citationType":"journal article","firstPage":"759","id":"29411094","journal":"Plant Cell Rep.","lastPage":"773","publicationDate":"2018","title":"OsPKS2 is required for rice male fertility by participating in pollen wall formation.","volume":"37"},"referenceNumber":6,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","DEVELOPMENTAL STAGE","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)  
**Locator:** `lines 62-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-02T04:32:02.084503+00:00.  

```text
RN   [6]
RP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION
RP   PHENOTYPE.
RX   PubMed=29411094; DOI=10.1007/s00299-018-2265-x;
RA   Zou T., Liu M., Xiao Q., Wang T., Chen D., Luo T., Yuan G., Li Q., Zhu J.,
RA   Liang Y., Deng Q., Wang S., Zheng A., Wang L., Li P., Li S.;
RT   "OsPKS2 is required for rice male fertility by participating in pollen wall
RT   formation.";
RL   Plant Cell Rep. 37:759-773(2018).
```

Source SHA-256: `087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)  
**Locator:** `lines 92-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-02T04:32:02.084503+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Endoplasmic reticulum
CC       {ECO:0000269|PubMed:29411094}.
```

Source SHA-256: `087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)  
**Locator:** `lines 133-133`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 131 / 1.  
**Retrieved:** 2026-11-02T04:32:02.084503+00:00.  

```text
DR   GO; GO:0005783; C:endoplasmic reticulum; IDA:UniProtKB.
```

Source SHA-256: `087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
