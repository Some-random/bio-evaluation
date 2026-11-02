# cofactor_0133

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Mn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGRDARRLPLLPFLLLLLAAAAGVAESATDAEAIHDLARSVPALGWDGDNVCGFEGVTCERGGAGKVTELNLADRGLSGTLPDSLSSLTSLTALQLQGNALTGAVPSLARMGSLARLALDGNAFTSLPPDFLHGLTSLQYLTMENLPLPPWPVPDAIANCSSLDTFSASNASISGPFPAVLATLVSLRNLRLSYNNLTGGLPPELSSLIAMESLQLNNQRSDDKLSGPIDVIASMKSLKLLWIQSNKFTGPIPDLNGTQLEAFNVRDNMLTGVVPPSLTGLMSLKNVSLSNNNFQGPKPAFAAIPGQDEDSGNGFCLNTPGPCSPLTTTLLQVAEGFGYPYELAKTWKGNDPCSPAWVGIVCTSSDVSMINLSRKNLSGRISPALANLTRLARLDLSNNNLTGVIPDVLTTLPSLTVLNVANNRLTGEVPKFKPSVNVLAQGNLFGQSSGSSGGGGGSDGDSSSSDSAGGGKSKPNTGMIIGIIVAVIILFACIALLVHHRKKKNVEKFRPVSTKTSPAESEMMKIQVVGANGISNGSSAFPTELYSHVSAANSSNISELFESHGMQLSVEVLLKATNNFSEDCILGRGGFGVVFKGNLNGKLVAVKRCDSGTMGTKGQEEFLAEIDVLRKVRHRHLVALLGYCTHGNERLLVYEYMSGGTLREHLCDLQQSGFIPLTWTQRMTIALDVARGIEYLHGLAQETFIHRDLKPSNILLDQDLRAKVSDFGLVKLAKDTDKSLMTRIAGTFGYLAPEYATTGKVTTKVDVYAYGVILMEMITGRKVLDDSLPDDETHLVTIFRRNILDKEKFRKFVDPTLELSAEGWTSLLEVADLARHCTAREPYQRPDMCHCVNRLSSLVDQWKPTNIDEDDYEGETSEMGLHQQLEKWRCDDFTISDSDTFGSFNVPRKYNG

[Multiple Choices]
A. Ca(2+)
B. Mn(2+)
C. [2Fe-2S] cluster
D. pantetheine 4'-phosphate
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

> The sequence matches the rice WSS1 entry, which annotates Mn(2+) as a cofactor. However, the annotation is transferred by similarity from UniProtKB:P43298, not evidence of a direct measurement on this protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a protein kinase domain, which makes a metal cofactor more plausible than an iron-sulfur cluster or pantetheine phosphate. General kinase knowledge does not establish that this particular kinase uses Mn(2+) rather than another divalent ion.


**Missing item-specific fact**

> The protein-specific Mn(2+) cofactor annotation, or experimental evidence identifying its catalytic metal; the supplied input provides neither.


**Reason**

> Identifying the kinase-like domain can narrow the choices, but the exact metal assignment depends on a protein-specific annotation or measurement absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports the keyed choice as an annotation, though it is similarity-transferred rather than directly demonstrated here. The sequence alone does not resolve the exact metal.


### Important caveats

- The reviewer-only UniProt records match the supplied sequence, but the author’s source snapshot is unknown.
- The cited cofactor evidence is computationally transferred from UniProtKB:P43298; it should not be described as direct experimental confirmation for WSS1.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a protein kinase domain, which makes a metal cofactor more plausible than an iron-sulfur cluster or pantetheine phosphate. General kinase knowledge does not establish that this particular kinase uses Mn(2+) rather than another divalent ion.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific Mn(2+) cofactor annotation, or experimental evidence identifying its catalytic metal; the supplied input provides neither.",
    "reason": "Identifying the kinase-like domain can narrow the choices, but the exact metal assignment depends on a protein-specific annotation or measurement absent from the question."
  },
  "case_id": "cofactor_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the rice WSS1 entry, which annotates Mn(2+) as a cofactor. However, the annotation is transferred by similarity from UniProtKB:P43298, not evidence of a direct measurement on this protein."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence, but the author’s source snapshot is unknown.",
    "The cited cofactor evidence is computationally transferred from UniProtKB:P43298; it should not be described as direct experimental confirmation for WSS1."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports the keyed choice as an annotation, though it is similarity-transferred rather than directly demonstrated here. The sequence alone does not resolve the exact metal."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the rice WSS1 entry, which annotates Mn(2+) as a cofactor. However, the annotation is transferred by similarity from UniProtKB:P43298, not evidence of a direct measurement on this protein.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a protein kinase domain, which makes a metal cofactor more plausible than an iron-sulfur cluster or pantetheine phosphate. General kinase knowledge does not establish that this particular kinase uses Mn(2+) rather than another divalent ion.",
    "missing_item_specific_fact": "The protein-specific Mn(2+) cofactor annotation, or experimental evidence identifying its catalytic metal; the supplied input provides neither.",
    "reason": "Identifying the kinase-like domain can narrow the choices, but the exact metal assignment depends on a protein-specific annotation or measurement absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports the keyed choice as an annotation, though it is similarity-transferred rather than directly demonstrated here. The sequence alone does not resolve the exact metal."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence, but the author’s source snapshot is unknown.",
    "The cited cofactor evidence is computationally transferred from UniProtKB:P43298; it should not be described as direct experimental confirmation for WSS1."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q2R560 (WSS1_ORYSJ, Rice WATER-SOAKED SPOT1) explicitly annotates Mn(2+) (ChEBI:CHEBI:29035) as the cofactor. The evidence code is ECO:0000250 (inferred by similarity from P43298), meaning this is a computational/similarity-based inference rather than direct experimental measurement. The protein is classified as a serine/threonine-protein kinase (EC 2.7.11.1), a receptor-like kinase with LRR extracellular domain and a canonical kinase domain (GGFGVVFKG glycine-rich loop, HRD catalytic motif, DFG motif visible in the sequence). While Mg(2+) is the more canonical kinase metal cofactor, the database annotation for this specific entry lists Mn(2+), and the answer key matches that annotation. The annotation is present, sequence-matched, and consistent across historical and current entry versions.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unambiguous serine/threonine kinase domain motifs: the glycine-rich loop (GGFGVVFKG), the HRD catalytic motif (HRDLKPSN), and the DFG motif (DFGLVKL), identifying the protein as a protein kinase. Protein kinases require a divalent metal ion to coordinate ATP phosphates during phosphotransfer. Among the four options, Mn(2+) is the only divalent metal ion capable of serving as a kinase active-site cofactor. &#91;2Fe-2S&#93; clusters are electron-transfer cofactors (ferredoxins, Rieske proteins), pantetheine 4'-phosphate is the prosthetic group of acyl carrier proteins in fatty acid biosynthesis, and Ca(2+) is not a standard kinase active-site cofactor (Ca2+ signaling operates through calmodulin/CaMK complexes, not direct kinase coordination). Thus, identifying the kinase domain and eliminating non-kinase cofactors provides a meaningful reasoning path to select Mn(2+).


**Missing item-specific fact**

> The specific database annotation assigning Mn(2+) (rather than the more typical Mg(2+)) to this particular WSS1 kinase is a similarity-inferred annotation (ECO:0000250) not derivable from sequence alone. However, since Mg(2+) is not among the answer choices, the question is answerable by elimination without needing this specific annotation.


**Reason**

> The kinase domain motifs are directly readable from the sequence, and the elimination of &#91;2Fe-2S&#93;, pantetheine 4'-phosphate, and Ca(2+) as non-kinase cofactors is standard biochemistry. The question is answerable because Mg(2+), the more typical kinase cofactor, is absent from the options, making Mn(2+) the only kinase-compatible metal. This is a valid reasoning path, though somewhat dependent on the particular set of distractors chosen.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the four options, only Mn(2+) is a plausible kinase metal cofactor. Ca(2+) is not a direct kinase active-site cofactor; &#91;2Fe-2S&#93; and pantetheine 4'-phosphate serve entirely different enzyme classes. No other option is defensible for a serine/threonine kinase.


### Important caveats

- The Mn(2+) annotation is inferred by similarity (ECO:0000250 from P43298), not experimentally measured for WSS1 itself. The canonical kinase cofactor is Mg(2+), which is absent from the options.
- The question's answerability partly depends on Mg(2+) not being offered as a distractor; if Mg(2+) were included, the question would become ambiguous between the database annotation (Mn) and general kinase biochemistry (Mg).
- The protein is a plant receptor-like kinase (RLK) with LRR extracellular domain, transmembrane region, and intracellular kinase domain, consistent with the EC 2.7.11.1 assignment.
- The UniProt entry was first publicly released on 2025-02-05, after many benchmark construction dates; the author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unambiguous serine/threonine kinase domain motifs: the glycine-rich loop (GGFGVVFKG), the HRD catalytic motif (HRDLKPSN), and the DFG motif (DFGLVKL), identifying the protein as a protein kinase. Protein kinases require a divalent metal ion to coordinate ATP phosphates during phosphotransfer. Among the four options, Mn(2+) is the only divalent metal ion capable of serving as a kinase active-site cofactor. [2Fe-2S] clusters are electron-transfer cofactors (ferredoxins, Rieske proteins), pantetheine 4'-phosphate is the prosthetic group of acyl carrier proteins in fatty acid biosynthesis, and Ca(2+) is not a standard kinase active-site cofactor (Ca2+ signaling operates through calmodulin/CaMK complexes, not direct kinase coordination). Thus, identifying the kinase domain and eliminating non-kinase cofactors provides a meaningful reasoning path to select Mn(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific database annotation assigning Mn(2+) (rather than the more typical Mg(2+)) to this particular WSS1 kinase is a similarity-inferred annotation (ECO:0000250) not derivable from sequence alone. However, since Mg(2+) is not among the answer choices, the question is answerable by elimination without needing this specific annotation.",
    "reason": "The kinase domain motifs are directly readable from the sequence, and the elimination of [2Fe-2S], pantetheine 4'-phosphate, and Ca(2+) as non-kinase cofactors is standard biochemistry. The question is answerable because Mg(2+), the more typical kinase cofactor, is absent from the options, making Mn(2+) the only kinase-compatible metal. This is a valid reasoning path, though somewhat dependent on the particular set of distractors chosen."
  },
  "case_id": "cofactor_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q2R560 (WSS1_ORYSJ, Rice WATER-SOAKED SPOT1) explicitly annotates Mn(2+) (ChEBI:CHEBI:29035) as the cofactor. The evidence code is ECO:0000250 (inferred by similarity from P43298), meaning this is a computational/similarity-based inference rather than direct experimental measurement. The protein is classified as a serine/threonine-protein kinase (EC 2.7.11.1), a receptor-like kinase with LRR extracellular domain and a canonical kinase domain (GGFGVVFKG glycine-rich loop, HRD catalytic motif, DFG motif visible in the sequence). While Mg(2+) is the more canonical kinase metal cofactor, the database annotation for this specific entry lists Mn(2+), and the answer key matches that annotation. The annotation is present, sequence-matched, and consistent across historical and current entry versions."
  },
  "important_caveats": [
    "The Mn(2+) annotation is inferred by similarity (ECO:0000250 from P43298), not experimentally measured for WSS1 itself. The canonical kinase cofactor is Mg(2+), which is absent from the options.",
    "The question's answerability partly depends on Mg(2+) not being offered as a distractor; if Mg(2+) were included, the question would become ambiguous between the database annotation (Mn) and general kinase biochemistry (Mg).",
    "The protein is a plant receptor-like kinase (RLK) with LRR extracellular domain, transmembrane region, and intracellular kinase domain, consistent with the EC 2.7.11.1 assignment.",
    "The UniProt entry was first publicly released on 2025-02-05, after many benchmark construction dates; the author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four options, only Mn(2+) is a plausible kinase metal cofactor. Ca(2+) is not a direct kinase active-site cofactor; [2Fe-2S] and pantetheine 4'-phosphate serve entirely different enzyme classes. No other option is defensible for a serine/threonine kinase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q2R560 (WSS1_ORYSJ, Rice WATER-SOAKED SPOT1) explicitly annotates Mn(2+) (ChEBI:CHEBI:29035) as the cofactor. The evidence code is ECO:0000250 (inferred by similarity from P43298), meaning this is a computational/similarity-based inference rather than direct experimental measurement. The protein is classified as a serine/threonine-protein kinase (EC 2.7.11.1), a receptor-like kinase with LRR extracellular domain and a canonical kinase domain (GGFGVVFKG glycine-rich loop, HRD catalytic motif, DFG motif visible in the sequence). While Mg(2+) is the more canonical kinase metal cofactor, the database annotation for this specific entry lists Mn(2+), and the answer key matches that annotation. The annotation is present, sequence-matched, and consistent across historical and current entry versions.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unambiguous serine/threonine kinase domain motifs: the glycine-rich loop (GGFGVVFKG), the HRD catalytic motif (HRDLKPSN), and the DFG motif (DFGLVKL), identifying the protein as a protein kinase. Protein kinases require a divalent metal ion to coordinate ATP phosphates during phosphotransfer. Among the four options, Mn(2+) is the only divalent metal ion capable of serving as a kinase active-site cofactor. [2Fe-2S] clusters are electron-transfer cofactors (ferredoxins, Rieske proteins), pantetheine 4'-phosphate is the prosthetic group of acyl carrier proteins in fatty acid biosynthesis, and Ca(2+) is not a standard kinase active-site cofactor (Ca2+ signaling operates through calmodulin/CaMK complexes, not direct kinase coordination). Thus, identifying the kinase domain and eliminating non-kinase cofactors provides a meaningful reasoning path to select Mn(2+).",
    "missing_item_specific_fact": "The specific database annotation assigning Mn(2+) (rather than the more typical Mg(2+)) to this particular WSS1 kinase is a similarity-inferred annotation (ECO:0000250) not derivable from sequence alone. However, since Mg(2+) is not among the answer choices, the question is answerable by elimination without needing this specific annotation.",
    "reason": "The kinase domain motifs are directly readable from the sequence, and the elimination of [2Fe-2S], pantetheine 4'-phosphate, and Ca(2+) as non-kinase cofactors is standard biochemistry. The question is answerable because Mg(2+), the more typical kinase cofactor, is absent from the options, making Mn(2+) the only kinase-compatible metal. This is a valid reasoning path, though somewhat dependent on the particular set of distractors chosen."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the four options, only Mn(2+) is a plausible kinase metal cofactor. Ca(2+) is not a direct kinase active-site cofactor; [2Fe-2S] and pantetheine 4'-phosphate serve entirely different enzyme classes. No other option is defensible for a serine/threonine kinase."
  },
  "important_caveats": [
    "The Mn(2+) annotation is inferred by similarity (ECO:0000250 from P43298), not experimentally measured for WSS1 itself. The canonical kinase cofactor is Mg(2+), which is absent from the options.",
    "The question's answerability partly depends on Mg(2+) not being offered as a distractor; if Mg(2+) were included, the question would become ambiguous between the database annotation (Mn) and general kinase biochemistry (Mg).",
    "The protein is a plant receptor-like kinase (RLK) with LRR extracellular domain, transmembrane region, and intracellular kinase domain, consistent with the EC 2.7.11.1 assignment.",
    "The UniProt entry was first publicly released on 2025-02-05, after many benchmark construction dates; the author source snapshot is unknown."
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

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2R560.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
"Q2R560"
```

Source SHA-256: `6134946c5befacc9a9d4eee6c7262603fd779f3b8b073ce00fe2d5c0e1a621c4`.

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
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.782611+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29035"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P43298","source":"UniProtKB"}],"name":"Mn(2+)"}],"commentType":"COFACTOR"}
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
**Locator:** `lines 96-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-01T06:28:32.565844+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;
CC         Evidence={ECO:0000250|UniProtKB:P43298};
```

Source SHA-256: `8a1500792a74c38b22c2f5627966de80a760b1fed597a74e00b3d2510fcaa15a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
