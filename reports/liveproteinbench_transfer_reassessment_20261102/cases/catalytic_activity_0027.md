# catalytic_activity_0027

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0027.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSLSNKLAITDVDLKDKRVLIRVDFNVPLDADKKITNNQRIVGALPTIKYAIENGAKAVVLMSHLGRPDGKANPKYSLKPVATELEKLLSKSVIFAENCVGKETEEIVNKATGGQVILLENLRFHAEEEGSSKDAEGKKVKADKEKVEEFRKGLTALGDVYINDAFGTAHRAHSSMVGVDLPQKASGFLVKKELEYFAKALESPQRPFLAILGGAKVSDKIQLIDNLLPKVNSLIITGAMAFTFKKTLENVKIGNSLFDEAGSKIVGDIVEKAKKNNVKIVLPVDYVTADKFAADAKTGYATDADGIPDGYMGLDVGEKSVELYKKTIAEAKTILWNGPPGVFELEPFANATKKTLDAAVAAAQSGSIVIIGGGDTATVAAKYGAEAKLSHVSTGGGASLELLEGKVLPGVDALSSK

[Multiple Choices]
A. ATP + protein L-histidine = ADP + protein N-phospho-L-histidine.
B. L-lysyl-[protein] + acetyl-CoA = N(6)-acetyl-L-lysyl-[protein] + CoA + H(+)
C. (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP
D. (2R,3R,5S)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + AH2 + 2 S-adenosyl-L-methionine = (2R,3R,5S,6R)-6-(methyl)-2-(S-pantetheinyl)-carbapenam-3-carboxylate + 5'-deoxyadenosine + L-methionine + A + S-adenosyl-L-homocysteine + 2 H(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as phosphoglycerate kinase, and the recorded catalytic reaction is option C. The annotation is transferred by similarity from UniProtKB:P00560 (ECO:0000250), rather than direct experimental evidence for this exact protein in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 417-residue sequence is consistent with the conserved, two-domain phosphoglycerate kinase family. Knowledge of this enzyme family supports the ATP-dependent phosphorylation of 3-phosphoglycerate represented by C. The alternatives instead describe protein histidine phosphorylation, lysine acetylation, or specialized carbapenam methylation, none of which matches the PGK family inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the well-established PGK reaction meaningfully distinguish C from the offered alternatives without requiring the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct activities, and the sequence supports the phosphoglycerate kinase activity in C.


### Important caveats

- The supplied reviewer-only annotation supports C but attributes the reaction annotation to similarity with another UniProtKB protein; it is not direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 417-residue sequence is consistent with the conserved, two-domain phosphoglycerate kinase family. Knowledge of this enzyme family supports the ATP-dependent phosphorylation of 3-phosphoglycerate represented by C. The alternatives instead describe protein histidine phosphorylation, lysine acetylation, or specialized carbapenam methylation, none of which matches the PGK family inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the well-established PGK reaction meaningfully distinguish C from the offered alternatives without requiring the exact protein's database record."
  },
  "case_id": "catalytic_activity_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as phosphoglycerate kinase, and the recorded catalytic reaction is option C. The annotation is transferred by similarity from UniProtKB:P00560 (ECO:0000250), rather than direct experimental evidence for this exact protein in the supplied excerpts."
  },
  "important_caveats": [
    "The supplied reviewer-only annotation supports C but attributes the reaction annotation to similarity with another UniProtKB protein; it is not direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct activities, and the sequence supports the phosphoglycerate kinase activity in C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as phosphoglycerate kinase, and the recorded catalytic reaction is option C. The annotation is transferred by similarity from UniProtKB:P00560 (ECO:0000250), rather than direct experimental evidence for this exact protein in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 417-residue sequence is consistent with the conserved, two-domain phosphoglycerate kinase family. Knowledge of this enzyme family supports the ATP-dependent phosphorylation of 3-phosphoglycerate represented by C. The alternatives instead describe protein histidine phosphorylation, lysine acetylation, or specialized carbapenam methylation, none of which matches the PGK family inference.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the well-established PGK reaction meaningfully distinguish C from the offered alternatives without requiring the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct activities, and the sequence supports the phosphoglycerate kinase activity in C."
  },
  "important_caveats": [
    "The supplied reviewer-only annotation supports C but attributes the reaction annotation to similarity with another UniProtKB protein; it is not direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7G5KET3 (PGK1_ASPFN) annotates this protein as Phosphoglycerate kinase (EC 2.7.2.3) with catalytic activity exactly matching option C: (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP. The annotation evidence code is ECO:0000250 (inferred by similarity from UniProtKB:P00560), which is computational but the sequence match is exact and the family assignment is unambiguous.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple highly conserved phosphoglycerate kinase (PGK) signature motifs that are transferable knowledge across all PGK homologs: (1) 'GGAKV' glycine-rich loop motif (~residues 250-254), a hallmark of the PGK family found in every characterized PGK from bacteria to humans; (2) 'VSTGGGAS' Walker-A-like motif (~residues 393-400), a distinctive PGK-specific nucleotide-binding signature; (3) 'GGGDTATVAA' active-site motif (~residues 370-380), another PGK-specific conserved stretch; (4) overall ~417 aa length and two-domain architecture typical of PGK. These motifs are extensively documented in protein family databases (Pfam PF00162, PROSITE PS00065) and taught in biochemistry. Option A (histidine kinase), B (lysine acetyltransferase), and D (radical SAM methyltransferase) belong to entirely different enzyme classes with no sequence resemblance to PGK. A knowledgeable model recognizing the GGAKV and STGGGAS motifs would confidently select C without needing the specific UniProt record for this exact Aspergillus flavus protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PGK-specific sequence motifs (GGAKV, VSTGGGAS, GGGDTATVAA) are universally conserved across the PGK family and constitute standard transferable knowledge. These motifs unambiguously identify the protein as phosphoglycerate kinase and distinguish it from the three other offered enzyme classes, none of which share these motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four completely different enzyme classes (histidine kinase, lysine acetyltransferase, phosphoglycerate kinase, radical SAM methyltransferase). The PGK-specific motifs in the sequence leave no ambiguity; only option C is consistent with the observed sequence features.


### Important caveats

- The UniProt catalytic activity annotation carries evidence code ECO:0000250 (similarity-based inference from P00560), not direct experimental characterization of this specific Aspergillus flavus protein. However, the sequence identity to canonical PGK is extremely high and the family assignment is unambiguous.
- The reviewer-only evidence confirms sequence match and annotation, but this information was not available to the evaluated model. The reasoning above relies solely on transferable PGK family knowledge accessible from the sequence itself.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple highly conserved phosphoglycerate kinase (PGK) signature motifs that are transferable knowledge across all PGK homologs: (1) 'GGAKV' glycine-rich loop motif (~residues 250-254), a hallmark of the PGK family found in every characterized PGK from bacteria to humans; (2) 'VSTGGGAS' Walker-A-like motif (~residues 393-400), a distinctive PGK-specific nucleotide-binding signature; (3) 'GGGDTATVAA' active-site motif (~residues 370-380), another PGK-specific conserved stretch; (4) overall ~417 aa length and two-domain architecture typical of PGK. These motifs are extensively documented in protein family databases (Pfam PF00162, PROSITE PS00065) and taught in biochemistry. Option A (histidine kinase), B (lysine acetyltransferase), and D (radical SAM methyltransferase) belong to entirely different enzyme classes with no sequence resemblance to PGK. A knowledgeable model recognizing the GGAKV and STGGGAS motifs would confidently select C without needing the specific UniProt record for this exact Aspergillus flavus protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PGK-specific sequence motifs (GGAKV, VSTGGGAS, GGGDTATVAA) are universally conserved across the PGK family and constitute standard transferable knowledge. These motifs unambiguously identify the protein as phosphoglycerate kinase and distinguish it from the three other offered enzyme classes, none of which share these motifs."
  },
  "case_id": "catalytic_activity_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7G5KET3 (PGK1_ASPFN) annotates this protein as Phosphoglycerate kinase (EC 2.7.2.3) with catalytic activity exactly matching option C: (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP. The annotation evidence code is ECO:0000250 (inferred by similarity from UniProtKB:P00560), which is computational but the sequence match is exact and the family assignment is unambiguous."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation carries evidence code ECO:0000250 (similarity-based inference from P00560), not direct experimental characterization of this specific Aspergillus flavus protein. However, the sequence identity to canonical PGK is extremely high and the family assignment is unambiguous.",
    "The reviewer-only evidence confirms sequence match and annotation, but this information was not available to the evaluated model. The reasoning above relies solely on transferable PGK family knowledge accessible from the sequence itself."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four completely different enzyme classes (histidine kinase, lysine acetyltransferase, phosphoglycerate kinase, radical SAM methyltransferase). The PGK-specific motifs in the sequence leave no ambiguity; only option C is consistent with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7G5KET3 (PGK1_ASPFN) annotates this protein as Phosphoglycerate kinase (EC 2.7.2.3) with catalytic activity exactly matching option C: (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP. The annotation evidence code is ECO:0000250 (inferred by similarity from UniProtKB:P00560), which is computational but the sequence match is exact and the family assignment is unambiguous.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple highly conserved phosphoglycerate kinase (PGK) signature motifs that are transferable knowledge across all PGK homologs: (1) 'GGAKV' glycine-rich loop motif (~residues 250-254), a hallmark of the PGK family found in every characterized PGK from bacteria to humans; (2) 'VSTGGGAS' Walker-A-like motif (~residues 393-400), a distinctive PGK-specific nucleotide-binding signature; (3) 'GGGDTATVAA' active-site motif (~residues 370-380), another PGK-specific conserved stretch; (4) overall ~417 aa length and two-domain architecture typical of PGK. These motifs are extensively documented in protein family databases (Pfam PF00162, PROSITE PS00065) and taught in biochemistry. Option A (histidine kinase), B (lysine acetyltransferase), and D (radical SAM methyltransferase) belong to entirely different enzyme classes with no sequence resemblance to PGK. A knowledgeable model recognizing the GGAKV and STGGGAS motifs would confidently select C without needing the specific UniProt record for this exact Aspergillus flavus protein.",
    "missing_item_specific_fact": "",
    "reason": "The PGK-specific sequence motifs (GGAKV, VSTGGGAS, GGGDTATVAA) are universally conserved across the PGK family and constitute standard transferable knowledge. These motifs unambiguously identify the protein as phosphoglycerate kinase and distinguish it from the three other offered enzyme classes, none of which share these motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four completely different enzyme classes (histidine kinase, lysine acetyltransferase, phosphoglycerate kinase, radical SAM methyltransferase). The PGK-specific motifs in the sequence leave no ambiguity; only option C is consistent with the observed sequence features."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation carries evidence code ECO:0000250 (similarity-based inference from P00560), not direct experimental characterization of this specific Aspergillus flavus protein. However, the sequence identity to canonical PGK is extremely high and the family assignment is unambiguous.",
    "The reviewer-only evidence confirms sequence match and annotation, but this information was not available to the evaluated model. The reasoning above relies solely on transferable PGK family knowledge accessible from the sequence itself."
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
  "benchmark_sequence_length": 417,
  "benchmark_sequence_sha256": "275622872aa5039ffd4e2fafadfa8fcabe446204f6ab488fbd8b5e29f8a6b5e4",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-02-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 417,
  "current_source_sequence_sha256": "275622872aa5039ffd4e2fafadfa8fcabe446204f6ab488fbd8b5e29f8a6b5e4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7G5KET3",
  "selected_historical_entry_version": 18,
  "selected_historical_record_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "selected_historical_source_sequence_length": 417,
  "selected_historical_source_sequence_sha256": "275622872aa5039ffd4e2fafadfa8fcabe446204f6ab488fbd8b5e29f8a6b5e4",
  "selected_historical_version": {
    "accession": "A0A7G5KET3",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PGK1_ASPFN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7G5KET3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-02-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000596276\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357 / JCM 12722 / SRRC 167)\",\"taxonId\":332952}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00560\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.3\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU000532\",\"source\":\"RuleBase\"}],\"value\":\"Phosphoglycerate kinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.2.3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P00560\",\"source\":\"UniProtKB\"}],\"name\":\"(2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14801\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57604\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58272\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:35.568831+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "79f801166dc030cf4959c0881b37cd1bd39704c428283cc65f9c68002c1fbb5b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7G5KET3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H1",
  "excerpt": "ID   PGK1_ASPFN              Reviewed;         417 AA.\nAC   A0A7G5KET3; B8NIQ9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-FEB-2021, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=Phosphoglycerate kinase {ECO:0000255|RuleBase:RU000532};\nDE            EC=2.7.2.3 {ECO:0000250|UniProtKB:P00560};\nGN   Name=pgk1 {ECO:0000303|PubMed:37754565};\nGN   ORFNames=F9C07_8361 {ECO:0000312|EMBL:QRD93909.1};\nOS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357\nOS   / JCM 12722 / SRRC 167).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=332952 {ECO:0000312|Proteomes:UP000596276};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Phosphoglycerate kinase {ECO:0000255|RuleBase:RU000532};\nDE            EC=2.7.2.3 {ECO:0000250|UniProtKB:P00560};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, PHOSPHORYLATION AT\nRP   SER-203, AND MUTAGENESIS OF SER-203.\nRX   PubMed=37754565; DOI=10.1128/mbio.00977-23;\nRA   Zhu Z., Yang M., Yang G., Zhang B., Cao X., Yuan J., Ge F., Wang S.;\nRT   \"PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy\nRT   and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.\";\nRL   MBio 14:e0097723-e0097723(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl\nCC         phosphate + ADP; Xref=Rhea:RHEA:14801, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:57604, ChEBI:CHEBI:58272, ChEBI:CHEBI:456216; EC=2.7.2.3;\nCC         Evidence={ECO:0000250|UniProtKB:P00560};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:37.377118+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b429698fb3b322f2fc43bbd8bc72a321c4e8bcf2772d689c13b699dd201233ec",
  "url": "https://rest.uniprot.org/unisave/A0A7G5KET3?format=txt&versions=18"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
