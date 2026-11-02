# EC_number_0137

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.7.11.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVMKFTWRSIIPRCSKGIEEPEAEAEAEPETKKQDSKQGSFSRLAMIDLSYPSSRFTEDLSTSLAGSNLYVFTLEELKVITQCFSSANFLGEGGFGPVHKGFIDDNLRPGLEAQPVAVKLLDLEGLQGHREWLTEVVFLAQLSHPHLVKLIGYCCEDEHRLLVYEYMPRGSLENQLFAKYSVPLPWSTRMKIALGAAKGLAYLHEAEKPVIYRDFKASNILLDSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDKSRSPREQNLAEWARPMLNESRRLARIMDPKLEGQYSETGARKAAALAYQCLSHRAKQRPKMSDVVNILEPLLDYEETSVGTFVYTVPTHQNGGSPPKDDTDTKECEAKTELKKENGDHHNRHHHRRSHKSRDGHRHRNKSSSQSSVHSENYTSKQTLENGSNEECNID

[Multiple Choices]
A. 2.7.11.11
B. 2.1.1.395
C. 2.7.11.1
D. 1.14.15.9
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

> The exact sequence matches a UniProt entry annotated as EC 2.7.11.1. The EC assignment is supported by a PROSITE-ProRule computational annotation; the cited catalytic activity is also annotated with that evidence code, so this does not establish an independent experimental EC determination.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a protein-kinase domain, which supports a protein-phosphorylation function and distinguishes it from the methyltransferase and oxidoreductase choices. That general inference does not establish the precise EC assignment among kinase choices.


**Missing item-specific fact**

> The protein-specific kinase-family or functional annotation needed to distinguish EC 2.7.11.1 from the other kinase option.


**Reason**

> Selecting the complete EC number requires a protein-specific classification not supplied in the prompt. Recognizing the generic kinase motifs does not by itself establish the exact EC subclass.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Reviewer-only, sequence-matched annotation supports C. The sequence alone provides general kinase evidence but does not independently establish a competing EC assignment.


### Important caveats

- The annotation is computationally supported by PROSITE-ProRule, not demonstrated here by independent experimental evidence.
- The source accession and its annotations were reviewer-only and absent from the evaluated input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a protein-kinase domain, which supports a protein-phosphorylation function and distinguishes it from the methyltransferase and oxidoreductase choices. That general inference does not establish the precise EC assignment among kinase choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific kinase-family or functional annotation needed to distinguish EC 2.7.11.1 from the other kinase option.",
    "reason": "Selecting the complete EC number requires a protein-specific classification not supplied in the prompt. Recognizing the generic kinase motifs does not by itself establish the exact EC subclass."
  },
  "case_id": "EC_number_0137",
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
    "reason": "The exact sequence matches a UniProt entry annotated as EC 2.7.11.1. The EC assignment is supported by a PROSITE-ProRule computational annotation; the cited catalytic activity is also annotated with that evidence code, so this does not establish an independent experimental EC determination."
  },
  "important_caveats": [
    "The annotation is computationally supported by PROSITE-ProRule, not demonstrated here by independent experimental evidence.",
    "The source accession and its annotations were reviewer-only and absent from the evaluated input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only, sequence-matched annotation supports C. The sequence alone provides general kinase evidence but does not independently establish a competing EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as EC 2.7.11.1. The EC assignment is supported by a PROSITE-ProRule computational annotation; the cited catalytic activity is also annotated with that evidence code, so this does not establish an independent experimental EC determination.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a protein-kinase domain, which supports a protein-phosphorylation function and distinguishes it from the methyltransferase and oxidoreductase choices. That general inference does not establish the precise EC assignment among kinase choices.",
    "missing_item_specific_fact": "The protein-specific kinase-family or functional annotation needed to distinguish EC 2.7.11.1 from the other kinase option.",
    "reason": "Selecting the complete EC number requires a protein-specific classification not supplied in the prompt. Recognizing the generic kinase motifs does not by itself establish the exact EC subclass."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Reviewer-only, sequence-matched annotation supports C. The sequence alone provides general kinase evidence but does not independently establish a competing EC assignment."
  },
  "important_caveats": [
    "The annotation is computationally supported by PROSITE-ProRule, not demonstrated here by independent experimental evidence.",
    "The source accession and its annotations were reviewer-only and absent from the evaluated input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A5J5T2N2 (GbEIR5A, Gossypium barbadense) is annotated with EC 2.7.11.1 (non-specific serine/threonine-protein kinase), supported by catalytic activity reactions for both Ser and Thr phosphorylation. The sequence contains canonical protein kinase motifs: glycine-rich loop (GGFGPVHKGF), DFG motif (DFGLAK), activation segment, and APE motif (AAPEYIMT). The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU10027), indicating pattern-based computational inference rather than direct experimental substrate characterization, but the sequence motifs are unambiguous for a Ser/Thr protein kinase.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable protein kinase motifs: a glycine-rich loop (GGFGPVHKGF), the catalytic DFG motif (DFGLAK), an activation segment (DSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDK), and an APE motif. These definitively identify the protein as a protein kinase, eliminating EC 2.1.1.395 (methyltransferase, option B) and EC 1.14.15.9 (oxidoreductase/cytochrome P450, option D). Between options A (2.7.11.11, MAP3K) and C (2.7.11.1, non-specific Ser/Thr kinase): plant receptor-like cytoplasmic kinases (RLCKs) are a well-known class of general Ser/Thr kinases in plant immunity, not MAP3Ks. The absence of the characteristic MAP3K-specific docking domains and the overall RLCK architecture favor 2.7.11.1.


**Missing item-specific fact**

> The precise distinction between 2.7.11.1 and 2.7.11.11 ultimately rests on experimentally determined substrate specificity (whether it phosphorylates MAP2Ks). However, the general classification of plant RLCKs as non-specific Ser/Thr kinases is well-established biological knowledge.


**Reason**

> The kinase motifs are clearly identifiable from the sequence, allowing elimination of B and D. The plant RLCK context and general Ser/Thr kinase architecture support C over A through general biological knowledge of plant immune signaling kinases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the distinction between 2.7.11.1 and 2.7.11.11 is not trivially obvious from sequence alone, the plant RLCK context and the general convention of classifying such kinases as non-specific Ser/Thr kinases make C the most defensible answer. Options B and D are clearly eliminated by the kinase motifs.


### Important caveats

- The UniProt EC annotation uses ECO:0000255 (PROSITE-ProRule pattern matching), not direct experimental substrate specificity data. The 2.7.11.1 assignment is computational/pattern-based.
- The distinction between 2.7.11.1 and 2.7.11.11 in EC classification is partly a matter of annotation convention; 2.7.11.1 serves as a catch-all for Ser/Thr kinases lacking a more specific classification.
- The PubMed reference (39488762) documents function, interaction with V. dahliae EPD1, and phosphorylation sites but the EC assignment itself relies on PROSITE-ProRule pattern matching rather than in vitro substrate specificity assays.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase motifs: a glycine-rich loop (GGFGPVHKGF), the catalytic DFG motif (DFGLAK), an activation segment (DSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDK), and an APE motif. These definitively identify the protein as a protein kinase, eliminating EC 2.1.1.395 (methyltransferase, option B) and EC 1.14.15.9 (oxidoreductase/cytochrome P450, option D). Between options A (2.7.11.11, MAP3K) and C (2.7.11.1, non-specific Ser/Thr kinase): plant receptor-like cytoplasmic kinases (RLCKs) are a well-known class of general Ser/Thr kinases in plant immunity, not MAP3Ks. The absence of the characteristic MAP3K-specific docking domains and the overall RLCK architecture favor 2.7.11.1.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise distinction between 2.7.11.1 and 2.7.11.11 ultimately rests on experimentally determined substrate specificity (whether it phosphorylates MAP2Ks). However, the general classification of plant RLCKs as non-specific Ser/Thr kinases is well-established biological knowledge.",
    "reason": "The kinase motifs are clearly identifiable from the sequence, allowing elimination of B and D. The plant RLCK context and general Ser/Thr kinase architecture support C over A through general biological knowledge of plant immune signaling kinases."
  },
  "case_id": "EC_number_0137",
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
    "reason": "The UniProt entry A0A5J5T2N2 (GbEIR5A, Gossypium barbadense) is annotated with EC 2.7.11.1 (non-specific serine/threonine-protein kinase), supported by catalytic activity reactions for both Ser and Thr phosphorylation. The sequence contains canonical protein kinase motifs: glycine-rich loop (GGFGPVHKGF), DFG motif (DFGLAK), activation segment, and APE motif (AAPEYIMT). The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU10027), indicating pattern-based computational inference rather than direct experimental substrate characterization, but the sequence motifs are unambiguous for a Ser/Thr protein kinase."
  },
  "important_caveats": [
    "The UniProt EC annotation uses ECO:0000255 (PROSITE-ProRule pattern matching), not direct experimental substrate specificity data. The 2.7.11.1 assignment is computational/pattern-based.",
    "The distinction between 2.7.11.1 and 2.7.11.11 in EC classification is partly a matter of annotation convention; 2.7.11.1 serves as a catch-all for Ser/Thr kinases lacking a more specific classification.",
    "The PubMed reference (39488762) documents function, interaction with V. dahliae EPD1, and phosphorylation sites but the EC assignment itself relies on PROSITE-ProRule pattern matching rather than in vitro substrate specificity assays."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the distinction between 2.7.11.1 and 2.7.11.11 is not trivially obvious from sequence alone, the plant RLCK context and the general convention of classifying such kinases as non-specific Ser/Thr kinases make C the most defensible answer. Options B and D are clearly eliminated by the kinase motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A5J5T2N2 (GbEIR5A, Gossypium barbadense) is annotated with EC 2.7.11.1 (non-specific serine/threonine-protein kinase), supported by catalytic activity reactions for both Ser and Thr phosphorylation. The sequence contains canonical protein kinase motifs: glycine-rich loop (GGFGPVHKGF), DFG motif (DFGLAK), activation segment, and APE motif (AAPEYIMT). The annotation evidence code is ECO:0000255 (PROSITE-ProRule:PRU10027), indicating pattern-based computational inference rather than direct experimental substrate characterization, but the sequence motifs are unambiguous for a Ser/Thr protein kinase.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase motifs: a glycine-rich loop (GGFGPVHKGF), the catalytic DFG motif (DFGLAK), an activation segment (DSDYSAKLSDFGLAKDGPEGDKTHVSTRVMGTRGYAAPEYIMTGHLTAMSDVYSFGVVLLELLTGRRSLDK), and an APE motif. These definitively identify the protein as a protein kinase, eliminating EC 2.1.1.395 (methyltransferase, option B) and EC 1.14.15.9 (oxidoreductase/cytochrome P450, option D). Between options A (2.7.11.11, MAP3K) and C (2.7.11.1, non-specific Ser/Thr kinase): plant receptor-like cytoplasmic kinases (RLCKs) are a well-known class of general Ser/Thr kinases in plant immunity, not MAP3Ks. The absence of the characteristic MAP3K-specific docking domains and the overall RLCK architecture favor 2.7.11.1.",
    "missing_item_specific_fact": "The precise distinction between 2.7.11.1 and 2.7.11.11 ultimately rests on experimentally determined substrate specificity (whether it phosphorylates MAP2Ks). However, the general classification of plant RLCKs as non-specific Ser/Thr kinases is well-established biological knowledge.",
    "reason": "The kinase motifs are clearly identifiable from the sequence, allowing elimination of B and D. The plant RLCK context and general Ser/Thr kinase architecture support C over A through general biological knowledge of plant immune signaling kinases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the distinction between 2.7.11.1 and 2.7.11.11 is not trivially obvious from sequence alone, the plant RLCK context and the general convention of classifying such kinases as non-specific Ser/Thr kinases make C the most defensible answer. Options B and D are clearly eliminated by the kinase motifs."
  },
  "important_caveats": [
    "The UniProt EC annotation uses ECO:0000255 (PROSITE-ProRule pattern matching), not direct experimental substrate specificity data. The 2.7.11.1 assignment is computational/pattern-based.",
    "The distinction between 2.7.11.1 and 2.7.11.11 in EC classification is partly a matter of annotation convention; 2.7.11.1 serves as a catch-all for Ser/Thr kinases lacking a more specific classification.",
    "The PubMed reference (39488762) documents function, interaction with V. dahliae EPD1, and phosphorylation sites but the EC assignment itself relies on PROSITE-ProRule pattern matching rather than in vitro substrate specificity assays."
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

**Accession:** `A0A5J5T2N2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 17. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.786512+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39488762","source":"PubMed"}],"value":"EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39488762","source":"PubMed"}],"value":"GbEIR5A"}]}}
```

Source SHA-256: `2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.786512+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5J5T2N2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:28.786512+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `2ece754385a5f041030f1f4fddbd86bd00446105777fa2aac740d0360cfceeb6`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:31.043989+00:00.  

```text
DE   RecName: Full=EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase 5A {ECO:0000303|PubMed:39488762};
DE            Short=GbEIR5A {ECO:0000303|PubMed:39488762};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)  
**Locator:** `lines 52-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:31.043989+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5J5T2N2?format=txt&versions=17)  
**Locator:** `lines 58-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 17 / 1.  
**Retrieved:** 2026-11-02T04:25:31.043989+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `a27cf5e5e496f33f777075570513133dd9cab456f6ea93a4b85764e616bd6633`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 137. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
