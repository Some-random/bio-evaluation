# EC_number_0064

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0064.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.2.1.11

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASYPKKKCGVLGATGSVGQRFILLLADHPFLELHAIGASNRSAGKKYKDAVRWKQTTAMSERLSNLVLRDCRADQFSDCDLVFSGLNSDVAGEIEMEFIKAEIPVFSNAKNYRKHPLVPLVVPTVNPQHLDLIPHQRKEFGLKKGFLVCNSNCAVIGVVIPFAALQAKFGPVEEVEVFTEQAVSGAGYPGVPSMDIMDNVIPYISGEEDKLENEAQKILGSLNADATAFDEQKGLTVGATCTRVGVTDGHMAFVSLRFKNRPGPSAEEVKQAMREYQSEAQKLGCPSAPREAIKVFDEPDRPQPRLDRDISKGYTVSVGRVREAAPGSYFDLRFAALSHNTVIGAAGSSILNAEVAVIKGYI

[Multiple Choices]
A. 1.2.1.46
B. 1.1.1.195
C. 2.7.1.39
D. 1.2.1.11
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record assigns EC 1.2.1.11 and gives the corresponding catalytic reaction, with both supported by experimental evidence codes. This supports choice D.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has features consistent with the aspartate-semialdehyde dehydrogenase family, including a nucleotide-binding-like N-terminal motif and a conserved cysteine-containing region. Transferable family knowledge connects this enzyme to the phosphorylating oxidation of aspartate semialdehyde, distinguishing EC 1.2.1.11 (D) from the other offered enzyme classifications.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a meaningful basis for choosing among these options without needing the exact protein's database annotation. The inference is not experimental proof, but the offered alternatives make the family distinction relevant.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based family inference and the sequence-matched annotation support the same offered option.


### Important caveats

- The annotation excerpts cite experimental evidence, but the cited primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with the aspartate-semialdehyde dehydrogenase family, including a nucleotide-binding-like N-terminal motif and a conserved cysteine-containing region. Transferable family knowledge connects this enzyme to the phosphorylating oxidation of aspartate semialdehyde, distinguishing EC 1.2.1.11 (D) from the other offered enzyme classifications.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing among these options without needing the exact protein's database annotation. The inference is not experimental proof, but the offered alternatives make the family distinction relevant."
  },
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.2.1.11 and gives the corresponding catalytic reaction, with both supported by experimental evidence codes. This supports choice D."
  },
  "important_caveats": [
    "The annotation excerpts cite experimental evidence, but the cited primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference and the sequence-matched annotation support the same offered option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.2.1.11 and gives the corresponding catalytic reaction, with both supported by experimental evidence codes. This supports choice D.",
    "evidence_ids": ["C1", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has features consistent with the aspartate-semialdehyde dehydrogenase family, including a nucleotide-binding-like N-terminal motif and a conserved cysteine-containing region. Transferable family knowledge connects this enzyme to the phosphorylating oxidation of aspartate semialdehyde, distinguishing EC 1.2.1.11 (D) from the other offered enzyme classifications.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for choosing among these options without needing the exact protein's database annotation. The inference is not experimental proof, but the offered alternatives make the family distinction relevant."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based family inference and the sequence-matched annotation support the same offered option."
  },
  "important_caveats": [
    "The annotation excerpts cite experimental evidence, but the cited primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer-only UniProt evidence (C4, C5, H2, H5) confirms the protein is Aspartate-semialdehyde dehydrogenase (Q4WWR8) with EC 1.2.1.11, annotated with experimental evidence codes (ECO:0000269 from PubMed 28045392 and 29608391). A crystal structure (PDB 5JW6) and biochemical characterization support the catalytic activity: L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+). The sequence matches exactly (363 aa, same SHA256).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark features of the aspartate-semialdehyde dehydrogenase (ASADH) family, one of the most extensively characterized enzyme families across bacteria, fungi, and plants. (1) The N-terminal 'GVLGATGSVG' motif is a canonical Rossmann-fold NAD(P)-binding signature (GxGxxG), shared with hundreds of dehydrogenases but with the specific spacing and flanking context matching ASADH homologs. (2) The catalytic cysteine in the 'GFLVCNSNCAVIG' region is characteristic of aldehyde dehydrogenases (EC 1.2.1.x) that use a Cys-thioester intermediate mechanism, distinguishing them from alcohol dehydrogenases (EC 1.1.x.x) which use Ser/Zn catalysis. This eliminates option B (1.1.1.195). (3) The overall ~363 aa length and two-domain architecture (Rossmann NAD(P)-binding domain + catalytic domain) match the ASADH family size (~340-370 aa) and are inconsistent with multi-domain enzymes. (4) The transferase option C (2.7.1.39) is excluded by the clear oxidoreductase signature (Rossmann fold + catalytic Cys + NAD(P) binding). (5) Between the remaining EC 1.2.1.x options (A: 1.2.1.46 vs D: 1.2.1.11), the specific combination of N-terminal Rossmann fold sequence, catalytic Cys context, and overall fold architecture matches ASADH homologs studied in E. coli, Saccharomyces, and other fungi, where EC 1.2.1.11 is the established assignment. This is transferable family-level knowledge from ASADH characterization across many organisms.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use transferable ASADH family knowledge (Rossmann fold motif, catalytic Cys mechanism, ~360 aa size, two-domain architecture) learned from homologs in E. coli, yeast, plants, and other fungi to distinguish EC 1.2.1.11 from an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), and a different aldehyde dehydrogenase (EC 1.2.1.46). The sequence features are diagnostic at the family level without requiring recall of this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence features (Rossmann fold, catalytic Cys, ~363 aa length, two-domain architecture) clearly point to the ASADH family (EC 1.2.1.11) and are inconsistent with an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), or a structurally distinct aldehyde dehydrogenase. No other option is well-supported by the sequence evidence.


### Important caveats

- The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269) with a crystal structure, not merely computational prediction.
- The exact identity of EC 1.2.1.46 (option A) was not independently verified from the provided materials; the argument for excluding it relies on the sequence matching ASADH family features rather than on knowing the specific properties of 1.2.1.46.
- The UniProt entry was first public in 2025-02-05; the author's source snapshot is unknown, though the sequence has been stable since 2005.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark features of the aspartate-semialdehyde dehydrogenase (ASADH) family, one of the most extensively characterized enzyme families across bacteria, fungi, and plants. (1) The N-terminal 'GVLGATGSVG' motif is a canonical Rossmann-fold NAD(P)-binding signature (GxGxxG), shared with hundreds of dehydrogenases but with the specific spacing and flanking context matching ASADH homologs. (2) The catalytic cysteine in the 'GFLVCNSNCAVIG' region is characteristic of aldehyde dehydrogenases (EC 1.2.1.x) that use a Cys-thioester intermediate mechanism, distinguishing them from alcohol dehydrogenases (EC 1.1.x.x) which use Ser/Zn catalysis. This eliminates option B (1.1.1.195). (3) The overall ~363 aa length and two-domain architecture (Rossmann NAD(P)-binding domain + catalytic domain) match the ASADH family size (~340-370 aa) and are inconsistent with multi-domain enzymes. (4) The transferase option C (2.7.1.39) is excluded by the clear oxidoreductase signature (Rossmann fold + catalytic Cys + NAD(P) binding). (5) Between the remaining EC 1.2.1.x options (A: 1.2.1.46 vs D: 1.2.1.11), the specific combination of N-terminal Rossmann fold sequence, catalytic Cys context, and overall fold architecture matches ASADH homologs studied in E. coli, Saccharomyces, and other fungi, where EC 1.2.1.11 is the established assignment. This is transferable family-level knowledge from ASADH characterization across many organisms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable ASADH family knowledge (Rossmann fold motif, catalytic Cys mechanism, ~360 aa size, two-domain architecture) learned from homologs in E. coli, yeast, plants, and other fungi to distinguish EC 1.2.1.11 from an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), and a different aldehyde dehydrogenase (EC 1.2.1.46). The sequence features are diagnostic at the family level without requiring recall of this specific UniProt entry."
  },
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only UniProt evidence (C4, C5, H2, H5) confirms the protein is Aspartate-semialdehyde dehydrogenase (Q4WWR8) with EC 1.2.1.11, annotated with experimental evidence codes (ECO:0000269 from PubMed 28045392 and 29608391). A crystal structure (PDB 5JW6) and biochemical characterization support the catalytic activity: L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+). The sequence matches exactly (363 aa, same SHA256)."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269) with a crystal structure, not merely computational prediction.",
    "The exact identity of EC 1.2.1.46 (option A) was not independently verified from the provided materials; the argument for excluding it relies on the sequence matching ASADH family features rather than on knowing the specific properties of 1.2.1.46.",
    "The UniProt entry was first public in 2025-02-05; the author's source snapshot is unknown, though the sequence has been stable since 2005."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features (Rossmann fold, catalytic Cys, ~363 aa length, two-domain architecture) clearly point to the ASADH family (EC 1.2.1.11) and are inconsistent with an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), or a structurally distinct aldehyde dehydrogenase. No other option is well-supported by the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only UniProt evidence (C4, C5, H2, H5) confirms the protein is Aspartate-semialdehyde dehydrogenase (Q4WWR8) with EC 1.2.1.11, annotated with experimental evidence codes (ECO:0000269 from PubMed 28045392 and 29608391). A crystal structure (PDB 5JW6) and biochemical characterization support the catalytic activity: L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+). The sequence matches exactly (363 aa, same SHA256).",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark features of the aspartate-semialdehyde dehydrogenase (ASADH) family, one of the most extensively characterized enzyme families across bacteria, fungi, and plants. (1) The N-terminal 'GVLGATGSVG' motif is a canonical Rossmann-fold NAD(P)-binding signature (GxGxxG), shared with hundreds of dehydrogenases but with the specific spacing and flanking context matching ASADH homologs. (2) The catalytic cysteine in the 'GFLVCNSNCAVIG' region is characteristic of aldehyde dehydrogenases (EC 1.2.1.x) that use a Cys-thioester intermediate mechanism, distinguishing them from alcohol dehydrogenases (EC 1.1.x.x) which use Ser/Zn catalysis. This eliminates option B (1.1.1.195). (3) The overall ~363 aa length and two-domain architecture (Rossmann NAD(P)-binding domain + catalytic domain) match the ASADH family size (~340-370 aa) and are inconsistent with multi-domain enzymes. (4) The transferase option C (2.7.1.39) is excluded by the clear oxidoreductase signature (Rossmann fold + catalytic Cys + NAD(P) binding). (5) Between the remaining EC 1.2.1.x options (A: 1.2.1.46 vs D: 1.2.1.11), the specific combination of N-terminal Rossmann fold sequence, catalytic Cys context, and overall fold architecture matches ASADH homologs studied in E. coli, Saccharomyces, and other fungi, where EC 1.2.1.11 is the established assignment. This is transferable family-level knowledge from ASADH characterization across many organisms.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use transferable ASADH family knowledge (Rossmann fold motif, catalytic Cys mechanism, ~360 aa size, two-domain architecture) learned from homologs in E. coli, yeast, plants, and other fungi to distinguish EC 1.2.1.11 from an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), and a different aldehyde dehydrogenase (EC 1.2.1.46). The sequence features are diagnostic at the family level without requiring recall of this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features (Rossmann fold, catalytic Cys, ~363 aa length, two-domain architecture) clearly point to the ASADH family (EC 1.2.1.11) and are inconsistent with an alcohol dehydrogenase (EC 1.1), a transferase (EC 2.7), or a structurally distinct aldehyde dehydrogenase. No other option is well-supported by the sequence evidence."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the annotation is experimentally supported (ECO:0000269) with a crystal structure, not merely computational prediction.",
    "The exact identity of EC 1.2.1.46 (option A) was not independently verified from the provided materials; the argument for excluding it relies on the sequence matching ASADH family features rather than on knowing the specific properties of 1.2.1.46.",
    "The UniProt entry was first public in 2025-02-05; the author's source snapshot is unknown, though the sequence has been stable since 2005."
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
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "current_entry_audit": {
    "entryVersion": 120,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 118,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4WWR8",
  "selected_historical_entry_version": 118,
  "selected_historical_record_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "1177097afcf10563b60e9501753c380ca6ca0a2b4415255d6701ffc15b96c576",
  "selected_historical_version": {
    "accession": "Q4WWR8",
    "database": "Swiss-Prot",
    "entryVersion": 118,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHAS_ASPFU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WWR8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":120,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002530\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28045392\",\"source\":\"PubMed\"}],\"value\":\"AfASADH\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aspartate-semialdehyde dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24286\"}}],\"reaction\":{\"ecNumber\":\"1.2.1.11\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28045392\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29608391\",\"source\":\"PubMed\"}],\"name\":\"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24284\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:537519\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29608391\"},{\"database\":\"DOI\",\"id\":\"10.1177/2472555218767844\"}],\"citationType\":\"journal article\",\"firstPage\":\"520\",\"id\":\"29608391\",\"journal\":\"SLAS Discovery\",\"lastPage\":\"531\",\"publicationDate\":\"2018\",\"title\":\"A Fragment Library Screening Approach to Identify Selective Inhibitors against an Essential Fungal Enzyme.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WWR8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dahal G.P.\",\"Viola R.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28045392\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2053230x16020070\"}],\"citationType\":\"journal article\",\"firstPage\":\"36\",\"id\":\"28045392\",\"journal\":\"Acta Crystallogr. F\",\"lastPage\":\"44\",\"publicationDate\":\"2017\",\"title\":\"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from Aspergillus fumigatus.\",\"volume\":\"73\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5JW6\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:30:55.999038+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "28ec07124002a977d699617a66669087fd52133733f4ac2a92b841504b5fe5c9",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WWR8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H1",
  "excerpt": "ID   DHAS_ASPFU              Reviewed;         363 AA.\nAC   Q4WWR8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 118.\nDE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\nDE   AltName: Full=AfASADH {ECO:0000303|PubMed:28045392};\nGN   Name=hom2 {ECO:0000305};\nGN   ORFNames=AFUA_3G06830 {ECO:0000312|EMBL:EAL92885.1};\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879 {ECO:0000312|Proteomes:UP000002530};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};\nDE            EC=1.2.1.11 {ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\nDE   AltName: Full=AfASADH {ECO:0000303|PubMed:28045392};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND ACTIVITY REGULATION.\nRX   PubMed=29608391; DOI=10.1177/2472555218767844;\nRA   Dahal G.P., Viola R.E.;\nRT   \"A Fragment Library Screening Approach to Identify Selective Inhibitors\nRT   against an Essential Fungal Enzyme.\";\nRL   SLAS Discovery 23:520-531(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:5JW6}\nRP   X-RAY CRYSTALLOGRAPHY (2.39 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.\nRX   PubMed=28045392; DOI=10.1107/s2053230x16020070;\nRA   Dahal G.P., Viola R.E.;\nRT   \"Structure of a fungal form of aspartate-semialdehyde dehydrogenase from\nRT   Aspergillus fumigatus.\";\nRL   Acta Crystallogr. F 73:36-44(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118)

```json
{
  "entry_version": 118,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-\nCC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;\nCC         Evidence={ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;\nCC         Evidence={ECO:0000269|PubMed:28045392, ECO:0000269|PubMed:29608391};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.563757+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "048d52ae97c993889e1431497fcaeb51109d4ebcaca7f00814be073cab21ee35",
  "url": "https://rest.uniprot.org/unisave/Q4WWR8?format=txt&versions=118"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
