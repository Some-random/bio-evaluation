# catalytic_activity_0142

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAARDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNEMGCFTYPLVPGFETVGIATEVGSKVTKMKVGDKVAVGIMVGSCGKCDDCVNDRECYCPEVITSYGRIDHDGTPTYGGFSNETVANEKFVFRFPEKLPMAAGAPLLNAGVSVYSPMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGADAFLVSTDAKQMQAGSGTLDGILDTVPVVHPIEPLLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVASTVGGSTTEAQEMLDFAAEHNITANVEIIPMDYINTAMERIEKNDVRYRFVIDVGNTLTPPES

[Multiple Choices]
A. benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)
B. 17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)
C. (2E,6E)-farnesyl diphosphate = (S,S)-drim-8-en-11-yl diphosphate
D. UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + H(+) = UDP-N-acetyl-alpha-D-xylosamine + CO2
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

> The exact sequence matches a UniProt entry annotating choice B as a catalytic reaction, but that assignment is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence. The same entry reports experimental evidence for a different reaction, which does not contradict B.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence could plausibly indicate an oxidoreductase, making the NADP-linked choice B more compatible than the transferase, terpene-cyclization, or sugar-decarboxylation choices. That broad class inference does not establish the specific substrates and products in B.


**Missing item-specific fact**

> The protein-specific catalytic annotation linking this sequence to the 17-O-acetylnorajmaline reaction.


**Reason**

> Choosing the exact transformation requires protein-specific functional information absent from the input; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice B is supported by the supplied reviewer evidence as an annotation for the matching sequence; the separately reported experimental reaction is not among the options.


### Important caveats

- The choice-B annotation is transferred from a related UniProt entry, rather than directly experimentally established for this sequence in the cited annotation.
- The matching protein has experimental evidence for a distinct catalytic reaction, which does not by itself exclude the transferred choice-B activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence could plausibly indicate an oxidoreductase, making the NADP-linked choice B more compatible than the transferase, terpene-cyclization, or sugar-decarboxylation choices. That broad class inference does not establish the specific substrates and products in B.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic annotation linking this sequence to the 17-O-acetylnorajmaline reaction.",
    "reason": "Choosing the exact transformation requires protein-specific functional information absent from the input; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating choice B as a catalytic reaction, but that assignment is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence. The same entry reports experimental evidence for a different reaction, which does not contradict B."
  },
  "important_caveats": [
    "The choice-B annotation is transferred from a related UniProt entry, rather than directly experimentally established for this sequence in the cited annotation.",
    "The matching protein has experimental evidence for a distinct catalytic reaction, which does not by itself exclude the transferred choice-B activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice B is supported by the supplied reviewer evidence as an annotation for the matching sequence; the separately reported experimental reaction is not among the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating choice B as a catalytic reaction, but that assignment is transferred by similarity (ECO:0000250), not direct experimental evidence for this sequence. The same entry reports experimental evidence for a different reaction, which does not contradict B.",
    "evidence_ids": ["C1", "C5", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence could plausibly indicate an oxidoreductase, making the NADP-linked choice B more compatible than the transferase, terpene-cyclization, or sugar-decarboxylation choices. That broad class inference does not establish the specific substrates and products in B.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation linking this sequence to the 17-O-acetylnorajmaline reaction.",
    "reason": "Choosing the exact transformation requires protein-specific functional information absent from the input; recognizing the sequence or recalling its database annotation would be lookup or memorization, not reasoning from the supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice B is supported by the supplied reviewer evidence as an annotation for the matching sequence; the separately reported experimental reaction is not among the options."
  },
  "important_caveats": [
    "The choice-B annotation is transferred from a related UniProt entry, rather than directly experimentally established for this sequence in the cited annotation.",
    "The matching protein has experimental evidence for a distinct catalytic reaction, which does not by itself exclude the transferred choice-B activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0U4BHM2 (sequence matched exactly) lists the reaction '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)' (EC 1.3.1.73) as a catalytic activity (C5/H4). The recommended protein name is '1,2-Dihydrovomilenine reductase' with EC 1.3.1.73. However, the evidence code for this specific reaction is ECO:0000250 (inferred by similarity from A0A0U3S9Q3), not direct experimental assay. The experimentally verified activity (ECO:0000269, C6/H5) is a different reaction: (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+). The expected answer matches the UniProt annotation but rests on similarity-based inference rather than direct experimental confirmation for this particular substrate.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains identifiable Rossmann-fold nucleotide-binding motifs: 'GATMGSFELPILPLGVGRKS' (GxGxxG variant) and 'GGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGA' (GGLGH motif), characteristic of NAD(P)-dependent oxidoreductases. Among the four choices, only B describes an NADP+-dependent oxidation-reduction reaction (EC 1.3.1.73). Choice A is an acyltransferase (no NADP+), C is a cyclase (no cofactor), and D is a decarboxylase (no NADP+). Identifying the protein as an oxidoreductase from these structural motifs eliminates A, C, and D, leaving B.


**Missing item-specific fact**

> The specific substrate identity (17-O-acetylnorajmaline) cannot be determined from sequence alone; however, the elimination of non-oxidoreductase choices via cofactor/enzyme-class reasoning is sufficient to select B from the given options.


**Reason**

> The sequence provides sufficient structural information (Rossmann fold motifs, overall ~363 aa oxidoreductase architecture) to identify the enzyme class as an NAD(P)-dependent reductase. This uniquely matches choice B among the four options, which differ in enzyme class (transferase, oxidoreductase, cyclase, decarboxylase). The reasoning does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (acyltransferase, oxidoreductase, sesquiterpene cyclase, decarboxylase), making them mutually exclusive. Only B is consistent with an NAD(P)-dependent oxidoreductase, which the sequence motifs support.


### Important caveats

- The EC 1.3.1.73 assignment for the 17-O-acetylnorajmaline reaction is based on similarity inference (ECO:0000250), not direct experimental evidence for this protein.
- The experimentally characterized activity (ECO:0000269, PubMed:26715562) is for the dihydrovomilenine→vomilenine reduction, a different reaction not offered as a choice.
- The protein is annotated as a 'CAD-like reductase' (cinnamyl alcohol dehydrogenase-like), which is a broad family; substrate specificity within this family cannot be predicted from sequence motifs alone.
- The physiological direction of the B reaction is right-to-left (reducing 1,2-dihydrovomilenine), though the equation is written left-to-right in the answer choice, consistent with UniProt's convention.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains identifiable Rossmann-fold nucleotide-binding motifs: 'GATMGSFELPILPLGVGRKS' (GxGxxG variant) and 'GGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGA' (GGLGH motif), characteristic of NAD(P)-dependent oxidoreductases. Among the four choices, only B describes an NADP+-dependent oxidation-reduction reaction (EC 1.3.1.73). Choice A is an acyltransferase (no NADP+), C is a cyclase (no cofactor), and D is a decarboxylase (no NADP+). Identifying the protein as an oxidoreductase from these structural motifs eliminates A, C, and D, leaving B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity (17-O-acetylnorajmaline) cannot be determined from sequence alone; however, the elimination of non-oxidoreductase choices via cofactor/enzyme-class reasoning is sufficient to select B from the given options.",
    "reason": "The sequence provides sufficient structural information (Rossmann fold motifs, overall ~363 aa oxidoreductase architecture) to identify the enzyme class as an NAD(P)-dependent reductase. This uniquely matches choice B among the four options, which differ in enzyme class (transferase, oxidoreductase, cyclase, decarboxylase). The reasoning does not require memorizing this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4BHM2 (sequence matched exactly) lists the reaction '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)' (EC 1.3.1.73) as a catalytic activity (C5/H4). The recommended protein name is '1,2-Dihydrovomilenine reductase' with EC 1.3.1.73. However, the evidence code for this specific reaction is ECO:0000250 (inferred by similarity from A0A0U3S9Q3), not direct experimental assay. The experimentally verified activity (ECO:0000269, C6/H5) is a different reaction: (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+). The expected answer matches the UniProt annotation but rests on similarity-based inference rather than direct experimental confirmation for this particular substrate."
  },
  "important_caveats": [
    "The EC 1.3.1.73 assignment for the 17-O-acetylnorajmaline reaction is based on similarity inference (ECO:0000250), not direct experimental evidence for this protein.",
    "The experimentally characterized activity (ECO:0000269, PubMed:26715562) is for the dihydrovomilenine→vomilenine reduction, a different reaction not offered as a choice.",
    "The protein is annotated as a 'CAD-like reductase' (cinnamyl alcohol dehydrogenase-like), which is a broad family; substrate specificity within this family cannot be predicted from sequence motifs alone.",
    "The physiological direction of the B reaction is right-to-left (reducing 1,2-dihydrovomilenine), though the equation is written left-to-right in the answer choice, consistent with UniProt's convention."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (acyltransferase, oxidoreductase, sesquiterpene cyclase, decarboxylase), making them mutually exclusive. Only B is consistent with an NAD(P)-dependent oxidoreductase, which the sequence motifs support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4BHM2 (sequence matched exactly) lists the reaction '17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)' (EC 1.3.1.73) as a catalytic activity (C5/H4). The recommended protein name is '1,2-Dihydrovomilenine reductase' with EC 1.3.1.73. However, the evidence code for this specific reaction is ECO:0000250 (inferred by similarity from A0A0U3S9Q3), not direct experimental assay. The experimentally verified activity (ECO:0000269, C6/H5) is a different reaction: (20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+). The expected answer matches the UniProt annotation but rests on similarity-based inference rather than direct experimental confirmation for this particular substrate.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains identifiable Rossmann-fold nucleotide-binding motifs: 'GATMGSFELPILPLGVGRKS' (GxGxxG variant) and 'GGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGA' (GGLGH motif), characteristic of NAD(P)-dependent oxidoreductases. Among the four choices, only B describes an NADP+-dependent oxidation-reduction reaction (EC 1.3.1.73). Choice A is an acyltransferase (no NADP+), C is a cyclase (no cofactor), and D is a decarboxylase (no NADP+). Identifying the protein as an oxidoreductase from these structural motifs eliminates A, C, and D, leaving B.",
    "missing_item_specific_fact": "The specific substrate identity (17-O-acetylnorajmaline) cannot be determined from sequence alone; however, the elimination of non-oxidoreductase choices via cofactor/enzyme-class reasoning is sufficient to select B from the given options.",
    "reason": "The sequence provides sufficient structural information (Rossmann fold motifs, overall ~363 aa oxidoreductase architecture) to identify the enzyme class as an NAD(P)-dependent reductase. This uniquely matches choice B among the four options, which differ in enzyme class (transferase, oxidoreductase, cyclase, decarboxylase). The reasoning does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (acyltransferase, oxidoreductase, sesquiterpene cyclase, decarboxylase), making them mutually exclusive. Only B is consistent with an NAD(P)-dependent oxidoreductase, which the sequence motifs support."
  },
  "important_caveats": [
    "The EC 1.3.1.73 assignment for the 17-O-acetylnorajmaline reaction is based on similarity inference (ECO:0000250), not direct experimental evidence for this protein.",
    "The experimentally characterized activity (ECO:0000269, PubMed:26715562) is for the dihydrovomilenine→vomilenine reduction, a different reaction not offered as a choice.",
    "The protein is annotated as a 'CAD-like reductase' (cinnamyl alcohol dehydrogenase-like), which is a broad family; substrate specificity within this family cannot be predicted from sequence motifs alone.",
    "The physiological direction of the B reaction is right-to-left (reducing 1,2-dihydrovomilenine), though the equation is written left-to-right in the answer choice, consistent with UniProt's convention."
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

**Accession:** `A0A0U4BHM2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
"A0A0U4BHM2"
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Protein RR2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RtRR2"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"value":"1.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Vomilenine reductase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RtVR2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0U3S9Q3","source":"UniProtKB"}],"value":"1.3.1.73"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"1,2-Dihydrovomilenine reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RtDHVR"}]}}
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0U3S9Q3","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:12322"}}],"reaction":{"ecNumber":"1.3.1.73","evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0U3S9Q3","source":"UniProtKB"}],"name":"17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine + NADPH + 2 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:12320"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17372"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:77725"}]}}
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:79637"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"name":"(20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:79635"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16408"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:230482"}]}}
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)  
**Locator:** `lines 1-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:25.840272+00:00.  

```text
ID   DHVOR_RAUTE             Reviewed;         363 AA.
AC   A0A0U4BHM2;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-MAR-2016, sequence version 1.
DT   28-JAN-2026, entry version 30.
DE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};
DE            Short=RtDHVR {ECO:0000303|PubMed:26715562};
DE            EC=1.3.1.73 {ECO:0000250|UniProtKB:A0A0U3S9Q3};
DE   AltName: Full=Protein RR2 {ECO:0000303|PubMed:26715562};
DE            Short=RtRR2 {ECO:0000303|PubMed:26715562};
DE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};
DE            Short=RtVR2 {ECO:0000303|PubMed:26715562};
DE            EC=1.5.1.- {ECO:0000269|PubMed:26715562};
GN   Name=DHVR {ECO:0000303|PubMed:26715562};
GN   Synonyms=RR2 {ECO:0000303|PubMed:26715562},
GN   VR2 {ECO:0000303|PubMed:26715562};
OS   Rauvolfia tetraphylla (Be still tree).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;
OC   Rauvolfiinae; Rauvolfia.
OX   NCBI_TaxID=545371;
```

Source SHA-256: `f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)  
**Locator:** `lines 39-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:25.840272+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=17-O-acetylnorajmaline + NADP(+) = (2R)-1,2-dihydrovomilenine
CC         + NADPH + 2 H(+); Xref=Rhea:RHEA:12320, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:17372, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,
CC         ChEBI:CHEBI:77725; EC=1.3.1.73;
CC         Evidence={ECO:0000250|UniProtKB:A0A0U3S9Q3};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:12322;
CC         Evidence={ECO:0000250|UniProtKB:A0A0U3S9Q3};
```

Source SHA-256: `f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)  
**Locator:** `lines 47-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:25.840272+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(20S)-19,20-dihydrovomilenine + NADP(+) = vomilenine + NADPH +
CC         H(+); Xref=Rhea:RHEA:79635, ChEBI:CHEBI:15378, ChEBI:CHEBI:16408,
CC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349, ChEBI:CHEBI:230482;
CC         Evidence={ECO:0000269|PubMed:26715562};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:79637;
CC         Evidence={ECO:0000269|PubMed:26715562};
```

Source SHA-256: `f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
