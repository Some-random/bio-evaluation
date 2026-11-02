# GO_cellular_component_0105

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — chloroplast

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKSLVAHFSTPLITARLVPRCIIHRASISAVSFSTVRRRFSPLTMASAAQSSSQAVSYGSGNSDTDVFKLIQAHEEKAARLSPVEEIRTVLNGSICGMLSTFSQKYEGYPSGSMVDFACDADGSPILAVSSLAVHTKDLLANPKCSLLIARDPEDRTGLRITLHGDAVLVSEKDQAAVRSAYLAKHPKAFWVDFGDFSFMRIEPKVVRYVSGVATAFLGSGEFSKEEYQAAKVDPIAQYAKPVTSHMNKDHEEDTKAIVHNITSIPVESALMLDLDSLGFNVKATLQGNTFKLRVPFPRRAQDRKDVKTLIVEMLQAAKSN

[Multiple Choices]
A. inclusion body
B. caveola
C. chloroplast
D. virion component
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

> The reviewer-only record matches the supplied sequence and annotates the protein to chloroplast; the GO annotation is IDA, and the subcellular-location annotation cites experimental evidence as well as a computational annotation. This supports C, while not establishing what source snapshot the author used.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus has a long stretch enriched in Ser/Thr and basic residues, with no acidic residues in the initial region, consistent with a chloroplast transit peptide. That offers a meaningful sequence-based reason to favor chloroplast over the listed alternatives.


**Missing item-specific fact**

> A direct experimental localization result for this particular protein is not provided in the question; such evidence would confirm the predicted compartment.


**Reason**

> The sequence contains a plausible targeting signal that distinguishes chloroplast as a biologically defensible choice. The reviewer-only annotation provides separate, sequence-matched support for the key, but is not needed to identify the sequence-based argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, chloroplast is meaningfully favored by the N-terminal targeting-region features; the other options do not have comparable support from the supplied sequence.


### Important caveats

- The database record matches the supplied sequence, but the author's actual source snapshot is unknown.
- The reviewer-only record includes both computational and experimental annotation evidence; the sequence-based inference alone is predictive, not direct experimental proof.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus has a long stretch enriched in Ser/Thr and basic residues, with no acidic residues in the initial region, consistent with a chloroplast transit peptide. That offers a meaningful sequence-based reason to favor chloroplast over the listed alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "A direct experimental localization result for this particular protein is not provided in the question; such evidence would confirm the predicted compartment.",
    "reason": "The sequence contains a plausible targeting signal that distinguishes chloroplast as a biologically defensible choice. The reviewer-only annotation provides separate, sequence-matched support for the key, but is not needed to identify the sequence-based argument."
  },
  "case_id": "GO_cellular_component_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only record matches the supplied sequence and annotates the protein to chloroplast; the GO annotation is IDA, and the subcellular-location annotation cites experimental evidence as well as a computational annotation. This supports C, while not establishing what source snapshot the author used."
  },
  "important_caveats": [
    "The database record matches the supplied sequence, but the author's actual source snapshot is unknown.",
    "The reviewer-only record includes both computational and experimental annotation evidence; the sequence-based inference alone is predictive, not direct experimental proof."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, chloroplast is meaningfully favored by the N-terminal targeting-region features; the other options do not have comparable support from the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only record matches the supplied sequence and annotates the protein to chloroplast; the GO annotation is IDA, and the subcellular-location annotation cites experimental evidence as well as a computational annotation. This supports C, while not establishing what source snapshot the author used.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a long stretch enriched in Ser/Thr and basic residues, with no acidic residues in the initial region, consistent with a chloroplast transit peptide. That offers a meaningful sequence-based reason to favor chloroplast over the listed alternatives.",
    "missing_item_specific_fact": "A direct experimental localization result for this particular protein is not provided in the question; such evidence would confirm the predicted compartment.",
    "reason": "The sequence contains a plausible targeting signal that distinguishes chloroplast as a biologically defensible choice. The reviewer-only annotation provides separate, sequence-matched support for the key, but is not needed to identify the sequence-based argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, chloroplast is meaningfully favored by the N-terminal targeting-region features; the other options do not have comparable support from the supplied sequence."
  },
  "important_caveats": [
    "The database record matches the supplied sequence, but the author's actual source snapshot is unknown.",
    "The reviewer-only record includes both computational and experimental annotation evidence; the sequence-based inference alone is predictive, not direct experimental proof."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8LDU1 (HOZ_ARATH) from Arabidopsis thaliana is annotated as 'Non-canonical heme oxygenase HOZ, chloroplastic' with subcellular location 'Plastid, chloroplast' supported by both computational prediction (ECO:0000255) and experimental evidence (ECO:0000269|PubMed:33284325, IDA:TAIR). The GO annotation GO:0009507 (chloroplast) carries an IDA evidence code indicating direct experimental assay. X-ray crystallography (PDB 6M09/6M0A) confirmed structure and subcellular location. The sequence is flagged as 'Precursor,' consistent with a cleavable chloroplast transit peptide. The sequence matches exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three of four options can be eliminated by general biological reasoning: (1) Caveola is an animal-specific plasma membrane invagination requiring transmembrane domains and caveolin-binding motifs—this protein lacks any predicted TM segments. (2) Virion component requires viral origin—this protein shows no viral structural protein characteristics (no capsid-like β-barrel symmetry, no viral packaging motifs). (3) Inclusion body is an aggregation artifact of misfolded overexpressed proteins, not a native functional compartment for a properly annotated enzyme. Positive identification: The N-terminal ~50 residues (MKSLVAHFSTPLITARLVPRCIIHRASISAVSFSTVRRRFSPLTMASAAQSSSQAVSYGSGNSDTDVFKLIQAHEEK) display hallmarks of a chloroplast transit peptide—enrichment in Ser, Thr, and Arg with absence of acidic residues in the proximal region, and the protein is flagged as a 'Precursor' implying a cleavable targeting signal. Combined with the heme-oxygenase-like catalytic domain architecture (known to exist in plant chloroplasts), chloroplast is the most defensible answer.


**Missing item-specific fact**

> None critical. Organism identity (Arabidopsis thaliana) is not stated in the prompt, but the transit peptide features and elimination logic allow reasoning to the answer without it.


**Reason**

> The elimination of three implausible options (animal-specific structure, viral component, aggregation artifact) combined with positive recognition of N-terminal transit-peptide-like features (S/T/R-rich, no acidic residues, precursor flag implied by sequence architecture) provides a concrete biological argument distinguishable from the sequence alone. The transit peptide recognition is not trivially obvious but is a standard bioinformatics inference within the scope of general molecular biology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different biological categories (aggregation artifact, animal membrane structure, plant organelle, viral component). For a native, properly-folded, non-viral protein without transmembrane domains, only chloroplast is biologically plausible. No other option is defensible.


### Important caveats

- The organism (Arabidopsis thaliana) is not stated in the model input; the model must infer plant origin from transit peptide features or rely on elimination logic.
- Transit peptide recognition from sequence alone is heuristic and not always unambiguous; here it is moderately clear but not a textbook-perfect example.
- The IDA:TAIR evidence code confirms experimental validation of chloroplast localization, strengthening the key beyond mere computational annotation.
- The GO term 'extracellular region' (GO:0005576, ISM:TAIR) also appears in the annotation (C7), but this is an inferred-by-sequence-match annotation and does not conflict with the primary chloroplast assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three of four options can be eliminated by general biological reasoning: (1) Caveola is an animal-specific plasma membrane invagination requiring transmembrane domains and caveolin-binding motifs—this protein lacks any predicted TM segments. (2) Virion component requires viral origin—this protein shows no viral structural protein characteristics (no capsid-like β-barrel symmetry, no viral packaging motifs). (3) Inclusion body is an aggregation artifact of misfolded overexpressed proteins, not a native functional compartment for a properly annotated enzyme. Positive identification: The N-terminal ~50 residues (MKSLVAHFSTPLITARLVPRCIIHRASISAVSFSTVRRRFSPLTMASAAQSSSQAVSYGSGNSDTDVFKLIQAHEEK) display hallmarks of a chloroplast transit peptide—enrichment in Ser, Thr, and Arg with absence of acidic residues in the proximal region, and the protein is flagged as a 'Precursor' implying a cleavable targeting signal. Combined with the heme-oxygenase-like catalytic domain architecture (known to exist in plant chloroplasts), chloroplast is the most defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Organism identity (Arabidopsis thaliana) is not stated in the prompt, but the transit peptide features and elimination logic allow reasoning to the answer without it.",
    "reason": "The elimination of three implausible options (animal-specific structure, viral component, aggregation artifact) combined with positive recognition of N-terminal transit-peptide-like features (S/T/R-rich, no acidic residues, precursor flag implied by sequence architecture) provides a concrete biological argument distinguishable from the sequence alone. The transit peptide recognition is not trivially obvious but is a standard bioinformatics inference within the scope of general molecular biology knowledge."
  },
  "case_id": "GO_cellular_component_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8LDU1 (HOZ_ARATH) from Arabidopsis thaliana is annotated as 'Non-canonical heme oxygenase HOZ, chloroplastic' with subcellular location 'Plastid, chloroplast' supported by both computational prediction (ECO:0000255) and experimental evidence (ECO:0000269|PubMed:33284325, IDA:TAIR). The GO annotation GO:0009507 (chloroplast) carries an IDA evidence code indicating direct experimental assay. X-ray crystallography (PDB 6M09/6M0A) confirmed structure and subcellular location. The sequence is flagged as 'Precursor,' consistent with a cleavable chloroplast transit peptide. The sequence matches exactly."
  },
  "important_caveats": [
    "The organism (Arabidopsis thaliana) is not stated in the model input; the model must infer plant origin from transit peptide features or rely on elimination logic.",
    "Transit peptide recognition from sequence alone is heuristic and not always unambiguous; here it is moderately clear but not a textbook-perfect example.",
    "The IDA:TAIR evidence code confirms experimental validation of chloroplast localization, strengthening the key beyond mere computational annotation.",
    "The GO term 'extracellular region' (GO:0005576, ISM:TAIR) also appears in the annotation (C7), but this is an inferred-by-sequence-match annotation and does not conflict with the primary chloroplast assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological categories (aggregation artifact, animal membrane structure, plant organelle, viral component). For a native, properly-folded, non-viral protein without transmembrane domains, only chloroplast is biologically plausible. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8LDU1 (HOZ_ARATH) from Arabidopsis thaliana is annotated as 'Non-canonical heme oxygenase HOZ, chloroplastic' with subcellular location 'Plastid, chloroplast' supported by both computational prediction (ECO:0000255) and experimental evidence (ECO:0000269|PubMed:33284325, IDA:TAIR). The GO annotation GO:0009507 (chloroplast) carries an IDA evidence code indicating direct experimental assay. X-ray crystallography (PDB 6M09/6M0A) confirmed structure and subcellular location. The sequence is flagged as 'Precursor,' consistent with a cleavable chloroplast transit peptide. The sequence matches exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three of four options can be eliminated by general biological reasoning: (1) Caveola is an animal-specific plasma membrane invagination requiring transmembrane domains and caveolin-binding motifs—this protein lacks any predicted TM segments. (2) Virion component requires viral origin—this protein shows no viral structural protein characteristics (no capsid-like β-barrel symmetry, no viral packaging motifs). (3) Inclusion body is an aggregation artifact of misfolded overexpressed proteins, not a native functional compartment for a properly annotated enzyme. Positive identification: The N-terminal ~50 residues (MKSLVAHFSTPLITARLVPRCIIHRASISAVSFSTVRRRFSPLTMASAAQSSSQAVSYGSGNSDTDVFKLIQAHEEK) display hallmarks of a chloroplast transit peptide—enrichment in Ser, Thr, and Arg with absence of acidic residues in the proximal region, and the protein is flagged as a 'Precursor' implying a cleavable targeting signal. Combined with the heme-oxygenase-like catalytic domain architecture (known to exist in plant chloroplasts), chloroplast is the most defensible answer.",
    "missing_item_specific_fact": "None critical. Organism identity (Arabidopsis thaliana) is not stated in the prompt, but the transit peptide features and elimination logic allow reasoning to the answer without it.",
    "reason": "The elimination of three implausible options (animal-specific structure, viral component, aggregation artifact) combined with positive recognition of N-terminal transit-peptide-like features (S/T/R-rich, no acidic residues, precursor flag implied by sequence architecture) provides a concrete biological argument distinguishable from the sequence alone. The transit peptide recognition is not trivially obvious but is a standard bioinformatics inference within the scope of general molecular biology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological categories (aggregation artifact, animal membrane structure, plant organelle, viral component). For a native, properly-folded, non-viral protein without transmembrane domains, only chloroplast is biologically plausible. No other option is defensible."
  },
  "important_caveats": [
    "The organism (Arabidopsis thaliana) is not stated in the model input; the model must infer plant origin from transit peptide features or rely on elimination logic.",
    "Transit peptide recognition from sequence alone is heuristic and not always unambiguous; here it is moderately clear but not a textbook-perfect example.",
    "The IDA:TAIR evidence code confirms experimental validation of chloroplast localization, strengthening the key beyond mere computational annotation.",
    "The GO term 'extracellular region' (GO:0005576, ISM:TAIR) also appears in the annotation (C7), but this is an inferred-by-sequence-match annotation and does not conflict with the primary chloroplast assignment."
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

**Accession:** `Q8LDU1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 145. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8LDU1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:22.839915+00:00.  

```json
"Q8LDU1"
```

Source SHA-256: `23e9b1091ccdd21a1a4857df560994042b0828be0fe2d9480a64c5911fb5d009`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8LDU1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:22.839915+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33284325","source":"PubMed"}],"value":"Protein HOMOLOG OF HugZ"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33284325","source":"PubMed"}],"value":"1.14.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Non-canonical heme oxygenase HOZ, chloroplastic"}}}
```

Source SHA-256: `23e9b1091ccdd21a1a4857df560994042b0828be0fe2d9480a64c5911fb5d009`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8LDU1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:22.839915+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255"},{"evidenceCode":"ECO:0000269","id":"33284325","source":"PubMed"}],"id":"SL-0049","value":"Plastid, chloroplast"}}]}
```

Source SHA-256: `23e9b1091ccdd21a1a4857df560994042b0828be0fe2d9480a64c5911fb5d009`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8LDU1.json)  
**Locator:** `/uniProtKBCrossReferences/32`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:22.839915+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"33284325","source":"PubMed"}],"id":"GO:0009507","properties":[{"key":"GoTerm","value":"C:chloroplast"},{"key":"GoEvidenceType","value":"IDA:TAIR"}]}
```

Source SHA-256: `23e9b1091ccdd21a1a4857df560994042b0828be0fe2d9480a64c5911fb5d009`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8LDU1.json)  
**Locator:** `/uniProtKBCrossReferences/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:22.839915+00:00.  

```json
{"database":"GO","id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"ISM:TAIR"}]}
```

Source SHA-256: `23e9b1091ccdd21a1a4857df560994042b0828be0fe2d9480a64c5911fb5d009`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8LDU1.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:22.839915+00:00.  

```json
{"citation":{"authors":["Wang J.","Guo Q.","Li X.","Wang X.","Liu L."],"citationCrossReferences":[{"database":"PubMed","id":"33284325"},{"database":"DOI","id":"10.1042/bcj20200712"}],"citationType":"journal article","firstPage":"4785","id":"33284325","journal":"Biochem. J.","lastPage":"4796","publicationDate":"2020","title":"The Arabidopsis locus At3g03890 encodes a dimeric beta-barrel protein implicated in heme degradation.","volume":"477"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6M09","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6M0A","source":"PDB"}],"referenceNumber":7,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) OF 63-321 IN COMPLEX WITH HEME B","FUNCTION","SUBUNIT","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `23e9b1091ccdd21a1a4857df560994042b0828be0fe2d9480a64c5911fb5d009`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8LDU1?format=txt&versions=145)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:32:31.264078+00:00.  

```text
ID   HOZ_ARATH               Reviewed;         321 AA.
AC   Q8LDU1; Q93WM0; Q9SRW6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2002, sequence version 1.
DT   28-JAN-2026, entry version 145.
DE   RecName: Full=Non-canonical heme oxygenase HOZ, chloroplastic {ECO:0000305};
DE            EC=1.14.-.- {ECO:0000269|PubMed:33284325};
DE   AltName: Full=Protein HOMOLOG OF HugZ {ECO:0000303|PubMed:33284325};
DE   Flags: Precursor;
GN   Name=HOZ {ECO:0000303|PubMed:33284325};
GN   OrderedLocusNames=At3g03890 {ECO:0000312|Araport:AT3G03890};
GN   ORFNames=F20H23.6 {ECO:0000312|EMBL:AAF00629.1};
OS   Arabidopsis thaliana (Mouse-ear cress).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   rosids; malvids; Brassicales; Brassicaceae; Camelineae; Arabidopsis.
OX   NCBI_TaxID=3702;
```

Source SHA-256: `7b566d5d1dd3bbf0e72985c250664254b7c75aa6454d79beda6fcd53797d29f2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8LDU1?format=txt&versions=145)  
**Locator:** `lines 91-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:32:31.264078+00:00.  

```text
RN   [6] {ECO:0007744|PDB:6M09, ECO:0007744|PDB:6M0A}
RP   X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) OF 63-321 IN COMPLEX WITH HEME B,
RP   FUNCTION, SUBUNIT, AND SUBCELLULAR LOCATION.
RX   PubMed=33284325; DOI=10.1042/bcj20200712;
RA   Wang J., Guo Q., Li X., Wang X., Liu L.;
RT   "The Arabidopsis locus At3g03890 encodes a dimeric beta-barrel protein
RT   implicated in heme degradation.";
RL   Biochem. J. 477:4785-4796(2020).
```

Source SHA-256: `7b566d5d1dd3bbf0e72985c250664254b7c75aa6454d79beda6fcd53797d29f2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8LDU1?format=txt&versions=145)  
**Locator:** `lines 106-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:32:31.264078+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Plastid, chloroplast {ECO:0000255,
CC       ECO:0000269|PubMed:33284325}.
```

Source SHA-256: `7b566d5d1dd3bbf0e72985c250664254b7c75aa6454d79beda6fcd53797d29f2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8LDU1?format=txt&versions=145)  
**Locator:** `lines 153-153`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:32:31.264078+00:00.  

```text
DR   GO; GO:0009507; C:chloroplast; IDA:TAIR.
```

Source SHA-256: `7b566d5d1dd3bbf0e72985c250664254b7c75aa6454d79beda6fcd53797d29f2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 105. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
