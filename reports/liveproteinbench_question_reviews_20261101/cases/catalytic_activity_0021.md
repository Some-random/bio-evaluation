# catalytic_activity_0021

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **A** — Hydrolysis of alpha-(2-&gt;3)-, alpha-(2-&gt;6)-, alpha-(2-&gt;8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEPSKLFTMSDNATFAPGPVVNAADKKTFRTCFRILVLSVQAVTLILVIVTLGELVRMINDQGLSNQLSSIADKIRESATMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATIRTGKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYISMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYVSTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPTGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGNQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.
B. 4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+)
C. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
D. L-fucose + NAD(+) = L-fucono-1,5-lactone + NADH + H(+)
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

> The exact sequence matches the Mumps orthorubulavirus hemagglutinin-neuraminidase entry, whose catalytic activity is the reaction in choice A. The annotation cites experimental evidence for EC 3.2.1.18, although the primary study was not independently assessed here.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a hydrophobic segment consistent with membrane anchoring and a large extracellular region, which may make a membrane-associated viral protein more plausible than the soluble enzymes in B–D. That broad inference does not establish sialidase activity or the specific linkages in A.


**Missing item-specific fact**

> The protein-specific identification as a hemagglutinin-neuraminidase with sialidase activity is absent from the input and is needed to select A confidently.


**Reason**

> The sequence and choices provide, at most, broad contextual clues. Distinguishing the specific catalytic reaction requires a protein-specific functional annotation or experimental knowledge, not merely general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports A for the sequence-matched protein; the other choices describe distinct reactions without comparable support.


### Important caveats

- The source annotation reports experimental evidence associated with a 2024 publication and specifies strain 13V165E2; the primary paper was not comprehensively retrieved or independently validated.
- Reviewer-only accession and annotation evidence were not present in the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic segment consistent with membrane anchoring and a large extracellular region, which may make a membrane-associated viral protein more plausible than the soluble enzymes in B–D. That broad inference does not establish sialidase activity or the specific linkages in A.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as a hemagglutinin-neuraminidase with sialidase activity is absent from the input and is needed to select A confidently.",
    "reason": "The sequence and choices provide, at most, broad contextual clues. Distinguishing the specific catalytic reaction requires a protein-specific functional annotation or experimental knowledge, not merely general biological reasoning."
  },
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Mumps orthorubulavirus hemagglutinin-neuraminidase entry, whose catalytic activity is the reaction in choice A. The annotation cites experimental evidence for EC 3.2.1.18, although the primary study was not independently assessed here."
  },
  "important_caveats": [
    "The source annotation reports experimental evidence associated with a 2024 publication and specifies strain 13V165E2; the primary paper was not comprehensively retrieved or independently validated.",
    "Reviewer-only accession and annotation evidence were not present in the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A for the sequence-matched protein; the other choices describe distinct reactions without comparable support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Mumps orthorubulavirus hemagglutinin-neuraminidase entry, whose catalytic activity is the reaction in choice A. The annotation cites experimental evidence for EC 3.2.1.18, although the primary study was not independently assessed here.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a hydrophobic segment consistent with membrane anchoring and a large extracellular region, which may make a membrane-associated viral protein more plausible than the soluble enzymes in B–D. That broad inference does not establish sialidase activity or the specific linkages in A.",
    "missing_item_specific_fact": "The protein-specific identification as a hemagglutinin-neuraminidase with sialidase activity is absent from the input and is needed to select A confidently.",
    "reason": "The sequence and choices provide, at most, broad contextual clues. Distinguishing the specific catalytic reaction requires a protein-specific functional annotation or experimental knowledge, not merely general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports A for the sequence-matched protein; the other choices describe distinct reactions without comparable support."
  },
  "important_caveats": [
    "The source annotation reports experimental evidence associated with a 2024 publication and specifies strain 13V165E2; the primary paper was not comprehensively retrieved or independently validated.",
    "Reviewer-only accession and annotation evidence were not present in the evaluated model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 582-aa sequence matches UniProt Q9WAF5 (Mumps orthorubulavirus Hemagglutinin-neuraminidase, HN_MUMPV) exactly (SHA-256 confirmed in both current and historical snapshots). The UniProt entry annotates EC 3.2.1.18 with the catalytic activity text identical to Choice A, supported by experimental evidence (ECO:0000269, PubMed:39088577, a 2024 Glycobiology paper on sialidase inhibitors suppressing mumps virus replication). The annotation is present in both the current entry (v132) and the archived entry (v130, first released 2026-01-28), so the key was available at the benchmark construction cutoff.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a hydrophobic stretch near the N-terminus (approx. residues 30–60) consistent with a type-II transmembrane anchor, multiple N-linked glycosylation sequons (N-X-S/T), and a length (~580 aa) typical of paramyxovirus surface glycoproteins. These features indicate a membrane-anchored viral surface glycoprotein that contacts host-cell surface glycans. Among the four choices, only A (neuraminidase/sialidase hydrolysis of sialic-acid linkages on cell-surface glycoconjugates) describes an activity mechanistically consistent with a membrane-tethered viral attachment protein. Choices B (radical-SAM taurine dioxygenase), C (soluble lipoxygenase), and D (soluble NAD-dependent fucose dehydrogenase) all describe activities of soluble, non-membrane enzymes with no plausible role for a type-II TM viral glycoprotein. Eliminating B, C, and D on the basis of membrane topology and biological context is a defensible general-knowledge argument that does not require exact sequence-to-database lookup.


**Missing item-specific fact**

> None strictly required. Full confidence that the specific sialidase linkages (α2→3, α2→6, α2→8) match this particular enzyme would benefit from recognizing the paramyxovirus HN family, but the coarse elimination of B/C/D via membrane-topology reasoning is sufficient to single out A among the given options.


**Reason**

> A model with general virology and membrane-biology knowledge can note the type-II TM domain, glycosylation pattern, and viral-glycoprotein architecture, then reason that only a cell-surface glycan-acting hydrolase (sialidase) fits among the four choices. The three distractors are all soluble enzymes whose catalytic mechanisms and cellular contexts are incompatible with a membrane-anchored viral surface protein. This constitutes a concrete biological argument grounded in the supplied sequence features rather than a pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices B, C, and D describe soluble enzymes (radical-SAM dioxygenase, lipoxygenase, NAD-dependent dehydrogenase) with no membrane-anchoring requirement, making them inconsistent with the observed type-II TM topology and viral glycoprotein context. Only A describes a membrane-associated glycan-acting hydrolase. No second option is defensible given the sequence features.


### Important caveats

- The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational, strengthening the key.
- The reasoning argument (TM domain → membrane protein → eliminates soluble enzymes) is a coarse but valid discriminator among these four specific choices; it would not, by itself, distinguish sialidase from other membrane glycosidases if such alternatives were present.
- The UniProt entry was first publicly released 2025-04-09 (entry v130 in UniSave, 2026-01-28); the benchmark's exact construction date is unknown, but the annotation was available well before the 2026-05-07 cutoff.
- Sequence match is exact (SHA-256 identical) across current and historical snapshots; no numbering or isoform ambiguity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a hydrophobic stretch near the N-terminus (approx. residues 30–60) consistent with a type-II transmembrane anchor, multiple N-linked glycosylation sequons (N-X-S/T), and a length (~580 aa) typical of paramyxovirus surface glycoproteins. These features indicate a membrane-anchored viral surface glycoprotein that contacts host-cell surface glycans. Among the four choices, only A (neuraminidase/sialidase hydrolysis of sialic-acid linkages on cell-surface glycoconjugates) describes an activity mechanistically consistent with a membrane-tethered viral attachment protein. Choices B (radical-SAM taurine dioxygenase), C (soluble lipoxygenase), and D (soluble NAD-dependent fucose dehydrogenase) all describe activities of soluble, non-membrane enzymes with no plausible role for a type-II TM viral glycoprotein. Eliminating B, C, and D on the basis of membrane topology and biological context is a defensible general-knowledge argument that does not require exact sequence-to-database lookup.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Full confidence that the specific sialidase linkages (α2→3, α2→6, α2→8) match this particular enzyme would benefit from recognizing the paramyxovirus HN family, but the coarse elimination of B/C/D via membrane-topology reasoning is sufficient to single out A among the given options.",
    "reason": "A model with general virology and membrane-biology knowledge can note the type-II TM domain, glycosylation pattern, and viral-glycoprotein architecture, then reason that only a cell-surface glycan-acting hydrolase (sialidase) fits among the four choices. The three distractors are all soluble enzymes whose catalytic mechanisms and cellular contexts are incompatible with a membrane-anchored viral surface protein. This constitutes a concrete biological argument grounded in the supplied sequence features rather than a pure database lookup."
  },
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 582-aa sequence matches UniProt Q9WAF5 (Mumps orthorubulavirus Hemagglutinin-neuraminidase, HN_MUMPV) exactly (SHA-256 confirmed in both current and historical snapshots). The UniProt entry annotates EC 3.2.1.18 with the catalytic activity text identical to Choice A, supported by experimental evidence (ECO:0000269, PubMed:39088577, a 2024 Glycobiology paper on sialidase inhibitors suppressing mumps virus replication). The annotation is present in both the current entry (v132) and the archived entry (v130, first released 2026-01-28), so the key was available at the benchmark construction cutoff."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational, strengthening the key.",
    "The reasoning argument (TM domain → membrane protein → eliminates soluble enzymes) is a coarse but valid discriminator among these four specific choices; it would not, by itself, distinguish sialidase from other membrane glycosidases if such alternatives were present.",
    "The UniProt entry was first publicly released 2025-04-09 (entry v130 in UniSave, 2026-01-28); the benchmark's exact construction date is unknown, but the annotation was available well before the 2026-05-07 cutoff.",
    "Sequence match is exact (SHA-256 identical) across current and historical snapshots; no numbering or isoform ambiguity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B, C, and D describe soluble enzymes (radical-SAM dioxygenase, lipoxygenase, NAD-dependent dehydrogenase) with no membrane-anchoring requirement, making them inconsistent with the observed type-II TM topology and viral glycoprotein context. Only A describes a membrane-associated glycan-acting hydrolase. No second option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 582-aa sequence matches UniProt Q9WAF5 (Mumps orthorubulavirus Hemagglutinin-neuraminidase, HN_MUMPV) exactly (SHA-256 confirmed in both current and historical snapshots). The UniProt entry annotates EC 3.2.1.18 with the catalytic activity text identical to Choice A, supported by experimental evidence (ECO:0000269, PubMed:39088577, a 2024 Glycobiology paper on sialidase inhibitors suppressing mumps virus replication). The annotation is present in both the current entry (v132) and the archived entry (v130, first released 2026-01-28), so the key was available at the benchmark construction cutoff.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a hydrophobic stretch near the N-terminus (approx. residues 30–60) consistent with a type-II transmembrane anchor, multiple N-linked glycosylation sequons (N-X-S/T), and a length (~580 aa) typical of paramyxovirus surface glycoproteins. These features indicate a membrane-anchored viral surface glycoprotein that contacts host-cell surface glycans. Among the four choices, only A (neuraminidase/sialidase hydrolysis of sialic-acid linkages on cell-surface glycoconjugates) describes an activity mechanistically consistent with a membrane-tethered viral attachment protein. Choices B (radical-SAM taurine dioxygenase), C (soluble lipoxygenase), and D (soluble NAD-dependent fucose dehydrogenase) all describe activities of soluble, non-membrane enzymes with no plausible role for a type-II TM viral glycoprotein. Eliminating B, C, and D on the basis of membrane topology and biological context is a defensible general-knowledge argument that does not require exact sequence-to-database lookup.",
    "missing_item_specific_fact": "None strictly required. Full confidence that the specific sialidase linkages (α2→3, α2→6, α2→8) match this particular enzyme would benefit from recognizing the paramyxovirus HN family, but the coarse elimination of B/C/D via membrane-topology reasoning is sufficient to single out A among the given options.",
    "reason": "A model with general virology and membrane-biology knowledge can note the type-II TM domain, glycosylation pattern, and viral-glycoprotein architecture, then reason that only a cell-surface glycan-acting hydrolase (sialidase) fits among the four choices. The three distractors are all soluble enzymes whose catalytic mechanisms and cellular contexts are incompatible with a membrane-anchored viral surface protein. This constitutes a concrete biological argument grounded in the supplied sequence features rather than a pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B, C, and D describe soluble enzymes (radical-SAM dioxygenase, lipoxygenase, NAD-dependent dehydrogenase) with no membrane-anchoring requirement, making them inconsistent with the observed type-II TM topology and viral glycoprotein context. Only A describes a membrane-associated glycan-acting hydrolase. No second option is defensible given the sequence features."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269), not merely computational, strengthening the key.",
    "The reasoning argument (TM domain → membrane protein → eliminates soluble enzymes) is a coarse but valid discriminator among these four specific choices; it would not, by itself, distinguish sialidase from other membrane glycosidases if such alternatives were present.",
    "The UniProt entry was first publicly released 2025-04-09 (entry v130 in UniSave, 2026-01-28); the benchmark's exact construction date is unknown, but the annotation was available well before the 2026-05-07 cutoff.",
    "Sequence match is exact (SHA-256 identical) across current and historical snapshots; no numbering or isoform ambiguity."
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

**Accession:** `Q9WAF5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 130. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
"Q9WAF5"
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"commonName":"MuV","lineage":["Viruses","Riboviria","Orthornavirae","Negarnaviricota","Haploviricotina","Monjiviricetes","Mononegavirales","Paramyxoviridae","Rubulavirinae","Orthorubulavirus","Orthorubulavirus parotitidis"],"scientificName":"Mumps orthorubulavirus","taxonId":2560602}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39088577","source":"PubMed"}],"value":"3.2.1.18"}],"fullName":{"value":"Hemagglutinin-neuraminidase"}}}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.18","evidences":[{"evidenceCode":"ECO:0000269","id":"39088577","source":"PubMed"}],"name":"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates."}}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9WAF5.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:53.145631+00:00.  

```json
{"citation":{"authors":["Takahashi T.","Kurebayashi Y.","Otsubo T.","Ikeda K.","Konagaya K.","Suzuki S.","Yamazaki M.","Suzuki K.","Narimichi Y.","Minami A.","Takeuchi H."],"citationCrossReferences":[{"database":"PubMed","id":"39088577"},{"database":"DOI","id":"10.1093/glycob/cwae059"}],"citationType":"journal article","firstPage":"0","id":"39088577","journal":"Glycobiology","lastPage":"0","publicationDate":"2024","title":"Novel sialidase inhibitors suppress mumps virus replication and infection.","volume":"34"},"referenceComments":[{"type":"STRAIN","value":"13V165E2"}],"referenceNumber":6,"referencePositions":["CATALYTIC ACTIVITY"]}
```

Source SHA-256: `f2c4b74d6065a62ee3de80fb119bec8f410076958143fbd7300617256d292508`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-02T04:33:57.899829+00:00.  

```text
ID   HN_MUMPV                Reviewed;         582 AA.
AC   Q9WAF5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-NOV-1999, sequence version 1.
DT   28-JAN-2026, entry version 130.
DE   RecName: Full=Hemagglutinin-neuraminidase;
DE            EC=3.2.1.18 {ECO:0000269|PubMed:39088577};
GN   Name=HN {ECO:0000312|EMBL:BAG84572.1};
OS   Mumps orthorubulavirus (MuV).
OC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;
OC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;
OC   Orthorubulavirus; Orthorubulavirus parotitidis.
OX   NCBI_TaxID=2560602;
```

Source SHA-256: `eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-02T04:33:57.899829+00:00.  

```text
DE   RecName: Full=Hemagglutinin-neuraminidase;
DE            EC=3.2.1.18 {ECO:0000269|PubMed:39088577};
```

Source SHA-256: `eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)  
**Locator:** `lines 54-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-02T04:33:57.899829+00:00.  

```text
RN   [6]
RP   CATALYTIC ACTIVITY.
RC   STRAIN=13V165E2;
RX   PubMed=39088577; DOI=10.1093/glycob/cwae059;
RA   Takahashi T., Kurebayashi Y., Otsubo T., Ikeda K., Konagaya K., Suzuki S.,
RA   Yamazaki M., Suzuki K., Narimichi Y., Minami A., Takeuchi H.;
RT   "Novel sialidase inhibitors suppress mumps virus replication and
RT   infection.";
RL   Glycobiology 34:0-0(2024).
```

Source SHA-256: `eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9WAF5?format=txt&versions=130)  
**Locator:** `lines 93-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 130 / 1.  
**Retrieved:** 2026-11-02T04:33:57.899829+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-
CC         (2->8)- glycosidic linkages of terminal sialic acid residues in
CC         oligosaccharides, glycoproteins, glycolipids, colominic acid and
CC         synthetic substrates.; EC=3.2.1.18;
CC         Evidence={ECO:0000269|PubMed:39088577};
```

Source SHA-256: `eadd08bd5c3ea900dbbb7f47921a7b42efcfc71e9582122d1a848e3de17765f7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
