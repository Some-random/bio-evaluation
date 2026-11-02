# cofactor_0180

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — FAD

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLRYRQVVGLLQRRNFSAGATSNGSGSSGGDKSGEDLHPIRRTLRLLGNDMRKVKEFFVPKEPETEKVPIPTQSQFHFSGERDKSKEATVPDDFQTHCDVLIIGGGGVGSSIAYWLKEKARDGLNVVVVEKDDTYAQSATRVSVGGLCQQFSLPENIQMSLFAADFLRSARKHFGEEVPLQFTPHGHLMLAGEEHAESLKRSSQLQNELGARNELLTADRLTARFPWLNTKGIALGCLGLEKEGWFNPLALLSNFRRSASGYGAHFISGQVVDFEFKSQTDISVVTDLGSNEGAYTGLEKAVIQLPDGTRRTCKFALCVISAGASSEQIARLARIGVGPGILRVPLPINARKRYMYAINSQAQSAPGMNMPMTIDPSGIFIRRDGLGGNYICVQDSTEEYNSAMIDPQYFAQHIRPHLYNRIPVLGEAQVVDSWAGCYDHNVYDENGILGAHPYYNNLYLATGFSGHGVQQSLAVGRAISELIMDGQFRTIDLSRLSFDRLIVDQPMFELNNVLS

[Multiple Choices]
A. tungstopterin
B. heme
C. FAD
D. NAD(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the 515-residue Drosophila protein annotated as a FAD-dependent oxidoreductase, and its UniProt cofactor annotation specifies FAD. This supports choice C as a database annotation; the cited cofactor evidence code does not by itself establish that the claim was experimentally measured.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may be consistent with an oxidoreductase, but that broad inference does not distinguish FAD from NAD(+) or establish the particular cofactor requirement.


**Missing item-specific fact**

> The identity and cofactor annotation of this specific protein as FAD-dependent are not supplied in the question.


**Reason**

> Selecting FAD is supported by the matched protein-specific database annotation, not by a sequence feature or biological argument in the input that meaningfully rules out the other choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein's cofactor annotation specifies FAD; the sequence-only prompt, however, does not provide enough information to derive that specificity.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but it was not available to the evaluated model.
- The cofactor annotation is database evidence, not independently verified experimental evidence in the supplied material.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may be consistent with an oxidoreductase, but that broad inference does not distinguish FAD from NAD(+) or establish the particular cofactor requirement.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity and cofactor annotation of this specific protein as FAD-dependent are not supplied in the question.",
    "reason": "Selecting FAD is supported by the matched protein-specific database annotation, not by a sequence feature or biological argument in the input that meaningfully rules out the other choices."
  },
  "case_id": "cofactor_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 515-residue Drosophila protein annotated as a FAD-dependent oxidoreductase, and its UniProt cofactor annotation specifies FAD. This supports choice C as a database annotation; the cited cofactor evidence code does not by itself establish that the claim was experimentally measured."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but it was not available to the evaluated model.",
    "The cofactor annotation is database evidence, not independently verified experimental evidence in the supplied material."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's cofactor annotation specifies FAD; the sequence-only prompt, however, does not provide enough information to derive that specificity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 515-residue Drosophila protein annotated as a FAD-dependent oxidoreductase, and its UniProt cofactor annotation specifies FAD. This supports choice C as a database annotation; the cited cofactor evidence code does not by itself establish that the claim was experimentally measured.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may be consistent with an oxidoreductase, but that broad inference does not distinguish FAD from NAD(+) or establish the particular cofactor requirement.",
    "missing_item_specific_fact": "The identity and cofactor annotation of this specific protein as FAD-dependent are not supplied in the question.",
    "reason": "Selecting FAD is supported by the matched protein-specific database annotation, not by a sequence feature or biological argument in the input that meaningfully rules out the other choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's cofactor annotation specifies FAD; the sequence-only prompt, however, does not provide enough information to derive that specificity."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but it was not available to the evaluated model.",
    "The cofactor annotation is database evidence, not independently verified experimental evidence in the supplied material."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> UniProt entry Q9VJ10 (FXRD1_DROME) explicitly annotates FAD as the cofactor (C5, H4: 'COFACTOR: Name=FAD; Xref=ChEBI:CHEBI:57692'). The recommended protein name is 'FAD-dependent oxidoreductase domain-containing protein 1 homolog' (C4, H2). The evidence code is ECO:0000305 (inferred by curator), which is a database annotation rather than direct experimental measurement, but it is consistent with the well-characterized FOXRED1 domain family that is defined by its FAD dependence. The sequence matches the benchmark exactly (515 aa, SHA-256 match).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains Rossmann-fold-like glycine-rich motifs (e.g., 'GGGGVG' near position ~100, 'GCLGLEKEGWF') that indicate dinucleotide binding, which helps rule out heme (no Cys-His/His-His ligation motifs present) and tungstopterin (no molybdopterin/tungstopterin-specific features, and this is a eukaryotic mitochondrial protein). However, the critical distinction between FAD (C) and NAD(+) (D) cannot be reliably made from sequence motifs alone: both cofactors bind through overlapping GxGxxG Rossmann-fold motifs, and the sequence does not contain a unique, unambiguous FAD-specific signature that a general-knowledge model could extract. The correct answer depends on recognizing the specific FOXRED1 (FAD-dependent oxidoreductase domain) fold and knowing that this domain family is defined by FAD (not NAD+) dependence.


**Missing item-specific fact**

> Knowledge that this particular domain architecture corresponds to the FOXRED1 domain family, which is specifically FAD-dependent rather than NAD+-dependent. This is a domain-family-level annotation, not derivable from generic Rossmann-fold pattern recognition.


**Reason**

> While the sequence allows elimination of heme and tungstopterin through absence of their characteristic binding motifs, the FAD-vs-NAD(+) distinction requires recognizing the specific FOXRED1 domain fold. General Rossmann-fold motifs are shared between FAD- and NAD-binding proteins, so the answer hinges on item-specific domain-family knowledge (or a trained predictor), not on general biological reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C (FAD)",
  "D (NAD(+))"
]
```

> Both FAD and NAD(+) bind through Rossmann-fold GxGxxG motifs present in the sequence. Without domain-family-level knowledge, a model could reasonably argue for either dinucleotide cofactor. The other two options (tungstopterin, heme) are clearly eliminable by absence of their characteristic motifs.


### Important caveats

- The cofactor annotation carries evidence code ECO:0000305 (inferred by curator), meaning it is a database annotation based on domain-family assignment and literature, not a direct experimental cofactor assay reported in a primary paper.
- The protein name itself contains 'FAD-dependent,' which is the strongest single indicator of the answer; however, the model receives only the raw sequence, not the name.
- The UniProt entry was first publicly released 2025-02-05; the author's source snapshot is unknown, though the historical entry (version 178, released 2026-01-28) already contains the FAD cofactor annotation.
- Tungstopterin (A) is an extremely unusual cofactor found primarily in archaeal/algal oxidoreductases and is a clear distractor for a Drosophila mitochondrial protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains Rossmann-fold-like glycine-rich motifs (e.g., 'GGGGVG' near position ~100, 'GCLGLEKEGWF') that indicate dinucleotide binding, which helps rule out heme (no Cys-His/His-His ligation motifs present) and tungstopterin (no molybdopterin/tungstopterin-specific features, and this is a eukaryotic mitochondrial protein). However, the critical distinction between FAD (C) and NAD(+) (D) cannot be reliably made from sequence motifs alone: both cofactors bind through overlapping GxGxxG Rossmann-fold motifs, and the sequence does not contain a unique, unambiguous FAD-specific signature that a general-knowledge model could extract. The correct answer depends on recognizing the specific FOXRED1 (FAD-dependent oxidoreductase domain) fold and knowing that this domain family is defined by FAD (not NAD+) dependence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowledge that this particular domain architecture corresponds to the FOXRED1 domain family, which is specifically FAD-dependent rather than NAD+-dependent. This is a domain-family-level annotation, not derivable from generic Rossmann-fold pattern recognition.",
    "reason": "While the sequence allows elimination of heme and tungstopterin through absence of their characteristic binding motifs, the FAD-vs-NAD(+) distinction requires recognizing the specific FOXRED1 domain fold. General Rossmann-fold motifs are shared between FAD- and NAD-binding proteins, so the answer hinges on item-specific domain-family knowledge (or a trained predictor), not on general biological reasoning from the sequence."
  },
  "case_id": "cofactor_0180",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9VJ10 (FXRD1_DROME) explicitly annotates FAD as the cofactor (C5, H4: 'COFACTOR: Name=FAD; Xref=ChEBI:CHEBI:57692'). The recommended protein name is 'FAD-dependent oxidoreductase domain-containing protein 1 homolog' (C4, H2). The evidence code is ECO:0000305 (inferred by curator), which is a database annotation rather than direct experimental measurement, but it is consistent with the well-characterized FOXRED1 domain family that is defined by its FAD dependence. The sequence matches the benchmark exactly (515 aa, SHA-256 match)."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000305 (inferred by curator), meaning it is a database annotation based on domain-family assignment and literature, not a direct experimental cofactor assay reported in a primary paper.",
    "The protein name itself contains 'FAD-dependent,' which is the strongest single indicator of the answer; however, the model receives only the raw sequence, not the name.",
    "The UniProt entry was first publicly released 2025-02-05; the author's source snapshot is unknown, though the historical entry (version 178, released 2026-01-28) already contains the FAD cofactor annotation.",
    "Tungstopterin (A) is an extremely unusual cofactor found primarily in archaeal/algal oxidoreductases and is a clear distractor for a Drosophila mitochondrial protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C (FAD)",
      "D (NAD(+))"
    ],
    "reason": "Both FAD and NAD(+) bind through Rossmann-fold GxGxxG motifs present in the sequence. Without domain-family-level knowledge, a model could reasonably argue for either dinucleotide cofactor. The other two options (tungstopterin, heme) are clearly eliminable by absence of their characteristic motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0180",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9VJ10 (FXRD1_DROME) explicitly annotates FAD as the cofactor (C5, H4: 'COFACTOR: Name=FAD; Xref=ChEBI:CHEBI:57692'). The recommended protein name is 'FAD-dependent oxidoreductase domain-containing protein 1 homolog' (C4, H2). The evidence code is ECO:0000305 (inferred by curator), which is a database annotation rather than direct experimental measurement, but it is consistent with the well-characterized FOXRED1 domain family that is defined by its FAD dependence. The sequence matches the benchmark exactly (515 aa, SHA-256 match).",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains Rossmann-fold-like glycine-rich motifs (e.g., 'GGGGVG' near position ~100, 'GCLGLEKEGWF') that indicate dinucleotide binding, which helps rule out heme (no Cys-His/His-His ligation motifs present) and tungstopterin (no molybdopterin/tungstopterin-specific features, and this is a eukaryotic mitochondrial protein). However, the critical distinction between FAD (C) and NAD(+) (D) cannot be reliably made from sequence motifs alone: both cofactors bind through overlapping GxGxxG Rossmann-fold motifs, and the sequence does not contain a unique, unambiguous FAD-specific signature that a general-knowledge model could extract. The correct answer depends on recognizing the specific FOXRED1 (FAD-dependent oxidoreductase domain) fold and knowing that this domain family is defined by FAD (not NAD+) dependence.",
    "missing_item_specific_fact": "Knowledge that this particular domain architecture corresponds to the FOXRED1 domain family, which is specifically FAD-dependent rather than NAD+-dependent. This is a domain-family-level annotation, not derivable from generic Rossmann-fold pattern recognition.",
    "reason": "While the sequence allows elimination of heme and tungstopterin through absence of their characteristic binding motifs, the FAD-vs-NAD(+) distinction requires recognizing the specific FOXRED1 domain fold. General Rossmann-fold motifs are shared between FAD- and NAD-binding proteins, so the answer hinges on item-specific domain-family knowledge (or a trained predictor), not on general biological reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C (FAD)", "D (NAD(+))"],
    "reason": "Both FAD and NAD(+) bind through Rossmann-fold GxGxxG motifs present in the sequence. Without domain-family-level knowledge, a model could reasonably argue for either dinucleotide cofactor. The other two options (tungstopterin, heme) are clearly eliminable by absence of their characteristic motifs."
  },
  "important_caveats": [
    "The cofactor annotation carries evidence code ECO:0000305 (inferred by curator), meaning it is a database annotation based on domain-family assignment and literature, not a direct experimental cofactor assay reported in a primary paper.",
    "The protein name itself contains 'FAD-dependent,' which is the strongest single indicator of the answer; however, the model receives only the raw sequence, not the name.",
    "The UniProt entry was first publicly released 2025-02-05; the author's source snapshot is unknown, though the historical entry (version 178, released 2026-01-28) already contains the FAD cofactor annotation.",
    "Tungstopterin (A) is an extremely unusual cofactor found primarily in archaeal/algal oxidoreductases and is a clear distractor for a Drosophila mitochondrial protein."
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

**Accession:** `Q9VJ10` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 178. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
"Q9VJ10"
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"FBgn0002021","source":"FlyBase"}],"value":"Protein lethal (2) 37Bb"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34386730","source":"PubMed"}],"value":"FAD-dependent oxidoreductase domain-containing protein 1 homolog"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34386730","source":"PubMed"}],"value":"dFOXRED1"}]}}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ10.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:20.331974+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:57692"},"evidences":[{"evidenceCode":"ECO:0000305"}],"name":"FAD"}],"commentType":"COFACTOR"}
```

Source SHA-256: `5928264ea67fff4feffb21b27781b1256523a5cc83b17b4b26cd4301a622bbde`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:33:26.250109+00:00.  

```text
ID   FXRD1_DROME             Reviewed;         515 AA.
AC   Q9VJ10;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 178.
DE   RecName: Full=FAD-dependent oxidoreductase domain-containing protein 1 homolog {ECO:0000303|PubMed:34386730};
DE            Short=dFOXRED1 {ECO:0000303|PubMed:34386730};
DE   AltName: Full=Protein lethal (2) 37Bb {ECO:0000312|FlyBase:FBgn0002021};
GN   Name=l(2)37Bb {ECO:0000312|FlyBase:FBgn0002021};
GN   Synonyms=Bb {ECO:0000312|FlyBase:FBgn0002021},
GN   l(2)35B2 {ECO:0000312|FlyBase:FBgn0002021};
GN   ORFNames=CG10655 {ECO:0000312|FlyBase:FBgn0002021};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:33:26.250109+00:00.  

```text
DE   RecName: Full=FAD-dependent oxidoreductase domain-containing protein 1 homolog {ECO:0000303|PubMed:34386730};
DE            Short=dFOXRED1 {ECO:0000303|PubMed:34386730};
DE   AltName: Full=Protein lethal (2) 37Bb {ECO:0000312|FlyBase:FBgn0002021};
```

Source SHA-256: `4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ10?format=txt&versions=178)  
**Locator:** `lines 92-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 178 / 1.  
**Retrieved:** 2026-11-02T04:33:26.250109+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=FAD; Xref=ChEBI:CHEBI:57692; Evidence={ECO:0000305};
```

Source SHA-256: `4c84d9e5f4082dd84cbeb45e53111c4d92eafe5818533b97e0eb0502064c3096`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 180. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
