# pathway_0162

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPHNTCTLQITRALLSRLHILFHSALVASVFYYRFSNFSSGPAWALMTFAELTLAFIWALTQAFRWRPVVRAVFGPEEIDPAQLPGLDVFICTADPRKEPVMEVMNSVVSALALDYPAEKLAVYLSDDGGSPLTREVIREAAVFGKYWVGFCGKYNVKTRCPEAYFSSFCDGERVDHNQDYLNDELSVKSKFEAFKKYVQKASEDATKCIVVNDRPSCVEIIHDSKQNGEGEVKMPLLVYVAREKRPGFNHHAKAGAINTLLRVSGLLSNSPFFLVLDCDMYCNDPTSARQAMCFHLDPKLAPSLAFVQYPQIFYNTSKNDIYDGQARAAFKTKYQGMDGLRGPVMSGTGYFLKRKALYGKPHDQDELLREQPTKAFGSSKIFIASLGENTCVALKGLSKDELLQETQKLAACTYESNTLWGSEVGYSYDCLLESTYCGYLLHCKGWISVYLYPKKPCFLGCATVDMNDAMLQIMKWTSGLIGVGISKFSPFTYAMSRISIMQSLCYAYFAFSGLFAVFFLIYGVVLPYSLLQGVPLFPKAGDPWLLAFAGVFISSLLQHLYEVLSSGETVKAWWNEQRIWIIKSITACLFGLLDAMLNKIGVLKASFRLTNKAVDKQKLDKYEKGRFDFQGAQMFMVPLMILVVFNLVSFFGGLRRTVIHKNYEDMFAQLFLSLFILALSYPIMEEIVRKARKGRS

[Multiple Choices]
A. Lipid metabolism
B. Secondary metabolite biosynthesis
C. capsule polysaccharide biosynthesis. .
D. Capsule biogenesis
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

> The exact sequence matches a UniProt entry annotating the protein as quillaic acid 3-O-glycosyltransferase and placing it in secondary metabolite biosynthesis (terpenoid biosynthesis). The pathway assertion cites a publication with ECO:0000269 evidence; this supports the key as a database annotation, though the primary paper was not independently assessed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a membrane-associated glycosyltransferase, which suggests a biosynthetic role but does not identify the specific substrate or pathway well enough to distinguish secondary-metabolite biosynthesis from the listed alternatives.


**Missing item-specific fact**

> The protein-specific functional fact that it glycosylates quillaic acid in saponin biosynthesis is needed to select secondary metabolite biosynthesis.


**Reason**

> That specific function and pathway are not supplied in the sequence or prompt. Inferring them requires an item-specific annotation, experimental result, or prior recognition of the protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein annotation supports B. The sequence alone does not resolve the alternatives, but that information gap does not establish another option as a defensible pathway for this protein.


### Important caveats

- The reviewer-only source is sequence-matched, including in the historical record, but the author's exact source snapshot is unknown.
- The pathway evidence is a cited database annotation; the underlying publication was not independently reviewed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated glycosyltransferase, which suggests a biosynthetic role but does not identify the specific substrate or pathway well enough to distinguish secondary-metabolite biosynthesis from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional fact that it glycosylates quillaic acid in saponin biosynthesis is needed to select secondary metabolite biosynthesis.",
    "reason": "That specific function and pathway are not supplied in the sequence or prompt. Inferring them requires an item-specific annotation, experimental result, or prior recognition of the protein."
  },
  "case_id": "pathway_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating the protein as quillaic acid 3-O-glycosyltransferase and placing it in secondary metabolite biosynthesis (terpenoid biosynthesis). The pathway assertion cites a publication with ECO:0000269 evidence; this supports the key as a database annotation, though the primary paper was not independently assessed here."
  },
  "important_caveats": [
    "The reviewer-only source is sequence-matched, including in the historical record, but the author's exact source snapshot is unknown.",
    "The pathway evidence is a cited database annotation; the underlying publication was not independently reviewed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation supports B. The sequence alone does not resolve the alternatives, but that information gap does not establish another option as a defensible pathway for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotating the protein as quillaic acid 3-O-glycosyltransferase and placing it in secondary metabolite biosynthesis (terpenoid biosynthesis). The pathway assertion cites a publication with ECO:0000269 evidence; this supports the key as a database annotation, though the primary paper was not independently assessed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a membrane-associated glycosyltransferase, which suggests a biosynthetic role but does not identify the specific substrate or pathway well enough to distinguish secondary-metabolite biosynthesis from the listed alternatives.",
    "missing_item_specific_fact": "The protein-specific functional fact that it glycosylates quillaic acid in saponin biosynthesis is needed to select secondary metabolite biosynthesis.",
    "reason": "That specific function and pathway are not supplied in the sequence or prompt. Inferring them requires an item-specific annotation, experimental result, or prior recognition of the protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein annotation supports B. The sequence alone does not resolve the alternatives, but that information gap does not establish another option as a defensible pathway for this protein."
  },
  "important_caveats": [
    "The reviewer-only source is sequence-matched, including in the historical record, but the author's exact source snapshot is unknown.",
    "The pathway evidence is a cited database annotation; the underlying publication was not independently reviewed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAW1HA02 (CSL1_SAPOF, Quillaic acid 3-O-glycosyltransferase) carries the explicit PATHWAY annotation 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with evidence code ECO:0000269 (experimental evidence from PubMed:39043959, Nat. Chem. Biol. 2025, 'Unlocking saponin biosynthesis in soapwort'). The protein glycosylates quillaic acid, a triterpenoid aglycone, placing it squarely in secondary metabolite (saponin) biosynthesis. The sequence in the question matches the UniProt entry exactly (SHA-256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can partially reason: (1) the protein is clearly eukaryotic (long single-pass membrane topology, no bacterial signal peptides or capsule-specific machinery), eliminating C and D; (2) conserved GT4-family motifs (e.g., 'HxxxH', 'DxD' regions) identify it as a glycosyltransferase. However, the critical step—choosing B (secondary metabolite biosynthesis) over A (lipid metabolism)—requires knowing that the substrate is quillaic acid, a triterpenoid secondary metabolite, rather than a phospholipid or fatty-acid intermediate. Triterpenoids are broadly 'lipophilic' and derived from the isoprenoid pathway, so a model reasoning only from sequence and general biology could plausibly select A. The CSL (Cellulose Synthase-Like) family name further muddies the distinction, as it superficially evokes polysaccharide biosynthesis.


**Missing item-specific fact**

> The identity of the glycosyl acceptor as quillaic acid (a triterpenoid saponin aglycone) and the organism (Saponaria officinalis, a saponin-producing plant). Neither the substrate specificity nor the organism is provided in the question input; only the raw 698-aa sequence is given. Without this item-specific fact, the A-vs-B distinction cannot be resolved by general biological reasoning from sequence alone.


**Reason**

> Eliminating C and D (bacterial capsule pathways) is achievable from the eukaryotic membrane-protein architecture. However, distinguishing lipid metabolism (A) from secondary metabolite biosynthesis (B) for a plant membrane glycosyltransferase demands knowledge of the specific substrate (quillaic acid → triterpenoid → secondary metabolite). This is a protein-specific experimental fact (ECO:0000269) not inferable from sequence motifs or general pathway logic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Triterpenoids (saponin aglycones) are isoprenoid-derived lipophilic molecules. A model or student reasoning broadly could classify a triterpenoid glycosyltransferase under 'lipid metabolism' (A), since terpenoids are a subclass of lipids in many textbook classifications. The UniProt annotation places it under 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (B), which is the more precise and correct classification, but the boundary between A and B is genuinely fuzzy without knowing the specific substrate context. Options C and D are clearly wrong (bacterial capsule pathways) and do not create ambiguity.


### Important caveats

- The pathway annotation (C5, H3) carries ECO:0000269 (experimental evidence), strengthening the key's reliability.
- The CSL family nomenclature ('Cellulose Synthase-Like') is a misnomer for this particular member, which does not synthesize cellulose but glycosylates a triterpenoid; this could mislead a model toward a polysaccharide-related answer.
- The organism (Saponaria officinalis) is not provided in the question input, removing a major contextual clue (soapwort is famous for saponins).
- The sequence is a 698-aa membrane protein with no obvious sequence-level signature that uniquely distinguishes 'secondary metabolite' from 'lipid' metabolism for a plant glycosyltransferase.
- Options C and D are near-duplicates (both bacterial capsule pathways) and serve as easy distractors; they do not affect the core A-vs-B difficulty.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can partially reason: (1) the protein is clearly eukaryotic (long single-pass membrane topology, no bacterial signal peptides or capsule-specific machinery), eliminating C and D; (2) conserved GT4-family motifs (e.g., 'HxxxH', 'DxD' regions) identify it as a glycosyltransferase. However, the critical step—choosing B (secondary metabolite biosynthesis) over A (lipid metabolism)—requires knowing that the substrate is quillaic acid, a triterpenoid secondary metabolite, rather than a phospholipid or fatty-acid intermediate. Triterpenoids are broadly 'lipophilic' and derived from the isoprenoid pathway, so a model reasoning only from sequence and general biology could plausibly select A. The CSL (Cellulose Synthase-Like) family name further muddies the distinction, as it superficially evokes polysaccharide biosynthesis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the glycosyl acceptor as quillaic acid (a triterpenoid saponin aglycone) and the organism (Saponaria officinalis, a saponin-producing plant). Neither the substrate specificity nor the organism is provided in the question input; only the raw 698-aa sequence is given. Without this item-specific fact, the A-vs-B distinction cannot be resolved by general biological reasoning from sequence alone.",
    "reason": "Eliminating C and D (bacterial capsule pathways) is achievable from the eukaryotic membrane-protein architecture. However, distinguishing lipid metabolism (A) from secondary metabolite biosynthesis (B) for a plant membrane glycosyltransferase demands knowledge of the specific substrate (quillaic acid → triterpenoid → secondary metabolite). This is a protein-specific experimental fact (ECO:0000269) not inferable from sequence motifs or general pathway logic."
  },
  "case_id": "pathway_0162",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1HA02 (CSL1_SAPOF, Quillaic acid 3-O-glycosyltransferase) carries the explicit PATHWAY annotation 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with evidence code ECO:0000269 (experimental evidence from PubMed:39043959, Nat. Chem. Biol. 2025, 'Unlocking saponin biosynthesis in soapwort'). The protein glycosylates quillaic acid, a triterpenoid aglycone, placing it squarely in secondary metabolite (saponin) biosynthesis. The sequence in the question matches the UniProt entry exactly (SHA-256 match confirmed)."
  },
  "important_caveats": [
    "The pathway annotation (C5, H3) carries ECO:0000269 (experimental evidence), strengthening the key's reliability.",
    "The CSL family nomenclature ('Cellulose Synthase-Like') is a misnomer for this particular member, which does not synthesize cellulose but glycosylates a triterpenoid; this could mislead a model toward a polysaccharide-related answer.",
    "The organism (Saponaria officinalis) is not provided in the question input, removing a major contextual clue (soapwort is famous for saponins).",
    "The sequence is a 698-aa membrane protein with no obvious sequence-level signature that uniquely distinguishes 'secondary metabolite' from 'lipid' metabolism for a plant glycosyltransferase.",
    "Options C and D are near-duplicates (both bacterial capsule pathways) and serve as easy distractors; they do not affect the core A-vs-B difficulty."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Triterpenoids (saponin aglycones) are isoprenoid-derived lipophilic molecules. A model or student reasoning broadly could classify a triterpenoid glycosyltransferase under 'lipid metabolism' (A), since terpenoids are a subclass of lipids in many textbook classifications. The UniProt annotation places it under 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (B), which is the more precise and correct classification, but the boundary between A and B is genuinely fuzzy without knowing the specific substrate context. Options C and D are clearly wrong (bacterial capsule pathways) and do not create ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0162",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1HA02 (CSL1_SAPOF, Quillaic acid 3-O-glycosyltransferase) carries the explicit PATHWAY annotation 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with evidence code ECO:0000269 (experimental evidence from PubMed:39043959, Nat. Chem. Biol. 2025, 'Unlocking saponin biosynthesis in soapwort'). The protein glycosylates quillaic acid, a triterpenoid aglycone, placing it squarely in secondary metabolite (saponin) biosynthesis. The sequence in the question matches the UniProt entry exactly (SHA-256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can partially reason: (1) the protein is clearly eukaryotic (long single-pass membrane topology, no bacterial signal peptides or capsule-specific machinery), eliminating C and D; (2) conserved GT4-family motifs (e.g., 'HxxxH', 'DxD' regions) identify it as a glycosyltransferase. However, the critical step—choosing B (secondary metabolite biosynthesis) over A (lipid metabolism)—requires knowing that the substrate is quillaic acid, a triterpenoid secondary metabolite, rather than a phospholipid or fatty-acid intermediate. Triterpenoids are broadly 'lipophilic' and derived from the isoprenoid pathway, so a model reasoning only from sequence and general biology could plausibly select A. The CSL (Cellulose Synthase-Like) family name further muddies the distinction, as it superficially evokes polysaccharide biosynthesis.",
    "missing_item_specific_fact": "The identity of the glycosyl acceptor as quillaic acid (a triterpenoid saponin aglycone) and the organism (Saponaria officinalis, a saponin-producing plant). Neither the substrate specificity nor the organism is provided in the question input; only the raw 698-aa sequence is given. Without this item-specific fact, the A-vs-B distinction cannot be resolved by general biological reasoning from sequence alone.",
    "reason": "Eliminating C and D (bacterial capsule pathways) is achievable from the eukaryotic membrane-protein architecture. However, distinguishing lipid metabolism (A) from secondary metabolite biosynthesis (B) for a plant membrane glycosyltransferase demands knowledge of the specific substrate (quillaic acid → triterpenoid → secondary metabolite). This is a protein-specific experimental fact (ECO:0000269) not inferable from sequence motifs or general pathway logic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Triterpenoids (saponin aglycones) are isoprenoid-derived lipophilic molecules. A model or student reasoning broadly could classify a triterpenoid glycosyltransferase under 'lipid metabolism' (A), since terpenoids are a subclass of lipids in many textbook classifications. The UniProt annotation places it under 'Secondary metabolite biosynthesis; terpenoid biosynthesis' (B), which is the more precise and correct classification, but the boundary between A and B is genuinely fuzzy without knowing the specific substrate context. Options C and D are clearly wrong (bacterial capsule pathways) and do not create ambiguity."
  },
  "important_caveats": [
    "The pathway annotation (C5, H3) carries ECO:0000269 (experimental evidence), strengthening the key's reliability.",
    "The CSL family nomenclature ('Cellulose Synthase-Like') is a misnomer for this particular member, which does not synthesize cellulose but glycosylates a triterpenoid; this could mislead a model toward a polysaccharide-related answer.",
    "The organism (Saponaria officinalis) is not provided in the question input, removing a major contextual clue (soapwort is famous for saponins).",
    "The sequence is a 698-aa membrane protein with no obvious sequence-level signature that uniquely distinguishes 'secondary metabolite' from 'lipid' metabolism for a plant glycosyltransferase.",
    "Options C and D are near-duplicates (both bacterial capsule pathways) and serve as easy distractors; they do not affect the core A-vs-B difficulty."
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

**Accession:** `A0AAW1HA02` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"Cellulose synthase-like protein 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoCSL1"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"2.4.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39043959","source":"PubMed"}],"value":"Quillaic acid 3-O-glycosyltransferase CSL1"}}}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1HA02.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:29.725144+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48157.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `ced1a85f4bd178ca3a21351af4130064faa92db4910f1c839491e60a08e4daf9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
ID   CSL1_SAPOF              Reviewed;         698 AA.
AC   A0AAW1HA02;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=Quillaic acid 3-O-glycosyltransferase CSL1 {ECO:0000305|PubMed:39043959};
DE            EC=2.4.1.- {ECO:0000269|PubMed:39043959};
DE   AltName: Full=Cellulose synthase-like protein 1 {ECO:0000303|PubMed:39043959};
DE            Short=SoCSL1 {ECO:0000303|PubMed:39043959};
GN   Name=CSL1 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11064433m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_12G127200 {ECO:0000312|EMBL:KAK9672824.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 18-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:WWM48157.1}
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

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1HA02?format=txt&versions=5)  
**Locator:** `lines 50-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:31.462058+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `e565ff77eec1b44dd5ee2a404680772ba99cc36e620917e40ca47a72ffd020f9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 162. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
