# pathway_0049

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0049.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Bacterial outer membrane biogenesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. deamido-NAD(+) from nicotinate D-ribonucleotide: step 1/1. .
B. sterol biosynthesis. .
C. Bacterial outer membrane biogenesis
D. L-threonine from L-aspartate: step 2/5. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry identifies the protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase and annotates it in bacterial outer membrane biogenesis/LPS O-antigen biosynthesis. The pathway annotation cites experimental and curated literature, supporting choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with an NAD-dependent sugar-nucleotide dehydrogenase, including a Rossmann-like dinucleotide-binding region and the size of this enzyme family. Transferable knowledge of UDP-sugar dehydrogenases links their modified sugar-nucleotide products to bacterial polysaccharide and LPS O-antigen synthesis, distinguishing bacterial outer membrane biogenesis from NAD biosynthesis, sterol biosynthesis, and threonine biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can meaningfully favor C among these choices without needing the exact protein's database annotation. The inference is not a guarantee from the sequence alone, but the alternatives are sufficiently distinct.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered pathways are distinct, and the sequence's likely sugar-nucleotide dehydrogenase family points to the LPS/O-antigen pathway represented by C.


### Important caveats

- The source annotation is for a sequence-matched database entry; the cited pathway support includes both experimental and curated evidence, not just a computational prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with an NAD-dependent sugar-nucleotide dehydrogenase, including a Rossmann-like dinucleotide-binding region and the size of this enzyme family. Transferable knowledge of UDP-sugar dehydrogenases links their modified sugar-nucleotide products to bacterial polysaccharide and LPS O-antigen synthesis, distinguishing bacterial outer membrane biogenesis from NAD biosynthesis, sterol biosynthesis, and threonine biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully favor C among these choices without needing the exact protein's database annotation. The inference is not a guarantee from the sequence alone, but the alternatives are sufficiently distinct."
  },
  "case_id": "pathway_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry identifies the protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase and annotates it in bacterial outer membrane biogenesis/LPS O-antigen biosynthesis. The pathway annotation cites experimental and curated literature, supporting choice C."
  },
  "important_caveats": [
    "The source annotation is for a sequence-matched database entry; the cited pathway support includes both experimental and curated evidence, not just a computational prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered pathways are distinct, and the sequence's likely sugar-nucleotide dehydrogenase family points to the LPS/O-antigen pathway represented by C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry identifies the protein as UDP-N-acetyl-D-glucosamine 6-dehydrogenase and annotates it in bacterial outer membrane biogenesis/LPS O-antigen biosynthesis. The pathway annotation cites experimental and curated literature, supporting choice C.",
    "evidence_ids": ["C4", "C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with an NAD-dependent sugar-nucleotide dehydrogenase, including a Rossmann-like dinucleotide-binding region and the size of this enzyme family. Transferable knowledge of UDP-sugar dehydrogenases links their modified sugar-nucleotide products to bacterial polysaccharide and LPS O-antigen synthesis, distinguishing bacterial outer membrane biogenesis from NAD biosynthesis, sterol biosynthesis, and threonine biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully favor C among these choices without needing the exact protein's database annotation. The inference is not a guarantee from the sequence alone, but the alternatives are sufficiently distinct."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered pathways are distinct, and the sequence's likely sugar-nucleotide dehydrogenase family points to the LPS/O-antigen pathway represented by C."
  },
  "important_caveats": [
    "The source annotation is for a sequence-matched database entry; the cited pathway support includes both experimental and curated evidence, not just a computational prediction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9RHD7 (WbpO, UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136) is explicitly annotated with pathway 'Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis' (evidence C5, H6). The pathway annotation carries experimental evidence (ECO:0000269, PubMed:10627048) in addition to sequence-based inference. The expected answer C matches this annotation directly.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C4](#evidence-c4), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal Rossmann-fold NAD-binding motif (VAVVGLGYVGLP, GxGxxG pattern), identifying it as an NAD-dependent dehydrogenase. This eliminates option A (a synthetase/ligase, not a dehydrogenase) and option B (sterol biosynthesis is a eukaryotic pathway; the compact 422-aa bacterial-type sequence lacks eukaryotic targeting signals and ER-associated features). Between C and D: aspartate-semialdehyde dehydrogenase (Asd, option D, step 2/5 of threonine biosynthesis) is typically ~340–360 aa, uses NADP+, and has a distinct active-site architecture. The 422-aa sequence here contains the hallmark 'GTP' and 'TPSHG' motifs (e.g., 'GTPVGTPSHGAYDGIILAVAHSEFKNM') characteristic of the UDP-sugar dehydrogenase superfamily (learned from other members such as UDP-GlcA dehydrogenase, UDP-GlcNAc 6-dehydrogenase homologs in E. coli, Salmonella, etc.). This superfamily catalyzes oxidation of sugar-nucleotide substrates, which in Gram-negative bacteria feeds directly into LPS O-antigen biosynthesis and outer membrane assembly. Within the offered choices, recognizing the UDP-sugar dehydrogenase family in a bacterial context points specifically to option C (bacterial outer membrane biogenesis via LPS O-antigen) rather than option D (amino acid biosynthesis).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition of the UDP-sugar dehydrogenase superfamily motifs (GTP, TPSHG), combined with the enzyme class (NAD-dependent dehydrogenase, not synthetase), the organism domain inference (bacterial), and the known metabolic context of sugar-nucleotide oxidation in Gram-negative LPS biosynthesis, provides a concrete transferable argument that meaningfully distinguishes C from A, B, and D without requiring recall of this specific protein's UniProt record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are clearly eliminable (wrong enzyme class and wrong domain, respectively). Option D is distinguishable from C by sequence length, cofactor preference, and family-specific motifs. Only C is consistent with all observable features.


### Important caveats

- The pathway annotation in UniProt carries mixed evidence codes: ECO:0000269 (experimental, PubMed:10627048) and ECO:0000305 (inferred from sequence). The functional role in LPS O-antigen biosynthesis is experimentally supported by gene disruption studies in P. aeruginosa serotype O6.
- The model does not receive organism identity or protein name; the bacterial inference must come from sequence features (compact size, lack of eukaryotic motifs, bacterial-type N-terminal Met-Lys start).
- Distinguishing UDP-sugar dehydrogenase family from Asd by sequence motifs alone requires familiarity with multiple family members; a model without exposure to the UDP-sugar dehydrogenase superfamily might struggle between C and D, though the 422-aa length and GTP/TPSHG motifs provide reasonable discrimination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal Rossmann-fold NAD-binding motif (VAVVGLGYVGLP, GxGxxG pattern), identifying it as an NAD-dependent dehydrogenase. This eliminates option A (a synthetase/ligase, not a dehydrogenase) and option B (sterol biosynthesis is a eukaryotic pathway; the compact 422-aa bacterial-type sequence lacks eukaryotic targeting signals and ER-associated features). Between C and D: aspartate-semialdehyde dehydrogenase (Asd, option D, step 2/5 of threonine biosynthesis) is typically ~340–360 aa, uses NADP+, and has a distinct active-site architecture. The 422-aa sequence here contains the hallmark 'GTP' and 'TPSHG' motifs (e.g., 'GTPVGTPSHGAYDGIILAVAHSEFKNM') characteristic of the UDP-sugar dehydrogenase superfamily (learned from other members such as UDP-GlcA dehydrogenase, UDP-GlcNAc 6-dehydrogenase homologs in E. coli, Salmonella, etc.). This superfamily catalyzes oxidation of sugar-nucleotide substrates, which in Gram-negative bacteria feeds directly into LPS O-antigen biosynthesis and outer membrane assembly. Within the offered choices, recognizing the UDP-sugar dehydrogenase family in a bacterial context points specifically to option C (bacterial outer membrane biogenesis via LPS O-antigen) rather than option D (amino acid biosynthesis).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of the UDP-sugar dehydrogenase superfamily motifs (GTP, TPSHG), combined with the enzyme class (NAD-dependent dehydrogenase, not synthetase), the organism domain inference (bacterial), and the known metabolic context of sugar-nucleotide oxidation in Gram-negative LPS biosynthesis, provides a concrete transferable argument that meaningfully distinguishes C from A, B, and D without requiring recall of this specific protein's UniProt record."
  },
  "case_id": "pathway_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9RHD7 (WbpO, UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136) is explicitly annotated with pathway 'Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis' (evidence C5, H6). The pathway annotation carries experimental evidence (ECO:0000269, PubMed:10627048) in addition to sequence-based inference. The expected answer C matches this annotation directly."
  },
  "important_caveats": [
    "The pathway annotation in UniProt carries mixed evidence codes: ECO:0000269 (experimental, PubMed:10627048) and ECO:0000305 (inferred from sequence). The functional role in LPS O-antigen biosynthesis is experimentally supported by gene disruption studies in P. aeruginosa serotype O6.",
    "The model does not receive organism identity or protein name; the bacterial inference must come from sequence features (compact size, lack of eukaryotic motifs, bacterial-type N-terminal Met-Lys start).",
    "Distinguishing UDP-sugar dehydrogenase family from Asd by sequence motifs alone requires familiarity with multiple family members; a model without exposure to the UDP-sugar dehydrogenase superfamily might struggle between C and D, though the 422-aa length and GTP/TPSHG motifs provide reasonable discrimination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly eliminable (wrong enzyme class and wrong domain, respectively). Option D is distinguishable from C by sequence length, cofactor preference, and family-specific motifs. Only C is consistent with all observable features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9RHD7 (WbpO, UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136) is explicitly annotated with pathway 'Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis' (evidence C5, H6). The pathway annotation carries experimental evidence (ECO:0000269, PubMed:10627048) in addition to sequence-based inference. The expected answer C matches this annotation directly.",
    "evidence_ids": ["C5", "H6", "C4", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal Rossmann-fold NAD-binding motif (VAVVGLGYVGLP, GxGxxG pattern), identifying it as an NAD-dependent dehydrogenase. This eliminates option A (a synthetase/ligase, not a dehydrogenase) and option B (sterol biosynthesis is a eukaryotic pathway; the compact 422-aa bacterial-type sequence lacks eukaryotic targeting signals and ER-associated features). Between C and D: aspartate-semialdehyde dehydrogenase (Asd, option D, step 2/5 of threonine biosynthesis) is typically ~340–360 aa, uses NADP+, and has a distinct active-site architecture. The 422-aa sequence here contains the hallmark 'GTP' and 'TPSHG' motifs (e.g., 'GTPVGTPSHGAYDGIILAVAHSEFKNM') characteristic of the UDP-sugar dehydrogenase superfamily (learned from other members such as UDP-GlcA dehydrogenase, UDP-GlcNAc 6-dehydrogenase homologs in E. coli, Salmonella, etc.). This superfamily catalyzes oxidation of sugar-nucleotide substrates, which in Gram-negative bacteria feeds directly into LPS O-antigen biosynthesis and outer membrane assembly. Within the offered choices, recognizing the UDP-sugar dehydrogenase family in a bacterial context points specifically to option C (bacterial outer membrane biogenesis via LPS O-antigen) rather than option D (amino acid biosynthesis).",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of the UDP-sugar dehydrogenase superfamily motifs (GTP, TPSHG), combined with the enzyme class (NAD-dependent dehydrogenase, not synthetase), the organism domain inference (bacterial), and the known metabolic context of sugar-nucleotide oxidation in Gram-negative LPS biosynthesis, provides a concrete transferable argument that meaningfully distinguishes C from A, B, and D without requiring recall of this specific protein's UniProt record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly eliminable (wrong enzyme class and wrong domain, respectively). Option D is distinguishable from C by sequence length, cofactor preference, and family-specific motifs. Only C is consistent with all observable features."
  },
  "important_caveats": [
    "The pathway annotation in UniProt carries mixed evidence codes: ECO:0000269 (experimental, PubMed:10627048) and ECO:0000305 (inferred from sequence). The functional role in LPS O-antigen biosynthesis is experimentally supported by gene disruption studies in P. aeruginosa serotype O6.",
    "The model does not receive organism identity or protein name; the bacterial inference must come from sequence features (compact size, lack of eukaryotic motifs, bacterial-type N-terminal Met-Lys start).",
    "Distinguishing UDP-sugar dehydrogenase family from Asd by sequence motifs alone requires familiarity with multiple family members; a model without exposure to the UDP-sugar dehydrogenase superfamily might struggle between C and D, though the 422-aa length and GTP/TPSHG motifs provide reasonable discrimination."
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
  "benchmark_sequence_length": 422,
  "benchmark_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "current_entry_audit": {
    "entryVersion": 113,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 422,
  "current_source_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 111,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9RHD7",
  "selected_historical_entry_version": 111,
  "selected_historical_record_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "selected_historical_source_sequence_length": 422,
  "selected_historical_source_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "selected_historical_version": {
    "accession": "Q9RHD7",
    "database": "Swiss-Prot",
    "entryVersion": 111,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "WBPO_PSEAI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9RHD7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":113,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa\",\"taxonId\":287}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.136\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-D-glucosamine 6-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-GlcNAc 6-dehydrogenase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10627048\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"10931835\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"Bacterial outer membrane biogenesis; LPS O-antigen biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Belanger M.\",\"Burrows L.L.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10627048\"},{\"database\":\"DOI\",\"id\":\"10.1099/00221287-145-12-3505\"}],\"citationType\":\"journal article\",\"firstPage\":\"3505\",\"id\":\"10627048\",\"journal\":\"Microbiology\",\"lastPage\":\"3521\",\"publicationDate\":\"1999\",\"title\":\"Functional analysis of genes responsible for the synthesis of the B-band O antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.\",\"volume\":\"145\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF23997.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 33354 / Serotype O6\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhao X.\",\"Creuzenet C.\",\"Belanger M.\",\"Egbosimba E.\",\"Li J.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10931835\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m004191200\"}],\"citationType\":\"journal article\",\"firstPage\":\"33252\",\"id\":\"10931835\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"33259\",\"publicationDate\":\"2000\",\"title\":\"WbpO, a UDP-N-acetyl-D-galactosamine dehydrogenase from Pseudomonas aeruginosa serotype O6.\",\"volume\":\"275\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Miller W.L.\",\"Matewish M.J.\",\"McNally D.J.\",\"Ishiyama N.\",\"Anderson E.M.\",\"Brewer D.\",\"Brisson J.R.\",\"Berghuis A.M.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18065759\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m708894200\"}],\"citationType\":\"journal article\",\"firstPage\":\"3507\",\"id\":\"18065759\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"3518\",\"publicationDate\":\"2008\",\"title\":\"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.\",\"volume\":\"283\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"PAK / Serotype O6\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H1",
  "excerpt": "ID   WBPO_PSEAI              Reviewed;         422 AA.\nAC   Q9RHD7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 111.\nDE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000305};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000305};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:18065759};\nGN   Name=wbpO {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};\nGN   ORFNames=CAZ10_03215 {ECO:0000312|EMBL:OTI64803.1};\nOS   Pseudomonas aeruginosa.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=287;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAF23997.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 33354 / Serotype O6;\nRX   PubMed=10627048; DOI=10.1099/00221287-145-12-3505;\nRA   Belanger M., Burrows L.L., Lam J.S.;\nRT   \"Functional analysis of genes responsible for the synthesis of the B-band O\nRT   antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.\";\nRL   Microbiology 145:3505-3521(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:AAM27816.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=Serotype O6;\nRX   PubMed=12057956; DOI=10.1128/jb.184.13.3614-3622.2002;\nRA   Raymond C.K., Sims E.H., Kas A., Spencer D.H., Kutyavin T.V., Ivey R.G.,\nRA   Zhou Y., Kaul R., Clendenning J.B., Olson M.V.;\nRT   \"Genetic variation at the O-antigen biosynthetic locus in Pseudomonas\nRT   aeruginosa.\";\nRL   J. Bacteriol. 184:3614-3622(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H4",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=Serotype O6;\nRX   PubMed=10931835; DOI=10.1074/jbc.m004191200;\nRA   Zhao X., Creuzenet C., Belanger M., Egbosimba E., Li J., Lam J.S.;\nRT   \"WbpO, a UDP-N-acetyl-D-galactosamine dehydrogenase from Pseudomonas\nRT   aeruginosa serotype O6.\";\nRL   J. Biol. Chem. 275:33252-33259(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H5",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=PAK / Serotype O6;\nRX   PubMed=18065759; DOI=10.1074/jbc.m708894200;\nRA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,\nRA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;\nRT   \"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-\nRT   antigen biosynthesis enzyme WbpO.\";\nRL   J. Biol. Chem. 283:3507-3518(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H6",
  "excerpt": "CC   -!- PATHWAY: Bacterial outer membrane biogenesis; LPS O-antigen\nCC       biosynthesis. {ECO:0000269|PubMed:10627048,\nCC       ECO:0000305|PubMed:10931835, ECO:0000305|PubMed:18065759}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
