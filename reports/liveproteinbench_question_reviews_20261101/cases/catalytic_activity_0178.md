# catalytic_activity_0178

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1-&gt;4)-beta-linkages in chitin and chitodextrins.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFPKIFLTAATALLSAKSTFAQTYSSCNPLFTTGCPANTALGKSIDVDFTSGSVNSFDGSGDITYDSNGASFTVAKSGDAPTLSSIFYIMFGKVQITMKAAPGAGIVSTLVLQSDDLDEIDMEWLGADDTEVQTNYFGKGKVTDYNRGAFNPAANNQGEFITYTIEWTSEQVVWSVGSTVVRVLTPATADTDQYPQSPMQIKFGAWSGGDSSNAAGTISWARGPTDYSNGPFTMVVQSIDVSDYSTGTQYKYGDQSGDWTSIEAIGGSVNGNVPASASSIQTAGAAAVTSSSPTIPAGINNGNSATRTGYPWVAGTQTVSEVTWSTGPSIPSGWEISSEGKIVPVSASPINISRINPLLLCGPFTFFFFAAIRRWP

[Multiple Choices]
A. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
B. (1S,3S,6S,7S,8R)-7-hydroxy-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecan-9-one + NADPH + H(+) = (1S,3S,6S,7S,8S,9S)-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecane-7,9-diol + NADP(+)
C. 2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2'-hydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. ATP-independent breakage of single-stranded DNA, followed by passage and rejoining.
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

> The sequence-matched UniProt entry annotates the exact reaction in A. However, the chitinase assignment is transferred by similarity (ECO:0000250) from Q8J0P4, not shown here as a direct experimental measurement on this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted fungal protein, and the sequence is compatible with a carbohydrate-active enzyme; these clues make A more plausible than the unrelated reactions in B–D but do not establish chitin specificity or the stated hydrolytic activity.


**Missing item-specific fact**

> The protein-specific assignment to a chitinase with the reaction in A, which the supplied sequence does not establish by itself.


**Reason**

> Choosing the precise reaction depends on protein-family or activity annotation not supplied in the question. Broad sequence clues favor a secreted carbohydrate-active protein, but do not distinguish the exact substrate and reaction with adequate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are distinct, and the available reviewer-only annotation supports A; no other listed reaction is comparably supported.


### Important caveats

- The UniProt catalytic-activity annotation is an inference transferred from a related entry, not evidence here of direct experimental validation for this exact sequence.
- The entry also annotates chitin transglycosylase activity, so the sequence's broader biological role may not be fully represented by choice A alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal protein, and the sequence is compatible with a carbohydrate-active enzyme; these clues make A more plausible than the unrelated reactions in B–D but do not establish chitin specificity or the stated hydrolytic activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment to a chitinase with the reaction in A, which the supplied sequence does not establish by itself.",
    "reason": "Choosing the precise reaction depends on protein-family or activity annotation not supplied in the question. Broad sequence clues favor a secreted carbohydrate-active protein, but do not distinguish the exact substrate and reaction with adequate specificity."
  },
  "case_id": "catalytic_activity_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the exact reaction in A. However, the chitinase assignment is transferred by similarity (ECO:0000250) from Q8J0P4, not shown here as a direct experimental measurement on this protein."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation is an inference transferred from a related entry, not evidence here of direct experimental validation for this exact sequence.",
    "The entry also annotates chitin transglycosylase activity, so the sequence's broader biological role may not be fully represented by choice A alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct, and the available reviewer-only annotation supports A; no other listed reaction is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the exact reaction in A. However, the chitinase assignment is transferred by similarity (ECO:0000250) from Q8J0P4, not shown here as a direct experimental measurement on this protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal protein, and the sequence is compatible with a carbohydrate-active enzyme; these clues make A more plausible than the unrelated reactions in B–D but do not establish chitin specificity or the stated hydrolytic activity.",
    "missing_item_specific_fact": "The protein-specific assignment to a chitinase with the reaction in A, which the supplied sequence does not establish by itself.",
    "reason": "Choosing the precise reaction depends on protein-family or activity annotation not supplied in the question. Broad sequence clues favor a secreted carbohydrate-active protein, but do not distinguish the exact substrate and reaction with adequate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are distinct, and the available reviewer-only annotation supports A; no other listed reaction is comparably supported."
  },
  "important_caveats": [
    "The UniProt catalytic-activity annotation is an inference transferred from a related entry, not evidence here of direct experimental validation for this exact sequence.",
    "The entry also annotates chitin transglycosylase activity, so the sequence's broader biological role may not be fully represented by choice A alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384JN58 (CRH4_BOTFB, Botrytis cinerea) explicitly annotates the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' with EC 3.2.1.14 (evidence C5, H4). However, the evidence code is ECO:0000250 (similarity, transferred from Q8J0P4), not direct experimental demonstration for this specific protein. The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), and the cited PubMed paper (33846308) describes Crh proteins as transglycosylases/cytoplasmic effectors. The annotation nonetheless supports Choice A as the database-assigned catalytic activity.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence ('...INPLLLCGPFTFFFFAAIRRWP') displays the characteristic cysteine spacing and hydrophobic pattern of a CBM5/ChtBD2 chitin-binding domain. The central region has a GH18-like fold architecture (fungal chitinase superfamily). Together with the N-terminal signal peptide, this domain architecture (signal peptide → GH18-like → CBM5) is diagnostic of fungal chitin-related enzymes. Among the four choices, only A involves chitin chemistry; B is an NADPH-dependent alkaloid reduction, C is a ferredoxin-dependent carotenoid hydroxylase, and D is an ATP-independent topoisomerase. Recognizing the chitin-binding domain and GH18-like fold provides meaningful grounds to select A over the three completely unrelated enzyme classes.


**Missing item-specific fact**

> The precise assignment to 'random endo-hydrolysis' (endo-chitinase) vs. transglycosylase activity requires knowing that the Crh-like GH18 fold retains chitinase annotation by similarity (ECO:0000250), and that Crh proteins lack the canonical DXXDXDXE catalytic motif yet are still annotated as chitinases. However, this distinction is irrelevant for choosing among the four given options since only A is chitin-related.


**Reason**

> A model with general knowledge of fungal enzyme domain architecture can recognize the CBM5 chitin-binding domain and GH18-like fold from sequence features, then eliminate B (NADPH-dependent reduction), C (carotenoid hydroxylase), and D (topoisomerase) as mechanistically unrelated. The reasoning path is concrete and does not require memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein carries dual annotations (chitinase EC 3.2.1.14 and chitin transglycosylase EC 2.4.-.-), but transglycosylase activity is not among the choices. Among A–D, only A involves chitin substrates. The other three choices describe entirely unrelated enzyme classes with no structural or mechanistic overlap with the observed domain architecture.


### Important caveats

- The chitinase annotation (EC 3.2.1.14) is transferred by similarity (ECO:0000250) from Q8J0P4, not directly demonstrated experimentally for Crh4 itself.
- Crh proteins are atypical GH18 members lacking the canonical catalytic DXXDXDXE motif; their primary characterized activity in the literature is transglycosylase/effector function (PubMed 33846308).
- The sequence-match to UniProt A0A384JN58 is confirmed (SHA-256 match, 376 aa), so the annotation applies to the exact supplied sequence.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what a model could infer from the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence ('...INPLLLCGPFTFFFFAAIRRWP') displays the characteristic cysteine spacing and hydrophobic pattern of a CBM5/ChtBD2 chitin-binding domain. The central region has a GH18-like fold architecture (fungal chitinase superfamily). Together with the N-terminal signal peptide, this domain architecture (signal peptide → GH18-like → CBM5) is diagnostic of fungal chitin-related enzymes. Among the four choices, only A involves chitin chemistry; B is an NADPH-dependent alkaloid reduction, C is a ferredoxin-dependent carotenoid hydroxylase, and D is an ATP-independent topoisomerase. Recognizing the chitin-binding domain and GH18-like fold provides meaningful grounds to select A over the three completely unrelated enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise assignment to 'random endo-hydrolysis' (endo-chitinase) vs. transglycosylase activity requires knowing that the Crh-like GH18 fold retains chitinase annotation by similarity (ECO:0000250), and that Crh proteins lack the canonical DXXDXDXE catalytic motif yet are still annotated as chitinases. However, this distinction is irrelevant for choosing among the four given options since only A is chitin-related.",
    "reason": "A model with general knowledge of fungal enzyme domain architecture can recognize the CBM5 chitin-binding domain and GH18-like fold from sequence features, then eliminate B (NADPH-dependent reduction), C (carotenoid hydroxylase), and D (topoisomerase) as mechanistically unrelated. The reasoning path is concrete and does not require memorizing the specific UniProt entry."
  },
  "case_id": "catalytic_activity_0178",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384JN58 (CRH4_BOTFB, Botrytis cinerea) explicitly annotates the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' with EC 3.2.1.14 (evidence C5, H4). However, the evidence code is ECO:0000250 (similarity, transferred from Q8J0P4), not direct experimental demonstration for this specific protein. The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), and the cited PubMed paper (33846308) describes Crh proteins as transglycosylases/cytoplasmic effectors. The annotation nonetheless supports Choice A as the database-assigned catalytic activity."
  },
  "important_caveats": [
    "The chitinase annotation (EC 3.2.1.14) is transferred by similarity (ECO:0000250) from Q8J0P4, not directly demonstrated experimentally for Crh4 itself.",
    "Crh proteins are atypical GH18 members lacking the canonical catalytic DXXDXDXE motif; their primary characterized activity in the literature is transglycosylase/effector function (PubMed 33846308).",
    "The sequence-match to UniProt A0A384JN58 is confirmed (SHA-256 match, 376 aa), so the annotation applies to the exact supplied sequence.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what a model could infer from the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein carries dual annotations (chitinase EC 3.2.1.14 and chitin transglycosylase EC 2.4.-.-), but transglycosylase activity is not among the choices. Among A–D, only A involves chitin substrates. The other three choices describe entirely unrelated enzyme classes with no structural or mechanistic overlap with the observed domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0178",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384JN58 (CRH4_BOTFB, Botrytis cinerea) explicitly annotates the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' with EC 3.2.1.14 (evidence C5, H4). However, the evidence code is ECO:0000250 (similarity, transferred from Q8J0P4), not direct experimental demonstration for this specific protein. The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), and the cited PubMed paper (33846308) describes Crh proteins as transglycosylases/cytoplasmic effectors. The annotation nonetheless supports Choice A as the database-assigned catalytic activity.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence ('...INPLLLCGPFTFFFFAAIRRWP') displays the characteristic cysteine spacing and hydrophobic pattern of a CBM5/ChtBD2 chitin-binding domain. The central region has a GH18-like fold architecture (fungal chitinase superfamily). Together with the N-terminal signal peptide, this domain architecture (signal peptide → GH18-like → CBM5) is diagnostic of fungal chitin-related enzymes. Among the four choices, only A involves chitin chemistry; B is an NADPH-dependent alkaloid reduction, C is a ferredoxin-dependent carotenoid hydroxylase, and D is an ATP-independent topoisomerase. Recognizing the chitin-binding domain and GH18-like fold provides meaningful grounds to select A over the three completely unrelated enzyme classes.",
    "missing_item_specific_fact": "The precise assignment to 'random endo-hydrolysis' (endo-chitinase) vs. transglycosylase activity requires knowing that the Crh-like GH18 fold retains chitinase annotation by similarity (ECO:0000250), and that Crh proteins lack the canonical DXXDXDXE catalytic motif yet are still annotated as chitinases. However, this distinction is irrelevant for choosing among the four given options since only A is chitin-related.",
    "reason": "A model with general knowledge of fungal enzyme domain architecture can recognize the CBM5 chitin-binding domain and GH18-like fold from sequence features, then eliminate B (NADPH-dependent reduction), C (carotenoid hydroxylase), and D (topoisomerase) as mechanistically unrelated. The reasoning path is concrete and does not require memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein carries dual annotations (chitinase EC 3.2.1.14 and chitin transglycosylase EC 2.4.-.-), but transglycosylase activity is not among the choices. Among A–D, only A involves chitin substrates. The other three choices describe entirely unrelated enzyme classes with no structural or mechanistic overlap with the observed domain architecture."
  },
  "important_caveats": [
    "The chitinase annotation (EC 3.2.1.14) is transferred by similarity (ECO:0000250) from Q8J0P4, not directly demonstrated experimentally for Crh4 itself.",
    "Crh proteins are atypical GH18 members lacking the canonical catalytic DXXDXDXE motif; their primary characterized activity in the literature is transglycosylase/effector function (PubMed 33846308).",
    "The sequence-match to UniProt A0A384JN58 is confirmed (SHA-256 match, 376 aa), so the annotation applies to the exact supplied sequence.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what a model could infer from the sequence and general biological knowledge."
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

**Accession:** `A0A384JN58` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 23. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:57.593651+00:00.  

```json
{"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"3.2.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitinase crh4"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitin transglycosylase crh4"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33846308","source":"PubMed"}],"value":"Crh-like protein 4"}}}
```

Source SHA-256: `1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384JN58.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:57.593651+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.14","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"name":"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins."}}
```

Source SHA-256: `1c942047a94946fea0938c220d7e21eb1b2a90fe7cbc50ba6e1b5d15c24be4f5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)  
**Locator:** `lines 6-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:25:00.993379+00:00.  

```text
DE   RecName: Full=Crh-like protein 4 {ECO:0000303|PubMed:33846308};
DE   Includes:
DE     RecName: Full=Chitinase crh4 {ECO:0000250|UniProtKB:Q8J0P4};
DE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};
DE   Includes:
DE     RecName: Full=Chitin transglycosylase crh4 {ECO:0000250|UniProtKB:Q8J0P4};
DE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};
DE   Flags: Precursor;
```

Source SHA-256: `4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384JN58?format=txt&versions=23)  
**Locator:** `lines 71-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 23 / 1.  
**Retrieved:** 2026-11-02T04:25:00.993379+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide
CC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;
CC         Evidence={ECO:0000250|UniProtKB:Q8J0P4};
```

Source SHA-256: `4dc3e06f6178fdfc6f41e22a26117b81e3fe17c3e6e2a087e6c84be3ece91987`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 178. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
