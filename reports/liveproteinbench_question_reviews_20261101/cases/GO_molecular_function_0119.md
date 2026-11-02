# GO_molecular_function_0119

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — cardiolipin synthase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTFNGRFRATLRGINIRNASMTSLSLTGSHAQKQTVLGSTPGALGTIPTVALNGVNPLPRYRHNLLFGTLSFGDRWDRIQRRLAVLGRASTGNVVVPFSDSADAFRRMWESVDSASDSVLWQTYICKDDFVGQKTVKKLEEAHRRGCKTELLYDCGGNITGRRRLVGDLKKSGANVIEHRPMWEHFFPYFLRGMKWELSPGIRNHRKILIVDNKLGFCGGLNIGDEYCGTSEGGNGRFRDTHCVVMGPAVMHMREVYEDTKAPKPWKWSLARWRQIASATMNLRYLEGMNVKHDYLEPTTTFVRQGGGVYLRRQMERAERSTVRMMERMRWKRQRERLNRCLLTLAKNLREGQGLVFKAATGKGDDVATTDAGSKRNNEVSHGQWKLMKRRIDEYRQRAIKNAEESFFRRLRVVNPSMRLLEDTSPVAEAEAYGQAHAAVTQVLSCNPHSRDWSIPYAFWQVSKFVHQRLWVTTPYYMPHRKLMRALQLAARRGVDVRILAGSNRTTDPWFMWYASNYITGMLMASGVRVYEYKGGQVMHAKTVVADSIWTSIGSYNWDMMSNKNMEICVCHLDHNLALTMEKQFLDDMNVSEEVNYEEYQRRSLWLRFSSWFFYTALRIAEKFTFRTFWDPDLSSEID

[Multiple Choices]
A. carbohydrate derivative binding
B. carboxylesterase activity
C. cardiolipin synthase activity
D. NAD+ synthase (glutamine-hydrolyzing) activity
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

> The exact sequence matches a Trypanosoma brucei cardiolipin synthetase entry. Its function annotation reports catalysis of cardiolipin formation and cites experimental evidence; its GO annotation is cardiolipin synthase activity.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices do not provide a sufficiently specific general biological argument to identify cardiolipin synthase activity over the other listed functions.


**Missing item-specific fact**

> The protein-specific functional annotation or equivalent evidence linking this sequence to cardiolipin synthesis.


**Reason**

> The reviewer-only evidence establishes the key for this sequence, but that evidence was absent from the model input. Inferring the exact activity would require protein-specific annotation, experimental knowledge, or a validated sequence homology/function analysis; generic sequence heuristics do not distinguish these options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matching sequence-specific annotation supports C, and the listed activities are distinct.


### Important caveats

- The reviewer evidence reports experimental evidence codes and cited publications, but the primary papers were not independently reviewed here.
- The sequence matches both a historical UniProt record and the current entry; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific general biological argument to identify cardiolipin synthase activity over the other listed functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or equivalent evidence linking this sequence to cardiolipin synthesis.",
    "reason": "The reviewer-only evidence establishes the key for this sequence, but that evidence was absent from the model input. Inferring the exact activity would require protein-specific annotation, experimental knowledge, or a validated sequence homology/function analysis; generic sequence heuristics do not distinguish these options."
  },
  "case_id": "GO_molecular_function_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a Trypanosoma brucei cardiolipin synthetase entry. Its function annotation reports catalysis of cardiolipin formation and cites experimental evidence; its GO annotation is cardiolipin synthase activity."
  },
  "important_caveats": [
    "The reviewer evidence reports experimental evidence codes and cited publications, but the primary papers were not independently reviewed here.",
    "The sequence matches both a historical UniProt record and the current entry; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matching sequence-specific annotation supports C, and the listed activities are distinct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a Trypanosoma brucei cardiolipin synthetase entry. Its function annotation reports catalysis of cardiolipin formation and cites experimental evidence; its GO annotation is cardiolipin synthase activity.",
    "evidence_ids": ["C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices do not provide a sufficiently specific general biological argument to identify cardiolipin synthase activity over the other listed functions.",
    "missing_item_specific_fact": "The protein-specific functional annotation or equivalent evidence linking this sequence to cardiolipin synthesis.",
    "reason": "The reviewer-only evidence establishes the key for this sequence, but that evidence was absent from the model input. Inferring the exact activity would require protein-specific annotation, experimental knowledge, or a validated sequence homology/function analysis; generic sequence heuristics do not distinguish these options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matching sequence-specific annotation supports C, and the listed activities are distinct."
  },
  "important_caveats": [
    "The reviewer evidence reports experimental evidence codes and cited publications, but the primary papers were not independently reviewed here.",
    "The sequence matches both a historical UniProt record and the current entry; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q584D1 (CLS_TRYB2) from Trypanosoma brucei brucei. The UniProt entry explicitly names the protein 'Cardiolipin synthetase' (EC 2.7.8.-) with experimental evidence (ECO:0000269, PubMed:22451910 and PubMed:29167800). The GO annotation GO:0008808 'cardiolipin synthase activity' is assigned with IMP (Inferred by Mutant Phenotype) evidence. The catalytic reaction (2 phosphatidylglycerol → cardiolipin + glycerol) is confirmed experimentally. The expected answer C is directly supported by experimental data.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A weak reasoning pathway exists: the sequence contains a variant CDP-alcohol phosphatidyltransferase motif ('DRWDRIQRRL' near residues 85-95, and 'GPAVMHMRE' later), which could identify the protein as a phosphatidyltransferase. Among the four options, only C (cardiolipin synthase) is a phosphatidyltransferase, while A is a binding function, B is a hydrolase, and D is a ligase/amidotransferase. However, the motifs are non-canonical variants, and identifying them from a 639-aa sequence without context is highly specialized. Moreover, the CDP-alcohol phosphatidyltransferase superfamily includes many members (PS synthase, PC synthase, CDP-DAG synthase, etc.), so even identifying the family does not specifically yield 'cardiolipin synthase' without additional knowledge.


**Missing item-specific fact**

> The specific annotation of this protein as a bacterial-type cardiolipin synthase in a eukaryotic organism (Trypanosoma brucei) is an unusual, item-specific fact. Recognizing the sequence as Q584D1 or knowing its experimentally determined function requires database lookup or memorization. The bacterial-type CLS architecture in a eukaryote does not match typical eukaryotic CLS expectations, further limiting general reasoning.


**Reason**

> While the four options span different enzyme classes (binding, hydrolase, transferase, ligase), the primary reliable pathway to the answer is recognizing this specific protein's annotation. The CDP-alcohol phosphatidyltransferase motifs present in the sequence are non-canonical variants, and even if identified, the superfamily contains many phosphatidyltransferases beyond cardiolipin synthase. The unusual bacterial-type CLS in a eukaryote makes this an item-specific identification problem rather than one solvable by general biological reasoning from sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct GO molecular function categories (binding, hydrolase, transferase, ligase). Given the experimental evidence, only C is correct. The distractors (carbohydrate binding, carboxylesterase, NAD+ synthase) do not match the protein's actual function and lack supporting sequence features.


### Important caveats

- The protein is a bacterial-type cardiolipin synthase in a eukaryote (Trypanosoma brucei), an unusual evolutionary case that limits general reasoning from eukaryotic protein family expectations.
- The UniProt GO annotation uses IMP (Inferred by Mutant Phenotype) from GeneDB plus ECO:0000315, indicating genetic/experimental evidence rather than pure sequence homology.
- The sequence match to Q584D1 is exact (SHA-256 confirmed), but the identity origin is reviewer-only; the evaluated model receives only the raw sequence.
- The CDP-alcohol phosphatidyltransferase motifs in this sequence are variant forms (DRW rather than canonical DRR; GPAVMHMRE rather than canonical GxHH), making family identification from raw sequence non-trivial.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A weak reasoning pathway exists: the sequence contains a variant CDP-alcohol phosphatidyltransferase motif ('DRWDRIQRRL' near residues 85-95, and 'GPAVMHMRE' later), which could identify the protein as a phosphatidyltransferase. Among the four options, only C (cardiolipin synthase) is a phosphatidyltransferase, while A is a binding function, B is a hydrolase, and D is a ligase/amidotransferase. However, the motifs are non-canonical variants, and identifying them from a 639-aa sequence without context is highly specialized. Moreover, the CDP-alcohol phosphatidyltransferase superfamily includes many members (PS synthase, PC synthase, CDP-DAG synthase, etc.), so even identifying the family does not specifically yield 'cardiolipin synthase' without additional knowledge.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific annotation of this protein as a bacterial-type cardiolipin synthase in a eukaryotic organism (Trypanosoma brucei) is an unusual, item-specific fact. Recognizing the sequence as Q584D1 or knowing its experimentally determined function requires database lookup or memorization. The bacterial-type CLS architecture in a eukaryote does not match typical eukaryotic CLS expectations, further limiting general reasoning.",
    "reason": "While the four options span different enzyme classes (binding, hydrolase, transferase, ligase), the primary reliable pathway to the answer is recognizing this specific protein's annotation. The CDP-alcohol phosphatidyltransferase motifs present in the sequence are non-canonical variants, and even if identified, the superfamily contains many phosphatidyltransferases beyond cardiolipin synthase. The unusual bacterial-type CLS in a eukaryote makes this an item-specific identification problem rather than one solvable by general biological reasoning from sequence."
  },
  "case_id": "GO_molecular_function_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q584D1 (CLS_TRYB2) from Trypanosoma brucei brucei. The UniProt entry explicitly names the protein 'Cardiolipin synthetase' (EC 2.7.8.-) with experimental evidence (ECO:0000269, PubMed:22451910 and PubMed:29167800). The GO annotation GO:0008808 'cardiolipin synthase activity' is assigned with IMP (Inferred by Mutant Phenotype) evidence. The catalytic reaction (2 phosphatidylglycerol → cardiolipin + glycerol) is confirmed experimentally. The expected answer C is directly supported by experimental data."
  },
  "important_caveats": [
    "The protein is a bacterial-type cardiolipin synthase in a eukaryote (Trypanosoma brucei), an unusual evolutionary case that limits general reasoning from eukaryotic protein family expectations.",
    "The UniProt GO annotation uses IMP (Inferred by Mutant Phenotype) from GeneDB plus ECO:0000315, indicating genetic/experimental evidence rather than pure sequence homology.",
    "The sequence match to Q584D1 is exact (SHA-256 confirmed), but the identity origin is reviewer-only; the evaluated model receives only the raw sequence.",
    "The CDP-alcohol phosphatidyltransferase motifs in this sequence are variant forms (DRW rather than canonical DRR; GPAVMHMRE rather than canonical GxHH), making family identification from raw sequence non-trivial."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct GO molecular function categories (binding, hydrolase, transferase, ligase). Given the experimental evidence, only C is correct. The distractors (carbohydrate binding, carboxylesterase, NAD+ synthase) do not match the protein's actual function and lack supporting sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q584D1 (CLS_TRYB2) from Trypanosoma brucei brucei. The UniProt entry explicitly names the protein 'Cardiolipin synthetase' (EC 2.7.8.-) with experimental evidence (ECO:0000269, PubMed:22451910 and PubMed:29167800). The GO annotation GO:0008808 'cardiolipin synthase activity' is assigned with IMP (Inferred by Mutant Phenotype) evidence. The catalytic reaction (2 phosphatidylglycerol → cardiolipin + glycerol) is confirmed experimentally. The expected answer C is directly supported by experimental data.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A weak reasoning pathway exists: the sequence contains a variant CDP-alcohol phosphatidyltransferase motif ('DRWDRIQRRL' near residues 85-95, and 'GPAVMHMRE' later), which could identify the protein as a phosphatidyltransferase. Among the four options, only C (cardiolipin synthase) is a phosphatidyltransferase, while A is a binding function, B is a hydrolase, and D is a ligase/amidotransferase. However, the motifs are non-canonical variants, and identifying them from a 639-aa sequence without context is highly specialized. Moreover, the CDP-alcohol phosphatidyltransferase superfamily includes many members (PS synthase, PC synthase, CDP-DAG synthase, etc.), so even identifying the family does not specifically yield 'cardiolipin synthase' without additional knowledge.",
    "missing_item_specific_fact": "The specific annotation of this protein as a bacterial-type cardiolipin synthase in a eukaryotic organism (Trypanosoma brucei) is an unusual, item-specific fact. Recognizing the sequence as Q584D1 or knowing its experimentally determined function requires database lookup or memorization. The bacterial-type CLS architecture in a eukaryote does not match typical eukaryotic CLS expectations, further limiting general reasoning.",
    "reason": "While the four options span different enzyme classes (binding, hydrolase, transferase, ligase), the primary reliable pathway to the answer is recognizing this specific protein's annotation. The CDP-alcohol phosphatidyltransferase motifs present in the sequence are non-canonical variants, and even if identified, the superfamily contains many phosphatidyltransferases beyond cardiolipin synthase. The unusual bacterial-type CLS in a eukaryote makes this an item-specific identification problem rather than one solvable by general biological reasoning from sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct GO molecular function categories (binding, hydrolase, transferase, ligase). Given the experimental evidence, only C is correct. The distractors (carbohydrate binding, carboxylesterase, NAD+ synthase) do not match the protein's actual function and lack supporting sequence features."
  },
  "important_caveats": [
    "The protein is a bacterial-type cardiolipin synthase in a eukaryote (Trypanosoma brucei), an unusual evolutionary case that limits general reasoning from eukaryotic protein family expectations.",
    "The UniProt GO annotation uses IMP (Inferred by Mutant Phenotype) from GeneDB plus ECO:0000315, indicating genetic/experimental evidence rather than pure sequence homology.",
    "The sequence match to Q584D1 is exact (SHA-256 confirmed), but the identity origin is reviewer-only; the evaluated model receives only the raw sequence.",
    "The CDP-alcohol phosphatidyltransferase motifs in this sequence are variant forms (DRW rather than canonical DRR; GPAVMHMRE rather than canonical GxHH), making family identification from raw sequence non-trivial."
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

**Accession:** `Q584D1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 102. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"22451910","source":"PubMed"}],"value":"2.7.8.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Cardiolipin synthetase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"CL synthase"}]}}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22451910","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29167800","source":"PubMed"}],"value":"Catalyzes the reversible phosphatidyl group transfer from one phosphatidylglycerol molecule to another to form cardiolipin (CL) (diphosphatidylglycerol) and glycerol (PubMed:22451910, PubMed:29167800). CL is a key phospholipid in mitochondrial membranes and plays important roles in maintaining the functional integrity and dynamics of mitochondria under both optimal and stress conditions (PubMed:22451910, PubMed:29167800)"}]}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"22451910","source":"PubMed"}],"name":"2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:31451"},{"database":"ChEBI","id":"CHEBI:17754"},{"database":"ChEBI","id":"CHEBI:62237"},{"database":"ChEBI","id":"CHEBI:64716"}]}}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.049114+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000315","id":"20382188","source":"PubMed"},{"evidenceCode":"ECO:0000315","id":"22451910","source":"PubMed"}],"id":"GO:0008808","properties":[{"key":"GoTerm","value":"F:cardiolipin synthase activity"},{"key":"GoEvidenceType","value":"IMP:GeneDB"}]}
```

Source SHA-256: `06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 80-87`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the reversible phosphatidyl group transfer from one
CC       phosphatidylglycerol molecule to another to form cardiolipin (CL)
CC       (diphosphatidylglycerol) and glycerol (PubMed:22451910,
CC       PubMed:29167800). CL is a key phospholipid in mitochondrial membranes
CC       and plays important roles in maintaining the functional integrity and
CC       dynamics of mitochondria under both optimal and stress conditions
CC       (PubMed:22451910, PubMed:29167800). {ECO:0000269|PubMed:22451910,
CC       ECO:0000269|PubMed:29167800}.
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 88-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a
CC         cardiolipin + glycerol; Xref=Rhea:RHEA:31451, ChEBI:CHEBI:17754,
CC         ChEBI:CHEBI:62237, ChEBI:CHEBI:64716;
CC         Evidence={ECO:0000305|PubMed:22451910};
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)  
**Locator:** `lines 129-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 102 / 1.  
**Retrieved:** 2026-11-02T04:31:03.966233+00:00.  

```text
DR   GO; GO:0008808; F:cardiolipin synthase activity; IMP:GeneDB.
```

Source SHA-256: `88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
