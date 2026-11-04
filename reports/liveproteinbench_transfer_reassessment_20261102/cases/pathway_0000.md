# pathway_0000

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0000.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Capsule biogenesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKKILFITGTRADYSKIKSLMYRVQNSSEFELCIFATGMHLSKNFGYTVKELYKNGFKNIYEFINYDKYYQTDKALATTIDGFSRYVNELKPDLIVVHGDRIEPLAAAIVGALNNILVAHIEGGEISGTIDDSLRHAISKLAHIHLVNDEFAKKRLMQLGEDEKSIFIIGSPDLELLNDNKISLNEAKKYYDINYENYALLMFHPVTTEITSIKNQADNLVKALIQSNKNYIVIYPNNDLGFELILQSYEELKNNPRFKLFPSLRFEYFITLLKNADFIIGNSSCILKEALYLKTAGILVGSRQNGRLGNENTLKVNANSDEILKAINTIHKKQDLFSAKLEILDSSKLFFEYLQSGEFFKLSTQKVFKDIII

[Multiple Choices]
A. Capsule biogenesis
B. Bacterial outer membrane biogenesis
C. Amino-acid degradation
D. peptidoglycan degradation. .
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

> The sequence-matched UniProt entry assigns the protein to capsule biogenesis and capsule polysaccharide biosynthesis, citing experimental evidence. The entry identifies it as UDP-N-acetylglucosamine 2-epimerase; the cited publication concerns synthesis of sugar precursors for Campylobacter capsular polysaccharides. This supports choice A, though the primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble enzyme rather than a membrane component, and its enzyme-family-level relationship to UDP-GlcNAc 2-epimerases is the informative signal. Such enzymes supply amino-sugar precursors used in bacterial polysaccharide synthesis, making capsule biogenesis a meaningful fit among these options; the degradation choices are a poorer fit, and the sequence lacks the character expected of an outer-membrane structural protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence similarity and transferable knowledge of nucleotide-sugar enzyme functions can distinguish capsule biogenesis from the offered alternatives. It need not depend on recalling this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, capsule biogenesis is the distinct fit for an enzyme associated with amino-sugar precursor synthesis.


### Important caveats

- The supporting pathway annotation is database evidence citing a study; that study was not independently evaluated here.
- The sequence matches the cited current and historical records, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme rather than a membrane component, and its enzyme-family-level relationship to UDP-GlcNAc 2-epimerases is the informative signal. Such enzymes supply amino-sugar precursors used in bacterial polysaccharide synthesis, making capsule biogenesis a meaningful fit among these options; the degradation choices are a poorer fit, and the sequence lacks the character expected of an outer-membrane structural protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence similarity and transferable knowledge of nucleotide-sugar enzyme functions can distinguish capsule biogenesis from the offered alternatives. It need not depend on recalling this exact protein's database record."
  },
  "case_id": "pathway_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns the protein to capsule biogenesis and capsule polysaccharide biosynthesis, citing experimental evidence. The entry identifies it as UDP-N-acetylglucosamine 2-epimerase; the cited publication concerns synthesis of sugar precursors for Campylobacter capsular polysaccharides. This supports choice A, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The supporting pathway annotation is database evidence citing a study; that study was not independently evaluated here.",
    "The sequence matches the cited current and historical records, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, capsule biogenesis is the distinct fit for an enzyme associated with amino-sugar precursor synthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns the protein to capsule biogenesis and capsule polysaccharide biosynthesis, citing experimental evidence. The entry identifies it as UDP-N-acetylglucosamine 2-epimerase; the cited publication concerns synthesis of sugar precursors for Campylobacter capsular polysaccharides. This supports choice A, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme rather than a membrane component, and its enzyme-family-level relationship to UDP-GlcNAc 2-epimerases is the informative signal. Such enzymes supply amino-sugar precursors used in bacterial polysaccharide synthesis, making capsule biogenesis a meaningful fit among these options; the degradation choices are a poorer fit, and the sequence lacks the character expected of an outer-membrane structural protein.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence similarity and transferable knowledge of nucleotide-sugar enzyme functions can distinguish capsule biogenesis from the offered alternatives. It need not depend on recalling this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, capsule biogenesis is the distinct fit for an enzyme associated with amino-sugar precursor synthesis."
  },
  "important_caveats": [
    "The supporting pathway annotation is database evidence citing a study; that study was not independently evaluated here.",
    "The sequence matches the cited current and historical records, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DY05 (UAEPH_CAMJ8) is annotated as UDP-N-acetylglucosamine 2-epimerase (EC 3.2.1.183, hydrolyzing UDP-GlcNAc 2-epimerase) with the pathway comment 'Capsule biogenesis; capsule polysaccharide biosynthesis' supported by experimental evidence (ECO:0000269|PubMed:38382015, Ghosh & Raushel 2024). The sequence matches the benchmark input exactly (373 AA, SHA256 confirmed). The annotation is backed by a 2024 Biochemistry paper characterizing the enzyme's role in producing UDP-α-N-Acetyl-D-mannosaminuronic acid and CMP-β-N-Acetyl-D-neuraminic acid for Campylobacter jejuni capsule polysaccharides.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 373-residue sequence contains multiple motifs characteristic of nucleotide-sugar processing enzymes: a 'GDRIEP' glycosyltransferase/sugar-processing motif, 'GSPDLELL' and 'IYPNND' segments consistent with Rossmann-like nucleotide-binding folds, and 'IGNSS' resembling a nucleotide-binding loop. These features indicate a sugar-nucleotide-binding/processing enzyme rather than a PLP-dependent aminotransferase, amino-acid dehydrogenase, or lysozyme/amidase. This allows confident elimination of C (amino-acid degradation, which requires amino-acid-specific catalytic motifs such as PLP-binding lysines) and D (peptidoglycan degradation, which requires lysozyme, transglycosylase, or amidase motifs). Between A (capsule biogenesis) and B (outer membrane biogenesis): in bacterial metabolism, sugar-nucleotide-processing enzymes (epimerases, hydrolases acting on UDP-sugars) are directly part of polysaccharide/capsule biosynthesis pathways that generate nucleotide-activated sugar precursors. Outer membrane biogenesis in Gram-negative bacteria primarily involves protein translocation (Sec/Tat), LPS transport (Lpt), and β-barrel assembly (Bam), not sugar-nucleotide hydrolase/epimerase chemistry. Thus, a model recognizing the sugar-nucleotide-processing architecture can reasonably assign the protein to capsule/polysaccharide biosynthesis (A) over outer membrane assembly (B).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence motifs (GDRIEP, GSPDLELL, IYPNND, IGNSS) are recognizable sugar-nucleotide-binding/processing features. General bacterial biology knowledge establishes that sugar-nucleotide-processing enzymes participate in capsule/polysaccharide biosynthesis, not amino-acid degradation or peptidoglycan degradation. The distinction from outer membrane biogenesis rests on the well-known fact that OMB is primarily a protein/lipid assembly process. This is a transferable family-level and pathway-organization inference, not a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the distinction between A (capsule biogenesis) and B (outer membrane biogenesis) is somewhat subtle, the sugar-nucleotide-processing architecture of the sequence more directly implicates polysaccharide/capsule biosynthesis. Options C and D are clearly excluded by the absence of amino-acid-degradation or peptidoglycan-degradation motifs. No option is truly ambiguous given the sequence features.


### Important caveats

- The enzyme (EC 3.2.1.183, hydrolyzing UDP-GlcNAc 2-epimerase) was experimentally characterized in a 2024 paper (Ghosh & Raushel, Biochemistry). A model trained before mid-2024 would not have this specific enzyme in its training data, but the pathway assignment relies on general sugar-nucleotide-processing biology, not on memorizing this specific entry.
- The organism (Campylobacter jejuni) is not provided in the original input. The reasoning relies on general bacterial pathway organization, not organism-specific knowledge.
- The 'hydrolyzing epimerase' activity is mechanistically unusual (a hydrolase with EC 3.2.1.x assigned to epimerase-like function), but the pathway question asks about the broader metabolic context, which is accessible from the sugar-nucleotide-binding architecture.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 373-residue sequence contains multiple motifs characteristic of nucleotide-sugar processing enzymes: a 'GDRIEP' glycosyltransferase/sugar-processing motif, 'GSPDLELL' and 'IYPNND' segments consistent with Rossmann-like nucleotide-binding folds, and 'IGNSS' resembling a nucleotide-binding loop. These features indicate a sugar-nucleotide-binding/processing enzyme rather than a PLP-dependent aminotransferase, amino-acid dehydrogenase, or lysozyme/amidase. This allows confident elimination of C (amino-acid degradation, which requires amino-acid-specific catalytic motifs such as PLP-binding lysines) and D (peptidoglycan degradation, which requires lysozyme, transglycosylase, or amidase motifs). Between A (capsule biogenesis) and B (outer membrane biogenesis): in bacterial metabolism, sugar-nucleotide-processing enzymes (epimerases, hydrolases acting on UDP-sugars) are directly part of polysaccharide/capsule biosynthesis pathways that generate nucleotide-activated sugar precursors. Outer membrane biogenesis in Gram-negative bacteria primarily involves protein translocation (Sec/Tat), LPS transport (Lpt), and β-barrel assembly (Bam), not sugar-nucleotide hydrolase/epimerase chemistry. Thus, a model recognizing the sugar-nucleotide-processing architecture can reasonably assign the protein to capsule/polysaccharide biosynthesis (A) over outer membrane assembly (B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence motifs (GDRIEP, GSPDLELL, IYPNND, IGNSS) are recognizable sugar-nucleotide-binding/processing features. General bacterial biology knowledge establishes that sugar-nucleotide-processing enzymes participate in capsule/polysaccharide biosynthesis, not amino-acid degradation or peptidoglycan degradation. The distinction from outer membrane biogenesis rests on the well-known fact that OMB is primarily a protein/lipid assembly process. This is a transferable family-level and pathway-organization inference, not a lookup of this specific protein's record."
  },
  "case_id": "pathway_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DY05 (UAEPH_CAMJ8) is annotated as UDP-N-acetylglucosamine 2-epimerase (EC 3.2.1.183, hydrolyzing UDP-GlcNAc 2-epimerase) with the pathway comment 'Capsule biogenesis; capsule polysaccharide biosynthesis' supported by experimental evidence (ECO:0000269|PubMed:38382015, Ghosh & Raushel 2024). The sequence matches the benchmark input exactly (373 AA, SHA256 confirmed). The annotation is backed by a 2024 Biochemistry paper characterizing the enzyme's role in producing UDP-α-N-Acetyl-D-mannosaminuronic acid and CMP-β-N-Acetyl-D-neuraminic acid for Campylobacter jejuni capsule polysaccharides."
  },
  "important_caveats": [
    "The enzyme (EC 3.2.1.183, hydrolyzing UDP-GlcNAc 2-epimerase) was experimentally characterized in a 2024 paper (Ghosh & Raushel, Biochemistry). A model trained before mid-2024 would not have this specific enzyme in its training data, but the pathway assignment relies on general sugar-nucleotide-processing biology, not on memorizing this specific entry.",
    "The organism (Campylobacter jejuni) is not provided in the original input. The reasoning relies on general bacterial pathway organization, not organism-specific knowledge.",
    "The 'hydrolyzing epimerase' activity is mechanistically unusual (a hydrolase with EC 3.2.1.x assigned to epimerase-like function), but the pathway question asks about the broader metabolic context, which is accessible from the sugar-nucleotide-binding architecture."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the distinction between A (capsule biogenesis) and B (outer membrane biogenesis) is somewhat subtle, the sugar-nucleotide-processing architecture of the sequence more directly implicates polysaccharide/capsule biosynthesis. Options C and D are clearly excluded by the absence of amino-acid-degradation or peptidoglycan-degradation motifs. No option is truly ambiguous given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DY05 (UAEPH_CAMJ8) is annotated as UDP-N-acetylglucosamine 2-epimerase (EC 3.2.1.183, hydrolyzing UDP-GlcNAc 2-epimerase) with the pathway comment 'Capsule biogenesis; capsule polysaccharide biosynthesis' supported by experimental evidence (ECO:0000269|PubMed:38382015, Ghosh & Raushel 2024). The sequence matches the benchmark input exactly (373 AA, SHA256 confirmed). The annotation is backed by a 2024 Biochemistry paper characterizing the enzyme's role in producing UDP-α-N-Acetyl-D-mannosaminuronic acid and CMP-β-N-Acetyl-D-neuraminic acid for Campylobacter jejuni capsule polysaccharides.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 373-residue sequence contains multiple motifs characteristic of nucleotide-sugar processing enzymes: a 'GDRIEP' glycosyltransferase/sugar-processing motif, 'GSPDLELL' and 'IYPNND' segments consistent with Rossmann-like nucleotide-binding folds, and 'IGNSS' resembling a nucleotide-binding loop. These features indicate a sugar-nucleotide-binding/processing enzyme rather than a PLP-dependent aminotransferase, amino-acid dehydrogenase, or lysozyme/amidase. This allows confident elimination of C (amino-acid degradation, which requires amino-acid-specific catalytic motifs such as PLP-binding lysines) and D (peptidoglycan degradation, which requires lysozyme, transglycosylase, or amidase motifs). Between A (capsule biogenesis) and B (outer membrane biogenesis): in bacterial metabolism, sugar-nucleotide-processing enzymes (epimerases, hydrolases acting on UDP-sugars) are directly part of polysaccharide/capsule biosynthesis pathways that generate nucleotide-activated sugar precursors. Outer membrane biogenesis in Gram-negative bacteria primarily involves protein translocation (Sec/Tat), LPS transport (Lpt), and β-barrel assembly (Bam), not sugar-nucleotide hydrolase/epimerase chemistry. Thus, a model recognizing the sugar-nucleotide-processing architecture can reasonably assign the protein to capsule/polysaccharide biosynthesis (A) over outer membrane assembly (B).",
    "missing_item_specific_fact": "",
    "reason": "The sequence motifs (GDRIEP, GSPDLELL, IYPNND, IGNSS) are recognizable sugar-nucleotide-binding/processing features. General bacterial biology knowledge establishes that sugar-nucleotide-processing enzymes participate in capsule/polysaccharide biosynthesis, not amino-acid degradation or peptidoglycan degradation. The distinction from outer membrane biogenesis rests on the well-known fact that OMB is primarily a protein/lipid assembly process. This is a transferable family-level and pathway-organization inference, not a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the distinction between A (capsule biogenesis) and B (outer membrane biogenesis) is somewhat subtle, the sugar-nucleotide-processing architecture of the sequence more directly implicates polysaccharide/capsule biosynthesis. Options C and D are clearly excluded by the absence of amino-acid-degradation or peptidoglycan-degradation motifs. No option is truly ambiguous given the sequence features."
  },
  "important_caveats": [
    "The enzyme (EC 3.2.1.183, hydrolyzing UDP-GlcNAc 2-epimerase) was experimentally characterized in a 2024 paper (Ghosh & Raushel, Biochemistry). A model trained before mid-2024 would not have this specific enzyme in its training data, but the pathway assignment relies on general sugar-nucleotide-processing biology, not on memorizing this specific entry.",
    "The organism (Campylobacter jejuni) is not provided in the original input. The reasoning relies on general bacterial pathway organization, not organism-specific knowledge.",
    "The 'hydrolyzing epimerase' activity is mechanistically unusual (a hydrolase with EC 3.2.1.x assigned to epimerase-like function), but the pathway question asks about the broader metabolic context, which is accessible from the sugar-nucleotide-binding architecture."
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
  "benchmark_sequence_length": 373,
  "benchmark_sequence_sha256": "e7bbdfb124fa6a1f8e0776ef9cfe10605110b022d22f31aa7d87fd2dc63013ef",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 373,
  "current_source_sequence_sha256": "e7bbdfb124fa6a1f8e0776ef9cfe10605110b022d22f31aa7d87fd2dc63013ef",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DY05",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "selected_historical_source_sequence_length": 373,
  "selected_historical_source_sequence_sha256": "e7bbdfb124fa6a1f8e0776ef9cfe10605110b022d22f31aa7d87fd2dc63013ef",
  "selected_historical_version": {
    "accession": "P0DY05",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "UAEPH_CAMJ8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DY05\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC 11828)\",\"taxonId\":407148}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Hydrolyzing UDP-GlcNAc 2-epimerase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.183\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetylglucosamine 2-epimerase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Capsule biogenesis; capsule polysaccharide biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY05.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"81116 / NCTC 11828\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:02.588931+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "937863d80c17ba7d03766f73daed6baf04c3868cee0583cc1c8025708304b5ec",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY05.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   UAEPH_CAMJ8             Reviewed;         373 AA.\nAC   P0DY05;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};\nDE            EC=3.2.1.183 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=Hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};\nGN   Name=HS6.10 {ECO:0000303|PubMed:38382015};\nGN   OrderedLocusNames=C8J_1338 {ECO:0000312|EMBL:ABV52936.1};\nOS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC\nOS   11828).\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=407148;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=81116 / NCTC 11828;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Capsule biogenesis; capsule polysaccharide biosynthesis.\nCC       {ECO:0000269|PubMed:38382015}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:04.730217+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5278ef9f060bf7f207cf54b4687f7078769e5e37b32a8bf7f2e5dacb2ff686b5",
  "url": "https://rest.uniprot.org/unisave/P0DY05?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
