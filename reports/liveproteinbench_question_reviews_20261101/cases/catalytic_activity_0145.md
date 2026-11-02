# catalytic_activity_0145

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMSRYEELRKELPAQPKVWLITGVAGFIGSNLLETLLKLDQKVVGLDNFATGHQRNLDEVRSLVSEKQWSNFKFIQGDIRNLDDCNNACAGVDYVLHQAALGSVPRSINDPITSNATNIDGFLNMLIAARDAKVQSFTYAASSSTYGDHPGLPKVEDTIGKPLSPYAVTKYVNELYADVFSRCYGFSTIGLRYFNVFGRRQDPNGAYAAVIPKWTSSMIQGDDVYINGDGETSRDFCYIENTVQANLLAATAGLDARNQVYNIAVGGRTSLNQLFFALRDGLAENGVSYHREPVYRDFREGDVRHSLADISKAAKLLGYAPKYDVSAGVALAMPWYIMFLK

[Multiple Choices]
A. 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)
B. L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)
C. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
D. UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate
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

> The supplied sequence exactly matches the UniProt entry, whose catalytic-activity annotation gives the reaction in choice D and cites experimental evidence (PubMed 18065759). The archived entry available by the stated historical cutoff records the same reaction.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features might support a broad enzyme-family inference, but the input does not provide a concrete basis for identifying this protein's specific UDP-sugar epimerase substrate and reaction over other epimerase or enzyme reactions.


**Missing item-specific fact**

> The protein-specific functional assignment that this sequence catalyzes UDP-2-acetamido-2-deoxy-alpha-D-glucuronate to UDP-2-acetamido-2-deoxy-alpha-D-galacturonate.


**Reason**

> The exact reaction depends on protein-specific functional evidence or recognition of the protein, neither of which is supplied. Reviewer-only database evidence supports the key but does not make it reasoning-supported for the evaluated input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the matched entry's annotated reaction corresponds to D; its separately annotated UDP-GlcNAc C4 epimerase activity is not listed.


### Important caveats

- The database annotation attributes the D reaction to experimental evidence, but this review did not independently examine the primary study.
- The source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features might support a broad enzyme-family inference, but the input does not provide a concrete basis for identifying this protein's specific UDP-sugar epimerase substrate and reaction over other epimerase or enzyme reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that this sequence catalyzes UDP-2-acetamido-2-deoxy-alpha-D-glucuronate to UDP-2-acetamido-2-deoxy-alpha-D-galacturonate.",
    "reason": "The exact reaction depends on protein-specific functional evidence or recognition of the protein, neither of which is supplied. Reviewer-only database evidence supports the key but does not make it reasoning-supported for the evaluated input."
  },
  "case_id": "catalytic_activity_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry, whose catalytic-activity annotation gives the reaction in choice D and cites experimental evidence (PubMed 18065759). The archived entry available by the stated historical cutoff records the same reaction."
  },
  "important_caveats": [
    "The database annotation attributes the D reaction to experimental evidence, but this review did not independently examine the primary study.",
    "The source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched entry's annotated reaction corresponds to D; its separately annotated UDP-GlcNAc C4 epimerase activity is not listed."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry, whose catalytic-activity annotation gives the reaction in choice D and cites experimental evidence (PubMed 18065759). The archived entry available by the stated historical cutoff records the same reaction.",
    "evidence_ids": ["C1", "C5", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features might support a broad enzyme-family inference, but the input does not provide a concrete basis for identifying this protein's specific UDP-sugar epimerase substrate and reaction over other epimerase or enzyme reactions.",
    "missing_item_specific_fact": "The protein-specific functional assignment that this sequence catalyzes UDP-2-acetamido-2-deoxy-alpha-D-glucuronate to UDP-2-acetamido-2-deoxy-alpha-D-galacturonate.",
    "reason": "The exact reaction depends on protein-specific functional evidence or recognition of the protein, neither of which is supplied. Reviewer-only database evidence supports the key but does not make it reasoning-supported for the evaluated input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the matched entry's annotated reaction corresponds to D; its separately annotated UDP-GlcNAc C4 epimerase activity is not listed."
  },
  "important_caveats": [
    "The database annotation attributes the D reaction to experimental evidence, but this review did not independently examine the primary study.",
    "The source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8KN66 (WbpP, Pseudomonas aeruginosa) lists the recommended catalytic activity as EC 5.1.3.45: UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate, supported by experimental evidence (ECO:0000269, PubMed:18065759, a 2008 J. Biol. Chem. paper on flagellin glycosylation). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed). Choice D reproduces this reaction verbatim. The entry also lists a secondary activity (EC 5.1.3.7, UDP-GlcNAc epimerase), but that reaction is not among the answer choices, so D is the only option matching any annotated activity of this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C9](#evidence-c9), [H9](#evidence-h9), [H1](#evidence-h1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal region contains a GxGxxG Rossmann-fold motif (WLITGVAGFIGSNL), indicating NAD/NADP binding. This could eliminate option C (xylanase, a hydrolase with no Rossmann fold). However, the Rossmann fold is shared across hundreds of enzyme families including both dehydrogenases (options A, B) and epimerases (option D). Distinguishing a UDP-hexose 4-epimerase (GalE-like, NAD used catalytically without net consumption) from an NAD-dependent dehydrogenase (NAD consumed to NADH) from sequence alone requires recognition of the specific GalE-like fold architecture and active-site geometry, which is specialized family-level knowledge rather than general biological inference. The specific substrate identity (UDP-GlcNAcA vs. L-galactose vs. a plant alkaloid) cannot be deduced from sequence features without database lookup.


**Missing item-specific fact**

> The specific assignment of this 341-aa protein to the UDP-hexose 4-epimerase family (GalE-like) and its experimentally determined substrate specificity for UDP-N-acetyl-alpha-D-glucosaminouronate (rather than other NAD-binding substrates) is an item-specific annotation/experimental fact not derivable from the sequence by general reasoning.


**Reason**

> While the Rossmann motif narrows the superfamily, the critical distinction between epimerase (D) and dehydrogenase (A, B) within the same fold family requires knowing the specific protein family architecture and substrate specificity, which is an item-specific experimental/annotation fact. A model would need to recognize this exact sequence as WbpP or recall the GalE-like epimerase family signature to select D over A or B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only D matches any experimentally verified catalytic activity of this protein. The secondary activity (EC 5.1.3.7, UDP-GlcNAc → UDP-GalNAc) is not offered as a distractor. Options A, B, and C correspond to entirely different enzyme classes (plant alkaloid reductase, sugar dehydrogenase, glycoside hydrolase) with no overlap with WbpP's known activities. The question is unambiguous in its correct answer.


### Important caveats

- WbpP is a dual-specificity enzyme: it catalyzes both EC 5.1.3.45 (UDP-GlcNAcA epimerase, recommended name) and EC 5.1.3.7 (UDP-GlcNAc epimerase, alternative name). The question's expected answer corresponds to the recommended name reaction, but the protein's broader activity is not reflected in the choices.
- The EC 5.1.3.45 assignment and its experimental evidence (PubMed:18065759, 2008) post-date the original 2000 characterization of WbpP as a UDP-GlcNAc C4 epimerase. The primary recommended name and EC number were updated based on later work.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q8KN66, but this accession identification was not available to the evaluated model.
- The entry was first public in Swiss-Prot on 2025-02-05; the author data-construction date is unknown, so the annotation available at question-creation time may have differed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a GxGxxG Rossmann-fold motif (WLITGVAGFIGSNL), indicating NAD/NADP binding. This could eliminate option C (xylanase, a hydrolase with no Rossmann fold). However, the Rossmann fold is shared across hundreds of enzyme families including both dehydrogenases (options A, B) and epimerases (option D). Distinguishing a UDP-hexose 4-epimerase (GalE-like, NAD used catalytically without net consumption) from an NAD-dependent dehydrogenase (NAD consumed to NADH) from sequence alone requires recognition of the specific GalE-like fold architecture and active-site geometry, which is specialized family-level knowledge rather than general biological inference. The specific substrate identity (UDP-GlcNAcA vs. L-galactose vs. a plant alkaloid) cannot be deduced from sequence features without database lookup.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific assignment of this 341-aa protein to the UDP-hexose 4-epimerase family (GalE-like) and its experimentally determined substrate specificity for UDP-N-acetyl-alpha-D-glucosaminouronate (rather than other NAD-binding substrates) is an item-specific annotation/experimental fact not derivable from the sequence by general reasoning.",
    "reason": "While the Rossmann motif narrows the superfamily, the critical distinction between epimerase (D) and dehydrogenase (A, B) within the same fold family requires knowing the specific protein family architecture and substrate specificity, which is an item-specific experimental/annotation fact. A model would need to recognize this exact sequence as WbpP or recall the GalE-like epimerase family signature to select D over A or B."
  },
  "case_id": "catalytic_activity_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C9",
      "H9",
      "H1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8KN66 (WbpP, Pseudomonas aeruginosa) lists the recommended catalytic activity as EC 5.1.3.45: UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate, supported by experimental evidence (ECO:0000269, PubMed:18065759, a 2008 J. Biol. Chem. paper on flagellin glycosylation). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed). Choice D reproduces this reaction verbatim. The entry also lists a secondary activity (EC 5.1.3.7, UDP-GlcNAc epimerase), but that reaction is not among the answer choices, so D is the only option matching any annotated activity of this protein."
  },
  "important_caveats": [
    "WbpP is a dual-specificity enzyme: it catalyzes both EC 5.1.3.45 (UDP-GlcNAcA epimerase, recommended name) and EC 5.1.3.7 (UDP-GlcNAc epimerase, alternative name). The question's expected answer corresponds to the recommended name reaction, but the protein's broader activity is not reflected in the choices.",
    "The EC 5.1.3.45 assignment and its experimental evidence (PubMed:18065759, 2008) post-date the original 2000 characterization of WbpP as a UDP-GlcNAc C4 epimerase. The primary recommended name and EC number were updated based on later work.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q8KN66, but this accession identification was not available to the evaluated model.",
    "The entry was first public in Swiss-Prot on 2025-02-05; the author data-construction date is unknown, so the annotation available at question-creation time may have differed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D matches any experimentally verified catalytic activity of this protein. The secondary activity (EC 5.1.3.7, UDP-GlcNAc → UDP-GalNAc) is not offered as a distractor. Options A, B, and C correspond to entirely different enzyme classes (plant alkaloid reductase, sugar dehydrogenase, glycoside hydrolase) with no overlap with WbpP's known activities. The question is unambiguous in its correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8KN66 (WbpP, Pseudomonas aeruginosa) lists the recommended catalytic activity as EC 5.1.3.45: UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate, supported by experimental evidence (ECO:0000269, PubMed:18065759, a 2008 J. Biol. Chem. paper on flagellin glycosylation). The sequence in the question matches the UniProt sequence exactly (SHA-256 confirmed). Choice D reproduces this reaction verbatim. The entry also lists a secondary activity (EC 5.1.3.7, UDP-GlcNAc epimerase), but that reaction is not among the answer choices, so D is the only option matching any annotated activity of this protein.",
    "evidence_ids": ["C4", "C5", "C7", "C9", "H9", "H1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal region contains a GxGxxG Rossmann-fold motif (WLITGVAGFIGSNL), indicating NAD/NADP binding. This could eliminate option C (xylanase, a hydrolase with no Rossmann fold). However, the Rossmann fold is shared across hundreds of enzyme families including both dehydrogenases (options A, B) and epimerases (option D). Distinguishing a UDP-hexose 4-epimerase (GalE-like, NAD used catalytically without net consumption) from an NAD-dependent dehydrogenase (NAD consumed to NADH) from sequence alone requires recognition of the specific GalE-like fold architecture and active-site geometry, which is specialized family-level knowledge rather than general biological inference. The specific substrate identity (UDP-GlcNAcA vs. L-galactose vs. a plant alkaloid) cannot be deduced from sequence features without database lookup.",
    "missing_item_specific_fact": "The specific assignment of this 341-aa protein to the UDP-hexose 4-epimerase family (GalE-like) and its experimentally determined substrate specificity for UDP-N-acetyl-alpha-D-glucosaminouronate (rather than other NAD-binding substrates) is an item-specific annotation/experimental fact not derivable from the sequence by general reasoning.",
    "reason": "While the Rossmann motif narrows the superfamily, the critical distinction between epimerase (D) and dehydrogenase (A, B) within the same fold family requires knowing the specific protein family architecture and substrate specificity, which is an item-specific experimental/annotation fact. A model would need to recognize this exact sequence as WbpP or recall the GalE-like epimerase family signature to select D over A or B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only D matches any experimentally verified catalytic activity of this protein. The secondary activity (EC 5.1.3.7, UDP-GlcNAc → UDP-GalNAc) is not offered as a distractor. Options A, B, and C correspond to entirely different enzyme classes (plant alkaloid reductase, sugar dehydrogenase, glycoside hydrolase) with no overlap with WbpP's known activities. The question is unambiguous in its correct answer."
  },
  "important_caveats": [
    "WbpP is a dual-specificity enzyme: it catalyzes both EC 5.1.3.45 (UDP-GlcNAcA epimerase, recommended name) and EC 5.1.3.7 (UDP-GlcNAc epimerase, alternative name). The question's expected answer corresponds to the recommended name reaction, but the protein's broader activity is not reflected in the choices.",
    "The EC 5.1.3.45 assignment and its experimental evidence (PubMed:18065759, 2008) post-date the original 2000 characterization of WbpP as a UDP-GlcNAc C4 epimerase. The primary recommended name and EC number were updated based on later work.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt Q8KN66, but this accession identification was not available to the evaluated model.",
    "The entry was first public in Swiss-Prot on 2025-02-05; the author data-construction date is unknown, so the annotation available at question-creation time may have differed."
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

**Accession:** `Q8KN66` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 87. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
"Q8KN66"
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10747995","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15016816","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15752069","source":"PubMed"}],"value":"5.1.3.7"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"15752069","source":"PubMed"}],"value":"UDP-N-acetylglucosamine C4 epimerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10747995","source":"PubMed"}],"value":"UDP-GlcNAc C4 epimerase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"5.1.3.45"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-GlcNAcA 4-epimerase"}]}}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81512"}}],"reaction":{"ecNumber":"5.1.3.45","evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"name":"UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81511"},{"database":"ChEBI","id":"CHEBI:65040"},{"database":"ChEBI","id":"CHEBI:231899"}]}}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"citation":{"authors":["Creuzenet C.","Belanger M.","Wakarchuk W.W.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"10747995"},{"database":"DOI","id":"10.1074/jbc.m001171200"}],"citationType":"journal article","firstPage":"19060","id":"10747995","journal":"J. Biol. Chem.","lastPage":"19067","publicationDate":"2000","title":"Expression, purification, and biochemical characterization of WbpP, a new UDP-GlcNAc C4 epimerase from Pseudomonas aeruginosa serotype O6.","volume":"275"},"referenceComments":[{"type":"STRAIN","value":"Serotype O6"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"citation":{"authors":["Miller W.L.","Matewish M.J.","McNally D.J.","Ishiyama N.","Anderson E.M.","Brewer D.","Brisson J.R.","Berghuis A.M.","Lam J.S."],"citationCrossReferences":[{"database":"PubMed","id":"18065759"},{"database":"DOI","id":"10.1074/jbc.m708894200"}],"citationType":"journal article","firstPage":"3507","id":"18065759","journal":"J. Biol. Chem.","lastPage":"3518","publicationDate":"2008","title":"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.","volume":"283"},"referenceComments":[{"type":"STRAIN","value":"PAK / Serotype O6"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-01T06:28:41.451179+00:00.  

```text
ID   WBPP_PSEAI              Reviewed;         341 AA.
AC   Q8KN66; Q9RHD6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2002, sequence version 1.
DT   28-JAN-2026, entry version 87.
DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase {ECO:0000305};
DE            Short=UDP-GlcNAcA 4-epimerase {ECO:0000305};
DE            EC=5.1.3.45 {ECO:0000269|PubMed:18065759};
DE   AltName: Full=UDP-N-acetylglucosamine C4 epimerase {ECO:0000303|PubMed:15752069};
DE            Short=UDP-GlcNAc C4 epimerase {ECO:0000303|PubMed:10747995};
DE            EC=5.1.3.7 {ECO:0000269|PubMed:10747995, ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};
GN   Name=wbpP {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};
OS   Pseudomonas aeruginosa.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.
OX   NCBI_TaxID=287;
```

Source SHA-256: `d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)  
**Locator:** `lines 85-91`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-01T06:28:41.451179+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-
CC         2-deoxy-alpha-D-galacturonate; Xref=Rhea:RHEA:81511,
CC         ChEBI:CHEBI:65040, ChEBI:CHEBI:231899; EC=5.1.3.45;
CC         Evidence={ECO:0000269|PubMed:18065759};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81512;
CC         Evidence={ECO:0000269|PubMed:18065759};
```

Source SHA-256: `d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 145. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
