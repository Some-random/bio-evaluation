# cofactor_0085

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0085.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — a divalent metal cation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MALKLVYGVFTLALLGISSVNADCSLKIPESVENEKTPVIMVRKSLKTFEYDLFQPTGEVTNFPERTELLLACTGAQNYFKNGEESVTLMCHNNEFDDGQGNGLDLFTCVKTPTAELRKTKERCSLGDLYVYDVVFRISEEELVGPVYDICYNEYSQKPAYSRNIINGAAVNYRVPESETDLTVSLAKDFTTRDVNNYFKLENQKQRFQGYTIDGKPLVDDKNFFAPGQLAPDTSMITPADKLSTYDYANIVPQYKTVYDGNVWRVENITRDLAVNRQAKFEVYTGGYERLTALHNGKEEEIFLSAKKYVHEIPKYIYKFVVDKENDAGIVFFTLNNPHVKNVKGTEFCKNQCEEANVLDSNFKDWTQGYTFCCTWNNVKDYVRALPQDIEINNLLKFN

[Multiple Choices]
A. Mo-bis(molybdopterin guanine dinucleotide)
B. Mn(2+)
C. FMN
D. a divalent metal cation
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

> The sequence-matched UniProt annotation identifies a divalent metal cation as the cofactor and cites experimental evidence. This supports choice D, though the underlying study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> That this particular protein has nuclease activity and is annotated as requiring a divalent metal cation.


**Reason**

> The sequence has a hydrophobic N-terminus consistent with secretion and is cysteine-rich, but these features do not identify a nuclease family or establish metal dependence. The broad divalent-metal choice would be plausible if nuclease activity were known, but that function is not established by the supplied sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports the broad divalent-metal option; it does not identify Mn(2+) specifically.


### Important caveats

- The supporting cofactor annotation cites an experimental evidence code, but the primary study was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular protein has nuclease activity and is annotated as requiring a divalent metal cation.",
    "reason": "The sequence has a hydrophobic N-terminus consistent with secretion and is cysteine-rich, but these features do not identify a nuclease family or establish metal dependence. The broad divalent-metal choice would be plausible if nuclease activity were known, but that function is not established by the supplied sequence and choices."
  },
  "case_id": "cofactor_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies a divalent metal cation as the cofactor and cites experimental evidence. This supports choice D, though the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The supporting cofactor annotation cites an experimental evidence code, but the primary study was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the broad divalent-metal option; it does not identify Mn(2+) specifically."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies a divalent metal cation as the cofactor and cites experimental evidence. This supports choice D, though the underlying study was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "That this particular protein has nuclease activity and is annotated as requiring a divalent metal cation.",
    "reason": "The sequence has a hydrophobic N-terminus consistent with secretion and is cysteine-rich, but these features do not identify a nuclease family or establish metal dependence. The broad divalent-metal choice would be plausible if nuclease activity were known, but that function is not established by the supplied sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports the broad divalent-metal option; it does not identify Mn(2+) specifically."
  },
  "important_caveats": [
    "The supporting cofactor annotation cites an experimental evidence code, but the primary study was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry D3TS87 (Salivary protein Tsal1, EC 3.1.-.-) annotates the cofactor as 'a divalent metal cation' (ChEBI:CHEBI:60240) with experimental evidence (ECO:0000269|PubMed:23110062, Caljon et al. 2012, PLoS ONE). The sequence matches the benchmark input exactly. The annotation is backed by a primary publication reporting cofactor data for this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains features consistent with a secreted nuclease: an N-terminal signal peptide (MALKLVYGVFTLALLGISSVNADCS), multiple conserved cysteine-rich motifs (e.g., 'CHNNE', 'CVKTPTAELRKTKERCSLG', 'CCTWNNVKDY'), and a central domain with motifs reminiscent of nuclease/ribonuclease superfamily active sites (acidic residues, His-containing stretches like 'YERLTALHNGKEEE'). Recognizing this as a nuclease (EC 3.1.-.-) eliminates A (Mo-bis-MGD, a cofactor for molybdoenzymes such as nitrate/sulfite reductases) and C (FMN, a flavin cofactor for oxidoreductases). Between B (Mn2+) and D (a divalent metal cation): general nuclease biochemistry dictates that the catalytic metal requirement is broadly a divalent cation (Mg2+, Mn2+, Ca2+, Zn2+), and the standard database annotation for nucleases without rigorously metal-specific evidence is the general category 'a divalent metal cation.' The sequence's metal-coordinating residues (His, Asp, Glu) form a generic coordination sphere compatible with multiple divalent metals rather than a highly specific Mn2+-selective site (e.g., no distinctive Mn-specific ligand geometry like a single Asp-His-Asp triad with unusual spacing). Thus, the general category D is the expected and more defensible answer over the overly specific B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can (1) identify nuclease-like sequence architecture (signal peptide, cysteine-rich motifs, acidic/His-containing active-site region), (2) apply general biochemistry that nucleases require divalent metal cations, and (3) apply the learned database pattern that nucleases are typically annotated with the general 'divalent metal cation' category rather than a single specific metal unless metal-specific evidence is compelling. This transfers from other nucleases and general enzyme biochemistry without needing to recall this exact protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A and C are clearly eliminated by enzyme-class reasoning. The B vs D distinction is resolvable by the general pattern that nucleases are annotated with the broad 'divalent metal cation' category; selecting a single specific metal (Mn2+) without metal-specific structural or kinetic evidence is less defensible. No other option pair is genuinely ambiguous.


### Important caveats

- The reviewer evidence confirms experimental support (PubMed 23110062) for the cofactor annotation, but the evaluated model does not see this evidence.
- The B-vs-D distinction relies on a soft learned regularity (general vs. specific metal annotation in nuclease databases) rather than a hard sequence-level rule; a model might still select B if it over-specializes.
- The protein is from Glossina morsitans morsitans (tsetse fly); organism identity is not given to the model but is not needed for the cofactor inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains features consistent with a secreted nuclease: an N-terminal signal peptide (MALKLVYGVFTLALLGISSVNADCS), multiple conserved cysteine-rich motifs (e.g., 'CHNNE', 'CVKTPTAELRKTKERCSLG', 'CCTWNNVKDY'), and a central domain with motifs reminiscent of nuclease/ribonuclease superfamily active sites (acidic residues, His-containing stretches like 'YERLTALHNGKEEE'). Recognizing this as a nuclease (EC 3.1.-.-) eliminates A (Mo-bis-MGD, a cofactor for molybdoenzymes such as nitrate/sulfite reductases) and C (FMN, a flavin cofactor for oxidoreductases). Between B (Mn2+) and D (a divalent metal cation): general nuclease biochemistry dictates that the catalytic metal requirement is broadly a divalent cation (Mg2+, Mn2+, Ca2+, Zn2+), and the standard database annotation for nucleases without rigorously metal-specific evidence is the general category 'a divalent metal cation.' The sequence's metal-coordinating residues (His, Asp, Glu) form a generic coordination sphere compatible with multiple divalent metals rather than a highly specific Mn2+-selective site (e.g., no distinctive Mn-specific ligand geometry like a single Asp-His-Asp triad with unusual spacing). Thus, the general category D is the expected and more defensible answer over the overly specific B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) identify nuclease-like sequence architecture (signal peptide, cysteine-rich motifs, acidic/His-containing active-site region), (2) apply general biochemistry that nucleases require divalent metal cations, and (3) apply the learned database pattern that nucleases are typically annotated with the general 'divalent metal cation' category rather than a single specific metal unless metal-specific evidence is compelling. This transfers from other nucleases and general enzyme biochemistry without needing to recall this exact protein's record."
  },
  "case_id": "cofactor_0085",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry D3TS87 (Salivary protein Tsal1, EC 3.1.-.-) annotates the cofactor as 'a divalent metal cation' (ChEBI:CHEBI:60240) with experimental evidence (ECO:0000269|PubMed:23110062, Caljon et al. 2012, PLoS ONE). The sequence matches the benchmark input exactly. The annotation is backed by a primary publication reporting cofactor data for this protein."
  },
  "important_caveats": [
    "The reviewer evidence confirms experimental support (PubMed 23110062) for the cofactor annotation, but the evaluated model does not see this evidence.",
    "The B-vs-D distinction relies on a soft learned regularity (general vs. specific metal annotation in nuclease databases) rather than a hard sequence-level rule; a model might still select B if it over-specializes.",
    "The protein is from Glossina morsitans morsitans (tsetse fly); organism identity is not given to the model but is not needed for the cofactor inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and C are clearly eliminated by enzyme-class reasoning. The B vs D distinction is resolvable by the general pattern that nucleases are annotated with the broad 'divalent metal cation' category; selecting a single specific metal (Mn2+) without metal-specific structural or kinetic evidence is less defensible. No other option pair is genuinely ambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0085",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry D3TS87 (Salivary protein Tsal1, EC 3.1.-.-) annotates the cofactor as 'a divalent metal cation' (ChEBI:CHEBI:60240) with experimental evidence (ECO:0000269|PubMed:23110062, Caljon et al. 2012, PLoS ONE). The sequence matches the benchmark input exactly. The annotation is backed by a primary publication reporting cofactor data for this protein.",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains features consistent with a secreted nuclease: an N-terminal signal peptide (MALKLVYGVFTLALLGISSVNADCS), multiple conserved cysteine-rich motifs (e.g., 'CHNNE', 'CVKTPTAELRKTKERCSLG', 'CCTWNNVKDY'), and a central domain with motifs reminiscent of nuclease/ribonuclease superfamily active sites (acidic residues, His-containing stretches like 'YERLTALHNGKEEE'). Recognizing this as a nuclease (EC 3.1.-.-) eliminates A (Mo-bis-MGD, a cofactor for molybdoenzymes such as nitrate/sulfite reductases) and C (FMN, a flavin cofactor for oxidoreductases). Between B (Mn2+) and D (a divalent metal cation): general nuclease biochemistry dictates that the catalytic metal requirement is broadly a divalent cation (Mg2+, Mn2+, Ca2+, Zn2+), and the standard database annotation for nucleases without rigorously metal-specific evidence is the general category 'a divalent metal cation.' The sequence's metal-coordinating residues (His, Asp, Glu) form a generic coordination sphere compatible with multiple divalent metals rather than a highly specific Mn2+-selective site (e.g., no distinctive Mn-specific ligand geometry like a single Asp-His-Asp triad with unusual spacing). Thus, the general category D is the expected and more defensible answer over the overly specific B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) identify nuclease-like sequence architecture (signal peptide, cysteine-rich motifs, acidic/His-containing active-site region), (2) apply general biochemistry that nucleases require divalent metal cations, and (3) apply the learned database pattern that nucleases are typically annotated with the general 'divalent metal cation' category rather than a single specific metal unless metal-specific evidence is compelling. This transfers from other nucleases and general enzyme biochemistry without needing to recall this exact protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and C are clearly eliminated by enzyme-class reasoning. The B vs D distinction is resolvable by the general pattern that nucleases are annotated with the broad 'divalent metal cation' category; selecting a single specific metal (Mn2+) without metal-specific structural or kinetic evidence is less defensible. No other option pair is genuinely ambiguous."
  },
  "important_caveats": [
    "The reviewer evidence confirms experimental support (PubMed 23110062) for the cofactor annotation, but the evaluated model does not see this evidence.",
    "The B-vs-D distinction relies on a soft learned regularity (general vs. specific metal annotation in nuclease databases) rather than a hard sequence-level rule; a model might still select B if it over-specializes.",
    "The protein is from Glossina morsitans morsitans (tsetse fly); organism identity is not given to the model but is not needed for the cofactor inference."
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
  "benchmark_sequence_length": 399,
  "benchmark_sequence_sha256": "b256b68cfd3ed8b59941ec1d71aba386118a2dce105bd6733b69c36c45f6f404",
  "current_entry_audit": {
    "entryVersion": 55,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-04-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 399,
  "current_source_sequence_sha256": "b256b68cfd3ed8b59941ec1d71aba386118a2dce105bd6733b69c36c45f6f404",
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
  "requested_accession": "D3TS87",
  "selected_historical_entry_version": 54,
  "selected_historical_record_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "selected_historical_source_sequence_length": 399,
  "selected_historical_source_sequence_sha256": "b256b68cfd3ed8b59941ec1d71aba386118a2dce105bd6733b69c36c45f6f404",
  "selected_historical_version": {
    "accession": "D3TS87",
    "database": "Swiss-Prot",
    "entryVersion": 54,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "SAL1_GLOMM",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D3TS87\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":55,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-04-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Savannah tsetse fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ADD20565.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Hippoboscoidea\",\"Glossinidae\",\"Glossina\"],\"scientificName\":\"Glossina morsitans morsitans\",\"taxonId\":37546}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23110062\",\"source\":\"PubMed\"}],\"value\":\"3.1.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Salivary protein Tsal1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:60240\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23110062\",\"source\":\"PubMed\"}],\"name\":\"a divalent metal cation\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3TS87.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Caljon G.\",\"De Ridder K.\",\"Stijlemans B.\",\"Coosemans M.\",\"Magez S.\",\"De Baetselier P.\",\"Van Den Abbeele J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23110062\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0047233\"}],\"citationType\":\"journal article\",\"firstPage\":\"e47233\",\"id\":\"23110062\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e47233\",\"publicationDate\":\"2012\",\"title\":\"Tsetse salivary gland proteins 1 and 2 are high affinity nucleic acid binding proteins with residual nuclease activity.\",\"volume\":\"7\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:05.191362+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3c1067e8370eea25297614bdbae67343e3373102000f82a7bc457cf5b90750cd",
  "url": "https://rest.uniprot.org/uniprotkb/D3TS87.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H1",
  "excerpt": "ID   SAL1_GLOMM              Reviewed;         399 AA.\nAC   D3TS87; Q9NBA5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-APR-2010, sequence version 1.\nDT   28-JAN-2026, entry version 54.\nDE   RecName: Full=Salivary protein Tsal1 {ECO:0000305};\nDE            EC=3.1.-.- {ECO:0000269|PubMed:23110062};\nDE   Flags: Precursor;\nGN   Name=Tsal1 {ECO:0000303|PubMed:23110062};\nOS   Glossina morsitans morsitans (Savannah tsetse fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Hippoboscoidea;\nOC   Glossinidae; Glossina.\nOX   NCBI_TaxID=37546 {ECO:0000312|EMBL:ADD20565.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Salivary protein Tsal1 {ECO:0000305};\nDE            EC=3.1.-.- {ECO:0000269|PubMed:23110062};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES,\nRP   SUBCELLULAR LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=23110062; DOI=10.1371/journal.pone.0047233;\nRA   Caljon G., De Ridder K., Stijlemans B., Coosemans M., Magez S.,\nRA   De Baetselier P., Van Den Abbeele J.;\nRT   \"Tsetse salivary gland proteins 1 and 2 are high affinity nucleic acid\nRT   binding proteins with residual nuclease activity.\";\nRL   PLoS ONE 7:e47233-e47233(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54)

```json
{
  "entry_version": 54,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=a divalent metal cation; Xref=ChEBI:CHEBI:60240;\nCC         Evidence={ECO:0000269|PubMed:23110062};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:59.125691+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb1240144f3c2dc980be53f5512a9c4a3ca7a37e1d5376ff2eb491982ca7d926",
  "url": "https://rest.uniprot.org/unisave/D3TS87?format=txt&versions=54"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 85. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
