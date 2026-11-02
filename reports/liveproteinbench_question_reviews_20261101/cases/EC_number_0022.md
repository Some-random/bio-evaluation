# EC_number_0022

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.7.11.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGRDARRLPLLPFLLLLLAAAAGVAESATDAEAIHDLARSVPALGWDGDNVCGFEGVTCERGGAGKVTELNLADRGLSGTLPDSLSSLTSLTALQLQGNALTGAVPSLARMGSLARLALDGNAFTSLPPDFLHGLTSLQYLTMENLPLPPWPVPDAIANCSSLDTFSASNASISGPFPAVLATLVSLRNLRLSYNNLTGGLPPELSSLIAMESLQLNNQRSDDKLSGPIDVIASMKSLKLLWIQSNKFTGPIPDLNGTQLEAFNVRDNMLTGVVPPSLTGLMSLKNVSLSNNNFQGPKPAFAAIPGQDEDSGNGFCLNTPGPCSPLTTTLLQVAEGFGYPYELAKTWKGNDPCSPAWVGIVCTSSDVSMINLSRKNLSGRISPALANLTRLARLDLSNNNLTGVIPDVLTTLPSLTVLNVANNRLTGEVPKFKPSVNVLAQGNLFGQSSGSSGGGGGSDGDSSSSDSAGGGKSKPNTGMIIGIIVAVIILFACIALLVHHRKKKNVEKFRPVSTKTSPAESEMMKIQVVGANGISNGSSAFPTELYSHVSAANSSNISELFESHGMQLSVEVLLKATNNFSEDCILGRGGFGVVFKGNLNGKLVAVKRCDSGTMGTKGQEEFLAEIDVLRKVRHRHLVALLGYCTHGNERLLVYEYMSGGTLREHLCDLQQSGFIPLTWTQRMTIALDVARGIEYLHGLAQETFIHRDLKPSNILLDQDLRAKVSDFGLVKLAKDTDKSLMTRIAGTFGYLAPEYATTGKVTTKVDVYAYGVILMEMITGRKVLDDSLPDDETHLVTIFRRNILDKEKFRKFVDPTLELSAEGWTSLLEVADLARHCTAREPYQRPDMCHCVNRLSSLVDQWKPTNIDEDDYEGETSEMGLHQQLEKWRCDDFTISDSDTFGSFNVPRKYNG

[Multiple Choices]
A. 2.7.11.11
B. 3.1.26.3
C. 2.1.1.353
D. 2.7.11.1
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the 912-aa rice WSS1 sequence. UniProt assigns EC 2.7.11.1 and serine/threonine phosphorylation reactions, but the annotation cites evidence transferred by similarity from UniProtKB:P43298 (ECO:0000250), not direct experimental evidence for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a receptor-like architecture, including an extracellular repeat-rich region, a transmembrane segment, and a cytoplasmic protein-kinase domain with conserved kinase motifs. This supports a receptor protein kinase and makes the broad protein-serine/threonine kinase choice D more plausible than the myosin-light-chain-specific kinase choice A, or the nuclease and methyltransferase choices.


**Missing item-specific fact**

> Directly establishing substrate specificity would require protein-specific functional evidence; the provided sequence supports the receptor-kinase interpretation but does not itself report an experimental substrate assay.


**Reason**

> The sequence and choices provide meaningful biological grounds for distinguishing D, though the precise EC assignment is also supported by a similarity-based database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The kinase-domain and receptor-like architecture favors D; the other kinase option specifies myosin-light-chain activity, which is not indicated by this plant receptor-like sequence.


### Important caveats

- The UniProt EC and catalytic-activity annotations are similarity-based transfers, not evidence of direct experimental characterization of this exact protein.
- The reviewer-only sequence match and annotations were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a receptor-like architecture, including an extracellular repeat-rich region, a transmembrane segment, and a cytoplasmic protein-kinase domain with conserved kinase motifs. This supports a receptor protein kinase and makes the broad protein-serine/threonine kinase choice D more plausible than the myosin-light-chain-specific kinase choice A, or the nuclease and methyltransferase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Directly establishing substrate specificity would require protein-specific functional evidence; the provided sequence supports the receptor-kinase interpretation but does not itself report an experimental substrate assay.",
    "reason": "The sequence and choices provide meaningful biological grounds for distinguishing D, though the precise EC assignment is also supported by a similarity-based database annotation."
  },
  "case_id": "EC_number_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the 912-aa rice WSS1 sequence. UniProt assigns EC 2.7.11.1 and serine/threonine phosphorylation reactions, but the annotation cites evidence transferred by similarity from UniProtKB:P43298 (ECO:0000250), not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The UniProt EC and catalytic-activity annotations are similarity-based transfers, not evidence of direct experimental characterization of this exact protein.",
    "The reviewer-only sequence match and annotations were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase-domain and receptor-like architecture favors D; the other kinase option specifies myosin-light-chain activity, which is not indicated by this plant receptor-like sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the 912-aa rice WSS1 sequence. UniProt assigns EC 2.7.11.1 and serine/threonine phosphorylation reactions, but the annotation cites evidence transferred by similarity from UniProtKB:P43298 (ECO:0000250), not direct experimental evidence for this sequence.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a receptor-like architecture, including an extracellular repeat-rich region, a transmembrane segment, and a cytoplasmic protein-kinase domain with conserved kinase motifs. This supports a receptor protein kinase and makes the broad protein-serine/threonine kinase choice D more plausible than the myosin-light-chain-specific kinase choice A, or the nuclease and methyltransferase choices.",
    "missing_item_specific_fact": "Directly establishing substrate specificity would require protein-specific functional evidence; the provided sequence supports the receptor-kinase interpretation but does not itself report an experimental substrate assay.",
    "reason": "The sequence and choices provide meaningful biological grounds for distinguishing D, though the precise EC assignment is also supported by a similarity-based database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase-domain and receptor-like architecture favors D; the other kinase option specifies myosin-light-chain activity, which is not indicated by this plant receptor-like sequence."
  },
  "important_caveats": [
    "The UniProt EC and catalytic-activity annotations are similarity-based transfers, not evidence of direct experimental characterization of this exact protein.",
    "The reviewer-only sequence match and annotations were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2R560 (WSS1_ORYSJ) annotates this protein with EC 2.7.11.1 (non-specific serine/threonine protein kinase), matching the author's key D. However, the evidence code is ECO:0000250 (inferred by similarity from P43298), meaning the EC assignment is a computational transfer rather than direct experimental characterization of this rice protein's substrate specificity. The protein's domain architecture (LRR extracellular domain, transmembrane helix, intracellular kinase domain with GxGxxG, HRD, and DFG motifs) is fully consistent with a serine/threonine protein kinase, making 2.7.11.1 a reasonable classification.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unambiguous protein kinase domain signatures: a glycine-rich loop (GRGGFGVVFKG), the catalytic HRD motif (HRDLKPSNILLDQ), the DFG motif (DFGLVKLAKDTDK), and an activation loop. Combined with the LRR extracellular repeats and a single transmembrane helix, this is a classic plant receptor-like kinase (RLK) with serine/threonine kinase activity. This immediately eliminates B (3.1.26.3, endoribonuclease) and C (2.1.1.353, methyltransferase) as mechanistically incompatible. Between A (2.7.11.11) and D (2.7.11.1): EC 2.7.11.1 is the standard 'non-specific serine/threonine protein kinase' designation applied to protein kinases lacking characterized specific substrate preference, which is the default for most plant RLKs. EC 2.7.11.11 does not appear to be a valid EC number in the current nomenclature (the 2.7.11.x series skips 11), making it a non-existent distractor that can be eliminated by EC nomenclature knowledge.


**Missing item-specific fact**

> If EC 2.7.11.11 were a valid EC number for a specific kinase family, distinguishing it from 2.7.11.1 would require knowing the specific phosphorylation substrate of this particular WSS1 protein, which is not determinable from sequence alone. However, the kinase domain architecture is generic (no tyrosine-kinase-specific features), and the 'non-specific' designation 2.7.11.1 is the default for uncharacterized serine/threonine kinases.


**Reason**

> The sequence provides strong structural evidence for serine/threonine kinase activity (eliminates B, C). The distinction between 2.7.11.1 and 2.7.11.11 rests on EC nomenclature validity (2.7.11.11 likely does not exist) and the default generic classification for plant RLKs, both of which are accessible through general biological and nomenclature knowledge rather than memorizing a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B (endoribonuclease) and C (methyltransferase) are mechanistically incompatible with the observed kinase domain. A (2.7.11.11) appears to be an invalid EC number. D (2.7.11.1) is the standard generic serine/threonine protein kinase EC and matches the database annotation. No other option is defensible.


### Important caveats

- The EC 2.7.11.1 annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity from P43298), not direct experimental verification for this rice WSS1 protein. The actual substrate specificity of WSS1 has not been experimentally determined.
- The protein is named 'Receptor protein kinase WSS1' and functions in chloroplast development and leaf senescence in rice, but its direct phosphorylation targets remain uncharacterized, which is why the generic EC 2.7.11.1 is assigned.
- The validity of EC 2.7.11.11 as a real EC number could not be independently confirmed by the reviewer; if it were valid for a specific kinase family, the A-vs-D distinction would become lookup-dependent.
- The UniProt entry was first publicly released on 2025-02-05 (entry version 23 at the historical cutoff), so this annotation postdates many training data cutoffs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unambiguous protein kinase domain signatures: a glycine-rich loop (GRGGFGVVFKG), the catalytic HRD motif (HRDLKPSNILLDQ), the DFG motif (DFGLVKLAKDTDK), and an activation loop. Combined with the LRR extracellular repeats and a single transmembrane helix, this is a classic plant receptor-like kinase (RLK) with serine/threonine kinase activity. This immediately eliminates B (3.1.26.3, endoribonuclease) and C (2.1.1.353, methyltransferase) as mechanistically incompatible. Between A (2.7.11.11) and D (2.7.11.1): EC 2.7.11.1 is the standard 'non-specific serine/threonine protein kinase' designation applied to protein kinases lacking characterized specific substrate preference, which is the default for most plant RLKs. EC 2.7.11.11 does not appear to be a valid EC number in the current nomenclature (the 2.7.11.x series skips 11), making it a non-existent distractor that can be eliminated by EC nomenclature knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "If EC 2.7.11.11 were a valid EC number for a specific kinase family, distinguishing it from 2.7.11.1 would require knowing the specific phosphorylation substrate of this particular WSS1 protein, which is not determinable from sequence alone. However, the kinase domain architecture is generic (no tyrosine-kinase-specific features), and the 'non-specific' designation 2.7.11.1 is the default for uncharacterized serine/threonine kinases.",
    "reason": "The sequence provides strong structural evidence for serine/threonine kinase activity (eliminates B, C). The distinction between 2.7.11.1 and 2.7.11.11 rests on EC nomenclature validity (2.7.11.11 likely does not exist) and the default generic classification for plant RLKs, both of which are accessible through general biological and nomenclature knowledge rather than memorizing a specific database entry."
  },
  "case_id": "EC_number_0022",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2R560 (WSS1_ORYSJ) annotates this protein with EC 2.7.11.1 (non-specific serine/threonine protein kinase), matching the author's key D. However, the evidence code is ECO:0000250 (inferred by similarity from P43298), meaning the EC assignment is a computational transfer rather than direct experimental characterization of this rice protein's substrate specificity. The protein's domain architecture (LRR extracellular domain, transmembrane helix, intracellular kinase domain with GxGxxG, HRD, and DFG motifs) is fully consistent with a serine/threonine protein kinase, making 2.7.11.1 a reasonable classification."
  },
  "important_caveats": [
    "The EC 2.7.11.1 annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity from P43298), not direct experimental verification for this rice WSS1 protein. The actual substrate specificity of WSS1 has not been experimentally determined.",
    "The protein is named 'Receptor protein kinase WSS1' and functions in chloroplast development and leaf senescence in rice, but its direct phosphorylation targets remain uncharacterized, which is why the generic EC 2.7.11.1 is assigned.",
    "The validity of EC 2.7.11.11 as a real EC number could not be independently confirmed by the reviewer; if it were valid for a specific kinase family, the A-vs-D distinction would become lookup-dependent.",
    "The UniProt entry was first publicly released on 2025-02-05 (entry version 23 at the historical cutoff), so this annotation postdates many training data cutoffs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B (endoribonuclease) and C (methyltransferase) are mechanistically incompatible with the observed kinase domain. A (2.7.11.11) appears to be an invalid EC number. D (2.7.11.1) is the standard generic serine/threonine protein kinase EC and matches the database annotation. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0022",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2R560 (WSS1_ORYSJ) annotates this protein with EC 2.7.11.1 (non-specific serine/threonine protein kinase), matching the author's key D. However, the evidence code is ECO:0000250 (inferred by similarity from P43298), meaning the EC assignment is a computational transfer rather than direct experimental characterization of this rice protein's substrate specificity. The protein's domain architecture (LRR extracellular domain, transmembrane helix, intracellular kinase domain with GxGxxG, HRD, and DFG motifs) is fully consistent with a serine/threonine protein kinase, making 2.7.11.1 a reasonable classification.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unambiguous protein kinase domain signatures: a glycine-rich loop (GRGGFGVVFKG), the catalytic HRD motif (HRDLKPSNILLDQ), the DFG motif (DFGLVKLAKDTDK), and an activation loop. Combined with the LRR extracellular repeats and a single transmembrane helix, this is a classic plant receptor-like kinase (RLK) with serine/threonine kinase activity. This immediately eliminates B (3.1.26.3, endoribonuclease) and C (2.1.1.353, methyltransferase) as mechanistically incompatible. Between A (2.7.11.11) and D (2.7.11.1): EC 2.7.11.1 is the standard 'non-specific serine/threonine protein kinase' designation applied to protein kinases lacking characterized specific substrate preference, which is the default for most plant RLKs. EC 2.7.11.11 does not appear to be a valid EC number in the current nomenclature (the 2.7.11.x series skips 11), making it a non-existent distractor that can be eliminated by EC nomenclature knowledge.",
    "missing_item_specific_fact": "If EC 2.7.11.11 were a valid EC number for a specific kinase family, distinguishing it from 2.7.11.1 would require knowing the specific phosphorylation substrate of this particular WSS1 protein, which is not determinable from sequence alone. However, the kinase domain architecture is generic (no tyrosine-kinase-specific features), and the 'non-specific' designation 2.7.11.1 is the default for uncharacterized serine/threonine kinases.",
    "reason": "The sequence provides strong structural evidence for serine/threonine kinase activity (eliminates B, C). The distinction between 2.7.11.1 and 2.7.11.11 rests on EC nomenclature validity (2.7.11.11 likely does not exist) and the default generic classification for plant RLKs, both of which are accessible through general biological and nomenclature knowledge rather than memorizing a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B (endoribonuclease) and C (methyltransferase) are mechanistically incompatible with the observed kinase domain. A (2.7.11.11) appears to be an invalid EC number. D (2.7.11.1) is the standard generic serine/threonine protein kinase EC and matches the database annotation. No other option is defensible."
  },
  "important_caveats": [
    "The EC 2.7.11.1 annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity from P43298), not direct experimental verification for this rice WSS1 protein. The actual substrate specificity of WSS1 has not been experimentally determined.",
    "The protein is named 'Receptor protein kinase WSS1' and functions in chloroplast development and leaf senescence in rice, but its direct phosphorylation targets remain uncharacterized, which is why the generic EC 2.7.11.1 is assigned.",
    "The validity of EC 2.7.11.11 as a real EC number could not be independently confirmed by the reviewer; if it were valid for a specific kinase family, the A-vs-D distinction would become lookup-dependent.",
    "The UniProt entry was first publicly released on 2025-02-05 (entry version 23 at the historical cutoff), so this annotation postdates many training data cutoffs."
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

**Accession:** `Q2R560` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 23. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35693165","source":"PubMed"}],"value":"Protein WATER-SOAKED SPOT1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"35693165","source":"PubMed"}],"value":"OsWSS1"}]}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P43298","source":"UniProtKB"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Receptor protein kinase WSS1"}}}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000250","id":"P43298","source":"UniProtKB"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000250","id":"P43298","source":"UniProtKB"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2R560?format=txt&versions=23)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
DE   RecName: Full=Receptor protein kinase WSS1 {ECO:0000305};
DE            EC=2.7.11.1 {ECO:0000250|UniProtKB:P43298};
DE   AltName: Full=Protein WATER-SOAKED SPOT1 {ECO:0000303|PubMed:35693165};
DE            Short=OsWSS1 {ECO:0000303|PubMed:35693165};
DE   Flags: Precursor;
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2R560?format=txt&versions=23)  
**Locator:** `lines 84-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000250|UniProtKB:P43298};
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2R560?format=txt&versions=23)  
**Locator:** `lines 90-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000250|UniProtKB:P43298};
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 22. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
