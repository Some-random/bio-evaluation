# GO_cellular_component_0140

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
MDFESKYCTSQVNGTITITTRKVLDENLKSLLDEGKGELFLSCIPRNHSCSPRWIVEVASELGEVYIMRYKIDFSGNSRGYAYLQYINVDLKESAMQYLPMRFRQLCMCLRVEPSTNNRELVLKNVESSLRPWQVYQEMLKIHPFTIVRVYEYQLDQFFYIFEYRNNDSAASAHQRVRNSIRKFGEHAHISWLTAENILSRASGSFCFQREVSQNRTRRVPPRQKGCFKF

[Multiple Choices]
A. vitelline envelope
B. ciliary basal body
C. cell surface
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

> The exact sequence matches the Drosophila tumorous testis protein. Its UniProt subcellular-location annotation reports cytoplasm with experimental evidence (ECO:0000269), and its GO cytoplasm annotation is IDA:FlyBase. This supports choice D, while not establishing that cytoplasm is its only location.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a soluble-looking protein without an obvious signal peptide or transmembrane segment, which argues against cell-surface or vitelline-envelope localization. That does not reliably distinguish cytoplasm from a ciliary basal body, and the localization is not determined by those features alone.


**Missing item-specific fact**

> The protein-specific localization evidence identifying this Drosophila protein as cytoplasmic is absent from the sequence and choices.


**Reason**

> General sequence features make some options less plausible, but the key distinction among intracellular destinations depends on protein-specific annotation or experimental localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports cytoplasm; it also notes a nucleus annotation, but nucleus is not an offered choice. No evidence supplied supports another listed option.


### Important caveats

- The localization evidence is reviewer-only and was not available to the evaluated model.
- The GO and UniProt records match the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble-looking protein without an obvious signal peptide or transmembrane segment, which argues against cell-surface or vitelline-envelope localization. That does not reliably distinguish cytoplasm from a ciliary basal body, and the localization is not determined by those features alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization evidence identifying this Drosophila protein as cytoplasmic is absent from the sequence and choices.",
    "reason": "General sequence features make some options less plausible, but the key distinction among intracellular destinations depends on protein-specific annotation or experimental localization."
  },
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila tumorous testis protein. Its UniProt subcellular-location annotation reports cytoplasm with experimental evidence (ECO:0000269), and its GO cytoplasm annotation is IDA:FlyBase. This supports choice D, while not establishing that cytoplasm is its only location."
  },
  "important_caveats": [
    "The localization evidence is reviewer-only and was not available to the evaluated model.",
    "The GO and UniProt records match the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports cytoplasm; it also notes a nucleus annotation, but nucleus is not an offered choice. No evidence supplied supports another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila tumorous testis protein. Its UniProt subcellular-location annotation reports cytoplasm with experimental evidence (ECO:0000269), and its GO cytoplasm annotation is IDA:FlyBase. This supports choice D, while not establishing that cytoplasm is its only location.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a soluble-looking protein without an obvious signal peptide or transmembrane segment, which argues against cell-surface or vitelline-envelope localization. That does not reliably distinguish cytoplasm from a ciliary basal body, and the localization is not determined by those features alone.",
    "missing_item_specific_fact": "The protein-specific localization evidence identifying this Drosophila protein as cytoplasmic is absent from the sequence and choices.",
    "reason": "General sequence features make some options less plausible, but the key distinction among intracellular destinations depends on protein-specific annotation or experimental localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports cytoplasm; it also notes a nucleus annotation, but nucleus is not an offered choice. No evidence supplied supports another listed option."
  },
  "important_caveats": [
    "The localization evidence is reviewer-only and was not available to the evaluated model.",
    "The GO and UniProt records match the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8IQA2 (TUT_DROME) carries a SUBCELLULAR LOCATION comment of 'Cytoplasm' with evidence code ECO:0000269 (direct assay, PubMed:25412508), and a GO:0005737 (cytoplasm) annotation with evidence type IDA (Inferred from Direct Assay, FlyBase). This is experimental immunolocalization evidence from Chen et al. 2014 (PLoS Genet), not merely computational inference. The protein is an RRM-containing RNA-binding protein (tumorous testis) that forms a complex with BAM and BGCN in germline stem cell differentiation, a role consistent with cytoplasmic mRNA regulation. Sequence match is confirmed (SHA256 identical across benchmark, current, and historical entry v156).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [C9](#evidence-c9), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 230-residue sequence lacks an N-terminal signal peptide (no hydrophobic 15-30 residue stretch at the N-terminus), ruling out secretion and thus the extracellular vitelline envelope (A) and cell surface (C). It lacks a transmembrane domain or GPI-anchor signal, further excluding C. It shows no tubulin-like repeats, no centriole/basal-body structural motifs, and no microtubule-organizing-center signatures, making ciliary basal body (B) implausible. The sequence contains a region consistent with an RRM (RNA Recognition Motif) fold, characteristic of cytoplasmic RNA-binding proteins. A small protein with no targeting signals and an RRM domain defaults to the cytoplasm by elimination and by functional class.


**Missing item-specific fact**

> None strictly required. Positive confirmation of the RRM domain and the specific TUT/BAM/BGCN complex role would benefit from database lookup, but the elimination of A, B, and C via absence of required targeting signals is achievable from the sequence and general biology.


**Reason**

> The three distractors each require specific structural features (signal peptide for A and C; centriole/basal-body architecture for B) that are demonstrably absent from the sequence. The remaining option, cytoplasm, is the default compartment for a small soluble protein lacking organelle-targeting signals, and the RRM-like fold is consistent with cytoplasmic RNA regulation. This constitutes a concrete, sequence-grounded biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The question asks for the primary cellular component. Among the four options, only cytoplasm is compatible with a small intracellular protein lacking signal peptides, transmembrane domains, or centriole structural motifs. The GO nucleus and ribonucleoprotein-complex annotations (both IBA, inferred by similarity) are not among the choices and do not conflict with the primary cytoplasmic assignment supported by direct assay.


### Important caveats

- The UniProt entry also carries GO:0005634 (nucleus, IBA:GO_Central) and GO:1990904 (ribonucleoprotein complex, IBA:GO_Central), but these are similarity-based inferences, not direct experimental assignments, and are not among the answer options.
- The RRM domain identification from the raw sequence is inferential; a model without domain-prediction tools may struggle to positively identify it, though the elimination approach does not depend on this.
- The identity of the protein (Q8IQA2, TUT_DROME) was inferred by the reviewer from dataset metadata absent from the model input; the model sees only the sequence and options.
- The GO ontology snapshot used by the benchmark authors is unknown; the current ontology was used for reviewer verification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 230-residue sequence lacks an N-terminal signal peptide (no hydrophobic 15-30 residue stretch at the N-terminus), ruling out secretion and thus the extracellular vitelline envelope (A) and cell surface (C). It lacks a transmembrane domain or GPI-anchor signal, further excluding C. It shows no tubulin-like repeats, no centriole/basal-body structural motifs, and no microtubule-organizing-center signatures, making ciliary basal body (B) implausible. The sequence contains a region consistent with an RRM (RNA Recognition Motif) fold, characteristic of cytoplasmic RNA-binding proteins. A small protein with no targeting signals and an RRM domain defaults to the cytoplasm by elimination and by functional class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Positive confirmation of the RRM domain and the specific TUT/BAM/BGCN complex role would benefit from database lookup, but the elimination of A, B, and C via absence of required targeting signals is achievable from the sequence and general biology.",
    "reason": "The three distractors each require specific structural features (signal peptide for A and C; centriole/basal-body architecture for B) that are demonstrably absent from the sequence. The remaining option, cytoplasm, is the default compartment for a small soluble protein lacking organelle-targeting signals, and the RRM-like fold is consistent with cytoplasmic RNA regulation. This constitutes a concrete, sequence-grounded biological argument."
  },
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "C9",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8IQA2 (TUT_DROME) carries a SUBCELLULAR LOCATION comment of 'Cytoplasm' with evidence code ECO:0000269 (direct assay, PubMed:25412508), and a GO:0005737 (cytoplasm) annotation with evidence type IDA (Inferred from Direct Assay, FlyBase). This is experimental immunolocalization evidence from Chen et al. 2014 (PLoS Genet), not merely computational inference. The protein is an RRM-containing RNA-binding protein (tumorous testis) that forms a complex with BAM and BGCN in germline stem cell differentiation, a role consistent with cytoplasmic mRNA regulation. Sequence match is confirmed (SHA256 identical across benchmark, current, and historical entry v156)."
  },
  "important_caveats": [
    "The UniProt entry also carries GO:0005634 (nucleus, IBA:GO_Central) and GO:1990904 (ribonucleoprotein complex, IBA:GO_Central), but these are similarity-based inferences, not direct experimental assignments, and are not among the answer options.",
    "The RRM domain identification from the raw sequence is inferential; a model without domain-prediction tools may struggle to positively identify it, though the elimination approach does not depend on this.",
    "The identity of the protein (Q8IQA2, TUT_DROME) was inferred by the reviewer from dataset metadata absent from the model input; the model sees only the sequence and options.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the current ontology was used for reviewer verification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for the primary cellular component. Among the four options, only cytoplasm is compatible with a small intracellular protein lacking signal peptides, transmembrane domains, or centriole structural motifs. The GO nucleus and ribonucleoprotein-complex annotations (both IBA, inferred by similarity) are not among the choices and do not conflict with the primary cytoplasmic assignment supported by direct assay."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8IQA2 (TUT_DROME) carries a SUBCELLULAR LOCATION comment of 'Cytoplasm' with evidence code ECO:0000269 (direct assay, PubMed:25412508), and a GO:0005737 (cytoplasm) annotation with evidence type IDA (Inferred from Direct Assay, FlyBase). This is experimental immunolocalization evidence from Chen et al. 2014 (PLoS Genet), not merely computational inference. The protein is an RRM-containing RNA-binding protein (tumorous testis) that forms a complex with BAM and BGCN in germline stem cell differentiation, a role consistent with cytoplasmic mRNA regulation. Sequence match is confirmed (SHA256 identical across benchmark, current, and historical entry v156).",
    "evidence_ids": ["C5", "C6", "H3", "H4", "C9", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 230-residue sequence lacks an N-terminal signal peptide (no hydrophobic 15-30 residue stretch at the N-terminus), ruling out secretion and thus the extracellular vitelline envelope (A) and cell surface (C). It lacks a transmembrane domain or GPI-anchor signal, further excluding C. It shows no tubulin-like repeats, no centriole/basal-body structural motifs, and no microtubule-organizing-center signatures, making ciliary basal body (B) implausible. The sequence contains a region consistent with an RRM (RNA Recognition Motif) fold, characteristic of cytoplasmic RNA-binding proteins. A small protein with no targeting signals and an RRM domain defaults to the cytoplasm by elimination and by functional class.",
    "missing_item_specific_fact": "None strictly required. Positive confirmation of the RRM domain and the specific TUT/BAM/BGCN complex role would benefit from database lookup, but the elimination of A, B, and C via absence of required targeting signals is achievable from the sequence and general biology.",
    "reason": "The three distractors each require specific structural features (signal peptide for A and C; centriole/basal-body architecture for B) that are demonstrably absent from the sequence. The remaining option, cytoplasm, is the default compartment for a small soluble protein lacking organelle-targeting signals, and the RRM-like fold is consistent with cytoplasmic RNA regulation. This constitutes a concrete, sequence-grounded biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The question asks for the primary cellular component. Among the four options, only cytoplasm is compatible with a small intracellular protein lacking signal peptides, transmembrane domains, or centriole structural motifs. The GO nucleus and ribonucleoprotein-complex annotations (both IBA, inferred by similarity) are not among the choices and do not conflict with the primary cytoplasmic assignment supported by direct assay."
  },
  "important_caveats": [
    "The UniProt entry also carries GO:0005634 (nucleus, IBA:GO_Central) and GO:1990904 (ribonucleoprotein complex, IBA:GO_Central), but these are similarity-based inferences, not direct experimental assignments, and are not among the answer options.",
    "The RRM domain identification from the raw sequence is inferential; a model without domain-prediction tools may struggle to positively identify it, though the elimination approach does not depend on this.",
    "The identity of the protein (Q8IQA2, TUT_DROME) was inferred by the reviewer from dataset metadata absent from the model input; the model sees only the sequence and options.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the current ontology was used for reviewer verification."
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

**Accession:** `Q8IQA2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 156. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:19.021600+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"25412508","source":"PubMed"}],"id":"SL-0086","value":"Cytoplasm"}}]}
```

Source SHA-256: `0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)  
**Locator:** `/uniProtKBCrossReferences/26`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:19.021600+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"25412508","source":"PubMed"}],"id":"GO:0005737","properties":[{"key":"GoTerm","value":"C:cytoplasm"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IQA2.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:19.021600+00:00.  

```json
{"citation":{"authors":["Chen D.","Wu C.","Zhao S.","Geng Q.","Gao Y.","Li X.","Zhang Y.","Wang Z."],"citationCrossReferences":[{"database":"PubMed","id":"25412508"},{"database":"DOI","id":"10.1371/journal.pgen.1004797"}],"citationType":"journal article","firstPage":"e1004797","id":"25412508","journal":"PLoS Genet.","lastPage":"e1004797","publicationDate":"2014","title":"Three RNA binding proteins form a complex to promote differentiation of germline stem cell lineage in Drosophila.","volume":"10"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","INTERACTION WITH BAM AND BGCN","SUBCELLULAR LOCATION","RRM DOMAIN","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `0602f9a5538349898a0569f81e032214b6d397ab9c4082ab5b5a31acc3ff8299`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156)  
**Locator:** `lines 68-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:32:22.135035+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, INTERACTION WITH BAM AND BGCN, SUBCELLULAR LOCATION, RRM DOMAIN,
RP   AND DISRUPTION PHENOTYPE.
RX   PubMed=25412508; DOI=10.1371/journal.pgen.1004797;
RA   Chen D., Wu C., Zhao S., Geng Q., Gao Y., Li X., Zhang Y., Wang Z.;
RT   "Three RNA binding proteins form a complex to promote differentiation of
RT   germline stem cell lineage in Drosophila.";
RL   PLoS Genet. 10:e1004797-e1004797(2014).
```

Source SHA-256: `ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156)  
**Locator:** `lines 111-111`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:32:22.135035+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:25412508}.
```

Source SHA-256: `ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IQA2?format=txt&versions=156)  
**Locator:** `lines 148-148`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 156 / 1.  
**Retrieved:** 2026-11-02T04:32:22.135035+00:00.  

```text
DR   GO; GO:0005737; C:cytoplasm; IDA:FlyBase.
```

Source SHA-256: `ee4b024dec0b13e4b3cd47072ce6c30cc94a8ba78c2a035c58f840273f55dfa6`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 140. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
