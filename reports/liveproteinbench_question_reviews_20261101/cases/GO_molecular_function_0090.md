# GO_molecular_function_0090

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — olfactory receptor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVNFTHVSEFVLLGFQGGPGMQAMLFLIFLILYGIAVVGNLGMIVIIWVDAHLHTPMYAFLQSLSLLDICYSSTIAPRALANSMQEDHTISFGGCAAQFFFLSLFGITEAFLLAAMAYDRFIAICNPLLYSVSMSHQVCVLLISGSYLWGVVNAIAQTTMTFRLPFCGSNEINDFFCDVPPLLSLSCSDTFINQLVLLGLCGSIIVSTFLIVLVSYIYIISTILRIPTMQGCQKAFSTCASHLTGVCLFFGTVFFMYAQPSAIFFMEQSKIVSIFYTMVIPMLNPLIYSLRNKEVKQALRRSMQKLSL

[Multiple Choices]
A. electron transfer activity
B. dol-P-Man:Man(8)GlcNAc(2)-PP-Dol alpha-1,2-mannosyltransferase activity
C. serine-type endopeptidase inhibitor activity
D. olfactory receptor activity
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

> The exact sequence matches the human OR9H1 record. That record identifies it as an odorant receptor and annotates olfactory receptor activity; the GO annotation is computational (IEA:InterPro), while the function statement carries ECO:0000305 rather than a cited direct assay.

Citations as saved: [H2](#evidence-h2), [H4](#evidence-h4), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple hydrophobic transmembrane regions and a class-A GPCR-like MAYDR...AIC motif, consistent with an olfactory-receptor-family GPCR. That distinguishes D from the offered enzyme, inhibitor, and electron-transfer functions.


**Missing item-specific fact**

> No separate item-specific fact is essential to distinguish these choices. The particular odorant ligand or direct receptor-response measurement is not supplied, but is not needed to select the broad molecular function offered.


**Reason**

> The sequence provides meaningful family-level evidence for an olfactory GPCR, rather than merely allowing recognition of an exact database entry. The distractors are functions of protein classes inconsistent with this sequence architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, olfactory receptor activity is the only one consistent with the sequence's GPCR-like transmembrane architecture and family motif.


### Important caveats

- The matching UniProt GO annotation is IEA:InterPro computational evidence, not a direct experimental demonstration of odorant response.
- The sequence match and database annotation support the key, but the precise historical author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic transmembrane regions and a class-A GPCR-like MAYDR...AIC motif, consistent with an olfactory-receptor-family GPCR. That distinguishes D from the offered enzyme, inhibitor, and electron-transfer functions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No separate item-specific fact is essential to distinguish these choices. The particular odorant ligand or direct receptor-response measurement is not supplied, but is not needed to select the broad molecular function offered.",
    "reason": "The sequence provides meaningful family-level evidence for an olfactory GPCR, rather than merely allowing recognition of an exact database entry. The distractors are functions of protein classes inconsistent with this sequence architecture."
  },
  "case_id": "GO_molecular_function_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H4",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the human OR9H1 record. That record identifies it as an odorant receptor and annotates olfactory receptor activity; the GO annotation is computational (IEA:InterPro), while the function statement carries ECO:0000305 rather than a cited direct assay."
  },
  "important_caveats": [
    "The matching UniProt GO annotation is IEA:InterPro computational evidence, not a direct experimental demonstration of odorant response.",
    "The sequence match and database annotation support the key, but the precise historical author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, olfactory receptor activity is the only one consistent with the sequence's GPCR-like transmembrane architecture and family motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the human OR9H1 record. That record identifies it as an odorant receptor and annotates olfactory receptor activity; the GO annotation is computational (IEA:InterPro), while the function statement carries ECO:0000305 rather than a cited direct assay.",
    "evidence_ids": ["H2", "H4", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic transmembrane regions and a class-A GPCR-like MAYDR...AIC motif, consistent with an olfactory-receptor-family GPCR. That distinguishes D from the offered enzyme, inhibitor, and electron-transfer functions.",
    "missing_item_specific_fact": "No separate item-specific fact is essential to distinguish these choices. The particular odorant ligand or direct receptor-response measurement is not supplied, but is not needed to select the broad molecular function offered.",
    "reason": "The sequence provides meaningful family-level evidence for an olfactory GPCR, rather than merely allowing recognition of an exact database entry. The distractors are functions of protein classes inconsistent with this sequence architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, olfactory receptor activity is the only one consistent with the sequence's GPCR-like transmembrane architecture and family motif."
  },
  "important_caveats": [
    "The matching UniProt GO annotation is IEA:InterPro computational evidence, not a direct experimental demonstration of odorant response.",
    "The sequence match and database annotation support the key, but the precise historical author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q6UXT6 (OR9H1_HUMAN), which is annotated as 'Olfactory receptor OR9H1' with GO:0004984 'olfactory receptor activity' (IEA:InterPro evidence). The FUNCTION comment states 'Odorant receptor' (ECO:0000305). The sequence SHA256 matches exactly. While the GO annotation is computational (IEA:InterPro), the protein is named, classified, and described as an olfactory receptor in Swiss-Prot, providing strong support for the expected answer.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 308-residue sequence exhibits a clear 7-transmembrane (7TM) GPCR topology: multiple long hydrophobic stretches (e.g., 'AMLFLIFLILYGIAVVGNLGMIVIIWVDAHLHTPMYAFLQSLSLLDICYSSTIAPRALANSMQEDHTISFGGCAAQFFFLSLFGITEAFLLAAMAYDRFIAICNPLLYSVSMSHQVCVLLISGSYLWGVVNAIAQTTMTFRLPFCGSNEINDFFCDVPPLLSLSCSDTFINQLVLLGLCGSIIVSTFLIVLVSYIYIISTILRIPTMQGCQKAFSTCASHLTGVCLFFGTVFFMYAQPSAIFFMEQSKIVSIFYTMVIPMLNPLIYSLRNKEVKQALRRSMQKLSL'), a conserved DRY-like motif region, and the characteristic C-terminal 'NPLIYSLRNKEV' GPCR motif. This architecture is incompatible with electron transfer proteins (cytochromes/ferredoxins, option A), glycosyltransferases (soluble or single-pass enzymes with catalytic domains, option B), or serine protease inhibitors (small secreted proteins, option C). Among the four options, only olfactory receptor activity (D) describes a 7TM GPCR, making the answer distinguishable by recognizing the transmembrane topology from the hydrophobic pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 7TM GPCR architecture is identifiable from the sequence's hydrophobic pattern and conserved motifs. Since the other three options describe fundamentally different protein classes (redox proteins, enzymes, small inhibitors) that are incompatible with a 7TM membrane receptor of ~300 residues, general biological reasoning about protein topology and function class is sufficient to select D without memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mutually exclusive protein functional classes (redox carrier, glycosyltransferase enzyme, protease inhibitor, 7TM receptor). The 7TM topology evident in the sequence uniquely points to the receptor option. No other option is compatible with the observed architecture.


### Important caveats

- The GO:0004984 annotation carries IEA:InterPro evidence (computational inference from family membership), not direct experimental ligand-binding data for this specific receptor.
- The protein is named OR9H1 but is also listed with synonym OR9H1P, suggesting it may be a pseudogene or have limited functional characterization; however, the molecular function annotation as olfactory receptor is maintained.
- The reviewer-only accession identification was inferred from dataset metadata; the evaluated model sees only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 308-residue sequence exhibits a clear 7-transmembrane (7TM) GPCR topology: multiple long hydrophobic stretches (e.g., 'AMLFLIFLILYGIAVVGNLGMIVIIWVDAHLHTPMYAFLQSLSLLDICYSSTIAPRALANSMQEDHTISFGGCAAQFFFLSLFGITEAFLLAAMAYDRFIAICNPLLYSVSMSHQVCVLLISGSYLWGVVNAIAQTTMTFRLPFCGSNEINDFFCDVPPLLSLSCSDTFINQLVLLGLCGSIIVSTFLIVLVSYIYIISTILRIPTMQGCQKAFSTCASHLTGVCLFFGTVFFMYAQPSAIFFMEQSKIVSIFYTMVIPMLNPLIYSLRNKEVKQALRRSMQKLSL'), a conserved DRY-like motif region, and the characteristic C-terminal 'NPLIYSLRNKEV' GPCR motif. This architecture is incompatible with electron transfer proteins (cytochromes/ferredoxins, option A), glycosyltransferases (soluble or single-pass enzymes with catalytic domains, option B), or serine protease inhibitors (small secreted proteins, option C). Among the four options, only olfactory receptor activity (D) describes a 7TM GPCR, making the answer distinguishable by recognizing the transmembrane topology from the hydrophobic pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 7TM GPCR architecture is identifiable from the sequence's hydrophobic pattern and conserved motifs. Since the other three options describe fundamentally different protein classes (redox proteins, enzymes, small inhibitors) that are incompatible with a 7TM membrane receptor of ~300 residues, general biological reasoning about protein topology and function class is sufficient to select D without memorizing the specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0090",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q6UXT6 (OR9H1_HUMAN), which is annotated as 'Olfactory receptor OR9H1' with GO:0004984 'olfactory receptor activity' (IEA:InterPro evidence). The FUNCTION comment states 'Odorant receptor' (ECO:0000305). The sequence SHA256 matches exactly. While the GO annotation is computational (IEA:InterPro), the protein is named, classified, and described as an olfactory receptor in Swiss-Prot, providing strong support for the expected answer."
  },
  "important_caveats": [
    "The GO:0004984 annotation carries IEA:InterPro evidence (computational inference from family membership), not direct experimental ligand-binding data for this specific receptor.",
    "The protein is named OR9H1 but is also listed with synonym OR9H1P, suggesting it may be a pseudogene or have limited functional characterization; however, the molecular function annotation as olfactory receptor is maintained.",
    "The reviewer-only accession identification was inferred from dataset metadata; the evaluated model sees only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive protein functional classes (redox carrier, glycosyltransferase enzyme, protease inhibitor, 7TM receptor). The 7TM topology evident in the sequence uniquely points to the receptor option. No other option is compatible with the observed architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0090",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q6UXT6 (OR9H1_HUMAN), which is annotated as 'Olfactory receptor OR9H1' with GO:0004984 'olfactory receptor activity' (IEA:InterPro evidence). The FUNCTION comment states 'Odorant receptor' (ECO:0000305). The sequence SHA256 matches exactly. While the GO annotation is computational (IEA:InterPro), the protein is named, classified, and described as an olfactory receptor in Swiss-Prot, providing strong support for the expected answer.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 308-residue sequence exhibits a clear 7-transmembrane (7TM) GPCR topology: multiple long hydrophobic stretches (e.g., 'AMLFLIFLILYGIAVVGNLGMIVIIWVDAHLHTPMYAFLQSLSLLDICYSSTIAPRALANSMQEDHTISFGGCAAQFFFLSLFGITEAFLLAAMAYDRFIAICNPLLYSVSMSHQVCVLLISGSYLWGVVNAIAQTTMTFRLPFCGSNEINDFFCDVPPLLSLSCSDTFINQLVLLGLCGSIIVSTFLIVLVSYIYIISTILRIPTMQGCQKAFSTCASHLTGVCLFFGTVFFMYAQPSAIFFMEQSKIVSIFYTMVIPMLNPLIYSLRNKEVKQALRRSMQKLSL'), a conserved DRY-like motif region, and the characteristic C-terminal 'NPLIYSLRNKEV' GPCR motif. This architecture is incompatible with electron transfer proteins (cytochromes/ferredoxins, option A), glycosyltransferases (soluble or single-pass enzymes with catalytic domains, option B), or serine protease inhibitors (small secreted proteins, option C). Among the four options, only olfactory receptor activity (D) describes a 7TM GPCR, making the answer distinguishable by recognizing the transmembrane topology from the hydrophobic pattern.",
    "missing_item_specific_fact": "",
    "reason": "The 7TM GPCR architecture is identifiable from the sequence's hydrophobic pattern and conserved motifs. Since the other three options describe fundamentally different protein classes (redox proteins, enzymes, small inhibitors) that are incompatible with a 7TM membrane receptor of ~300 residues, general biological reasoning about protein topology and function class is sufficient to select D without memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mutually exclusive protein functional classes (redox carrier, glycosyltransferase enzyme, protease inhibitor, 7TM receptor). The 7TM topology evident in the sequence uniquely points to the receptor option. No other option is compatible with the observed architecture."
  },
  "important_caveats": [
    "The GO:0004984 annotation carries IEA:InterPro evidence (computational inference from family membership), not direct experimental ligand-binding data for this specific receptor.",
    "The protein is named OR9H1 but is also listed with synonym OR9H1P, suggesting it may be a pseudogene or have limited functional characterization; however, the molecular function annotation as olfactory receptor is maintained.",
    "The reviewer-only accession identification was inferred from dataset metadata; the evaluated model sees only the raw sequence."
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

**Accession:** `Q6UXT6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 106. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
"Q6UXT6"
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Olfactory receptor family 9 subfamily H member 1"}}],"recommendedName":{"fullName":{"value":"Olfactory receptor OR9H1"}}}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Odorant receptor"}]}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6UXT6.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:45.136978+00:00.  

```json
{"database":"GO","id":"GO:0004984","properties":[{"key":"GoTerm","value":"F:olfactory receptor activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `d761824ae03c221d019ed712f82a29f42f3f5f479f6233c26b23ed7827f111d1`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
ID   OR9H1_HUMAN             Reviewed;         308 AA.
AC   Q6UXT6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2004, sequence version 1.
DT   28-JAN-2026, entry version 106.
DE   RecName: Full=Olfactory receptor OR9H1;
DE   AltName: Full=Olfactory receptor family 9 subfamily H member 1;
GN   Name=OR9H1 {ECO:0000312|HGNC:HGNC:15038};
GN   Synonyms=OR9H1P {ECO:0000312|HGNC:HGNC:15038}; ORFNames=UNQ9373;
OS   Homo sapiens (Human).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;
OC   Homo.
OX   NCBI_TaxID=9606;
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 65-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
CC   -!- FUNCTION: Odorant receptor. {ECO:0000305}.
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6UXT6?format=txt&versions=106)  
**Locator:** `lines 97-97`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 106 / 1.  
**Retrieved:** 2026-11-02T04:31:47.614110+00:00.  

```text
DR   GO; GO:0004984; F:olfactory receptor activity; IEA:InterPro.
```

Source SHA-256: `072cef681e411cc08becb56d888ebce42ad8a93eca1ca016afab23f858b5896a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 90. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
