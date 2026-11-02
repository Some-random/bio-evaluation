# GO_biological_process_0176

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — sterol metabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELITLLSALLVLAIVSLSTFFVLYYNTPTKDGKTLPPGRMGWPFIGESYDFFAAGWKGKPESFIFDRLKKFAKGNLNGQFRTSLFGNKSIVVAGAAANKLLFSNEKKLVTMWWPPSIDKAFPSTAQLSANEEALLMRKFFPSFLIRREALQRYIPIMDDCTRRHFATGAWGPSDKIEAFNVTQDYTFWVACRVFMSIDAQEDPETVDSLFRHFNVLKAGIYSMHIDLPWTNFHHAMKASHAIRSAVEQIAKKRRAELAEGKAFPTQDMLSYMLETPITSAEDSKDGKAKYLNDADIGTKILGLLVGGHDTSSTVIAFFFKFMAENPHVYEAIYKEQMEVAATKAPGELLNWDDLQKMKYSWCAICEVMRLTPPVQGAFRQAITDFTHNGYLIPKGWKIYWSTHSTHRNPEIFPQPEKFDPTRFEGNGPPAFSFVPFGGGPRMCPGKEYARLQVLTFVHHIVTKFKWEQILPNEKIIVSPMPYPEKNLPLRMIARSESATLA

[Multiple Choices]
A. daunorubicin transport
B. L-fucose catabolic process
C. sterol metabolic process
D. cellular response to tumor necrosis factor
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The exact sequence has a UniProt GO annotation for sterol metabolic process, but it is computationally inferred (IEA:TreeGrafter), not direct experimental evidence for that process. The cited experimental characterization instead describes oxidation of beta-amyrin and oleanolic acid in triterpenoid/saponin biosynthesis, so the support for choice C is annotation-level and qualified.

Citations as saved: [C8](#evidence-c8), [H6](#evidence-h6), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [C9](#evidence-c9), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and conserved P450 features are consistent with a membrane-associated cytochrome P450, but do not identify its particular substrate or biological pathway among these choices.


**Missing item-specific fact**

> Distinguishing choice C requires the protein-specific functional or GO annotation linking this P450 to sterol metabolism; the experimentally cited function concerns beta-amyrin and oleanolic acid oxidation in triterpenoid/saponin biosynthesis.


**Reason**

> Generic sequence features identify a broad enzyme class, not the substrate-specific pathway needed to choose among the listed processes. The relevant annotation and characterized substrate specificity are external protein-specific facts.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The provided sequence alone does not establish any listed pathway. Choice C is the only one supported by a matching GO annotation, although that annotation is computational and the directly cited characterization is for triterpenoid/saponin biosynthesis.


### Important caveats

- The sequence matches the cited UniProt record, but the author’s exact data-source snapshot is unknown.
- The sterol-metabolism GO annotation is computationally inferred; the cited experimental evidence supports triterpenoid/saponin biosynthesis, not specifically sterol metabolism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and conserved P450 features are consistent with a membrane-associated cytochrome P450, but do not identify its particular substrate or biological pathway among these choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing choice C requires the protein-specific functional or GO annotation linking this P450 to sterol metabolism; the experimentally cited function concerns beta-amyrin and oleanolic acid oxidation in triterpenoid/saponin biosynthesis.",
    "reason": "Generic sequence features identify a broad enzyme class, not the substrate-specific pathway needed to choose among the listed processes. The relevant annotation and characterized substrate specificity are external protein-specific facts."
  },
  "case_id": "GO_biological_process_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H6",
      "C4",
      "C5",
      "H3",
      "C9",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence has a UniProt GO annotation for sterol metabolic process, but it is computationally inferred (IEA:TreeGrafter), not direct experimental evidence for that process. The cited experimental characterization instead describes oxidation of beta-amyrin and oleanolic acid in triterpenoid/saponin biosynthesis, so the support for choice C is annotation-level and qualified."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the author’s exact data-source snapshot is unknown.",
    "The sterol-metabolism GO annotation is computationally inferred; the cited experimental evidence supports triterpenoid/saponin biosynthesis, not specifically sterol metabolism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The provided sequence alone does not establish any listed pathway. Choice C is the only one supported by a matching GO annotation, although that annotation is computational and the directly cited characterization is for triterpenoid/saponin biosynthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence has a UniProt GO annotation for sterol metabolic process, but it is computationally inferred (IEA:TreeGrafter), not direct experimental evidence for that process. The cited experimental characterization instead describes oxidation of beta-amyrin and oleanolic acid in triterpenoid/saponin biosynthesis, so the support for choice C is annotation-level and qualified.",
    "evidence_ids": ["C8", "H6", "C4", "C5", "H3", "C9", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and conserved P450 features are consistent with a membrane-associated cytochrome P450, but do not identify its particular substrate or biological pathway among these choices.",
    "missing_item_specific_fact": "Distinguishing choice C requires the protein-specific functional or GO annotation linking this P450 to sterol metabolism; the experimentally cited function concerns beta-amyrin and oleanolic acid oxidation in triterpenoid/saponin biosynthesis.",
    "reason": "Generic sequence features identify a broad enzyme class, not the substrate-specific pathway needed to choose among the listed processes. The relevant annotation and characterized substrate specificity are external protein-specific facts."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The provided sequence alone does not establish any listed pathway. Choice C is the only one supported by a matching GO annotation, although that annotation is computational and the directly cited characterization is for triterpenoid/saponin biosynthesis."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the author’s exact data-source snapshot is unknown.",
    "The sterol-metabolism GO annotation is computationally inferred; the cited experimental evidence supports triterpenoid/saponin biosynthesis, not specifically sterol metabolism."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1JA93 (CYP716A379, Beta-amyrin 28-monooxygenase) does carry the GO:0016125 'sterol metabolic process' annotation (evidence C8/H6). However, this annotation is IEA:TreeGrafter (computational similarity inference), not experimental. The experimentally determined (IDA) annotations are GO:0016135 'saponin biosynthetic process' and GO:0016104 'triterpenoid biosynthetic process' (C7, C9). The protein's actual function is oxidation of beta-amyrin to oleanolic acid and then to echinocystic acid in the triterpene saponin pathway (C5/H3). Triterpenoids are structurally related to sterols via the isoprenoid pathway, making the IEA mapping to 'sterol metabolic process' a defensible but imprecise computational assignment. Among the four provided choices, C is the only one with any connection to this enzyme's actual biology.

Citations as saved: [C8](#evidence-c8), [H6](#evidence-h6), [C7](#evidence-c7), [H5](#evidence-h5), [C9](#evidence-c9), [H7](#evidence-h7), [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable cytochrome P450 heme-binding motif (FGGGPRMCPGKEY...C), identifying it as a P450 monooxygenase. The N-terminal hydrophobic signal peptide and overall composition indicate a plant membrane-associated enzyme. Among the four options: (A) daunorubicin transport requires a transporter/pore, not an oxidoreductase; (B) L-fucose catabolic process involves sugar-metabolizing enzymes, not P450s; (D) cellular response to TNF is an animal cytokine signaling process irrelevant to a plant P450. Only (C) sterol metabolic process is consistent with a plant P450 oxidizing lipid/terpenoid substrates. Elimination of the three clearly incompatible options leaves C as the sole viable answer.


**Missing item-specific fact**

> Precise identification that this is CYP716A379 involved in triterpene saponin biosynthesis (rather than canonical sterol biosynthesis) requires the specific PubMed:39043959 experimental data. However, this distinction is not needed to select C among the given options, since the other three are categorically incompatible.


**Reason**

> General biological reasoning—recognizing P450 architecture, plant origin, and the incompatibility of transporter/sugar-catabolism/animal-signaling functions with a plant monooxygenase—sufficiently eliminates A, B, and D. The remaining option C is the only lipid/metabolism-related choice. No protein-specific database lookup is strictly required to arrive at C via elimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are categorically incompatible with a plant cytochrome P450 oxidoreductase. Only C has any plausible connection. While 'saponin biosynthetic process' or 'triterpenoid biosynthetic process' would be more precise, they are not offered, and C is the closest available match.


### Important caveats

- The 'sterol metabolic process' annotation is IEA:TreeGrafter (computational), not experimentally verified. The experimentally supported GO terms are 'saponin biosynthetic process' and 'triterpenoid biosynthetic process.'
- Triterpenoids (beta-amyrin, oleanolic acid) are not sterols per se; the GO mapping is a broad computational inference through the isoprenoid/terpenoid hierarchy.
- The UniProt entry was first public in June 2025; the benchmark author's source snapshot is unknown. The sequence match is confirmed across available snapshots.
- The question asks for the 'primary biological process,' and the most accurate answer (saponin/triterpenoid biosynthesis) is absent from the options; C is the best available proxy.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif (FGGGPRMCPGKEY...C), identifying it as a P450 monooxygenase. The N-terminal hydrophobic signal peptide and overall composition indicate a plant membrane-associated enzyme. Among the four options: (A) daunorubicin transport requires a transporter/pore, not an oxidoreductase; (B) L-fucose catabolic process involves sugar-metabolizing enzymes, not P450s; (D) cellular response to TNF is an animal cytokine signaling process irrelevant to a plant P450. Only (C) sterol metabolic process is consistent with a plant P450 oxidizing lipid/terpenoid substrates. Elimination of the three clearly incompatible options leaves C as the sole viable answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification that this is CYP716A379 involved in triterpene saponin biosynthesis (rather than canonical sterol biosynthesis) requires the specific PubMed:39043959 experimental data. However, this distinction is not needed to select C among the given options, since the other three are categorically incompatible.",
    "reason": "General biological reasoning—recognizing P450 architecture, plant origin, and the incompatibility of transporter/sugar-catabolism/animal-signaling functions with a plant monooxygenase—sufficiently eliminates A, B, and D. The remaining option C is the only lipid/metabolism-related choice. No protein-specific database lookup is strictly required to arrive at C via elimination."
  },
  "case_id": "GO_biological_process_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H6",
      "C7",
      "H5",
      "C9",
      "H7",
      "C5",
      "H3",
      "C6",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1JA93 (CYP716A379, Beta-amyrin 28-monooxygenase) does carry the GO:0016125 'sterol metabolic process' annotation (evidence C8/H6). However, this annotation is IEA:TreeGrafter (computational similarity inference), not experimental. The experimentally determined (IDA) annotations are GO:0016135 'saponin biosynthetic process' and GO:0016104 'triterpenoid biosynthetic process' (C7, C9). The protein's actual function is oxidation of beta-amyrin to oleanolic acid and then to echinocystic acid in the triterpene saponin pathway (C5/H3). Triterpenoids are structurally related to sterols via the isoprenoid pathway, making the IEA mapping to 'sterol metabolic process' a defensible but imprecise computational assignment. Among the four provided choices, C is the only one with any connection to this enzyme's actual biology."
  },
  "important_caveats": [
    "The 'sterol metabolic process' annotation is IEA:TreeGrafter (computational), not experimentally verified. The experimentally supported GO terms are 'saponin biosynthetic process' and 'triterpenoid biosynthetic process.'",
    "Triterpenoids (beta-amyrin, oleanolic acid) are not sterols per se; the GO mapping is a broad computational inference through the isoprenoid/terpenoid hierarchy.",
    "The UniProt entry was first public in June 2025; the benchmark author's source snapshot is unknown. The sequence match is confirmed across available snapshots.",
    "The question asks for the 'primary biological process,' and the most accurate answer (saponin/triterpenoid biosynthesis) is absent from the options; C is the best available proxy."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are categorically incompatible with a plant cytochrome P450 oxidoreductase. Only C has any plausible connection. While 'saponin biosynthetic process' or 'triterpenoid biosynthetic process' would be more precise, they are not offered, and C is the closest available match."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1JA93 (CYP716A379, Beta-amyrin 28-monooxygenase) does carry the GO:0016125 'sterol metabolic process' annotation (evidence C8/H6). However, this annotation is IEA:TreeGrafter (computational similarity inference), not experimental. The experimentally determined (IDA) annotations are GO:0016135 'saponin biosynthetic process' and GO:0016104 'triterpenoid biosynthetic process' (C7, C9). The protein's actual function is oxidation of beta-amyrin to oleanolic acid and then to echinocystic acid in the triterpene saponin pathway (C5/H3). Triterpenoids are structurally related to sterols via the isoprenoid pathway, making the IEA mapping to 'sterol metabolic process' a defensible but imprecise computational assignment. Among the four provided choices, C is the only one with any connection to this enzyme's actual biology.",
    "evidence_ids": ["C8", "H6", "C7", "H5", "C9", "H7", "C5", "H3", "C6", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif (FGGGPRMCPGKEY...C), identifying it as a P450 monooxygenase. The N-terminal hydrophobic signal peptide and overall composition indicate a plant membrane-associated enzyme. Among the four options: (A) daunorubicin transport requires a transporter/pore, not an oxidoreductase; (B) L-fucose catabolic process involves sugar-metabolizing enzymes, not P450s; (D) cellular response to TNF is an animal cytokine signaling process irrelevant to a plant P450. Only (C) sterol metabolic process is consistent with a plant P450 oxidizing lipid/terpenoid substrates. Elimination of the three clearly incompatible options leaves C as the sole viable answer.",
    "missing_item_specific_fact": "Precise identification that this is CYP716A379 involved in triterpene saponin biosynthesis (rather than canonical sterol biosynthesis) requires the specific PubMed:39043959 experimental data. However, this distinction is not needed to select C among the given options, since the other three are categorically incompatible.",
    "reason": "General biological reasoning—recognizing P450 architecture, plant origin, and the incompatibility of transporter/sugar-catabolism/animal-signaling functions with a plant monooxygenase—sufficiently eliminates A, B, and D. The remaining option C is the only lipid/metabolism-related choice. No protein-specific database lookup is strictly required to arrive at C via elimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are categorically incompatible with a plant cytochrome P450 oxidoreductase. Only C has any plausible connection. While 'saponin biosynthetic process' or 'triterpenoid biosynthetic process' would be more precise, they are not offered, and C is the closest available match."
  },
  "important_caveats": [
    "The 'sterol metabolic process' annotation is IEA:TreeGrafter (computational), not experimentally verified. The experimentally supported GO terms are 'saponin biosynthetic process' and 'triterpenoid biosynthetic process.'",
    "Triterpenoids (beta-amyrin, oleanolic acid) are not sterols per se; the GO mapping is a broad computational inference through the isoprenoid/terpenoid hierarchy.",
    "The UniProt entry was first public in June 2025; the benchmark author's source snapshot is unknown. The sequence match is confirmed across available snapshots.",
    "The question asks for the 'primary biological process,' and the most accurate answer (saponin/triterpenoid biosynthesis) is absent from the options; C is the best available proxy."
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

**Accession:** `A0AAW1JA93` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"Cytochrome P450 716A379"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoCYP716A379"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"1.14.14.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Oleanolic acid 16-monooxygenase CYP716A379"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"1.14.14.126"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Beta-amyrin 28-monooxygenase CYP716A379"}}}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). An oxidoreductase that facilitates the oxidation of the methyl group to a carboxyl group at the C-28 position of beta-amyrin, resulting in the formation of oleanolic acid (PubMed:39043959). Catalyzes also the subsequent oxidation of the methyl group to a< carboxyl group at the C-16 alpha position of oleanolic acid, resulting in the formation of echinocystic acid (PubMed:39043959)"}]}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0016135","properties":[{"key":"GoTerm","value":"P:saponin biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"database":"GO","id":"GO:0016125","properties":[{"key":"GoTerm","value":"P:sterol metabolic process"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1JA93.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:36.226265+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39043959","source":"PubMed"}],"id":"GO:0016104","properties":[{"key":"GoTerm","value":"P:triterpenoid biosynthetic process"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `27c181003e93f8aa0a2da8a958615ca61dfb7285897a49953a7d49e212a4ee58`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)  
**Locator:** `lines 37-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:38.624320+00:00.  

```text
CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.
CC       saponarioside A and saponarioside B) biosynthetic pathway, leading to
CC       the production of natural products with detergent properties used as
CC       traditional sources of soap (PubMed:39043959). An oxidoreductase that
CC       facilitates the oxidation of the methyl group to a carboxyl group at
CC       the C-28 position of beta-amyrin, resulting in the formation of
CC       oleanolic acid (PubMed:39043959). Catalyzes also the subsequent
CC       oxidation of the methyl group to a< carboxyl group at the C-16 alpha
CC       position of oleanolic acid, resulting in the formation of echinocystic
CC       acid (PubMed:39043959). {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)  
**Locator:** `lines 69-70`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:38.624320+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)  
**Locator:** `lines 97-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:38.624320+00:00.  

```text
DR   GO; GO:0016135; P:saponin biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)  
**Locator:** `lines 98-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:38.624320+00:00.  

```text
DR   GO; GO:0016125; P:sterol metabolic process; IEA:TreeGrafter.
```

Source SHA-256: `49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1JA93?format=txt&versions=5)  
**Locator:** `lines 99-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:38.624320+00:00.  

```text
DR   GO; GO:0016104; P:triterpenoid biosynthetic process; IDA:UniProtKB.
```

Source SHA-256: `49a8fa89a90d2e808f90c867ed334920ce8c0b798c341c1bcfe19311ab8ea9a9`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 123728-123736`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016125
name: sterol metabolic process
namespace: biological_process
def: "The chemical reactions and pathways involving sterols, steroids with one or more hydroxyl groups and a hydrocarbon side-chain in the molecule." [ISBN:0198547684]
synonym: "sterol metabolism" EXACT []
xref: Reactome:R-HSA-211976 "Endogenous sterols"
is_a: GO:0008202 ! steroid metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 176. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
