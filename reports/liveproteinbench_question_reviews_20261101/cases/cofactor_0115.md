# cofactor_0115

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **A** — FAD

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MYDVIVIGAGWCGLVAAKTYLQACPDAQVLIVDGDTSIGGTWSKERLYPHLVAEAHYGLFEFSDLPMNGDSVLPDGRIPSTAVHAYLVEYATKFNLIQRIRLNTWIENVRREAGELGMHWTLTAAGSQEQLHAKKVIITTGLTSEAFIPSLPGRDEFEGEVLHSKALGHPQTVERISDPSIRHVVVYGGSKSAFDAVYLLLRAGKTVDWVIREGGGGPSMMTPLSVLGQPSFRLNNSRLLALLSPHPFGTPGEQLSWWQRVVHHRSGQWAQFMILTIWRVMNYLFLRPWGYDSSPNGKRLKPLLGLDSLFWSPATLGVMTHPELWEEIHSGQRVKIHRDAITGLARDKRVMLSSGQELSSADLVVCATGWHARHSFFAPEEQLAVGLPGTASFDPKSQQKWLDLQRTADREITEELPILQKNPIPPPPLRCEDDHHLYRFIAPSRETPSHERSIAFVGFLRTAGAPIVYEAQSLWATAYLTGALEVPEAPQREREIARTNAWIRRRYLCGRKVPFALFDFLPYVDMLYRDLGINPNRKPNQIAELCGLYRPQDFKGVVSEWLANQQAKDVNGN

[Multiple Choices]
A. FAD
B. heme b
C. Ca(2+)
D. [2Fe-2S] cluster
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

> The sequence matches the archived UniProt record, which annotates the protein as a FAD-dependent monooxygenase and lists FAD as its cofactor. This is curator-level annotation evidence, not direct experimental proof in the excerpts.

Citations as saved: [H2](#evidence-h2), [H4](#evidence-h4), [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence contains a glycine-rich GxGxxG motif (GAGWCG), consistent with a dinucleotide-binding fold used by flavoproteins. That provides a meaningful sequence-based reason to favor FAD over the offered heme, calcium, and iron-sulfur choices.


**Missing item-specific fact**

> The sequence motif is not uniquely diagnostic of FAD and does not itself establish that FAD is required; direct confirmation would require protein-specific functional or binding evidence.


**Reason**

> The sequence offers a concrete, if not conclusive, flavoprotein clue that distinguishes FAD from the listed alternatives. The database annotation supports the key but was not supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> FAD is the best-supported choice among the options, although the sequence motif alone is not definitive.


### Important caveats

- The historical and current UniProt records match the supplied sequence.
- The cited cofactor annotation carries evidence code ECO:0000305; the supplied excerpts do not establish direct experimental measurement of FAD binding or necessity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence contains a glycine-rich GxGxxG motif (GAGWCG), consistent with a dinucleotide-binding fold used by flavoproteins. That provides a meaningful sequence-based reason to favor FAD over the offered heme, calcium, and iron-sulfur choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence motif is not uniquely diagnostic of FAD and does not itself establish that FAD is required; direct confirmation would require protein-specific functional or binding evidence.",
    "reason": "The sequence offers a concrete, if not conclusive, flavoprotein clue that distinguishes FAD from the listed alternatives. The database annotation supports the key but was not supplied to the evaluated model."
  },
  "case_id": "cofactor_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H4",
      "C1",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the archived UniProt record, which annotates the protein as a FAD-dependent monooxygenase and lists FAD as its cofactor. This is curator-level annotation evidence, not direct experimental proof in the excerpts."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence.",
    "The cited cofactor annotation carries evidence code ECO:0000305; the supplied excerpts do not establish direct experimental measurement of FAD binding or necessity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is the best-supported choice among the options, although the sequence motif alone is not definitive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the archived UniProt record, which annotates the protein as a FAD-dependent monooxygenase and lists FAD as its cofactor. This is curator-level annotation evidence, not direct experimental proof in the excerpts.",
    "evidence_ids": ["H2", "H4", "C1", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence contains a glycine-rich GxGxxG motif (GAGWCG), consistent with a dinucleotide-binding fold used by flavoproteins. That provides a meaningful sequence-based reason to favor FAD over the offered heme, calcium, and iron-sulfur choices.",
    "missing_item_specific_fact": "The sequence motif is not uniquely diagnostic of FAD and does not itself establish that FAD is required; direct confirmation would require protein-specific functional or binding evidence.",
    "reason": "The sequence offers a concrete, if not conclusive, flavoprotein clue that distinguishes FAD from the listed alternatives. The database annotation supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FAD is the best-supported choice among the options, although the sequence motif alone is not definitive."
  },
  "important_caveats": [
    "The historical and current UniProt records match the supplied sequence.",
    "The cited cofactor annotation carries evidence code ECO:0000305; the supplied excerpts do not establish direct experimental measurement of FAD binding or necessity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXV5 (sequence matched, 573 aa) is annotated as 'FAD-dependent monooxygenase resA' with cofactor FAD (ChEBI:CHEBI:57692, evidence ECO:0000305). The historical entry (version 3, released 2026_01) carries the same annotation. The sequence contains a clear Rossmann-fold GxGxxG motif (GAGWCGLVAA at the N-terminus) and multiple GGGG motifs characteristic of FAD-binding Rossmann folds, consistent with the annotation. Note: the evidence code ECO:0000305 indicates inference by similarity rather than direct experimental measurement, but the sequence-level motifs independently support FAD binding.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence contains a canonical Rossmann-fold GxGxxG dinucleotide-binding motif (GAGWCGLVAA: G-A-G-W-C-G), and the middle region harbors multiple GGGG motifs (e.g., 'VIREGGGGPSMMTPLSVLG', 'VVVYGGSKSAFDAVYLLLRAGKTVDWVIREGGGG') that are hallmarks of the FAD-binding loop in flavin-dependent oxidoreductases/monooxygenases. The overall ~573-aa architecture with tandem Rossmann-like domains is typical of FAD-dependent monooxygenases. In contrast, heme b would require Cys-His or bis-His coordination motifs (absent), Ca(2+) binding would require EF-hand DxDxDGxxE motifs (absent), and &#91;2Fe-2S&#93; clusters require Cys-X2-Cys-X2-Cys-X2-Cys arrangements (absent). Among the four options, only FAD is consistent with the observed Rossmann-fold and GGGG signatures.


**Missing item-specific fact**

> None critical. The Rossmann-fold GxGxxG and GGGG motifs are general, well-established sequence signatures for FAD binding and are directly observable in the supplied sequence.


**Reason**

> A knowledgeable model can identify the Rossmann-fold GxGxxG motif and GGGG FAD-binding loops from the raw sequence, then eliminate heme b (no His/Cys heme-ligating geometry), Ca(2+) (no EF-hands), and &#91;2Fe-2S&#93; (no Cys-rich cluster motifs). This constitutes a concrete, general biological argument that does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Rossmann-fold GxGxxG and GGGG motifs unambiguously point to a flavin/nucleotide-binding enzyme. Among the four choices, only FAD fits. Heme b, Ca(2+), and &#91;2Fe-2S&#93; each have well-defined sequence signatures that are absent from this protein.


### Important caveats

- The UniProt cofactor annotation carries evidence code ECO:0000305 (inferred by similarity), not direct experimental binding data; however, the sequence-level Rossmann-fold motifs independently corroborate FAD binding.
- The GxGxxG motif is shared between FAD- and NAD-binding enzymes; the distinction from NAD is not tested here because NAD is not among the options.
- The protein is flagged as a 'Precursor' in UniProt, meaning the mature form may differ slightly, but this does not affect the cofactor prediction.
- The reference (PubMed:39105744, 2024) reports function and pathway data from heterologous expression and genome mining; the FAD assignment is based on sequence similarity and genomic context rather than isolated cofactor-binding assays.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence contains a canonical Rossmann-fold GxGxxG dinucleotide-binding motif (GAGWCGLVAA: G-A-G-W-C-G), and the middle region harbors multiple GGGG motifs (e.g., 'VIREGGGGPSMMTPLSVLG', 'VVVYGGSKSAFDAVYLLLRAGKTVDWVIREGGGG') that are hallmarks of the FAD-binding loop in flavin-dependent oxidoreductases/monooxygenases. The overall ~573-aa architecture with tandem Rossmann-like domains is typical of FAD-dependent monooxygenases. In contrast, heme b would require Cys-His or bis-His coordination motifs (absent), Ca(2+) binding would require EF-hand DxDxDGxxE motifs (absent), and [2Fe-2S] clusters require Cys-X2-Cys-X2-Cys-X2-Cys arrangements (absent). Among the four options, only FAD is consistent with the observed Rossmann-fold and GGGG signatures.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The Rossmann-fold GxGxxG and GGGG motifs are general, well-established sequence signatures for FAD binding and are directly observable in the supplied sequence.",
    "reason": "A knowledgeable model can identify the Rossmann-fold GxGxxG motif and GGGG FAD-binding loops from the raw sequence, then eliminate heme b (no His/Cys heme-ligating geometry), Ca(2+) (no EF-hands), and [2Fe-2S] (no Cys-rich cluster motifs). This constitutes a concrete, general biological argument that does not require memorizing this specific protein's database entry."
  },
  "case_id": "cofactor_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXV5 (sequence matched, 573 aa) is annotated as 'FAD-dependent monooxygenase resA' with cofactor FAD (ChEBI:CHEBI:57692, evidence ECO:0000305). The historical entry (version 3, released 2026_01) carries the same annotation. The sequence contains a clear Rossmann-fold GxGxxG motif (GAGWCGLVAA at the N-terminus) and multiple GGGG motifs characteristic of FAD-binding Rossmann folds, consistent with the annotation. Note: the evidence code ECO:0000305 indicates inference by similarity rather than direct experimental measurement, but the sequence-level motifs independently support FAD binding."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000305 (inferred by similarity), not direct experimental binding data; however, the sequence-level Rossmann-fold motifs independently corroborate FAD binding.",
    "The GxGxxG motif is shared between FAD- and NAD-binding enzymes; the distinction from NAD is not tested here because NAD is not among the options.",
    "The protein is flagged as a 'Precursor' in UniProt, meaning the mature form may differ slightly, but this does not affect the cofactor prediction.",
    "The reference (PubMed:39105744, 2024) reports function and pathway data from heterologous expression and genome mining; the FAD assignment is based on sequence similarity and genomic context rather than isolated cofactor-binding assays."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold GxGxxG and GGGG motifs unambiguously point to a flavin/nucleotide-binding enzyme. Among the four choices, only FAD fits. Heme b, Ca(2+), and [2Fe-2S] each have well-defined sequence signatures that are absent from this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXV5 (sequence matched, 573 aa) is annotated as 'FAD-dependent monooxygenase resA' with cofactor FAD (ChEBI:CHEBI:57692, evidence ECO:0000305). The historical entry (version 3, released 2026_01) carries the same annotation. The sequence contains a clear Rossmann-fold GxGxxG motif (GAGWCGLVAA at the N-terminus) and multiple GGGG motifs characteristic of FAD-binding Rossmann folds, consistent with the annotation. Note: the evidence code ECO:0000305 indicates inference by similarity rather than direct experimental measurement, but the sequence-level motifs independently support FAD binding.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence contains a canonical Rossmann-fold GxGxxG dinucleotide-binding motif (GAGWCGLVAA: G-A-G-W-C-G), and the middle region harbors multiple GGGG motifs (e.g., 'VIREGGGGPSMMTPLSVLG', 'VVVYGGSKSAFDAVYLLLRAGKTVDWVIREGGGG') that are hallmarks of the FAD-binding loop in flavin-dependent oxidoreductases/monooxygenases. The overall ~573-aa architecture with tandem Rossmann-like domains is typical of FAD-dependent monooxygenases. In contrast, heme b would require Cys-His or bis-His coordination motifs (absent), Ca(2+) binding would require EF-hand DxDxDGxxE motifs (absent), and [2Fe-2S] clusters require Cys-X2-Cys-X2-Cys-X2-Cys arrangements (absent). Among the four options, only FAD is consistent with the observed Rossmann-fold and GGGG signatures.",
    "missing_item_specific_fact": "None critical. The Rossmann-fold GxGxxG and GGGG motifs are general, well-established sequence signatures for FAD binding and are directly observable in the supplied sequence.",
    "reason": "A knowledgeable model can identify the Rossmann-fold GxGxxG motif and GGGG FAD-binding loops from the raw sequence, then eliminate heme b (no His/Cys heme-ligating geometry), Ca(2+) (no EF-hands), and [2Fe-2S] (no Cys-rich cluster motifs). This constitutes a concrete, general biological argument that does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold GxGxxG and GGGG motifs unambiguously point to a flavin/nucleotide-binding enzyme. Among the four choices, only FAD fits. Heme b, Ca(2+), and [2Fe-2S] each have well-defined sequence signatures that are absent from this protein."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000305 (inferred by similarity), not direct experimental binding data; however, the sequence-level Rossmann-fold motifs independently corroborate FAD binding.",
    "The GxGxxG motif is shared between FAD- and NAD-binding enzymes; the distinction from NAD is not tested here because NAD is not among the options.",
    "The protein is flagged as a 'Precursor' in UniProt, meaning the mature form may differ slightly, but this does not affect the cofactor prediction.",
    "The reference (PubMed:39105744, 2024) reports function and pathway data from heterologous expression and genome mining; the FAD assignment is based on sequence similarity and genomic context rather than isolated cofactor-binding assays."
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

**Accession:** `P0DXV5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:47.174193+00:00.  

```json
"P0DXV5"
```

Source SHA-256: `e707f20abd7826b390bb5fc8cb46d8df7f258be31be61e0129f1d19c24be05d4`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:47.174193+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein A"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"value":"1.-.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"FAD-dependent monooxygenase resA"}}}
```

Source SHA-256: `e707f20abd7826b390bb5fc8cb46d8df7f258be31be61e0129f1d19c24be05d4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:47.174193+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:57692"},"evidences":[{"evidenceCode":"ECO:0000305"}],"name":"FAD"}],"commentType":"COFACTOR"}
```

Source SHA-256: `e707f20abd7826b390bb5fc8cb46d8df7f258be31be61e0129f1d19c24be05d4`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV5?format=txt&versions=3)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:49.115408+00:00.  

```text
ID   RESA_ASPSL              Reviewed;         573 AA.
AC   P0DXV5;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=FAD-dependent monooxygenase resA {ECO:0000303|PubMed:39105744};
DE            EC=1.-.-.- {ECO:0000305|PubMed:39105744};
DE   AltName: Full=Restricticin biosynthesis cluster protein A {ECO:0000303|PubMed:39105744};
DE   Flags: Precursor;
GN   Name=resA {ECO:0000303|PubMed:39105744};
OS   Aspergillus sclerotiorum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=138282;
```

Source SHA-256: `8f3c70f33ba4a6cc4d094784bec8580161b3aa6521967c7a1063dc12558b2f14`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV5?format=txt&versions=3)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:49.115408+00:00.  

```text
DE   RecName: Full=FAD-dependent monooxygenase resA {ECO:0000303|PubMed:39105744};
DE            EC=1.-.-.- {ECO:0000305|PubMed:39105744};
DE   AltName: Full=Restricticin biosynthesis cluster protein A {ECO:0000303|PubMed:39105744};
DE   Flags: Precursor;
```

Source SHA-256: `8f3c70f33ba4a6cc4d094784bec8580161b3aa6521967c7a1063dc12558b2f14`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV5?format=txt&versions=3)  
**Locator:** `lines 39-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:49.115408+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=FAD; Xref=ChEBI:CHEBI:57692; Evidence={ECO:0000305};
```

Source SHA-256: `8f3c70f33ba4a6cc4d094784bec8580161b3aa6521967c7a1063dc12558b2f14`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
