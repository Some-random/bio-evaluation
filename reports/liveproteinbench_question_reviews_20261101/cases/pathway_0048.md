# pathway_0048

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGTKELHIVMYPWLAFGHFIPYLHLSNKLAQKGHKITFLLPHRAKLQLDSQNLYPSLITLVPITVPQVDTLPLGAESTADIPLSQHGDLSIAMDRTRPEIESILSKLDPKPDLIFFDMAQWVPVIASKLGIKSVSYNIVCAISLDLVRDWYKKDDGSNVPSWTLKHDKSSHFGENISILERALIALGTPDAIGIRSCREIEGEYCDSIAERFKKPVLLSGTTLPEPSDDPLDPKWVKWLGKFEEGSVIFCCLGSQHVLDKPQLQELALGLEMTGLPFFLAIKPPLGYATLDEVLPEGFSERVRDRGVAHGGWVQQPQMLAHPSVGCFLCHCGSSSMWEALVSDTQLVLFPQIPDQALNAVLMADKLKVGVKVEREDDGGVSKEVWSRAIKSVMDKESEIAAEVKKNHTKWRDMLINEEFVNGYIDSFIKDLQDLVEK

[Multiple Choices]
A. LPS O-antigen biosynthesis. .
B. Alkaloid biosynthesis. .
C. Secondary metabolite biosynthesis
D. Membrane lipid metabolism. .
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

> The exact sequence matches the UniProt entry for UDP-glucosyl transferase 79L3 from Saponaria officinalis. Its pathway annotation is “Secondary metabolite biosynthesis; terpenoid biosynthesis,” with ECO:0000269 evidence linked to a cited publication. This supports choice C, while the underlying study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest a plant UDP-dependent glycosyltransferase, and such enzymes can modify specialized metabolites. That general inference does not establish this enzyme’s substrate or distinguish its terpenoid/saponin role from other possible pathways.


**Missing item-specific fact**

> The protein-specific functional assignment that this enzyme participates in terpenoid/saponin secondary-metabolite biosynthesis.


**Reason**

> The exact pathway assignment depends on a protein-specific annotation or experimental finding absent from the sequence and choices. Recognizing the sequence’s database entry would be lookup, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence specifically assigns the enzyme to secondary metabolite and terpenoid biosynthesis; it does not assign it to alkaloid biosynthesis, LPS O-antigen biosynthesis, or membrane lipid metabolism.


### Important caveats

- The sequence match is exact, and the historical UniProt entry available by the stated cutoff also gives the pathway annotation.
- The pathway evidence is database annotation linked to a publication; the publication and its experiments were not independently validated here.
- The organism and functional annotation were reviewer-only evidence, not information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest a plant UDP-dependent glycosyltransferase, and such enzymes can modify specialized metabolites. That general inference does not establish this enzyme’s substrate or distinguish its terpenoid/saponin role from other possible pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment that this enzyme participates in terpenoid/saponin secondary-metabolite biosynthesis.",
    "reason": "The exact pathway assignment depends on a protein-specific annotation or experimental finding absent from the sequence and choices. Recognizing the sequence’s database entry would be lookup, not reasoning from the supplied input."
  },
  "case_id": "pathway_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for UDP-glucosyl transferase 79L3 from Saponaria officinalis. Its pathway annotation is “Secondary metabolite biosynthesis; terpenoid biosynthesis,” with ECO:0000269 evidence linked to a cited publication. This supports choice C, while the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match is exact, and the historical UniProt entry available by the stated cutoff also gives the pathway annotation.",
    "The pathway evidence is database annotation linked to a publication; the publication and its experiments were not independently validated here.",
    "The organism and functional annotation were reviewer-only evidence, not information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence specifically assigns the enzyme to secondary metabolite and terpenoid biosynthesis; it does not assign it to alkaloid biosynthesis, LPS O-antigen biosynthesis, or membrane lipid metabolism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for UDP-glucosyl transferase 79L3 from Saponaria officinalis. Its pathway annotation is “Secondary metabolite biosynthesis; terpenoid biosynthesis,” with ECO:0000269 evidence linked to a cited publication. This supports choice C, while the underlying study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest a plant UDP-dependent glycosyltransferase, and such enzymes can modify specialized metabolites. That general inference does not establish this enzyme’s substrate or distinguish its terpenoid/saponin role from other possible pathways.",
    "missing_item_specific_fact": "The protein-specific functional assignment that this enzyme participates in terpenoid/saponin secondary-metabolite biosynthesis.",
    "reason": "The exact pathway assignment depends on a protein-specific annotation or experimental finding absent from the sequence and choices. Recognizing the sequence’s database entry would be lookup, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence specifically assigns the enzyme to secondary metabolite and terpenoid biosynthesis; it does not assign it to alkaloid biosynthesis, LPS O-antigen biosynthesis, or membrane lipid metabolism."
  },
  "important_caveats": [
    "The sequence match is exact, and the historical UniProt entry available by the stated cutoff also gives the pathway annotation.",
    "The pathway evidence is database annotation linked to a publication; the publication and its experiments were not independently validated here.",
    "The organism and functional annotation were reviewer-only evidence, not information supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for A0AAW1MQS1 (SoUGT79L3 from Saponaria officinalis) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269|PubMed:39043959). The protein is a UDP-glucosyl transferase (EC 2.4.2.-) that glycosylates saponin intermediates (triterpenoids), which are secondary metabolites. The sequence matches exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains features of a plant UDP-glycosyltransferase, including the PSPG (Plant Secondary Product Glycosyltransferase) motif region (e.g., 'HGGWVQQPQMLAHPSVGCFLCHCGSSSMWEALVSDTQLVLFPQIPDQALNAVLMADKLKVGVKVEREDDGGVSKEVWSRAIKSVMDKESEIAAEVKKNHTKWRDMLINEEFVNGYIDSFIKDLQDLVEK'). The PSPG motif is by definition associated with glycosylation of plant secondary products (saponins, flavonoids, terpenoids, etc.), providing a general biological argument for 'Secondary metabolite biosynthesis' (C) over 'Membrane lipid metabolism' (D). Option A (LPS O-antigen) is eliminable as a bacterial pathway incompatible with a eukaryotic plant UGT. Option B (Alkaloid biosynthesis) is a narrower subset; UGTs are more broadly associated with diverse secondary metabolites.


**Missing item-specific fact**

> The specific substrate of this UGT (saponin/triterpenoid intermediates vs. sterols or other acceptors) is not determinable from sequence alone. Distinguishing C from D with certainty requires knowing the enzyme's actual acceptor substrate, which is an experimentally determined property (confirmed in PubMed:39043959).


**Reason**

> The PSPG motif and UGT fold provide a defensible general biological argument favoring secondary metabolite biosynthesis over membrane lipid metabolism for a plant UGT. However, the precise distinction between C and D ultimately depends on substrate specificity knowledge. The general argument is meaningful but not fully decisive for this particular enzyme.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> While the PSPG motif strongly suggests secondary metabolite involvement, some plant UGTs with PSPG motifs do glycosylate sterols and other membrane lipid components. Without knowing the specific acceptor substrate, a knowledgeable student could argue D is plausible. However, the PSPG motif's literal naming ('Secondary Product') and the predominance of 79-family UGTs in secondary metabolism make C the stronger inference.


### Important caveats

- The UniProt pathway annotation carries experimental evidence (ECO:0000269) from PubMed:39043959 (Nat. Chem. Biol. 2025), confirming the enzyme's role in saponin (triterpenoid) biosynthesis.
- The organism (Saponaria officinalis) is not stated in the question; the model must infer plant origin from sequence features alone.
- The entry was first public in June 2025; depending on the benchmark construction date, this protein may have been very recently annotated.
- The PSPG motif argument is a general heuristic; it does not guarantee that every PSPG-containing UGT acts on secondary metabolites rather than lipids.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features of a plant UDP-glycosyltransferase, including the PSPG (Plant Secondary Product Glycosyltransferase) motif region (e.g., 'HGGWVQQPQMLAHPSVGCFLCHCGSSSMWEALVSDTQLVLFPQIPDQALNAVLMADKLKVGVKVEREDDGGVSKEVWSRAIKSVMDKESEIAAEVKKNHTKWRDMLINEEFVNGYIDSFIKDLQDLVEK'). The PSPG motif is by definition associated with glycosylation of plant secondary products (saponins, flavonoids, terpenoids, etc.), providing a general biological argument for 'Secondary metabolite biosynthesis' (C) over 'Membrane lipid metabolism' (D). Option A (LPS O-antigen) is eliminable as a bacterial pathway incompatible with a eukaryotic plant UGT. Option B (Alkaloid biosynthesis) is a narrower subset; UGTs are more broadly associated with diverse secondary metabolites.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate of this UGT (saponin/triterpenoid intermediates vs. sterols or other acceptors) is not determinable from sequence alone. Distinguishing C from D with certainty requires knowing the enzyme's actual acceptor substrate, which is an experimentally determined property (confirmed in PubMed:39043959).",
    "reason": "The PSPG motif and UGT fold provide a defensible general biological argument favoring secondary metabolite biosynthesis over membrane lipid metabolism for a plant UGT. However, the precise distinction between C and D ultimately depends on substrate specificity knowledge. The general argument is meaningful but not fully decisive for this particular enzyme."
  },
  "case_id": "pathway_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for A0AAW1MQS1 (SoUGT79L3 from Saponaria officinalis) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269|PubMed:39043959). The protein is a UDP-glucosyl transferase (EC 2.4.2.-) that glycosylates saponin intermediates (triterpenoids), which are secondary metabolites. The sequence matches exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries experimental evidence (ECO:0000269) from PubMed:39043959 (Nat. Chem. Biol. 2025), confirming the enzyme's role in saponin (triterpenoid) biosynthesis.",
    "The organism (Saponaria officinalis) is not stated in the question; the model must infer plant origin from sequence features alone.",
    "The entry was first public in June 2025; depending on the benchmark construction date, this protein may have been very recently annotated.",
    "The PSPG motif argument is a general heuristic; it does not guarantee that every PSPG-containing UGT acts on secondary metabolites rather than lipids."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "While the PSPG motif strongly suggests secondary metabolite involvement, some plant UGTs with PSPG motifs do glycosylate sterols and other membrane lipid components. Without knowing the specific acceptor substrate, a knowledgeable student could argue D is plausible. However, the PSPG motif's literal naming ('Secondary Product') and the predominance of 79-family UGTs in secondary metabolism make C the stronger inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for A0AAW1MQS1 (SoUGT79L3 from Saponaria officinalis) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269|PubMed:39043959). The protein is a UDP-glucosyl transferase (EC 2.4.2.-) that glycosylates saponin intermediates (triterpenoids), which are secondary metabolites. The sequence matches exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains features of a plant UDP-glycosyltransferase, including the PSPG (Plant Secondary Product Glycosyltransferase) motif region (e.g., 'HGGWVQQPQMLAHPSVGCFLCHCGSSSMWEALVSDTQLVLFPQIPDQALNAVLMADKLKVGVKVEREDDGGVSKEVWSRAIKSVMDKESEIAAEVKKNHTKWRDMLINEEFVNGYIDSFIKDLQDLVEK'). The PSPG motif is by definition associated with glycosylation of plant secondary products (saponins, flavonoids, terpenoids, etc.), providing a general biological argument for 'Secondary metabolite biosynthesis' (C) over 'Membrane lipid metabolism' (D). Option A (LPS O-antigen) is eliminable as a bacterial pathway incompatible with a eukaryotic plant UGT. Option B (Alkaloid biosynthesis) is a narrower subset; UGTs are more broadly associated with diverse secondary metabolites.",
    "missing_item_specific_fact": "The specific substrate of this UGT (saponin/triterpenoid intermediates vs. sterols or other acceptors) is not determinable from sequence alone. Distinguishing C from D with certainty requires knowing the enzyme's actual acceptor substrate, which is an experimentally determined property (confirmed in PubMed:39043959).",
    "reason": "The PSPG motif and UGT fold provide a defensible general biological argument favoring secondary metabolite biosynthesis over membrane lipid metabolism for a plant UGT. However, the precise distinction between C and D ultimately depends on substrate specificity knowledge. The general argument is meaningful but not fully decisive for this particular enzyme."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "While the PSPG motif strongly suggests secondary metabolite involvement, some plant UGTs with PSPG motifs do glycosylate sterols and other membrane lipid components. Without knowing the specific acceptor substrate, a knowledgeable student could argue D is plausible. However, the PSPG motif's literal naming ('Secondary Product') and the predominance of 79-family UGTs in secondary metabolism make C the stronger inference."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries experimental evidence (ECO:0000269) from PubMed:39043959 (Nat. Chem. Biol. 2025), confirming the enzyme's role in saponin (triterpenoid) biosynthesis.",
    "The organism (Saponaria officinalis) is not stated in the question; the model must infer plant origin from sequence features alone.",
    "The entry was first public in June 2025; depending on the benchmark construction date, this protein may have been very recently annotated.",
    "The PSPG motif argument is a general heuristic; it does not guarantee that every PSPG-containing UGT acts on secondary metabolites rather than lipids."
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

**Accession:** `A0AAW1MQS1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 5. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:42.921794+00:00.  

```json
"A0AAW1MQS1"
```

Source SHA-256: `38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:42.921794+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"2.4.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"UDP-glucosyl transferase 79L3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39043959","source":"PubMed"}],"value":"SoUGT79L3"}]}}
```

Source SHA-256: `38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:42.921794+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39043959","source":"PubMed"}],"value":"Secondary metabolite biosynthesis; terpenoid biosynthesis"}]}
```

Source SHA-256: `38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1MQS1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:42.921794+00:00.  

```json
{"citation":{"authors":["Jo S.","El-Demerdash A.","Owen C.","Srivastava V.","Wu D.","Kikuchi S.","Reed J.","Hodgson H.","Harkess A.","Shu S.","Plott C.","Jenkins J.","Williams M.","Boston L.-B.","Lacchini E.","Qu T.","Goossens A.","Grimwood J.","Schmutz J.","Leebens-Mack J.","Osbourn A."],"citationCrossReferences":[{"database":"PubMed","id":"39043959"},{"database":"DOI","id":"10.1038/s41589-024-01681-7"}],"citationType":"journal article","firstPage":"215","id":"39043959","journal":"Nat. Chem. Biol.","lastPage":"226","publicationDate":"2025","title":"Unlocking saponin biosynthesis in soapwort.","volume":"21"},"evidences":[{"evidenceCode":"ECO:0000312","id":"WWM48150.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","TISSUE SPECIFICITY","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `38e19d62d1e2fd0bdb2dcb0078a06ec483bdc0582d78b80c6fe365d966217911`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:44.890470+00:00.  

```text
ID   GT793_SAPOF             Reviewed;         437 AA.
AC   A0AAW1MQS1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   27-NOV-2024, sequence version 1.
DT   28-JAN-2026, entry version 5.
DE   RecName: Full=UDP-glucosyl transferase 79L3 {ECO:0000303|PubMed:39043959};
DE            Short=SoUGT79L3 {ECO:0000303|PubMed:39043959};
DE            EC=2.4.2.- {ECO:0000269|PubMed:39043959};
GN   Name=UGT79L3 {ECO:0000303|PubMed:39043959};
GN   Synonyms=Saoffv11006237m {ECO:0000303|PubMed:39043959};
GN   ORFNames=RND81_02G054000 {ECO:0000312|EMBL:KAK9748391.1};
OS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.
OX   NCBI_TaxID=3572;
```

Source SHA-256: `c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1MQS1?format=txt&versions=5)  
**Locator:** `lines 51-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 5 / 1.  
**Retrieved:** 2026-11-02T04:26:44.890470+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.
CC       {ECO:0000269|PubMed:39043959}.
```

Source SHA-256: `c9be8c78f74c494bf89b7deeee4376bf5b587b49421d7bfa1cdf2a6c1852ed8b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
