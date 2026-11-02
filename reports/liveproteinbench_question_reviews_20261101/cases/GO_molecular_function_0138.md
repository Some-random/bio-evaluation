# GO_molecular_function_0138

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — translation elongation factor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGFGDLKTPAGLQVLNDYLADKSYIEGYVPSQADVAVFEAISGPPPADLCHALRWYNHIKSYEKEKASLPGVKKSLGKYGPVSVADTTGSGAADAKDDDDIDLFGSDDEEESEDAKRLREERLAQYESKKAKKPAVVAKSSILLDVKPWDDETDMTKLEECVRSIQADGLVWGSSKLVPVGYGIKKLQIQCVVEDDKVGTDMLEEQITAFEDYVQSMDVAAFNKI

[Multiple Choices]
A. molecular condensate scaffold activity
B. translation elongation factor activity
C. peptidase activity
D. tRNA binding
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

> The exact sequence matches the UniProt entry for elongation factor 1-beta. Its annotated function is to promote GDP-to-GTP exchange on eEF1A within the eukaryotic elongation-factor complex, supporting choice B. The GO annotation is computationally assigned, and the function description is transferred by similarity; this is database support, not independently verified experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a soluble protein, but its length and composition do not provide a concrete, distinctive argument for translation elongation factor activity over the listed alternatives.


**Missing item-specific fact**

> The sequence's identity as eEF1B beta and its role in nucleotide exchange on eEF1A are needed to distinguish choice B.


**Reason**

> The correct choice is supported by a sequence-matched protein-specific annotation, not by an evident general biological inference from the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein-specific evidence supports B; the other listed functions are not supported by the supplied sequence-specific annotations.


### Important caveats

- The matched UniProt function annotation is supported by similarity evidence, and the GO term is annotated with IEA evidence; these should not be represented as direct experimental confirmation.
- The author's exact data-source snapshot is unknown, though a sequence-matched historical UniProt record also supports the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble protein, but its length and composition do not provide a concrete, distinctive argument for translation elongation factor activity over the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity as eEF1B beta and its role in nucleotide exchange on eEF1A are needed to distinguish choice B.",
    "reason": "The correct choice is supported by a sequence-matched protein-specific annotation, not by an evident general biological inference from the sequence and choices alone."
  },
  "case_id": "GO_molecular_function_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for elongation factor 1-beta. Its annotated function is to promote GDP-to-GTP exchange on eEF1A within the eukaryotic elongation-factor complex, supporting choice B. The GO annotation is computationally assigned, and the function description is transferred by similarity; this is database support, not independently verified experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The matched UniProt function annotation is supported by similarity evidence, and the GO term is annotated with IEA evidence; these should not be represented as direct experimental confirmation.",
    "The author's exact data-source snapshot is unknown, though a sequence-matched historical UniProt record also supports the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports B; the other listed functions are not supported by the supplied sequence-specific annotations."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for elongation factor 1-beta. Its annotated function is to promote GDP-to-GTP exchange on eEF1A within the eukaryotic elongation-factor complex, supporting choice B. The GO annotation is computationally assigned, and the function description is transferred by similarity; this is database support, not independently verified experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a soluble protein, but its length and composition do not provide a concrete, distinctive argument for translation elongation factor activity over the listed alternatives.",
    "missing_item_specific_fact": "The sequence's identity as eEF1B beta and its role in nucleotide exchange on eEF1A are needed to distinguish choice B.",
    "reason": "The correct choice is supported by a sequence-matched protein-specific annotation, not by an evident general biological inference from the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein-specific evidence supports B; the other listed functions are not supported by the supplied sequence-specific annotations."
  },
  "important_caveats": [
    "The matched UniProt function annotation is supported by similarity evidence, and the GO term is annotated with IEA evidence; these should not be represented as direct experimental confirmation.",
    "The author's exact data-source snapshot is unknown, though a sequence-matched historical UniProt record also supports the annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt A6IPG1 (Elongation factor 1-beta / eEF-1B alpha, rat). The FUNCTION comment (C5, H2) describes it as the catalytic subunit of the GEF (eEF1B subcomplex) of the eukaryotic elongation factor 1 complex, stimulating GDP-to-GTP exchange on eEF1A. GO:0003746 (translation elongation factor activity) is annotated (C6, H3) with IEA:InterPro evidence. While the specific GO annotation is computationally inferred (IEA), the protein's identity, name, and described function as a component of the eEF1 translation elongation complex are consistent with and support the 'translation elongation factor activity' assignment. The GO term definition (GO2: 'Functions in chain elongation during polypeptide synthesis at the ribosome') applies to EF-1B as part of the eEF1 machinery.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two highly diagnostic features of the EF-Ts/EF-1B family: (1) a strongly acidic N-terminal region (DDDDIDLFGSDDEEESEDAKRLREERLAQYESKKAKK) characteristic of eEF1Bα's acidic domain, and (2) a C-terminal domain with GTP-binding-like motifs (GSSKLVPVGYGIKK...) resembling the nucleotide-exchange domain of EF-Ts/EF-1B. These features, combined with the 225-aa length, point to the EF-Ts/EF-1B family. Within the translation elongation machinery, EF-1B functions as a GEF for EF-1A (part of the eEF1 complex), not as a direct tRNA binder—tRNA binding is the role of EF-1A. Peptidase activity (C) is excluded by the absence of any catalytic triad, zinc-binding motif, or aspartic-protease signature. Molecular condensate scaffold activity (A) is not supported by the domain architecture. Thus, general knowledge of translation factor families allows reasoning from sequence features to 'translation elongation factor activity' over 'tRNA binding.'


**Missing item-specific fact**

> None critical. The distinction between B and D relies on knowing that EF-1B/EF-Ts is a GEF (not a tRNA binder), which is standard textbook knowledge about the eEF1/eEF-Tu translation system.


**Reason**

> The acidic region and EF-Ts-like nucleotide-exchange domain are distinctive sequence features that a knowledgeable model can use to identify the EF-1B family and reason that its primary molecular function is translation elongation factor activity (GEF for EF-1A) rather than tRNA binding. Peptidase and condensate scaffold options are eliminable by absence of catalytic/structural features. This constitutes a concrete biological argument from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C (peptidase) is clearly excluded by absence of catalytic residues. Option A (molecular condensate scaffold) is a weak distractor with no structural basis in this protein. Option D (tRNA binding) is the closest competitor but is distinguishable because EF-1B's established role is GEF activity on EF-1A, not direct tRNA interaction; the GO term GO:0000049 (tRNA binding) is not annotated for this protein. Option B is the single best-supported answer.


### Important caveats

- The GO:0003746 annotation carries IEA:InterPro evidence code (computational inference from InterPro domain match), not direct experimental evidence. However, the protein's identity as EF-1B and its described GEF function in the eEF1 complex are well-established.
- The sequence was matched to UniProt A6IPG1 (rat EF-1B alpha, 225 aa) in both current and archived (v13) snapshots.
- The identity origin (accession inferred from dataset metadata) is reviewer-only and was not available to the evaluated model.
- The acidic region, while highly characteristic of eEF1Bα, is not unique to translation factors; the reasoning depends on recognizing the combined domain architecture as EF-Ts/EF-1B-like.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two highly diagnostic features of the EF-Ts/EF-1B family: (1) a strongly acidic N-terminal region (DDDDIDLFGSDDEEESEDAKRLREERLAQYESKKAKK) characteristic of eEF1Bα's acidic domain, and (2) a C-terminal domain with GTP-binding-like motifs (GSSKLVPVGYGIKK...) resembling the nucleotide-exchange domain of EF-Ts/EF-1B. These features, combined with the 225-aa length, point to the EF-Ts/EF-1B family. Within the translation elongation machinery, EF-1B functions as a GEF for EF-1A (part of the eEF1 complex), not as a direct tRNA binder—tRNA binding is the role of EF-1A. Peptidase activity (C) is excluded by the absence of any catalytic triad, zinc-binding motif, or aspartic-protease signature. Molecular condensate scaffold activity (A) is not supported by the domain architecture. Thus, general knowledge of translation factor families allows reasoning from sequence features to 'translation elongation factor activity' over 'tRNA binding.'",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The distinction between B and D relies on knowing that EF-1B/EF-Ts is a GEF (not a tRNA binder), which is standard textbook knowledge about the eEF1/eEF-Tu translation system.",
    "reason": "The acidic region and EF-Ts-like nucleotide-exchange domain are distinctive sequence features that a knowledgeable model can use to identify the EF-1B family and reason that its primary molecular function is translation elongation factor activity (GEF for EF-1A) rather than tRNA binding. Peptidase and condensate scaffold options are eliminable by absence of catalytic/structural features. This constitutes a concrete biological argument from the sequence."
  },
  "case_id": "GO_molecular_function_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt A6IPG1 (Elongation factor 1-beta / eEF-1B alpha, rat). The FUNCTION comment (C5, H2) describes it as the catalytic subunit of the GEF (eEF1B subcomplex) of the eukaryotic elongation factor 1 complex, stimulating GDP-to-GTP exchange on eEF1A. GO:0003746 (translation elongation factor activity) is annotated (C6, H3) with IEA:InterPro evidence. While the specific GO annotation is computationally inferred (IEA), the protein's identity, name, and described function as a component of the eEF1 translation elongation complex are consistent with and support the 'translation elongation factor activity' assignment. The GO term definition (GO2: 'Functions in chain elongation during polypeptide synthesis at the ribosome') applies to EF-1B as part of the eEF1 machinery."
  },
  "important_caveats": [
    "The GO:0003746 annotation carries IEA:InterPro evidence code (computational inference from InterPro domain match), not direct experimental evidence. However, the protein's identity as EF-1B and its described GEF function in the eEF1 complex are well-established.",
    "The sequence was matched to UniProt A6IPG1 (rat EF-1B alpha, 225 aa) in both current and archived (v13) snapshots.",
    "The identity origin (accession inferred from dataset metadata) is reviewer-only and was not available to the evaluated model.",
    "The acidic region, while highly characteristic of eEF1Bα, is not unique to translation factors; the reasoning depends on recognizing the combined domain architecture as EF-Ts/EF-1B-like."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (peptidase) is clearly excluded by absence of catalytic residues. Option A (molecular condensate scaffold) is a weak distractor with no structural basis in this protein. Option D (tRNA binding) is the closest competitor but is distinguishable because EF-1B's established role is GEF activity on EF-1A, not direct tRNA interaction; the GO term GO:0000049 (tRNA binding) is not annotated for this protein. Option B is the single best-supported answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt A6IPG1 (Elongation factor 1-beta / eEF-1B alpha, rat). The FUNCTION comment (C5, H2) describes it as the catalytic subunit of the GEF (eEF1B subcomplex) of the eukaryotic elongation factor 1 complex, stimulating GDP-to-GTP exchange on eEF1A. GO:0003746 (translation elongation factor activity) is annotated (C6, H3) with IEA:InterPro evidence. While the specific GO annotation is computationally inferred (IEA), the protein's identity, name, and described function as a component of the eEF1 translation elongation complex are consistent with and support the 'translation elongation factor activity' assignment. The GO term definition (GO2: 'Functions in chain elongation during polypeptide synthesis at the ribosome') applies to EF-1B as part of the eEF1 machinery.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two highly diagnostic features of the EF-Ts/EF-1B family: (1) a strongly acidic N-terminal region (DDDDIDLFGSDDEEESEDAKRLREERLAQYESKKAKK) characteristic of eEF1Bα's acidic domain, and (2) a C-terminal domain with GTP-binding-like motifs (GSSKLVPVGYGIKK...) resembling the nucleotide-exchange domain of EF-Ts/EF-1B. These features, combined with the 225-aa length, point to the EF-Ts/EF-1B family. Within the translation elongation machinery, EF-1B functions as a GEF for EF-1A (part of the eEF1 complex), not as a direct tRNA binder—tRNA binding is the role of EF-1A. Peptidase activity (C) is excluded by the absence of any catalytic triad, zinc-binding motif, or aspartic-protease signature. Molecular condensate scaffold activity (A) is not supported by the domain architecture. Thus, general knowledge of translation factor families allows reasoning from sequence features to 'translation elongation factor activity' over 'tRNA binding.'",
    "missing_item_specific_fact": "None critical. The distinction between B and D relies on knowing that EF-1B/EF-Ts is a GEF (not a tRNA binder), which is standard textbook knowledge about the eEF1/eEF-Tu translation system.",
    "reason": "The acidic region and EF-Ts-like nucleotide-exchange domain are distinctive sequence features that a knowledgeable model can use to identify the EF-1B family and reason that its primary molecular function is translation elongation factor activity (GEF for EF-1A) rather than tRNA binding. Peptidase and condensate scaffold options are eliminable by absence of catalytic/structural features. This constitutes a concrete biological argument from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (peptidase) is clearly excluded by absence of catalytic residues. Option A (molecular condensate scaffold) is a weak distractor with no structural basis in this protein. Option D (tRNA binding) is the closest competitor but is distinguishable because EF-1B's established role is GEF activity on EF-1A, not direct tRNA interaction; the GO term GO:0000049 (tRNA binding) is not annotated for this protein. Option B is the single best-supported answer."
  },
  "important_caveats": [
    "The GO:0003746 annotation carries IEA:InterPro evidence code (computational inference from InterPro domain match), not direct experimental evidence. However, the protein's identity as EF-1B and its described GEF function in the eEF1 complex are well-established.",
    "The sequence was matched to UniProt A6IPG1 (rat EF-1B alpha, 225 aa) in both current and archived (v13) snapshots.",
    "The identity origin (accession inferred from dataset metadata) is reviewer-only and was not available to the evaluated model.",
    "The acidic region, while highly characteristic of eEF1Bα, is not unique to translation factors; the reasoning depends on recognizing the combined domain architecture as EF-Ts/EF-1B-like."
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

**Accession:** `A6IPG1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6IPG1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.217950+00:00.  

```json
"A6IPG1"
```

Source SHA-256: `d0bfa7d1ff28b79c14a3e1edab1da37e11dc7a4061db221fb6a4b6a25a0546a4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6IPG1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.217950+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"eEF-1B alpha"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Elongation factor 1-beta"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"EF-1-beta"}]}}
```

Source SHA-256: `d0bfa7d1ff28b79c14a3e1edab1da37e11dc7a4061db221fb6a4b6a25a0546a4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6IPG1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.217950+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32471","source":"UniProtKB"}],"value":"Catalytic subunit of the guanine nucleotide exchange factor (GEF) (eEF1B subcomplex) of the eukaryotic elongation factor 1 complex (eEF1). Stimulates the exchange of GDP for GTP on elongation factor 1A (eEF1A), probably by displacing GDP from the nucleotide binding pocket in eEF1A"}]}
```

Source SHA-256: `d0bfa7d1ff28b79c14a3e1edab1da37e11dc7a4061db221fb6a4b6a25a0546a4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6IPG1.json)  
**Locator:** `/uniProtKBCrossReferences/33`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:05.217950+00:00.  

```json
{"database":"GO","id":"GO:0003746","properties":[{"key":"GoTerm","value":"F:translation elongation factor activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `d0bfa7d1ff28b79c14a3e1edab1da37e11dc7a4061db221fb6a4b6a25a0546a4`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6IPG1?format=txt&versions=13)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:27:07.173978+00:00.  

```text
ID   EF1B_RAT                Reviewed;         225 AA.
AC   A6IPG1; B5DEN5; F6SZC1;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   28-JUN-2023, sequence version 1.
DT   28-JAN-2026, entry version 13.
DE   RecName: Full=Elongation factor 1-beta {ECO:0000305};
DE            Short=EF-1-beta {ECO:0000305};
DE   AltName: Full=eEF-1B alpha {ECO:0000305};
GN   Name=Eef1b2 {ECO:0000312|RGD:1311415};
OS   Rattus norvegicus (Rat).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Rattus.
OX   NCBI_TaxID=10116 {ECO:0000312|EMBL:AAI68738.1};
```

Source SHA-256: `54a509c2a7ee7e581d42ed411dc4041c0472dbfba5bbc038c88b767ab744ff49`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6IPG1?format=txt&versions=13)  
**Locator:** `lines 102-106`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:27:07.173978+00:00.  

```text
CC   -!- FUNCTION: Catalytic subunit of the guanine nucleotide exchange factor
CC       (GEF) (eEF1B subcomplex) of the eukaryotic elongation factor 1 complex
CC       (eEF1). Stimulates the exchange of GDP for GTP on elongation factor 1A
CC       (eEF1A), probably by displacing GDP from the nucleotide binding pocket
CC       in eEF1A. {ECO:0000250|UniProtKB:P32471}.
```

Source SHA-256: `54a509c2a7ee7e581d42ed411dc4041c0472dbfba5bbc038c88b767ab744ff49`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6IPG1?format=txt&versions=13)  
**Locator:** `lines 149-149`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:27:07.173978+00:00.  

```text
DR   GO; GO:0003746; F:translation elongation factor activity; IEA:UniProtKB-KW.
```

Source SHA-256: `54a509c2a7ee7e581d42ed411dc4041c0472dbfba5bbc038c88b767ab744ff49`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 28414-28424`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003746
name: translation elongation factor activity
namespace: molecular_function
alt_id: GO:0008182
alt_id: GO:0008183
def: "Functions in chain elongation during polypeptide synthesis at the ribosome." [ISBN:0198506732]
xref: Reactome:R-HSA-192704 "Synthesis of PB1-F2"
xref: Reactome:R-HSA-192841 "Viral Protein Synthesis"
is_a: GO:0180051 ! translation factor activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 138. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
