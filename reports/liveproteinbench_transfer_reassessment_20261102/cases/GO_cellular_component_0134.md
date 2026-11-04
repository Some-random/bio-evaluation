# GO_cellular_component_0134

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0134.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — endoplasmic reticulum

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSTNAGGIASKQASSMAPNPGKATILALGHAFPQQLVMQDYVVDGFMRNTNCDDPELKEKLTRLCKTTTVKTRYVVMSEEILKSYPELAQEGQPTMKQRLDISNKAVTQMATEASLACVRSWGGALSEITHLVYVSSSEARFPGGDLHLARALGLSPDVRRVMLAFTGCSGGVAGLRVAKGLAESCPGARVLLATSETTIVGFRPPSPDRPYDLVGVALFGDGAGAAVVGADPTPVERPLFELHSALQRFLPDTDKTIDGRLTEEGIKFQLGRELPHIIEANVEAFCQKLMQEHPQAADKLTYGDMFWAVHPGGPAILTKMEGRLGLDGGKLRASRSALRDFGNASSNTIVYVLENMVEETRQRREEAAEEEDCEWGLILAFGPGITFEGILARNLQARARARD

[Multiple Choices]
A. actin cytoskeleton
B. site of double-strand break
C. endoplasmic reticulum
D. vesicle
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence matches the protein in the supplied UniProt records. Both the historical and current records annotate endoplasmic reticulum localization, with the GO annotation carrying IDA evidence; this supports choice C, though the underlying study was not independently reviewed here.

Citations as saved: [H5](#evidence-h5), [H6](#evidence-h6), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble type III polyketide synthase, rather than a cytoskeletal component or a DNA-damage-site protein. But that family-level information does not specifically favor ER localization: such enzymes are generally soluble, and this sequence has no obvious signal peptide or transmembrane segment. ER association may occur, but it is not reliably inferable from the sequence and choices alone.


**Missing item-specific fact**

> Whether this particular enzyme localizes to the endoplasmic reticulum, rather than being a soluble enzyme elsewhere in the cell.


**Reason**

> Transferable family and sequence features make the actin-cytoskeleton and double-strand-break options unlikely, but do not establish the specific ER localization needed to choose C over the remaining alternative. The distinguishing fact is this protein’s experimentally reported localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports ER localization, and no other offered choice is comparably supported. The limitation is that this localization is not meaningfully predictable from the original sequence alone.


### Important caveats

- The localization evidence is a database annotation with IDA evidence; the cited primary study was not independently evaluated.
- The sequence match and historical record support applicability, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble type III polyketide synthase, rather than a cytoskeletal component or a DNA-damage-site protein. But that family-level information does not specifically favor ER localization: such enzymes are generally soluble, and this sequence has no obvious signal peptide or transmembrane segment. ER association may occur, but it is not reliably inferable from the sequence and choices alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular enzyme localizes to the endoplasmic reticulum, rather than being a soluble enzyme elsewhere in the cell.",
    "reason": "Transferable family and sequence features make the actin-cytoskeleton and double-strand-break options unlikely, but do not establish the specific ER localization needed to choose C over the remaining alternative. The distinguishing fact is this protein’s experimentally reported localization."
  },
  "case_id": "GO_cellular_component_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H6",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the protein in the supplied UniProt records. Both the historical and current records annotate endoplasmic reticulum localization, with the GO annotation carrying IDA evidence; this supports choice C, though the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The localization evidence is a database annotation with IDA evidence; the cited primary study was not independently evaluated.",
    "The sequence match and historical record support applicability, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports ER localization, and no other offered choice is comparably supported. The limitation is that this localization is not meaningfully predictable from the original sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the protein in the supplied UniProt records. Both the historical and current records annotate endoplasmic reticulum localization, with the GO annotation carrying IDA evidence; this supports choice C, though the underlying study was not independently reviewed here.",
    "evidence_ids": ["H5", "H6", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble type III polyketide synthase, rather than a cytoskeletal component or a DNA-damage-site protein. But that family-level information does not specifically favor ER localization: such enzymes are generally soluble, and this sequence has no obvious signal peptide or transmembrane segment. ER association may occur, but it is not reliably inferable from the sequence and choices alone.",
    "missing_item_specific_fact": "Whether this particular enzyme localizes to the endoplasmic reticulum, rather than being a soluble enzyme elsewhere in the cell.",
    "reason": "Transferable family and sequence features make the actin-cytoskeleton and double-strand-break options unlikely, but do not establish the specific ER localization needed to choose C over the remaining alternative. The distinguishing fact is this protein’s experimentally reported localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports ER localization, and no other offered choice is comparably supported. The limitation is that this localization is not meaningfully predictable from the original sequence alone."
  },
  "important_caveats": [
    "The localization evidence is a database annotation with IDA evidence; the cited primary study was not independently evaluated.",
    "The sequence match and historical record support applicability, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8H305 (PKS10_ORYSJ) carries the subcellular location annotation 'Endoplasmic reticulum' with evidence code ECO:0000269 (experimental) from PubMed:29411094 (Zou et al., 2018, Plant Cell Rep.), and the corresponding GO:0005783 annotation is IDA:UniProtKB. The sequence in the question matches the UniProt entry exactly (405 aa, SHA-256 match). The experimental evidence directly supports ER localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable Type III polyketide synthase (chalcone synthase superfamily) catalytic motifs (e.g., 'GCSGGVAGLRVAKG', 'FGDGAGAAVVGADPTP', 'GPGITFEGILARNLQ'), identifying it as a lipid-modifying enzyme. Options A (actin cytoskeleton) and B (site of double-strand break) are readily eliminated because the protein has no cytoskeletal or DNA-repair motifs. Between C (ER) and D (vesicle): transferable knowledge from plant biology shows that enzymes catalyzing lipid modifications for structural polymers (sporopollenin, cutin, suberin) — such as CYP703, CYP704, ACOS5, and related PKSs — are consistently ER-associated, working on the ER membrane surface where lipid precursors are available. Additionally, the sequence lacks a strong N-terminal signal peptide (the N-terminus 'MVSTNAGGIASKQASSMAPNPGK...' is not a classic cleavable signal peptide), which argues against entry into the secretory/vesicle trafficking pathway. A PKS engaged in biosynthetic lipid modification is functionally an ER-membrane enzyme, not a vesicle cargo. This family-level and functional inference meaningfully distinguishes C from D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the PKS catalytic motifs, eliminate cytoskeletal and DNA-damage options, and use the well-established pattern that plant lipid-modification enzymes for structural polymers localize to the ER. The absence of a strong signal peptide further disfavors vesicle targeting. The inference is probabilistic and family-level rather than definitive from a single sequence feature, but it meaningfully distinguishes the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are clearly incompatible with a PKS enzyme. Between C and D, the functional context (lipid biosynthesis enzyme) and absence of a signal peptide favor ER over vesicle, though the ER-vs-vesicle distinction is not trivially encoded in the sequence and relies on family-level biological knowledge.


### Important caveats

- The ER localization was established experimentally (IDA) via fluorescent protein fusion in rice tapetum cells; the sequence alone does not contain a canonical signal peptide or transmembrane domain that unambiguously predicts ER targeting.
- Most Type III PKSs (e.g., chalcone synthase) are cytoplasmic; ER localization is a specialized feature of sporopollenin-related PKSs, so the family-level argument requires recognizing the specific functional sub-class.
- The model input does not include organism identity or protein name; the inference relies on recognizing PKS catalytic motifs and applying general plant secondary-metabolism compartmentation knowledge.
- The ER-vs-vesicle distinction is the weakest part of the reasoning chain; both are membrane compartments and the sequence does not contain a definitive feature separating them.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable Type III polyketide synthase (chalcone synthase superfamily) catalytic motifs (e.g., 'GCSGGVAGLRVAKG', 'FGDGAGAAVVGADPTP', 'GPGITFEGILARNLQ'), identifying it as a lipid-modifying enzyme. Options A (actin cytoskeleton) and B (site of double-strand break) are readily eliminated because the protein has no cytoskeletal or DNA-repair motifs. Between C (ER) and D (vesicle): transferable knowledge from plant biology shows that enzymes catalyzing lipid modifications for structural polymers (sporopollenin, cutin, suberin) — such as CYP703, CYP704, ACOS5, and related PKSs — are consistently ER-associated, working on the ER membrane surface where lipid precursors are available. Additionally, the sequence lacks a strong N-terminal signal peptide (the N-terminus 'MVSTNAGGIASKQASSMAPNPGK...' is not a classic cleavable signal peptide), which argues against entry into the secretory/vesicle trafficking pathway. A PKS engaged in biosynthetic lipid modification is functionally an ER-membrane enzyme, not a vesicle cargo. This family-level and functional inference meaningfully distinguishes C from D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PKS catalytic motifs, eliminate cytoskeletal and DNA-damage options, and use the well-established pattern that plant lipid-modification enzymes for structural polymers localize to the ER. The absence of a strong signal peptide further disfavors vesicle targeting. The inference is probabilistic and family-level rather than definitive from a single sequence feature, but it meaningfully distinguishes the offered alternatives."
  },
  "case_id": "GO_cellular_component_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C9",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8H305 (PKS10_ORYSJ) carries the subcellular location annotation 'Endoplasmic reticulum' with evidence code ECO:0000269 (experimental) from PubMed:29411094 (Zou et al., 2018, Plant Cell Rep.), and the corresponding GO:0005783 annotation is IDA:UniProtKB. The sequence in the question matches the UniProt entry exactly (405 aa, SHA-256 match). The experimental evidence directly supports ER localization."
  },
  "important_caveats": [
    "The ER localization was established experimentally (IDA) via fluorescent protein fusion in rice tapetum cells; the sequence alone does not contain a canonical signal peptide or transmembrane domain that unambiguously predicts ER targeting.",
    "Most Type III PKSs (e.g., chalcone synthase) are cytoplasmic; ER localization is a specialized feature of sporopollenin-related PKSs, so the family-level argument requires recognizing the specific functional sub-class.",
    "The model input does not include organism identity or protein name; the inference relies on recognizing PKS catalytic motifs and applying general plant secondary-metabolism compartmentation knowledge.",
    "The ER-vs-vesicle distinction is the weakest part of the reasoning chain; both are membrane compartments and the sequence does not contain a definitive feature separating them."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly incompatible with a PKS enzyme. Between C and D, the functional context (lipid biosynthesis enzyme) and absence of a signal peptide favor ER over vesicle, though the ER-vs-vesicle distinction is not trivially encoded in the sequence and relies on family-level biological knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8H305 (PKS10_ORYSJ) carries the subcellular location annotation 'Endoplasmic reticulum' with evidence code ECO:0000269 (experimental) from PubMed:29411094 (Zou et al., 2018, Plant Cell Rep.), and the corresponding GO:0005783 annotation is IDA:UniProtKB. The sequence in the question matches the UniProt entry exactly (405 aa, SHA-256 match). The experimental evidence directly supports ER localization.",
    "evidence_ids": ["C5", "C6", "C9", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable Type III polyketide synthase (chalcone synthase superfamily) catalytic motifs (e.g., 'GCSGGVAGLRVAKG', 'FGDGAGAAVVGADPTP', 'GPGITFEGILARNLQ'), identifying it as a lipid-modifying enzyme. Options A (actin cytoskeleton) and B (site of double-strand break) are readily eliminated because the protein has no cytoskeletal or DNA-repair motifs. Between C (ER) and D (vesicle): transferable knowledge from plant biology shows that enzymes catalyzing lipid modifications for structural polymers (sporopollenin, cutin, suberin) — such as CYP703, CYP704, ACOS5, and related PKSs — are consistently ER-associated, working on the ER membrane surface where lipid precursors are available. Additionally, the sequence lacks a strong N-terminal signal peptide (the N-terminus 'MVSTNAGGIASKQASSMAPNPGK...' is not a classic cleavable signal peptide), which argues against entry into the secretory/vesicle trafficking pathway. A PKS engaged in biosynthetic lipid modification is functionally an ER-membrane enzyme, not a vesicle cargo. This family-level and functional inference meaningfully distinguishes C from D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PKS catalytic motifs, eliminate cytoskeletal and DNA-damage options, and use the well-established pattern that plant lipid-modification enzymes for structural polymers localize to the ER. The absence of a strong signal peptide further disfavors vesicle targeting. The inference is probabilistic and family-level rather than definitive from a single sequence feature, but it meaningfully distinguishes the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are clearly incompatible with a PKS enzyme. Between C and D, the functional context (lipid biosynthesis enzyme) and absence of a signal peptide favor ER over vesicle, though the ER-vs-vesicle distinction is not trivially encoded in the sequence and relies on family-level biological knowledge."
  },
  "important_caveats": [
    "The ER localization was established experimentally (IDA) via fluorescent protein fusion in rice tapetum cells; the sequence alone does not contain a canonical signal peptide or transmembrane domain that unambiguously predicts ER targeting.",
    "Most Type III PKSs (e.g., chalcone synthase) are cytoplasmic; ER localization is a specialized feature of sporopollenin-related PKSs, so the family-level argument requires recognizing the specific functional sub-class.",
    "The model input does not include organism identity or protein name; the inference relies on recognizing PKS catalytic motifs and applying general plant secondary-metabolism compartmentation knowledge.",
    "The ER-vs-vesicle distinction is the weakest part of the reasoning chain; both are membrane compartments and the sequence does not contain a definitive feature separating them."
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
  "benchmark_sequence_length": 405,
  "benchmark_sequence_sha256": "8a56cfb606e4fe50f8190fb2e20628feacd1ddf83ddaf17985ab255c0e083848",
  "current_entry_audit": {
    "entryVersion": 133,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 405,
  "current_source_sequence_sha256": "8a56cfb606e4fe50f8190fb2e20628feacd1ddf83ddaf17985ab255c0e083848",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 131,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8H305",
  "selected_historical_entry_version": 131,
  "selected_historical_record_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "selected_historical_source_sequence_length": 405,
  "selected_historical_source_sequence_sha256": "8a56cfb606e4fe50f8190fb2e20628feacd1ddf83ddaf17985ab255c0e083848",
  "selected_historical_version": {
    "accession": "Q8H305",
    "database": "Swiss-Prot",
    "entryVersion": 131,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PKS10_ORYSJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8H305\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":133,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"Liliopsida\",\"Poales\",\"Poaceae\",\"BOP clade\",\"Oryzoideae\",\"Oryzeae\",\"Oryzinae\",\"Oryza\",\"Oryza sativa\"],\"scientificName\":\"Oryza sativa subsp. japonica\",\"taxonId\":39947}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28783252\",\"source\":\"PubMed\"}],\"value\":\"Type III polyketide synthase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28783252\",\"source\":\"PubMed\"}],\"value\":\"OsPKS2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28783252\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27878652\",\"source\":\"PubMed\"}],\"value\":\"Type III polyketide synthase 10\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27878652\",\"source\":\"PubMed\"}],\"value\":\"OsPKS10\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29411094\",\"source\":\"PubMed\"}],\"id\":\"SL-0095\",\"value\":\"Endoplasmic reticulum\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"29411094\",\"source\":\"PubMed\"}],\"id\":\"GO:0005783\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:endoplasmic reticulum\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhu X.\",\"Yu J.\",\"Shi J.\",\"Tohge T.\",\"Fernie A.R.\",\"Meir S.\",\"Aharoni A.\",\"Xu D.\",\"Zhang D.\",\"Liang W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28783252\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.12574\"}],\"citationType\":\"journal article\",\"firstPage\":\"612\",\"id\":\"28783252\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"628\",\"publicationDate\":\"2017\",\"title\":\"The polyketide synthase OsPKS2 is essential for pollen exine and Ubisch body patterning in rice.\",\"volume\":\"59\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Hu L.\",\"He H.\",\"Zhu C.\",\"Peng X.\",\"Fu J.\",\"He X.\",\"Chen X.\",\"Ouyang L.\",\"Bian J.\",\"Liu S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27878652\"},{\"database\":\"DOI\",\"id\":\"10.1007/s10265-016-0871-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"95\",\"id\":\"27878652\",\"journal\":\"J. Plant Res.\",\"lastPage\":\"105\",\"publicationDate\":\"2017\",\"title\":\"Genome-wide identification and phylogenetic analysis of the chalcone synthase gene family in rice.\",\"volume\":\"130\"},\"referenceNumber\":5,\"referencePositions\":[\"GENE FAMILY\",\"NOMENCLATURE\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8H305.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Zou T.\",\"Liu M.\",\"Xiao Q.\",\"Wang T.\",\"Chen D.\",\"Luo T.\",\"Yuan G.\",\"Li Q.\",\"Zhu J.\",\"Liang Y.\",\"Deng Q.\",\"Wang S.\",\"Zheng A.\",\"Wang L.\",\"Li P.\",\"Li S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29411094\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00299-018-2265-x\"}],\"citationType\":\"journal article\",\"firstPage\":\"759\",\"id\":\"29411094\",\"journal\":\"Plant Cell Rep.\",\"lastPage\":\"773\",\"publicationDate\":\"2018\",\"title\":\"OsPKS2 is required for rice male fertility by participating in pollen wall formation.\",\"volume\":\"37\"},\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:31:57.631660+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "725c43792b5cff8298b1771be62e5326ec303acf22c3a36d81c4c5bf4079ff65",
  "url": "https://rest.uniprot.org/uniprotkb/Q8H305.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H1",
  "excerpt": "ID   PKS10_ORYSJ             Reviewed;         405 AA.\nAC   Q8H305; A0A5S6RAJ2; Q0D710;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 131.\nDE   RecName: Full=Type III polyketide synthase 10 {ECO:0000303|PubMed:27878652};\nDE            Short=OsPKS10 {ECO:0000303|PubMed:27878652};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:28783252};\nDE   AltName: Full=Type III polyketide synthase 2 {ECO:0000303|PubMed:28783252};\nDE            Short=OsPKS2 {ECO:0000303|PubMed:28783252};\nGN   Name=PKS10 {ECO:0000303|PubMed:27878652};\nGN   Synonyms=PKS2 {ECO:0000303|PubMed:28783252};\nGN   OrderedLocusNames=Os07g0411300 {ECO:0000312|EMBL:BAT01127.1},\nGN   LOC_Os07g22850 {ECO:0000305};\nOS   Oryza sativa subsp. japonica (Rice).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; Liliopsida; Poales; Poaceae; BOP clade;\nOC   Oryzoideae; Oryzeae; Oryzinae; Oryza; Oryza sativa.\nOX   NCBI_TaxID=39947;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=28783252; DOI=10.1111/jipb.12574;\nRA   Zhu X., Yu J., Shi J., Tohge T., Fernie A.R., Meir S., Aharoni A., Xu D.,\nRA   Zhang D., Liang W.;\nRT   \"The polyketide synthase OsPKS2 is essential for pollen exine and Ubisch\nRT   body patterning in rice.\";\nRL   J. Integr. Plant Biol. 59:612-628(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H3",
  "excerpt": "RN   [5]\nRP   GENE FAMILY, NOMENCLATURE, AND TISSUE SPECIFICITY.\nRX   PubMed=27878652; DOI=10.1007/s10265-016-0871-7;\nRA   Hu L., He H., Zhu C., Peng X., Fu J., He X., Chen X., Ouyang L., Bian J.,\nRA   Liu S.;\nRT   \"Genome-wide identification and phylogenetic analysis of the chalcone\nRT   synthase gene family in rice.\";\nRL   J. Plant Res. 130:95-105(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H4",
  "excerpt": "RN   [6]\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=29411094; DOI=10.1007/s00299-018-2265-x;\nRA   Zou T., Liu M., Xiao Q., Wang T., Chen D., Luo T., Yuan G., Li Q., Zhu J.,\nRA   Liang Y., Deng Q., Wang S., Zheng A., Wang L., Li P., Li S.;\nRT   \"OsPKS2 is required for rice male fertility by participating in pollen wall\nRT   formation.\";\nRL   Plant Cell Rep. 37:759-773(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H5",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Endoplasmic reticulum\nCC       {ECO:0000269|PubMed:29411094}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131)

```json
{
  "entry_version": 131,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0005783; C:endoplasmic reticulum; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:02.084503+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "087e3fd396545934ba1c15f147eb9357fac43fedfd73e6e5d9a9e98b77653b37",
  "url": "https://rest.uniprot.org/unisave/Q8H305?format=txt&versions=131"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005783\nname: endoplasmic reticulum\nnamespace: cellular_component\ndef: \"The irregular network of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm of many eukaryotic cells. The membranes form a complex meshwork of tubular channels, which are often expanded into slitlike cavities called cisternae. The ER takes two forms, rough (or granular), with ribosomes adhering to the outer surface, and smooth (with no ribosomes attached).\" [ISBN:0198506732]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_yeast\nsynonym: \"ER\" EXACT []\nxref: NIF_Subcellular:sao1036339110\nxref: Wikipedia:Endoplasmic_reticulum\nis_a: GO:0043231 ! intracellular membrane-bounded organelle\nrelationship: part_of GO:0005737 ! cytoplasm\nrelationship: part_of GO:0012505 ! endomembrane system\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005783",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59450-59472",
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
  "excerpt": "[Term]\nid: GO:0015629\nname: actin cytoskeleton\nnamespace: cellular_component\ndef: \"The part of the cytoskeleton (the internal framework of a cell) composed of actin and associated proteins. Includes actin cytoskeleton-associated complexes.\" [GOC:jl, ISBN:0395825172, ISBN:0815316194]\nis_a: GO:0005856 ! cytoskeleton\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015629",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 119402-119408",
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
  "excerpt": "[Term]\nid: GO:0031982\nname: vesicle\nnamespace: cellular_component\nalt_id: GO:0031988\ndef: \"Any small, fluid-filled, spherical organelle enclosed by membrane.\" [GOC:mah, GOC:pz, GOC:vesicles]\nsubset: goslim_pir\nsynonym: \"membrane-bounded vesicle\" RELATED []\nsynonym: \"membrane-enclosed vesicle\" RELATED []\nxref: NIF_Subcellular:sao221389602\nxref: Wikipedia:Vesicle_(biology)\nis_a: GO:0043227 ! membrane-bounded organelle\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031982",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 181606-181618",
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
  "excerpt": "[Term]\nid: GO:0035861\nname: site of double-strand break\nnamespace: cellular_component\ndef: \"A region of a chromosome at which a DNA double-strand break has occurred. DNA damage signaling and repair proteins accumulate at the lesion to respond to the damage and repair the DNA to form a continuous DNA helix.\" [GOC:bf, GOC:mah, GOC:vw, PMID:20096808, PMID:21035408]\nsynonym: \"DNA damage foci\" RELATED [GOC:vw]\nsynonym: \"DNA damage focus\" RELATED [GOC:mah, PMID:20096808, PMID:21035408]\nsynonym: \"ionizing radiation-induced foci\" RELATED [PMID:20096808, PMID:21035408]\nsynonym: \"IRIF\" RELATED [PMID:20096808, PMID:21035408]\nsynonym: \"site of DSB\" EXACT [PMID:21035408]\nis_a: GO:0090734 ! site of DNA damage\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035861",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 221963-221974",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
