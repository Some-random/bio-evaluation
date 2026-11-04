# GO_molecular_function_0119

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0119.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — cardiolipin synthase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

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
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches the annotated protein sequence. The matched record describes cardiolipin synthesis and gives experimental evidence for that function, supporting choice C; it also records the corresponding GO molecular-function term.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two HxKxxxxD motifs (including HRKILIVD and HAKTVVAD). Tandem HKD motifs are characteristic of phospholipase-D-superfamily enzymes, a family that includes bacterial-type cardiolipin synthases. This provides a transferable sequence-family basis for choosing cardiolipin synthase over the unrelated binding, carboxylesterase, and NAD+ synthase alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The family-level motif pattern meaningfully distinguishes the offered cardiolipin synthase option without relying on the target's database record. It supports an inference rather than proving the exact substrate specificity by itself.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct molecular functions, and the sequence-family inference favors cardiolipin synthase.


### Important caveats

- The sequence-based family inference is not a substitute for direct biochemical characterization; the reviewer-only record supplies experimental support for the keyed function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two HxKxxxxD motifs (including HRKILIVD and HAKTVVAD). Tandem HKD motifs are characteristic of phospholipase-D-superfamily enzymes, a family that includes bacterial-type cardiolipin synthases. This provides a transferable sequence-family basis for choosing cardiolipin synthase over the unrelated binding, carboxylesterase, and NAD+ synthase alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The family-level motif pattern meaningfully distinguishes the offered cardiolipin synthase option without relying on the target's database record. It supports an inference rather than proving the exact substrate specificity by itself."
  },
  "case_id": "GO_molecular_function_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein sequence. The matched record describes cardiolipin synthesis and gives experimental evidence for that function, supporting choice C; it also records the corresponding GO molecular-function term."
  },
  "important_caveats": [
    "The sequence-based family inference is not a substitute for direct biochemical characterization; the reviewer-only record supplies experimental support for the keyed function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct molecular functions, and the sequence-family inference favors cardiolipin synthase."
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
    "reason": "The supplied sequence matches the annotated protein sequence. The matched record describes cardiolipin synthesis and gives experimental evidence for that function, supporting choice C; it also records the corresponding GO molecular-function term.",
    "evidence_ids": ["H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two HxKxxxxD motifs (including HRKILIVD and HAKTVVAD). Tandem HKD motifs are characteristic of phospholipase-D-superfamily enzymes, a family that includes bacterial-type cardiolipin synthases. This provides a transferable sequence-family basis for choosing cardiolipin synthase over the unrelated binding, carboxylesterase, and NAD+ synthase alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The family-level motif pattern meaningfully distinguishes the offered cardiolipin synthase option without relying on the target's database record. It supports an inference rather than proving the exact substrate specificity by itself."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct molecular functions, and the sequence-family inference favors cardiolipin synthase."
  },
  "important_caveats": [
    "The sequence-based family inference is not a substitute for direct biochemical characterization; the reviewer-only record supplies experimental support for the keyed function."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q584D1 (CLS_TRYB2, 639 AA, sequence SHA256 matched) is annotated as Cardiolipin synthetase (EC 2.7.8.-) with GO:0008808 (cardiolipin synthase activity). The function is supported by two experimental studies (PubMed:22451910, PubMed:29167800, ECO:0000269) demonstrating reversible phosphatidyl group transfer from phosphatidylglycerol to form cardiolipin. The GO annotation carries IMP:GeneDB evidence. The sequence in the question matches the canonical entry exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can use elimination and positive family-level inference. (1) Carboxylesterase (B): Serine carboxylesterases require a classic α/β-hydrolase fold with a GxSxG catalytic motif and a Ser-His-Asp triad. The 639-residue sequence lacks a convincing GxSxG motif and does not display the compact α/β-hydrolase architecture typical of carboxylesterases (~500 AA, distinct fold). This eliminates B. (2) NAD+ synthase (D): NAD synthetase (EC 6.3.5.1) has a characteristic glutaminase (GATase) domain with a Cys-His-Glu triad and a synthetase domain with a PP-loop. The sequence shows no GATase-domain signature (no conserved Cys-His-Glu arrangement in the expected geometry) and no synthetase PP-loop, eliminating D. (3) Carbohydrate derivative binding (A): This is a binding GO term; the protein is 639 residues with multiple internal catalytic-appearing motifs (e.g., conserved DD pairs, GxGxxG-like patterns such as 'GFCGGLNIG', 'GDDVATTD', 'GPAVMHMRE') inconsistent with a simple binding protein. (4) Cardiolipin synthase (C): The bacterial-type CLS (ClsA) belongs to the CDP-diacylglycerol synthase (CDS) superfamily (Pfam PF02244), a phosphatidyltransferase family sharing conserved motifs including GxGxxG-like patterns and catalytic aspartate pairs. The sequence contains suggestive CDS-like motifs ('GFCGGLNIG' resembling GxGxxG, 'ICKDDFVG' with catalytic DD, 'GPAVMHMRE' with a GPA motif seen in phosphatidyltransferases). Recognizing these as consistent with the CDS/phosphatidyltransferase superfamily, and noting that among the four options only C corresponds to a phosphatidyltransferase, meaningfully distinguishes C from A, B, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The four options span four very different molecular-function classes (binding, hydrolase, phosphatidyltransferase, ligase). Transferable knowledge of protein folds and catalytic motifs allows elimination of B (no serine-hydrolase fold), D (no GATase/synthetase architecture), and A (catalytic-scale protein with internal motifs inconsistent with a pure binding role). The residual phosphatidyltransferase-like sequence features (GxGxxG-like motifs, conserved Asp pairs) point toward C, the only phosphatidyltransferase option. This is a family-level inference from other proteins (E. coli CdsA, ClsA, and related CDS-family members) applied to a divergent Trypanosoma homolog, which is permitted transferable reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular-function categories (binding vs. hydrolase vs. phosphatidyltransferase vs. ligase). The sequence features and fold-level reasoning cleanly separate C from A, B, and D. No two options are close enough to be confused by a knowledgeable model.


### Important caveats

- The Trypanosoma CLS is a bacterial-type (ClsA-like) enzyme in a eukaryote, a somewhat unusual evolutionary context noted in the 2012 paper. A model must recognize CDS-family homology in a divergent eukaryotic sequence, which adds difficulty but does not change the family-level reasoning.
- The CDS-like motifs in this sequence are not as crisp as in well-studied E. coli CdsA; recognition relies on pattern-level analogy rather than exact motif identity.
- The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning above relies only on the sequence and general protein-family knowledge.
- The GO annotation evidence code is IMP (inferred by mutant phenotype) via GeneDB, supplemented by direct biochemical assays (ECO:0000269), providing strong experimental support for the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can use elimination and positive family-level inference. (1) Carboxylesterase (B): Serine carboxylesterases require a classic α/β-hydrolase fold with a GxSxG catalytic motif and a Ser-His-Asp triad. The 639-residue sequence lacks a convincing GxSxG motif and does not display the compact α/β-hydrolase architecture typical of carboxylesterases (~500 AA, distinct fold). This eliminates B. (2) NAD+ synthase (D): NAD synthetase (EC 6.3.5.1) has a characteristic glutaminase (GATase) domain with a Cys-His-Glu triad and a synthetase domain with a PP-loop. The sequence shows no GATase-domain signature (no conserved Cys-His-Glu arrangement in the expected geometry) and no synthetase PP-loop, eliminating D. (3) Carbohydrate derivative binding (A): This is a binding GO term; the protein is 639 residues with multiple internal catalytic-appearing motifs (e.g., conserved DD pairs, GxGxxG-like patterns such as 'GFCGGLNIG', 'GDDVATTD', 'GPAVMHMRE') inconsistent with a simple binding protein. (4) Cardiolipin synthase (C): The bacterial-type CLS (ClsA) belongs to the CDP-diacylglycerol synthase (CDS) superfamily (Pfam PF02244), a phosphatidyltransferase family sharing conserved motifs including GxGxxG-like patterns and catalytic aspartate pairs. The sequence contains suggestive CDS-like motifs ('GFCGGLNIG' resembling GxGxxG, 'ICKDDFVG' with catalytic DD, 'GPAVMHMRE' with a GPA motif seen in phosphatidyltransferases). Recognizing these as consistent with the CDS/phosphatidyltransferase superfamily, and noting that among the four options only C corresponds to a phosphatidyltransferase, meaningfully distinguishes C from A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The four options span four very different molecular-function classes (binding, hydrolase, phosphatidyltransferase, ligase). Transferable knowledge of protein folds and catalytic motifs allows elimination of B (no serine-hydrolase fold), D (no GATase/synthetase architecture), and A (catalytic-scale protein with internal motifs inconsistent with a pure binding role). The residual phosphatidyltransferase-like sequence features (GxGxxG-like motifs, conserved Asp pairs) point toward C, the only phosphatidyltransferase option. This is a family-level inference from other proteins (E. coli CdsA, ClsA, and related CDS-family members) applied to a divergent Trypanosoma homolog, which is permitted transferable reasoning."
  },
  "case_id": "GO_molecular_function_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q584D1 (CLS_TRYB2, 639 AA, sequence SHA256 matched) is annotated as Cardiolipin synthetase (EC 2.7.8.-) with GO:0008808 (cardiolipin synthase activity). The function is supported by two experimental studies (PubMed:22451910, PubMed:29167800, ECO:0000269) demonstrating reversible phosphatidyl group transfer from phosphatidylglycerol to form cardiolipin. The GO annotation carries IMP:GeneDB evidence. The sequence in the question matches the canonical entry exactly."
  },
  "important_caveats": [
    "The Trypanosoma CLS is a bacterial-type (ClsA-like) enzyme in a eukaryote, a somewhat unusual evolutionary context noted in the 2012 paper. A model must recognize CDS-family homology in a divergent eukaryotic sequence, which adds difficulty but does not change the family-level reasoning.",
    "The CDS-like motifs in this sequence are not as crisp as in well-studied E. coli CdsA; recognition relies on pattern-level analogy rather than exact motif identity.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning above relies only on the sequence and general protein-family knowledge.",
    "The GO annotation evidence code is IMP (inferred by mutant phenotype) via GeneDB, supplemented by direct biochemical assays (ECO:0000269), providing strong experimental support for the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular-function categories (binding vs. hydrolase vs. phosphatidyltransferase vs. ligase). The sequence features and fold-level reasoning cleanly separate C from A, B, and D. No two options are close enough to be confused by a knowledgeable model."
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
    "reason": "The UniProt entry Q584D1 (CLS_TRYB2, 639 AA, sequence SHA256 matched) is annotated as Cardiolipin synthetase (EC 2.7.8.-) with GO:0008808 (cardiolipin synthase activity). The function is supported by two experimental studies (PubMed:22451910, PubMed:29167800, ECO:0000269) demonstrating reversible phosphatidyl group transfer from phosphatidylglycerol to form cardiolipin. The GO annotation carries IMP:GeneDB evidence. The sequence in the question matches the canonical entry exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "H1", "H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can use elimination and positive family-level inference. (1) Carboxylesterase (B): Serine carboxylesterases require a classic α/β-hydrolase fold with a GxSxG catalytic motif and a Ser-His-Asp triad. The 639-residue sequence lacks a convincing GxSxG motif and does not display the compact α/β-hydrolase architecture typical of carboxylesterases (~500 AA, distinct fold). This eliminates B. (2) NAD+ synthase (D): NAD synthetase (EC 6.3.5.1) has a characteristic glutaminase (GATase) domain with a Cys-His-Glu triad and a synthetase domain with a PP-loop. The sequence shows no GATase-domain signature (no conserved Cys-His-Glu arrangement in the expected geometry) and no synthetase PP-loop, eliminating D. (3) Carbohydrate derivative binding (A): This is a binding GO term; the protein is 639 residues with multiple internal catalytic-appearing motifs (e.g., conserved DD pairs, GxGxxG-like patterns such as 'GFCGGLNIG', 'GDDVATTD', 'GPAVMHMRE') inconsistent with a simple binding protein. (4) Cardiolipin synthase (C): The bacterial-type CLS (ClsA) belongs to the CDP-diacylglycerol synthase (CDS) superfamily (Pfam PF02244), a phosphatidyltransferase family sharing conserved motifs including GxGxxG-like patterns and catalytic aspartate pairs. The sequence contains suggestive CDS-like motifs ('GFCGGLNIG' resembling GxGxxG, 'ICKDDFVG' with catalytic DD, 'GPAVMHMRE' with a GPA motif seen in phosphatidyltransferases). Recognizing these as consistent with the CDS/phosphatidyltransferase superfamily, and noting that among the four options only C corresponds to a phosphatidyltransferase, meaningfully distinguishes C from A, B, and D.",
    "missing_item_specific_fact": "",
    "reason": "The four options span four very different molecular-function classes (binding, hydrolase, phosphatidyltransferase, ligase). Transferable knowledge of protein folds and catalytic motifs allows elimination of B (no serine-hydrolase fold), D (no GATase/synthetase architecture), and A (catalytic-scale protein with internal motifs inconsistent with a pure binding role). The residual phosphatidyltransferase-like sequence features (GxGxxG-like motifs, conserved Asp pairs) point toward C, the only phosphatidyltransferase option. This is a family-level inference from other proteins (E. coli CdsA, ClsA, and related CDS-family members) applied to a divergent Trypanosoma homolog, which is permitted transferable reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular-function categories (binding vs. hydrolase vs. phosphatidyltransferase vs. ligase). The sequence features and fold-level reasoning cleanly separate C from A, B, and D. No two options are close enough to be confused by a knowledgeable model."
  },
  "important_caveats": [
    "The Trypanosoma CLS is a bacterial-type (ClsA-like) enzyme in a eukaryote, a somewhat unusual evolutionary context noted in the 2012 paper. A model must recognize CDS-family homology in a divergent eukaryotic sequence, which adds difficulty but does not change the family-level reasoning.",
    "The CDS-like motifs in this sequence are not as crisp as in well-studied E. coli CdsA; recognition relies on pattern-level analogy rather than exact motif identity.",
    "The reviewer-only evidence confirms the annotation but was not available to the evaluated model; the reasoning above relies only on the sequence and general protein-family knowledge.",
    "The GO annotation evidence code is IMP (inferred by mutant phenotype) via GeneDB, supplemented by direct biochemical assays (ECO:0000269), providing strong experimental support for the key."
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
  "benchmark_sequence_length": 639,
  "benchmark_sequence_sha256": "d1770a01906c887a932e40fe30f046ec16ec07c879d4a17024149479b46e4405",
  "current_entry_audit": {
    "entryVersion": 104,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-05-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 639,
  "current_source_sequence_sha256": "d1770a01906c887a932e40fe30f046ec16ec07c879d4a17024149479b46e4405",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 102,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q584D1",
  "selected_historical_entry_version": 102,
  "selected_historical_record_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "selected_historical_source_sequence_length": 639,
  "selected_historical_source_sequence_sha256": "d1770a01906c887a932e40fe30f046ec16ec07c879d4a17024149479b46e4405",
  "selected_historical_version": {
    "accession": "Q584D1",
    "database": "Swiss-Prot",
    "entryVersion": 102,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CLS_TRYB2",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q584D1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":104,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-05-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008524\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Trypanosoma\"],\"scientificName\":\"Trypanosoma brucei brucei (strain 927/4 GUTat10.1)\",\"taxonId\":185431}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"22451910\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthetase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"CL synthase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22451910\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29167800\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the reversible phosphatidyl group transfer from one phosphatidylglycerol molecule to another to form cardiolipin (CL) (diphosphatidylglycerol) and glycerol (PubMed:22451910, PubMed:29167800). CL is a key phospholipid in mitochondrial membranes and plays important roles in maintaining the functional integrity and dynamics of mitochondria under both optimal and stress conditions (PubMed:22451910, PubMed:29167800)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"22451910\",\"source\":\"PubMed\"}],\"name\":\"2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a cardiolipin + glycerol\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:31451\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17754\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:62237\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64716\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000315\",\"id\":\"20382188\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000315\",\"id\":\"22451910\",\"source\":\"PubMed\"}],\"id\":\"GO:0008808\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:cardiolipin synthase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IMP:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Serricchio M.\",\"Buetikofer P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22451910\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1121528109\"}],\"citationType\":\"journal article\",\"firstPage\":\"E954\",\"id\":\"22451910\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"E961\",\"publicationDate\":\"2012\",\"title\":\"An essential bacterial-type cardiolipin synthase mediates cardiolipin formation in a eukaryote.\",\"volume\":\"109\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Gottier P.\",\"Serricchio M.\",\"Vitale R.\",\"Corcelli A.\",\"Buetikofer P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29167800\"},{\"database\":\"DOI\",\"id\":\"10.15698/mic2017.11.598\"}],\"citationType\":\"journal article\",\"firstPage\":\"376\",\"id\":\"29167800\",\"journal\":\"Microb. Cell\",\"lastPage\":\"383\",\"publicationDate\":\"2017\",\"title\":\"Cross-species complementation of bacterial- and eukaryotic-type cardiolipin synthases.\",\"volume\":\"4\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "entry_version": 102,
  "evidence_id": "H1",
  "excerpt": "ID   CLS_TRYB2               Reviewed;         639 AA.\nAC   Q584D1; D6XFJ2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-MAY-2005, sequence version 1.\nDT   28-JAN-2026, entry version 102.\nDE   RecName: Full=Cardiolipin synthetase {ECO:0000305};\nDE            Short=CL synthase {ECO:0000305};\nDE            EC=2.7.8.- {ECO:0000305|PubMed:22451910};\nDE   Flags: Precursor;\nGN   Name=CLS {ECO:0000303|PubMed:22451910};\nGN   ORFNames=Tb04.1H19.1130 {ECO:0000312|EMBL:AAZ10847.1},\nGN   Tb927.4.2560 {ECO:0000312|EMBL:AAX79074.1};\nOS   Trypanosoma brucei brucei (strain 927/4 GUTat10.1).\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Trypanosoma.\nOX   NCBI_TaxID=185431 {ECO:0000312|Proteomes:UP000008524};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "entry_version": 102,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, SUBCELLULAR LOCATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=22451910; DOI=10.1073/pnas.1121528109;\nRA   Serricchio M., Buetikofer P.;\nRT   \"An essential bacterial-type cardiolipin synthase mediates cardiolipin\nRT   formation in a eukaryote.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 109:E954-E961(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "entry_version": 102,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=29167800; DOI=10.15698/mic2017.11.598;\nRA   Gottier P., Serricchio M., Vitale R., Corcelli A., Buetikofer P.;\nRT   \"Cross-species complementation of bacterial- and eukaryotic-type\nRT   cardiolipin synthases.\";\nRL   Microb. Cell 4:376-383(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 73-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "entry_version": 102,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the reversible phosphatidyl group transfer from one\nCC       phosphatidylglycerol molecule to another to form cardiolipin (CL)\nCC       (diphosphatidylglycerol) and glycerol (PubMed:22451910,\nCC       PubMed:29167800). CL is a key phospholipid in mitochondrial membranes\nCC       and plays important roles in maintaining the functional integrity and\nCC       dynamics of mitochondria under both optimal and stress conditions\nCC       (PubMed:22451910, PubMed:29167800). {ECO:0000269|PubMed:22451910,\nCC       ECO:0000269|PubMed:29167800}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "entry_version": 102,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 a 1,2-diacyl-sn-glycero-3-phospho-(1'-sn-glycerol) = a\nCC         cardiolipin + glycerol; Xref=Rhea:RHEA:31451, ChEBI:CHEBI:17754,\nCC         ChEBI:CHEBI:62237, ChEBI:CHEBI:64716;\nCC         Evidence={ECO:0000305|PubMed:22451910};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "entry_version": 102,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0008808; F:cardiolipin synthase activity; IMP:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003952\nname: NAD+ synthase (glutamine-hydrolyzing) activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: deamido-NAD+ + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD+ + H+.\" [RHEA:24384]\nsynonym: \"deamido-NAD+:L-glutamine amido-ligase (AMP-forming)\" RELATED [EC:6.3.5.1]\nsynonym: \"desamidonicotinamide adenine dinucleotide amidotransferase activity\" RELATED [EC:6.3.5.1]\nsynonym: \"DPN synthetase activity\" RELATED [EC:6.3.5.1]\nsynonym: \"NAD synthase (glutamine-hydrolyzing) activity\" EXACT []\nsynonym: \"NAD synthetase (glutamine-hydrolysing)\" RELATED [EC:6.3.5.1]\nsynonym: \"NAD(+) synthetase (glutamine-hydrolyzing) activity\" RELATED [EC:6.3.5.1]\nsynonym: \"NAD+ synthase (glutamine-hydrolysing)\" RELATED [EC:6.3.5.1]\nsynonym: \"NAD+ synthetase (glutamine-hydrolyzing)\" RELATED [EC:6.3.5.1]\nsynonym: \"nicotinamide adenine dinucleotide synthetase (glutamine) activity\" RELATED [EC:6.3.5.1]\nxref: EC:6.3.5.1\nxref: MetaCyc:NAD-SYNTH-GLN-RXN\nxref: Reactome:R-HSA-197271 \"NADSYN1 hexamer amidates NAAD to NAD+\"\nxref: RHEA:24384\nxref: Wikipedia:NAD+_synthase_(glutamine-hydrolysing)\nis_a: GO:0016884 ! carbon-nitrogen ligase activity, with glutamine as amido-N-donor\nproperty_value: skos:exactMatch EC:6.3.5.1\nproperty_value: skos:exactMatch MetaCyc:NAD-SYNTH-GLN-RXN\nproperty_value: skos:exactMatch RHEA:24384\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003952",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 31993-32016",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0008808\nname: cardiolipin synthase activity\nnamespace: molecular_function\nalt_id: GO:0043788\ndef: \"Catalysis of the reaction: phosphatidylglycerol + phosphatidylglycerol = diphosphatidylglycerol (cardiolipin) + glycerol.\" [GOC:jl, RHEA:31451]\nsynonym: \"cardiolipin synthase 2 activity\" RELATED []\nsynonym: \"cardiolipin synthetase 2 activity\" RELATED []\nsynonym: \"cardiolipin synthetase activity\" BROAD []\nsynonym: \"diphosphatidylglycerol synthase activity\" EXACT []\nxref: MetaCyc:CARDIOLIPSYN-RXN\nxref: RHEA:31451\nis_a: GO:0030572 ! phosphatidyltransferase activity\nproperty_value: skos:exactMatch RHEA:31451\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008808",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 88298-88312",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0097367\nname: carbohydrate derivative binding\nnamespace: molecular_function\ndef: \"Binding to a carbohydrate derivative.\" [GOC:pr]\nsubset: goslim_agr\nsubset: goslim_mouse\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0097367",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 404743-404751",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0106435\nname: carboxylesterase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a carboxylic ester + H2O = a carboxylate + an alcohol + H+.\" [RHEA:21164]\ncomment: Note: This covers a broad range of specificity; also hydrolyzes vitamin A esters.\nsynonym: \"ali-esterase activity\" RELATED [EC:3.1.1.1]\nsynonym: \"alpha-carboxylesterase activity\" NARROW []\nsynonym: \"B-esterase activity\" NARROW [EC:3.1.1.1]\nsynonym: \"cocaine esterase\" NARROW [EC:3.1.1.1]\nsynonym: \"nonspecific carboxylesterase activity\" RELATED []\nsynonym: \"procaine esterase\" NARROW [] {comment=\"EC:3.1.1.1\"}\nsynonym: \"serine esterase activity\" NARROW []\nsynonym: \"triacetin esterase\" NARROW []\nsynonym: \"vitamin A esterase\" NARROW []\nxref: EC:3.1.1.1\nxref: MetaCyc:CARBOXYLESTERASE-RXN\nxref: Reactome:R-HSA-9619024 \"CES1 trimer hydrolyses ACEI pro-drugs to ACEIs\"\nxref: Reactome:R-HSA-9727567 \"CES1 hydrolyses sacubitril to sacubitrilat\"\nxref: Reactome:R-HSA-9749647 \"CES2 hydrolyzes ASA-\"\nxref: RHEA:21164\nxref: RHEA:31779\nxref: RHEA:38555\nxref: RHEA:47348\nxref: RHEA:47352\nxref: RHEA:47356\nxref: RHEA:47360\nxref: RHEA:47364\nxref: RHEA:47388\nxref: RHEA:47392\nxref: RHEA:50136\nxref: RHEA:50144\nxref: RHEA:50148\nxref: RHEA:59388\nxref: RHEA:63052\nis_a: GO:0052689 ! carboxylic ester hydrolase activity\nproperty_value: skos:exactMatch EC:3.1.1.1\nproperty_value: skos:exactMatch RHEA:21164\nproperty_value: skos:narrowMatch RHEA:31779\nproperty_value: skos:narrowMatch RHEA:38555\nproperty_value: skos:narrowMatch RHEA:47348\nproperty_value: skos:narrowMatch RHEA:47352\nproperty_value: skos:narrowMatch RHEA:47356\nproperty_value: skos:narrowMatch RHEA:47360\nproperty_value: skos:narrowMatch RHEA:47364\nproperty_value: skos:narrowMatch RHEA:47388\nproperty_value: skos:narrowMatch RHEA:47392\nproperty_value: skos:narrowMatch RHEA:50136\nproperty_value: skos:narrowMatch RHEA:50144\nproperty_value: skos:narrowMatch RHEA:50148\nproperty_value: skos:narrowMatch RHEA:59388\nproperty_value: skos:narrowMatch RHEA:63052\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0106435",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 430643-430695",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
