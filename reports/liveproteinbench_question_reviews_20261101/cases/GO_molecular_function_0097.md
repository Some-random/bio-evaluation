# GO_molecular_function_0097

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — zinc ion binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MESMMAAHPMYMMQYQYDNRQHAHYAHLPSQQPMAFYPAVPMVPSTPTYSRPASACSQPAMQSMKQMPMTSYPSAMTPMASPQPMARRSNIVLETEACDWEGKRHQAHGIYYPSTPPLSSSGSAISSPESCDMLSTPMNPMFSGLDSIESIKPEVNSPESFPVLEWTSCASPPMTPVYLNNVNNNLHSKQNLRPAPTSSCSPELAPAVSACPSLSPSPVPQTRSFTSETSFCDPRNLTVGNVTLGLEPASLSTETLVAQADNSFVFVAPQAAPTWDAISELESEEDFVKGLVNLDDSKSDAQGTRTRASSDAVSLNFDEVEAFPLLPTAHTHSDDDCHKSKRQRTCGGPKMDSATNESASSAAAPSSEQQQQPKSSDVPSNEETKSNSGASTNSDGTGLPAPTSRRGRKQSLTEDPSKAFKCELCDRRFRRQEHLKRHYRSLHTQDKPFECNECGKKFSRSDNLTQHARTHGSGAIPLNIMGEEDLAAAAANGYMHPPQHMYSMVPNVPTLPDYNSYGKVLFQIAAEVPGSASDYSDDGSERKRKRTD

[Multiple Choices]
A. aspartate-semialdehyde dehydrogenase activity
B. zinc ion binding
C. FAD binding
D. nucleotide binding
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

> The sequence contains C2H2-type zinc-finger motifs, consistent with zinc ion binding. The matched UniProt entry also annotates zinc ion binding, though that annotation is IEA:UniProtKB-KW rather than direct evidence of a zinc-binding measurement.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence's C-terminal region contains Cys/His-rich C2H2-type zinc-finger motifs, a recognizable sequence feature that supports zinc coordination and distinguishes zinc ion binding from the listed enzyme, FAD-binding, and nucleotide-binding alternatives.


**Missing item-specific fact**

> No protein-specific external fact is needed to make this sequence-based inference, although direct experimental confirmation of zinc binding is not supplied.


**Reason**

> The relevant motif is visible in the supplied sequence and provides a concrete biological basis for selecting B; this is not merely recognition of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Of the listed choices, zinc ion binding is the one supported by the sequence's zinc-finger motifs. DNA-binding transcription factor activity may describe the protein but is not offered.


### Important caveats

- The matched database annotation is computational/keyword-based; it should not be represented as a direct experimental zinc-binding assay.
- The reviewer-only evidence identifies the protein as a transcription factor, but that identity is not needed for the sequence-based distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's C-terminal region contains Cys/His-rich C2H2-type zinc-finger motifs, a recognizable sequence feature that supports zinc coordination and distinguishes zinc ion binding from the listed enzyme, FAD-binding, and nucleotide-binding alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific external fact is needed to make this sequence-based inference, although direct experimental confirmation of zinc binding is not supplied.",
    "reason": "The relevant motif is visible in the supplied sequence and provides a concrete biological basis for selecting B; this is not merely recognition of a database entry."
  },
  "case_id": "GO_molecular_function_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence contains C2H2-type zinc-finger motifs, consistent with zinc ion binding. The matched UniProt entry also annotates zinc ion binding, though that annotation is IEA:UniProtKB-KW rather than direct evidence of a zinc-binding measurement."
  },
  "important_caveats": [
    "The matched database annotation is computational/keyword-based; it should not be represented as a direct experimental zinc-binding assay.",
    "The reviewer-only evidence identifies the protein as a transcription factor, but that identity is not needed for the sequence-based distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Of the listed choices, zinc ion binding is the one supported by the sequence's zinc-finger motifs. DNA-binding transcription factor activity may describe the protein but is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence contains C2H2-type zinc-finger motifs, consistent with zinc ion binding. The matched UniProt entry also annotates zinc ion binding, though that annotation is IEA:UniProtKB-KW rather than direct evidence of a zinc-binding measurement.",
    "evidence_ids": ["C1", "C4", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence's C-terminal region contains Cys/His-rich C2H2-type zinc-finger motifs, a recognizable sequence feature that supports zinc coordination and distinguishes zinc ion binding from the listed enzyme, FAD-binding, and nucleotide-binding alternatives.",
    "missing_item_specific_fact": "No protein-specific external fact is needed to make this sequence-based inference, although direct experimental confirmation of zinc binding is not supplied.",
    "reason": "The relevant motif is visible in the supplied sequence and provides a concrete biological basis for selecting B; this is not merely recognition of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Of the listed choices, zinc ion binding is the one supported by the sequence's zinc-finger motifs. DNA-binding transcription factor activity may describe the protein but is not offered."
  },
  "important_caveats": [
    "The matched database annotation is computational/keyword-based; it should not be represented as a direct experimental zinc-binding assay.",
    "The reviewer-only evidence identifies the protein as a transcription factor, but that identity is not needed for the sequence-based distinction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is UniProt G4NBR8, C2H2-type transcription factor MSN2 from Magnaporthe oryzae. The UniProt entry annotates GO:0008270 (zinc ion binding) with evidence code IEA:UniProtKB-KW, and the protein is explicitly described as a 'C2H2-type transcription factor' and 'putative zinc-finger protein' (PubMed:24405033 title). The C2H2 zinc finger motif is identifiable in the sequence (…CNECGKKFSRSDNLTQHARTH…), which coordinates Zn²⁺. Among the four options, zinc ion binding is the only molecular function consistent with a zinc-finger transcription factor: the protein is not an enzyme (rules out A), not a flavoprotein (rules out C), and does not bind free nucleotides (rules out D, per GO:0000166 definition). The annotation is keyword-inferred (IEA), but the C2H2 structural motif is a well-characterized zinc-coordinating domain, providing strong structural support.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5), [H8](#evidence-h8), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C2H2 zinc finger motif (C-x2-4-C-x12-H-x3-5-H) is identifiable in the supplied sequence at approximately residues 390–415 (…PFECNECGKKFSRSDNLTQHARTHGSG…). A model with standard knowledge of protein structural motifs can recognize this as a zinc-coordinating C2H2 domain. The protein's overall character—a long, serine/threonine-rich transcription factor with a single C2H2 DNA-binding domain and no enzymatic motifs (no Rossmann fold, no FAD-binding GXGXXG, no aspartate-semialdehyde dehydrogenase catalytic residues)—allows elimination of A (enzyme), C (flavoprotein cofactor), and D (free nucleotide binding, which GO:0000166 defines as binding to free nucleotides, not DNA). Zinc ion binding (B) is the only option consistent with the identified C2H2 motif and the absence of catalytic or cofactor-binding features.


**Missing item-specific fact**

> None critical. The C2H2 motif is directly visible in the sequence, and its zinc-coordinating role is standard textbook knowledge. The protein's identity as MSN2 could be looked up, but is not required to identify the zinc finger and eliminate the other options.


**Reason**

> The C2H2 zinc finger pattern is recognizable from the sequence itself, and general biological knowledge about zinc finger structure and the definitions of the GO terms (especially that GO:0000166 nucleotide binding refers to free nucleotides, not DNA) provide a concrete reasoning path to select B over A, C, and D. No protein-specific experimental measurement or obscure annotation is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein's true primary molecular function is DNA-binding transcription factor activity (GO:0003700), which is not offered. Among the four provided choices, zinc ion binding (B) is the only one structurally and functionally consistent with a C2H2 zinc-finger transcription factor. Option D (nucleotide binding) might superficially seem relevant because DNA is a nucleotide polymer, but GO:0000166 explicitly defines nucleotide binding as binding to free nucleotides (e.g., ATP, GTP), not to polymeric DNA. Options A and C require enzymatic/flavoprotein features entirely absent from this sequence. No genuine ambiguity exists among the choices.


### Important caveats

- The zinc ion binding annotation (GO:0008270) carries evidence code IEA:UniProtKB-KW (keyword-based inference), not direct experimental zinc-binding measurement. However, the C2H2 motif's zinc coordination is an established structural fact.
- The protein's primary molecular function is arguably DNA-binding transcription factor activity (GO:0003700, also IEA:TreeGrafter), which is not among the options. The question asks to select the best option from those given, and B is the best fit.
- The GO terms for options A, C, and D have no term_ids matched to this protein's annotation, further confirming they are not applicable.
- The sequence is 548 aa and matches the UniProt canonical sequence exactly (SHA-256 confirmed in both current and historical snapshots).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C2H2 zinc finger motif (C-x2-4-C-x12-H-x3-5-H) is identifiable in the supplied sequence at approximately residues 390–415 (…PFECNECGKKFSRSDNLTQHARTHGSG…). A model with standard knowledge of protein structural motifs can recognize this as a zinc-coordinating C2H2 domain. The protein's overall character—a long, serine/threonine-rich transcription factor with a single C2H2 DNA-binding domain and no enzymatic motifs (no Rossmann fold, no FAD-binding GXGXXG, no aspartate-semialdehyde dehydrogenase catalytic residues)—allows elimination of A (enzyme), C (flavoprotein cofactor), and D (free nucleotide binding, which GO:0000166 defines as binding to free nucleotides, not DNA). Zinc ion binding (B) is the only option consistent with the identified C2H2 motif and the absence of catalytic or cofactor-binding features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The C2H2 motif is directly visible in the sequence, and its zinc-coordinating role is standard textbook knowledge. The protein's identity as MSN2 could be looked up, but is not required to identify the zinc finger and eliminate the other options.",
    "reason": "The C2H2 zinc finger pattern is recognizable from the sequence itself, and general biological knowledge about zinc finger structure and the definitions of the GO terms (especially that GO:0000166 nucleotide binding refers to free nucleotides, not DNA) provide a concrete reasoning path to select B over A, C, and D. No protein-specific experimental measurement or obscure annotation is needed."
  },
  "case_id": "GO_molecular_function_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5",
      "H8",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein is UniProt G4NBR8, C2H2-type transcription factor MSN2 from Magnaporthe oryzae. The UniProt entry annotates GO:0008270 (zinc ion binding) with evidence code IEA:UniProtKB-KW, and the protein is explicitly described as a 'C2H2-type transcription factor' and 'putative zinc-finger protein' (PubMed:24405033 title). The C2H2 zinc finger motif is identifiable in the sequence (…CNECGKKFSRSDNLTQHARTH…), which coordinates Zn²⁺. Among the four options, zinc ion binding is the only molecular function consistent with a zinc-finger transcription factor: the protein is not an enzyme (rules out A), not a flavoprotein (rules out C), and does not bind free nucleotides (rules out D, per GO:0000166 definition). The annotation is keyword-inferred (IEA), but the C2H2 structural motif is a well-characterized zinc-coordinating domain, providing strong structural support."
  },
  "important_caveats": [
    "The zinc ion binding annotation (GO:0008270) carries evidence code IEA:UniProtKB-KW (keyword-based inference), not direct experimental zinc-binding measurement. However, the C2H2 motif's zinc coordination is an established structural fact.",
    "The protein's primary molecular function is arguably DNA-binding transcription factor activity (GO:0003700, also IEA:TreeGrafter), which is not among the options. The question asks to select the best option from those given, and B is the best fit.",
    "The GO terms for options A, C, and D have no term_ids matched to this protein's annotation, further confirming they are not applicable.",
    "The sequence is 548 aa and matches the UniProt canonical sequence exactly (SHA-256 confirmed in both current and historical snapshots)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein's true primary molecular function is DNA-binding transcription factor activity (GO:0003700), which is not offered. Among the four provided choices, zinc ion binding (B) is the only one structurally and functionally consistent with a C2H2 zinc-finger transcription factor. Option D (nucleotide binding) might superficially seem relevant because DNA is a nucleotide polymer, but GO:0000166 explicitly defines nucleotide binding as binding to free nucleotides (e.g., ATP, GTP), not to polymeric DNA. Options A and C require enzymatic/flavoprotein features entirely absent from this sequence. No genuine ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is UniProt G4NBR8, C2H2-type transcription factor MSN2 from Magnaporthe oryzae. The UniProt entry annotates GO:0008270 (zinc ion binding) with evidence code IEA:UniProtKB-KW, and the protein is explicitly described as a 'C2H2-type transcription factor' and 'putative zinc-finger protein' (PubMed:24405033 title). The C2H2 zinc finger motif is identifiable in the sequence (…CNECGKKFSRSDNLTQHARTH…), which coordinates Zn²⁺. Among the four options, zinc ion binding is the only molecular function consistent with a zinc-finger transcription factor: the protein is not an enzyme (rules out A), not a flavoprotein (rules out C), and does not bind free nucleotides (rules out D, per GO:0000166 definition). The annotation is keyword-inferred (IEA), but the C2H2 structural motif is a well-characterized zinc-coordinating domain, providing strong structural support.",
    "evidence_ids": ["C4", "C5", "H2", "H5", "H8", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C2H2 zinc finger motif (C-x2-4-C-x12-H-x3-5-H) is identifiable in the supplied sequence at approximately residues 390–415 (…PFECNECGKKFSRSDNLTQHARTHGSG…). A model with standard knowledge of protein structural motifs can recognize this as a zinc-coordinating C2H2 domain. The protein's overall character—a long, serine/threonine-rich transcription factor with a single C2H2 DNA-binding domain and no enzymatic motifs (no Rossmann fold, no FAD-binding GXGXXG, no aspartate-semialdehyde dehydrogenase catalytic residues)—allows elimination of A (enzyme), C (flavoprotein cofactor), and D (free nucleotide binding, which GO:0000166 defines as binding to free nucleotides, not DNA). Zinc ion binding (B) is the only option consistent with the identified C2H2 motif and the absence of catalytic or cofactor-binding features.",
    "missing_item_specific_fact": "None critical. The C2H2 motif is directly visible in the sequence, and its zinc-coordinating role is standard textbook knowledge. The protein's identity as MSN2 could be looked up, but is not required to identify the zinc finger and eliminate the other options.",
    "reason": "The C2H2 zinc finger pattern is recognizable from the sequence itself, and general biological knowledge about zinc finger structure and the definitions of the GO terms (especially that GO:0000166 nucleotide binding refers to free nucleotides, not DNA) provide a concrete reasoning path to select B over A, C, and D. No protein-specific experimental measurement or obscure annotation is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein's true primary molecular function is DNA-binding transcription factor activity (GO:0003700), which is not offered. Among the four provided choices, zinc ion binding (B) is the only one structurally and functionally consistent with a C2H2 zinc-finger transcription factor. Option D (nucleotide binding) might superficially seem relevant because DNA is a nucleotide polymer, but GO:0000166 explicitly defines nucleotide binding as binding to free nucleotides (e.g., ATP, GTP), not to polymeric DNA. Options A and C require enzymatic/flavoprotein features entirely absent from this sequence. No genuine ambiguity exists among the choices."
  },
  "important_caveats": [
    "The zinc ion binding annotation (GO:0008270) carries evidence code IEA:UniProtKB-KW (keyword-based inference), not direct experimental zinc-binding measurement. However, the C2H2 motif's zinc coordination is an established structural fact.",
    "The protein's primary molecular function is arguably DNA-binding transcription factor activity (GO:0003700, also IEA:TreeGrafter), which is not among the options. The question asks to select the best option from those given, and B is the best fit.",
    "The GO terms for options A, C, and D have no term_ids matched to this protein's annotation, further confirming they are not applicable.",
    "The sequence is 548 aa and matches the UniProt canonical sequence exactly (SHA-256 confirmed in both current and historical snapshots)."
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

**Accession:** `G4NBR8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 61. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NBR8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:44.257787+00:00.  

```json
"G4NBR8"
```

Source SHA-256: `e492ea13b316910c9e1d74aac40a8e7cb37cf329b0709cc53b9ab1f27b888985`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NBR8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:44.257787+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24405033","source":"PubMed"}],"value":"C2H2-type transcription factor MSN2"}}}
```

Source SHA-256: `e492ea13b316910c9e1d74aac40a8e7cb37cf329b0709cc53b9ab1f27b888985`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NBR8.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:44.257787+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24405033","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"32431008","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36774535","source":"PubMed"}],"value":"Transcription factor that acts as a key downstream transcription factor in the HOG1-MAPK pathway (PubMed:24405033, PubMed:32431008, PubMed:36774535). Regulates the expression of a series of downstream genes and controls vegetative growth, conidiogenesis, cell wall integrity, stress response, mitochondrial morphology, and pathogenicity (PubMed:24405033, PubMed:32431008, PubMed:36774535). Binds to a putative promoter region 1500 bp upstream of the start codons of the target genes MGG_07019, POX1 and DCI1 (PubMed:32431008, PubMed:36774535). Binds to the AGGGG and CCCCT motif of the COS1 promoter region (PubMed:24405033). Involved in fatty acid beta-oxidation by directly regulating the expression of the dienoyl-CoA isomerase DCI1, thereby facilitating invasive hyphal growth during the early infection stage (PubMed:32431008, PubMed:36774535). Targets also the 3-methylglutaconyl-CoA hydratase-encoding gene (AUH1) to control mitochondrial morphology and mitophagy, which are critical for the infectious growth of the pathogen (PubMed:32431008)"}]}
```

Source SHA-256: `e492ea13b316910c9e1d74aac40a8e7cb37cf329b0709cc53b9ab1f27b888985`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NBR8?format=txt&versions=61)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-02T04:28:46.842628+00:00.  

```text
RN   [2]
RP   FUNCTION, INTERACTION WITH HOG1/OSM1, DISRUPTION PHENOTYPE, AND SUBCELLULAR
RP   LOCATION.
RX   PubMed=24405033; DOI=10.1094/mpmi-09-13-0271-r;
RA   Zhang H., Zhao Q., Guo X., Guo M., Qi Z., Tang W., Dong Y., Ye W.,
RA   Zheng X., Wang P., Zhang Z.;
RT   "Pleiotropic function of the putative zinc-finger protein MoMsn2 in
RT   Magnaporthe oryzae.";
RL   Mol. Plant Microbe Interact. 27:446-460(2014).
```

Source SHA-256: `b0b7f49db47fe81b856c8e8cbeb350e0a98c3cfdba81bb1c4fa6d8d07ac5a90f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NBR8?format=txt&versions=61)  
**Locator:** `lines 52-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-02T04:28:46.842628+00:00.  

```text
CC   -!- FUNCTION: Transcription factor that acts as a key downstream
CC       transcription factor in the HOG1-MAPK pathway (PubMed:24405033,
CC       PubMed:32431008, PubMed:36774535). Regulates the expression of a series
CC       of downstream genes and controls vegetative growth, conidiogenesis,
CC       cell wall integrity, stress response, mitochondrial morphology, and
CC       pathogenicity (PubMed:24405033, PubMed:32431008, PubMed:36774535).
CC       Binds to a putative promoter region 1500 bp upstream of the start
CC       codons of the target genes MGG_07019, POX1 and DCI1 (PubMed:32431008,
CC       PubMed:36774535). Binds to the AGGGG and CCCCT motif of the COS1
CC       promoter region (PubMed:24405033). Involved in fatty acid beta-
CC       oxidation by directly regulating the expression of the dienoyl-CoA
CC       isomerase DCI1, thereby facilitating invasive hyphal growth during the
CC       early infection stage (PubMed:32431008, PubMed:36774535). Targets also
CC       the 3-methylglutaconyl-CoA hydratase-encoding gene (AUH1) to control
CC       mitochondrial morphology and mitophagy, which are critical for the
CC       infectious growth of the pathogen (PubMed:32431008).
CC       {ECO:0000269|PubMed:24405033, ECO:0000269|PubMed:32431008,
CC       ECO:0000269|PubMed:36774535}.
```

Source SHA-256: `b0b7f49db47fe81b856c8e8cbeb350e0a98c3cfdba81bb1c4fa6d8d07ac5a90f`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NBR8?format=txt&versions=61)  
**Locator:** `lines 108-108`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 61 / 1.  
**Retrieved:** 2026-11-02T04:28:46.842628+00:00.  

```text
DR   GO; GO:0008270; F:zinc ion binding; IEA:UniProtKB-KW.
```

Source SHA-256: `b0b7f49db47fe81b856c8e8cbeb350e0a98c3cfdba81bb1c4fa6d8d07ac5a90f`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 81431-81439`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0008270
name: zinc ion binding
namespace: molecular_function
def: "Binding to a zinc ion (Zn)." [GOC:ai]
synonym: "zinc binding" EXACT []
synonym: "Zn binding" EXACT []
is_a: GO:0046914 ! transition metal ion binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
