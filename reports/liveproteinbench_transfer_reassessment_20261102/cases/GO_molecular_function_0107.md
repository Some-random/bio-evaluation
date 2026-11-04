# GO_molecular_function_0107

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0107.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — calcium ion binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMKINLYKLLCFICVIFLLHKNVVRSGDNMKYNDMKGLDDLSKLNDDQVKDILGLKIDGAKERIEKLFHLIDKNNDKEITEEELNTWSSFLKNEIFLKQVQAEMGQIDSDKDGFISLNELNDAFAQNLDAKEVEKHSEGLLKRFQIVDKDKDGKLSINEVGLLIDPMKDEELKELEINEILEHHDVNKDGKISLDEFKQTRSDESSGVKKDDEMALDDFNFFDANKDGFIDKEEIIKVYFDPAHESGAINVNEIKENIFEGKKITYDLWNEKALKIAVTSLTDYGDVIRYPEDFKLDIGKNVILPTARSRAFEDDDMDADNTEDDKDEADDASQQKSPAIDEL

[Multiple Choices]
A. cystathionine gamma-synthase activity
B. CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity
C. ATP binding
D. calcium ion binding
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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1050)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports calcium binding with experimental evidence (ECO:0000269), supporting choice D for the molecular function asked.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is rich in acidic residues and includes repeated acidic/glycine-containing segments consistent with calcium-coordinating EF-hand-like loops. Transferable knowledge that EF-hand proteins bind Ca2+ meaningfully favors calcium ion binding over the two enzyme activities; the sequence also lacks an obvious ATP-binding motif that would support ATP binding.",
    "missing_item_specific_fact": "",
    "reason": "The sequence features and familiar calcium-binding motif pattern provide a credible family-level inference that distinguishes D among these options, without requiring the exact protein's database annotation.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The acidic, repeated calcium-binding-like sequence pattern favors D over the offered catalytic activities and ATP binding."
  },
  "important_caveats": [
    "Sequence motifs support a functional inference but do not by themselves experimentally establish calcium binding."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IIR7 (PFERC_PLAF7) is named 'Endoplasmic reticulum-resident calcium binding protein' and carries GO:0005509 (calcium ion binding) annotation. The 1997 paper (PubMed:9364972) experimentally identified 'multiple EF-hand motifs' and demonstrated calcium binding. The 2020 paper (PubMed:32098818) further confirms it as a CREC-family calcium-binding protein. The GO annotation uses ISS:GeneDB evidence, but the protein name and functional description are supported by experimental evidence codes (ECO:0000269).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple canonical EF-hand calcium-binding loop motifs with the D-x-D-x-D-G pattern: 'IDSDKDGFISL' (~position 80), 'IDKDKDGKLSI' (~position 145), and 'IDANKDGFIDK' (~position 185). These match the textbook EF-hand consensus (D/N-x-D/N-x-K/R-x-x-x-x-x-x-I/L/V) that is the defining feature of calcium-binding proteins across eukaryotes. Additionally, the N-terminal hydrophobic stretch (MMKINLYKLLCFICVIFLLHKNVV) is a signal peptide consistent with ER targeting, and the overall high aspartate/glutamate content is characteristic of calcium-binding proteins. None of the other options are supported: there is no PLP-binding motif (rules out A: cystathionine gamma-synthase), no phosphatidyltransferase membrane-spanning architecture (rules out B), and no Walker A/P-loop GxxxxGK&#91;T/S&#93; motif (rules out C: ATP binding). The EF-hand motif is a universally recognized, transferable structural feature that directly and uniquely distinguishes option D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The EF-hand calcium-binding loop motifs are clearly identifiable from the raw amino acid sequence and represent one of the most well-characterized and transferable protein structural motifs in biology. A knowledgeable model recognizing the D-x-D-x-D-G pattern in multiple positions, combined with the signal peptide and acidic residue enrichment, can confidently select calcium ion binding over the three enzymatic/binding alternatives that lack any corresponding sequence signature.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The EF-hand motifs unambiguously point to calcium binding. The other three options (cystathionine gamma-synthase, phosphatidyltransferase, ATP binding) require entirely different structural motifs (PLP-binding, membrane-spanning with specific catalytic residues, P-loop/Walker motifs) that are absent from this sequence. No alternative is defensible.


### Important caveats

- The GO annotation evidence code is ISS (Inferred by Sequence Similarity), not direct experimental evidence for this specific protein, though the protein name and function are experimentally supported by PubMed:9364972 and PubMed:32098818.
- The reviewer identified the protein as a CREC-family protein (2020 paper), which provides additional family-level context, but the EF-hand motifs alone are sufficient to distinguish the answer from the sequence.
- The signal peptide and ER-residency are consistent with but not strictly necessary for the molecular function answer of calcium ion binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple canonical EF-hand calcium-binding loop motifs with the D-x-D-x-D-G pattern: 'IDSDKDGFISL' (~position 80), 'IDKDKDGKLSI' (~position 145), and 'IDANKDGFIDK' (~position 185). These match the textbook EF-hand consensus (D/N-x-D/N-x-K/R-x-x-x-x-x-x-I/L/V) that is the defining feature of calcium-binding proteins across eukaryotes. Additionally, the N-terminal hydrophobic stretch (MMKINLYKLLCFICVIFLLHKNVV) is a signal peptide consistent with ER targeting, and the overall high aspartate/glutamate content is characteristic of calcium-binding proteins. None of the other options are supported: there is no PLP-binding motif (rules out A: cystathionine gamma-synthase), no phosphatidyltransferase membrane-spanning architecture (rules out B), and no Walker A/P-loop GxxxxGK[T/S] motif (rules out C: ATP binding). The EF-hand motif is a universally recognized, transferable structural feature that directly and uniquely distinguishes option D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The EF-hand calcium-binding loop motifs are clearly identifiable from the raw amino acid sequence and represent one of the most well-characterized and transferable protein structural motifs in biology. A knowledgeable model recognizing the D-x-D-x-D-G pattern in multiple positions, combined with the signal peptide and acidic residue enrichment, can confidently select calcium ion binding over the three enzymatic/binding alternatives that lack any corresponding sequence signature."
  },
  "case_id": "GO_molecular_function_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IIR7 (PFERC_PLAF7) is named 'Endoplasmic reticulum-resident calcium binding protein' and carries GO:0005509 (calcium ion binding) annotation. The 1997 paper (PubMed:9364972) experimentally identified 'multiple EF-hand motifs' and demonstrated calcium binding. The 2020 paper (PubMed:32098818) further confirms it as a CREC-family calcium-binding protein. The GO annotation uses ISS:GeneDB evidence, but the protein name and functional description are supported by experimental evidence codes (ECO:0000269)."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISS (Inferred by Sequence Similarity), not direct experimental evidence for this specific protein, though the protein name and function are experimentally supported by PubMed:9364972 and PubMed:32098818.",
    "The reviewer identified the protein as a CREC-family protein (2020 paper), which provides additional family-level context, but the EF-hand motifs alone are sufficient to distinguish the answer from the sequence.",
    "The signal peptide and ER-residency are consistent with but not strictly necessary for the molecular function answer of calcium ion binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EF-hand motifs unambiguously point to calcium binding. The other three options (cystathionine gamma-synthase, phosphatidyltransferase, ATP binding) require entirely different structural motifs (PLP-binding, membrane-spanning with specific catalytic residues, P-loop/Walker motifs) that are absent from this sequence. No alternative is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IIR7 (PFERC_PLAF7) is named 'Endoplasmic reticulum-resident calcium binding protein' and carries GO:0005509 (calcium ion binding) annotation. The 1997 paper (PubMed:9364972) experimentally identified 'multiple EF-hand motifs' and demonstrated calcium binding. The 2020 paper (PubMed:32098818) further confirms it as a CREC-family calcium-binding protein. The GO annotation uses ISS:GeneDB evidence, but the protein name and functional description are supported by experimental evidence codes (ECO:0000269).",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple canonical EF-hand calcium-binding loop motifs with the D-x-D-x-D-G pattern: 'IDSDKDGFISL' (~position 80), 'IDKDKDGKLSI' (~position 145), and 'IDANKDGFIDK' (~position 185). These match the textbook EF-hand consensus (D/N-x-D/N-x-K/R-x-x-x-x-x-x-I/L/V) that is the defining feature of calcium-binding proteins across eukaryotes. Additionally, the N-terminal hydrophobic stretch (MMKINLYKLLCFICVIFLLHKNVV) is a signal peptide consistent with ER targeting, and the overall high aspartate/glutamate content is characteristic of calcium-binding proteins. None of the other options are supported: there is no PLP-binding motif (rules out A: cystathionine gamma-synthase), no phosphatidyltransferase membrane-spanning architecture (rules out B), and no Walker A/P-loop GxxxxGK[T/S] motif (rules out C: ATP binding). The EF-hand motif is a universally recognized, transferable structural feature that directly and uniquely distinguishes option D.",
    "missing_item_specific_fact": "",
    "reason": "The EF-hand calcium-binding loop motifs are clearly identifiable from the raw amino acid sequence and represent one of the most well-characterized and transferable protein structural motifs in biology. A knowledgeable model recognizing the D-x-D-x-D-G pattern in multiple positions, combined with the signal peptide and acidic residue enrichment, can confidently select calcium ion binding over the three enzymatic/binding alternatives that lack any corresponding sequence signature."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EF-hand motifs unambiguously point to calcium binding. The other three options (cystathionine gamma-synthase, phosphatidyltransferase, ATP binding) require entirely different structural motifs (PLP-binding, membrane-spanning with specific catalytic residues, P-loop/Walker motifs) that are absent from this sequence. No alternative is defensible."
  },
  "important_caveats": [
    "The GO annotation evidence code is ISS (Inferred by Sequence Similarity), not direct experimental evidence for this specific protein, though the protein name and function are experimentally supported by PubMed:9364972 and PubMed:32098818.",
    "The reviewer identified the protein as a CREC-family protein (2020 paper), which provides additional family-level context, but the EF-hand motifs alone are sufficient to distinguish the answer from the sequence.",
    "The signal peptide and ER-residency are consistent with but not strictly necessary for the molecular function answer of calcium ion binding."
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
  "benchmark_sequence_length": 343,
  "benchmark_sequence_sha256": "5aaa315c0f202540b1464349f5584d0b2d8ead010738a7162723881d6234a475",
  "current_entry_audit": {
    "entryVersion": 148,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 343,
  "current_source_sequence_sha256": "5aaa315c0f202540b1464349f5584d0b2d8ead010738a7162723881d6234a475",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 146,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IIR7",
  "selected_historical_entry_version": 146,
  "selected_historical_record_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "selected_historical_source_sequence_length": 343,
  "selected_historical_source_sequence_sha256": "5aaa315c0f202540b1464349f5584d0b2d8ead010738a7162723881d6234a475",
  "selected_historical_version": {
    "accession": "Q8IIR7",
    "database": "Swiss-Prot",
    "entryVersion": 146,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PFERC_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IIR7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":148,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9497061\",\"source\":\"PubMed\"}],\"value\":\"Pf39\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9497061\",\"source\":\"PubMed\"}],\"value\":\"Pfs40\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23061985\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32098818\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"value\":\"Endoplasmic reticulum-resident calcium binding protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23061985\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32098818\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"value\":\"PfERC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32098818\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"value\":\"Calcium-binding protein (PubMed:9364972). Required for schizont to ring transition (PubMed:32098818). Required for the breakdown of the parasitophorous vacuole membrane during egress (PubMed:32098818). Required for the proteolytic maturation of apical membrane antigen 1 (AMA-1) during egress (PubMed:32098818). Required for the proteolytic maturation of subtilisin-like protease 1 (SUB1) during egress (PubMed:32098818). Required for the proteolytic maturation of plasmepsin X (PMX) during egress (PubMed:32098818)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"12368867\",\"source\":\"PubMed\"}],\"id\":\"GO:0005509\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:calcium ion binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"La Greca N.\",\"Hibbs A.R.\",\"Riffkin C.\",\"Foley M.\",\"Tilley L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9364972\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0166-6851(97)00134-5\"}],\"citationType\":\"journal article\",\"firstPage\":\"283\",\"id\":\"9364972\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"293\",\"publicationDate\":\"1997\",\"title\":\"Identification of an endoplasmic reticulum-resident calcium-binding protein with multiple EF-hand motifs in asexual stages of Plasmodium falciparum.\",\"volume\":\"89\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"D10\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9364972\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"FCR3\"}],\"referenceNumber\":2,\"referencePositions\":[\"PROTEIN SEQUENCE OF 238-249\",\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Templeton T.J.\",\"Fujioka H.\",\"Aikawa M.\",\"Parker K.C.\",\"Kaslow D.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9497061\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0166-6851(97)00164-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"359\",\"id\":\"9497061\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"365\",\"publicationDate\":\"1997\",\"title\":\"Plasmodium falciparum Pfs40, renamed Pf39, is localized to an intracellular membrane-bound compartment and is not sexual stage-specific.\",\"volume\":\"90\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Morita M.\",\"Sanai H.\",\"Hiramoto A.\",\"Sato A.\",\"Hiraoka O.\",\"Sakura T.\",\"Kaneko O.\",\"Masuyama A.\",\"Nojima M.\",\"Wataya Y.\",\"Kim H.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23061985\"},{\"database\":\"DOI\",\"id\":\"10.1021/pr3005315\"}],\"citationType\":\"journal article\",\"firstPage\":\"5704\",\"id\":\"23061985\",\"journal\":\"J. Proteome Res.\",\"lastPage\":\"5711\",\"publicationDate\":\"2012\",\"title\":\"Plasmodium falciparum endoplasmic reticulum-resident calcium binding protein is a possible target of synthetic antimalarial endoperoxides, N-89 and N-251.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23061985\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"FCR3\"}],\"referenceNumber\":4,\"referencePositions\":[\"IDENTIFICATION BY MASS SPECTROMETRY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IIR7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Fierro M.A.\",\"Asady B.\",\"Brooks C.F.\",\"Cobb D.W.\",\"Villegas A.\",\"Moreno S.N.J.\",\"Muralidharan V.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32098818\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.03078-19\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"32098818\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2020\",\"title\":\"An Endoplasmic Reticulum CREC Family Protein Regulates the Egress Proteolytic Cascade in Malaria Parasites.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:32:13.166389+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bcddaef36fecdf3fdd66cbdd4d19140f076342af6ffb8d5385940d2e894415a8",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IIR7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H1",
  "excerpt": "ID   PFERC_PLAF7             Reviewed;         343 AA.\nAC   Q8IIR7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 146.\nDE   RecName: Full=Endoplasmic reticulum-resident calcium binding protein {ECO:0000303|PubMed:23061985, ECO:0000303|PubMed:32098818, ECO:0000303|PubMed:9364972};\nDE            Short=PfERC {ECO:0000303|PubMed:23061985, ECO:0000303|PubMed:32098818, ECO:0000303|PubMed:9364972};\nDE   AltName: Full=Pf39 {ECO:0000303|PubMed:9497061};\nDE   AltName: Full=Pfs40 {ECO:0000303|PubMed:9364972, ECO:0000303|PubMed:9497061};\nDE   Flags: Precursor;\nGN   Name=ERC {ECO:0000305};\nGN   ORFNames=PF3D7_1108600 {ECO:0000312|EMBL:CZT98752.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   PROTEIN SEQUENCE OF 238-249, FUNCTION, SUBCELLULAR LOCATION, AND\nRP   DEVELOPMENTAL STAGE.\nRC   STRAIN=D10 {ECO:0000303|PubMed:9364972}, and\nRC   FCR3 {ECO:0000303|PubMed:9364972};\nRX   PubMed=9364972; DOI=10.1016/s0166-6851(97)00134-5;\nRA   La Greca N., Hibbs A.R., Riffkin C., Foley M., Tilley L.;\nRT   \"Identification of an endoplasmic reticulum-resident calcium-binding\nRT   protein with multiple EF-hand motifs in asexual stages of Plasmodium\nRT   falciparum.\";\nRL   Mol. Biochem. Parasitol. 89:283-293(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   SUBCELLULAR LOCATION, AND DEVELOPMENTAL STAGE.\nRX   PubMed=9497061; DOI=10.1016/s0166-6851(97)00164-3;\nRA   Templeton T.J., Fujioka H., Aikawa M., Parker K.C., Kaslow D.C.;\nRT   \"Plasmodium falciparum Pfs40, renamed Pf39, is localized to an\nRT   intracellular membrane-bound compartment and is not sexual stage-\nRT   specific.\";\nRL   Mol. Biochem. Parasitol. 90:359-365(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   IDENTIFICATION BY MASS SPECTROMETRY, AND SUBCELLULAR LOCATION.\nRC   STRAIN=FCR3 {ECO:0000303|PubMed:23061985};\nRX   PubMed=23061985; DOI=10.1021/pr3005315;\nRA   Morita M., Sanai H., Hiramoto A., Sato A., Hiraoka O., Sakura T.,\nRA   Kaneko O., Masuyama A., Nojima M., Wataya Y., Kim H.S.;\nRT   \"Plasmodium falciparum endoplasmic reticulum-resident calcium binding\nRT   protein is a possible target of synthetic antimalarial endoperoxides, N-89\nRT   and N-251.\";\nRL   J. Proteome Res. 11:5704-5711(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H5",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32098818; DOI=10.1128/mbio.03078-19;\nRA   Fierro M.A., Asady B., Brooks C.F., Cobb D.W., Villegas A., Moreno S.N.J.,\nRA   Muralidharan V.;\nRT   \"An Endoplasmic Reticulum CREC Family Protein Regulates the Egress\nRT   Proteolytic Cascade in Malaria Parasites.\";\nRL   MBio 11:0-0(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H6",
  "excerpt": "CC   -!- FUNCTION: Calcium-binding protein (PubMed:9364972). Required for\nCC       schizont to ring transition (PubMed:32098818). Required for the\nCC       breakdown of the parasitophorous vacuole membrane during egress\nCC       (PubMed:32098818). Required for the proteolytic maturation of apical\nCC       membrane antigen 1 (AMA-1) during egress (PubMed:32098818). Required\nCC       for the proteolytic maturation of subtilisin-like protease 1 (SUB1)\nCC       during egress (PubMed:32098818). Required for the proteolytic\nCC       maturation of plasmepsin X (PMX) during egress (PubMed:32098818).\nCC       {ECO:0000269|PubMed:32098818, ECO:0000269|PubMed:9364972}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146)

```json
{
  "entry_version": 146,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0005509; F:calcium ion binding; ISS:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:17.560132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-127",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6364a781ef22504ba42ffaa5320cce8c074a7dae5af9dc14106152f1668016e1",
  "url": "https://rest.uniprot.org/unisave/Q8IIR7?format=txt&versions=146"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003962\nname: cystathionine gamma-synthase activity\nnamespace: molecular_function\nalt_id: GO:0000505\ndef: \"Catalysis of the reaction: L-cysteine + O-succinyl-L-homoserine = H+ + L,L-cystathionine + succinate.\" [RHEA:20397]\nsynonym: \"CTT gamma synthase activity\" EXACT []\nsynonym: \"cystathionine g-synthase activity\" EXACT []\nsynonym: \"cystathionine gamma synthase activity\" EXACT []\nsynonym: \"cystathionine gamma-synthase activity (acts on O-phosphohomoserine)\" NARROW []\nsynonym: \"cystathionine synthase activity\" RELATED [EC:2.5.1.48]\nsynonym: \"cystathionine synthetase activity\" RELATED [EC:2.5.1.48]\nsynonym: \"homoserine O-transsuccinylase activity\" BROAD [EC:2.5.1.48]\nsynonym: \"homoserine transsuccinylase activity\" BROAD [EC:2.5.1.48]\nsynonym: \"O-succinyl-L-homoserine (thiol)-lyase activity\" EXACT []\nsynonym: \"O-succinyl-L-homoserine succinate-lyase (adding cysteine) activity\" RELATED [EC:2.5.1.48]\nsynonym: \"O-succinyl-L-homoserine succinate-lyase activity\" EXACT []\nsynonym: \"O-succinylhomoserine (thiol)-lyase activity\" RELATED [EC:2.5.1.48]\nsynonym: \"O-succinylhomoserine synthase activity\" RELATED [EC:2.5.1.48]\nsynonym: \"O-succinylhomoserine synthetase activity\" RELATED [EC:2.5.1.48]\nsynonym: \"O4-succinyl-L-homoserine:L-cysteine S-(3-amino-3-carboxypropyl)transferase activity\" RELATED [EC:2.5.1.48]\nxref: EC:2.5.1.48\nxref: MetaCyc:O-SUCCHOMOSERLYASE-RXN\nxref: RHEA:20397\nis_a: GO:0016765 ! transferase activity, transferring alkyl or aryl (other than methyl) groups\nproperty_value: skos:exactMatch EC:2.5.1.48\nproperty_value: skos:exactMatch MetaCyc:O-SUCCHOMOSERLYASE-RXN\nproperty_value: skos:exactMatch RHEA:20397\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003962",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 32256-32284",
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
  "excerpt": "[Term]\nid: GO:0005509\nname: calcium ion binding\nnamespace: molecular_function\ndef: \"Binding to a calcium ion (Ca2+).\" [GOC:ai]\nsynonym: \"calcium ion storage activity\" RELATED []\nis_a: GO:0046872 ! metal ion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005509",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 56927-56934",
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
  "excerpt": "[Term]\nid: GO:0005524\nname: ATP binding\nnamespace: molecular_function\ndef: \"Binding to ATP, adenosine 5'-triphosphate, a universally important coenzyme and enzyme regulator.\" [ISBN:0198506732]\nsynonym: \"Mg-ATP binding\" EXACT []\nsynonym: \"MgATP binding\" EXACT []\nxref: Reactome:R-HSA-265682 \"KCNJ11 tetramer:ABCC8 tetramer binds 4xATP, closing the channel\"\nis_a: GO:0032559 ! adenyl ribonucleotide binding\nis_a: GO:0035639 ! purine ribonucleoside triphosphate binding\nis_a: GO:0043168 ! anion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005524",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 57041-57052",
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
  "excerpt": "[Term]\nid: GO:0008444\nname: CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: sn-glycerol 3-phosphate + CDP-diacylglycerol = 3-(3-sn-phosphatidyl)-sn-glycerol 1-phosphate + CMP + H+.\" [EC:2.7.8.5, RHEA:12593]\nsynonym: \"3-phosphatidyl-1'-glycerol-3'-phosphate synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDP-diacylglycerol:sn-glycerol-3-phosphate 3-phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDPdiacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDPdiacylglycerol-sn-glycerol-3-phosphate 3-phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDPdiacylglycerol:glycerol-3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"CDPdiacylglycerol:sn-glycero-3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"cytidine 5'-diphospho-1,2-diacyl-sn-glycerol (CDPdiglyceride):sn-glycerol-3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"glycerol 3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"glycerol phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"glycerophosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"PGP synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerol phosphate synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerol phosphate synthetase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerolphosphate synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerophosphate synthase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"phosphatidylglycerophosphate synthetase activity\" RELATED [EC:2.7.8.5]\nsynonym: \"sn-glycerol-3-phosphate phosphatidyltransferase activity\" RELATED [EC:2.7.8.5]\nxref: EC:2.7.8.5\nxref: KEGG_REACTION:R01801\nxref: MetaCyc:PHOSPHAGLYPSYN-RXN\nxref: Reactome:R-HSA-1482939 \"CDP-DAG is converted to PGP by PGS1\"\nxref: RHEA:12593\nis_a: GO:0017169 ! CDP-alcohol phosphatidyltransferase activity\nproperty_value: skos:exactMatch EC:2.7.8.5\nproperty_value: skos:exactMatch RHEA:12593\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008444",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 83359-83389",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
