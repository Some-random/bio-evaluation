# GO_cellular_component_0010

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — cytosolic small ribosomal subunit

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATVYDVPGDLLVERVAKALKEVPEIKPPEWAPFVKTGRHKERLPEQEDWWYYRVASVFRKVYIDGPVGIERLRTWYGGRKNRGHAPEHFYKAGGSIIRKALQQLEAAGFVQKVPGEGRIVTPKGQSFLDKIATELKKELEEQIPELKKY

[Multiple Choices]
A. ATP-binding cassette (ABC) transporter complex
B. checkpoint clamp complex
C. transcription regulator complex
D. cytosolic small ribosomal subunit
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

> The exact supplied sequence matches a Thermococcus kodakarensis protein annotated as small ribosomal subunit protein eS19, and the matched record assigns it to the cytosolic small ribosomal subunit. The protein name is supported by a HAMAP rule, and the GO annotation is IBA, so this is computational/phylogenetic annotation rather than direct experimental evidence in the excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The short, soluble sequence lacks the hydrophobic character expected for a membrane transporter, making the ABC-transporter choice less plausible; its size also makes a checkpoint clamp subunit unlikely. Those broad clues do not specifically distinguish a ribosomal protein from a transcription-related protein.


**Missing item-specific fact**

> The sequence's identity or family as archaeal ribosomal protein eS19, or an equivalent protein-specific functional annotation, is not supplied.


**Reason**

> Selecting D depends on knowing the protein-specific ribosomal identity. Generic sequence properties can help eliminate some choices but do not establish membership in the small ribosomal subunit over the remaining alternative.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein-specific annotation supports D; the other choices are not comparably supported by the supplied sequence.


### Important caveats

- The historical record also matches the sequence, but the author's exact source snapshot is unknown.
- The cited GO evidence is IBA, and the protein-name evidence is computational; the excerpts do not establish direct experimental localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short, soluble sequence lacks the hydrophobic character expected for a membrane transporter, making the ABC-transporter choice less plausible; its size also makes a checkpoint clamp subunit unlikely. Those broad clues do not specifically distinguish a ribosomal protein from a transcription-related protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity or family as archaeal ribosomal protein eS19, or an equivalent protein-specific functional annotation, is not supplied.",
    "reason": "Selecting D depends on knowing the protein-specific ribosomal identity. Generic sequence properties can help eliminate some choices but do not establish membership in the small ribosomal subunit over the remaining alternative."
  },
  "case_id": "GO_cellular_component_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a Thermococcus kodakarensis protein annotated as small ribosomal subunit protein eS19, and the matched record assigns it to the cytosolic small ribosomal subunit. The protein name is supported by a HAMAP rule, and the GO annotation is IBA, so this is computational/phylogenetic annotation rather than direct experimental evidence in the excerpts."
  },
  "important_caveats": [
    "The historical record also matches the sequence, but the author's exact source snapshot is unknown.",
    "The cited GO evidence is IBA, and the protein-name evidence is computational; the excerpts do not establish direct experimental localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein-specific annotation supports D; the other choices are not comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a Thermococcus kodakarensis protein annotated as small ribosomal subunit protein eS19, and the matched record assigns it to the cytosolic small ribosomal subunit. The protein name is supported by a HAMAP rule, and the GO annotation is IBA, so this is computational/phylogenetic annotation rather than direct experimental evidence in the excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The short, soluble sequence lacks the hydrophobic character expected for a membrane transporter, making the ABC-transporter choice less plausible; its size also makes a checkpoint clamp subunit unlikely. Those broad clues do not specifically distinguish a ribosomal protein from a transcription-related protein.",
    "missing_item_specific_fact": "The sequence's identity or family as archaeal ribosomal protein eS19, or an equivalent protein-specific functional annotation, is not supplied.",
    "reason": "Selecting D depends on knowing the protein-specific ribosomal identity. Generic sequence properties can help eliminate some choices but do not establish membership in the small ribosomal subunit over the remaining alternative."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein-specific annotation supports D; the other choices are not comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The historical record also matches the sequence, but the author's exact source snapshot is unknown.",
    "The cited GO evidence is IBA, and the protein-name evidence is computational; the excerpts do not establish direct experimental localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (150 aa, SHA256-matched) corresponds to UniProt Q5JGN5, annotated as 'Small ribosomal subunit protein eS19' (via HAMAP-Rule MF_01474) and carrying GO:0022627 'cytosolic small ribosomal subunit' (evidence IBA:GO_Central). The protein is from Thermococcus kodakarensis, an archaeon whose ribosomes are cytosolic; GO:0022627 includes 'prokaryotic small ribosomal subunit' as a NARROW synonym, making the term appropriate. The evidence codes (HAMAP-Rule, IBA) indicate computational/pattern-based inference rather than direct experimental localization, but the protein identity as a small ribosomal subunit protein is well-established.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 150-aa protein is extremely rich in basic residues (numerous K and R) typical of rRNA-binding ribosomal proteins. It lacks any transmembrane segments or Walker A/B ATP-binding motifs, ruling out ABC transporter complex (A). Its small size (150 aa) is far below the ~300-500+ aa of checkpoint clamp subunits (Rad9/Rad1/Hus1), ruling out (B). No canonical DNA-binding motifs (zinc fingers, helix-turn-helix, leucine zippers) are present, weakening (C). The combination of very small size, high basic-residue density, absence of membrane/ATP/DNA-binding domains, and no signal peptide is most consistent with a cytosolic small ribosomal subunit protein (D).


**Missing item-specific fact**

> None critical. The reasoning relies on general structural/functional domain absence and compositional bias rather than recognition of a specific database entry.


**Reason**

> A model can eliminate A (no TM/ATP motifs), B (too small for clamp subunits), and partially C (no DNA-binding domains) through general protein-structure knowledge, leaving D as the best fit given the small size and basic-residue enrichment characteristic of ribosomal proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While option C (transcription regulator complex) could superficially be considered for a small basic protein, the absence of any recognizable DNA-binding structural motif and the overall ribosomal-protein-like composition make D clearly the most defensible choice. The other options (A, B) are effectively excluded by size and domain content.


### Important caveats

- The GO annotation evidence is IBA:GO_Central (computational inference by biological aspect), not direct experimental localization. The protein name derives from a HAMAP pattern rule, also computational.
- The protein is archaeal (Thermococcus kodakarensis); 'cytosolic' in GO:0022627 encompasses prokaryotic/archaeal ribosomes per the NARROW synonym 'prokaryotic small ribosomal subunit'.
- The reasoning argument (basic-residue enrichment, small size, absence of functional domains) is suggestive but not definitive; some small basic proteins are not ribosomal. The elimination logic is the primary discriminator.
- Identity of the accession Q5JGN5 was inferred by the reviewer from dataset metadata, not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 150-aa protein is extremely rich in basic residues (numerous K and R) typical of rRNA-binding ribosomal proteins. It lacks any transmembrane segments or Walker A/B ATP-binding motifs, ruling out ABC transporter complex (A). Its small size (150 aa) is far below the ~300-500+ aa of checkpoint clamp subunits (Rad9/Rad1/Hus1), ruling out (B). No canonical DNA-binding motifs (zinc fingers, helix-turn-helix, leucine zippers) are present, weakening (C). The combination of very small size, high basic-residue density, absence of membrane/ATP/DNA-binding domains, and no signal peptide is most consistent with a cytosolic small ribosomal subunit protein (D).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The reasoning relies on general structural/functional domain absence and compositional bias rather than recognition of a specific database entry.",
    "reason": "A model can eliminate A (no TM/ATP motifs), B (too small for clamp subunits), and partially C (no DNA-binding domains) through general protein-structure knowledge, leaving D as the best fit given the small size and basic-residue enrichment characteristic of ribosomal proteins."
  },
  "case_id": "GO_cellular_component_0010",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The sequence (150 aa, SHA256-matched) corresponds to UniProt Q5JGN5, annotated as 'Small ribosomal subunit protein eS19' (via HAMAP-Rule MF_01474) and carrying GO:0022627 'cytosolic small ribosomal subunit' (evidence IBA:GO_Central). The protein is from Thermococcus kodakarensis, an archaeon whose ribosomes are cytosolic; GO:0022627 includes 'prokaryotic small ribosomal subunit' as a NARROW synonym, making the term appropriate. The evidence codes (HAMAP-Rule, IBA) indicate computational/pattern-based inference rather than direct experimental localization, but the protein identity as a small ribosomal subunit protein is well-established."
  },
  "important_caveats": [
    "The GO annotation evidence is IBA:GO_Central (computational inference by biological aspect), not direct experimental localization. The protein name derives from a HAMAP pattern rule, also computational.",
    "The protein is archaeal (Thermococcus kodakarensis); 'cytosolic' in GO:0022627 encompasses prokaryotic/archaeal ribosomes per the NARROW synonym 'prokaryotic small ribosomal subunit'.",
    "The reasoning argument (basic-residue enrichment, small size, absence of functional domains) is suggestive but not definitive; some small basic proteins are not ribosomal. The elimination logic is the primary discriminator.",
    "Identity of the accession Q5JGN5 was inferred by the reviewer from dataset metadata, not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option C (transcription regulator complex) could superficially be considered for a small basic protein, the absence of any recognizable DNA-binding structural motif and the overall ribosomal-protein-like composition make D clearly the most defensible choice. The other options (A, B) are effectively excluded by size and domain content."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (150 aa, SHA256-matched) corresponds to UniProt Q5JGN5, annotated as 'Small ribosomal subunit protein eS19' (via HAMAP-Rule MF_01474) and carrying GO:0022627 'cytosolic small ribosomal subunit' (evidence IBA:GO_Central). The protein is from Thermococcus kodakarensis, an archaeon whose ribosomes are cytosolic; GO:0022627 includes 'prokaryotic small ribosomal subunit' as a NARROW synonym, making the term appropriate. The evidence codes (HAMAP-Rule, IBA) indicate computational/pattern-based inference rather than direct experimental localization, but the protein identity as a small ribosomal subunit protein is well-established.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H2", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 150-aa protein is extremely rich in basic residues (numerous K and R) typical of rRNA-binding ribosomal proteins. It lacks any transmembrane segments or Walker A/B ATP-binding motifs, ruling out ABC transporter complex (A). Its small size (150 aa) is far below the ~300-500+ aa of checkpoint clamp subunits (Rad9/Rad1/Hus1), ruling out (B). No canonical DNA-binding motifs (zinc fingers, helix-turn-helix, leucine zippers) are present, weakening (C). The combination of very small size, high basic-residue density, absence of membrane/ATP/DNA-binding domains, and no signal peptide is most consistent with a cytosolic small ribosomal subunit protein (D).",
    "missing_item_specific_fact": "None critical. The reasoning relies on general structural/functional domain absence and compositional bias rather than recognition of a specific database entry.",
    "reason": "A model can eliminate A (no TM/ATP motifs), B (too small for clamp subunits), and partially C (no DNA-binding domains) through general protein-structure knowledge, leaving D as the best fit given the small size and basic-residue enrichment characteristic of ribosomal proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option C (transcription regulator complex) could superficially be considered for a small basic protein, the absence of any recognizable DNA-binding structural motif and the overall ribosomal-protein-like composition make D clearly the most defensible choice. The other options (A, B) are effectively excluded by size and domain content."
  },
  "important_caveats": [
    "The GO annotation evidence is IBA:GO_Central (computational inference by biological aspect), not direct experimental localization. The protein name derives from a HAMAP pattern rule, also computational.",
    "The protein is archaeal (Thermococcus kodakarensis); 'cytosolic' in GO:0022627 encompasses prokaryotic/archaeal ribosomes per the NARROW synonym 'prokaryotic small ribosomal subunit'.",
    "The reasoning argument (basic-residue enrichment, small size, absence of functional domains) is suggestive but not definitive; some small basic proteins are not ribosomal. The elimination logic is the primary discriminator.",
    "Identity of the accession Q5JGN5 was inferred by the reviewer from dataset metadata, not provided to the evaluated model."
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

**Accession:** `Q5JGN5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 104. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JGN5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:19.785707+00:00.  

```json
"Q5JGN5"
```

Source SHA-256: `e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JGN5.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:19.785707+00:00.  

```json
{"commonName":"Pyrococcus kodakaraensis (strain KOD1)","lineage":["Archaea","Methanobacteriati","Methanobacteriota","Thermococci","Thermococcales","Thermococcaceae","Thermococcus"],"scientificName":"Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)","taxonId":69014}
```

Source SHA-256: `e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JGN5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:19.785707+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01474","source":"HAMAP-Rule"}],"value":"Small ribosomal subunit protein eS19"}}}
```

Source SHA-256: `e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JGN5.json)  
**Locator:** `/uniProtKBCrossReferences/27`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:19.785707+00:00.  

```json
{"database":"GO","id":"GO:0022627","properties":[{"key":"GoTerm","value":"C:cytosolic small ribosomal subunit"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `e144e65e3685bef7f3cec25fa03f0af6a1a9ecfa4cc3f83127dc7805eff27a59`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JGN5?format=txt&versions=104)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 104 / 1.  
**Retrieved:** 2026-11-02T04:31:23.320142+00:00.  

```text
ID   RS19E_THEKO             Reviewed;         150 AA.
AC   Q5JGN5;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-FEB-2005, sequence version 1.
DT   18-JUN-2025, entry version 104.
DE   RecName: Full=Small ribosomal subunit protein eS19 {ECO:0000255|HAMAP-Rule:MF_01474};
GN   Name=rps19e {ECO:0000255|HAMAP-Rule:MF_01474};
GN   OrderedLocusNames=TK1276 {ECO:0000312|EMBL:BAD85465.1};
OS   Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)
OS   (Pyrococcus kodakaraensis (strain KOD1)).
OC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;
OC   Thermococcaceae; Thermococcus.
OX   NCBI_TaxID=69014;
```

Source SHA-256: `6db90196a1a395ff770ce2fe5f3dc8be7b57ed1244fe3114f10726e4eadae529`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JGN5?format=txt&versions=104)  
**Locator:** `lines 72-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 104 / 1.  
**Retrieved:** 2026-11-02T04:31:23.320142+00:00.  

```text
DR   GO; GO:0022627; C:cytosolic small ribosomal subunit; IBA:GO_Central.
```

Source SHA-256: `6db90196a1a395ff770ce2fe5f3dc8be7b57ed1244fe3114f10726e4eadae529`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 160585-160600`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0022627
name: cytosolic small ribosomal subunit
namespace: cellular_component
alt_id: GO:0005843
alt_id: GO:0009283
alt_id: GO:0030499
alt_id: GO:0030873
def: "The small subunit of a ribosome located in the cytosol." [GOC:mtg_sensu]
synonym: "30S ribosomal subunit" NARROW []
synonym: "40S ribosomal subunit" NARROW []
synonym: "eukaryotic ribosomal SSU" NARROW []
synonym: "prokaryotic small ribosomal subunit" NARROW []
is_a: GO:0015935 ! small ribosomal subunit
relationship: part_of GO:0022626 ! cytosolic ribosome

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 10. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
