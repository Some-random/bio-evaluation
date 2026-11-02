# catalytic_activity_0161

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1-&gt;4)-beta-linkages in chitin and chitodextrins.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRLSLVGVAIGLLSSSAIVTAQTYTDCNPLQKTCPPDPALGRSVTYDFTKGSSPDFKPVGSPTYDSNNGAAFSVAKQGDAPLIQSNWYMMFGHVEFVIKTAPGKGIVSSAVLQSDDLDEIDWEWLGANNLYVQTNYFGKGDTGSYNRGAAHDNAGNQDGFHTYTIDWTSTQIVWQIDGKTVRVLTAESAGDHFPQSPMMVKVGVWAGGDPNNAPGTIQWAGGETDYSAGPYTMYLKSLVATDYSTGKSYTYSDKSGSWRSITSDGGQINGNSDAESISTVESAPPVTATIDSAPIPFSGTHRETSSFVTPSIWPWVPKPTTLSSSVAKDTTLPSGWTFSGSRQVQPPSAASSTPPCTSSSLVSSLASPSHSGLKTSSISSVPNSSSATKSTGHLASTATYQISTYDSTLPSFSASIAHVAPTVAAANDLLEAPLGMGVFCALLGGLIAIF

[Multiple Choices]
A. cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)
B. Couples ATP hydrolysis with the unwinding of duplex DNA by translocating in the 3'-5' direction.
C. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
D. O-succinyl-L-homoserine + L-cysteine = L,L-cystathionine + succinate + H(+)
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

> The sequence exactly matches the UniProt Crh4 entry, which annotates EC 3.2.1.14 with the reaction stated in choice C. This is database annotation linked to a publication, not independent verification here of the underlying experiment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal signal-peptide-like region and C-terminal hydrophobic anchor, together with a large intervening domain, are consistent with a secreted or cell-wall-associated enzyme. Among the options, C is the extracellular polysaccharide reaction; A, B, and D describe unrelated intracellular processes.


**Missing item-specific fact**

> The sequence context does not by itself establish chitin as the substrate or prove the precise hydrolysis reaction; that specificity would require recognizing the enzyme family or consulting a protein-specific annotation.


**Reason**

> The sequence architecture meaningfully favors C over the listed alternatives, although the exact catalytic specificity is not experimentally demonstrated by the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C among the listed reactions fits an extracellular or cell-wall-associated polysaccharide enzyme; the other choices concern distinct cellular processes.


### Important caveats

- The cited database annotation supports the key, but the supplied evidence does not independently validate the primary study's experimental results.
- The sequence-based argument supports choosing among these distractors more strongly than it establishes the exact substrate specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal signal-peptide-like region and C-terminal hydrophobic anchor, together with a large intervening domain, are consistent with a secreted or cell-wall-associated enzyme. Among the options, C is the extracellular polysaccharide reaction; A, B, and D describe unrelated intracellular processes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence context does not by itself establish chitin as the substrate or prove the precise hydrolysis reaction; that specificity would require recognizing the enzyme family or consulting a protein-specific annotation.",
    "reason": "The sequence architecture meaningfully favors C over the listed alternatives, although the exact catalytic specificity is not experimentally demonstrated by the supplied input."
  },
  "case_id": "catalytic_activity_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt Crh4 entry, which annotates EC 3.2.1.14 with the reaction stated in choice C. This is database annotation linked to a publication, not independent verification here of the underlying experiment."
  },
  "important_caveats": [
    "The cited database annotation supports the key, but the supplied evidence does not independently validate the primary study's experimental results.",
    "The sequence-based argument supports choosing among these distractors more strongly than it establishes the exact substrate specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the listed reactions fits an extracellular or cell-wall-associated polysaccharide enzyme; the other choices concern distinct cellular processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt Crh4 entry, which annotates EC 3.2.1.14 with the reaction stated in choice C. This is database annotation linked to a publication, not independent verification here of the underlying experiment.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal signal-peptide-like region and C-terminal hydrophobic anchor, together with a large intervening domain, are consistent with a secreted or cell-wall-associated enzyme. Among the options, C is the extracellular polysaccharide reaction; A, B, and D describe unrelated intracellular processes.",
    "missing_item_specific_fact": "The sequence context does not by itself establish chitin as the substrate or prove the precise hydrolysis reaction; that specificity would require recognizing the enzyme family or consulting a protein-specific annotation.",
    "reason": "The sequence architecture meaningfully favors C over the listed alternatives, although the exact catalytic specificity is not experimentally demonstrated by the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the listed reactions fits an extracellular or cell-wall-associated polysaccharide enzyme; the other choices concern distinct cellular processes."
  },
  "important_caveats": [
    "The cited database annotation supports the key, but the supplied evidence does not independently validate the primary study's experimental results.",
    "The sequence-based argument supports choosing among these distractors more strongly than it establishes the exact substrate specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WMW2 (CRH4_ASPFU) explicitly annotates EC 3.2.1.14 with the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' (evidence_id C5, H4). The sequence matches exactly (SHA-256 confirmed). However, the EC 3.2.1.14 assignment carries evidence code ECO:0000305 (curator inference from PubMed:30971696), while the protein's experimentally confirmed activity (ECO:0000269) is the chitin transglycosylase activity (EC 2.4.-.-). The chitinase annotation is a reasonable family-based assignment for a GH18 domain protein but is not directly experimentally validated in isolation. The key is nonetheless supported by the database annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable features of a glycosyl hydrolase family 18 (GH18) domain: the DXXDXDXE-like catalytic motif region ('DDLDEIDWEWLGANNLY' and 'DWTSTQ'), a signal peptide (MRLSLVGVAIGLLSSSAIVTAQ), and a C-terminal transmembrane anchor (GVFCALLGGLIAIF), indicating a secreted cell-wall-associated enzyme. Among the four options, only C describes a glycosyl hydrolase reaction on a polysaccharide substrate. Option A is an acetyltransferase (tRNA modification), B is a DNA helicase (requires Walker/recA motifs absent here), and D is a cystathionine synthase (requires PLP-binding and CBS domains absent here). A model recognizing the GH-domain architecture and eliminating non-hydrolase enzyme classes can arrive at C without knowing the exact accession.


**Missing item-specific fact**

> Precise distinction between chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-) activity for this specific Crh4 protein requires the UniProt annotation or the Fang et al. 2019 paper. However, since no transglycosylase option is offered, this distinction does not affect answer selection among the given choices.


**Reason**

> The sequence provides sufficient structural clues (GH18 domain motifs, secretion signal, TM anchor, fungal origin) to identify a glycosyl hydrolase acting on a polysaccharide. The three distractors belong to entirely different enzyme classes (transferase, helicase, amino-acid biosynthesis enzyme) with incompatible sequence signatures. General biological knowledge of enzyme classification and domain recognition enables elimination to C without memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe reactions catalyzed by structurally unrelated enzyme classes (acetyltransferase, ATP-dependent helicase, PLP-dependent synthase) whose sequence signatures are entirely absent from the supplied sequence. Only C involves a glycosyl hydrolase acting on a beta-1,4-linked polysaccharide, consistent with the GH18-like domain evident in the sequence. No ambiguity among the four choices.


### Important caveats

- The EC 3.2.1.14 (chitinase) annotation is by curator inference (ECO:0000305), not direct experimental measurement. The experimentally validated activity (ECO:0000269) is the transglycosylase function (EC 2.4.-.-). The question's option C describes the inferred chitinase activity rather than the experimentally confirmed transglycosylase activity.
- The protein's primary biological role, per the 2019 Fang et al. paper, is as a chitin transglycosylase involved in cell-wall remodeling. The chitinase activity is a secondary/inferred annotation.
- The sequence is from Aspergillus fumigatus (fungal pathogen), and the Crh family proteins are cell-wall-associated enzymes with both hydrolytic and transglycosylase capabilities.
- The question does not offer a transglycosylase option, so the distinction between the two annotated activities does not create ambiguity among the given choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable features of a glycosyl hydrolase family 18 (GH18) domain: the DXXDXDXE-like catalytic motif region ('DDLDEIDWEWLGANNLY' and 'DWTSTQ'), a signal peptide (MRLSLVGVAIGLLSSSAIVTAQ), and a C-terminal transmembrane anchor (GVFCALLGGLIAIF), indicating a secreted cell-wall-associated enzyme. Among the four options, only C describes a glycosyl hydrolase reaction on a polysaccharide substrate. Option A is an acetyltransferase (tRNA modification), B is a DNA helicase (requires Walker/recA motifs absent here), and D is a cystathionine synthase (requires PLP-binding and CBS domains absent here). A model recognizing the GH-domain architecture and eliminating non-hydrolase enzyme classes can arrive at C without knowing the exact accession.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise distinction between chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-) activity for this specific Crh4 protein requires the UniProt annotation or the Fang et al. 2019 paper. However, since no transglycosylase option is offered, this distinction does not affect answer selection among the given choices.",
    "reason": "The sequence provides sufficient structural clues (GH18 domain motifs, secretion signal, TM anchor, fungal origin) to identify a glycosyl hydrolase acting on a polysaccharide. The three distractors belong to entirely different enzyme classes (transferase, helicase, amino-acid biosynthesis enzyme) with incompatible sequence signatures. General biological knowledge of enzyme classification and domain recognition enables elimination to C without memorizing this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0161",
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
    "reason": "UniProt entry Q4WMW2 (CRH4_ASPFU) explicitly annotates EC 3.2.1.14 with the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' (evidence_id C5, H4). The sequence matches exactly (SHA-256 confirmed). However, the EC 3.2.1.14 assignment carries evidence code ECO:0000305 (curator inference from PubMed:30971696), while the protein's experimentally confirmed activity (ECO:0000269) is the chitin transglycosylase activity (EC 2.4.-.-). The chitinase annotation is a reasonable family-based assignment for a GH18 domain protein but is not directly experimentally validated in isolation. The key is nonetheless supported by the database annotation."
  },
  "important_caveats": [
    "The EC 3.2.1.14 (chitinase) annotation is by curator inference (ECO:0000305), not direct experimental measurement. The experimentally validated activity (ECO:0000269) is the transglycosylase function (EC 2.4.-.-). The question's option C describes the inferred chitinase activity rather than the experimentally confirmed transglycosylase activity.",
    "The protein's primary biological role, per the 2019 Fang et al. paper, is as a chitin transglycosylase involved in cell-wall remodeling. The chitinase activity is a secondary/inferred annotation.",
    "The sequence is from Aspergillus fumigatus (fungal pathogen), and the Crh family proteins are cell-wall-associated enzymes with both hydrolytic and transglycosylase capabilities.",
    "The question does not offer a transglycosylase option, so the distinction between the two annotated activities does not create ambiguity among the given choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe reactions catalyzed by structurally unrelated enzyme classes (acetyltransferase, ATP-dependent helicase, PLP-dependent synthase) whose sequence signatures are entirely absent from the supplied sequence. Only C involves a glycosyl hydrolase acting on a beta-1,4-linked polysaccharide, consistent with the GH18-like domain evident in the sequence. No ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WMW2 (CRH4_ASPFU) explicitly annotates EC 3.2.1.14 with the catalytic activity 'Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins' (evidence_id C5, H4). The sequence matches exactly (SHA-256 confirmed). However, the EC 3.2.1.14 assignment carries evidence code ECO:0000305 (curator inference from PubMed:30971696), while the protein's experimentally confirmed activity (ECO:0000269) is the chitin transglycosylase activity (EC 2.4.-.-). The chitinase annotation is a reasonable family-based assignment for a GH18 domain protein but is not directly experimentally validated in isolation. The key is nonetheless supported by the database annotation.",
    "evidence_ids": ["C4", "C5", "H2", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable features of a glycosyl hydrolase family 18 (GH18) domain: the DXXDXDXE-like catalytic motif region ('DDLDEIDWEWLGANNLY' and 'DWTSTQ'), a signal peptide (MRLSLVGVAIGLLSSSAIVTAQ), and a C-terminal transmembrane anchor (GVFCALLGGLIAIF), indicating a secreted cell-wall-associated enzyme. Among the four options, only C describes a glycosyl hydrolase reaction on a polysaccharide substrate. Option A is an acetyltransferase (tRNA modification), B is a DNA helicase (requires Walker/recA motifs absent here), and D is a cystathionine synthase (requires PLP-binding and CBS domains absent here). A model recognizing the GH-domain architecture and eliminating non-hydrolase enzyme classes can arrive at C without knowing the exact accession.",
    "missing_item_specific_fact": "Precise distinction between chitinase (EC 3.2.1.14) and chitin transglycosylase (EC 2.4.-.-) activity for this specific Crh4 protein requires the UniProt annotation or the Fang et al. 2019 paper. However, since no transglycosylase option is offered, this distinction does not affect answer selection among the given choices.",
    "reason": "The sequence provides sufficient structural clues (GH18 domain motifs, secretion signal, TM anchor, fungal origin) to identify a glycosyl hydrolase acting on a polysaccharide. The three distractors belong to entirely different enzyme classes (transferase, helicase, amino-acid biosynthesis enzyme) with incompatible sequence signatures. General biological knowledge of enzyme classification and domain recognition enables elimination to C without memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe reactions catalyzed by structurally unrelated enzyme classes (acetyltransferase, ATP-dependent helicase, PLP-dependent synthase) whose sequence signatures are entirely absent from the supplied sequence. Only C involves a glycosyl hydrolase acting on a beta-1,4-linked polysaccharide, consistent with the GH18-like domain evident in the sequence. No ambiguity among the four choices."
  },
  "important_caveats": [
    "The EC 3.2.1.14 (chitinase) annotation is by curator inference (ECO:0000305), not direct experimental measurement. The experimentally validated activity (ECO:0000269) is the transglycosylase function (EC 2.4.-.-). The question's option C describes the inferred chitinase activity rather than the experimentally confirmed transglycosylase activity.",
    "The protein's primary biological role, per the 2019 Fang et al. paper, is as a chitin transglycosylase involved in cell-wall remodeling. The chitinase activity is a secondary/inferred annotation.",
    "The sequence is from Aspergillus fumigatus (fungal pathogen), and the Crh family proteins are cell-wall-associated enzymes with both hydrolytic and transglycosylase capabilities.",
    "The question does not offer a transglycosylase option, so the distinction between the two annotated activities does not create ambiguity among the given choices."
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

**Accession:** `Q4WMW2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 109. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.573750+00:00.  

```json
"Q4WMW2"
```

Source SHA-256: `a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.573750+00:00.  

```json
{"flag":"Precursor","includes":[{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"30971696","source":"PubMed"}],"value":"3.2.1.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Chitinase crh4"}}},{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"30971696","source":"PubMed"}],"value":"2.4.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Chitin transglycosylase crh4"}}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30971696","source":"PubMed"}],"value":"Crh-like protein 4"}}}
```

Source SHA-256: `a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.573750+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.14","evidences":[{"evidenceCode":"ECO:0000305","id":"30971696","source":"PubMed"}],"name":"Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins."}}
```

Source SHA-256: `a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WMW2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.573750+00:00.  

```json
{"citation":{"authors":["Fang W.","Sanz A.B.","Bartual S.G.","Wang B.","Ferenbach A.T.","Farkas V.","Hurtado-Guerrero R.","Arroyo J.","van Aalten D.M.F."],"citationCrossReferences":[{"database":"PubMed","id":"30971696"},{"database":"DOI","id":"10.1038/s41467-019-09674-0"}],"citationType":"journal article","firstPage":"1669","id":"30971696","journal":"Nat. Commun.","lastPage":"1669","publicationDate":"2019","title":"Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh transglycosylases.","volume":"10"},"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `a16f4a5b1d00ea4fa7e71345e504452af9679d3c799e955993ae094fd43634a1`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)  
**Locator:** `lines 6-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 109 / 1.  
**Retrieved:** 2026-11-01T06:28:35.372546+00:00.  

```text
DE   RecName: Full=Crh-like protein 4 {ECO:0000303|PubMed:30971696};
DE   Includes:
DE     RecName: Full=Chitinase crh4 {ECO:0000303|PubMed:30971696};
DE              EC=3.2.1.14 {ECO:0000305|PubMed:30971696};
DE   Includes:
DE     RecName: Full=Chitin transglycosylase crh4 {ECO:0000303|PubMed:30971696};
DE              EC=2.4.-.- {ECO:0000269|PubMed:30971696};
DE   Flags: Precursor;
```

Source SHA-256: `b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)  
**Locator:** `lines 46-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 109 / 1.  
**Retrieved:** 2026-11-01T06:28:35.372546+00:00.  

```text
RN   [2]
RP   FUNCTION, AND DISRUPTION PHENOTYPE.
RX   PubMed=30971696; DOI=10.1038/s41467-019-09674-0;
RA   Fang W., Sanz A.B., Bartual S.G., Wang B., Ferenbach A.T., Farkas V.,
RA   Hurtado-Guerrero R., Arroyo J., van Aalten D.M.F.;
RT   "Mechanisms of redundancy and specificity of the Aspergillus fumigatus Crh
RT   transglycosylases.";
RL   Nat. Commun. 10:1669-1669(2019).
```

Source SHA-256: `b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WMW2?format=txt&versions=109)  
**Locator:** `lines 61-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 109 / 1.  
**Retrieved:** 2026-11-01T06:28:35.372546+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide
CC         (1->4)-beta-linkages in chitin and chitodextrins.; EC=3.2.1.14;
CC         Evidence={ECO:0000305|PubMed:30971696};
```

Source SHA-256: `b8ce3d47aef38da81d748840324f945f4956eb9724d00b739e22b58d1b4a2e82`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 161. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
