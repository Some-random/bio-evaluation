# GO_molecular_function_0098

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — peptidyl-tRNA hydrolase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAIKLIVGLANPGAEYAATRHNAGAWYVDLLAERLRAPLREEPKFFGYTSRITLEGEDVRLLVPTTFMNLSGKAVGAMASFYRIQPDEILVAHDELDLPPGVAKFKLGGGHGGHNGLKDIISKLGNNPNFHRLRVGIGHPGDKNKVVGFVLGKPPVSEQKLIDEAIDEAARCTELWFKEGLAKATSRLHTFKAQ

[Multiple Choices]
A. peptidyl-tRNA hydrolase activity
B. transcription coactivator activity
C. polyubiquitin modification-dependent protein binding
D. alpha-1,6-mannosyltransferase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches a Salmonella peptidyl-tRNA hydrolase entry. Its protein name and canonical function are assigned by a HAMAP rule, and the matching record carries the corresponding GO annotation by UniProtKB-UniRule. The record also reports experimental tRNA deacetylation, which supports related tRNA-hydrolyzing activity, though the classical peptidyl-tRNA hydrolase annotation is rule-based rather than shown here as a direct experimental assay.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C10](#evidence-c10), [H4](#evidence-h4), [H6](#evidence-h6), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a compact, apparently soluble protein, which makes a membrane-associated mannosyltransferase and eukaryotic transcription or ubiquitin-binding functions less plausible. But those broad features do not identify peptidyl-tRNA hydrolase activity; that requires recognizing its specific protein family or consulting a protein-specific annotation.


**Missing item-specific fact**

> The sequence's identity as a bacterial Pth-family enzyme, or a reliable family/profile match linking its conserved residues to peptidyl-tRNA hydrolase activity, is not supplied.


**Reason**

> The choices allow broad plausibility judgments from sequence characteristics, but those are not enough to establish the specific catalytic function. Exact-sequence recognition or family annotation would supply the decisive fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports option A; the other listed functions are not comparably supported.


### Important caveats

- The reviewer evidence is not information supplied to the evaluated model and does not make the task reasoning-supported.
- The canonical peptidyl-tRNA hydrolase assignment is computationally annotated by HAMAP/UniRule; the cited experimental evidence specifically describes tRNA deacetylation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a compact, apparently soluble protein, which makes a membrane-associated mannosyltransferase and eukaryotic transcription or ubiquitin-binding functions less plausible. But those broad features do not identify peptidyl-tRNA hydrolase activity; that requires recognizing its specific protein family or consulting a protein-specific annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity as a bacterial Pth-family enzyme, or a reliable family/profile match linking its conserved residues to peptidyl-tRNA hydrolase activity, is not supplied.",
    "reason": "The choices allow broad plausibility judgments from sequence characteristics, but those are not enough to establish the specific catalytic function. Exact-sequence recognition or family annotation would supply the decisive fact."
  },
  "case_id": "GO_molecular_function_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "C10",
      "H4",
      "H6",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a Salmonella peptidyl-tRNA hydrolase entry. Its protein name and canonical function are assigned by a HAMAP rule, and the matching record carries the corresponding GO annotation by UniProtKB-UniRule. The record also reports experimental tRNA deacetylation, which supports related tRNA-hydrolyzing activity, though the classical peptidyl-tRNA hydrolase annotation is rule-based rather than shown here as a direct experimental assay."
  },
  "important_caveats": [
    "The reviewer evidence is not information supplied to the evaluated model and does not make the task reasoning-supported.",
    "The canonical peptidyl-tRNA hydrolase assignment is computationally annotated by HAMAP/UniRule; the cited experimental evidence specifically describes tRNA deacetylation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports option A; the other listed functions are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a Salmonella peptidyl-tRNA hydrolase entry. Its protein name and canonical function are assigned by a HAMAP rule, and the matching record carries the corresponding GO annotation by UniProtKB-UniRule. The record also reports experimental tRNA deacetylation, which supports related tRNA-hydrolyzing activity, though the classical peptidyl-tRNA hydrolase annotation is rule-based rather than shown here as a direct experimental assay.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "C10", "H4", "H6", "H9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a compact, apparently soluble protein, which makes a membrane-associated mannosyltransferase and eukaryotic transcription or ubiquitin-binding functions less plausible. But those broad features do not identify peptidyl-tRNA hydrolase activity; that requires recognizing its specific protein family or consulting a protein-specific annotation.",
    "missing_item_specific_fact": "The sequence's identity as a bacterial Pth-family enzyme, or a reliable family/profile match linking its conserved residues to peptidyl-tRNA hydrolase activity, is not supplied.",
    "reason": "The choices allow broad plausibility judgments from sequence characteristics, but those are not enough to establish the specific catalytic function. Exact-sequence recognition or family annotation would supply the decisive fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports option A; the other listed functions are not comparably supported."
  },
  "important_caveats": [
    "The reviewer evidence is not information supplied to the evaluated model and does not make the task reasoning-supported.",
    "The canonical peptidyl-tRNA hydrolase assignment is computationally annotated by HAMAP/UniRule; the cited experimental evidence specifically describes tRNA deacetylation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A0F6B281 (PTH_SALT1, Salmonella typhimurium 14028s) exactly (SHA256 match confirmed). The entry is annotated with GO:0004045 (peptidyl-tRNA hydrolase activity) via UniRule/HAMAP-Rule MF_00083, EC 3.1.1.29, and supported by experimental references (PubMed 27264868, 29777131). The GO annotation evidence code is IEA:UniProtKB-UniRule (computational), but the catalytic activity is corroborated by ECO:0000269/ECO:0000305 experimental evidence from published papers.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H1](#evidence-h1), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 194-residue sequence lacks eukaryotic-specific domains and exhibits characteristics of a small bacterial protein (no signal peptide, no transmembrane segments, no eukaryotic regulatory motifs). Options B (transcription coactivator activity), C (polyubiquitin modification-dependent protein binding), and D (alpha-1,6-mannosyltransferase activity) describe functions intrinsic to eukaryotic systems: coactivators require eukaryotic transcription machinery (Mediator, chromatin remodeling); polyubiquitin binding requires the ubiquitin-proteasome system absent in bacteria; alpha-1,6-mannosyltransferase participates in eukaryotic N-glycan biosynthesis. Peptidyl-tRNA hydrolase (Pth) is a universally conserved enzyme present in bacteria, making A the only function biologically plausible for this bacterial protein.


**Missing item-specific fact**

> Positive identification of Pth-specific catalytic motifs (e.g., the conserved His-Asp catalytic dyad region) from the raw sequence alone would require specialized structural knowledge of the Pth fold, but the elimination-based reasoning through eukaryotic vs. bacterial function is sufficient among the given choices.


**Reason**

> A model with general biological knowledge can reason that a small bacterial protein cannot perform eukaryotic-specific functions (ubiquitin binding, eukaryotic transcription coactivation, N-glycosylation), leaving peptidyl-tRNA hydrolase activity as the only viable option. This is general biological reasoning, not item-specific memorization, though the positive confirmation of Pth from sequence motifs would require specialized knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are unambiguously eukaryotic functions incompatible with a bacterial protein of this size and composition. Option A is the only function present in both prokaryotes and eukaryotes among the choices, making the answer uniquely determined by biological context.


### Important caveats

- The primary GO annotation (GO:0004045) carries evidence code IEA:UniProtKB-UniRule, meaning the functional assignment is computational (HAMAP-Rule MF_00083), though corroborated by experimental papers.
- The reasoning path to the answer relies heavily on elimination of eukaryotic-specific functions rather than positive recognition of Pth catalytic motifs from sequence.
- The sequence is from Salmonella typhimurium strain 14028s; the entry was first released in 2025 and the benchmark author's source snapshot is unknown.
- The identity of this protein was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 194-residue sequence lacks eukaryotic-specific domains and exhibits characteristics of a small bacterial protein (no signal peptide, no transmembrane segments, no eukaryotic regulatory motifs). Options B (transcription coactivator activity), C (polyubiquitin modification-dependent protein binding), and D (alpha-1,6-mannosyltransferase activity) describe functions intrinsic to eukaryotic systems: coactivators require eukaryotic transcription machinery (Mediator, chromatin remodeling); polyubiquitin binding requires the ubiquitin-proteasome system absent in bacteria; alpha-1,6-mannosyltransferase participates in eukaryotic N-glycan biosynthesis. Peptidyl-tRNA hydrolase (Pth) is a universally conserved enzyme present in bacteria, making A the only function biologically plausible for this bacterial protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of Pth-specific catalytic motifs (e.g., the conserved His-Asp catalytic dyad region) from the raw sequence alone would require specialized structural knowledge of the Pth fold, but the elimination-based reasoning through eukaryotic vs. bacterial function is sufficient among the given choices.",
    "reason": "A model with general biological knowledge can reason that a small bacterial protein cannot perform eukaryotic-specific functions (ubiquitin binding, eukaryotic transcription coactivation, N-glycosylation), leaving peptidyl-tRNA hydrolase activity as the only viable option. This is general biological reasoning, not item-specific memorization, though the positive confirmation of Pth from sequence motifs would require specialized knowledge."
  },
  "case_id": "GO_molecular_function_0098",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "H1",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A0F6B281 (PTH_SALT1, Salmonella typhimurium 14028s) exactly (SHA256 match confirmed). The entry is annotated with GO:0004045 (peptidyl-tRNA hydrolase activity) via UniRule/HAMAP-Rule MF_00083, EC 3.1.1.29, and supported by experimental references (PubMed 27264868, 29777131). The GO annotation evidence code is IEA:UniProtKB-UniRule (computational), but the catalytic activity is corroborated by ECO:0000269/ECO:0000305 experimental evidence from published papers."
  },
  "important_caveats": [
    "The primary GO annotation (GO:0004045) carries evidence code IEA:UniProtKB-UniRule, meaning the functional assignment is computational (HAMAP-Rule MF_00083), though corroborated by experimental papers.",
    "The reasoning path to the answer relies heavily on elimination of eukaryotic-specific functions rather than positive recognition of Pth catalytic motifs from sequence.",
    "The sequence is from Salmonella typhimurium strain 14028s; the entry was first released in 2025 and the benchmark author's source snapshot is unknown.",
    "The identity of this protein was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are unambiguously eukaryotic functions incompatible with a bacterial protein of this size and composition. Option A is the only function present in both prokaryotes and eukaryotes among the choices, making the answer uniquely determined by biological context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0098",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A0F6B281 (PTH_SALT1, Salmonella typhimurium 14028s) exactly (SHA256 match confirmed). The entry is annotated with GO:0004045 (peptidyl-tRNA hydrolase activity) via UniRule/HAMAP-Rule MF_00083, EC 3.1.1.29, and supported by experimental references (PubMed 27264868, 29777131). The GO annotation evidence code is IEA:UniProtKB-UniRule (computational), but the catalytic activity is corroborated by ECO:0000269/ECO:0000305 experimental evidence from published papers.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "C10", "H1", "H4", "H5", "H6", "H7", "H8", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 194-residue sequence lacks eukaryotic-specific domains and exhibits characteristics of a small bacterial protein (no signal peptide, no transmembrane segments, no eukaryotic regulatory motifs). Options B (transcription coactivator activity), C (polyubiquitin modification-dependent protein binding), and D (alpha-1,6-mannosyltransferase activity) describe functions intrinsic to eukaryotic systems: coactivators require eukaryotic transcription machinery (Mediator, chromatin remodeling); polyubiquitin binding requires the ubiquitin-proteasome system absent in bacteria; alpha-1,6-mannosyltransferase participates in eukaryotic N-glycan biosynthesis. Peptidyl-tRNA hydrolase (Pth) is a universally conserved enzyme present in bacteria, making A the only function biologically plausible for this bacterial protein.",
    "missing_item_specific_fact": "Positive identification of Pth-specific catalytic motifs (e.g., the conserved His-Asp catalytic dyad region) from the raw sequence alone would require specialized structural knowledge of the Pth fold, but the elimination-based reasoning through eukaryotic vs. bacterial function is sufficient among the given choices.",
    "reason": "A model with general biological knowledge can reason that a small bacterial protein cannot perform eukaryotic-specific functions (ubiquitin binding, eukaryotic transcription coactivation, N-glycosylation), leaving peptidyl-tRNA hydrolase activity as the only viable option. This is general biological reasoning, not item-specific memorization, though the positive confirmation of Pth from sequence motifs would require specialized knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are unambiguously eukaryotic functions incompatible with a bacterial protein of this size and composition. Option A is the only function present in both prokaryotes and eukaryotes among the choices, making the answer uniquely determined by biological context."
  },
  "important_caveats": [
    "The primary GO annotation (GO:0004045) carries evidence code IEA:UniProtKB-UniRule, meaning the functional assignment is computational (HAMAP-Rule MF_00083), though corroborated by experimental papers.",
    "The reasoning path to the answer relies heavily on elimination of eukaryotic-specific functions rather than positive recognition of Pth catalytic motifs from sequence.",
    "The sequence is from Salmonella typhimurium strain 14028s; the entry was first released in 2025 and the benchmark author's source snapshot is unknown.",
    "The identity of this protein was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence."
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

**Accession:** `A0A0F6B281` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 42. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
"A0A0F6B281"
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"3.1.1.29"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"Peptidyl-tRNA hydrolase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"Pth"}]}}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"Hydrolyzes ribosome-free peptidyl-tRNAs (with 1 or more amino acids incorporated), which drop off the ribosome during protein synthesis, or as a result of ribosome stalling"}]}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"value":"Catalyzes the release of premature peptidyl moieties from peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits, and thus maintains levels of free tRNAs and 50S ribosomes"}]}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27264868","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29777131","source":"PubMed"}],"value":"Expression in lag phase counteracts expression of tRNA-acetylating toxin TacT, deacetylates bulk tRNA modified by TacT in vitro"}]}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.1.1.29","evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00083","source":"HAMAP-Rule"}],"name":"an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino acid + a tRNA + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:54448"},{"database":"Rhea","id":"RHEA-COMP:10123"},{"database":"Rhea","id":"RHEA-COMP:13883"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:59874"},{"database":"ChEBI","id":"CHEBI:78442"},{"database":"ChEBI","id":"CHEBI:138191"}]}}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"27264868","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"29777131","source":"PubMed"}],"name":"N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81979"},{"database":"Rhea","id":"RHEA-COMP:9664"},{"database":"Rhea","id":"RHEA-COMP:19766"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:61887"},{"database":"ChEBI","id":"CHEBI:78442"},{"database":"ChEBI","id":"CHEBI:232036"}]}}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6B281.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:01.196338+00:00.  

```json
{"database":"GO","id":"GO:0004045","properties":[{"key":"GoTerm","value":"F:peptidyl-tRNA hydrolase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniRule"}]}
```

Source SHA-256: `99ef3361027bbc1bd059e6fe036660533ee139a5048dd1899d1a3c331a969aa0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
ID   PTH_SALT1               Reviewed;         194 AA.
AC   A0A0F6B281;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   24-JUN-2015, sequence version 1.
DT   28-JAN-2026, entry version 42.
DE   RecName: Full=Peptidyl-tRNA hydrolase {ECO:0000255|HAMAP-Rule:MF_00083};
DE            Short=Pth {ECO:0000255|HAMAP-Rule:MF_00083};
DE            EC=3.1.1.29 {ECO:0000255|HAMAP-Rule:MF_00083};
GN   Name=pth {ECO:0000255|HAMAP-Rule:MF_00083, ECO:0000312|EMBL:ACY88619.1};
GN   OrderedLocusNames=STM14_2156 {ECO:0000312|EMBL:ACY88619.1};
OS   Salmonella typhimurium (strain 14028s / SGSC 2262).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Enterobacteriaceae; Salmonella.
OX   NCBI_TaxID=588858;
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 41-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
CC   -!- FUNCTION: Hydrolyzes ribosome-free peptidyl-tRNAs (with 1 or more amino
CC       acids incorporated), which drop off the ribosome during protein
CC       synthesis, or as a result of ribosome stalling. {ECO:0000255|HAMAP-
CC       Rule:MF_00083}.
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 45-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the release of premature peptidyl moieties from
CC       peptidyl-tRNA molecules trapped in stalled 50S ribosomal subunits, and
CC       thus maintains levels of free tRNAs and 50S ribosomes.
CC       {ECO:0000255|HAMAP-Rule:MF_00083}.
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 49-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
CC   -!- FUNCTION: Expression in lag phase counteracts expression of tRNA-
CC       acetylating toxin TacT, deacetylates bulk tRNA modified by TacT in
CC       vitro. {ECO:0000269|PubMed:27264868, ECO:0000269|PubMed:29777131}.
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 52-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an N-acyl-L-alpha-aminoacyl-tRNA + H2O = an N-acyl-L-amino
CC         acid + a tRNA + H(+); Xref=Rhea:RHEA:54448, Rhea:RHEA-COMP:10123,
CC         Rhea:RHEA-COMP:13883, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:59874, ChEBI:CHEBI:78442, ChEBI:CHEBI:138191;
CC         EC=3.1.1.29; Evidence={ECO:0000255|HAMAP-Rule:MF_00083};
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 58-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N-acetylglycyl-tRNA(Gly) + H2O = N-acetylglycine + tRNA(Gly) +
CC         H(+); Xref=Rhea:RHEA:81979, Rhea:RHEA-COMP:9664, Rhea:RHEA-
CC         COMP:19766, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:61887,
CC         ChEBI:CHEBI:78442, ChEBI:CHEBI:232036;
CC         Evidence={ECO:0000305|PubMed:27264868, ECO:0000305|PubMed:29777131};
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6B281?format=txt&versions=42)  
**Locator:** `lines 83-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 42 / 1.  
**Retrieved:** 2026-11-02T04:24:05.242925+00:00.  

```text
DR   GO; GO:0004045; F:peptidyl-tRNA hydrolase activity; IEA:UniProtKB-UniRule.
```

Source SHA-256: `60b2125307db6a1a0373bc7d2279f21c78a94c37b3be59796a932c5d6fc020f9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 98. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
