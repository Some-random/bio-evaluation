# catalytic_activity_0089

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — rhazimol + acetyl-CoA = akuammiline + CoA + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNITILSKETIKPLAPTPHHHKYYKVSLLDQFAPSSYMPFIFFYPNKFADRDAAGILTQLKESLSQILTIYYPLAGRVKDTVYVECNDEGVEFIEAQANGSLSDFLKQPDIAALNNFLPRNGNGLEKGCSISPVAIKATVFECSGIVLGVCIFHKVVDAAAAGEFLQSWAKIGRGSKETVELPNFTSASSLFPPRESLSSKFVRDFDNFFFQGSKSFMRRFVFDATAITTLRTKATSEKVPNPSRVEALMEFVVQHLSTAFKTAKSETPETLMITHPVNLRKRIEPPLPDSTFGNVIWLAFAFYDCDPSETKIKPGDVVERVREAFAALDKESISELETDDAFTSLSELLESVYTNEKIKIYRFTSTCNMGFYDVDFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN

[Multiple Choices]
A. 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O
B. rhazimol + acetyl-CoA = akuammiline + CoA + H(+)
C. dimethylamine + NADPH + O2 + H(+) = methylamine + formaldehyde + NADP(+) + H2O
D. 4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
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

> The exact 450-aa sequence matches the UniProt entry annotated as akuammiline synthase 2, with the reaction in choice B. The annotation cites experimental evidence (ECO:0000269), though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains BAHD-family acyltransferase hallmarks, including an HXXXD motif and a DFGWG motif, consistent with an acetyl-CoA-dependent acyl transfer as in B. The other choices describe a large polyketide-forming reaction, an oxidative demethylation, or SAM-dependent methylation, which do not fit that sequence-level enzyme-family evidence.


**Missing item-specific fact**

> The exact rhazimol-to-akuammiline substrate specificity is not established by the sequence motifs alone; that specific reaction is supported by the external experimental annotation.


**Reason**

> Although the precise substrate and product would require protein-specific evidence, the sequence and contrasting reaction classes provide a meaningful basis to select B among these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reaction classes, and the sequence's acyltransferase-family features favor B.


### Important caveats

- The reviewer-only annotation confirms the exact reaction for a sequence-matched entry but was not supplied to the evaluated model.
- Sequence-family motifs support the reaction class more directly than the exact substrate-product pair.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains BAHD-family acyltransferase hallmarks, including an HXXXD motif and a DFGWG motif, consistent with an acetyl-CoA-dependent acyl transfer as in B. The other choices describe a large polyketide-forming reaction, an oxidative demethylation, or SAM-dependent methylation, which do not fit that sequence-level enzyme-family evidence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact rhazimol-to-akuammiline substrate specificity is not established by the sequence motifs alone; that specific reaction is supported by the external experimental annotation.",
    "reason": "Although the precise substrate and product would require protein-specific evidence, the sequence and contrasting reaction classes provide a meaningful basis to select B among these choices."
  },
  "case_id": "catalytic_activity_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 450-aa sequence matches the UniProt entry annotated as akuammiline synthase 2, with the reaction in choice B. The annotation cites experimental evidence (ECO:0000269), though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only annotation confirms the exact reaction for a sequence-matched entry but was not supplied to the evaluated model.",
    "Sequence-family motifs support the reaction class more directly than the exact substrate-product pair."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction classes, and the sequence's acyltransferase-family features favor B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 450-aa sequence matches the UniProt entry annotated as akuammiline synthase 2, with the reaction in choice B. The annotation cites experimental evidence (ECO:0000269), though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains BAHD-family acyltransferase hallmarks, including an HXXXD motif and a DFGWG motif, consistent with an acetyl-CoA-dependent acyl transfer as in B. The other choices describe a large polyketide-forming reaction, an oxidative demethylation, or SAM-dependent methylation, which do not fit that sequence-level enzyme-family evidence.",
    "missing_item_specific_fact": "The exact rhazimol-to-akuammiline substrate specificity is not established by the sequence motifs alone; that specific reaction is supported by the external experimental annotation.",
    "reason": "Although the precise substrate and product would require protein-specific evidence, the sequence and contrasting reaction classes provide a meaningful basis to select B among these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reaction classes, and the sequence's acyltransferase-family features favor B."
  },
  "important_caveats": [
    "The reviewer-only annotation confirms the exact reaction for a sequence-matched entry but was not supplied to the evaluated model.",
    "Sequence-family motifs support the reaction class more directly than the exact substrate-product pair."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A0A9E7LUL3 (AKS2_ALSSC, Akuammiline synthase 2, EC 2.3.1.322). The catalytic activity is explicitly annotated as 'rhazimol + acetyl-CoA = akuammiline + CoA + H(+)' with experimental evidence (ECO:0000269|PubMed:36349266, Wang et al. 2022, Chem. Sci.). The sequence match is confirmed in both current (v15) and historical (v13) snapshots.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the DFGWG motif (visible at positions ~370-374: 'DFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN'), which is the hallmark of the BAHD acyltransferase superfamily. BAHD acyltransferases catalyze acyl transfer from an acyl-CoA donor to an acceptor, releasing free CoA. This mechanism is consistent ONLY with Choice B (acetyl-CoA → CoA transfer). Choice A involves NADPH-dependent polyketide chain elongation with CO2 release (type III PKS mechanism). Choice C involves O2 and NADPH (CYP450/amine oxidase). Choice D involves S-adenosyl-L-methionine (SAM-dependent methyltransferase). None of these cofactor requirements are compatible with BAHD acyltransferase chemistry.


**Missing item-specific fact**

> The specific substrates (rhazimol as acceptor, akuammiline as product) cannot be deduced from the sequence alone, but they are not needed to eliminate the other three choices, which are mechanistically incompatible with BAHD acyltransferase catalysis.


**Reason**

> A model with general enzymology knowledge can identify the DFGWG motif, recognize it as diagnostic of BAHD acyltransferases, and eliminate choices A, C, and D based on their incompatible cofactors (NADPH, O2, SAM). The remaining choice B is the only acyl-CoA → CoA transfer reaction. This is a concrete mechanistic argument grounded in the sequence, not a database lookup of this specific enzyme's substrates.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four distinct enzyme classes (polyketide synthase, BAHD acyltransferase, amine oxidase, methyltransferase) with mutually exclusive cofactor requirements. The DFGWG motif uniquely identifies the BAHD class, leaving only Choice B mechanistically viable.


### Important caveats

- The specific natural-product substrates (rhazimol, akuammiline) are highly specialized and would not be predictable from sequence alone; however, the question is answerable by mechanism-type elimination without knowing these substrates.
- The BAHD motif identification requires the model to recognize a ~5-residue motif within a 450-aa sequence, which is a reasonable but non-trivial pattern-recognition task.
- The annotation is based on experimental evidence from a 2022 publication, confirming the reaction is not merely computational inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the DFGWG motif (visible at positions ~370-374: 'DFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN'), which is the hallmark of the BAHD acyltransferase superfamily. BAHD acyltransferases catalyze acyl transfer from an acyl-CoA donor to an acceptor, releasing free CoA. This mechanism is consistent ONLY with Choice B (acetyl-CoA → CoA transfer). Choice A involves NADPH-dependent polyketide chain elongation with CO2 release (type III PKS mechanism). Choice C involves O2 and NADPH (CYP450/amine oxidase). Choice D involves S-adenosyl-L-methionine (SAM-dependent methyltransferase). None of these cofactor requirements are compatible with BAHD acyltransferase chemistry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrates (rhazimol as acceptor, akuammiline as product) cannot be deduced from the sequence alone, but they are not needed to eliminate the other three choices, which are mechanistically incompatible with BAHD acyltransferase catalysis.",
    "reason": "A model with general enzymology knowledge can identify the DFGWG motif, recognize it as diagnostic of BAHD acyltransferases, and eliminate choices A, C, and D based on their incompatible cofactors (NADPH, O2, SAM). The remaining choice B is the only acyl-CoA → CoA transfer reaction. This is a concrete mechanistic argument grounded in the sequence, not a database lookup of this specific enzyme's substrates."
  },
  "case_id": "catalytic_activity_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9E7LUL3 (AKS2_ALSSC, Akuammiline synthase 2, EC 2.3.1.322). The catalytic activity is explicitly annotated as 'rhazimol + acetyl-CoA = akuammiline + CoA + H(+)' with experimental evidence (ECO:0000269|PubMed:36349266, Wang et al. 2022, Chem. Sci.). The sequence match is confirmed in both current (v15) and historical (v13) snapshots."
  },
  "important_caveats": [
    "The specific natural-product substrates (rhazimol, akuammiline) are highly specialized and would not be predictable from sequence alone; however, the question is answerable by mechanism-type elimination without knowing these substrates.",
    "The BAHD motif identification requires the model to recognize a ~5-residue motif within a 450-aa sequence, which is a reasonable but non-trivial pattern-recognition task.",
    "The annotation is based on experimental evidence from a 2022 publication, confirming the reaction is not merely computational inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (polyketide synthase, BAHD acyltransferase, amine oxidase, methyltransferase) with mutually exclusive cofactor requirements. The DFGWG motif uniquely identifies the BAHD class, leaving only Choice B mechanistically viable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A0A9E7LUL3 (AKS2_ALSSC, Akuammiline synthase 2, EC 2.3.1.322). The catalytic activity is explicitly annotated as 'rhazimol + acetyl-CoA = akuammiline + CoA + H(+)' with experimental evidence (ECO:0000269|PubMed:36349266, Wang et al. 2022, Chem. Sci.). The sequence match is confirmed in both current (v15) and historical (v13) snapshots.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the DFGWG motif (visible at positions ~370-374: 'DFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN'), which is the hallmark of the BAHD acyltransferase superfamily. BAHD acyltransferases catalyze acyl transfer from an acyl-CoA donor to an acceptor, releasing free CoA. This mechanism is consistent ONLY with Choice B (acetyl-CoA → CoA transfer). Choice A involves NADPH-dependent polyketide chain elongation with CO2 release (type III PKS mechanism). Choice C involves O2 and NADPH (CYP450/amine oxidase). Choice D involves S-adenosyl-L-methionine (SAM-dependent methyltransferase). None of these cofactor requirements are compatible with BAHD acyltransferase chemistry.",
    "missing_item_specific_fact": "The specific substrates (rhazimol as acceptor, akuammiline as product) cannot be deduced from the sequence alone, but they are not needed to eliminate the other three choices, which are mechanistically incompatible with BAHD acyltransferase catalysis.",
    "reason": "A model with general enzymology knowledge can identify the DFGWG motif, recognize it as diagnostic of BAHD acyltransferases, and eliminate choices A, C, and D based on their incompatible cofactors (NADPH, O2, SAM). The remaining choice B is the only acyl-CoA → CoA transfer reaction. This is a concrete mechanistic argument grounded in the sequence, not a database lookup of this specific enzyme's substrates."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four distinct enzyme classes (polyketide synthase, BAHD acyltransferase, amine oxidase, methyltransferase) with mutually exclusive cofactor requirements. The DFGWG motif uniquely identifies the BAHD class, leaving only Choice B mechanistically viable."
  },
  "important_caveats": [
    "The specific natural-product substrates (rhazimol, akuammiline) are highly specialized and would not be predictable from sequence alone; however, the question is answerable by mechanism-type elimination without knowing these substrates.",
    "The BAHD motif identification requires the model to recognize a ~5-residue motif within a 450-aa sequence, which is a reasonable but non-trivial pattern-recognition task.",
    "The annotation is based on experimental evidence from a 2022 publication, confirming the reaction is not merely computational inference."
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

**Accession:** `A0A9E7LUL3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
"A0A9E7LUL3"
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"2.3.1.322"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Akuammiline synthase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsAKS2"}]}}
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79624"}}],"reaction":{"ecNumber":"2.3.1.322","evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"name":"rhazimol + acetyl-CoA = akuammiline + CoA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79623"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57288"},{"database":"ChEBI","id":"CHEBI:141879"},{"database":"ChEBI","id":"CHEBI:230474"}]}}
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.133287+00:00.  

```text
ID   AKS2_ALSSC              Reviewed;         450 AA.
AC   A0A9E7LUL3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   03-MAY-2023, sequence version 1.
DT   28-JAN-2026, entry version 13.
DE   RecName: Full=Akuammiline synthase 2 {ECO:0000303|PubMed:36349266};
DE            Short=AsAKS2 {ECO:0000303|PubMed:36349266};
DE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};
GN   Name=AKS2 {ECO:0000303|PubMed:36349266};
GN   Synonyms=BAHD5 {ECO:0000303|PubMed:36349266};
OS   Alstonia scholaris (Dogbane) (Echites scholaris).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;
OC   Alstonia.
OX   NCBI_TaxID=52822;
```

Source SHA-256: `00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.133287+00:00.  

```text
DE   RecName: Full=Akuammiline synthase 2 {ECO:0000303|PubMed:36349266};
DE            Short=AsAKS2 {ECO:0000303|PubMed:36349266};
DE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};
```

Source SHA-256: `00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.133287+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=rhazimol + acetyl-CoA = akuammiline + CoA + H(+);
CC         Xref=Rhea:RHEA:79623, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,
CC         ChEBI:CHEBI:57288, ChEBI:CHEBI:141879, ChEBI:CHEBI:230474;
CC         EC=2.3.1.322; Evidence={ECO:0000269|PubMed:36349266};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79624;
CC         Evidence={ECO:0000269|PubMed:36349266};
```

Source SHA-256: `00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 89. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
