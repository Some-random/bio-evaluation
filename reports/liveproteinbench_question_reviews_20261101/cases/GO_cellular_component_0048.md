# GO_cellular_component_0048

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRVLALSAVFLVASIIGMPAVAKEWQENKSWNAHFTEHKSQGVVVLWNENKQQGFTNNLKRANQAFLPASTFKIPNSLIALDLGVVKDEHQVFKWDGQTRDIATWNRDHNLITAMKYSVVPVYQEFARQIGEARMSKMLHAFDYGNEDISGNVDSFWLDGGIRISATEQISFLRKLYHNKLHVSERSQRIVKQAMLTEANGDYIIRAKTGYSTRIEPKIGWWVGWVELDDNVWFFAMNMDMPTSDGLGLRQAITKEVLKQEKIIP

[Multiple Choices]
A. spindle
B. apicoplast
C. early endosome membrane
D. plasma membrane
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

> The exact sequence matches the OXA-48 entry, which assigns GO:0005886 (plasma membrane) to it. This is a computational IEA:TreeGrafter annotation, not direct experimental localization evidence, so it supports the key as a GO annotation without establishing membrane residence experimentally.

Citations as saved: [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a bacterial export signal, making the eukaryotic spindle, apicoplast, and early-endosome options implausible. But export across the bacterial membrane does not by itself establish that the mature protein resides in that membrane.


**Missing item-specific fact**

> The protein-specific GO assignment of plasma membrane, or independent localization evidence supporting that assignment, is not supplied in the question.


**Reason**

> Sequence features can suggest bacterial export, but cannot reliably distinguish plasma-membrane residence from a soluble exported/periplasmic destination. Selecting D as the exact GO component therefore depends on the protein-specific annotation or equivalent external knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, D is the only one compatible with a bacterial protein. However, the choices omit the periplasm, a plausible destination for an exported bacterial enzyme, so the available options do not resolve the protein’s actual mature location.


### Important caveats

- Reviewer-only evidence matches the supplied sequence but was not available to the evaluated model.
- The supporting GO annotation is computationally inferred (IEA:TreeGrafter), not experimentally demonstrated.
- The identity of the author’s source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a bacterial export signal, making the eukaryotic spindle, apicoplast, and early-endosome options implausible. But export across the bacterial membrane does not by itself establish that the mature protein resides in that membrane.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific GO assignment of plasma membrane, or independent localization evidence supporting that assignment, is not supplied in the question.",
    "reason": "Sequence features can suggest bacterial export, but cannot reliably distinguish plasma-membrane residence from a soluble exported/periplasmic destination. Selecting D as the exact GO component therefore depends on the protein-specific annotation or equivalent external knowledge."
  },
  "case_id": "GO_cellular_component_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C3",
      "C4",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the OXA-48 entry, which assigns GO:0005886 (plasma membrane) to it. This is a computational IEA:TreeGrafter annotation, not direct experimental localization evidence, so it supports the key as a GO annotation without establishing membrane residence experimentally."
  },
  "important_caveats": [
    "Reviewer-only evidence matches the supplied sequence but was not available to the evaluated model.",
    "The supporting GO annotation is computationally inferred (IEA:TreeGrafter), not experimentally demonstrated.",
    "The identity of the author’s source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D is the only one compatible with a bacterial protein. However, the choices omit the periplasm, a plausible destination for an exported bacterial enzyme, so the available options do not resolve the protein’s actual mature location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the OXA-48 entry, which assigns GO:0005886 (plasma membrane) to it. This is a computational IEA:TreeGrafter annotation, not direct experimental localization evidence, so it supports the key as a GO annotation without establishing membrane residence experimentally.",
    "evidence_ids": ["C3", "C4", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a bacterial export signal, making the eukaryotic spindle, apicoplast, and early-endosome options implausible. But export across the bacterial membrane does not by itself establish that the mature protein resides in that membrane.",
    "missing_item_specific_fact": "The protein-specific GO assignment of plasma membrane, or independent localization evidence supporting that assignment, is not supplied in the question.",
    "reason": "Sequence features can suggest bacterial export, but cannot reliably distinguish plasma-membrane residence from a soluble exported/periplasmic destination. Selecting D as the exact GO component therefore depends on the protein-specific annotation or equivalent external knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D is the only one compatible with a bacterial protein. However, the choices omit the periplasm, a plausible destination for an exported bacterial enzyme, so the available options do not resolve the protein’s actual mature location."
  },
  "important_caveats": [
    "Reviewer-only evidence matches the supplied sequence but was not available to the evaluated model.",
    "The supporting GO annotation is computationally inferred (IEA:TreeGrafter), not experimentally demonstrated.",
    "The identity of the author’s source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q6XEC0 (Beta-lactamase OXA-48, Klebsiella pneumoniae) carries a GO:0005886 (plasma membrane) annotation (evidence C5, H6). However, the evidence code is IEA:TreeGrafter, a computational prediction rather than experimental localization data. The protein is flagged as a Precursor (C4/H1) with an N-terminal signal peptide, consistent with Sec-mediated export. In Gram-negative bacteria, beta-lactamases are periplasmic; GO:0005886 includes the NARROW synonym 'bacterial inner membrane,' making the annotation broadly defensible for a protein trafficked across the inner membrane, though 'periplasmic space' would be more precise. The key matches the sole available GO cellular-component annotation in the database.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C4](#evidence-c4), [H1](#evidence-h1), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three of the four options are exclusively eukaryotic structures: spindle (mitotic/meiotic microtubule array, GO:0005819), apicoplast (plastid organelle of apicomplexan parasites, GO:0020011), and early endosome membrane (eukaryotic endocytic pathway, GO:0031901). The sequence exhibits a canonical bacterial Sec-type signal peptide (MRVLALSAVFLVASIIGMPAVA↓KEW, with a hydrophobic h-region and AXA cleavage motif) followed by a soluble globular domain with no predicted transmembrane segments—hallmarks of a bacterially exported periplasmic enzyme. No eukaryotic-specific targeting motifs (e.g., nuclear localization signals, mitochondrial transit peptides, ER retention sequences) are present. Therefore, spindle, apicoplast, and early endosome membrane are biologically impossible for this protein, leaving plasma membrane (the bacterial inner/cytoplasmic membrane, per GO synonym 'bacterial inner membrane') as the only compartment among the choices that is compatible with a Sec-exported bacterial protein.


**Missing item-specific fact**

> None critical. Knowledge that spindle, apicoplast, and early endosome are eukaryotic-only structures, combined with recognition of the bacterial Sec signal peptide architecture, is sufficient to eliminate three options.


**Reason**

> A model with general cell-biology knowledge can reason: (1) the N-terminal hydrophobic stretch with an AXA cleavage motif is a bacterial Sec signal peptide; (2) the mature domain is a soluble enzyme fold with no transmembrane helices; (3) spindle, apicoplast, and early endosome membrane are structures that exist only in eukaryotes and cannot house a bacterially encoded, Sec-exported protein; (4) plasma membrane (synonymous with bacterial inner membrane in GO) is the only viable compartment. This chain of reasoning does not require memorizing the UniProt entry for Q6XEC0.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C are eukaryotic-specific compartments that are categorically incompatible with a bacterial protein bearing a Sec signal peptide. Only D (plasma membrane) is biologically plausible. While the protein is more precisely periplasmic rather than an integral membrane component, 'plasma membrane' (with its GO synonym 'bacterial inner membrane') is the closest and only defensible choice among the four.


### Important caveats

- The GO:0005886 annotation is IEA:TreeGrafter (computational), not experimental. No experimental subcellular localization study for OXA-48 is cited in the evidence.
- OXA-48 beta-lactamase is functionally periplasmic in Gram-negative bacteria; the 'plasma membrane' GO term is a broad approximation used by TreeGrafter rather than a precise experimental assignment.
- The reviewer-only UniProt accession (Q6XEC0) and its metadata were not available to the evaluated model; the reasoning argument relies solely on sequence features and general biology.
- The GO ontology snapshot used by the benchmark authors is unknown; the current ontology definitions cited here may differ slightly from those at construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three of the four options are exclusively eukaryotic structures: spindle (mitotic/meiotic microtubule array, GO:0005819), apicoplast (plastid organelle of apicomplexan parasites, GO:0020011), and early endosome membrane (eukaryotic endocytic pathway, GO:0031901). The sequence exhibits a canonical bacterial Sec-type signal peptide (MRVLALSAVFLVASIIGMPAVA↓KEW, with a hydrophobic h-region and AXA cleavage motif) followed by a soluble globular domain with no predicted transmembrane segments—hallmarks of a bacterially exported periplasmic enzyme. No eukaryotic-specific targeting motifs (e.g., nuclear localization signals, mitochondrial transit peptides, ER retention sequences) are present. Therefore, spindle, apicoplast, and early endosome membrane are biologically impossible for this protein, leaving plasma membrane (the bacterial inner/cytoplasmic membrane, per GO synonym 'bacterial inner membrane') as the only compartment among the choices that is compatible with a Sec-exported bacterial protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Knowledge that spindle, apicoplast, and early endosome are eukaryotic-only structures, combined with recognition of the bacterial Sec signal peptide architecture, is sufficient to eliminate three options.",
    "reason": "A model with general cell-biology knowledge can reason: (1) the N-terminal hydrophobic stretch with an AXA cleavage motif is a bacterial Sec signal peptide; (2) the mature domain is a soluble enzyme fold with no transmembrane helices; (3) spindle, apicoplast, and early endosome membrane are structures that exist only in eukaryotes and cannot house a bacterially encoded, Sec-exported protein; (4) plasma membrane (synonymous with bacterial inner membrane in GO) is the only viable compartment. This chain of reasoning does not require memorizing the UniProt entry for Q6XEC0."
  },
  "case_id": "GO_cellular_component_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C4",
      "H1",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q6XEC0 (Beta-lactamase OXA-48, Klebsiella pneumoniae) carries a GO:0005886 (plasma membrane) annotation (evidence C5, H6). However, the evidence code is IEA:TreeGrafter, a computational prediction rather than experimental localization data. The protein is flagged as a Precursor (C4/H1) with an N-terminal signal peptide, consistent with Sec-mediated export. In Gram-negative bacteria, beta-lactamases are periplasmic; GO:0005886 includes the NARROW synonym 'bacterial inner membrane,' making the annotation broadly defensible for a protein trafficked across the inner membrane, though 'periplasmic space' would be more precise. The key matches the sole available GO cellular-component annotation in the database."
  },
  "important_caveats": [
    "The GO:0005886 annotation is IEA:TreeGrafter (computational), not experimental. No experimental subcellular localization study for OXA-48 is cited in the evidence.",
    "OXA-48 beta-lactamase is functionally periplasmic in Gram-negative bacteria; the 'plasma membrane' GO term is a broad approximation used by TreeGrafter rather than a precise experimental assignment.",
    "The reviewer-only UniProt accession (Q6XEC0) and its metadata were not available to the evaluated model; the reasoning argument relies solely on sequence features and general biology.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the current ontology definitions cited here may differ slightly from those at construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are eukaryotic-specific compartments that are categorically incompatible with a bacterial protein bearing a Sec signal peptide. Only D (plasma membrane) is biologically plausible. While the protein is more precisely periplasmic rather than an integral membrane component, 'plasma membrane' (with its GO synonym 'bacterial inner membrane') is the closest and only defensible choice among the four."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q6XEC0 (Beta-lactamase OXA-48, Klebsiella pneumoniae) carries a GO:0005886 (plasma membrane) annotation (evidence C5, H6). However, the evidence code is IEA:TreeGrafter, a computational prediction rather than experimental localization data. The protein is flagged as a Precursor (C4/H1) with an N-terminal signal peptide, consistent with Sec-mediated export. In Gram-negative bacteria, beta-lactamases are periplasmic; GO:0005886 includes the NARROW synonym 'bacterial inner membrane,' making the annotation broadly defensible for a protein trafficked across the inner membrane, though 'periplasmic space' would be more precise. The key matches the sole available GO cellular-component annotation in the database.",
    "evidence_ids": ["C5", "H6", "C4", "H1", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three of the four options are exclusively eukaryotic structures: spindle (mitotic/meiotic microtubule array, GO:0005819), apicoplast (plastid organelle of apicomplexan parasites, GO:0020011), and early endosome membrane (eukaryotic endocytic pathway, GO:0031901). The sequence exhibits a canonical bacterial Sec-type signal peptide (MRVLALSAVFLVASIIGMPAVA↓KEW, with a hydrophobic h-region and AXA cleavage motif) followed by a soluble globular domain with no predicted transmembrane segments—hallmarks of a bacterially exported periplasmic enzyme. No eukaryotic-specific targeting motifs (e.g., nuclear localization signals, mitochondrial transit peptides, ER retention sequences) are present. Therefore, spindle, apicoplast, and early endosome membrane are biologically impossible for this protein, leaving plasma membrane (the bacterial inner/cytoplasmic membrane, per GO synonym 'bacterial inner membrane') as the only compartment among the choices that is compatible with a Sec-exported bacterial protein.",
    "missing_item_specific_fact": "None critical. Knowledge that spindle, apicoplast, and early endosome are eukaryotic-only structures, combined with recognition of the bacterial Sec signal peptide architecture, is sufficient to eliminate three options.",
    "reason": "A model with general cell-biology knowledge can reason: (1) the N-terminal hydrophobic stretch with an AXA cleavage motif is a bacterial Sec signal peptide; (2) the mature domain is a soluble enzyme fold with no transmembrane helices; (3) spindle, apicoplast, and early endosome membrane are structures that exist only in eukaryotes and cannot house a bacterially encoded, Sec-exported protein; (4) plasma membrane (synonymous with bacterial inner membrane in GO) is the only viable compartment. This chain of reasoning does not require memorizing the UniProt entry for Q6XEC0."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C are eukaryotic-specific compartments that are categorically incompatible with a bacterial protein bearing a Sec signal peptide. Only D (plasma membrane) is biologically plausible. While the protein is more precisely periplasmic rather than an integral membrane component, 'plasma membrane' (with its GO synonym 'bacterial inner membrane') is the closest and only defensible choice among the four."
  },
  "important_caveats": [
    "The GO:0005886 annotation is IEA:TreeGrafter (computational), not experimental. No experimental subcellular localization study for OXA-48 is cited in the evidence.",
    "OXA-48 beta-lactamase is functionally periplasmic in Gram-negative bacteria; the 'plasma membrane' GO term is a broad approximation used by TreeGrafter rather than a precise experimental assignment.",
    "The reviewer-only UniProt accession (Q6XEC0) and its metadata were not available to the evaluated model; the reasoning argument relies solely on sequence features and general biology.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the current ontology definitions cited here may differ slightly from those at construction time."
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

**Accession:** `Q6XEC0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 136. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAP70012.1","source":"EMBL"}],"lineage":["Bacteria","Pseudomonadati","Pseudomonadota","Gammaproteobacteria","Enterobacterales","Enterobacteriaceae","Klebsiella","Klebsiella pneumoniae complex"],"scientificName":"Klebsiella pneumoniae","taxonId":573}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"14693513","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"19477418","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"27073009","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38161376","source":"PubMed"}],"value":"3.5.2.6"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"14693513","source":"PubMed"}],"value":"Beta-lactamase OXA-48"}}}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6XEC0.json)  
**Locator:** `/uniProtKBCrossReferences/257`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.821901+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `7a7b0d77f1f923e008e8fc5048255b02d3f9e2d1a0d4b680f7c01328fb477d33`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 1-28`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
ID   BLO48_KLEPN             Reviewed;         265 AA.
AC   Q6XEC0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2004, sequence version 1.
DT   28-JAN-2026, entry version 136.
DE   RecName: Full=Beta-lactamase OXA-48 {ECO:0000255|RuleBase:RU361140, ECO:0000303|PubMed:14693513};
DE            EC=3.5.2.6 {ECO:0000255|RuleBase:RU361140, ECO:0000269|PubMed:14693513, ECO:0000269|PubMed:19477418, ECO:0000269|PubMed:27073009, ECO:0000269|PubMed:38161376};
DE   Flags: Precursor;
GN   Name=OXA-48 {ECO:0000303|PubMed:14693513};
GN   Synonyms=bla OXA-48 {ECO:0000312|EMBL:AAP70012.1},
GN   bla_4 {ECO:0000312|EMBL:SWV87943.1},
GN   blaOXA-48 {ECO:0000303|PubMed:14693513, ECO:0000312|EMBL:AEV46197.1};
GN   ORFNames=KPE71T_00045 {ECO:0000312|EMBL:AGW25497.1},
GN   SAMEA3727706_05517 {ECO:0000312|EMBL:SWV87943.1};
OS   Klebsiella pneumoniae.
OG   Plasmid pJEG011 {ECO:0000312|EMBL:AGJ73905.1},
OG   Plasmid pKP112 {ECO:0000312|EMBL:CRN12897.1},
OG   Plasmid pKPoxa-48N1 {ECO:0000312|EMBL:AGL12970.1},
OG   Plasmid pKPoxa-48N2 {ECO:0000312|EMBL:AGL13044.1},
OG   Plasmid pKpn-E1.Nr7 {ECO:0000312|EMBL:AKA86737.1},
OG   Plasmid pOXA-48 {ECO:0000312|EMBL:AEV46197.1},
OG   Plasmid pOXA-48E1 {ECO:0000312|EMBL:AKJ18670.1},
OG   Plasmid unnamed {ECO:0000312|EMBL:AGW25497.1}, and
OG   Plasmid P1 {ECO:0000312|EMBL:CAH5611484.1}.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Enterobacteriaceae; Klebsiella/Raoultella group;
OC   Klebsiella; Klebsiella pneumoniae complex.
OX   NCBI_TaxID=573 {ECO:0000312|EMBL:AAP70012.1};
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6XEC0?format=txt&versions=136)  
**Locator:** `lines 588-588`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 1.  
**Retrieved:** 2026-11-02T04:31:51.921802+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.
```

Source SHA-256: `748d62da6dbda55945d3952c2004e283e2a5bc809be9fd394e2b1d0eff688b3a`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
