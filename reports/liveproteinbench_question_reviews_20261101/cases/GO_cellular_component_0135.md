# GO_cellular_component_0135

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — nematocyst

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKPIFIVALLFSTCLVNAKPSIDDAEMKREPKPNIINPPCIGCYYQVGNECVYDKFKCGAVRKREPKPNIINPPCIGCYYQVGNECVYDKFKCGAV

[Multiple Choices]
A. endosome membrane
B. microtubule cytoskeleton
C. NF-kappaB p50/p65 complex
D. nematocyst
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

> The exact 96-aa sequence matches a UniProt entry annotated as secreted and localized to a nematocyst, supporting D. The GO nematocyst assignment is computational (IEA), while the UniProt subcellular-location annotation is manually attributed; the cited paper documents toxin-related work but the supplied excerpts do not establish a direct experimental localization measurement.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a signal peptide, and the sequence is compatible with a secreted peptide toxin. That supports secretion, but does not identify a nematocyst as the particular cellular component.


**Missing item-specific fact**

> The protein's identity and its specific association with a cnidarian nematocyst are absent from the input; distinguishing D requires that protein-specific annotation or equivalent external knowledge.


**Reason**

> General sequence reasoning can make the intracellular distractors less plausible, but it cannot distinguish nematocyst localization from other destinations of a secreted protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, D is supported by the matched sequence's annotation. The sequence alone does not establish that specific location, but the other options are not comparably supported.


### Important caveats

- The evidence identifies a matched database record, but the author’s exact source snapshot is unknown.
- The GO annotation is inferred electronically; the excerpts do not show direct experimental localization to nematocysts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and the sequence is compatible with a secreted peptide toxin. That supports secretion, but does not identify a nematocyst as the particular cellular component.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and its specific association with a cnidarian nematocyst are absent from the input; distinguishing D requires that protein-specific annotation or equivalent external knowledge.",
    "reason": "General sequence reasoning can make the intracellular distractors less plausible, but it cannot distinguish nematocyst localization from other destinations of a secreted protein."
  },
  "case_id": "GO_cellular_component_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "C8",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact 96-aa sequence matches a UniProt entry annotated as secreted and localized to a nematocyst, supporting D. The GO nematocyst assignment is computational (IEA), while the UniProt subcellular-location annotation is manually attributed; the cited paper documents toxin-related work but the supplied excerpts do not establish a direct experimental localization measurement."
  },
  "important_caveats": [
    "The evidence identifies a matched database record, but the author’s exact source snapshot is unknown.",
    "The GO annotation is inferred electronically; the excerpts do not show direct experimental localization to nematocysts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D is supported by the matched sequence's annotation. The sequence alone does not establish that specific location, but the other options are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 96-aa sequence matches a UniProt entry annotated as secreted and localized to a nematocyst, supporting D. The GO nematocyst assignment is computational (IEA), while the UniProt subcellular-location annotation is manually attributed; the cited paper documents toxin-related work but the supplied excerpts do not establish a direct experimental localization measurement.",
    "evidence_ids": ["C1", "C5", "C7", "C8", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and the sequence is compatible with a secreted peptide toxin. That supports secretion, but does not identify a nematocyst as the particular cellular component.",
    "missing_item_specific_fact": "The protein's identity and its specific association with a cnidarian nematocyst are absent from the input; distinguishing D requires that protein-specific annotation or equivalent external knowledge.",
    "reason": "General sequence reasoning can make the intracellular distractors less plausible, but it cannot distinguish nematocyst localization from other destinations of a secreted protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D is supported by the matched sequence's annotation. The sequence alone does not establish that specific location, but the other options are not comparably supported."
  },
  "important_caveats": [
    "The evidence identifies a matched database record, but the author’s exact source snapshot is unknown.",
    "The GO annotation is inferred electronically; the excerpts do not show direct experimental localization to nematocysts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0P0UTQ7 (U-stichotoxin-Hau2b from Heteractis aurora, a sea anemone) explicitly annotates subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, curator inference). GO:0042151 (C:nematocyst) is assigned with IEA:UniProtKB-SubCell evidence. The sequence matches exactly (SHA256 confirmed across both current and historical entry versions). The nematocyst annotation is consistent with the protein being a small cysteine-rich peptide toxin from a cnidarian, stored in nematocyst organelles.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch (MKPIFIVALLFSTCLVNA) is a canonical signal peptide indicating entry into the secretory pathway. The mature region is a small (~60 aa) cysteine-rich peptide with repeated inhibitor-cystine-knot-like motifs (CIGCYYQVGNECVYDKFKCGAV), characteristic of peptide toxins. Among the four options, only nematocyst (D) is a secretory-pathway-derived organelle that stores peptide toxins. Options A (endosome membrane), B (microtubule cytoskeleton), and C (NF-kappaB p50/p65 complex) are all intracellular structures incompatible with a signal-peptide-bearing small secreted toxin lacking transmembrane domains, microtubule-binding motifs, or nuclear localization signals. The elimination of A, B, and C via the signal peptide and absence of relevant targeting features is a concrete biological argument.


**Missing item-specific fact**

> The organism (cnidarian/sea anemone) is not stated in the question. Recognizing that nematocysts are the cnidarian-specific toxin-storage organelle requires either organism context or specialized knowledge of cnidarian biology. However, the signal peptide + toxin-like cysteine-rich structure + elimination of three clearly intracellular options provides a defensible reasoning path to D even without explicit organism annotation.


**Reason**

> The signal peptide provides a strong, general biological argument that the protein enters the secretory pathway, which is incompatible with options A, B, and C (all intracellular, non-secretory structures). The cysteine-rich small-peptide architecture supports a toxin stored in a specialized secretory organelle. While the specific term 'nematocyst' is cnidarian-specific, the elimination logic and the toxin-like sequence features make D the only biologically coherent choice among the four options without requiring exact sequence memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are biologically distinct: endosome membrane (requires endosomal sorting signals), microtubule cytoskeleton (requires cytoplasmic MT-binding domains), NF-kappaB complex (requires nuclear localization and specific protein-protein interaction domains), and nematocyst (secretory toxin-storage organelle). The signal peptide and small cysteine-rich toxin architecture clearly favor D and disfavor A, B, and C. No ambiguity among the given choices.


### Important caveats

- The UniProt subcellular location annotation uses ECO:0000305 (curator inference), not direct experimental localization. The GO annotation is IEA (Inferred from Electronic Annotation), derived from the UniProt subcellular location field.
- The organism is not stated in the question input. Reasoning to 'nematocyst' specifically (rather than generic 'secreted') requires recognizing cnidarian toxin biology, which is general knowledge but adds a layer of specialized context.
- The identity of this protein as U-stichotoxin-Hau2b from Heteractis aurora was established by reviewer-only accession lookup; the evaluated model receives only the raw sequence.
- The sequence contains a duplicated 28-residue block (CIGCYYQVGNECVYDKFKCGAVRKREPKPNIINPPCIGCYYQVGNECVYDKFKCGAV), which is unusual but does not alter the compartment prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MKPIFIVALLFSTCLVNA) is a canonical signal peptide indicating entry into the secretory pathway. The mature region is a small (~60 aa) cysteine-rich peptide with repeated inhibitor-cystine-knot-like motifs (CIGCYYQVGNECVYDKFKCGAV), characteristic of peptide toxins. Among the four options, only nematocyst (D) is a secretory-pathway-derived organelle that stores peptide toxins. Options A (endosome membrane), B (microtubule cytoskeleton), and C (NF-kappaB p50/p65 complex) are all intracellular structures incompatible with a signal-peptide-bearing small secreted toxin lacking transmembrane domains, microtubule-binding motifs, or nuclear localization signals. The elimination of A, B, and C via the signal peptide and absence of relevant targeting features is a concrete biological argument.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The organism (cnidarian/sea anemone) is not stated in the question. Recognizing that nematocysts are the cnidarian-specific toxin-storage organelle requires either organism context or specialized knowledge of cnidarian biology. However, the signal peptide + toxin-like cysteine-rich structure + elimination of three clearly intracellular options provides a defensible reasoning path to D even without explicit organism annotation.",
    "reason": "The signal peptide provides a strong, general biological argument that the protein enters the secretory pathway, which is incompatible with options A, B, and C (all intracellular, non-secretory structures). The cysteine-rich small-peptide architecture supports a toxin stored in a specialized secretory organelle. While the specific term 'nematocyst' is cnidarian-specific, the elimination logic and the toxin-like sequence features make D the only biologically coherent choice among the four options without requiring exact sequence memorization."
  },
  "case_id": "GO_cellular_component_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C7",
      "H1",
      "H3",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0P0UTQ7 (U-stichotoxin-Hau2b from Heteractis aurora, a sea anemone) explicitly annotates subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, curator inference). GO:0042151 (C:nematocyst) is assigned with IEA:UniProtKB-SubCell evidence. The sequence matches exactly (SHA256 confirmed across both current and historical entry versions). The nematocyst annotation is consistent with the protein being a small cysteine-rich peptide toxin from a cnidarian, stored in nematocyst organelles."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses ECO:0000305 (curator inference), not direct experimental localization. The GO annotation is IEA (Inferred from Electronic Annotation), derived from the UniProt subcellular location field.",
    "The organism is not stated in the question input. Reasoning to 'nematocyst' specifically (rather than generic 'secreted') requires recognizing cnidarian toxin biology, which is general knowledge but adds a layer of specialized context.",
    "The identity of this protein as U-stichotoxin-Hau2b from Heteractis aurora was established by reviewer-only accession lookup; the evaluated model receives only the raw sequence.",
    "The sequence contains a duplicated 28-residue block (CIGCYYQVGNECVYDKFKCGAVRKREPKPNIINPPCIGCYYQVGNECVYDKFKCGAV), which is unusual but does not alter the compartment prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are biologically distinct: endosome membrane (requires endosomal sorting signals), microtubule cytoskeleton (requires cytoplasmic MT-binding domains), NF-kappaB complex (requires nuclear localization and specific protein-protein interaction domains), and nematocyst (secretory toxin-storage organelle). The signal peptide and small cysteine-rich toxin architecture clearly favor D and disfavor A, B, and C. No ambiguity among the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0P0UTQ7 (U-stichotoxin-Hau2b from Heteractis aurora, a sea anemone) explicitly annotates subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, curator inference). GO:0042151 (C:nematocyst) is assigned with IEA:UniProtKB-SubCell evidence. The sequence matches exactly (SHA256 confirmed across both current and historical entry versions). The nematocyst annotation is consistent with the protein being a small cysteine-rich peptide toxin from a cnidarian, stored in nematocyst organelles.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C7", "H1", "H3", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MKPIFIVALLFSTCLVNA) is a canonical signal peptide indicating entry into the secretory pathway. The mature region is a small (~60 aa) cysteine-rich peptide with repeated inhibitor-cystine-knot-like motifs (CIGCYYQVGNECVYDKFKCGAV), characteristic of peptide toxins. Among the four options, only nematocyst (D) is a secretory-pathway-derived organelle that stores peptide toxins. Options A (endosome membrane), B (microtubule cytoskeleton), and C (NF-kappaB p50/p65 complex) are all intracellular structures incompatible with a signal-peptide-bearing small secreted toxin lacking transmembrane domains, microtubule-binding motifs, or nuclear localization signals. The elimination of A, B, and C via the signal peptide and absence of relevant targeting features is a concrete biological argument.",
    "missing_item_specific_fact": "The organism (cnidarian/sea anemone) is not stated in the question. Recognizing that nematocysts are the cnidarian-specific toxin-storage organelle requires either organism context or specialized knowledge of cnidarian biology. However, the signal peptide + toxin-like cysteine-rich structure + elimination of three clearly intracellular options provides a defensible reasoning path to D even without explicit organism annotation.",
    "reason": "The signal peptide provides a strong, general biological argument that the protein enters the secretory pathway, which is incompatible with options A, B, and C (all intracellular, non-secretory structures). The cysteine-rich small-peptide architecture supports a toxin stored in a specialized secretory organelle. While the specific term 'nematocyst' is cnidarian-specific, the elimination logic and the toxin-like sequence features make D the only biologically coherent choice among the four options without requiring exact sequence memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are biologically distinct: endosome membrane (requires endosomal sorting signals), microtubule cytoskeleton (requires cytoplasmic MT-binding domains), NF-kappaB complex (requires nuclear localization and specific protein-protein interaction domains), and nematocyst (secretory toxin-storage organelle). The signal peptide and small cysteine-rich toxin architecture clearly favor D and disfavor A, B, and C. No ambiguity among the given choices."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses ECO:0000305 (curator inference), not direct experimental localization. The GO annotation is IEA (Inferred from Electronic Annotation), derived from the UniProt subcellular location field.",
    "The organism is not stated in the question input. Reasoning to 'nematocyst' specifically (rather than generic 'secreted') requires recognizing cnidarian toxin biology, which is general knowledge but adds a layer of specialized context.",
    "The identity of this protein as U-stichotoxin-Hau2b from Heteractis aurora was established by reviewer-only accession lookup; the evaluated model receives only the raw sequence.",
    "The sequence contains a duplicated 28-residue block (CIGCYYQVGNECVYDKFKCGAVRKREPKPNIINPPCIGCYYQVGNECVYDKFKCGAV), which is unusual but does not alter the compartment prediction."
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

**Accession:** `A0A0P0UTQ7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 8. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.589867+00:00.  

```json
"A0A0P0UTQ7"
```

Source SHA-256: `94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.589867+00:00.  

```json
{"commonName":"Banded sea anemone","lineage":["Eukaryota","Metazoa","Cnidaria","Anthozoa","Hexacorallia","Actiniaria","Stichodactylidae","Heteractis"],"scientificName":"Heteractis aurora","synonyms":["Actinia aurora"],"taxonId":478399}
```

Source SHA-256: `94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.589867+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39530114","source":"PubMed"}],"value":"Hau III"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39530114","source":"PubMed"}],"value":"U-stichotoxin-Hau2b"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39530114","source":"PubMed"}],"value":"U-SHTX-Hau2b"}]}}
```

Source SHA-256: `94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.589867+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0177","value":"Nematocyst"}}]}
```

Source SHA-256: `94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.589867+00:00.  

```json
{"database":"GO","id":"GO:0042151","properties":[{"key":"GoTerm","value":"C:nematocyst"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTQ7.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.589867+00:00.  

```json
{"citation":{"authors":["Homma T.","Ishida M.","Nagashima Y.","Shiomi K."],"citationCrossReferences":[{"database":"PubMed","id":"39530114"},{"database":"DOI","id":"10.1590/1678-9199-jvatitd-2024-0019"}],"citationType":"journal article","firstPage":"e20240019","id":"39530114","journal":"J. Venom. Anim. Toxins Incl. Trop. Dis.","lastPage":"e20240019","publicationDate":"2024","title":"Isolation and cDNA cloning of four peptide toxins from the sea anemone Heteractis aurora.","volume":"30"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAS68534.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","PROTEIN SEQUENCE OF 34-58 AND 69-93","MASS SPECTROMETRY","TOXIC DOSE"]}
```

Source SHA-256: `94a2d30620a2157d5ee7fe183533d9b6028d93d914b8118ec47fd44aee61e7f2`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 8 / 1.  
**Retrieved:** 2026-11-02T04:24:21.319533+00:00.  

```text
ID   BBH2B_HETAU             Reviewed;          96 AA.
AC   A0A0P0UTQ7;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-JAN-2016, sequence version 1.
DT   28-JAN-2026, entry version 8.
DE   RecName: Full=U-stichotoxin-Hau2b {ECO:0000303|PubMed:39530114};
DE            Short=U-SHTX-Hau2b {ECO:0000303|PubMed:39530114};
DE   AltName: Full=Hau III {ECO:0000303|PubMed:39530114};
DE   Flags: Precursor;
GN   Name=HAUTX3 {ECO:0000312|EMBL:BAS68534.1};
OS   Heteractis aurora (Banded sea anemone) (Actinia aurora).
OC   Eukaryota; Metazoa; Cnidaria; Anthozoa; Hexacorallia; Actiniaria;
OC   Stichodactylidae; Heteractis.
OX   NCBI_TaxID=478399;
```

Source SHA-256: `7b38529a8265c44e6300a8d5f7dec9b2e6c0d79bfeff7fbb32de9c7c77031881`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8)  
**Locator:** `lines 25-25`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 8 / 1.  
**Retrieved:** 2026-11-02T04:24:21.319533+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305}. Nematocyst {ECO:0000305}.
```

Source SHA-256: `7b38529a8265c44e6300a8d5f7dec9b2e6c0d79bfeff7fbb32de9c7c77031881`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTQ7?format=txt&versions=8)  
**Locator:** `lines 40-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 8 / 1.  
**Retrieved:** 2026-11-02T04:24:21.319533+00:00.  

```text
DR   GO; GO:0042151; C:nematocyst; IEA:UniProtKB-SubCell.
```

Source SHA-256: `7b38529a8265c44e6300a8d5f7dec9b2e6c0d79bfeff7fbb32de9c7c77031881`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 234754-234763`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0042151
name: nematocyst
namespace: cellular_component
def: "An organelle found in cnidoblast (nematoblast) cells. When matured, these stinging organelles store toxins and can deliver them when the cnidocil (a short extension of the cnidocyst) is stimulated by a prey or another stimulus." [DOI:10.1139/z02-135, GOC:jl]
synonym: "cnidocyst" EXACT []
xref: Wikipedia:Cnidocyte
is_a: GO:0043232 ! intracellular membraneless organelle
relationship: part_of GO:0005938 ! cell cortex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 135. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
