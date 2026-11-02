# catalytic_activity_0176

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVASKIAWKFILPNCFKAKNDRNILPSETKIIQICKQINSDHHHSRLAISDISTDSRSVFISLDDLSSNAIIGSNLHIFTYAELKIITSKFSSANFLGKGGFGPVHKGFIDDKIKPGLKAQPVAVKLLDLDGNQGHQEWLTEVVFLGQLRHPHLVKLIGYCWEEEQRLLVYEYMARGNLENHLFSRYSSCLPWSTRIKIAVGAAKGLAFLHGEEKPVIYRDFKASNILLDSDYKAKLSDFGLAKDGPEGDDTHVSTRVMGTHGYAAPEYIMTGHLTSKSDVYSFGVVLLELITGRPAMDKNRPIRERNLVDWARPMLRDFHKLDRIMDPRLEGQYSTEGAKKVAALAYQCLSHQPRSRPTMSNVVKSLEPISELTDIPIGPFVYVVPSSECDKELEIGALKSKLDEEKKMNVNEDEQKGARRHGHRHKHRPKSSAAAAAVYSDTHMQNFALSHERTNKKHILK

[Multiple Choices]
A. uridine(out) = uridine(in)
B. L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)
C. 17-O-acetylajmaline + H2O = ajmaline + acetate + H(+)
D. enterobactin + 3 H2O = 3 N-(2,3-dihydroxybenzoyl)-L-serine + 2 H(+)
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

> The supplied sequence exactly matches the 463-aa UniProt entry annotated as a serine/threonine-protein kinase, and that entry lists the reaction in choice B. The catalytic-activity annotation is supported by a PROSITE-ProRule computational inference; the supplied evidence does not establish direct experimental measurement of this reaction.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a protein-kinase-like catalytic region, including a glycine-rich region consistent with ATP binding and a DFG-like motif. That makes ATP-dependent protein phosphorylation the biologically fitting choice among these options; the other choices describe unrelated transport or specialized small-molecule reactions.


**Missing item-specific fact**

> No item-specific annotation is required to distinguish the broad reaction class. Identifying this particular kinase's documented serine and threonine activities would require protein-specific evidence, but the choices make protein phosphorylation the meaningful match.


**Reason**

> A kinase-domain inference from the supplied sequence meaningfully favors B over the chemically unrelated distractors. This is a defensible class-level inference, not proof of the exact reaction from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B is consistent with a protein kinase. The matched entry also annotates threonine phosphorylation, but no separate threonine option is offered.


### Important caveats

- The cited catalytic-activity annotations are computationally inferred using PROSITE-ProRule, not demonstrated by experimental evidence in the supplied excerpts.
- The sequence match and historical annotation support applicability to this sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a protein-kinase-like catalytic region, including a glycine-rich region consistent with ATP binding and a DFG-like motif. That makes ATP-dependent protein phosphorylation the biologically fitting choice among these options; the other choices describe unrelated transport or specialized small-molecule reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific annotation is required to distinguish the broad reaction class. Identifying this particular kinase's documented serine and threonine activities would require protein-specific evidence, but the choices make protein phosphorylation the meaningful match.",
    "reason": "A kinase-domain inference from the supplied sequence meaningfully favors B over the chemically unrelated distractors. This is a defensible class-level inference, not proof of the exact reaction from sequence alone."
  },
  "case_id": "catalytic_activity_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 463-aa UniProt entry annotated as a serine/threonine-protein kinase, and that entry lists the reaction in choice B. The catalytic-activity annotation is supported by a PROSITE-ProRule computational inference; the supplied evidence does not establish direct experimental measurement of this reaction."
  },
  "important_caveats": [
    "The cited catalytic-activity annotations are computationally inferred using PROSITE-ProRule, not demonstrated by experimental evidence in the supplied excerpts.",
    "The sequence match and historical annotation support applicability to this sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B is consistent with a protein kinase. The matched entry also annotates threonine phosphorylation, but no separate threonine option is offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 463-aa UniProt entry annotated as a serine/threonine-protein kinase, and that entry lists the reaction in choice B. The catalytic-activity annotation is supported by a PROSITE-ProRule computational inference; the supplied evidence does not establish direct experimental measurement of this reaction.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a protein-kinase-like catalytic region, including a glycine-rich region consistent with ATP binding and a DFG-like motif. That makes ATP-dependent protein phosphorylation the biologically fitting choice among these options; the other choices describe unrelated transport or specialized small-molecule reactions.",
    "missing_item_specific_fact": "No item-specific annotation is required to distinguish the broad reaction class. Identifying this particular kinase's documented serine and threonine activities would require protein-specific evidence, but the choices make protein phosphorylation the meaningful match.",
    "reason": "A kinase-domain inference from the supplied sequence meaningfully favors B over the chemically unrelated distractors. This is a defensible class-level inference, not proof of the exact reaction from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B is consistent with a protein kinase. The matched entry also annotates threonine phosphorylation, but no separate threonine option is offered."
  },
  "important_caveats": [
    "The cited catalytic-activity annotations are computationally inferred using PROSITE-ProRule, not demonstrated by experimental evidence in the supplied excerpts.",
    "The sequence match and historical annotation support applicability to this sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ0 (sequence matched) annotates this protein as 'EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase' (EC 2.7.11.1) with catalytic activity 'L-seryl-&#91;protein&#93; + ATP = O-phospho-L-seryl-&#91;protein&#93; + ADP + H(+)'. The EC assignment is based on PROSITE-ProRule PRU10027 (computational rule-based, ECO:0000255), while the protein name and function are supported by PubMed:39488762. The sequence itself contains canonical protein kinase motifs (GxGxxG glycine-rich loop 'GSGFGPVHK', β3 lysine, catalytic loop, DFG motif 'SDFGLAK', APE motif 'AAPEY'), confirming kinase activity. The expected answer B matches the annotated catalytic reaction exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 463-aa sequence contains an unambiguous protein kinase domain with all canonical sub-motifs: a glycine-rich loop (GSGFGPVHKG), a β3 lysine, a catalytic loop with HRD-like residues, the DFG activation-segment motif (SDFGLAK), and an APE motif (AAPEY). These motifs are diagnostic of the protein kinase superfamily and are incompatible with the three distractors: (A) a uridine transporter (would require ~12 transmembrane helices and MFS/NCS2 motifs), (C) a carboxylesterase acting on acetylajmaline (would require an α/β-hydrolase fold with a Ser-His-Asp catalytic triad), and (D) an enterobactin esterase (also a hydrolase fold). The only option involving ATP-dependent phosphorylation of a protein substrate is B, which is the sole reaction consistent with the observed kinase architecture. No tyrosine-kinase option is offered, so the Ser/Thr vs Tyr distinction is not required.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The kinase domain is recognizable from the sequence by general protein-kinase motif knowledge, and all three distractors belong to entirely different enzyme classes (transporter, hydrolases). A knowledgeable reader can eliminate A, C, and D and select B without needing to recall this specific protein's UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is annotated with both Ser and Thr phosphorylation activities (C5, C6), but only the Ser variant appears among the choices. The Thr reaction is not offered, so no ambiguity arises. All other options (transporter, two hydrolases) are incompatible with the observed kinase domain.


### Important caveats

- The EC 2.7.11.1 assignment is based on PROSITE-ProRule (ECO:0000255), a computational pattern-matching rule, not direct experimental measurement of Ser/Thr specificity. However, the protein is described as a serine/threonine-protein kinase in the primary literature (PubMed:39488762).
- The sequence-match is exact (SHA-256 identical) between the benchmark input and both the current and historical (entry version 2) UniProt records.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what a model could infer from the supplied sequence and choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 463-aa sequence contains an unambiguous protein kinase domain with all canonical sub-motifs: a glycine-rich loop (GSGFGPVHKG), a β3 lysine, a catalytic loop with HRD-like residues, the DFG activation-segment motif (SDFGLAK), and an APE motif (AAPEY). These motifs are diagnostic of the protein kinase superfamily and are incompatible with the three distractors: (A) a uridine transporter (would require ~12 transmembrane helices and MFS/NCS2 motifs), (C) a carboxylesterase acting on acetylajmaline (would require an α/β-hydrolase fold with a Ser-His-Asp catalytic triad), and (D) an enterobactin esterase (also a hydrolase fold). The only option involving ATP-dependent phosphorylation of a protein substrate is B, which is the sole reaction consistent with the observed kinase architecture. No tyrosine-kinase option is offered, so the Ser/Thr vs Tyr distinction is not required.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The kinase domain is recognizable from the sequence by general protein-kinase motif knowledge, and all three distractors belong to entirely different enzyme classes (transporter, hydrolases). A knowledgeable reader can eliminate A, C, and D and select B without needing to recall this specific protein's UniProt annotation."
  },
  "case_id": "catalytic_activity_0176",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ0 (sequence matched) annotates this protein as 'EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase' (EC 2.7.11.1) with catalytic activity 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)'. The EC assignment is based on PROSITE-ProRule PRU10027 (computational rule-based, ECO:0000255), while the protein name and function are supported by PubMed:39488762. The sequence itself contains canonical protein kinase motifs (GxGxxG glycine-rich loop 'GSGFGPVHK', β3 lysine, catalytic loop, DFG motif 'SDFGLAK', APE motif 'AAPEY'), confirming kinase activity. The expected answer B matches the annotated catalytic reaction exactly."
  },
  "important_caveats": [
    "The EC 2.7.11.1 assignment is based on PROSITE-ProRule (ECO:0000255), a computational pattern-matching rule, not direct experimental measurement of Ser/Thr specificity. However, the protein is described as a serine/threonine-protein kinase in the primary literature (PubMed:39488762).",
    "The sequence-match is exact (SHA-256 identical) between the benchmark input and both the current and historical (entry version 2) UniProt records.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what a model could infer from the supplied sequence and choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is annotated with both Ser and Thr phosphorylation activities (C5, C6), but only the Ser variant appears among the choices. The Thr reaction is not offered, so no ambiguity arises. All other options (transporter, two hydrolases) are incompatible with the observed kinase domain."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0176",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ0 (sequence matched) annotates this protein as 'EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase' (EC 2.7.11.1) with catalytic activity 'L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)'. The EC assignment is based on PROSITE-ProRule PRU10027 (computational rule-based, ECO:0000255), while the protein name and function are supported by PubMed:39488762. The sequence itself contains canonical protein kinase motifs (GxGxxG glycine-rich loop 'GSGFGPVHK', β3 lysine, catalytic loop, DFG motif 'SDFGLAK', APE motif 'AAPEY'), confirming kinase activity. The expected answer B matches the annotated catalytic reaction exactly.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 463-aa sequence contains an unambiguous protein kinase domain with all canonical sub-motifs: a glycine-rich loop (GSGFGPVHKG), a β3 lysine, a catalytic loop with HRD-like residues, the DFG activation-segment motif (SDFGLAK), and an APE motif (AAPEY). These motifs are diagnostic of the protein kinase superfamily and are incompatible with the three distractors: (A) a uridine transporter (would require ~12 transmembrane helices and MFS/NCS2 motifs), (C) a carboxylesterase acting on acetylajmaline (would require an α/β-hydrolase fold with a Ser-His-Asp catalytic triad), and (D) an enterobactin esterase (also a hydrolase fold). The only option involving ATP-dependent phosphorylation of a protein substrate is B, which is the sole reaction consistent with the observed kinase architecture. No tyrosine-kinase option is offered, so the Ser/Thr vs Tyr distinction is not required.",
    "missing_item_specific_fact": "",
    "reason": "The kinase domain is recognizable from the sequence by general protein-kinase motif knowledge, and all three distractors belong to entirely different enzyme classes (transporter, hydrolases). A knowledgeable reader can eliminate A, C, and D and select B without needing to recall this specific protein's UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is annotated with both Ser and Thr phosphorylation activities (C5, C6), but only the Ser variant appears among the choices. The Thr reaction is not offered, so no ambiguity arises. All other options (transporter, two hydrolases) are incompatible with the observed kinase domain."
  },
  "important_caveats": [
    "The EC 2.7.11.1 assignment is based on PROSITE-ProRule (ECO:0000255), a computational pattern-matching rule, not direct experimental measurement of Ser/Thr specificity. However, the protein is described as a serine/threonine-protein kinase in the primary literature (PubMed:39488762).",
    "The sequence-match is exact (SHA-256 identical) between the benchmark input and both the current and historical (entry version 2) UniProt records.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what a model could infer from the supplied sequence and choices."
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

**Accession:** `P0DXJ0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 2. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.004320+00:00.  

```json
"P0DXJ0"
```

Source SHA-256: `1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.004320+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39488762","source":"PubMed"}],"value":"EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39488762","source":"PubMed"}],"value":"NbEIR"}]}}
```

Source SHA-256: `1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.004320+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ0.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:15.004320+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.7.11.1","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU10027","source":"PROSITE-ProRule"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `1fb49b61ea018363feefe6e568f67a9f960b07057251e4e624f603a1b238380a`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:19.546423+00:00.  

```text
ID   EIR_NICBE               Reviewed;         463 AA.
AC   P0DXJ0;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   18-JUN-2025, sequence version 1.
DT   28-JAN-2026, entry version 2.
DE   RecName: Full=EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase {ECO:0000303|PubMed:39488762};
DE            Short=NbEIR {ECO:0000303|PubMed:39488762};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
GN   Name=EIR {ECO:0000303|PubMed:39488762};
GN   ORFNames=NbS00058880g0009 {ECO:0000303|PubMed:39488762};
OS   Nicotiana benthamiana.
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Solanales; Solanaceae; Nicotianoideae; Nicotianeae;
OC   Nicotiana.
OX   NCBI_TaxID=4100;
```

Source SHA-256: `dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:19.546423+00:00.  

```text
DE   RecName: Full=EPD1-interacting receptor-like cytoplasmic serine/threonine-protein kinase {ECO:0000303|PubMed:39488762};
DE            Short=NbEIR {ECO:0000303|PubMed:39488762};
DE            EC=2.7.11.1 {ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2)  
**Locator:** `lines 38-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:19.546423+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ0?format=txt&versions=2)  
**Locator:** `lines 44-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 2 / 1.  
**Retrieved:** 2026-11-01T06:28:19.546423+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.1;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU10027};
```

Source SHA-256: `dfc72a9fe284e8d09ff624e621a36800a15b634cee3411254b16ccf4f17ccdc8`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 176. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
