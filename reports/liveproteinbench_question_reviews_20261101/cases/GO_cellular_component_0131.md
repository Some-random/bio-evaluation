# GO_cellular_component_0131

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — nematocyst

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNHLIILVVAAVFLGMASAEDVFHKRFTVSCLCASDGPSVHGNKLTGTVAVGGCNPGWHKCNTEHNVLYECCKKN

[Multiple Choices]
A. inner membrane pellicle complex
B. mitochondrion
C. nematocyst
D. acrosomal membrane
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

> The exact 75-residue sequence matches a sea-anemone U-stichotoxin precursor whose UniProt record assigns it to the nematocyst and whose GO annotation is GO:0042151 (nematocyst). The GO assignment is computational (IEA); the record also gives a subcellular-location annotation, but the cited paper excerpt documents toxin characterization rather than independently demonstrating localization. Thus the key is supported as an annotation, not established here by direct localization evidence.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a signal peptide, and the cysteine-rich mature region is compatible with a secreted toxin. That supports secretion but does not, from sequence alone, specifically distinguish nematocyst storage from other secretory destinations.


**Missing item-specific fact**

> The sequence's identity as a Heteractis aurora stichotoxin and its protein-specific nematocyst annotation/localization are needed to select C over other possible secretory destinations.


**Reason**

> The question supplies no organism or functional context, and the sequence features do not uniquely identify a nematocyst. Selecting the keyed compartment depends on item-specific protein identity or annotation, rather than a sufficiently discriminating biological inference from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only matched-sequence annotation supports C. Although the sequence suggests secretion rather than a specific organelle, no other listed choice is comparably supported by the supplied evidence.


### Important caveats

- The GO nematocyst assignment is IEA, and the source snapshot used by the author is unknown.
- The matched database record lists both secreted and nematocyst locations; the cited publication excerpt does not itself establish localization experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and the cysteine-rich mature region is compatible with a secreted toxin. That supports secretion but does not, from sequence alone, specifically distinguish nematocyst storage from other secretory destinations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity as a Heteractis aurora stichotoxin and its protein-specific nematocyst annotation/localization are needed to select C over other possible secretory destinations.",
    "reason": "The question supplies no organism or functional context, and the sequence features do not uniquely identify a nematocyst. Selecting the keyed compartment depends on item-specific protein identity or annotation, rather than a sufficiently discriminating biological inference from the input."
  },
  "case_id": "GO_cellular_component_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C7",
      "C8",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact 75-residue sequence matches a sea-anemone U-stichotoxin precursor whose UniProt record assigns it to the nematocyst and whose GO annotation is GO:0042151 (nematocyst). The GO assignment is computational (IEA); the record also gives a subcellular-location annotation, but the cited paper excerpt documents toxin characterization rather than independently demonstrating localization. Thus the key is supported as an annotation, not established here by direct localization evidence."
  },
  "important_caveats": [
    "The GO nematocyst assignment is IEA, and the source snapshot used by the author is unknown.",
    "The matched database record lists both secreted and nematocyst locations; the cited publication excerpt does not itself establish localization experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports C. Although the sequence suggests secretion rather than a specific organelle, no other listed choice is comparably supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 75-residue sequence matches a sea-anemone U-stichotoxin precursor whose UniProt record assigns it to the nematocyst and whose GO annotation is GO:0042151 (nematocyst). The GO assignment is computational (IEA); the record also gives a subcellular-location annotation, but the cited paper excerpt documents toxin characterization rather than independently demonstrating localization. Thus the key is supported as an annotation, not established here by direct localization evidence.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C7", "C8", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a signal peptide, and the cysteine-rich mature region is compatible with a secreted toxin. That supports secretion but does not, from sequence alone, specifically distinguish nematocyst storage from other secretory destinations.",
    "missing_item_specific_fact": "The sequence's identity as a Heteractis aurora stichotoxin and its protein-specific nematocyst annotation/localization are needed to select C over other possible secretory destinations.",
    "reason": "The question supplies no organism or functional context, and the sequence features do not uniquely identify a nematocyst. Selecting the keyed compartment depends on item-specific protein identity or annotation, rather than a sufficiently discriminating biological inference from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports C. Although the sequence suggests secretion rather than a specific organelle, no other listed choice is comparably supported by the supplied evidence."
  },
  "important_caveats": [
    "The GO nematocyst assignment is IEA, and the source snapshot used by the author is unknown.",
    "The matched database record lists both secreted and nematocyst locations; the cited publication excerpt does not itself establish localization experimentally."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0N7KBN8 (U-stichotoxin-Hau3a from Heteractis aurora, banded sea anemone) annotates the subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, curator inference), with a corresponding GO cross-reference to GO:0042151 C:nematocyst (IEA:UniProtKB-SubCell). The sequence matches exactly (75 aa, SHA-256 confirmed in both current and historical snapshots). The evidence code is curator inference rather than direct experimental localization, but the biological context (a cnidarian peptide toxin isolated from sea anemone tissue) makes nematocyst storage well-established. The expected answer C is supported by the database annotation.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Weak elimination reasoning is possible: the N-terminal hydrophobic stretch (MNHLIILVVAAVFLGMASA) resembles a secretory signal peptide rather than a mitochondrial targeting sequence, arguing against B; there are no sperm-specific or acrosome-targeting features, arguing against D; and the inner membrane pellicle complex is exclusive to apicomplexan parasites, arguing against A. This leaves C. However, the positive identification of 'nematocyst' requires recognizing the cysteine-rich 75-aa peptide as a cnidarian toxin (the organism is not stated in the prompt), which is an item-specific fact.


**Missing item-specific fact**

> The organism identity (Cnidaria: Heteractis aurora, a sea anemone) and the recognition that this specific cysteine framework corresponds to a cnidarian stichotoxin family are not provided in the question input. Without organism context, the sequence's signal peptide + disulfide-rich small-peptide architecture is consistent with secreted toxins across many phyla, not uniquely with nematocyst storage.


**Reason**

> While the four distractors can be partially eliminated by general reasoning (signal peptide ≠ mitochondrial import; no acrosomal or apicomplexan features), the positive selection of 'nematocyst' over other possible secretory compartments (e.g., venom granules, secretory vesicles) depends on knowing this protein is a cnidarian toxin. Recognizing the specific cysteine pattern as a sea anemone toxin without organism metadata is effectively memorization of toxin-family sequence signatures, not general biological reasoning derivable from the prompt alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four provided choices, only nematocyst (C) matches the UniProt/GO annotation. The protein is also annotated as 'Secreted' (GO:0005576, extracellular region), but that term is not among the options, so no ambiguity arises within the given choices. The other three options (mitochondrion, acrosomal membrane, inner membrane pellicle complex) are clearly incompatible with a secreted cysteine-rich peptide.


### Important caveats

- The UniProt subcellular-location annotation carries evidence code ECO:0000305 (inferred by curator), not direct experimental localization (e.g., immunoelectron microscopy of nematocyst contents). The GO annotation is IEA (electronic annotation mapped from UniProt subcellular location).
- The organism (Heteractis aurora, Cnidaria) is absent from the evaluated model input; the reviewer identified it via accession metadata not shown to the model.
- The entry was first released in Swiss-Prot in April 2025; the benchmark construction date and author source snapshot are unknown, though the historical record (entry version 27, released by 2026-05-07) already contains the nematocyst annotation.
- The sequence is a precursor (75 aa including a 26-residue signal peptide); the mature toxin is residues 27–75. This does not affect the compartment annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Weak elimination reasoning is possible: the N-terminal hydrophobic stretch (MNHLIILVVAAVFLGMASA) resembles a secretory signal peptide rather than a mitochondrial targeting sequence, arguing against B; there are no sperm-specific or acrosome-targeting features, arguing against D; and the inner membrane pellicle complex is exclusive to apicomplexan parasites, arguing against A. This leaves C. However, the positive identification of 'nematocyst' requires recognizing the cysteine-rich 75-aa peptide as a cnidarian toxin (the organism is not stated in the prompt), which is an item-specific fact.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The organism identity (Cnidaria: Heteractis aurora, a sea anemone) and the recognition that this specific cysteine framework corresponds to a cnidarian stichotoxin family are not provided in the question input. Without organism context, the sequence's signal peptide + disulfide-rich small-peptide architecture is consistent with secreted toxins across many phyla, not uniquely with nematocyst storage.",
    "reason": "While the four distractors can be partially eliminated by general reasoning (signal peptide ≠ mitochondrial import; no acrosomal or apicomplexan features), the positive selection of 'nematocyst' over other possible secretory compartments (e.g., venom granules, secretory vesicles) depends on knowing this protein is a cnidarian toxin. Recognizing the specific cysteine pattern as a sea anemone toxin without organism metadata is effectively memorization of toxin-family sequence signatures, not general biological reasoning derivable from the prompt alone."
  },
  "case_id": "GO_cellular_component_0131",
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
      "GO3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0N7KBN8 (U-stichotoxin-Hau3a from Heteractis aurora, banded sea anemone) annotates the subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, curator inference), with a corresponding GO cross-reference to GO:0042151 C:nematocyst (IEA:UniProtKB-SubCell). The sequence matches exactly (75 aa, SHA-256 confirmed in both current and historical snapshots). The evidence code is curator inference rather than direct experimental localization, but the biological context (a cnidarian peptide toxin isolated from sea anemone tissue) makes nematocyst storage well-established. The expected answer C is supported by the database annotation."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation carries evidence code ECO:0000305 (inferred by curator), not direct experimental localization (e.g., immunoelectron microscopy of nematocyst contents). The GO annotation is IEA (electronic annotation mapped from UniProt subcellular location).",
    "The organism (Heteractis aurora, Cnidaria) is absent from the evaluated model input; the reviewer identified it via accession metadata not shown to the model.",
    "The entry was first released in Swiss-Prot in April 2025; the benchmark construction date and author source snapshot are unknown, though the historical record (entry version 27, released by 2026-05-07) already contains the nematocyst annotation.",
    "The sequence is a precursor (75 aa including a 26-residue signal peptide); the mature toxin is residues 27–75. This does not affect the compartment annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, only nematocyst (C) matches the UniProt/GO annotation. The protein is also annotated as 'Secreted' (GO:0005576, extracellular region), but that term is not among the options, so no ambiguity arises within the given choices. The other three options (mitochondrion, acrosomal membrane, inner membrane pellicle complex) are clearly incompatible with a secreted cysteine-rich peptide."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0N7KBN8 (U-stichotoxin-Hau3a from Heteractis aurora, banded sea anemone) annotates the subcellular location as 'Secreted' and 'Nematocyst' (ECO:0000305, curator inference), with a corresponding GO cross-reference to GO:0042151 C:nematocyst (IEA:UniProtKB-SubCell). The sequence matches exactly (75 aa, SHA-256 confirmed in both current and historical snapshots). The evidence code is curator inference rather than direct experimental localization, but the biological context (a cnidarian peptide toxin isolated from sea anemone tissue) makes nematocyst storage well-established. The expected answer C is supported by the database annotation.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C7", "H1", "H3", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Weak elimination reasoning is possible: the N-terminal hydrophobic stretch (MNHLIILVVAAVFLGMASA) resembles a secretory signal peptide rather than a mitochondrial targeting sequence, arguing against B; there are no sperm-specific or acrosome-targeting features, arguing against D; and the inner membrane pellicle complex is exclusive to apicomplexan parasites, arguing against A. This leaves C. However, the positive identification of 'nematocyst' requires recognizing the cysteine-rich 75-aa peptide as a cnidarian toxin (the organism is not stated in the prompt), which is an item-specific fact.",
    "missing_item_specific_fact": "The organism identity (Cnidaria: Heteractis aurora, a sea anemone) and the recognition that this specific cysteine framework corresponds to a cnidarian stichotoxin family are not provided in the question input. Without organism context, the sequence's signal peptide + disulfide-rich small-peptide architecture is consistent with secreted toxins across many phyla, not uniquely with nematocyst storage.",
    "reason": "While the four distractors can be partially eliminated by general reasoning (signal peptide ≠ mitochondrial import; no acrosomal or apicomplexan features), the positive selection of 'nematocyst' over other possible secretory compartments (e.g., venom granules, secretory vesicles) depends on knowing this protein is a cnidarian toxin. Recognizing the specific cysteine pattern as a sea anemone toxin without organism metadata is effectively memorization of toxin-family sequence signatures, not general biological reasoning derivable from the prompt alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, only nematocyst (C) matches the UniProt/GO annotation. The protein is also annotated as 'Secreted' (GO:0005576, extracellular region), but that term is not among the options, so no ambiguity arises within the given choices. The other three options (mitochondrion, acrosomal membrane, inner membrane pellicle complex) are clearly incompatible with a secreted cysteine-rich peptide."
  },
  "important_caveats": [
    "The UniProt subcellular-location annotation carries evidence code ECO:0000305 (inferred by curator), not direct experimental localization (e.g., immunoelectron microscopy of nematocyst contents). The GO annotation is IEA (electronic annotation mapped from UniProt subcellular location).",
    "The organism (Heteractis aurora, Cnidaria) is absent from the evaluated model input; the reviewer identified it via accession metadata not shown to the model.",
    "The entry was first released in Swiss-Prot in April 2025; the benchmark construction date and author source snapshot are unknown, though the historical record (entry version 27, released by 2026-05-07) already contains the nematocyst annotation.",
    "The sequence is a precursor (75 aa including a 26-residue signal peptide); the mature toxin is residues 27–75. This does not affect the compartment annotation."
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

**Accession:** `A0A0N7KBN8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 27. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:16.212733+00:00.  

```json
"A0A0N7KBN8"
```

Source SHA-256: `14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:16.212733+00:00.  

```json
{"commonName":"Banded sea anemone","lineage":["Eukaryota","Metazoa","Cnidaria","Anthozoa","Hexacorallia","Actiniaria","Stichodactylidae","Heteractis"],"scientificName":"Heteractis aurora","synonyms":["Actinia aurora"],"taxonId":478399}
```

Source SHA-256: `14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:16.212733+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39530114","source":"PubMed"}],"value":"Hau IV"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39530114","source":"PubMed"}],"value":"U-stichotoxin-Hau3a"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39530114","source":"PubMed"}],"value":"U-SHTX-Hau3a"}]}}
```

Source SHA-256: `14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:16.212733+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0177","value":"Nematocyst"}}]}
```

Source SHA-256: `14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)  
**Locator:** `/uniProtKBCrossReferences/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:16.212733+00:00.  

```json
{"database":"GO","id":"GO:0042151","properties":[{"key":"GoTerm","value":"C:nematocyst"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0N7KBN8.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:16.212733+00:00.  

```json
{"citation":{"authors":["Homma T.","Ishida M.","Nagashima Y.","Shiomi K."],"citationCrossReferences":[{"database":"PubMed","id":"39530114"},{"database":"DOI","id":"10.1590/1678-9199-jvatitd-2024-0019"}],"citationType":"journal article","firstPage":"e20240019","id":"39530114","journal":"J. Venom. Anim. Toxins Incl. Trop. Dis.","lastPage":"e20240019","publicationDate":"2024","title":"Isolation and cDNA cloning of four peptide toxins from the sea anemone Heteractis aurora.","volume":"30"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAS68535.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","PROTEIN SEQUENCE OF 27-45","MASS SPECTROMETRY","TOXIC DOSE"]}
```

Source SHA-256: `14a72a4a372579a74311518be743e4606d83221eb9050f5e99a1d83164f5a731`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:19.138834+00:00.  

```text
ID   NA3A_HETAU              Reviewed;          75 AA.
AC   A0A0N7KBN8;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-JAN-2016, sequence version 1.
DT   28-JAN-2026, entry version 27.
DE   RecName: Full=U-stichotoxin-Hau3a {ECO:0000303|PubMed:39530114};
DE            Short=U-SHTX-Hau3a {ECO:0000303|PubMed:39530114};
DE   AltName: Full=Hau IV {ECO:0000303|PubMed:39530114};
DE   Flags: Precursor;
GN   Name=HAUTX4 {ECO:0000312|EMBL:BAS68535.1};
OS   Heteractis aurora (Banded sea anemone) (Actinia aurora).
OC   Eukaryota; Metazoa; Cnidaria; Anthozoa; Hexacorallia; Actiniaria;
OC   Stichodactylidae; Heteractis.
OX   NCBI_TaxID=478399;
```

Source SHA-256: `1ce3ed23eec7f5b61c3571fb00341ae56831d6fb53df52f12c02ae9e520612ac`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27)  
**Locator:** `lines 24-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:19.138834+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305}. Nematocyst {ECO:0000305}.
```

Source SHA-256: `1ce3ed23eec7f5b61c3571fb00341ae56831d6fb53df52f12c02ae9e520612ac`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0N7KBN8?format=txt&versions=27)  
**Locator:** `lines 40-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-02T04:24:19.138834+00:00.  

```text
DR   GO; GO:0042151; C:nematocyst; IEA:UniProtKB-SubCell.
```

Source SHA-256: `1ce3ed23eec7f5b61c3571fb00341ae56831d6fb53df52f12c02ae9e520612ac`.

### Evidence GO3

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
