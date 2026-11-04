# cofactor_0083

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0083.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — pyridoxal 5&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKDLFEHIYANKGSIGRWSDHAEGYYVFPKLEGELGPHMKFQGKEILNWSINDYLGLANHPEVRKVDAEAAAEYGAAYPMGARMMSGHTTMHEELEKRLAKFVHKEASYLLNFGYQGMVSIIDALVTKNDVIVYDVDAHACIIDGVRLHFGKRYTYQHNDMESFEKNLERAAKLAETTGGGILVISEGVFGMRGEQGKLKEIVALKKKYPFRLLVDDAHGFGTLGPRGEGTGVHQGVQDEIDVYFSTFAKSMAGIGAFVAGNAKVVDYLKYNLRSQMFAKSLPMIYVKGALKRLEMMETMPELQQKLWDNVNRLQNGLKERGFNIGNTNTCVTPVFLHGSIPEAMAMVNDLREHYGIFLSIVVYPVIPKGMILLRIIPTASHSKEDIDRTLEAFSAIREKLETGVYRAINAELTKEMGDM

[Multiple Choices]
A. FAD
B. Mn(2+)
C. pyridoxal 5'-phosphate
D. Zn(2+)
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies pyridoxal 5'-phosphate as the cofactor and assigns experimental evidence linked to a publication. This supports choice C, though the primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 420-aa soluble-enzyme sequence is compatible with a PLP-dependent enzyme family: such enzymes commonly use a conserved lysine to bind PLP as an internal aldimine. A sequence-family inference of that kind meaningfully favors PLP over FAD, for which a characteristic nucleotide-binding motif is not apparent here, or the metal-ion choices, which would generally be supported by recognizable metal-binding features. This is a probabilistic inference, not proof from the sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable sequence-family inference can distinguish PLP from the offered alternatives without knowing this exact protein's database record. The evidence is not conclusive from the sequence alone, but exact-target lookup is not necessary for a meaningful choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports PLP, and no other offered choice is comparably supported.


### Important caveats

- The database annotation cites experimental evidence, but the underlying study was not independently examined.
- The sequence-based family inference is probabilistic; sequence alone does not establish the cofactor experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 420-aa soluble-enzyme sequence is compatible with a PLP-dependent enzyme family: such enzymes commonly use a conserved lysine to bind PLP as an internal aldimine. A sequence-family inference of that kind meaningfully favors PLP over FAD, for which a characteristic nucleotide-binding motif is not apparent here, or the metal-ion choices, which would generally be supported by recognizable metal-binding features. This is a probabilistic inference, not proof from the sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-family inference can distinguish PLP from the offered alternatives without knowing this exact protein's database record. The evidence is not conclusive from the sequence alone, but exact-target lookup is not necessary for a meaningful choice."
  },
  "case_id": "cofactor_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies pyridoxal 5'-phosphate as the cofactor and assigns experimental evidence linked to a publication. This supports choice C, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the underlying study was not independently examined.",
    "The sequence-based family inference is probabilistic; sequence alone does not establish the cofactor experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports PLP, and no other offered choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies pyridoxal 5'-phosphate as the cofactor and assigns experimental evidence linked to a publication. This supports choice C, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C5", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 420-aa soluble-enzyme sequence is compatible with a PLP-dependent enzyme family: such enzymes commonly use a conserved lysine to bind PLP as an internal aldimine. A sequence-family inference of that kind meaningfully favors PLP over FAD, for which a characteristic nucleotide-binding motif is not apparent here, or the metal-ion choices, which would generally be supported by recognizable metal-binding features. This is a probabilistic inference, not proof from the sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-family inference can distinguish PLP from the offered alternatives without knowing this exact protein's database record. The evidence is not conclusive from the sequence alone, but exact-target lookup is not necessary for a meaningful choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports PLP, and no other offered choice is comparably supported."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the underlying study was not independently examined.",
    "The sequence-based family inference is probabilistic; sequence alone does not establish the cofactor experimentally."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C7M8J6 (sequence matched exactly) explicitly annotates pyridoxal 5'-phosphate as the cofactor with experimental evidence (ECO:0000269, PubMed:35414181, Liu et al. Biochemistry 2022). The protein is Cysteate-C-fatty acyltransferase (CapB, EC 2.3.1.-) from Capnocytophaga ochracea, involved in sulfonolipid capnine biosynthesis. The cofactor annotation is backed by experimental characterization, not merely computational prediction.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple well-characterized motifs diagnostic of the fold-type I PLP-dependent enzyme superfamily: (1) the 'DAHG' motif in 'DDAHGFGTLGPRGEGTGVHQGVQDEIDVYFSTFAKSMAGIGAFVAGNAKVVDYLKY', a hallmark of fold-type I PLP enzymes found across hundreds of aminotransferases, decarboxylases, and racemases; (2) the 'GVFG' motif in 'ISEGVFGMRGEQ', another conserved PLP-binding signature in this superfamily; (3) the 'GAF' motif in 'SMAGIGAFVAGNAKVVDYLKY'. These motifs are broadly shared across the fold-type I PLP enzyme family and are not found in FAD-dependent (Rossmann-fold GxGxxG) proteins, Mn-binding phosphatases/decarboxylases (DxD motifs), or Zn-binding enzymes (Cys/His-rich clusters). A knowledgeable model recognizing these family-level sequence signatures can confidently assign PLP over the other three alternatives without knowing this specific protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The fold-type I PLP enzyme motifs (DAHG, GVFG, GAF) are extensively characterized across the aminotransferase/decarboxylase/racemase superfamily and constitute a well-known, transferable sequence signature. Their presence in this sequence meaningfully distinguishes PLP (C) from FAD (A), Mn2+ (B), and Zn2+ (D). The inference relies on family-level pattern recognition learned from many other PLP-dependent enzymes, not on memorizing this particular protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The fold-type I PLP motifs are clearly present and are inconsistent with FAD-binding Rossmann folds, Mn-binding catalytic centers, or Zn-binding Cys/His clusters. The four options are well-distinguished by sequence-level family signatures.


### Important caveats

- The protein's unusual catalytic function (C-C bond formation in sulfonolipid biosynthesis, EC 2.3.1.-) is atypical for a fold-type I PLP enzyme, but the PLP cofactor requirement is experimentally confirmed.
- The sequence is 420 amino acids, consistent with a fold-type I PLP enzyme (~400-450 aa typical range), further supporting the family assignment.
- The UniProt annotation is Swiss-Prot reviewed with experimental evidence, providing high confidence for the expected answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple well-characterized motifs diagnostic of the fold-type I PLP-dependent enzyme superfamily: (1) the 'DAHG' motif in 'DDAHGFGTLGPRGEGTGVHQGVQDEIDVYFSTFAKSMAGIGAFVAGNAKVVDYLKY', a hallmark of fold-type I PLP enzymes found across hundreds of aminotransferases, decarboxylases, and racemases; (2) the 'GVFG' motif in 'ISEGVFGMRGEQ', another conserved PLP-binding signature in this superfamily; (3) the 'GAF' motif in 'SMAGIGAFVAGNAKVVDYLKY'. These motifs are broadly shared across the fold-type I PLP enzyme family and are not found in FAD-dependent (Rossmann-fold GxGxxG) proteins, Mn-binding phosphatases/decarboxylases (DxD motifs), or Zn-binding enzymes (Cys/His-rich clusters). A knowledgeable model recognizing these family-level sequence signatures can confidently assign PLP over the other three alternatives without knowing this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The fold-type I PLP enzyme motifs (DAHG, GVFG, GAF) are extensively characterized across the aminotransferase/decarboxylase/racemase superfamily and constitute a well-known, transferable sequence signature. Their presence in this sequence meaningfully distinguishes PLP (C) from FAD (A), Mn2+ (B), and Zn2+ (D). The inference relies on family-level pattern recognition learned from many other PLP-dependent enzymes, not on memorizing this particular protein's annotation."
  },
  "case_id": "cofactor_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C7M8J6 (sequence matched exactly) explicitly annotates pyridoxal 5'-phosphate as the cofactor with experimental evidence (ECO:0000269, PubMed:35414181, Liu et al. Biochemistry 2022). The protein is Cysteate-C-fatty acyltransferase (CapB, EC 2.3.1.-) from Capnocytophaga ochracea, involved in sulfonolipid capnine biosynthesis. The cofactor annotation is backed by experimental characterization, not merely computational prediction."
  },
  "important_caveats": [
    "The protein's unusual catalytic function (C-C bond formation in sulfonolipid biosynthesis, EC 2.3.1.-) is atypical for a fold-type I PLP enzyme, but the PLP cofactor requirement is experimentally confirmed.",
    "The sequence is 420 amino acids, consistent with a fold-type I PLP enzyme (~400-450 aa typical range), further supporting the family assignment.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence, providing high confidence for the expected answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The fold-type I PLP motifs are clearly present and are inconsistent with FAD-binding Rossmann folds, Mn-binding catalytic centers, or Zn-binding Cys/His clusters. The four options are well-distinguished by sequence-level family signatures."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C7M8J6 (sequence matched exactly) explicitly annotates pyridoxal 5'-phosphate as the cofactor with experimental evidence (ECO:0000269, PubMed:35414181, Liu et al. Biochemistry 2022). The protein is Cysteate-C-fatty acyltransferase (CapB, EC 2.3.1.-) from Capnocytophaga ochracea, involved in sulfonolipid capnine biosynthesis. The cofactor annotation is backed by experimental characterization, not merely computational prediction.",
    "evidence_ids": ["C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple well-characterized motifs diagnostic of the fold-type I PLP-dependent enzyme superfamily: (1) the 'DAHG' motif in 'DDAHGFGTLGPRGEGTGVHQGVQDEIDVYFSTFAKSMAGIGAFVAGNAKVVDYLKY', a hallmark of fold-type I PLP enzymes found across hundreds of aminotransferases, decarboxylases, and racemases; (2) the 'GVFG' motif in 'ISEGVFGMRGEQ', another conserved PLP-binding signature in this superfamily; (3) the 'GAF' motif in 'SMAGIGAFVAGNAKVVDYLKY'. These motifs are broadly shared across the fold-type I PLP enzyme family and are not found in FAD-dependent (Rossmann-fold GxGxxG) proteins, Mn-binding phosphatases/decarboxylases (DxD motifs), or Zn-binding enzymes (Cys/His-rich clusters). A knowledgeable model recognizing these family-level sequence signatures can confidently assign PLP over the other three alternatives without knowing this specific protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "The fold-type I PLP enzyme motifs (DAHG, GVFG, GAF) are extensively characterized across the aminotransferase/decarboxylase/racemase superfamily and constitute a well-known, transferable sequence signature. Their presence in this sequence meaningfully distinguishes PLP (C) from FAD (A), Mn2+ (B), and Zn2+ (D). The inference relies on family-level pattern recognition learned from many other PLP-dependent enzymes, not on memorizing this particular protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The fold-type I PLP motifs are clearly present and are inconsistent with FAD-binding Rossmann folds, Mn-binding catalytic centers, or Zn-binding Cys/His clusters. The four options are well-distinguished by sequence-level family signatures."
  },
  "important_caveats": [
    "The protein's unusual catalytic function (C-C bond formation in sulfonolipid biosynthesis, EC 2.3.1.-) is atypical for a fold-type I PLP enzyme, but the PLP cofactor requirement is experimentally confirmed.",
    "The sequence is 420 amino acids, consistent with a fold-type I PLP enzyme (~400-450 aa typical range), further supporting the family assignment.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence, providing high confidence for the expected answer."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 420,
  "benchmark_sequence_sha256": "dd4259a5352210ed873f594b99e98145868737457d8a910589f73654ca4ff470",
  "current_entry_audit": {
    "entryVersion": 71,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-10-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 420,
  "current_source_sequence_sha256": "dd4259a5352210ed873f594b99e98145868737457d8a910589f73654ca4ff470",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 70,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C7M8J6",
  "selected_historical_entry_version": 70,
  "selected_historical_record_sha256": "a7856db74c2257c0ae32918e6ed89fb2b1448ac6527c4a62ff2b4a4bf082737a",
  "selected_historical_source_sequence_length": 420,
  "selected_historical_source_sequence_sha256": "dd4259a5352210ed873f594b99e98145868737457d8a910589f73654ca4ff470",
  "selected_historical_version": {
    "accession": "C7M8J6",
    "database": "Swiss-Prot",
    "entryVersion": 70,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "CAPB_CAPOD",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C7M8J6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:36.271476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":71,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-10-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:36.271476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacteroides ochraceus\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Bacteroidota\",\"Flavobacteriia\",\"Flavobacteriales\",\"Flavobacteriaceae\",\"Capnocytophaga\"],\"scientificName\":\"Capnocytophaga ochracea (strain ATCC 27872 / DSM 7271 / CCUG 9716 / JCM 12966 / NCTC 12371 / SS31 / VPI 2845)\",\"taxonId\":521097}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:36.271476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"Cysteate-C-fatty acyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:36.271476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:597326\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"name\":\"pyridoxal 5'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:36.271476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu Y.\",\"Wei Y.\",\"Teh T.M.\",\"Liu D.\",\"Zhou Y.\",\"Zhao S.\",\"Ang E.L.\",\"Zhao H.\",\"Zhang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35414181\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.2c00102\"}],\"citationType\":\"journal article\",\"firstPage\":\"2861\",\"id\":\"35414181\",\"journal\":\"Biochemistry\",\"lastPage\":\"2869\",\"publicationDate\":\"2022\",\"title\":\"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.\",\"volume\":\"61\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:36.271476+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b57fb928124b749a162ca2d4352e7e955e837f2a249eb7bd4c46e97dc2bd72a0",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H1",
  "excerpt": "ID   CAPB_CAPOD              Reviewed;         420 AA.\nAC   C7M8J6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-OCT-2009, sequence version 1.\nDT   28-JAN-2026, entry version 70.\nDE   RecName: Full=Cysteate-C-fatty acyltransferase {ECO:0000303|PubMed:35414181};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:35414181};\nGN   Name=capB {ECO:0000303|PubMed:35414181};\nGN   OrderedLocusNames=Coch_1830 {ECO:0000312|EMBL:ACU93375.1};\nOS   Capnocytophaga ochracea (strain ATCC 27872 / DSM 7271 / CCUG 9716 / JCM\nOS   12966 / NCTC 12371 / SS31 / VPI 2845) (Bacteroides ochraceus).\nOC   Bacteria; Pseudomonadati; Bacteroidota; Flavobacteriia; Flavobacteriales;\nOC   Flavobacteriaceae; Capnocytophaga.\nOX   NCBI_TaxID=521097;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:41.947109+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a7856db74c2257c0ae32918e6ed89fb2b1448ac6527c4a62ff2b4a4bf082737a",
  "url": "https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cysteate-C-fatty acyltransferase {ECO:0000303|PubMed:35414181};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:35414181};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:41.947109+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a7856db74c2257c0ae32918e6ed89fb2b1448ac6527c4a62ff2b4a4bf082737a",
  "url": "https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND COFACTOR.\nRX   PubMed=35414181; DOI=10.1021/acs.biochem.2c00102;\nRA   Liu Y., Wei Y., Teh T.M., Liu D., Zhou Y., Zhao S., Ang E.L., Zhao H.,\nRA   Zhang Y.;\nRT   \"Identification and Characterization of the Biosynthetic Pathway of the\nRT   Sulfonolipid Capnine.\";\nRL   Biochemistry 61:2861-2869(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:41.947109+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a7856db74c2257c0ae32918e6ed89fb2b1448ac6527c4a62ff2b4a4bf082737a",
  "url": "https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70)

```json
{
  "entry_version": 70,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;\nCC         Evidence={ECO:0000269|PubMed:35414181};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:41.947109+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a7856db74c2257c0ae32918e6ed89fb2b1448ac6527c4a62ff2b4a4bf082737a",
  "url": "https://rest.uniprot.org/unisave/C7M8J6?format=txt&versions=70"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 83. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
