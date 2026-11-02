# GO_cellular_component_0017

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — cytoplasm

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATYALSQAHREQMEKSLVDSDPEIAQIMEKEIQRQRESILLIASENVTSRAVFDALGSPMSNKYSEGYPGARYYGGNQHIDAIELTCQARALKAFNLDPEKWGVNVQCLSGSPANLEVYQALMRPHDRLMGLDLPHGGHLSHGYQTPSRKISAVSTYFETFPYRVNTETGIIDYDTLEANAELYRPKCLVAGTSAYCRLIDYGRMRKIADKVGAYLIVDMAHISGLVAAGVIPSPFEYADVVTTTTHKSLRGPRGAMIFFRKGVRSTDPKTGKEIMYDLEGPINFSVFPGHQGGPHNHTITALAVALKQAATPEFRQYQEQVLKNAKALEVEFKALGHKLVSDGTDSHMVLLDLRPKGLDGARVEAVLEQINIACNKNSIPGDKSALTPCGIRIGTPAMTSRGMSEEDFKRVARYIDQVINLCKSIQADLPKEANKLKDFKAKVASGSVPEILALRKEVAEWASTYPLPV

[Multiple Choices]
A. cytoplasm
B. primosome complex
C. NF-kappaB complex
D. endosome membrane
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates the protein as cytosolic/cytoplasmic, with ECO:0000269 evidence linked to a publication. This supports choice A, though the annotation is not an independent review of the primary study.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble globular protein and lacks an evident transmembrane segment or N-terminal secretion/membrane-targeting signal. Its enzyme-like character is more compatible with a cytoplasmic protein than with an endosome membrane protein or a component of the listed specialized complexes.


**Missing item-specific fact**

> Definitive confirmation of this protein's predominant location in this organism would require protein-specific localization evidence; sequence features alone do not establish localization experimentally.


**Reason**

> The supplied sequence offers meaningful grounds to favor a soluble cytoplasmic protein over these particular alternatives. This inference does not rely on recognizing the exact sequence or recalling its database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the sequence features favor cytoplasm; the other options describe a membrane or specific complexes for which the sequence provides no evident support.


### Important caveats

- The reviewer-only annotation applies to an exact sequence match, but was not available to the evaluated model.
- The cited experimental evidence code is reported in the database annotation; the underlying study was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble globular protein and lacks an evident transmembrane segment or N-terminal secretion/membrane-targeting signal. Its enzyme-like character is more compatible with a cytoplasmic protein than with an endosome membrane protein or a component of the listed specialized complexes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Definitive confirmation of this protein's predominant location in this organism would require protein-specific localization evidence; sequence features alone do not establish localization experimentally.",
    "reason": "The supplied sequence offers meaningful grounds to favor a soluble cytoplasmic protein over these particular alternatives. This inference does not rely on recognizing the exact sequence or recalling its database annotation."
  },
  "case_id": "GO_cellular_component_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as cytosolic/cytoplasmic, with ECO:0000269 evidence linked to a publication. This supports choice A, though the annotation is not an independent review of the primary study."
  },
  "important_caveats": [
    "The reviewer-only annotation applies to an exact sequence match, but was not available to the evaluated model.",
    "The cited experimental evidence code is reported in the database annotation; the underlying study was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence features favor cytoplasm; the other options describe a membrane or specific complexes for which the sequence provides no evident support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as cytosolic/cytoplasmic, with ECO:0000269 evidence linked to a publication. This supports choice A, though the annotation is not an independent review of the primary study.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble globular protein and lacks an evident transmembrane segment or N-terminal secretion/membrane-targeting signal. Its enzyme-like character is more compatible with a cytoplasmic protein than with an endosome membrane protein or a component of the listed specialized complexes.",
    "missing_item_specific_fact": "Definitive confirmation of this protein's predominant location in this organism would require protein-specific localization evidence; sequence features alone do not establish localization experimentally.",
    "reason": "The supplied sequence offers meaningful grounds to favor a soluble cytoplasmic protein over these particular alternatives. This inference does not rely on recognizing the exact sequence or recalling its database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence features favor cytoplasm; the other options describe a membrane or specific complexes for which the sequence provides no evident support."
  },
  "important_caveats": [
    "The reviewer-only annotation applies to an exact sequence match, but was not available to the evaluated model.",
    "The cited experimental evidence code is reported in the database annotation; the underlying study was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WXF4 (GLYC_ASPFU) is annotated as 'Serine hydroxymethyltransferase, cytosolic' with experimental subcellular localization evidence (ECO:0000269, direct assay from PubMed:39825596) stating 'Cytoplasm, cytosol.' The GO annotation GO:0005829 (cytosol) is part_of GO:0005737 (cytoplasm), making 'cytoplasm' the correct parent-level answer. A secondary GO:0005739 (mitochondrion) annotation exists but carries only IBA:GO_Central (computational inference from GO_Central), not experimental evidence. The experimental data unambiguously support cytoplasmic localization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark PLP-binding motif 'TTTTHK' and the overall fold of serine hydroxymethyltransferase (SHMT), a soluble pyridoxal-5'-phosphate-dependent metabolic enzyme. None of the distractors are compatible: (B) primosome complex requires helicase and primase domains for DNA replication, absent here; (C) NF-kappaB complex requires Rel homology domains and is metazoan-specific, not found in Aspergillus; (D) endosome membrane requires transmembrane segments and vesicular targeting signals, absent from this soluble enzyme. A soluble PLP-dependent enzyme lacking transmembrane domains, DNA-binding motifs, or organelle-targeting sequences defaults to the cytoplasm. The N-terminus contains multiple acidic residues (D, E) inconsistent with a strong mitochondrial targeting peptide, further supporting cytosolic/cytoplasmic residence.


**Missing item-specific fact**

> None critical. The distinction among the four options is achievable through general knowledge of PLP-enzyme biochemistry, absence of membrane/replication/transcription-factor domains, and fungal biology (NF-kappaB is metazoan-only).


**Reason**

> A knowledgeable model can identify the SHMT fold from the TTTTHK PLP-binding motif and domain architecture, then eliminate all three non-cytoplasmic options by domain-composition reasoning (no TM helices, no helicase/primase, no Rel homology domain, NF-kappaB absent in fungi). The correct answer follows from the protein being a soluble metabolic enzyme without targeting signals.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only 'cytoplasm' is compatible with a soluble PLP-dependent enzyme. Primosome (DNA replication), NF-kappaB (metazoan transcription factor complex), and endosome membrane (integral membrane protein) are all categorically incompatible with the identified enzyme class. No ambiguity exists.


### Important caveats

- The UniProt entry also carries GO:0005739 (mitochondrion) with IBA:GO_Central evidence, a computational inference. This is not an option here, but it indicates SHMT may have dual localization; the experimental evidence (ECO:0000269) supports cytoplasm/cytosol as the primary location.
- The reviewer-only accession (Q4WXF4) was inferred from dataset metadata not available to the evaluated model; the model must work from sequence alone.
- The GO term 'cytoplasm' (GO:0005737) is the parent of 'cytosol' (GO:0005829); the UniProt annotation specifies 'Cytoplasm, cytosol,' so the answer 'cytoplasm' is consistent at the parent level.
- The mitochondrial SHMT isoform (SHMT2) is not among the options, so the cytosolic-vs-mitochondrial distinction is not actually tested by this question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark PLP-binding motif 'TTTTHK' and the overall fold of serine hydroxymethyltransferase (SHMT), a soluble pyridoxal-5'-phosphate-dependent metabolic enzyme. None of the distractors are compatible: (B) primosome complex requires helicase and primase domains for DNA replication, absent here; (C) NF-kappaB complex requires Rel homology domains and is metazoan-specific, not found in Aspergillus; (D) endosome membrane requires transmembrane segments and vesicular targeting signals, absent from this soluble enzyme. A soluble PLP-dependent enzyme lacking transmembrane domains, DNA-binding motifs, or organelle-targeting sequences defaults to the cytoplasm. The N-terminus contains multiple acidic residues (D, E) inconsistent with a strong mitochondrial targeting peptide, further supporting cytosolic/cytoplasmic residence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The distinction among the four options is achievable through general knowledge of PLP-enzyme biochemistry, absence of membrane/replication/transcription-factor domains, and fungal biology (NF-kappaB is metazoan-only).",
    "reason": "A knowledgeable model can identify the SHMT fold from the TTTTHK PLP-binding motif and domain architecture, then eliminate all three non-cytoplasmic options by domain-composition reasoning (no TM helices, no helicase/primase, no Rel homology domain, NF-kappaB absent in fungi). The correct answer follows from the protein being a soluble metabolic enzyme without targeting signals."
  },
  "case_id": "GO_cellular_component_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "GO1",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WXF4 (GLYC_ASPFU) is annotated as 'Serine hydroxymethyltransferase, cytosolic' with experimental subcellular localization evidence (ECO:0000269, direct assay from PubMed:39825596) stating 'Cytoplasm, cytosol.' The GO annotation GO:0005829 (cytosol) is part_of GO:0005737 (cytoplasm), making 'cytoplasm' the correct parent-level answer. A secondary GO:0005739 (mitochondrion) annotation exists but carries only IBA:GO_Central (computational inference from GO_Central), not experimental evidence. The experimental data unambiguously support cytoplasmic localization."
  },
  "important_caveats": [
    "The UniProt entry also carries GO:0005739 (mitochondrion) with IBA:GO_Central evidence, a computational inference. This is not an option here, but it indicates SHMT may have dual localization; the experimental evidence (ECO:0000269) supports cytoplasm/cytosol as the primary location.",
    "The reviewer-only accession (Q4WXF4) was inferred from dataset metadata not available to the evaluated model; the model must work from sequence alone.",
    "The GO term 'cytoplasm' (GO:0005737) is the parent of 'cytosol' (GO:0005829); the UniProt annotation specifies 'Cytoplasm, cytosol,' so the answer 'cytoplasm' is consistent at the parent level.",
    "The mitochondrial SHMT isoform (SHMT2) is not among the options, so the cytosolic-vs-mitochondrial distinction is not actually tested by this question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'cytoplasm' is compatible with a soluble PLP-dependent enzyme. Primosome (DNA replication), NF-kappaB (metazoan transcription factor complex), and endosome membrane (integral membrane protein) are all categorically incompatible with the identified enzyme class. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WXF4 (GLYC_ASPFU) is annotated as 'Serine hydroxymethyltransferase, cytosolic' with experimental subcellular localization evidence (ECO:0000269, direct assay from PubMed:39825596) stating 'Cytoplasm, cytosol.' The GO annotation GO:0005829 (cytosol) is part_of GO:0005737 (cytoplasm), making 'cytoplasm' the correct parent-level answer. A secondary GO:0005739 (mitochondrion) annotation exists but carries only IBA:GO_Central (computational inference from GO_Central), not experimental evidence. The experimental data unambiguously support cytoplasmic localization.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5", "GO1", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark PLP-binding motif 'TTTTHK' and the overall fold of serine hydroxymethyltransferase (SHMT), a soluble pyridoxal-5'-phosphate-dependent metabolic enzyme. None of the distractors are compatible: (B) primosome complex requires helicase and primase domains for DNA replication, absent here; (C) NF-kappaB complex requires Rel homology domains and is metazoan-specific, not found in Aspergillus; (D) endosome membrane requires transmembrane segments and vesicular targeting signals, absent from this soluble enzyme. A soluble PLP-dependent enzyme lacking transmembrane domains, DNA-binding motifs, or organelle-targeting sequences defaults to the cytoplasm. The N-terminus contains multiple acidic residues (D, E) inconsistent with a strong mitochondrial targeting peptide, further supporting cytosolic/cytoplasmic residence.",
    "missing_item_specific_fact": "None critical. The distinction among the four options is achievable through general knowledge of PLP-enzyme biochemistry, absence of membrane/replication/transcription-factor domains, and fungal biology (NF-kappaB is metazoan-only).",
    "reason": "A knowledgeable model can identify the SHMT fold from the TTTTHK PLP-binding motif and domain architecture, then eliminate all three non-cytoplasmic options by domain-composition reasoning (no TM helices, no helicase/primase, no Rel homology domain, NF-kappaB absent in fungi). The correct answer follows from the protein being a soluble metabolic enzyme without targeting signals."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'cytoplasm' is compatible with a soluble PLP-dependent enzyme. Primosome (DNA replication), NF-kappaB (metazoan transcription factor complex), and endosome membrane (integral membrane protein) are all categorically incompatible with the identified enzyme class. No ambiguity exists."
  },
  "important_caveats": [
    "The UniProt entry also carries GO:0005739 (mitochondrion) with IBA:GO_Central evidence, a computational inference. This is not an option here, but it indicates SHMT may have dual localization; the experimental evidence (ECO:0000269) supports cytoplasm/cytosol as the primary location.",
    "The reviewer-only accession (Q4WXF4) was inferred from dataset metadata not available to the evaluated model; the model must work from sequence alone.",
    "The GO term 'cytoplasm' (GO:0005737) is the parent of 'cytosol' (GO:0005829); the UniProt annotation specifies 'Cytoplasm, cytosol,' so the answer 'cytoplasm' is consistent at the parent level.",
    "The mitochondrial SHMT isoform (SHMT2) is not among the options, so the cytosolic-vs-mitochondrial distinction is not actually tested by this question."
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

**Accession:** `Q4WXF4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P34896","source":"UniProtKB"}],"value":"2.1.2.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39825596","source":"PubMed"}],"value":"Serine hydroxymethyltransferase, cytosolic"}}}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39825596","source":"PubMed"}],"id":"SL-0091","value":"Cytoplasm, cytosol"}}]}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"citation":{"authors":["Alharthi R.","Sueiro-Olivares M.","Storer I.","Bin Shuraym H.","Scott J.","Al-Shidhani R.","Fortune-Grant R.","Bignell E.","Tabernero L.","Bromley M.","Zhao C.","Amich J."],"citationCrossReferences":[{"database":"PubMed","id":"39825596"},{"database":"DOI","id":"10.1080/21505594.2024.2449075"}],"citationType":"journal article","firstPage":"2449075","id":"39825596","journal":"Virulence","lastPage":"2449075","publicationDate":"2025","title":"The sulfur-related metabolic status of Aspergillus fumigatus during infection reveals cytosolic serine hydroxymethyltransferase as a promising antifungal target.","volume":"16"},"referenceNumber":2,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","INDUCTION","DISRUPTION PHENOTYPE","BIOTECHNOLOGY"]}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
ID   GLYC_ASPFU              Reviewed;         471 AA.
AC   Q4WXF4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2005, sequence version 1.
DT   28-JAN-2026, entry version 122.
DE   RecName: Full=Serine hydroxymethyltransferase, cytosolic {ECO:0000303|PubMed:39825596};
DE            EC=2.1.2.1 {ECO:0000250|UniProtKB:P34896};
GN   Name=shmB {ECO:0000303|PubMed:39825596}; ORFNames=AFUA_3G09320;
OS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /
OS   Af293) (Neosartorya fumigata).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Fumigati.
OX   NCBI_TaxID=330879;
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 40-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
RN   [2]
RP   FUNCTION, SUBCELLULAR LOCATION, INDUCTION, DISRUPTION PHENOTYPE, AND
RP   BIOTECHNOLOGY.
RX   PubMed=39825596; DOI=10.1080/21505594.2024.2449075;
RA   Alharthi R., Sueiro-Olivares M., Storer I., Bin Shuraym H., Scott J.,
RA   Al-Shidhani R., Fortune-Grant R., Bignell E., Tabernero L., Bromley M.,
RA   Zhao C., Amich J.;
RT   "The sulfur-related metabolic status of Aspergillus fumigatus during
RT   infection reveals cytosolic serine hydroxymethyltransferase as a promising
RT   antifungal target.";
RL   Virulence 16:2449075-2449075(2025).
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 66-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:39825596}.
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 98-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; IEA:UniProtKB-SubCell.
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 99-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
DR   GO; GO:0005739; C:mitochondrion; IBA:GO_Central.
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58957-58974`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005737
name: cytoplasm
namespace: cellular_component
def: "The contents of a cell excluding the plasma membrane and nucleus, but including other subcellular structures." [ISBN:0198547684]
subset: goslim_candida
subset: goslim_chembl
subset: goslim_metagenomics
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
xref: Wikipedia:Cytoplasm
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0005622 ! intracellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59936-59953`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005829
name: cytosol
namespace: cellular_component
def: "The part of the cytoplasm that does not contain organelles but which does contain other particulate matter, such as protein complexes." [GOC:hjd, GOC:jl]
subset: goslim_agr
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_plant
xref: NIF_Subcellular:sao101633890
xref: Wikipedia:Cytosol
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
