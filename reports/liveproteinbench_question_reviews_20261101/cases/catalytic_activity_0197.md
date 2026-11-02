# catalytic_activity_0197

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MADRVMCQELATPGSHYRRPKTGVPSTNVVYANGGGSWRAAPRQTQRLPRQTVQQYATGTPATGSAGRHSGRAFATAGATEEQTVEFNGAAVMGLPATPRTTKQARNKSEEAINDLLTRIPDIGKLFDVHSRIGNGTFSTVLLGTLRRESHLPDSLRRKFAIKHHIPTSHPDRIMKELQCMTKMGGKENVVGIHCCMRYDASAAFVMPFMAHDRFQDFYTRMDVPEIRQYMRNLLVALRHVHKFDVIHRDVKPSNFLYNRRRREFLLVDFGLAQHVNPPAARSSGSAAAIAAANNKNNNNNNNNNSKRPRERESKGDVQQIALDAGLGGAVKRMRLHEESNKMPLKPVNDIAPSDAPEQSVDGSNHVQPQLVQQEQQQLQPQQQQQQQQQQQQSQQQQQPQQQSQQQHPQRQPQLAQMDQTASTPSGSKYNTNRNVSAAAANNAKCVCFANPSVCLNCLMKKEVHASRAGTPGYRPPEVLLKYPDQTTAVDVWAAGVIFLSIMSTVYPFFKAPNDFIALAEIVTIFGDQAIRKTALALDRMITLSQRSRPLNLRKLCLRFRYRSVFSDAKLLKSYESVDGSCEVCRNCDQYFFNCLCEDSDYLTEPLDAYECFPPSAYDLLDRLLEINPHKRITAEEALKHPFFTAAEEAEQTEQDQLANGTPRKMRRQRYQSHRTVAASQEQVKQQVALDLQQAAINKL

[Multiple Choices]
A. N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
B. 4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
C. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
D. N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2
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

> The sequence exactly matches the historical and current UniProt entry for Drosophila Cdc7. That entry annotates serine phosphorylation as catalytic activity, supported by both a PROSITE rule and a cited publication; it also annotates threonine phosphorylation. The evidence supports choice C, while the cited study has not been independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable eukaryotic protein-kinase catalytic domain, including conserved kinase catalytic motifs. That supports ATP-dependent phosphorylation of protein residues (choice C) over the methyltransferase reactions in A/B and the phosphopantetheine-related reaction in D.


**Missing item-specific fact**

> The precise Cdc7 identity and its annotated serine/threonine substrate activity are item-specific facts not stated in the input; the sequence supports the kinase reaction class, but does not by itself establish the cited experimental characterization.


**Reason**

> The choices differ substantially in reaction class, and the conserved kinase-domain sequence provides a concrete biological basis for selecting the protein-phosphorylation option. The reviewer-only database evidence confirms the key but is not needed to distinguish these broad reaction classes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C describes protein phosphorylation. The annotation also includes threonine phosphorylation, but no threonine-phosphorylation option is offered; this does not create a competing listed choice.


### Important caveats

- The protein is annotated as a serine/threonine kinase, so choice C is supported but does not represent the full range of its annotated catalytic activity.
- The database annotation cites both computational rule-based evidence and a publication; these evidence types should not be conflated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic domain, including conserved kinase catalytic motifs. That supports ATP-dependent phosphorylation of protein residues (choice C) over the methyltransferase reactions in A/B and the phosphopantetheine-related reaction in D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise Cdc7 identity and its annotated serine/threonine substrate activity are item-specific facts not stated in the input; the sequence supports the kinase reaction class, but does not by itself establish the cited experimental characterization.",
    "reason": "The choices differ substantially in reaction class, and the conserved kinase-domain sequence provides a concrete biological basis for selecting the protein-phosphorylation option. The reviewer-only database evidence confirms the key but is not needed to distinguish these broad reaction classes."
  },
  "case_id": "catalytic_activity_0197",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical and current UniProt entry for Drosophila Cdc7. That entry annotates serine phosphorylation as catalytic activity, supported by both a PROSITE rule and a cited publication; it also annotates threonine phosphorylation. The evidence supports choice C, while the cited study has not been independently reviewed here."
  },
  "important_caveats": [
    "The protein is annotated as a serine/threonine kinase, so choice C is supported but does not represent the full range of its annotated catalytic activity.",
    "The database annotation cites both computational rule-based evidence and a publication; these evidence types should not be conflated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C describes protein phosphorylation. The annotation also includes threonine phosphorylation, but no threonine-phosphorylation option is offered; this does not create a competing listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0197",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical and current UniProt entry for Drosophila Cdc7. That entry annotates serine phosphorylation as catalytic activity, supported by both a PROSITE rule and a cited publication; it also annotates threonine phosphorylation. The evidence supports choice C, while the cited study has not been independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable eukaryotic protein-kinase catalytic domain, including conserved kinase catalytic motifs. That supports ATP-dependent phosphorylation of protein residues (choice C) over the methyltransferase reactions in A/B and the phosphopantetheine-related reaction in D.",
    "missing_item_specific_fact": "The precise Cdc7 identity and its annotated serine/threonine substrate activity are item-specific facts not stated in the input; the sequence supports the kinase reaction class, but does not by itself establish the cited experimental characterization.",
    "reason": "The choices differ substantially in reaction class, and the conserved kinase-domain sequence provides a concrete biological basis for selecting the protein-phosphorylation option. The reviewer-only database evidence confirms the key but is not needed to distinguish these broad reaction classes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C describes protein phosphorylation. The annotation also includes threonine phosphorylation, but no threonine-phosphorylation option is offered; this does not create a competing listed choice."
  },
  "important_caveats": [
    "The protein is annotated as a serine/threonine kinase, so choice C is supported but does not represent the full range of its annotated catalytic activity.",
    "The database annotation cites both computational rule-based evidence and a publication; these evidence types should not be conflated."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9W3Y1 (CDC7_DROME) explicitly annotates the catalytic activity as 'L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)' under EC 2.7.11.1, backed by experimental evidence (ECO:0000269, PubMed:25451925) and PROSITE-ProRule annotation (PRU10027). The benchmark sequence SHA256 matches the source entry exactly (700 aa, sequence version 2). The protein is identified as a non-specific serine/threonine protein kinase Cdc7 from Drosophila melanogaster.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unambiguous protein kinase catalytic domain hallmarks: the HRD catalytic loop motif ('HRDVKPSNFLYNRRRREFLLVDFGLAQ') and the DFG motif ('DFGLAQ'), along with a glycine-rich loop region upstream. These motifs are diagnostic of a protein kinase fold. Among the four choices, only C describes a protein kinase reaction (serine phosphorylation of a protein substrate by ATP). Choices A and B describe O-/N-methyltransferase reactions (COMT-type), and D describes a decarboxylase reaction (phosphopantothenoyl-cysteine decarboxylase). Identifying the kinase fold from the sequence is sufficient to eliminate A, B, and D and select C.


**Missing item-specific fact**

> None required. The kinase catalytic motifs (HRD, DFG) are directly observable in the supplied sequence and are sufficient to distinguish the kinase option from the non-kinase options.


**Reason**

> A model with general biological knowledge can recognize the HRD and DFG motifs as protein kinase signatures, classify the protein as a kinase, and select the only kinase-catalyzed reaction among the four choices. No item-specific database lookup is strictly necessary to arrive at C, though confirming the exact EC number and distinguishing serine vs. threonine specificity would require annotation. However, since only one kinase option is offered, the reasoning path is sufficient.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (C) corresponds to a protein kinase reaction. The other three (A, B: methyltransferases; D: decarboxylase) are mechanistically incompatible with the clearly identifiable kinase catalytic domain. Although the UniProt entry also lists threonine phosphorylation (C6/H5), that reaction is not among the choices, so no ambiguity arises.


### Important caveats

- The UniProt entry also annotates L-threonyl-&#91;protein&#93; phosphorylation as a catalytic activity (EC 2.7.11.1), but this is not offered as a distractor, so it does not create ambiguity.
- The evidence code ECO:0000255 (PROSITE-ProRule) for the catalytic activity annotation is a computational/curatorial inference based on sequence similarity to characterized kinases; the experimental component is ECO:0000269 (PubMed:25451925) confirming kinase activity in vitro.
- The HRD/DFG motif identification is a well-established general principle in protein biochemistry and does not constitute memorization of a specific database entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unambiguous protein kinase catalytic domain hallmarks: the HRD catalytic loop motif ('HRDVKPSNFLYNRRRREFLLVDFGLAQ') and the DFG motif ('DFGLAQ'), along with a glycine-rich loop region upstream. These motifs are diagnostic of a protein kinase fold. Among the four choices, only C describes a protein kinase reaction (serine phosphorylation of a protein substrate by ATP). Choices A and B describe O-/N-methyltransferase reactions (COMT-type), and D describes a decarboxylase reaction (phosphopantothenoyl-cysteine decarboxylase). Identifying the kinase fold from the sequence is sufficient to eliminate A, B, and D and select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The kinase catalytic motifs (HRD, DFG) are directly observable in the supplied sequence and are sufficient to distinguish the kinase option from the non-kinase options.",
    "reason": "A model with general biological knowledge can recognize the HRD and DFG motifs as protein kinase signatures, classify the protein as a kinase, and select the only kinase-catalyzed reaction among the four choices. No item-specific database lookup is strictly necessary to arrive at C, though confirming the exact EC number and distinguishing serine vs. threonine specificity would require annotation. However, since only one kinase option is offered, the reasoning path is sufficient."
  },
  "case_id": "catalytic_activity_0197",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9W3Y1 (CDC7_DROME) explicitly annotates the catalytic activity as 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' under EC 2.7.11.1, backed by experimental evidence (ECO:0000269, PubMed:25451925) and PROSITE-ProRule annotation (PRU10027). The benchmark sequence SHA256 matches the source entry exactly (700 aa, sequence version 2). The protein is identified as a non-specific serine/threonine protein kinase Cdc7 from Drosophila melanogaster."
  },
  "important_caveats": [
    "The UniProt entry also annotates L-threonyl-[protein] phosphorylation as a catalytic activity (EC 2.7.11.1), but this is not offered as a distractor, so it does not create ambiguity.",
    "The evidence code ECO:0000255 (PROSITE-ProRule) for the catalytic activity annotation is a computational/curatorial inference based on sequence similarity to characterized kinases; the experimental component is ECO:0000269 (PubMed:25451925) confirming kinase activity in vitro.",
    "The HRD/DFG motif identification is a well-established general principle in protein biochemistry and does not constitute memorization of a specific database entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (C) corresponds to a protein kinase reaction. The other three (A, B: methyltransferases; D: decarboxylase) are mechanistically incompatible with the clearly identifiable kinase catalytic domain. Although the UniProt entry also lists threonine phosphorylation (C6/H5), that reaction is not among the choices, so no ambiguity arises."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0197",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9W3Y1 (CDC7_DROME) explicitly annotates the catalytic activity as 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)' under EC 2.7.11.1, backed by experimental evidence (ECO:0000269, PubMed:25451925) and PROSITE-ProRule annotation (PRU10027). The benchmark sequence SHA256 matches the source entry exactly (700 aa, sequence version 2). The protein is identified as a non-specific serine/threonine protein kinase Cdc7 from Drosophila melanogaster.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unambiguous protein kinase catalytic domain hallmarks: the HRD catalytic loop motif ('HRDVKPSNFLYNRRRREFLLVDFGLAQ') and the DFG motif ('DFGLAQ'), along with a glycine-rich loop region upstream. These motifs are diagnostic of a protein kinase fold. Among the four choices, only C describes a protein kinase reaction (serine phosphorylation of a protein substrate by ATP). Choices A and B describe O-/N-methyltransferase reactions (COMT-type), and D describes a decarboxylase reaction (phosphopantothenoyl-cysteine decarboxylase). Identifying the kinase fold from the sequence is sufficient to eliminate A, B, and D and select C.",
    "missing_item_specific_fact": "None required. The kinase catalytic motifs (HRD, DFG) are directly observable in the supplied sequence and are sufficient to distinguish the kinase option from the non-kinase options.",
    "reason": "A model with general biological knowledge can recognize the HRD and DFG motifs as protein kinase signatures, classify the protein as a kinase, and select the only kinase-catalyzed reaction among the four choices. No item-specific database lookup is strictly necessary to arrive at C, though confirming the exact EC number and distinguishing serine vs. threonine specificity would require annotation. However, since only one kinase option is offered, the reasoning path is sufficient."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (C) corresponds to a protein kinase reaction. The other three (A, B: methyltransferases; D: decarboxylase) are mechanistically incompatible with the clearly identifiable kinase catalytic domain. Although the UniProt entry also lists threonine phosphorylation (C6/H5), that reaction is not among the choices, so no ambiguity arises."
  },
  "important_caveats": [
    "The UniProt entry also annotates L-threonyl-[protein] phosphorylation as a catalytic activity (EC 2.7.11.1), but this is not offered as a distractor, so it does not create ambiguity.",
    "The evidence code ECO:0000255 (PROSITE-ProRule) for the catalytic activity annotation is a computational/curatorial inference based on sequence similarity to characterized kinases; the experimental component is ECO:0000269 (PubMed:25451925) confirming kinase activity in vitro.",
    "The HRD/DFG motif identification is a well-established general principle in protein biochemistry and does not constitute memorization of a specific database entry."
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

**Accession:** `Q9W3Y1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 200. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W3Y1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.041859+00:00.  

```json
"Q9W3Y1"
```

Source SHA-256: `9797bfc846105931ee1dd7a285106ef06778360b3a9fa2f086bb0a6444ed1c98`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W3Y1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.041859+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cell division cycle 7"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25451925","source":"PubMed"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0028360","source":"FlyBase"}],"value":"non-specific serine/threonine protein kinase Cdc7"}}}
```

Source SHA-256: `9797bfc846105931ee1dd7a285106ef06778360b3a9fa2f086bb0a6444ed1c98`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W3Y1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.041859+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000269","id":"25451925","source":"PubMed"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `9797bfc846105931ee1dd7a285106ef06778360b3a9fa2f086bb0a6444ed1c98`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W3Y1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.041859+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"},{"evidenceCode":"ECO:0000269","id":"25451925","source":"PubMed"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `9797bfc846105931ee1dd7a285106ef06778360b3a9fa2f086bb0a6444ed1c98`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W3Y1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.041859+00:00.  

```json
{"citation":{"authors":["Stephenson R.","Hosler M.R.","Gavande N.S.","Ghosh A.K.","Weake V.M."],"citationCrossReferences":[{"database":"PubMed","id":"25451925"},{"database":"DOI","id":"10.1074/jbc.m114.597948"}],"citationType":"journal article","firstPage":"1332","id":"25451925","journal":"J. Biol. Chem.","lastPage":"1347","publicationDate":"2015","title":"Characterization of a Drosophila ortholog of the Cdc7 kinase: a role for Cdc7 in endoreplication independent of Chiffon.","volume":"290"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","IDENTIFICATION IN DDK COMPLEX","INTERACTION WITH CHIF","DISRUPTION PHENOTYPE","MUTAGENESIS OF ASP-269"]}
```

Source SHA-256: `9797bfc846105931ee1dd7a285106ef06778360b3a9fa2f086bb0a6444ed1c98`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W3Y1?format=txt&versions=200)  
**Locator:** `lines 1-18`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 200 / 2.  
**Retrieved:** 2026-11-02T04:33:53.792772+00:00.  

```text
ID   CDC7_DROME              Reviewed;         700 AA.
AC   Q9W3Y1; Q3KN27; X2JCT3;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2002, sequence version 2.
DT   28-JAN-2026, entry version 200.
DE   RecName: Full=non-specific serine/threonine protein kinase Cdc7 {ECO:0000312|FlyBase:FBgn0028360};
DE            EC=2.7.11.1 {ECO:0000269|PubMed:25451925};
DE   AltName: Full=Cell division cycle 7 {ECO:0000305};
GN   Name=Cdc7 {ECO:0000303|PubMed:25451925, ECO:0000312|FlyBase:FBgn0028360};
GN   Synonyms=l(1)G0148 {ECO:0000312|FlyBase:FBgn0028360},
GN   l(1)G0149 {ECO:0000312|FlyBase:FBgn0028360},
GN   l(1)G0461 {ECO:0000312|FlyBase:FBgn0028360};
GN   ORFNames=CG32742 {ECO:0000312|FlyBase:FBgn0028360};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `97004b763f3ffe1c7894222610f250f7760de0f848dcd41e62799d755551771d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W3Y1?format=txt&versions=200)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 200 / 2.  
**Retrieved:** 2026-11-02T04:33:53.792772+00:00.  

```text
DE   RecName: Full=non-specific serine/threonine protein kinase Cdc7 {ECO:0000312|FlyBase:FBgn0028360};
DE            EC=2.7.11.1 {ECO:0000269|PubMed:25451925};
DE   AltName: Full=Cell division cycle 7 {ECO:0000305};
```

Source SHA-256: `97004b763f3ffe1c7894222610f250f7760de0f848dcd41e62799d755551771d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W3Y1?format=txt&versions=200)  
**Locator:** `lines 77-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 200 / 2.  
**Retrieved:** 2026-11-02T04:33:53.792772+00:00.  

```text
RN   [4] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, IDENTIFICATION IN DDK
RP   COMPLEX, INTERACTION WITH CHIF, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF
RP   ASP-269.
RX   PubMed=25451925; DOI=10.1074/jbc.m114.597948;
RA   Stephenson R., Hosler M.R., Gavande N.S., Ghosh A.K., Weake V.M.;
RT   "Characterization of a Drosophila ortholog of the Cdc7 kinase: a role for
RT   Cdc7 in endoreplication independent of Chiffon.";
RL   J. Biol. Chem. 290:1332-1347(2015).
```

Source SHA-256: `97004b763f3ffe1c7894222610f250f7760de0f848dcd41e62799d755551771d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W3Y1?format=txt&versions=200)  
**Locator:** `lines 109-115`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 200 / 2.  
**Retrieved:** 2026-11-02T04:33:53.792772+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027,
CC         ECO:0000269|PubMed:25451925};
```

Source SHA-256: `97004b763f3ffe1c7894222610f250f7760de0f848dcd41e62799d755551771d`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W3Y1?format=txt&versions=200)  
**Locator:** `lines 116-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 200 / 2.  
**Retrieved:** 2026-11-02T04:33:53.792772+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027,
CC         ECO:0000269|PubMed:25451925};
```

Source SHA-256: `97004b763f3ffe1c7894222610f250f7760de0f848dcd41e62799d755551771d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 197. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
