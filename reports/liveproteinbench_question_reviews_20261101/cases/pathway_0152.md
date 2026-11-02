# pathway_0152

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MWRLKIAEGGNDPYLYSTNNFVGRQTWEFDSEYGTPEAIKEVEEARQIFYKNRFQVKPCGDLLWRFQFLREKNFKQTIPQVKVGDGEEVTYEAASTTLKRSVNLLTALQADDGHWPAEIAGPQFFLPPLVFCLYITGHLNVVFNVHHREEILRSIYYHQNEDGGWGLHIEGHSTMFCTALNYICLRMLGVGPDEGDDNACPRARKWILDHGSVTHIPSWGKTWLSILGLFDWSGSNPMPPEFWILPTFMPMYPAKMWCYCRMVYMPMSYLYGKRFVGPITPLIKQLREELFSEPFEEIKWKKVRHLCAPEDLYYPHPLIQDLMWDSLYLFTEPLLTRWPFNNLIRQKALQVTMDHIHYEDENSRYITIGCVEKVLCMLACWVEDPNGVCYKKHLARVPDYIWIAEDGLKMQSFGSQQWDCGFAVQALLASNMSLDEIGPALKKGHFFIKESQVKDNPSGDFKSMHRHISKGSWTFSDQDHGWQVSDCTAEGLKCCLILSTMPPEIVGEKMDPERLYDSVNVLLSLQSENGGLSAWEPAGAQAWLELLNPTEFFADIVIEHEYVECTGASIQALVLFKKMYPGHRKKEIENFIAKAAKYLEDTQYPNGSWYGNWGVCFTYGTWFALGGLAAAGKTYANCAAMRKGVEFLLKSQKEDGGWGESYVSCPKKDFVPLEGPSNLTQTAWALMGLIYARQMERDPTPLHQAAKLLINSQLENGDFPQQEITGVFMKNCMLHYPMYRTIYPLWAIAEYRTHVPLRLS

[Multiple Choices]
A. capsule polysaccharide biosynthesis. .
B. fatty acid beta-oxidation. .
C. Secondary metabolite biosynthesis
D. LPS O-antigen biosynthesis. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry for beta-amyrin synthase 1, annotated to secondary metabolite and terpenoid biosynthesis. The pathway annotation is attributed to a publication with experimental evidence code ECO:0000269; this supports the key, though the supplied excerpts do not independently detail or validate the experiments.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence contains features characteristic of plant oxidosqualene/triterpene synthases, including repeated QW motifs and a DCTAE motif. That enzyme family is associated with terpenoid secondary-metabolite biosynthesis, unlike the bacterial polysaccharide pathways or fatty-acid beta-oxidation in the distractors.


**Missing item-specific fact**

> No specific database accession or experimental measurement is necessary for a defensible choice, although recognizing the enzyme-family motifs requires specialized sequence knowledge.


**Reason**

> The sequence provides a plausible family-level biological basis for choosing secondary metabolite biosynthesis; the reviewer-only annotation corroborates the key but was not supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The pathway annotation and the sequence-based enzyme-family inference point to choice C; the alternatives describe distinct pathway classes.


### Important caveats

- The sequence match and pathway annotation are reviewer-only evidence, not information provided in the original question.
- The cited evidence supports the annotation but the excerpts do not provide details of the underlying experimental methods.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence contains features characteristic of plant oxidosqualene/triterpene synthases, including repeated QW motifs and a DCTAE motif. That enzyme family is associated with terpenoid secondary-metabolite biosynthesis, unlike the bacterial polysaccharide pathways or fatty-acid beta-oxidation in the distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No specific database accession or experimental measurement is necessary for a defensible choice, although recognizing the enzyme-family motifs requires specialized sequence knowledge.",
    "reason": "The sequence provides a plausible family-level biological basis for choosing secondary metabolite biosynthesis; the reviewer-only annotation corroborates the key but was not supplied to the model."
  },
  "case_id": "pathway_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for beta-amyrin synthase 1, annotated to secondary metabolite and terpenoid biosynthesis. The pathway annotation is attributed to a publication with experimental evidence code ECO:0000269; this supports the key, though the supplied excerpts do not independently detail or validate the experiments."
  },
  "important_caveats": [
    "The sequence match and pathway annotation are reviewer-only evidence, not information provided in the original question.",
    "The cited evidence supports the annotation but the excerpts do not provide details of the underlying experimental methods."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The pathway annotation and the sequence-based enzyme-family inference point to choice C; the alternatives describe distinct pathway classes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for beta-amyrin synthase 1, annotated to secondary metabolite and terpenoid biosynthesis. The pathway annotation is attributed to a publication with experimental evidence code ECO:0000269; this supports the key, though the supplied excerpts do not independently detail or validate the experiments.",
    "evidence_ids": ["C1", "C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence contains features characteristic of plant oxidosqualene/triterpene synthases, including repeated QW motifs and a DCTAE motif. That enzyme family is associated with terpenoid secondary-metabolite biosynthesis, unlike the bacterial polysaccharide pathways or fatty-acid beta-oxidation in the distractors.",
    "missing_item_specific_fact": "No specific database accession or experimental measurement is necessary for a defensible choice, although recognizing the enzyme-family motifs requires specialized sequence knowledge.",
    "reason": "The sequence provides a plausible family-level biological basis for choosing secondary metabolite biosynthesis; the reviewer-only annotation corroborates the key but was not supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The pathway annotation and the sequence-based enzyme-family inference point to choice C; the alternatives describe distinct pathway classes."
  },
  "important_caveats": [
    "The sequence match and pathway annotation are reviewer-only evidence, not information provided in the original question.",
    "The cited evidence supports the annotation but the excerpts do not provide details of the underlying experimental methods."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAW1L0L7 (Beta-amyrin synthase 1 / SobAS1, EC 5.4.99.39, Saponaria officinalis) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The enzyme catalyzes cyclization of 2,3-oxidosqualene to beta-amyrin, a key step in saponin (triterpenoid) biosynthesis, which UniProt classifies under secondary metabolite biosynthesis. The sequence in the question matches the canonical entry (760 AA, SHA256 confirmed).

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The ~760-residue plant protein contains the conserved DCTAE motif (visible as 'SDCTAEGLK' near residue ~430), a hallmark of the oxidosqualene cyclase (OSC) superfamily. OSCs catalyze cyclization of 2,3-oxidosqualene into triterpenoids or sterols. In plants, triterpenoid cyclases (producing saponins, etc.) are classified as secondary metabolite biosynthesis enzymes. Options A (capsule polysaccharide biosynthesis) and D (LPS O-antigen biosynthesis) are bacterial pathways incompatible with a eukaryotic/plant protein. Option B (fatty acid beta-oxidation) involves acyl-CoA dehydrogenases and hydratases with completely different fold and sequence signatures. Thus, recognizing the DCTAE motif as an OSC marker and knowing that plant triterpenoid/saponin biosynthesis falls under secondary metabolite biosynthesis provides a concrete, general-biochemistry reasoning chain to select C.


**Missing item-specific fact**

> None critical. The DCTAE motif is a widely taught conserved motif in the squalene cyclase superfamily, and the classification of plant triterpenoid biosynthesis as 'secondary metabolite biosynthesis' is standard biochemical terminology. A model would need to recognize the motif and connect OSCs to terpenoid/secondary-metabolite pathways, but this is general knowledge rather than a single protein-specific lookup.


**Reason**

> The question provides a sequence with recognizable OSC hallmarks (DCTAE motif, ~760 AA length, plant-like composition). A model with general biochemistry knowledge can eliminate bacterial pathways (A, D), eliminate fatty acid beta-oxidation (B, wrong enzyme class), and identify the OSC→triterpenoid→secondary metabolite link for C. This is a reasoning chain grounded in conserved motif recognition and pathway taxonomy, not a single-item database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are exclusively bacterial pathways, clearly inapplicable to a plant protein. Option B (fatty acid beta-oxidation) involves a completely different enzyme superfamily (acyl-CoA dehydrogenases, hydratases, thiolases) with no resemblance to OSCs. Only C (secondary metabolite biosynthesis) is consistent with a plant oxidosqualene cyclase. No other option is defensible.


### Important caveats

- The reviewer evidence confirms the UniProt annotation is experimental (ECO:0000269, PubMed:39043959, Nat. Chem. Biol. 2025), not merely computational.
- The UniProt pathway taxonomy places triterpenoid biosynthesis under 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' A model that instead expects a 'Terpenoid biosynthesis' or 'Saponin biosynthesis' label might be momentarily uncertain, but among the four given choices, C is unambiguously the correct umbrella term.
- The DCTAE motif is shared across the broader squalene-cyclase superfamily (including sterol cyclases). Distinguishing triterpenoid (secondary metabolite) from sterol (primary metabolism) cyclases from sequence alone is non-trivial, but the question's option set does not include a 'sterol biosynthesis' distractor, so this ambiguity does not affect answer selection.
- The identity of the protein was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence and four pathway labels.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The ~760-residue plant protein contains the conserved DCTAE motif (visible as 'SDCTAEGLK' near residue ~430), a hallmark of the oxidosqualene cyclase (OSC) superfamily. OSCs catalyze cyclization of 2,3-oxidosqualene into triterpenoids or sterols. In plants, triterpenoid cyclases (producing saponins, etc.) are classified as secondary metabolite biosynthesis enzymes. Options A (capsule polysaccharide biosynthesis) and D (LPS O-antigen biosynthesis) are bacterial pathways incompatible with a eukaryotic/plant protein. Option B (fatty acid beta-oxidation) involves acyl-CoA dehydrogenases and hydratases with completely different fold and sequence signatures. Thus, recognizing the DCTAE motif as an OSC marker and knowing that plant triterpenoid/saponin biosynthesis falls under secondary metabolite biosynthesis provides a concrete, general-biochemistry reasoning chain to select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The DCTAE motif is a widely taught conserved motif in the squalene cyclase superfamily, and the classification of plant triterpenoid biosynthesis as 'secondary metabolite biosynthesis' is standard biochemical terminology. A model would need to recognize the motif and connect OSCs to terpenoid/secondary-metabolite pathways, but this is general knowledge rather than a single protein-specific lookup.",
    "reason": "The question provides a sequence with recognizable OSC hallmarks (DCTAE motif, ~760 AA length, plant-like composition). A model with general biochemistry knowledge can eliminate bacterial pathways (A, D), eliminate fatty acid beta-oxidation (B, wrong enzyme class), and identify the OSC→triterpenoid→secondary metabolite link for C. This is a reasoning chain grounded in conserved motif recognition and pathway taxonomy, not a single-item database lookup."
  },
  "case_id": "pathway_0152",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1L0L7 (Beta-amyrin synthase 1 / SobAS1, EC 5.4.99.39, Saponaria officinalis) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The enzyme catalyzes cyclization of 2,3-oxidosqualene to beta-amyrin, a key step in saponin (triterpenoid) biosynthesis, which UniProt classifies under secondary metabolite biosynthesis. The sequence in the question matches the canonical entry (760 AA, SHA256 confirmed)."
  },
  "important_caveats": [
    "The reviewer evidence confirms the UniProt annotation is experimental (ECO:0000269, PubMed:39043959, Nat. Chem. Biol. 2025), not merely computational.",
    "The UniProt pathway taxonomy places triterpenoid biosynthesis under 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' A model that instead expects a 'Terpenoid biosynthesis' or 'Saponin biosynthesis' label might be momentarily uncertain, but among the four given choices, C is unambiguously the correct umbrella term.",
    "The DCTAE motif is shared across the broader squalene-cyclase superfamily (including sterol cyclases). Distinguishing triterpenoid (secondary metabolite) from sterol (primary metabolism) cyclases from sequence alone is non-trivial, but the question's option set does not include a 'sterol biosynthesis' distractor, so this ambiguity does not affect answer selection.",
    "The identity of the protein was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence and four pathway labels."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are exclusively bacterial pathways, clearly inapplicable to a plant protein. Option B (fatty acid beta-oxidation) involves a completely different enzyme superfamily (acyl-CoA dehydrogenases, hydratases, thiolases) with no resemblance to OSCs. Only C (secondary metabolite biosynthesis) is consistent with a plant oxidosqualene cyclase. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0152",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1L0L7 (Beta-amyrin synthase 1 / SobAS1, EC 5.4.99.39, Saponaria officinalis) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The enzyme catalyzes cyclization of 2,3-oxidosqualene to beta-amyrin, a key step in saponin (triterpenoid) biosynthesis, which UniProt classifies under secondary metabolite biosynthesis. The sequence in the question matches the canonical entry (760 AA, SHA256 confirmed).",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The ~760-residue plant protein contains the conserved DCTAE motif (visible as 'SDCTAEGLK' near residue ~430), a hallmark of the oxidosqualene cyclase (OSC) superfamily. OSCs catalyze cyclization of 2,3-oxidosqualene into triterpenoids or sterols. In plants, triterpenoid cyclases (producing saponins, etc.) are classified as secondary metabolite biosynthesis enzymes. Options A (capsule polysaccharide biosynthesis) and D (LPS O-antigen biosynthesis) are bacterial pathways incompatible with a eukaryotic/plant protein. Option B (fatty acid beta-oxidation) involves acyl-CoA dehydrogenases and hydratases with completely different fold and sequence signatures. Thus, recognizing the DCTAE motif as an OSC marker and knowing that plant triterpenoid/saponin biosynthesis falls under secondary metabolite biosynthesis provides a concrete, general-biochemistry reasoning chain to select C.",
    "missing_item_specific_fact": "None critical. The DCTAE motif is a widely taught conserved motif in the squalene cyclase superfamily, and the classification of plant triterpenoid biosynthesis as 'secondary metabolite biosynthesis' is standard biochemical terminology. A model would need to recognize the motif and connect OSCs to terpenoid/secondary-metabolite pathways, but this is general knowledge rather than a single protein-specific lookup.",
    "reason": "The question provides a sequence with recognizable OSC hallmarks (DCTAE motif, ~760 AA length, plant-like composition). A model with general biochemistry knowledge can eliminate bacterial pathways (A, D), eliminate fatty acid beta-oxidation (B, wrong enzyme class), and identify the OSC→triterpenoid→secondary metabolite link for C. This is a reasoning chain grounded in conserved motif recognition and pathway taxonomy, not a single-item database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are exclusively bacterial pathways, clearly inapplicable to a plant protein. Option B (fatty acid beta-oxidation) involves a completely different enzyme superfamily (acyl-CoA dehydrogenases, hydratases, thiolases) with no resemblance to OSCs. Only C (secondary metabolite biosynthesis) is consistent with a plant oxidosqualene cyclase. No other option is defensible."
  },
  "important_caveats": [
    "The reviewer evidence confirms the UniProt annotation is experimental (ECO:0000269, PubMed:39043959, Nat. Chem. Biol. 2025), not merely computational.",
    "The UniProt pathway taxonomy places triterpenoid biosynthesis under 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' A model that instead expects a 'Terpenoid biosynthesis' or 'Saponin biosynthesis' label might be momentarily uncertain, but among the four given choices, C is unambiguously the correct umbrella term.",
    "The DCTAE motif is shared across the broader squalene-cyclase superfamily (including sterol cyclases). Distinguishing triterpenoid (secondary metabolite) from sterol (primary metabolism) cyclases from sequence alone is non-trivial, but the question's option set does not include a 'sterol biosynthesis' distractor, so this ambiguity does not affect answer selection.",
    "The identity of the protein was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence and four pathway labels."
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

**Accession:** `A0AAW1L0L7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
"A0AAW1L0L7"
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"commonName":"Common soapwort","lineage":["Eukaryota","Viridiplantae","Streptophyta","Embryophyta","Tracheophyta","Spermatophyta","Magnoliopsida","eudicotyledons","Gunneridae","Pentapetalae","Caryophyllales","Caryophyllaceae","Caryophylleae","Saponaria"],"scientificName":"Saponaria officinalis","synonyms":["Lychnis saponaria"],"taxonId":3572}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"5.4.99.39"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"Beta-amyrin synthase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SobAS1"}]}}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1L0L7.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:39.404038+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48160.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `2592e3175ed7f3aa157d1122cffa94daf5bffb1ead9950fe05e8661ef34af401`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:41.045167+00:00.  

```text
ID   BAMS1_SAPOF             Reviewed;         760 AA.
AC   A0AAW1L0L7;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=Beta-amyrin synthase 1 {ECO:0000303|PubMed:39043959};
DE            Short=SobAS1 {ECO:0000303|PubMed:39043959};
DE            EC=5.4.99.39 {ECO:0000269|PubMed:39043959};
GN   Name=bAS1 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11027757m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_05G236200 {ECO:0000312|EMBL:KAK9726778.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)  
**Locator:** `lines 17-26`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:41.045167+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:WWM48160.1}
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE
RP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.
RX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;
RA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,
RA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,
RA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,
RA   Leebens-Mack J., Osbourn A.;
RT   "Unlocking saponin biosynthesis in soapwort.";
RL   Nat. Chem. Biol. 21:215-226(2025).
```

Source SHA-256: `7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1L0L7?format=txt&versions=5)  
**Locator:** `lines 47-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:41.045167+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `7d24bcffc9a88c6f7648cda9de366740d6556c36d7d06892bf26b5abff0fe742`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 152. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
