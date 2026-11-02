# catalytic_activity_0044

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
MVGKSTLLSVLASASVAFAACSLDSHCPEETPCCSQYGECGTGAYCLGGCDPRMSFSLESCVPEPVCESASYTFTSMDGITSNTKYLGDASKSNWVYSGSPVIYNDNVLLTMSANSVGTVMASSTYMWYGNVKAKFKTSRGQGVITAFILFSDVKDEIDYEFVGSELTTAQSNYYFQGITNYDNELNITLSDTYANYHEYEIDWTPDEITWLVDGQVGRTKKRADTWNATANQWNFPQTPARVQLSLWPGGLASNGAGTIAWAGGEIDWNSEDIQNNGYYYAAFESVDISCYNAKSAPGTNSGKSYYYNSVLGTNNTVIDSKNATILSSLLATGTNMTAGESAAASGSTAASTAATVPGLTGSGGGGVGDNHSDDGSSSSDSSSGSATSSSSGSSSTGSSGFSQGDGSTSTSKSSADSLVANQERVLKGSLFAGIVAVVAMMAL

[Multiple Choices]
A. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
B. benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)
C. L-isoleucyl-tRNA(Ile) + acetyl-CoA = N-acetyl-L-isoleucyl-tRNA(Ile) + CoA + H(+)
D. 2-hydroxyspirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
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

> The exact sequence matches the UniProt entry that annotates this reaction as EC 3.2.1.14. The annotation is transferred by similarity from Q8J0P4, so it supports A as a database annotation, not as direct experimental validation of this protein's activity.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and cysteine-rich, likely secretory protein sequence are compatible with a fungal cell-wall-associated protein and make intracellular tRNA or carotenoid reactions less plausible. These broad clues do not establish the specific chitin-hydrolysis reaction.


**Missing item-specific fact**

> A protein-specific functional annotation or experimental substrate-specificity evidence is needed to identify this sequence as having the chitinase activity described in A; the reviewer evidence supplies a homology-transferred annotation.


**Reason**

> Sequence and biological context provide at most broad localization and protein-class clues, not a defensible determination of the precise catalytic reaction. The choice depends on protein-specific functional information absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, A is the one supported by the matching entry's catalytic-activity annotation. The entry also carries a chitin-transglycosylase annotation, but no corresponding reaction is offered as another choice.


### Important caveats

- The reaction annotation is supported by evidence transferred from Q8J0P4 rather than direct evidence for the supplied protein.
- The supplied sequence matches the current and historical UniProt sequence for this entry, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and cysteine-rich, likely secretory protein sequence are compatible with a fungal cell-wall-associated protein and make intracellular tRNA or carotenoid reactions less plausible. These broad clues do not establish the specific chitin-hydrolysis reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific functional annotation or experimental substrate-specificity evidence is needed to identify this sequence as having the chitinase activity described in A; the reviewer evidence supplies a homology-transferred annotation.",
    "reason": "Sequence and biological context provide at most broad localization and protein-class clues, not a defensible determination of the precise catalytic reaction. The choice depends on protein-specific functional information absent from the question."
  },
  "case_id": "catalytic_activity_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry that annotates this reaction as EC 3.2.1.14. The annotation is transferred by similarity from Q8J0P4, so it supports A as a database annotation, not as direct experimental validation of this protein's activity."
  },
  "important_caveats": [
    "The reaction annotation is supported by evidence transferred from Q8J0P4 rather than direct evidence for the supplied protein.",
    "The supplied sequence matches the current and historical UniProt sequence for this entry, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, A is the one supported by the matching entry's catalytic-activity annotation. The entry also carries a chitin-transglycosylase annotation, but no corresponding reaction is offered as another choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry that annotates this reaction as EC 3.2.1.14. The annotation is transferred by similarity from Q8J0P4, so it supports A as a database annotation, not as direct experimental validation of this protein's activity.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and cysteine-rich, likely secretory protein sequence are compatible with a fungal cell-wall-associated protein and make intracellular tRNA or carotenoid reactions less plausible. These broad clues do not establish the specific chitin-hydrolysis reaction.",
    "missing_item_specific_fact": "A protein-specific functional annotation or experimental substrate-specificity evidence is needed to identify this sequence as having the chitinase activity described in A; the reviewer evidence supplies a homology-transferred annotation.",
    "reason": "Sequence and biological context provide at most broad localization and protein-class clues, not a defensible determination of the precise catalytic reaction. The choice depends on protein-specific functional information absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, A is the one supported by the matching entry's catalytic-activity annotation. The entry also carries a chitin-transglycosylase annotation, but no corresponding reaction is offered as another choice."
  },
  "important_caveats": [
    "The reaction annotation is supported by evidence transferred from Q8J0P4 rather than direct evidence for the supplied protein.",
    "The supplied sequence matches the current and historical UniProt sequence for this entry, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A384K116 (CRH3_BOTFB) lists EC 3.2.1.14 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' as a catalytic activity, matching Choice A verbatim. The sequence matches exactly (444 AA, SHA256 confirmed). However, the evidence code is ECO:0000250 (similarity-based inference from Q8J0P4), not direct experimental evidence. The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), and the primary literature (PubMed 33846308, Nat. Commun. 2021) emphasizes transglycosylase and effector functions. The chitinase annotation is computational transfer, not experimentally validated for this specific protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a large central domain with aspartate-rich motifs (e.g., 'DIDW', 'DWN', 'DIDSK') embedded in a TIM-barrel-like fold characteristic of glycosyl hydrolase family 18 (GH18) chitinases/chitin transglycosylases. The N-terminal signal peptide and C-terminal transmembrane anchor are consistent with a secreted/membrane-associated glycosidase. The three distractors describe entirely different enzyme classes: (B) a CoA-transferase requiring a distinct fold and CoA-binding motifs absent here; (C) a GNAT-like acetyltransferase with a completely different domain architecture; (D) a carotenoid desaturase requiring iron-binding (HXXHH) motifs and a different fold. None of these are compatible with the observed GH18-like domain architecture. Thus general knowledge of glycosyl hydrolase family 18 motifs and domain architecture allows elimination of B, C, and D, leaving A as the only glycosyl hydrolase option.


**Missing item-specific fact**

> The distinction between chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-) activity for this specific Crh-like protein requires protein-specific knowledge from the primary literature. However, since transglycosylase is not among the answer choices, this ambiguity does not affect selection among the four options.


**Reason**

> The GH18 domain architecture with its characteristic TIM-barrel fold and catalytic aspartate motifs is identifiable from the sequence using general knowledge of glycosyl hydrolase families. The other three options (transferase, acetyltransferase, desaturase) have fundamentally incompatible sequence features. A model with knowledge of GH18 family motifs can reason to A without memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein is annotated with both chitinase and transglycosylase activities, only the chitinase reaction (A) appears among the choices. The other three options (B, C, D) describe unrelated enzyme classes with no sequence compatibility. No ambiguity exists among the four provided options.


### Important caveats

- The EC 3.2.1.14 annotation is based on similarity inference (ECO:0000250 from Q8J0P4), not direct experimental validation of chitinase activity for this specific protein.
- The primary literature (PubMed 33846308) characterizes Crh3 primarily as a transglycosylase and plant-pathogen effector, not as a chitinase.
- The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), which is not among the answer choices but represents the protein's more experimentally characterized activity.
- The reviewer-only evidence was not available to the evaluated model; the reasoning path relies on recognizing GH18 domain features from the sequence itself.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a large central domain with aspartate-rich motifs (e.g., 'DIDW', 'DWN', 'DIDSK') embedded in a TIM-barrel-like fold characteristic of glycosyl hydrolase family 18 (GH18) chitinases/chitin transglycosylases. The N-terminal signal peptide and C-terminal transmembrane anchor are consistent with a secreted/membrane-associated glycosidase. The three distractors describe entirely different enzyme classes: (B) a CoA-transferase requiring a distinct fold and CoA-binding motifs absent here; (C) a GNAT-like acetyltransferase with a completely different domain architecture; (D) a carotenoid desaturase requiring iron-binding (HXXHH) motifs and a different fold. None of these are compatible with the observed GH18-like domain architecture. Thus general knowledge of glycosyl hydrolase family 18 motifs and domain architecture allows elimination of B, C, and D, leaving A as the only glycosyl hydrolase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The distinction between chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-) activity for this specific Crh-like protein requires protein-specific knowledge from the primary literature. However, since transglycosylase is not among the answer choices, this ambiguity does not affect selection among the four options.",
    "reason": "The GH18 domain architecture with its characteristic TIM-barrel fold and catalytic aspartate motifs is identifiable from the sequence using general knowledge of glycosyl hydrolase families. The other three options (transferase, acetyltransferase, desaturase) have fundamentally incompatible sequence features. A model with knowledge of GH18 family motifs can reason to A without memorizing this specific UniProt entry."
  },
  "case_id": "catalytic_activity_0044",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A384K116 (CRH3_BOTFB) lists EC 3.2.1.14 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' as a catalytic activity, matching Choice A verbatim. The sequence matches exactly (444 AA, SHA256 confirmed). However, the evidence code is ECO:0000250 (similarity-based inference from Q8J0P4), not direct experimental evidence. The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), and the primary literature (PubMed 33846308, Nat. Commun. 2021) emphasizes transglycosylase and effector functions. The chitinase annotation is computational transfer, not experimentally validated for this specific protein."
  },
  "important_caveats": [
    "The EC 3.2.1.14 annotation is based on similarity inference (ECO:0000250 from Q8J0P4), not direct experimental validation of chitinase activity for this specific protein.",
    "The primary literature (PubMed 33846308) characterizes Crh3 primarily as a transglycosylase and plant-pathogen effector, not as a chitinase.",
    "The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), which is not among the answer choices but represents the protein's more experimentally characterized activity.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning path relies on recognizing GH18 domain features from the sequence itself."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is annotated with both chitinase and transglycosylase activities, only the chitinase reaction (A) appears among the choices. The other three options (B, C, D) describe unrelated enzyme classes with no sequence compatibility. No ambiguity exists among the four provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0044",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A384K116 (CRH3_BOTFB) lists EC 3.2.1.14 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' as a catalytic activity, matching Choice A verbatim. The sequence matches exactly (444 AA, SHA256 confirmed). However, the evidence code is ECO:0000250 (similarity-based inference from Q8J0P4), not direct experimental evidence. The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), and the primary literature (PubMed 33846308, Nat. Commun. 2021) emphasizes transglycosylase and effector functions. The chitinase annotation is computational transfer, not experimentally validated for this specific protein.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a large central domain with aspartate-rich motifs (e.g., 'DIDW', 'DWN', 'DIDSK') embedded in a TIM-barrel-like fold characteristic of glycosyl hydrolase family 18 (GH18) chitinases/chitin transglycosylases. The N-terminal signal peptide and C-terminal transmembrane anchor are consistent with a secreted/membrane-associated glycosidase. The three distractors describe entirely different enzyme classes: (B) a CoA-transferase requiring a distinct fold and CoA-binding motifs absent here; (C) a GNAT-like acetyltransferase with a completely different domain architecture; (D) a carotenoid desaturase requiring iron-binding (HXXHH) motifs and a different fold. None of these are compatible with the observed GH18-like domain architecture. Thus general knowledge of glycosyl hydrolase family 18 motifs and domain architecture allows elimination of B, C, and D, leaving A as the only glycosyl hydrolase option.",
    "missing_item_specific_fact": "The distinction between chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-) activity for this specific Crh-like protein requires protein-specific knowledge from the primary literature. However, since transglycosylase is not among the answer choices, this ambiguity does not affect selection among the four options.",
    "reason": "The GH18 domain architecture with its characteristic TIM-barrel fold and catalytic aspartate motifs is identifiable from the sequence using general knowledge of glycosyl hydrolase families. The other three options (transferase, acetyltransferase, desaturase) have fundamentally incompatible sequence features. A model with knowledge of GH18 family motifs can reason to A without memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein is annotated with both chitinase and transglycosylase activities, only the chitinase reaction (A) appears among the choices. The other three options (B, C, D) describe unrelated enzyme classes with no sequence compatibility. No ambiguity exists among the four provided options."
  },
  "important_caveats": [
    "The EC 3.2.1.14 annotation is based on similarity inference (ECO:0000250 from Q8J0P4), not direct experimental validation of chitinase activity for this specific protein.",
    "The primary literature (PubMed 33846308) characterizes Crh3 primarily as a transglycosylase and plant-pathogen effector, not as a chitinase.",
    "The protein is also annotated as a chitin transglycosylase (EC 2.4.-.-), which is not among the answer choices but represents the protein's more experimentally characterized activity.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning path relies on recognizing GH18 domain features from the sequence itself."
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

**Accession:** `A0A384K116` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"3.2.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitinase crh3"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"value":"Chitin transglycosylase crh3"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33846308","source":"PubMed"}],"value":"Crh-like protein 3"}}}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.14","evidences":[{"evidenceCode":"ECO:0000250","id":"Q8J0P4","source":"UniProtKB"}],"name":"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins."}}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K116.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:58.718541+00:00.  

```json
{"citation":{"authors":["Bi K.","Scalschi L.","Jaiswal N.","Mengiste T.","Fried R.","Sanz A.B.","Arroyo J.","Zhu W.","Masrati G.","Sharon A."],"citationCrossReferences":[{"database":"PubMed","id":"33846308"},{"database":"DOI","id":"10.1038/s41467-021-22436-1"}],"citationType":"journal article","firstPage":"2166","id":"33846308","journal":"Nat. Commun.","lastPage":"2166","publicationDate":"2021","title":"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.","volume":"12"},"referenceNumber":4,"referencePositions":["FUNCTION","SUBUNIT","INTERACTION WITH CRH1 AND CRH2"]}
```

Source SHA-256: `ae9eff1dbbfe0af01782868981ec4a41bfb86565bf11b3d1021735be00b7c0c5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)  
**Locator:** `lines 6-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:01.844205+00:00.  

```text
DE   RecName: Full=Crh-like protein 3 {ECO:0000303|PubMed:33846308};
DE   Includes:
DE     RecName: Full=Chitinase crh3 {ECO:0000250|UniProtKB:Q8J0P4};
DE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};
DE   Includes:
DE     RecName: Full=Chitin transglycosylase crh3 {ECO:0000250|UniProtKB:Q8J0P4};
DE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};
DE   Flags: Precursor;
```

Source SHA-256: `68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)  
**Locator:** `lines 56-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:01.844205+00:00.  

```text
RN   [4]
RP   FUNCTION, SUBUNIT, AND INTERACTION WITH CRH1 AND CRH2.
RX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;
RA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,
RA   Arroyo J., Zhu W., Masrati G., Sharon A.;
RT   "The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector
RT   triggering plant cell death and defense response.";
RL   Nat. Commun. 12:2166-2166(2021).
```

Source SHA-256: `68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K116?format=txt&versions=26)  
**Locator:** `lines 71-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:25:01.844205+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide
CC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;
CC         Evidence={ECO:0000250|UniProtKB:Q8J0P4};
```

Source SHA-256: `68d6b3f7883bf2c351d257d0b49f28ef36ee9ed02d5d90e8d579c1df134c9f41`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 44. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
