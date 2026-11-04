# GO_molecular_function_0029

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0029.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — folic acid transmembrane transporter activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEDDDFSIKDKKENYETCSTETISSYISINEKCQLIEKDINDDNHENPYMIFNKISSSLIAMLQGVEVLCNLSIIYLLKDNYHLHPASLSIVMCFIKIPWSIKLVWAVISDNYPIFGYRRKYYLLLGSFLCILSLICLGLITHNNLFITILLLFIYFFGSSLCNVIGEAQVVESNRNCSINSSARNVSLFFAFRKLSFAIMSYLSGYLLLLISKKHIFLIGSFLPICVFTSGFFIIEKRNYTKSSIKDQIKCIYSIIKLSYLKNFIIFIFIMMSTPSCGNTLFFYITNELKFSPNLLGKMAMFQSLASFISIISYMLFFTKIDIRKLLLYSTIIITPFCLLPLVVIKKVNYFLFIPNTLFFITDTVLIEFIAEFQTMPILVLCSRLIPEGFESTIYSLLLSSNNFASIISSFLSSLLTYSLNITSTNFTNLPYMIIICCLTNIIPIFFLYILPNHSQKKNLQHSNSHTQKYYSYPSTDYISSQKSDSSEITKFSADMQIDDITLE

[Multiple Choices]
A. folic acid transmembrane transporter activity
B. beta-glucuronidase activity
C. NAD binding
D. calcium-dependent phospholipid binding
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

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt entry describes folate transport and cites experimental evidence for that function; it also assigns the exact GO term in option A with IDA evidence. This supports the keyed answer, though the primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains many long hydrophobic stretches, strongly suggesting a multipass membrane protein. That is consistent with a transmembrane transporter and unlike the soluble enzyme implied by beta-glucuronidase activity, the usual cofactor-binding role implied by NAD binding, or calcium-dependent phospholipid binding. Given these particular alternatives, folic acid transmembrane transporter activity is the meaningful fit.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence supports a membrane-transporter inference that distinguishes A from the offered alternatives. It does not by itself establish folate as the transported substrate, so the substrate-specific conclusion is probabilistic rather than independently proven from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the sequence alone gives limited evidence for substrate specificity, the offered alternatives do not present another plausible multipass membrane-transporter function.


### Important caveats

- Reviewer-only evidence supports the exact folate transport annotation but was not available as an original input.
- The sequence-based distinction supports A among these choices; it should not be taken as a precise independent determination of substrate specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains many long hydrophobic stretches, strongly suggesting a multipass membrane protein. That is consistent with a transmembrane transporter and unlike the soluble enzyme implied by beta-glucuronidase activity, the usual cofactor-binding role implied by NAD binding, or calcium-dependent phospholipid binding. Given these particular alternatives, folic acid transmembrane transporter activity is the meaningful fit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports a membrane-transporter inference that distinguishes A from the offered alternatives. It does not by itself establish folate as the transported substrate, so the substrate-specific conclusion is probabilistic rather than independently proven from the sequence."
  },
  "case_id": "GO_molecular_function_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry describes folate transport and cites experimental evidence for that function; it also assigns the exact GO term in option A with IDA evidence. This supports the keyed answer, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the exact folate transport annotation but was not available as an original input.",
    "The sequence-based distinction supports A among these choices; it should not be taken as a precise independent determination of substrate specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the sequence alone gives limited evidence for substrate specificity, the offered alternatives do not present another plausible multipass membrane-transporter function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry describes folate transport and cites experimental evidence for that function; it also assigns the exact GO term in option A with IDA evidence. This supports the keyed answer, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains many long hydrophobic stretches, strongly suggesting a multipass membrane protein. That is consistent with a transmembrane transporter and unlike the soluble enzyme implied by beta-glucuronidase activity, the usual cofactor-binding role implied by NAD binding, or calcium-dependent phospholipid binding. Given these particular alternatives, folic acid transmembrane transporter activity is the meaningful fit.",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports a membrane-transporter inference that distinguishes A from the offered alternatives. It does not by itself establish folate as the transported substrate, so the substrate-specific conclusion is probabilistic rather than independently proven from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the sequence alone gives limited evidence for substrate specificity, the offered alternatives do not present another plausible multipass membrane-transporter function."
  },
  "important_caveats": [
    "Reviewer-only evidence supports the exact folate transport annotation but was not available as an original input.",
    "The sequence-based distinction supports A among these choices; it should not be taken as a precise independent determination of substrate specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IBB7 (Folate transporter 1, PfFT1, Plasmodium falciparum 3D7) is annotated with GO:0008517 (folic acid transmembrane transporter activity) with IDA evidence from PubMed:21998306 (Salcedo-Sora et al., JBC 2011), an experimental transporter characterization study. The catalytic activity reaction 'folate(in) + H+(in) = folate(out) + H+(out)' is also recorded. The sequence in the question matches the canonical 505-aa entry exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 505-aa sequence displays a clear polytopic membrane transporter architecture with approximately 10-12 long hydrophobic segments (stretches rich in L, I, V, F, Y, C) separated by short polar/charged loops, characteristic of the SLC (Solute Carrier) superfamily. Among the four options, only option A describes a transmembrane transporter activity. Option B (beta-glucuronidase, EC 3.2.1.31) is a soluble glycosidase with a specific catalytic domain and no polytopic TM architecture. Option C (NAD binding) is associated with Rossmann-fold proteins (dehydrogenases, oxidoreductases) that are typically soluble and contain the GxGxxG motif, absent here. Option D (calcium-dependent phospholipid binding) requires a C2 domain (~130 aa calcium-binding loops), incompatible with a 12-TM membrane protein. The polytopic TM architecture alone eliminates B, C, and D and uniquely supports A. Additionally, the ~500 aa length and ~12 TM topology match the well-characterized SLC19 folate transporter family architecture known from human and bacterial homologs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the polytopic membrane transporter architecture from the hydrophobic segment pattern and eliminate the three non-transporter options using general structural biology knowledge: beta-glucuronidases are soluble enzymes, NAD-binding proteins have Rossmann folds and are soluble, and C2-domain proteins are small calcium-binding modules. The SLC superfamily's 12-TM, ~500 aa architecture is a well-known family-level pattern. This meaningfully distinguishes option A from the others without needing the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The polytopic TM architecture unambiguously points to a transmembrane transporter function. The other three options (soluble enzyme, nucleotide-binding protein, calcium-binding domain protein) are structurally incompatible with the observed sequence architecture. No ambiguity exists among the offered choices.


### Important caveats

- The specific substrate (folic acid) is not directly identifiable from sequence architecture alone; however, since only one transporter option is offered, the question tests recognition of transporter architecture versus non-transporter functions.
- The UniProt annotation is from Plasmodium falciparum, but organism identity was not provided to the model; the answer relies on structural architecture recognition rather than organism-specific knowledge.
- The experimental evidence (PubMed:21998306) confirms the folate transporter function, but the sequence-based reasoning path (polytopic TM → transporter) is sufficient to select A among the given alternatives.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 505-aa sequence displays a clear polytopic membrane transporter architecture with approximately 10-12 long hydrophobic segments (stretches rich in L, I, V, F, Y, C) separated by short polar/charged loops, characteristic of the SLC (Solute Carrier) superfamily. Among the four options, only option A describes a transmembrane transporter activity. Option B (beta-glucuronidase, EC 3.2.1.31) is a soluble glycosidase with a specific catalytic domain and no polytopic TM architecture. Option C (NAD binding) is associated with Rossmann-fold proteins (dehydrogenases, oxidoreductases) that are typically soluble and contain the GxGxxG motif, absent here. Option D (calcium-dependent phospholipid binding) requires a C2 domain (~130 aa calcium-binding loops), incompatible with a 12-TM membrane protein. The polytopic TM architecture alone eliminates B, C, and D and uniquely supports A. Additionally, the ~500 aa length and ~12 TM topology match the well-characterized SLC19 folate transporter family architecture known from human and bacterial homologs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the polytopic membrane transporter architecture from the hydrophobic segment pattern and eliminate the three non-transporter options using general structural biology knowledge: beta-glucuronidases are soluble enzymes, NAD-binding proteins have Rossmann folds and are soluble, and C2-domain proteins are small calcium-binding modules. The SLC superfamily's 12-TM, ~500 aa architecture is a well-known family-level pattern. This meaningfully distinguishes option A from the others without needing the specific UniProt annotation for this exact protein."
  },
  "case_id": "GO_molecular_function_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H1",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IBB7 (Folate transporter 1, PfFT1, Plasmodium falciparum 3D7) is annotated with GO:0008517 (folic acid transmembrane transporter activity) with IDA evidence from PubMed:21998306 (Salcedo-Sora et al., JBC 2011), an experimental transporter characterization study. The catalytic activity reaction 'folate(in) + H+(in) = folate(out) + H+(out)' is also recorded. The sequence in the question matches the canonical 505-aa entry exactly."
  },
  "important_caveats": [
    "The specific substrate (folic acid) is not directly identifiable from sequence architecture alone; however, since only one transporter option is offered, the question tests recognition of transporter architecture versus non-transporter functions.",
    "The UniProt annotation is from Plasmodium falciparum, but organism identity was not provided to the model; the answer relies on structural architecture recognition rather than organism-specific knowledge.",
    "The experimental evidence (PubMed:21998306) confirms the folate transporter function, but the sequence-based reasoning path (polytopic TM → transporter) is sufficient to select A among the given alternatives."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The polytopic TM architecture unambiguously points to a transmembrane transporter function. The other three options (soluble enzyme, nucleotide-binding protein, calcium-binding domain protein) are structurally incompatible with the observed sequence architecture. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IBB7 (Folate transporter 1, PfFT1, Plasmodium falciparum 3D7) is annotated with GO:0008517 (folic acid transmembrane transporter activity) with IDA evidence from PubMed:21998306 (Salcedo-Sora et al., JBC 2011), an experimental transporter characterization study. The catalytic activity reaction 'folate(in) + H+(in) = folate(out) + H+(out)' is also recorded. The sequence in the question matches the canonical 505-aa entry exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H1", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 505-aa sequence displays a clear polytopic membrane transporter architecture with approximately 10-12 long hydrophobic segments (stretches rich in L, I, V, F, Y, C) separated by short polar/charged loops, characteristic of the SLC (Solute Carrier) superfamily. Among the four options, only option A describes a transmembrane transporter activity. Option B (beta-glucuronidase, EC 3.2.1.31) is a soluble glycosidase with a specific catalytic domain and no polytopic TM architecture. Option C (NAD binding) is associated with Rossmann-fold proteins (dehydrogenases, oxidoreductases) that are typically soluble and contain the GxGxxG motif, absent here. Option D (calcium-dependent phospholipid binding) requires a C2 domain (~130 aa calcium-binding loops), incompatible with a 12-TM membrane protein. The polytopic TM architecture alone eliminates B, C, and D and uniquely supports A. Additionally, the ~500 aa length and ~12 TM topology match the well-characterized SLC19 folate transporter family architecture known from human and bacterial homologs.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the polytopic membrane transporter architecture from the hydrophobic segment pattern and eliminate the three non-transporter options using general structural biology knowledge: beta-glucuronidases are soluble enzymes, NAD-binding proteins have Rossmann folds and are soluble, and C2-domain proteins are small calcium-binding modules. The SLC superfamily's 12-TM, ~500 aa architecture is a well-known family-level pattern. This meaningfully distinguishes option A from the others without needing the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The polytopic TM architecture unambiguously points to a transmembrane transporter function. The other three options (soluble enzyme, nucleotide-binding protein, calcium-binding domain protein) are structurally incompatible with the observed sequence architecture. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The specific substrate (folic acid) is not directly identifiable from sequence architecture alone; however, since only one transporter option is offered, the question tests recognition of transporter architecture versus non-transporter functions.",
    "The UniProt annotation is from Plasmodium falciparum, but organism identity was not provided to the model; the answer relies on structural architecture recognition rather than organism-specific knowledge.",
    "The experimental evidence (PubMed:21998306) confirms the folate transporter function, but the sequence-based reasoning path (polytopic TM → transporter) is sufficient to select A among the given alternatives."
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
  "benchmark_sequence_length": 505,
  "benchmark_sequence_sha256": "c119806f4af8df36d96a0b3132aa84ccec0f7513a38b42c3ceb1495fb192ffc3",
  "current_entry_audit": {
    "entryVersion": 100,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 505,
  "current_source_sequence_sha256": "c119806f4af8df36d96a0b3132aa84ccec0f7513a38b42c3ceb1495fb192ffc3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 98,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IBB7",
  "selected_historical_entry_version": 98,
  "selected_historical_record_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "selected_historical_source_sequence_length": 505,
  "selected_historical_source_sequence_sha256": "c119806f4af8df36d96a0b3132aa84ccec0f7513a38b42c3ceb1495fb192ffc3",
  "selected_historical_version": {
    "accession": "Q8IBB7",
    "database": "Swiss-Prot",
    "entryVersion": 98,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FT1_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IBB7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":100,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"Folate transporter 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"PfFT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"value\":\"Folate transporter with broad substrate specificity (PubMed:21998306). Transports folic acid, folinic acid, pteroic acid, dihydropteroic acid, the folate precursor p-amino benzoic acid (pABA) and the human folate catabolite pABA monoglutamate (PubMed:21998306)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"name\":\"folate(in) + H(+)(in) = folate(out) + H(+)(out)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:70159\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:62501\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"21998306\",\"source\":\"PubMed\"}],\"id\":\"GO:0008517\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:folic acid transmembrane transporter activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/17",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBB7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Salcedo-Sora J.E.\",\"Ochong E.\",\"Beveridge S.\",\"Johnson D.\",\"Nzila A.\",\"Biagini G.A.\",\"Stocks P.A.\",\"O'Neill P.M.\",\"Krishna S.\",\"Bray P.G.\",\"Ward S.A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21998306\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m111.286054\"}],\"citationType\":\"journal article\",\"firstPage\":\"44659\",\"id\":\"21998306\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"44668\",\"publicationDate\":\"2011\",\"title\":\"The molecular basis of folate salvage in Plasmodium falciparum: characterization of two folate transporters.\",\"volume\":\"286\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"TRANSPORTER ACTIVITY\",\"ACTIVITY REGULATION\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:06.455529+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f181b4dbb2ac2ea55eb60db5ac65720a1ffcd9dd3096b131edc4a79c0f2331cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBB7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H1",
  "excerpt": "ID   FT1_PLAF7               Reviewed;         505 AA.\nAC   Q8IBB7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 98.\nDE   RecName: Full=Folate transporter 1 {ECO:0000303|PubMed:21998306};\nDE            Short=PfFT1 {ECO:0000303|PubMed:21998306};\nGN   ORFNames=PF3D7_0828600 {ECO:0000312|EMBL:CAD51089.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, TRANSPORTER ACTIVITY, ACTIVITY REGULATION, AND SUBCELLULAR\nRP   LOCATION.\nRX   PubMed=21998306; DOI=10.1074/jbc.m111.286054;\nRA   Salcedo-Sora J.E., Ochong E., Beveridge S., Johnson D., Nzila A.,\nRA   Biagini G.A., Stocks P.A., O'Neill P.M., Krishna S., Bray P.G., Ward S.A.;\nRT   \"The molecular basis of folate salvage in Plasmodium falciparum:\nRT   characterization of two folate transporters.\";\nRL   J. Biol. Chem. 286:44659-44668(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Folate transporter with broad substrate specificity\nCC       (PubMed:21998306). Transports folic acid, folinic acid, pteroic acid,\nCC       dihydropteroic acid, the folate precursor p-amino benzoic acid (pABA)\nCC       and the human folate catabolite pABA monoglutamate (PubMed:21998306).\nCC       {ECO:0000269|PubMed:21998306}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=folate(in) + H(+)(in) = folate(out) + H(+)(out);\nCC         Xref=Rhea:RHEA:70159, ChEBI:CHEBI:15378, ChEBI:CHEBI:62501;\nCC         Evidence={ECO:0000305|PubMed:21998306};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98)

```json
{
  "entry_version": 98,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0008517; F:folic acid transmembrane transporter activity; IDA:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.640562+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "23128f941b579a9921cbe78a9e91da7734842a0f3c2311d1bf182aed647224f0",
  "url": "https://rest.uniprot.org/unisave/Q8IBB7?format=txt&versions=98"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004566\nname: beta-glucuronidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a beta-D-glucuronoside + H2O = an alcohol + D-glucuronate.\" [EC:3.2.1.31]\nsynonym: \"beta-D-glucuronoside glucuronosohydrolase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"beta-glucuronide glucuronohydrolase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"exo-beta-D-glucuronidase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"glucuronidase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"ketodase activity\" RELATED [EC:3.2.1.31]\nxref: EC:3.2.1.31\nxref: MetaCyc:BETA-GLUCURONID-RXN\nxref: Reactome:R-HSA-1678854 \"GUSB tetramer hydrolyses CS/HS precursor\"\nxref: Reactome:R-HSA-2162226 \"GUSB tetramer hydrolyzes GlcA-1,3-GlcNAc\"\nxref: Reactome:R-HSA-2162227 \"GUSB tetramer hydrolyses (HA)2\"\nxref: Reactome:R-HSA-2318373 \"Defective GUSB does not hydrolyse (HA)2\"\nxref: Reactome:R-HSA-9036068 \"Defective GUSB does not hydrolyse GlcA-1,3-GlcNAc\"\nxref: Reactome:R-HSA-9036070 \"Defective GUSB does not hydrolyse CS/HS precursor\"\nxref: RHEA:17633\nxref: RHEA:28326\nxref: RHEA:30475\nxref: RHEA:76111\nis_a: GO:0046574 ! glucuronidase activity\nproperty_value: skos:exactMatch EC:3.2.1.31\nproperty_value: skos:exactMatch RHEA:17633\nproperty_value: skos:narrowMatch RHEA:28326\nproperty_value: skos:narrowMatch RHEA:30475\nproperty_value: skos:narrowMatch RHEA:76111\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004566",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 44488-44516",
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
  "excerpt": "[Term]\nid: GO:0005544\nname: calcium-dependent phospholipid binding\nnamespace: molecular_function\ndef: \"Binding to a phospholipid, a class of lipids containing phosphoric acid as a mono- or diester, in the presence of calcium.\" [GOC:jl]\nis_a: GO:0005543 ! phospholipid binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005544",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 57197-57203",
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
  "excerpt": "[Term]\nid: GO:0008517\nname: folic acid transmembrane transporter activity\nnamespace: molecular_function\ndef: \"Enables the transfer of folic acid (pteroylglutamic acid) from one side of a membrane to the other. Folic acid is widely distributed as a member of the vitamin B complex and is essential for the synthesis of purine and pyrimidines.\" [GOC:ai]\nsynonym: \"folate transmembrane transporter activity\" EXACT []\nsynonym: \"folate transporter activity\" EXACT []\nsynonym: \"folic acid transporter activity\" RELATED []\nsynonym: \"vitamin B9 transporter activity\" EXACT []\nsynonym: \"vitamin M transporter activity\" EXACT []\nxref: Reactome:R-HSA-200652 \"SLC19A1 transports 5-methyl-THF from extracellular region to cytosol\"\nxref: Reactome:R-HSA-200680 \"SLC25A32 transports THF from cytosol to mitochondrial matrix\"\nxref: Reactome:R-HSA-200720 \"SLC25A32 transports THF from mitochondrial matrix to cytosol\"\nis_a: GO:0005310 ! dicarboxylic acid transmembrane transporter activity\nis_a: GO:0072349 ! modified amino acid transmembrane transporter activity\nis_a: GO:0090482 ! vitamin transmembrane transporter activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008517",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 84461-84477",
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
  "excerpt": "[Term]\nid: GO:0051287\nname: NAD binding\nnamespace: molecular_function\nalt_id: GO:0051288\ndef: \"Binding to nicotinamide adenine dinucleotide, a coenzyme involved in many redox and biosynthetic reactions; binding may be to either the oxidized form, NAD+, or the reduced form, NADH.\" [GOC:ai]\nsubset: goslim_chembl\nsynonym: \"NAD or NADH binding\" RELATED [GOC:mah]\nsynonym: \"NAD+ or NADH binding\" RELATED []\nsynonym: \"nicotinamide adenine dinucleotide binding\" EXACT []\nis_a: GO:0030554 ! adenyl nucleotide binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051287",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 325123-325134",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 29. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
