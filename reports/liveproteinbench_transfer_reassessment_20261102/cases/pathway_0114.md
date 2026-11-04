# pathway_0114

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0114.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSDNTPTPQKNPDTNPYASLISQQIAIIPSFTLESGVTLNNVPVAYKTWGKLNEKADNCLVICHALTGSADVEDWWGPLLGLNKAFDPTRFFIFCGNVIGSPYGTISSVTTNPETGKPFGPEMPGSSVKDDVRLHYIILKSLGVRSVAAVVGGSMGGMTVLEYPLNTPPGFVRAIIPLATSARHSAWCISWGEAQRQSIYSDPDYKDGYYYEIEEEGGKVDLARQPARGLAAARMAALLTYRSRDSFESRFGRRAGGGKSSVPKGGVRIMGGQETTDPSVPSESDLAAKSPSWRAWREHNDGHRSAGARPISRSGSEGPAHREGDAAQAEVVKTQDVKANGNKIGTGGEAPPKIFSAQSYLRYQGDKFTGRFDANCYIHITRKLDTHDLSAPSRDTSLSSLSSGLPSSPDATEEELNARLIHALSLEPPALVIGIESDGLFTTSEQRELAAGIPDAELVVIPSPDGHDGFLLEFEAINGWVEGWLKRKMPEFYERRVINPEEYVQGEEGFGIKKESVFGEAEADVTRW

[Multiple Choices]
A. Lipid metabolism
B. Amino-acid biosynthesis
C. Amino-acid degradation. .
D. tetrahydrofolate interconversion. .
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

> The sequence-matched UniProt record identifies the protein as homoserine O-acetyltransferase and places its reaction in de novo methionine biosynthesis, supporting amino-acid biosynthesis. The annotations cite experimental evidence, though the excerpts do not independently show the underlying experiments.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A credible family-level inference is that the conserved enzyme region belongs to the homoserine O-acetyltransferase family. Homoserine O-acetyltransferases produce O-acetylhomoserine, an intermediate in methionine biosynthesis, which distinguishes amino-acid biosynthesis (B) from lipid metabolism, amino-acid degradation, and tetrahydrofolate interconversion.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing a homologous enzyme family and transferring its known reaction-to-pathway relationship offers a meaningful basis for choosing B; the exact protein's database annotation is not necessary for this broad distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options distinguish broad pathway categories, and the inferred methionine-biosynthesis role supports B rather than another listed option.


### Important caveats

- The source annotations are reviewer-only and were not part of the original model input.
- The sequence-to-family recognition is an inference, not experimental confirmation from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A credible family-level inference is that the conserved enzyme region belongs to the homoserine O-acetyltransferase family. Homoserine O-acetyltransferases produce O-acetylhomoserine, an intermediate in methionine biosynthesis, which distinguishes amino-acid biosynthesis (B) from lipid metabolism, amino-acid degradation, and tetrahydrofolate interconversion.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing a homologous enzyme family and transferring its known reaction-to-pathway relationship offers a meaningful basis for choosing B; the exact protein's database annotation is not necessary for this broad distinction."
  },
  "case_id": "pathway_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as homoserine O-acetyltransferase and places its reaction in de novo methionine biosynthesis, supporting amino-acid biosynthesis. The annotations cite experimental evidence, though the excerpts do not independently show the underlying experiments."
  },
  "important_caveats": [
    "The source annotations are reviewer-only and were not part of the original model input.",
    "The sequence-to-family recognition is an inference, not experimental confirmation from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options distinguish broad pathway categories, and the inferred methionine-biosynthesis role supports B rather than another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies the protein as homoserine O-acetyltransferase and places its reaction in de novo methionine biosynthesis, supporting amino-acid biosynthesis. The annotations cite experimental evidence, though the excerpts do not independently show the underlying experiments.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A credible family-level inference is that the conserved enzyme region belongs to the homoserine O-acetyltransferase family. Homoserine O-acetyltransferases produce O-acetylhomoserine, an intermediate in methionine biosynthesis, which distinguishes amino-acid biosynthesis (B) from lipid metabolism, amino-acid degradation, and tetrahydrofolate interconversion.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing a homologous enzyme family and transferring its known reaction-to-pathway relationship offers a meaningful basis for choosing B; the exact protein's database annotation is not necessary for this broad distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options distinguish broad pathway categories, and the inferred methionine-biosynthesis role supports B rather than another listed option."
  },
  "important_caveats": [
    "The source annotations are reviewer-only and were not part of the original model input.",
    "The sequence-to-family recognition is an inference, not experimental confirmation from the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (J9VIY8) annotates this protein as Homoserine O-acetyltransferase (EC 2.3.1.31) with the pathway 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1.' This annotation is backed by experimental evidence (ECO:0000269, PubMed:17353245, Nazi et al. 2007). The expected answer B (Amino-acid biosynthesis) is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) superfamily motifs: a glycine-rich acetyl-CoA binding region ('GGSMGGMT'), an RGG motif ('GRRAGGGKSS'), and a Q-R motif region ('QRQSIYSDPDY'). GNAT-fold enzymes are a well-characterized family whose members in amino acid metabolism are predominantly biosynthetic acetyltransferases (e.g., homoserine O-acetyltransferase, N-acetylglutamate synthase). Among the four options: (D) tetrahydrofolate interconversion enzymes (e.g., SHMT, MTHFR) have entirely different folds; (A) lipid metabolism enzymes (FAS, desaturases, lipases) lack GNAT motifs and typically contain lipid-binding or thioesterase domains absent here; (C) amino-acid degradation relies mainly on transaminases, deaminases, and oxidases, not GNAT acetyltransferases. The combination of GNAT fold + cytoplasmic localization + acetyl-CoA binding motifs is a learned family-level pattern that strongly favors biosynthetic acetyltransferase function in amino acid metabolism over the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the GNAT fold from sequence motifs (Q-R, RGG, glycine-rich acetyl-CoA binding) is transferable knowledge from many characterized acetyltransferases. Within the GNAT superfamily, amino-acid biosynthetic acetyltransferases are the dominant functional class, and the other three pathway categories involve structurally unrelated enzyme families. This provides a concrete, credible inference distinguishing option B from A, C, and D without requiring the exact UniProt annotation for this specific protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GNAT fold and its strong association with biosynthetic acetyltransferases in amino acid metabolism clearly favors B over the other three options. Lipid metabolism, amino-acid degradation, and tetrahydrofolate interconversion involve fundamentally different enzyme folds and mechanisms not suggested by the sequence.


### Important caveats

- The GNAT superfamily is functionally diverse; while amino acid biosynthesis is the most common pathway for GNAT enzymes in primary metabolism, some GNAT members function in other contexts. The inference is probabilistic rather than deterministic.
- The sequence is from a fungal organism (Cryptococcus neoformans), but the GNAT fold recognition and pathway assignment logic is organism-independent.
- The reviewer-only evidence confirms the annotation experimentally, but the model would need to rely on family-level pattern recognition from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) superfamily motifs: a glycine-rich acetyl-CoA binding region ('GGSMGGMT'), an RGG motif ('GRRAGGGKSS'), and a Q-R motif region ('QRQSIYSDPDY'). GNAT-fold enzymes are a well-characterized family whose members in amino acid metabolism are predominantly biosynthetic acetyltransferases (e.g., homoserine O-acetyltransferase, N-acetylglutamate synthase). Among the four options: (D) tetrahydrofolate interconversion enzymes (e.g., SHMT, MTHFR) have entirely different folds; (A) lipid metabolism enzymes (FAS, desaturases, lipases) lack GNAT motifs and typically contain lipid-binding or thioesterase domains absent here; (C) amino-acid degradation relies mainly on transaminases, deaminases, and oxidases, not GNAT acetyltransferases. The combination of GNAT fold + cytoplasmic localization + acetyl-CoA binding motifs is a learned family-level pattern that strongly favors biosynthetic acetyltransferase function in amino acid metabolism over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the GNAT fold from sequence motifs (Q-R, RGG, glycine-rich acetyl-CoA binding) is transferable knowledge from many characterized acetyltransferases. Within the GNAT superfamily, amino-acid biosynthetic acetyltransferases are the dominant functional class, and the other three pathway categories involve structurally unrelated enzyme families. This provides a concrete, credible inference distinguishing option B from A, C, and D without requiring the exact UniProt annotation for this specific protein."
  },
  "case_id": "pathway_0114",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (J9VIY8) annotates this protein as Homoserine O-acetyltransferase (EC 2.3.1.31) with the pathway 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1.' This annotation is backed by experimental evidence (ECO:0000269, PubMed:17353245, Nazi et al. 2007). The expected answer B (Amino-acid biosynthesis) is directly and experimentally supported."
  },
  "important_caveats": [
    "The GNAT superfamily is functionally diverse; while amino acid biosynthesis is the most common pathway for GNAT enzymes in primary metabolism, some GNAT members function in other contexts. The inference is probabilistic rather than deterministic.",
    "The sequence is from a fungal organism (Cryptococcus neoformans), but the GNAT fold recognition and pathway assignment logic is organism-independent.",
    "The reviewer-only evidence confirms the annotation experimentally, but the model would need to rely on family-level pattern recognition from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GNAT fold and its strong association with biosynthetic acetyltransferases in amino acid metabolism clearly favors B over the other three options. Lipid metabolism, amino-acid degradation, and tetrahydrofolate interconversion involve fundamentally different enzyme folds and mechanisms not suggested by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0114",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (J9VIY8) annotates this protein as Homoserine O-acetyltransferase (EC 2.3.1.31) with the pathway 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1.' This annotation is backed by experimental evidence (ECO:0000269, PubMed:17353245, Nazi et al. 2007). The expected answer B (Amino-acid biosynthesis) is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) superfamily motifs: a glycine-rich acetyl-CoA binding region ('GGSMGGMT'), an RGG motif ('GRRAGGGKSS'), and a Q-R motif region ('QRQSIYSDPDY'). GNAT-fold enzymes are a well-characterized family whose members in amino acid metabolism are predominantly biosynthetic acetyltransferases (e.g., homoserine O-acetyltransferase, N-acetylglutamate synthase). Among the four options: (D) tetrahydrofolate interconversion enzymes (e.g., SHMT, MTHFR) have entirely different folds; (A) lipid metabolism enzymes (FAS, desaturases, lipases) lack GNAT motifs and typically contain lipid-binding or thioesterase domains absent here; (C) amino-acid degradation relies mainly on transaminases, deaminases, and oxidases, not GNAT acetyltransferases. The combination of GNAT fold + cytoplasmic localization + acetyl-CoA binding motifs is a learned family-level pattern that strongly favors biosynthetic acetyltransferase function in amino acid metabolism over the other three options.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the GNAT fold from sequence motifs (Q-R, RGG, glycine-rich acetyl-CoA binding) is transferable knowledge from many characterized acetyltransferases. Within the GNAT superfamily, amino-acid biosynthetic acetyltransferases are the dominant functional class, and the other three pathway categories involve structurally unrelated enzyme families. This provides a concrete, credible inference distinguishing option B from A, C, and D without requiring the exact UniProt annotation for this specific protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GNAT fold and its strong association with biosynthetic acetyltransferases in amino acid metabolism clearly favors B over the other three options. Lipid metabolism, amino-acid degradation, and tetrahydrofolate interconversion involve fundamentally different enzyme folds and mechanisms not suggested by the sequence."
  },
  "important_caveats": [
    "The GNAT superfamily is functionally diverse; while amino acid biosynthesis is the most common pathway for GNAT enzymes in primary metabolism, some GNAT members function in other contexts. The inference is probabilistic rather than deterministic.",
    "The sequence is from a fungal organism (Cryptococcus neoformans), but the GNAT fold recognition and pathway assignment logic is organism-independent.",
    "The reviewer-only evidence confirms the annotation experimentally, but the model would need to rely on family-level pattern recognition from the sequence alone."
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
  "benchmark_sequence_length": 528,
  "benchmark_sequence_sha256": "57825f4d67b7b8a868fb283bc084d32ce6202d902a078ce010f45f7dba5b26c0",
  "current_entry_audit": {
    "entryVersion": 56,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 528,
  "current_source_sequence_sha256": "57825f4d67b7b8a868fb283bc084d32ce6202d902a078ce010f45f7dba5b26c0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 54,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VIY8",
  "selected_historical_entry_version": 54,
  "selected_historical_record_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "selected_historical_source_sequence_length": 528,
  "selected_historical_source_sequence_sha256": "57825f4d67b7b8a868fb283bc084d32ce6202d902a078ce010f45f7dba5b26c0",
  "selected_historical_version": {
    "accession": "J9VIY8",
    "database": "Swiss-Prot",
    "entryVersion": 54,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MET2_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VIY8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":56,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17353245\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.31\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Homoserine O-acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17353245\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Nazi I.\",\"Scott A.\",\"Sham A.\",\"Rossi L.\",\"Williamson P.R.\",\"Kronstad J.W.\",\"Wright G.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17353245\"},{\"database\":\"DOI\",\"id\":\"10.1128/aac.01400-06\"}],\"citationType\":\"journal article\",\"firstPage\":\"1731\",\"id\":\"17353245\",\"journal\":\"Antimicrob. Agents Chemother.\",\"lastPage\":\"1736\",\"publicationDate\":\"2007\",\"title\":\"Role of homoserine transacetylase as a new target for antifungal agents.\",\"volume\":\"51\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:54.980036+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda",
  "url": "https://rest.uniprot.org/uniprotkb/J9VIY8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H1",
  "excerpt": "ID   MET2_CRYN9              Reviewed;         528 AA.\nAC   J9VIY8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 54.\nDE   RecName: Full=Homoserine O-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.31 {ECO:0000269|PubMed:17353245};\nGN   Name=MET2 {ECO:0000303|PubMed:17353245};\nGN   ORFNames=CNAG_05122 {ECO:0000312|EMBL:AFR94387.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "url": "https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=17353245; DOI=10.1128/aac.01400-06;\nRA   Nazi I., Scott A., Sham A., Rossi L., Williamson P.R., Kronstad J.W.,\nRA   Wright G.D.;\nRT   \"Role of homoserine transacetylase as a new target for antifungal agents.\";\nRL   Antimicrob. Agents Chemother. 51:1731-1736(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "url": "https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway; O-acetyl-L-homoserine from L-homoserine: step 1/1.\nCC       {ECO:0000269|PubMed:17353245}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:57.924962+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844",
  "url": "https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 114. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
