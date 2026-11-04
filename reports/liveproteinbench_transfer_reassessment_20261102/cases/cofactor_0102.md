# cofactor_0102

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0102.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — pyridoxal 5&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAQEMRYFSTRGGKETLSFEDAVLTGLAPNGGLYIPTHIPALPKDWKTKWAGLSFPELSHEILSLFVPTSVIPSDDLQSIINTAYSSFRSPATTPIRQTGDNEYVLELWHGPTWAFKDVALQFLGELFRYFLERRNKDKTEDMEELTVVGATSGDTGSAAIYGLRSKPSITIFILYPDGRVSPIQEAQMATVPDANVYCVAVEDSDFDTCQSIVKTLFSDAQFNATHRLGAINSINWARILAQIVYYFSAYFQLPEEARKDGAKLQFVVPTGNFGDILAGWYAKKLGLPMEQLVVATNENDILERFFRTGRYEADDAVQQDQTAETAAVNGSSDGQQAVSAVKATHSPAMDILLSSNFERLLYYLALETNGTEGSDEEKRFKAQERLNDWMSTLKKDGKVDLGEDVRQAAGKDFWAERVSDGQTLEEIQKYYRREKYGPYVVDPHTAVGLTAQERSAKKASPDTTWITLSTAHPAKFSGAVELALSASEFPDFDFRRDVLPDELKKLEGLEKRVHRVKGEEGVRALIEKVKSASHEKVDAEEGRGSL

[Multiple Choices]
A. pyridoxal 5'-phosphate
B. Fe(2+)
C. FMN
D. Ca(2+)
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

> The sequence-matched UniProt annotation identifies pyridoxal 5'-phosphate as the cofactor, with evidence transferred from UniProtKB:P16120; the entry also annotates the protein as threonine synthase. This supports the key, though the cited evidence is not direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 547-residue sequence is consistent with the threonine-synthase family, whose PLP-dependent chemistry is a transferable family-level clue. PLP is therefore meaningfully favored over the offered metal-ion and FMN alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use sequence-family recognition and the known cofactor dependence of threonine synthases to distinguish PLP without recalling this exact protein's database record. This is a family-based inference, not proof of the cofactor experimentally for this individual protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, PLP is the clear family-level expectation; no competing option is comparably supported.


### Important caveats

- The cited cofactor annotation is transferred from a homolog (ECO:0000250), rather than shown here to derive from a direct cofactor-binding or activity experiment on this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 547-residue sequence is consistent with the threonine-synthase family, whose PLP-dependent chemistry is a transferable family-level clue. PLP is therefore meaningfully favored over the offered metal-ion and FMN alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use sequence-family recognition and the known cofactor dependence of threonine synthases to distinguish PLP without recalling this exact protein's database record. This is a family-based inference, not proof of the cofactor experimentally for this individual protein."
  },
  "case_id": "cofactor_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies pyridoxal 5'-phosphate as the cofactor, with evidence transferred from UniProtKB:P16120; the entry also annotates the protein as threonine synthase. This supports the key, though the cited evidence is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The cited cofactor annotation is transferred from a homolog (ECO:0000250), rather than shown here to derive from a direct cofactor-binding or activity experiment on this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, PLP is the clear family-level expectation; no competing option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies pyridoxal 5'-phosphate as the cofactor, with evidence transferred from UniProtKB:P16120; the entry also annotates the protein as threonine synthase. This supports the key, though the cited evidence is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 547-residue sequence is consistent with the threonine-synthase family, whose PLP-dependent chemistry is a transferable family-level clue. PLP is therefore meaningfully favored over the offered metal-ion and FMN alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use sequence-family recognition and the known cofactor dependence of threonine synthases to distinguish PLP without recalling this exact protein's database record. This is a family-based inference, not proof of the cofactor experimentally for this individual protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, PLP is the clear family-level expectation; no competing option is comparably supported."
  },
  "important_caveats": [
    "The cited cofactor annotation is transferred from a homolog (ECO:0000250), rather than shown here to derive from a direct cofactor-binding or activity experiment on this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (J9VI85) identifies this protein as Threonine synthase (EC 4.2.3.1) with cofactor pyridoxal 5'-phosphate (ChEBI:597326). The evidence code ECO:0000250 indicates inference by similarity to P16120 (E. coli threonine synthase), a well-characterized PLP-dependent enzyme. Threonine synthase is a canonical member of the fold-type II PLP enzyme superfamily, and the sequence contains the highly conserved PLP-binding motif 'GATSGDTGSAAIYGL' (~residues 148-162), which is a hallmark of PLP-dependent enzymes. The annotation is consistent with established biochemistry of threonine synthase across multiple organisms.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical PLP-binding motif 'GATSGDTGS' (visible at approximately positions 148-156: 'VGATSGDTGSAAIYGL'), which is one of the most recognizable sequence signatures in enzymology. This motif is shared across hundreds of fold-type II PLP-dependent enzymes (serine hydroxymethyltransferase, threonine synthase, serine palmitoyltransferase, aspartate decarboxylase, etc.), making it highly transferable knowledge. The motif 'GxTSGDTG' coordinates the PLP cofactor via a lysine residue and is essentially diagnostic of PLP dependence. The distractors are readily excluded: Fe(2+)-dependent enzymes typically feature His/Asp/Glu metal-binding triads (e.g., 2-His-1-carboxylate facial triad); FMN-binding enzymes use Rossmann-like 'GxGxxG' dinucleotide-binding motifs; Ca(2+)-binding proteins use 'DxDxDG' or EF-hand motifs. None of these alternative signatures are present. The overall ~547-residue length and domain architecture are also consistent with fold-type II PLP enzymes. A knowledgeable model trained on general biochemistry could recognize the 'GATSGDTGS' motif and conclude PLP dependence without memorizing this specific protein's annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PLP-binding 'GATSGDTGS' motif is a textbook-level sequence signature shared across the entire fold-type II PLP enzyme superfamily. This is standard transferable knowledge from dozens of well-characterized PLP enzymes. The motif directly distinguishes option A from the three distractors, whose characteristic cofactor-binding motifs (metal triads, Rossmann folds, EF-hands) are absent from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PLP-binding motif is unambiguous and the distractors (Fe2+, FMN, Ca2+) each have well-defined alternative sequence signatures not present in this sequence. No other option is defensible.


### Important caveats

- The UniProt cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to P16120), not direct experimental evidence for this specific Cryptococcus protein. However, the PLP dependence of threonine synthase is experimentally established in the E. coli homolog and the sequence motif is directly visible.
- The protein was integrated into Swiss-Prot in February 2025; the author's source snapshot is unknown but the sequence has been unchanged since 2012.
- The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning relies solely on the sequence motif and general PLP-enzyme knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical PLP-binding motif 'GATSGDTGS' (visible at approximately positions 148-156: 'VGATSGDTGSAAIYGL'), which is one of the most recognizable sequence signatures in enzymology. This motif is shared across hundreds of fold-type II PLP-dependent enzymes (serine hydroxymethyltransferase, threonine synthase, serine palmitoyltransferase, aspartate decarboxylase, etc.), making it highly transferable knowledge. The motif 'GxTSGDTG' coordinates the PLP cofactor via a lysine residue and is essentially diagnostic of PLP dependence. The distractors are readily excluded: Fe(2+)-dependent enzymes typically feature His/Asp/Glu metal-binding triads (e.g., 2-His-1-carboxylate facial triad); FMN-binding enzymes use Rossmann-like 'GxGxxG' dinucleotide-binding motifs; Ca(2+)-binding proteins use 'DxDxDG' or EF-hand motifs. None of these alternative signatures are present. The overall ~547-residue length and domain architecture are also consistent with fold-type II PLP enzymes. A knowledgeable model trained on general biochemistry could recognize the 'GATSGDTGS' motif and conclude PLP dependence without memorizing this specific protein's annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PLP-binding 'GATSGDTGS' motif is a textbook-level sequence signature shared across the entire fold-type II PLP enzyme superfamily. This is standard transferable knowledge from dozens of well-characterized PLP enzymes. The motif directly distinguishes option A from the three distractors, whose characteristic cofactor-binding motifs (metal triads, Rossmann folds, EF-hands) are absent from the sequence."
  },
  "case_id": "cofactor_0102",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (J9VI85) identifies this protein as Threonine synthase (EC 4.2.3.1) with cofactor pyridoxal 5'-phosphate (ChEBI:597326). The evidence code ECO:0000250 indicates inference by similarity to P16120 (E. coli threonine synthase), a well-characterized PLP-dependent enzyme. Threonine synthase is a canonical member of the fold-type II PLP enzyme superfamily, and the sequence contains the highly conserved PLP-binding motif 'GATSGDTGSAAIYGL' (~residues 148-162), which is a hallmark of PLP-dependent enzymes. The annotation is consistent with established biochemistry of threonine synthase across multiple organisms."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to P16120), not direct experimental evidence for this specific Cryptococcus protein. However, the PLP dependence of threonine synthase is experimentally established in the E. coli homolog and the sequence motif is directly visible.",
    "The protein was integrated into Swiss-Prot in February 2025; the author's source snapshot is unknown but the sequence has been unchanged since 2012.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning relies solely on the sequence motif and general PLP-enzyme knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PLP-binding motif is unambiguous and the distractors (Fe2+, FMN, Ca2+) each have well-defined alternative sequence signatures not present in this sequence. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0102",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (J9VI85) identifies this protein as Threonine synthase (EC 4.2.3.1) with cofactor pyridoxal 5'-phosphate (ChEBI:597326). The evidence code ECO:0000250 indicates inference by similarity to P16120 (E. coli threonine synthase), a well-characterized PLP-dependent enzyme. Threonine synthase is a canonical member of the fold-type II PLP enzyme superfamily, and the sequence contains the highly conserved PLP-binding motif 'GATSGDTGSAAIYGL' (~residues 148-162), which is a hallmark of PLP-dependent enzymes. The annotation is consistent with established biochemistry of threonine synthase across multiple organisms.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical PLP-binding motif 'GATSGDTGS' (visible at approximately positions 148-156: 'VGATSGDTGSAAIYGL'), which is one of the most recognizable sequence signatures in enzymology. This motif is shared across hundreds of fold-type II PLP-dependent enzymes (serine hydroxymethyltransferase, threonine synthase, serine palmitoyltransferase, aspartate decarboxylase, etc.), making it highly transferable knowledge. The motif 'GxTSGDTG' coordinates the PLP cofactor via a lysine residue and is essentially diagnostic of PLP dependence. The distractors are readily excluded: Fe(2+)-dependent enzymes typically feature His/Asp/Glu metal-binding triads (e.g., 2-His-1-carboxylate facial triad); FMN-binding enzymes use Rossmann-like 'GxGxxG' dinucleotide-binding motifs; Ca(2+)-binding proteins use 'DxDxDG' or EF-hand motifs. None of these alternative signatures are present. The overall ~547-residue length and domain architecture are also consistent with fold-type II PLP enzymes. A knowledgeable model trained on general biochemistry could recognize the 'GATSGDTGS' motif and conclude PLP dependence without memorizing this specific protein's annotation.",
    "missing_item_specific_fact": "",
    "reason": "The PLP-binding 'GATSGDTGS' motif is a textbook-level sequence signature shared across the entire fold-type II PLP enzyme superfamily. This is standard transferable knowledge from dozens of well-characterized PLP enzymes. The motif directly distinguishes option A from the three distractors, whose characteristic cofactor-binding motifs (metal triads, Rossmann folds, EF-hands) are absent from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PLP-binding motif is unambiguous and the distractors (Fe2+, FMN, Ca2+) each have well-defined alternative sequence signatures not present in this sequence. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to P16120), not direct experimental evidence for this specific Cryptococcus protein. However, the PLP dependence of threonine synthase is experimentally established in the E. coli homolog and the sequence motif is directly visible.",
    "The protein was integrated into Swiss-Prot in February 2025; the author's source snapshot is unknown but the sequence has been unchanged since 2012.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning relies solely on the sequence motif and general PLP-enzyme knowledge."
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
  "benchmark_sequence_length": 547,
  "benchmark_sequence_sha256": "c29de6f54eb7b3652e0ebb99edcca36018a5532e49d71f579a4be901d48f70b5",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 547,
  "current_source_sequence_sha256": "c29de6f54eb7b3652e0ebb99edcca36018a5532e49d71f579a4be901d48f70b5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 52,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VI85",
  "selected_historical_entry_version": 52,
  "selected_historical_record_sha256": "5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5",
  "selected_historical_source_sequence_length": 547,
  "selected_historical_source_sequence_sha256": "c29de6f54eb7b3652e0ebb99edcca36018a5532e49d71f579a4be901d48f70b5",
  "selected_historical_version": {
    "accession": "J9VI85",
    "database": "Swiss-Prot",
    "entryVersion": 52,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "THRC_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VI85\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR93116.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P16120\",\"source\":\"UniProtKB\"}],\"value\":\"4.2.3.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Threonine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"TS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:597326\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P16120\",\"source\":\"UniProtKB\"}],\"name\":\"pyridoxal 5'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)

```json
{
  "entry_version": 52,
  "evidence_id": "H1",
  "excerpt": "ID   THRC_CRYN9              Reviewed;         547 AA.\nAC   J9VI85; B2MW84;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 52.\nDE   RecName: Full=Threonine synthase {ECO:0000305};\nDE            Short=TS {ECO:0000305};\nDE            EC=4.2.3.1 {ECO:0000250|UniProtKB:P16120};\nGN   Name=THR4 {ECO:0000303|PubMed:18757810};\nGN   ORFNames=CNAG_03612 {ECO:0000312|EMBL:AFR93116.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|EMBL:AFR93116.1, ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.836361+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5",
  "url": "https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)

```json
{
  "entry_version": 52,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Threonine synthase {ECO:0000305};\nDE            Short=TS {ECO:0000305};\nDE            EC=4.2.3.1 {ECO:0000250|UniProtKB:P16120};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.836361+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5",
  "url": "https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)

```json
{
  "entry_version": 52,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ACC94295.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=H99 / ATCC 208821 / CBS 10515 / FGSC 9487\nRC   {ECO:0000303|PubMed:18757810};\nRX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;\nRA   Kingsbury J.M., McCusker J.H.;\nRT   \"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\";\nRL   Microbiology 154:2767-2775(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.836361+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5",
  "url": "https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)

```json
{
  "entry_version": 52,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;\nCC         Evidence={ECO:0000250|UniProtKB:P16120};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.836361+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5",
  "url": "https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 102. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
