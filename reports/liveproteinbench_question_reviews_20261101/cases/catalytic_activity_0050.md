# catalytic_activity_0050

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)

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
A. L-proline + 2-oxoglutarate + O2 = trans-3-hydroxy-L-proline + succinate + CO2
B. inosine(in) + H(+)(in) = inosine(out) + H(+)(out)
C. 32-oxolanosterol + reduced [NADPH--hemoprotein reductase] + O2 = 4,4-dimethyl-5alpha-cholesta-8,14,24-trien-3beta-ol + formate + oxidized [NADPH--hemoprotein reductase] + H2O + 2 H(+)
D. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry annotated as MAP kinase kinase Mkk1, EC 2.7.11.24, with the serine-phosphorylation reaction in choice D. The annotation cites a PubMed source; this supports the key, though it is not independent validation of the underlying experiments.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable eukaryotic protein-kinase catalytic domain, including the HRD and DFG motifs and an ATP-binding region. That supports protein phosphorylation and distinguishes choice D from the proline hydroxylation, inosine transport, and sterol-oxidation alternatives.


**Missing item-specific fact**

> The sequence alone does not establish the precise substrate-residue preference as securely as a protein-specific annotation or experiment would; however, only choice D describes protein phosphorylation.


**Reason**

> A concrete kinase-domain signature in the supplied sequence meaningfully distinguishes the reaction class among the choices. This is not merely recognition of an exact sequence or reliance on an unseen database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice D is the only candidate consistent with the protein-kinase domain evident in the sequence.


### Important caveats

- The reviewer-only database evidence is not information supplied to the evaluated model.
- The supporting annotation is linked to a cited publication, but the underlying experimental evidence was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic domain, including the HRD and DFG motifs and an ATP-binding region. That supports protein phosphorylation and distinguishes choice D from the proline hydroxylation, inosine transport, and sterol-oxidation alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish the precise substrate-residue preference as securely as a protein-specific annotation or experiment would; however, only choice D describes protein phosphorylation.",
    "reason": "A concrete kinase-domain signature in the supplied sequence meaningfully distinguishes the reaction class among the choices. This is not merely recognition of an exact sequence or reliance on an unseen database entry."
  },
  "case_id": "catalytic_activity_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as MAP kinase kinase Mkk1, EC 2.7.11.24, with the serine-phosphorylation reaction in choice D. The annotation cites a PubMed source; this supports the key, though it is not independent validation of the underlying experiments."
  },
  "important_caveats": [
    "The reviewer-only database evidence is not information supplied to the evaluated model.",
    "The supporting annotation is linked to a cited publication, but the underlying experimental evidence was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice D is the only candidate consistent with the protein-kinase domain evident in the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as MAP kinase kinase Mkk1, EC 2.7.11.24, with the serine-phosphorylation reaction in choice D. The annotation cites a PubMed source; this supports the key, though it is not independent validation of the underlying experiments.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic domain, including the HRD and DFG motifs and an ATP-binding region. That supports protein phosphorylation and distinguishes choice D from the proline hydroxylation, inosine transport, and sterol-oxidation alternatives.",
    "missing_item_specific_fact": "The sequence alone does not establish the precise substrate-residue preference as securely as a protein-specific annotation or experiment would; however, only choice D describes protein phosphorylation.",
    "reason": "A concrete kinase-domain signature in the supplied sequence meaningfully distinguishes the reaction class among the choices. This is not merely recognition of an exact sequence or reliance on an unseen database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice D is the only candidate consistent with the protein-kinase domain evident in the sequence."
  },
  "important_caveats": [
    "The reviewer-only database evidence is not information supplied to the evaluated model.",
    "The supporting annotation is linked to a cited publication, but the underlying experimental evidence was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A194VNL2 (MKK1_CYTMA, Cytospora mali) is annotated with EC 2.7.11.24 (MAP kinase kinase) and explicitly lists the catalytic reaction 'L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)' (RHEA:17989) with evidence code ECO:0000305 (inferred by sequence similarity) supported by PubMed:39631571. The supplied sequence matches the canonical entry (532 AA, SHA-256 confirmed). The expected answer D corresponds exactly to this annotated reaction. Note the entry also lists a parallel threonyl kinase reaction, but that does not contradict the seryl reaction being listed as a valid catalytic activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple canonical protein kinase motifs identifiable by inspection: a glycine-rich loop (GGLGEGAGGAVTRCKLKGGKT, GxGxxG), the catalytic lysine in the VAIK region, the HRD catalytic loop (HRDIKPSNILLCRNGEVKLCDFGVSGDFGTKGEANTFIGTSYYMAPERITGQTYTITSDVWSTGVTLLEVAQHRFPFPADGTEMQPRAGLIDLLTYIVQQPIPKLKDEPEAGIFWSDNFKHFIEACLEKNPKRRGMPWKMLEHPWMTELKTKRVNMSKYLTQVWGWDDPKGSK), the DFG motif, and the APE motif (MAPER). These motifs are diagnostic of the protein kinase superfamily. Among the four options, only D describes a kinase-catalyzed phosphoryl-transfer reaction. Option A is a 2-oxoglutarate-dependent dioxygenase (prolyl hydroxylase), B is a nucleoside transporter, and C is a cytochrome P450 sterol demethylase—none of which would display kinase motifs. Thus, identifying the kinase fold from the sequence and recognizing that only D is a kinase reaction provides a concrete reasoning path to the answer.


**Missing item-specific fact**

> None critical. While the specific assignment to EC 2.7.11.24 (MAPKK) versus another Ser/Thr kinase subclass would require additional annotation or phylogenetic context, the question only requires distinguishing a kinase reaction from three non-kinase reactions, which is achievable from the conserved kinase motifs visible in the sequence.


**Reason**

> The kinase motifs (glycine-rich loop, HRD, DFG, APE, catalytic Lys) are directly readable from the supplied sequence and are hallmarks of the protein kinase superfamily taught in standard biochemistry. Three of the four options describe entirely different enzyme classes (dioxygenase, transporter, P450) with incompatible structural motifs. A knowledgeable reader can eliminate A, B, and C on the basis that none of these enzyme classes would present the observed kinase architecture, leaving D as the only consistent choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry also annotates a threonyl-&#91;protein&#93; kinase reaction (C6/H5), that reaction is not offered as a separate option. Among the four provided choices, only D represents a kinase-catalyzed phosphoryl transfer. The other three options (dioxygenase, transporter, P450) are categorically incompatible with the observed kinase motifs. No ambiguity in selection exists.


### Important caveats

- The UniProt evidence code is ECO:0000305 (inferred by sequence similarity), meaning the enzymatic assignment is primarily computational/annotation-based rather than from direct in vitro kinetics on this specific protein, though it is supported by a PubMed reference (39631571) reporting functional characterization in Valsa mali.
- The entry was first publicly released in 2025-06-18 and reviewed (Swiss-Prot) in 2026-01-28; the author's source snapshot date is unknown. The sequence itself has been in databases since 2016-10-05.
- The protein also catalyzes L-threonyl-&#91;protein&#93; phosphorylation under the same EC number; the question selects only the seryl reaction as the correct option, which is valid but not exhaustive of the enzyme's activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple canonical protein kinase motifs identifiable by inspection: a glycine-rich loop (GGLGEGAGGAVTRCKLKGGKT, GxGxxG), the catalytic lysine in the VAIK region, the HRD catalytic loop (HRDIKPSNILLCRNGEVKLCDFGVSGDFGTKGEANTFIGTSYYMAPERITGQTYTITSDVWSTGVTLLEVAQHRFPFPADGTEMQPRAGLIDLLTYIVQQPIPKLKDEPEAGIFWSDNFKHFIEACLEKNPKRRGMPWKMLEHPWMTELKTKRVNMSKYLTQVWGWDDPKGSK), the DFG motif, and the APE motif (MAPER). These motifs are diagnostic of the protein kinase superfamily. Among the four options, only D describes a kinase-catalyzed phosphoryl-transfer reaction. Option A is a 2-oxoglutarate-dependent dioxygenase (prolyl hydroxylase), B is a nucleoside transporter, and C is a cytochrome P450 sterol demethylase—none of which would display kinase motifs. Thus, identifying the kinase fold from the sequence and recognizing that only D is a kinase reaction provides a concrete reasoning path to the answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While the specific assignment to EC 2.7.11.24 (MAPKK) versus another Ser/Thr kinase subclass would require additional annotation or phylogenetic context, the question only requires distinguishing a kinase reaction from three non-kinase reactions, which is achievable from the conserved kinase motifs visible in the sequence.",
    "reason": "The kinase motifs (glycine-rich loop, HRD, DFG, APE, catalytic Lys) are directly readable from the supplied sequence and are hallmarks of the protein kinase superfamily taught in standard biochemistry. Three of the four options describe entirely different enzyme classes (dioxygenase, transporter, P450) with incompatible structural motifs. A knowledgeable reader can eliminate A, B, and C on the basis that none of these enzyme classes would present the observed kinase architecture, leaving D as the only consistent choice."
  },
  "case_id": "catalytic_activity_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A194VNL2 (MKK1_CYTMA, Cytospora mali) is annotated with EC 2.7.11.24 (MAP kinase kinase) and explicitly lists the catalytic reaction 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' (RHEA:17989) with evidence code ECO:0000305 (inferred by sequence similarity) supported by PubMed:39631571. The supplied sequence matches the canonical entry (532 AA, SHA-256 confirmed). The expected answer D corresponds exactly to this annotated reaction. Note the entry also lists a parallel threonyl kinase reaction, but that does not contradict the seryl reaction being listed as a valid catalytic activity."
  },
  "important_caveats": [
    "The UniProt evidence code is ECO:0000305 (inferred by sequence similarity), meaning the enzymatic assignment is primarily computational/annotation-based rather than from direct in vitro kinetics on this specific protein, though it is supported by a PubMed reference (39631571) reporting functional characterization in Valsa mali.",
    "The entry was first publicly released in 2025-06-18 and reviewed (Swiss-Prot) in 2026-01-28; the author's source snapshot date is unknown. The sequence itself has been in databases since 2016-10-05.",
    "The protein also catalyzes L-threonyl-[protein] phosphorylation under the same EC number; the question selects only the seryl reaction as the correct option, which is valid but not exhaustive of the enzyme's activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry also annotates a threonyl-[protein] kinase reaction (C6/H5), that reaction is not offered as a separate option. Among the four provided choices, only D represents a kinase-catalyzed phosphoryl transfer. The other three options (dioxygenase, transporter, P450) are categorically incompatible with the observed kinase motifs. No ambiguity in selection exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A194VNL2 (MKK1_CYTMA, Cytospora mali) is annotated with EC 2.7.11.24 (MAP kinase kinase) and explicitly lists the catalytic reaction 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' (RHEA:17989) with evidence code ECO:0000305 (inferred by sequence similarity) supported by PubMed:39631571. The supplied sequence matches the canonical entry (532 AA, SHA-256 confirmed). The expected answer D corresponds exactly to this annotated reaction. Note the entry also lists a parallel threonyl kinase reaction, but that does not contradict the seryl reaction being listed as a valid catalytic activity.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple canonical protein kinase motifs identifiable by inspection: a glycine-rich loop (GGLGEGAGGAVTRCKLKGGKT, GxGxxG), the catalytic lysine in the VAIK region, the HRD catalytic loop (HRDIKPSNILLCRNGEVKLCDFGVSGDFGTKGEANTFIGTSYYMAPERITGQTYTITSDVWSTGVTLLEVAQHRFPFPADGTEMQPRAGLIDLLTYIVQQPIPKLKDEPEAGIFWSDNFKHFIEACLEKNPKRRGMPWKMLEHPWMTELKTKRVNMSKYLTQVWGWDDPKGSK), the DFG motif, and the APE motif (MAPER). These motifs are diagnostic of the protein kinase superfamily. Among the four options, only D describes a kinase-catalyzed phosphoryl-transfer reaction. Option A is a 2-oxoglutarate-dependent dioxygenase (prolyl hydroxylase), B is a nucleoside transporter, and C is a cytochrome P450 sterol demethylase—none of which would display kinase motifs. Thus, identifying the kinase fold from the sequence and recognizing that only D is a kinase reaction provides a concrete reasoning path to the answer.",
    "missing_item_specific_fact": "None critical. While the specific assignment to EC 2.7.11.24 (MAPKK) versus another Ser/Thr kinase subclass would require additional annotation or phylogenetic context, the question only requires distinguishing a kinase reaction from three non-kinase reactions, which is achievable from the conserved kinase motifs visible in the sequence.",
    "reason": "The kinase motifs (glycine-rich loop, HRD, DFG, APE, catalytic Lys) are directly readable from the supplied sequence and are hallmarks of the protein kinase superfamily taught in standard biochemistry. Three of the four options describe entirely different enzyme classes (dioxygenase, transporter, P450) with incompatible structural motifs. A knowledgeable reader can eliminate A, B, and C on the basis that none of these enzyme classes would present the observed kinase architecture, leaving D as the only consistent choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry also annotates a threonyl-[protein] kinase reaction (C6/H5), that reaction is not offered as a separate option. Among the four provided choices, only D represents a kinase-catalyzed phosphoryl transfer. The other three options (dioxygenase, transporter, P450) are categorically incompatible with the observed kinase motifs. No ambiguity in selection exists."
  },
  "important_caveats": [
    "The UniProt evidence code is ECO:0000305 (inferred by sequence similarity), meaning the enzymatic assignment is primarily computational/annotation-based rather than from direct in vitro kinetics on this specific protein, though it is supported by a PubMed reference (39631571) reporting functional characterization in Valsa mali.",
    "The entry was first publicly released in 2025-06-18 and reviewed (Swiss-Prot) in 2026-01-28; the author's source snapshot date is unknown. The sequence itself has been in databases since 2016-10-05.",
    "The protein also catalyzes L-threonyl-[protein] phosphorylation under the same EC number; the question selects only the seryl reaction as the correct option, which is valid but not exhaustive of the enzyme's activity."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194VNL2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:31.030295+00:00.  

```json
"A0A194VNL2"
```

Source SHA-256: `64947efb12ffe31eb19d5377a2c11808353008c104c9963c727f55828a864fe3`.

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
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:31.030295+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:17990"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `64947efb12ffe31eb19d5377a2c11808353008c104c9963c727f55828a864fe3`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194VNL2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:31.030295+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:46609"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `64947efb12ffe31eb19d5377a2c11808353008c104c9963c727f55828a864fe3`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194VNL2?format=txt&versions=29)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-02T04:24:34.608752+00:00.  

```text
ID   MKK1_CYTMA              Reviewed;         532 AA.
AC   A0A194VNL2;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-OCT-2016, sequence version 1.
DT   28-JAN-2026, entry version 29.
DE   RecName: Full=Mitogen-activated protein kinase kinase mkk1 {ECO:0000303|PubMed:39631571};
DE            Short=MAP kinase kinase mkk1 {ECO:0000303|PubMed:39631571};
DE            Short=MAPKK mkk1 {ECO:0000303|PubMed:39631571};
DE            EC=2.7.11.24 {ECO:0000305|PubMed:39631571};
GN   Name=mkk1 {ECO:0000303|PubMed:39631571}; ORFNames=VM1G_00540;
OS   Cytospora mali (Apple Valsa canker fungus) (Valsa mali).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Diaporthales; Cytosporaceae; Cytospora.
OX   NCBI_TaxID=578113;
```

Source SHA-256: `7a2da14bfe1d104822e102f7877c4f08b310e89ec58d7f8998551d22b8e1a9d2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194VNL2?format=txt&versions=29)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-02T04:24:34.608752+00:00.  

```text
DE   RecName: Full=Mitogen-activated protein kinase kinase mkk1 {ECO:0000303|PubMed:39631571};
DE            Short=MAP kinase kinase mkk1 {ECO:0000303|PubMed:39631571};
DE            Short=MAPKK mkk1 {ECO:0000303|PubMed:39631571};
DE            EC=2.7.11.24 {ECO:0000305|PubMed:39631571};
```

Source SHA-256: `7a2da14bfe1d104822e102f7877c4f08b310e89ec58d7f8998551d22b8e1a9d2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194VNL2?format=txt&versions=29)  
**Locator:** `lines 37-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-02T04:24:34.608752+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000305|PubMed:39631571};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:17990;
CC         Evidence={ECO:0000305|PubMed:39631571};
```

Source SHA-256: `7a2da14bfe1d104822e102f7877c4f08b310e89ec58d7f8998551d22b8e1a9d2`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194VNL2?format=txt&versions=29)  
**Locator:** `lines 45-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-02T04:24:34.608752+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000305|PubMed:39631571};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:46609;
CC         Evidence={ECO:0000305|PubMed:39631571};
```

Source SHA-256: `7a2da14bfe1d104822e102f7877c4f08b310e89ec58d7f8998551d22b8e1a9d2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
