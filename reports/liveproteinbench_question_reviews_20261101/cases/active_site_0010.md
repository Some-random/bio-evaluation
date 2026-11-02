# active_site_0010

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 362 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMHNQGNSNGDPAAPMSNLQEPQVPMLSQTPNPVPMMNAPAPLLRPAIPGARGARPPRLGLAIPPSPNVKPVGGNAAGPPLQVPSRPPLPVLHLATPMGSTVAPQEHQPNRGAQPGQSASGGSESSAAHSRTGSFGPLDGRGSNPTSAGSQYSALSFASQYGLGGAKPHGTPDPVSAVGSLYSNASEGGVGMEREGSMHGLEASFDKMSLEKARTSDAEDLDDEGWRIVSMENRIVELGGLGEGAGGAVTRCKLKGGKTVFALKVITTNPDPDIKKQILREINFNKGCASEHICRYYGGFLDPSTATISIAMEFCEGGSLDSIYKEVKRLGGRTGEKVLGKIAEGVLQGLTYLEAKRILHRDIKPSNILLCRNGEVKLCDFGVSGDFGTKGEANTFIGTSYYMAPERITGQTYTITSDVWSTGVTLLEVAQHRFPFPADGTEMQPRAGLIDLLTYIVQQPIPKLKDEPEAGIFWSDNFKHFIEACLEKNPKRRGMPWKMLEHPWMTELKTKRVNMSKYLTQVWGWDDPKGSK

[Multiple Choices]
A. Position 409 (Proton acceptor)
B. Position 165 (Proton donor)
C. Position 362 (Proton acceptor)
D. Position 95 (Nucleophile)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the annotated MKK1 sequence, and both current and historical UniProt records annotate position 362 as an active-site proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a protein-kinase domain with the conserved HRD catalytic motif. In kinases, the Asp in this motif is the catalytic base, making the corresponding Asp the plausible proton acceptor among the options.


**Missing item-specific fact**

> No external protein-specific fact is essential for a defensible motif-based choice; experimental validation of this exact residue is not supplied.


**Reason**

> The conserved kinase motif provides a biological basis to distinguish the catalytic proton-accepting residue from positions outside that motif. The database annotation supports the key but was not part of the evaluated input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The conserved catalytic Asp in the kinase HRD motif provides a specific basis for selecting the proton-acceptor option.


### Important caveats

- The active-site annotation is computationally assigned through PROSITE-ProRule, not shown here to be experimentally measured.
- The sequence match is exact, but the author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a protein-kinase domain with the conserved HRD catalytic motif. In kinases, the Asp in this motif is the catalytic base, making the corresponding Asp the plausible proton acceptor among the options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external protein-specific fact is essential for a defensible motif-based choice; experimental validation of this exact residue is not supplied.",
    "reason": "The conserved kinase motif provides a biological basis to distinguish the catalytic proton-accepting residue from positions outside that motif. The database annotation supports the key but was not part of the evaluated input."
  },
  "case_id": "active_site_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated MKK1 sequence, and both current and historical UniProt records annotate position 362 as an active-site proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental confirmation."
  },
  "important_caveats": [
    "The active-site annotation is computationally assigned through PROSITE-ProRule, not shown here to be experimentally measured.",
    "The sequence match is exact, but the author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved catalytic Asp in the kinase HRD motif provides a specific basis for selecting the proton-acceptor option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated MKK1 sequence, and both current and historical UniProt records annotate position 362 as an active-site proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental confirmation.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a protein-kinase domain with the conserved HRD catalytic motif. In kinases, the Asp in this motif is the catalytic base, making the corresponding Asp the plausible proton acceptor among the options.",
    "missing_item_specific_fact": "No external protein-specific fact is essential for a defensible motif-based choice; experimental validation of this exact residue is not supplied.",
    "reason": "The conserved kinase motif provides a biological basis to distinguish the catalytic proton-accepting residue from positions outside that motif. The database annotation supports the key but was not part of the evaluated input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The conserved catalytic Asp in the kinase HRD motif provides a specific basis for selecting the proton-acceptor option."
  },
  "important_caveats": [
    "The active-site annotation is computationally assigned through PROSITE-ProRule, not shown here to be experimentally measured.",
    "The sequence match is exact, but the author's source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A194VNL2, MKK1_CYTMA) annotates position 362 as 'Proton acceptor' active site (C5, H3), with evidence code ECO:0000255|PROSITE-ProRule:PRU00159 (protein kinase ATP-binding signature). This is a computational/rule-based annotation, not a direct experimental measurement, but it is consistent with well-established protein kinase biochemistry: the aspartate in the HRD catalytic-loop motif acts as the catalytic base (proton acceptor) that deprotonates the substrate hydroxyl during phosphoryl transfer. The sequence contains the HRD motif ('KRILHRDIKPSNILLCRNGEVKLCDFGVSGDFGTKGEANTFIGTSYYMAPERITGQTYTITSDVWSTGVTLLEVAQHRFPFPADGTEMQPRAGLIDLLTYIVQQPIPKLKDEPEAGIFWSDNFKHFIEACLEKNPKRRGMPWKMLEHPWMTELKTKRVNMSKYLTQVWGWDDPKGSK'), and the D in HRD at position 362 is the expected proton acceptor. The protein is confirmed as a MAP kinase kinase (EC 2.7.11.24), for which this mechanism is canonical.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable protein-kinase domain motifs (glycine-rich loop, VAIK lysine, HRD catalytic loop, DFG motif, activation loop). General kinase biochemistry establishes that the catalytic proton acceptor is the aspartate in the HRD motif, which deprotonates the substrate hydroxyl for nucleophilic attack on ATP's gamma-phosphate. A model can (a) recognize the kinase fold from the sequence, (b) locate the HRD motif, (c) identify the D in HRD as the proton acceptor, and (d) count its position. The distractors (proton donor at 165, nucleophile at 95, proton acceptor at 409) do not correspond to any recognized protein-kinase catalytic residue, so the kinase mechanism meaningfully excludes them.


**Missing item-specific fact**

> Precise residue counting to confirm position 362 in a 532-residue sequence is mechanically tedious but not impossible; no additional external annotation is strictly required beyond recognizing the kinase fold and HRD motif.


**Reason**

> The biological reasoning path (recognize kinase → identify HRD motif → assign proton-acceptor role to its aspartate → count position) is grounded in general enzymology of protein kinases and is distinguishable from the distractors without memorizing this specific entry's UniProt record. The main difficulty is accurate position counting in a long sequence, which adds predictive difficulty but does not introduce a missing item-specific fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options assign distinct roles (proton acceptor, proton donor, nucleophile) at four different positions. Only the HRD aspartate (position 362) matches the established protein-kinase catalytic mechanism as a proton acceptor. The other positions and roles do not correspond to recognized kinase catalytic residues, so the wording adequately distinguishes a single correct answer.


### Important caveats

- The active-site annotation at position 362 is derived from PROSITE-ProRule PRU00159 (ECO:0000255), i.e., a computational pattern-matching rule, not a direct experimental determination of catalytic mechanism for this specific protein. However, the HRD-aspartate-as-proton-acceptor mechanism is well-established across the protein kinase superfamily.
- The UniProt entry was first publicly released 2025-06-18; the author's source snapshot is unknown. The sequence and annotation have been stable (sequence version 1, last sequence update 2016-10-05).
- The reviewer-only accession and annotation were absent from the evaluated model input; the model must rely solely on the sequence and general biological knowledge.
- Position counting in a 532-residue sequence is error-prone for language models, which may affect practical answerability even though the biological reasoning is sound.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable protein-kinase domain motifs (glycine-rich loop, VAIK lysine, HRD catalytic loop, DFG motif, activation loop). General kinase biochemistry establishes that the catalytic proton acceptor is the aspartate in the HRD motif, which deprotonates the substrate hydroxyl for nucleophilic attack on ATP's gamma-phosphate. A model can (a) recognize the kinase fold from the sequence, (b) locate the HRD motif, (c) identify the D in HRD as the proton acceptor, and (d) count its position. The distractors (proton donor at 165, nucleophile at 95, proton acceptor at 409) do not correspond to any recognized protein-kinase catalytic residue, so the kinase mechanism meaningfully excludes them.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise residue counting to confirm position 362 in a 532-residue sequence is mechanically tedious but not impossible; no additional external annotation is strictly required beyond recognizing the kinase fold and HRD motif.",
    "reason": "The biological reasoning path (recognize kinase → identify HRD motif → assign proton-acceptor role to its aspartate → count position) is grounded in general enzymology of protein kinases and is distinguishable from the distractors without memorizing this specific entry's UniProt record. The main difficulty is accurate position counting in a long sequence, which adds predictive difficulty but does not introduce a missing item-specific fact."
  },
  "case_id": "active_site_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A194VNL2, MKK1_CYTMA) annotates position 362 as 'Proton acceptor' active site (C5, H3), with evidence code ECO:0000255|PROSITE-ProRule:PRU00159 (protein kinase ATP-binding signature). This is a computational/rule-based annotation, not a direct experimental measurement, but it is consistent with well-established protein kinase biochemistry: the aspartate in the HRD catalytic-loop motif acts as the catalytic base (proton acceptor) that deprotonates the substrate hydroxyl during phosphoryl transfer. The sequence contains the HRD motif ('KRILHRDIKPSNILLCRNGEVKLCDFGVSGDFGTKGEANTFIGTSYYMAPERITGQTYTITSDVWSTGVTLLEVAQHRFPFPADGTEMQPRAGLIDLLTYIVQQPIPKLKDEPEAGIFWSDNFKHFIEACLEKNPKRRGMPWKMLEHPWMTELKTKRVNMSKYLTQVWGWDDPKGSK'), and the D in HRD at position 362 is the expected proton acceptor. The protein is confirmed as a MAP kinase kinase (EC 2.7.11.24), for which this mechanism is canonical."
  },
  "important_caveats": [
    "The active-site annotation at position 362 is derived from PROSITE-ProRule PRU00159 (ECO:0000255), i.e., a computational pattern-matching rule, not a direct experimental determination of catalytic mechanism for this specific protein. However, the HRD-aspartate-as-proton-acceptor mechanism is well-established across the protein kinase superfamily.",
    "The UniProt entry was first publicly released 2025-06-18; the author's source snapshot is unknown. The sequence and annotation have been stable (sequence version 1, last sequence update 2016-10-05).",
    "The reviewer-only accession and annotation were absent from the evaluated model input; the model must rely solely on the sequence and general biological knowledge.",
    "Position counting in a 532-residue sequence is error-prone for language models, which may affect practical answerability even though the biological reasoning is sound."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options assign distinct roles (proton acceptor, proton donor, nucleophile) at four different positions. Only the HRD aspartate (position 362) matches the established protein-kinase catalytic mechanism as a proton acceptor. The other positions and roles do not correspond to recognized kinase catalytic residues, so the wording adequately distinguishes a single correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A194VNL2, MKK1_CYTMA) annotates position 362 as 'Proton acceptor' active site (C5, H3), with evidence code ECO:0000255|PROSITE-ProRule:PRU00159 (protein kinase ATP-binding signature). This is a computational/rule-based annotation, not a direct experimental measurement, but it is consistent with well-established protein kinase biochemistry: the aspartate in the HRD catalytic-loop motif acts as the catalytic base (proton acceptor) that deprotonates the substrate hydroxyl during phosphoryl transfer. The sequence contains the HRD motif ('KRILHRDIKPSNILLCRNGEVKLCDFGVSGDFGTKGEANTFIGTSYYMAPERITGQTYTITSDVWSTGVTLLEVAQHRFPFPADGTEMQPRAGLIDLLTYIVQQPIPKLKDEPEAGIFWSDNFKHFIEACLEKNPKRRGMPWKMLEHPWMTELKTKRVNMSKYLTQVWGWDDPKGSK'), and the D in HRD at position 362 is the expected proton acceptor. The protein is confirmed as a MAP kinase kinase (EC 2.7.11.24), for which this mechanism is canonical.",
    "evidence_ids": ["C5", "H3", "C4", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable protein-kinase domain motifs (glycine-rich loop, VAIK lysine, HRD catalytic loop, DFG motif, activation loop). General kinase biochemistry establishes that the catalytic proton acceptor is the aspartate in the HRD motif, which deprotonates the substrate hydroxyl for nucleophilic attack on ATP's gamma-phosphate. A model can (a) recognize the kinase fold from the sequence, (b) locate the HRD motif, (c) identify the D in HRD as the proton acceptor, and (d) count its position. The distractors (proton donor at 165, nucleophile at 95, proton acceptor at 409) do not correspond to any recognized protein-kinase catalytic residue, so the kinase mechanism meaningfully excludes them.",
    "missing_item_specific_fact": "Precise residue counting to confirm position 362 in a 532-residue sequence is mechanically tedious but not impossible; no additional external annotation is strictly required beyond recognizing the kinase fold and HRD motif.",
    "reason": "The biological reasoning path (recognize kinase → identify HRD motif → assign proton-acceptor role to its aspartate → count position) is grounded in general enzymology of protein kinases and is distinguishable from the distractors without memorizing this specific entry's UniProt record. The main difficulty is accurate position counting in a long sequence, which adds predictive difficulty but does not introduce a missing item-specific fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options assign distinct roles (proton acceptor, proton donor, nucleophile) at four different positions. Only the HRD aspartate (position 362) matches the established protein-kinase catalytic mechanism as a proton acceptor. The other positions and roles do not correspond to recognized kinase catalytic residues, so the wording adequately distinguishes a single correct answer."
  },
  "important_caveats": [
    "The active-site annotation at position 362 is derived from PROSITE-ProRule PRU00159 (ECO:0000255), i.e., a computational pattern-matching rule, not a direct experimental determination of catalytic mechanism for this specific protein. However, the HRD-aspartate-as-proton-acceptor mechanism is well-established across the protein kinase superfamily.",
    "The UniProt entry was first publicly released 2025-06-18; the author's source snapshot is unknown. The sequence and annotation have been stable (sequence version 1, last sequence update 2016-10-05).",
    "The reviewer-only accession and annotation were absent from the evaluated model input; the model must rely solely on the sequence and general biological knowledge.",
    "Position counting in a 532-residue sequence is error-prone for language models, which may affect practical answerability even though the biological reasoning is sound."
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

**Accession:** `A0A194VNL2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 29. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194VNL2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:31.030295+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"value":"2.7.11.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39631571","source":"PubMed"}],"value":"Mitogen-activated protein kinase kinase mkk1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39631571","source":"PubMed"}],"value":"MAP kinase kinase mkk1"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"39631571","source":"PubMed"}],"value":"MAPKK mkk1"}]}}
```

Source SHA-256: `64947efb12ffe31eb19d5377a2c11808353008c104c9963c727f55828a864fe3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194VNL2.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:31.030295+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":362},"start":{"modifier":"EXACT","value":362}},"type":"Active site"}
```

Source SHA-256: `64947efb12ffe31eb19d5377a2c11808353008c104c9963c727f55828a864fe3`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194VNL2.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:31.030295+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:30616"}],"ligand":{"id":"ChEBI:CHEBI:30616","name":"ATP"},"location":{"end":{"modifier":"EXACT","value":249},"start":{"modifier":"EXACT","value":241}},"type":"Binding site"}
```

Source SHA-256: `64947efb12ffe31eb19d5377a2c11808353008c104c9963c727f55828a864fe3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194VNL2.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:31.030295+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:30616"}],"ligand":{"id":"ChEBI:CHEBI:30616","name":"ATP"},"location":{"end":{"modifier":"EXACT","value":264},"start":{"modifier":"EXACT","value":264}},"type":"Binding site"}
```

Source SHA-256: `64947efb12ffe31eb19d5377a2c11808353008c104c9963c727f55828a864fe3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194VNL2?format=txt&versions=29)  
**Locator:** `lines 119-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-02T04:24:34.608752+00:00.  

```text
FT   ACT_SITE        362
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159"
```

Source SHA-256: `7a2da14bfe1d104822e102f7877c4f08b310e89ec58d7f8998551d22b8e1a9d2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
