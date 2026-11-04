# cofactor_0037

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0037.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQPEFTRSIVGASFLLPVINGAMHIPPAVSATRVTLEDNQPRDAPILVLLFALSVLIDVMDKAADLPRQTRKTWLMTIVVFASPFVVLAVYGTMHCGLLALLRLLGVPLLAVVHAMPLIPVYSWKTGSISTVKLKYFLGPFKSLFGATCIGLMDVTAVVLYLRGTMLHPENASSAGHFRVLMYTITYDFLWESICDVRDIQEDEQNNITTLATAFGVRPTLIFLGGSTMMGDLSITLLGGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART

[Multiple Choices]
A. a divalent metal cation
B. Mg(2+)
C. heme b
D. Fe(2+)
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

> The sequence-matched UniProt annotation identifies Mg(2+) as the cofactor and cites ECO:0000269 evidence linked to a publication. This supports the key, although the excerpts are database annotations rather than an independent review of the experiment.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a small, strongly hydrophobic multipass protein, with acidic residues compatible with a membrane prenyltransferase-like enzyme. A transferable inference from membrane prenyltransferase families is that Mg(2+) commonly coordinates the diphosphate group of prenyl donors. That makes Mg(2+) a more meaningful choice than heme b or Fe(2+); it is a family-level inference, not proof of this exact protein's cofactor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a plausible family/architecture clue, and general knowledge of prenyl-diphosphate enzymes supports Mg(2+) among these alternatives. The precise annotation is absent from the original input, but it is not necessary for a credible choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Mg(2+) is itself a divalent metal cation, so A is broadly true if read as a category. B is the more specific answer and best fits the prompt's request for a specific cofactor, but the choices are not strictly mutually exclusive.


### Important caveats

- The family inference from sequence architecture is suggestive rather than conclusive.
- The cited experimental evidence was not independently inspected.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a small, strongly hydrophobic multipass protein, with acidic residues compatible with a membrane prenyltransferase-like enzyme. A transferable inference from membrane prenyltransferase families is that Mg(2+) commonly coordinates the diphosphate group of prenyl donors. That makes Mg(2+) a more meaningful choice than heme b or Fe(2+); it is a family-level inference, not proof of this exact protein's cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a plausible family/architecture clue, and general knowledge of prenyl-diphosphate enzymes supports Mg(2+) among these alternatives. The precise annotation is absent from the original input, but it is not necessary for a credible choice."
  },
  "case_id": "cofactor_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies Mg(2+) as the cofactor and cites ECO:0000269 evidence linked to a publication. This supports the key, although the excerpts are database annotations rather than an independent review of the experiment."
  },
  "important_caveats": [
    "The family inference from sequence architecture is suggestive rather than conclusive.",
    "The cited experimental evidence was not independently inspected."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Mg(2+) is itself a divalent metal cation, so A is broadly true if read as a category. B is the more specific answer and best fits the prompt's request for a specific cofactor, but the choices are not strictly mutually exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies Mg(2+) as the cofactor and cites ECO:0000269 evidence linked to a publication. This supports the key, although the excerpts are database annotations rather than an independent review of the experiment.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a small, strongly hydrophobic multipass protein, with acidic residues compatible with a membrane prenyltransferase-like enzyme. A transferable inference from membrane prenyltransferase families is that Mg(2+) commonly coordinates the diphosphate group of prenyl donors. That makes Mg(2+) a more meaningful choice than heme b or Fe(2+); it is a family-level inference, not proof of this exact protein's cofactor.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a plausible family/architecture clue, and general knowledge of prenyl-diphosphate enzymes supports Mg(2+) among these alternatives. The precise annotation is absent from the original input, but it is not necessary for a credible choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Mg(2+) is itself a divalent metal cation, so A is broadly true if read as a category. B is the more specific answer and best fits the prompt's request for a specific cofactor, but the choices are not strictly mutually exclusive."
  },
  "important_caveats": [
    "The family inference from sequence architecture is suggestive rather than conclusive.",
    "The cited experimental evidence was not independently inspected."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A6A6H402 (Prenyltransferase vviA from Viridothelium virens) annotates the cofactor as Mg(2+) (ChEBI:CHEBI:18420) with experimental evidence code ECO:0000269 from PubMed:39310987 (Tang & Zou, Org. Lett. 2024). The sequence matches the benchmark sequence exactly. The answer B (Mg(2+)) is directly supported by this experimental annotation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 293-residue sequence displays multiple hydrophobic transmembrane segments and contains conserved aspartate-containing motifs (e.g., 'GGSTMMGDLSIT' and 'GGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART') characteristic of membrane-bound prenyltransferases (EC 2.5.1.-). Prenyltransferases as a well-studied enzyme family (e.g., farnesyltransferase, geranylgeranyltransferase, aromatic prenyltransferases) characteristically coordinate Mg(2+) via conserved Asp/Glu residues to activate the diphosphate leaving group of the allylic donor. This family-level knowledge distinguishes B (Mg(2+)) from C (heme b, associated with electron-transfer/oxygen-binding proteins) and D (Fe(2+), associated with dioxygenases, oxidases). The question asks for the 'specific cofactor,' making the precise ion Mg(2+) the correct choice over the generic 'divalent metal cation' (A).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize prenyltransferase sequence signatures (transmembrane topology, GD/DD-type motifs) and apply the well-established family-level fact that prenyltransferases use Mg(2+) as their catalytic divalent metal cofactor. This transferable knowledge from many characterized prenyltransferases meaningfully eliminates heme b and Fe(2+), and the word 'specific' in the question stem resolves the Mg(2+) vs. generic divalent-cation distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although Mg(2+) is technically a divalent metal cation (making A not false), the question explicitly asks for the 'specific cofactor,' which conventionally selects the most precise correct answer (B) over the generic category (A). C and D are eliminated by family-level reasoning. No genuine ambiguity remains among the offered choices.


### Important caveats

- The cofactor annotation is based on a single 2024 experimental study (PubMed:39310987) on a fungal prenyltransferase; the evidence code ECO:0000269 indicates direct experimental determination.
- The sequence features used for family assignment (transmembrane helices, GD motifs) are consistent with but not uniquely diagnostic of prenyltransferases; however, among the four offered cofactor choices, only Mg(2+) aligns with the prenyltransferase family inference.
- Option A ('a divalent metal cation') is not factually incorrect if Mg(2+) is the cofactor, but the question's use of 'specific' resolves this in favor of B.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 293-residue sequence displays multiple hydrophobic transmembrane segments and contains conserved aspartate-containing motifs (e.g., 'GGSTMMGDLSIT' and 'GGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART') characteristic of membrane-bound prenyltransferases (EC 2.5.1.-). Prenyltransferases as a well-studied enzyme family (e.g., farnesyltransferase, geranylgeranyltransferase, aromatic prenyltransferases) characteristically coordinate Mg(2+) via conserved Asp/Glu residues to activate the diphosphate leaving group of the allylic donor. This family-level knowledge distinguishes B (Mg(2+)) from C (heme b, associated with electron-transfer/oxygen-binding proteins) and D (Fe(2+), associated with dioxygenases, oxidases). The question asks for the 'specific cofactor,' making the precise ion Mg(2+) the correct choice over the generic 'divalent metal cation' (A).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize prenyltransferase sequence signatures (transmembrane topology, GD/DD-type motifs) and apply the well-established family-level fact that prenyltransferases use Mg(2+) as their catalytic divalent metal cofactor. This transferable knowledge from many characterized prenyltransferases meaningfully eliminates heme b and Fe(2+), and the word 'specific' in the question stem resolves the Mg(2+) vs. generic divalent-cation distinction."
  },
  "case_id": "cofactor_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A6A6H402 (Prenyltransferase vviA from Viridothelium virens) annotates the cofactor as Mg(2+) (ChEBI:CHEBI:18420) with experimental evidence code ECO:0000269 from PubMed:39310987 (Tang & Zou, Org. Lett. 2024). The sequence matches the benchmark sequence exactly. The answer B (Mg(2+)) is directly supported by this experimental annotation."
  },
  "important_caveats": [
    "The cofactor annotation is based on a single 2024 experimental study (PubMed:39310987) on a fungal prenyltransferase; the evidence code ECO:0000269 indicates direct experimental determination.",
    "The sequence features used for family assignment (transmembrane helices, GD motifs) are consistent with but not uniquely diagnostic of prenyltransferases; however, among the four offered cofactor choices, only Mg(2+) aligns with the prenyltransferase family inference.",
    "Option A ('a divalent metal cation') is not factually incorrect if Mg(2+) is the cofactor, but the question's use of 'specific' resolves this in favor of B."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although Mg(2+) is technically a divalent metal cation (making A not false), the question explicitly asks for the 'specific cofactor,' which conventionally selects the most precise correct answer (B) over the generic category (A). C and D are eliminated by family-level reasoning. No genuine ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A6A6H402 (Prenyltransferase vviA from Viridothelium virens) annotates the cofactor as Mg(2+) (ChEBI:CHEBI:18420) with experimental evidence code ECO:0000269 from PubMed:39310987 (Tang & Zou, Org. Lett. 2024). The sequence matches the benchmark sequence exactly. The answer B (Mg(2+)) is directly supported by this experimental annotation.",
    "evidence_ids": ["C5", "H4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 293-residue sequence displays multiple hydrophobic transmembrane segments and contains conserved aspartate-containing motifs (e.g., 'GGSTMMGDLSIT' and 'GGGSAVLSVVRSTVFWGAFAALALHKPRSAVYPWGLATLFGLLPVWLASLGART') characteristic of membrane-bound prenyltransferases (EC 2.5.1.-). Prenyltransferases as a well-studied enzyme family (e.g., farnesyltransferase, geranylgeranyltransferase, aromatic prenyltransferases) characteristically coordinate Mg(2+) via conserved Asp/Glu residues to activate the diphosphate leaving group of the allylic donor. This family-level knowledge distinguishes B (Mg(2+)) from C (heme b, associated with electron-transfer/oxygen-binding proteins) and D (Fe(2+), associated with dioxygenases, oxidases). The question asks for the 'specific cofactor,' making the precise ion Mg(2+) the correct choice over the generic 'divalent metal cation' (A).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize prenyltransferase sequence signatures (transmembrane topology, GD/DD-type motifs) and apply the well-established family-level fact that prenyltransferases use Mg(2+) as their catalytic divalent metal cofactor. This transferable knowledge from many characterized prenyltransferases meaningfully eliminates heme b and Fe(2+), and the word 'specific' in the question stem resolves the Mg(2+) vs. generic divalent-cation distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although Mg(2+) is technically a divalent metal cation (making A not false), the question explicitly asks for the 'specific cofactor,' which conventionally selects the most precise correct answer (B) over the generic category (A). C and D are eliminated by family-level reasoning. No genuine ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The cofactor annotation is based on a single 2024 experimental study (PubMed:39310987) on a fungal prenyltransferase; the evidence code ECO:0000269 indicates direct experimental determination.",
    "The sequence features used for family assignment (transmembrane helices, GD motifs) are consistent with but not uniquely diagnostic of prenyltransferases; however, among the four offered cofactor choices, only Mg(2+) aligns with the prenyltransferase family inference.",
    "Option A ('a divalent metal cation') is not factually incorrect if Mg(2+) is the cofactor, but the question's use of 'specific' resolves this in favor of B."
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
  "benchmark_sequence_length": 293,
  "benchmark_sequence_sha256": "897fc4df843bf85f1cdd0a1f4daa86fcaba8dd7ff09001216f7df7ed7a613ef7",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2020-06-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 293,
  "current_source_sequence_sha256": "897fc4df843bf85f1cdd0a1f4daa86fcaba8dd7ff09001216f7df7ed7a613ef7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A6A6H402",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "selected_historical_source_sequence_length": 293,
  "selected_historical_source_sequence_sha256": "897fc4df843bf85f1cdd0a1f4daa86fcaba8dd7ff09001216f7df7ed7a613ef7",
  "selected_historical_version": {
    "accession": "A0A6A6H402",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "VVIA_VIRVR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A6A6H402\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2020-06-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Speckled blister lichen\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetes incertae sedis\",\"Trypetheliales\",\"Trypetheliaceae\",\"Viridothelium\"],\"scientificName\":\"Viridothelium virens\",\"synonyms\":[\"Trypethelium virens\"],\"taxonId\":1048519}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"Sporulositol A biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"value\":\"Prenyltransferase vviA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39310987\",\"source\":\"PubMed\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6A6H402.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Tang Y.J.\",\"Zou Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39310987\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.orglett.4c03154\"}],\"citationType\":\"journal article\",\"firstPage\":\"8366\",\"id\":\"39310987\",\"journal\":\"Org. Lett.\",\"lastPage\":\"8370\",\"publicationDate\":\"2024\",\"title\":\"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.\",\"volume\":\"26\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"PATHWAY\",\"MUTAGENESIS OF LEU-17; ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND THR-277\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:32.724960+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b8205d729e2e5bd4217fba29840a41164bb96c507173b89acd7a02b8a587f862",
  "url": "https://rest.uniprot.org/uniprotkb/A0A6A6H402.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   VVIA_VIRVR              Reviewed;         293 AA.\nAC   A0A6A6H402;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-JUN-2020, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Prenyltransferase vviA {ECO:0000303|PubMed:39310987};\nDE            EC=2.5.1.- {ECO:0000269|PubMed:39310987};\nDE   AltName: Full=Sporulositol A biosynthesis cluster protein A {ECO:0000303|PubMed:39310987};\nGN   Name=vviA {ECO:0000303|PubMed:39310987}; ORFNames=EV356DRAFT_253807;\nOS   Viridothelium virens (Speckled blister lichen) (Trypethelium virens).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetes incertae sedis; Trypetheliales; Trypetheliaceae;\nOC   Viridothelium.\nOX   NCBI_TaxID=1048519;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Prenyltransferase vviA {ECO:0000303|PubMed:39310987};\nDE            EC=2.5.1.- {ECO:0000269|PubMed:39310987};\nDE   AltName: Full=Sporulositol A biosynthesis cluster protein A {ECO:0000303|PubMed:39310987};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, PATHWAY, AND MUTAGENESIS OF LEU-17;\nRP   ASN-21; MET-24; LYS-63; HIS-115; TYR-137; ILE-151; ASP-189; TRP-192 AND\nRP   THR-277.\nRX   PubMed=39310987; DOI=10.1021/acs.orglett.4c03154;\nRA   Tang Y.J., Zou Y.;\nRT   \"Cyclo-farnesyl Diphosphate-Dependent Prenylation in Fungi.\";\nRL   Org. Lett. 26:8366-8370(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000269|PubMed:39310987};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:34.642719+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f3fb0188f37dd39fa5b2add2435b66089c72d61d50cfdb8351cca69e37efe727",
  "url": "https://rest.uniprot.org/unisave/A0A6A6H402?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
