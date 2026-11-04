# cofactor_0013

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0013.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNNDEQLEFLINYLLDERSESIDIPKTFSEKRNLLRSLMNMRHPSNISEEFLRIQDEFLSRETANKNLTSVEDISLSSGKIMLWQGDITTLSADAIVNAANSKLLGCFIPMHNCIDNIIHSASGLQLREECNRMIMLQGGDEDVGKAKITNAYNLPSKYVVHTVGPSIERGMRVSSDDVKKLERCYNSCLELASEYKLNSIAFCCISTGVFNFPQKKAAEIAIRTVKDFLNSNETSLNHIIFDVFTDKDYDIYKKLLFGN

[Multiple Choices]
A. pantetheine 4'-phosphate
B. FMN
C. Zn(2+)
D. tungstopterin
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

> The exact sequence matches the archived UniProt record, which annotates one Zn(2+) ion per subunit with experimental evidence. The cited crystallographic work also includes complexes with Zn(2+), supporting choice C for this protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains several histidine and cysteine residues in a pattern compatible with a metal-binding site. Transferable knowledge that some ADP-ribose-hydrolyzing macrodomains use catalytic Zn makes Zn(2+) a credible choice among these options; the alternatives are not suggested by an evident flavin-binding or other cofactor motif. This is a family-level inference, not proof of metal binding from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A meaningful sequence- and family-based inference favors Zn(2+) over the offered alternatives without needing the exact protein's database annotation. The sequence alone may not establish the cofactor conclusively, but certainty is not required for reasoning_supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is comparably supported by the sequence-based metal-binding and family-level inference.


### Important caveats

- The reviewer-only annotation and structural evidence support the key but were not part of the original model input.
- The sequence-based inference is probabilistic; the strongest direct evidence for this exact protein is the reviewer-only experimental annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several histidine and cysteine residues in a pattern compatible with a metal-binding site. Transferable knowledge that some ADP-ribose-hydrolyzing macrodomains use catalytic Zn makes Zn(2+) a credible choice among these options; the alternatives are not suggested by an evident flavin-binding or other cofactor motif. This is a family-level inference, not proof of metal binding from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A meaningful sequence- and family-based inference favors Zn(2+) over the offered alternatives without needing the exact protein's database annotation. The sequence alone may not establish the cofactor conclusively, but certainty is not required for reasoning_supported."
  },
  "case_id": "cofactor_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt record, which annotates one Zn(2+) ion per subunit with experimental evidence. The cited crystallographic work also includes complexes with Zn(2+), supporting choice C for this protein."
  },
  "important_caveats": [
    "The reviewer-only annotation and structural evidence support the key but were not part of the original model input.",
    "The sequence-based inference is probabilistic; the strongest direct evidence for this exact protein is the reviewer-only experimental annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence-based metal-binding and family-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt record, which annotates one Zn(2+) ion per subunit with experimental evidence. The cited crystallographic work also includes complexes with Zn(2+), supporting choice C for this protein.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains several histidine and cysteine residues in a pattern compatible with a metal-binding site. Transferable knowledge that some ADP-ribose-hydrolyzing macrodomains use catalytic Zn makes Zn(2+) a credible choice among these options; the alternatives are not suggested by an evident flavin-binding or other cofactor motif. This is a family-level inference, not proof of metal binding from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "A meaningful sequence- and family-based inference favors Zn(2+) over the offered alternatives without needing the exact protein's database annotation. The sequence alone may not establish the cofactor conclusively, but certainty is not required for reasoning_supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence-based metal-binding and family-level inference."
  },
  "important_caveats": [
    "The reviewer-only annotation and structural evidence support the key but were not part of the original model input.",
    "The sequence-based inference is probabilistic; the strongest direct evidence for this exact protein is the reviewer-only experimental annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A166ACJ5 (sequence matched, 260 AA) annotates this protein as a Protein-ADP-ribose hydrolase (MorMacro) with Zn(2+) as cofactor, supported by experimental evidence (ECO:0000269, PubMed:39270823). X-ray crystallography at 1.66 Å (PDB 8RSI, 8RSJ, 8RSK) confirmed Zn(2+) binding in complex with ADP-ribose and substrate analogues. The annotation states 'Binds 1 Zn(2+) ion per subunit.' This is direct experimental evidence, not computational inference.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable macrodomain (PF00563) fold signatures: the conserved 'GG-D-E-D' motif (GGDEDVGK around residues ~130-137), conserved Y and D residues, and the overall ~260-residue architecture. Macrodomains are a well-studied protein family functioning primarily as ADP-ribosylhydrolases or ADP-ribose readers. Among the four offered cofactors, Zn(2+) is the only one consistent with a hydrolase active site. Pantetheine 4'-phosphate is the prosthetic group of acyl carrier proteins and fatty acid synthases (requires a GHSQG-type serine motif absent here). FMN is a cofactor for oxidoreductases (ferredoxin-NADP+ reductases, NADH oxidases), not hydrolases. Tungstopterin is restricted to specific large multi-subunit methanogenesis enzymes (formylmethanofuran dehydrogenase, aldehyde oxidoreductase) with entirely different sequences and folds; while the organism is a methanogenic archaeon, tungstopterin enzymes are not 260-residue single-domain proteins. The zinc-dependent macrodomain subfamily is a recognized pattern in the ADP-ribosylation literature. Thus, recognizing the macrodomain fold and knowing the general biochemistry of macrodomain hydrolases (Zn-dependent catalysis is the dominant mechanism in characterized macrodomain hydrolases) meaningfully selects Zn(2+) over the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of the macrodomain protein family (sequence motifs, fold, function as ADP-ribosylhydrolase) and general cofactor-protein-family associations (pantetheine→ACP, FMN→oxidoreductase, tungstopterin→specific methanogenesis enzymes, Zn→hydrolases) can credibly eliminate A, B, and D and select C without knowing this exact protein's database annotation. The macrodomain fold recognition from the GGDEDVGK motif and conserved residues is a legitimate family-level inference from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are each associated with well-defined, unrelated protein families (ACP/fatty acid synthase for pantetheine, oxidoreductases for FMN, tungstopterin-dependent methanogenesis enzymes for tungstopterin). None of these families share the macrodomain fold or hydrolase function evident in the sequence. Zn(2+) is the only cofactor consistent with a macrodomain ADP-ribosylhydrolase.


### Important caveats

- The macrodomain fold recognition relies on the GG-D-E-D motif and other conserved residues being identifiable by a model; this is a well-characterized family (PF00563) but the exact subfamily assignment (zinc-dependent vs. other macrodomain types) benefits from specific literature knowledge.
- The organism being a methanogenic archaeon could superficially make tungstopterin seem plausible, but tungstopterin enzymes are large multi-subunit complexes with entirely different sequences, making this a weak distractor.
- The experimental evidence (X-ray crystallography, ECO:0000269) is reviewer-only and was not available to the evaluated model; the model must rely on sequence-based family recognition and general biochemistry.
- The UniProt entry was first publicly released in June 2025, so the specific annotation was not available at the time the benchmark was likely constructed; however, the macrodomain family and its Zn-dependence were known from other proteins well before this entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable macrodomain (PF00563) fold signatures: the conserved 'GG-D-E-D' motif (GGDEDVGK around residues ~130-137), conserved Y and D residues, and the overall ~260-residue architecture. Macrodomains are a well-studied protein family functioning primarily as ADP-ribosylhydrolases or ADP-ribose readers. Among the four offered cofactors, Zn(2+) is the only one consistent with a hydrolase active site. Pantetheine 4'-phosphate is the prosthetic group of acyl carrier proteins and fatty acid synthases (requires a GHSQG-type serine motif absent here). FMN is a cofactor for oxidoreductases (ferredoxin-NADP+ reductases, NADH oxidases), not hydrolases. Tungstopterin is restricted to specific large multi-subunit methanogenesis enzymes (formylmethanofuran dehydrogenase, aldehyde oxidoreductase) with entirely different sequences and folds; while the organism is a methanogenic archaeon, tungstopterin enzymes are not 260-residue single-domain proteins. The zinc-dependent macrodomain subfamily is a recognized pattern in the ADP-ribosylation literature. Thus, recognizing the macrodomain fold and knowing the general biochemistry of macrodomain hydrolases (Zn-dependent catalysis is the dominant mechanism in characterized macrodomain hydrolases) meaningfully selects Zn(2+) over the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the macrodomain protein family (sequence motifs, fold, function as ADP-ribosylhydrolase) and general cofactor-protein-family associations (pantetheine→ACP, FMN→oxidoreductase, tungstopterin→specific methanogenesis enzymes, Zn→hydrolases) can credibly eliminate A, B, and D and select C without knowing this exact protein's database annotation. The macrodomain fold recognition from the GGDEDVGK motif and conserved residues is a legitimate family-level inference from other proteins."
  },
  "case_id": "cofactor_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A166ACJ5 (sequence matched, 260 AA) annotates this protein as a Protein-ADP-ribose hydrolase (MorMacro) with Zn(2+) as cofactor, supported by experimental evidence (ECO:0000269, PubMed:39270823). X-ray crystallography at 1.66 Å (PDB 8RSI, 8RSJ, 8RSK) confirmed Zn(2+) binding in complex with ADP-ribose and substrate analogues. The annotation states 'Binds 1 Zn(2+) ion per subunit.' This is direct experimental evidence, not computational inference."
  },
  "important_caveats": [
    "The macrodomain fold recognition relies on the GG-D-E-D motif and other conserved residues being identifiable by a model; this is a well-characterized family (PF00563) but the exact subfamily assignment (zinc-dependent vs. other macrodomain types) benefits from specific literature knowledge.",
    "The organism being a methanogenic archaeon could superficially make tungstopterin seem plausible, but tungstopterin enzymes are large multi-subunit complexes with entirely different sequences, making this a weak distractor.",
    "The experimental evidence (X-ray crystallography, ECO:0000269) is reviewer-only and was not available to the evaluated model; the model must rely on sequence-based family recognition and general biochemistry.",
    "The UniProt entry was first publicly released in June 2025, so the specific annotation was not available at the time the benchmark was likely constructed; however, the macrodomain family and its Zn-dependence were known from other proteins well before this entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are each associated with well-defined, unrelated protein families (ACP/fatty acid synthase for pantetheine, oxidoreductases for FMN, tungstopterin-dependent methanogenesis enzymes for tungstopterin). None of these families share the macrodomain fold or hydrolase function evident in the sequence. Zn(2+) is the only cofactor consistent with a macrodomain ADP-ribosylhydrolase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A166ACJ5 (sequence matched, 260 AA) annotates this protein as a Protein-ADP-ribose hydrolase (MorMacro) with Zn(2+) as cofactor, supported by experimental evidence (ECO:0000269, PubMed:39270823). X-ray crystallography at 1.66 Å (PDB 8RSI, 8RSJ, 8RSK) confirmed Zn(2+) binding in complex with ADP-ribose and substrate analogues. The annotation states 'Binds 1 Zn(2+) ion per subunit.' This is direct experimental evidence, not computational inference.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable macrodomain (PF00563) fold signatures: the conserved 'GG-D-E-D' motif (GGDEDVGK around residues ~130-137), conserved Y and D residues, and the overall ~260-residue architecture. Macrodomains are a well-studied protein family functioning primarily as ADP-ribosylhydrolases or ADP-ribose readers. Among the four offered cofactors, Zn(2+) is the only one consistent with a hydrolase active site. Pantetheine 4'-phosphate is the prosthetic group of acyl carrier proteins and fatty acid synthases (requires a GHSQG-type serine motif absent here). FMN is a cofactor for oxidoreductases (ferredoxin-NADP+ reductases, NADH oxidases), not hydrolases. Tungstopterin is restricted to specific large multi-subunit methanogenesis enzymes (formylmethanofuran dehydrogenase, aldehyde oxidoreductase) with entirely different sequences and folds; while the organism is a methanogenic archaeon, tungstopterin enzymes are not 260-residue single-domain proteins. The zinc-dependent macrodomain subfamily is a recognized pattern in the ADP-ribosylation literature. Thus, recognizing the macrodomain fold and knowing the general biochemistry of macrodomain hydrolases (Zn-dependent catalysis is the dominant mechanism in characterized macrodomain hydrolases) meaningfully selects Zn(2+) over the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the macrodomain protein family (sequence motifs, fold, function as ADP-ribosylhydrolase) and general cofactor-protein-family associations (pantetheine→ACP, FMN→oxidoreductase, tungstopterin→specific methanogenesis enzymes, Zn→hydrolases) can credibly eliminate A, B, and D and select C without knowing this exact protein's database annotation. The macrodomain fold recognition from the GGDEDVGK motif and conserved residues is a legitimate family-level inference from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are each associated with well-defined, unrelated protein families (ACP/fatty acid synthase for pantetheine, oxidoreductases for FMN, tungstopterin-dependent methanogenesis enzymes for tungstopterin). None of these families share the macrodomain fold or hydrolase function evident in the sequence. Zn(2+) is the only cofactor consistent with a macrodomain ADP-ribosylhydrolase."
  },
  "important_caveats": [
    "The macrodomain fold recognition relies on the GG-D-E-D motif and other conserved residues being identifiable by a model; this is a well-characterized family (PF00563) but the exact subfamily assignment (zinc-dependent vs. other macrodomain types) benefits from specific literature knowledge.",
    "The organism being a methanogenic archaeon could superficially make tungstopterin seem plausible, but tungstopterin enzymes are large multi-subunit complexes with entirely different sequences, making this a weak distractor.",
    "The experimental evidence (X-ray crystallography, ECO:0000269) is reviewer-only and was not available to the evaluated model; the model must rely on sequence-based family recognition and general biochemistry.",
    "The UniProt entry was first publicly released in June 2025, so the specific annotation was not available at the time the benchmark was likely constructed; however, the macrodomain family and its Zn-dependence were known from other proteins well before this entry."
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
  "benchmark_sequence_length": 260,
  "benchmark_sequence_sha256": "65e85ca38633159b990366322b725e7b1ea032bffadbc04cde2fb4f55492a876",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2016-07-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 260,
  "current_source_sequence_sha256": "65e85ca38633159b990366322b725e7b1ea032bffadbc04cde2fb4f55492a876",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 27,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A166ACJ5",
  "selected_historical_entry_version": 27,
  "selected_historical_record_sha256": "f41d9345e837fc4cf2fc216b27d3d0376b1a15c8a77bce7c0dd1066928158c4f",
  "selected_historical_source_sequence_length": 260,
  "selected_historical_source_sequence_sha256": "65e85ca38633159b990366322b725e7b1ea032bffadbc04cde2fb4f55492a876",
  "selected_historical_version": {
    "accession": "A0A166ACJ5",
    "database": "Swiss-Prot",
    "entryVersion": 27,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ADPRH_METOA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A166ACJ5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:27.127121+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2016-07-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:27.127121+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanobacteria\",\"Methanobacteriales\",\"Methanobacteriaceae\",\"Methanobrevibacter\"],\"scientificName\":\"Methanobrevibacter oralis\",\"taxonId\":66851}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:27.127121+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"MorMacro\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Protein-ADP-ribose hydrolase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:27.127121+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 Zn(2+) ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:27.127121+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ariza A.\",\"Liu Q.\",\"Cowieson N.P.\",\"Ahel I.\",\"Filippov D.V.\",\"Rack J.G.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39270823\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107770\"}],\"citationType\":\"journal article\",\"firstPage\":\"107770\",\"id\":\"39270823\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107770\",\"publicationDate\":\"2024\",\"title\":\"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-dependent macrodomains.\",\"volume\":\"300\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8RSI\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8RSJ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8RSK\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.66 ANGSTROMS) IN COMPLEXES WITH ZN(2+); ADP-RIBOSE AND NONHYDROLYZABLE SUBSTRATE ASPARAGINE-ADP-RIBOSE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:27.127121+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dce5876ec2d350f0bac765c597eb0b1c98c4c62457defdc5e04c69c2b29bcfdb",
  "url": "https://rest.uniprot.org/uniprotkb/A0A166ACJ5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H1",
  "excerpt": "ID   ADPRH_METOA             Reviewed;         260 AA.\nAC   A0A166ACJ5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-JUL-2016, sequence version 1.\nDT   28-JAN-2026, entry version 27.\nDE   RecName: Full=Protein-ADP-ribose hydrolase {ECO:0000305};\nDE            EC=3.2.1.- {ECO:0000269|PubMed:39270823};\nDE   AltName: Full=MorMacro {ECO:0000303|PubMed:39270823};\nGN   ORFNames=MBORA_13990 {ECO:0000312|EMBL:KZX11859.1};\nOS   Methanobrevibacter oralis.\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanobacteria; Methanobacteriales; Methanobacteriaceae;\nOC   Methanobrevibacter.\nOX   NCBI_TaxID=66851;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:29.689150+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f41d9345e837fc4cf2fc216b27d3d0376b1a15c8a77bce7c0dd1066928158c4f",
  "url": "https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Protein-ADP-ribose hydrolase {ECO:0000305};\nDE            EC=3.2.1.- {ECO:0000269|PubMed:39270823};\nDE   AltName: Full=MorMacro {ECO:0000303|PubMed:39270823};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:29.689150+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f41d9345e837fc4cf2fc216b27d3d0376b1a15c8a77bce7c0dd1066928158c4f",
  "url": "https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:8RSI, ECO:0007744|PDB:8RSJ, ECO:0007744|PDB:8RSK}\nRP   X-RAY CRYSTALLOGRAPHY (1.66 ANGSTROMS) IN COMPLEXES WITH ZN(2+); ADP-RIBOSE\nRP   AND NONHYDROLYZABLE SUBSTRATE ASPARAGINE-ADP-RIBOSE, FUNCTION, CATALYTIC\nRP   ACTIVITY, COFACTOR, AND SUBUNIT.\nRX   PubMed=39270823; DOI=10.1016/j.jbc.2024.107770;\nRA   Ariza A., Liu Q., Cowieson N.P., Ahel I., Filippov D.V., Rack J.G.M.;\nRT   \"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-\nRT   dependent macrodomains.\";\nRL   J. Biol. Chem. 300:107770-107770(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:29.689150+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f41d9345e837fc4cf2fc216b27d3d0376b1a15c8a77bce7c0dd1066928158c4f",
  "url": "https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000269|PubMed:39270823};\nCC       Note=Binds 1 Zn(2+) ion per subunit. {ECO:0000269|PubMed:39270823};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:29.689150+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f41d9345e837fc4cf2fc216b27d3d0376b1a15c8a77bce7c0dd1066928158c4f",
  "url": "https://rest.uniprot.org/unisave/A0A166ACJ5?format=txt&versions=27"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
