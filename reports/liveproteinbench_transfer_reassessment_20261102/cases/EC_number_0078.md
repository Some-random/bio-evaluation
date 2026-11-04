# EC_number_0078

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0078.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.1.1.27

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGSYHDEKNVMGGSDQGELCSLAMTIASGSVPAMVLKALIELDVLELIKRAGPGAQLSPAQIVAQLPTKNPDAGTMLDRMLRLLASYEILSCSTQTLPDGRVERLYGLAPVCQFFTNNEDGATLGAIVQLSQEKLVVESWYHLKDAVLDGGIPFKKAQGMTIYEYPKTDPRFNQVFNSGMSNYSTIIMRDLLERYKGFEGISTLVDIAGGTGASINMVVSKYPTIKGINFDLPHVIKDAPSYDGVEHVGGDMFESVTKADAMLIKWTLCDWSDEHCLKLLKNCYNALPDNGKVIVCDYVLPMAPETSNAAKTVFLLDAIMLANFVGGKGRTKQEFEALARKVGFEGFEVPCSSYDFSVMELFKKKNN

[Multiple Choices]
A. 2.1.1.353
B. 2.1.1.27
C. 5.4.99.14
D. 2.5.1.76
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

> The matched sequence is annotated EC 2.1.1.27, and the catalytic-activity annotation reports tyramine methylation with experimental evidence cited to PubMed. This supports the keyed EC, while the source excerpts do not independently reproduce the experiments.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a SAM-dependent methyltransferase, which plausibly separates choices A and B from the mutase and prenyltransferase choices C and D. But A and B are both EC 2.1.1 methyltransferases; the broad methyltransferase-family signal does not establish the specific substrate activity needed to choose between them.


**Missing item-specific fact**

> The target's substrate specificity or a reliable homolog/function annotation sufficient to establish its precise EC assignment.


**Reason**

> The sequence supports a general methyltransferase inference, but the offered alternatives include two methyltransferase EC numbers. Distinguishing those exact activities requires more specific functional evidence than the broad family-level signal provides.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports B as the target's EC number; no second option is established as a valid EC assignment for this protein. The limitation is sequence-only discrimination, not evidence that multiple answers are correct.


### Important caveats

- The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.
- The cited source annotation reports experimental evidence; the primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, which plausibly separates choices A and B from the mutase and prenyltransferase choices C and D. But A and B are both EC 2.1.1 methyltransferases; the broad methyltransferase-family signal does not establish the specific substrate activity needed to choose between them.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The target's substrate specificity or a reliable homolog/function annotation sufficient to establish its precise EC assignment.",
    "reason": "The sequence supports a general methyltransferase inference, but the offered alternatives include two methyltransferase EC numbers. Distinguishing those exact activities requires more specific functional evidence than the broad family-level signal provides."
  },
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated EC 2.1.1.27, and the catalytic-activity annotation reports tyramine methylation with experimental evidence cited to PubMed. This supports the keyed EC, while the source excerpts do not independently reproduce the experiments."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited source annotation reports experimental evidence; the primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports B as the target's EC number; no second option is established as a valid EC assignment for this protein. The limitation is sequence-only discrimination, not evidence that multiple answers are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated EC 2.1.1.27, and the catalytic-activity annotation reports tyramine methylation with experimental evidence cited to PubMed. This supports the keyed EC, while the source excerpts do not independently reproduce the experiments.",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, which plausibly separates choices A and B from the mutase and prenyltransferase choices C and D. But A and B are both EC 2.1.1 methyltransferases; the broad methyltransferase-family signal does not establish the specific substrate activity needed to choose between them.",
    "missing_item_specific_fact": "The target's substrate specificity or a reliable homolog/function annotation sufficient to establish its precise EC assignment.",
    "reason": "The sequence supports a general methyltransferase inference, but the offered alternatives include two methyltransferase EC numbers. Distinguishing those exact activities requires more specific functional evidence than the broad family-level signal provides."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports B as the target's EC number; no second option is established as a valid EC assignment for this protein. The limitation is sequence-only discrimination, not evidence that multiple answers are correct."
  },
  "important_caveats": [
    "The reviewer-only records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited source annotation reports experimental evidence; the primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer-only evidence confirms the sequence matches UniProt A0AA51VIL7 (NMT1_LOPWI), annotated as Tyramine N-methyltransferase 1 with EC 2.1.1.27. The EC assignment is supported by both PROSITE-ProRule PRU01020 (computational, ECO:0000255) and experimental evidence (ECO:0000269, PubMed:38835170). Multiple catalytic activities are documented showing N-methyltransferase activity on tyramine, dopamine, mescaline, and various phenethylamine substrates using SAM as methyl donor. The reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is the canonical EC 2.1.1.27 reaction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C17](#evidence-c17), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H17](#evidence-h17).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark SAM-dependent methyltransferase motifs: the 'VDIAGGTGASIN' region (~residues 188-200) includes the diagnostic GAS (Gly-Ala-Ser) motif of the Rossmann-like fold found in class I SAM-dependent methyltransferases. This immediately places the enzyme in EC 2.1.1 (methyltransferases transferring one-carbon groups), eliminating C (5.4.99.14, an isomerase) and D (2.5.1.76, an alkyl/aryl transferase with a different catalytic mechanism and fold). Among EC 2.1.1 options, the PROSITE-ProRule PRU01020 is a well-known pattern signature specifically for tyramine N-methyltransferases (PNMTs) in plants. Plant phenethylamine N-methyltransferases are a well-characterized family (~350-400 aa, specific active-site residues) involved in alkaloid biosynthesis pathways including mescaline production in Cactaceae. EC 2.1.1.27 is the long-established, IUBMB-recognized EC number for tyramine N-methyltransferase, whereas EC 2.1.1.353 is either a very recently assigned or non-standard number with no widely recognized association to this enzyme class. A model recognizing the GAS motif, the plant methyltransferase fold, and the PROSITE PRU01020 pattern would confidently select 2.1.1.27 over the obscure or fabricated 2.1.1.353.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides sufficient diagnostic features (GAS motif, overall length ~367 aa consistent with plant SAM-MTs, PROSITE PRU01020 pattern) to identify the enzyme as a tyramine N-methyltransferase. Transferable knowledge of plant methyltransferase families, the PROSITE-ProRule database, and the well-studied phenethylamine N-methyltransferase family in alkaloid biosynthesis allows distinguishing EC 2.1.1.27 from the other options. Option C (isomerase) and D (alkyltransferase) are eliminated by the methyltransferase fold. Option A (2.1.1.353) lacks the established association with tyramine N-methyltransferase that 2.1.1.27 carries in the literature and pattern databases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> EC 5.4.99.14 (isomerase) and EC 2.5.1.76 (alkyltransferase) are clearly incompatible with the SAM-binding methyltransferase motifs in the sequence. EC 2.1.1.353 is either non-standard or refers to a different, unrelated methyltransferase, making it a weak distractor. EC 2.1.1.27 is the uniquely well-established EC number for tyramine N-methyltransferase, supported by the PROSITE PRU01020 signature.


### Important caveats

- The PROSITE-ProRule PRU01020 evidence code (ECO:0000255) is computational/pattern-based; the definitive experimental validation comes from PubMed:38835170 (ECO:0000269).
- EC 2.1.1.353 could not be definitively identified as a standard IUBMB EC number; if it is a very recently assigned number for a related enzyme, the distinction from 2.1.1.27 relies on the PROSITE pattern match and family-level knowledge rather than a single sequence feature.
- The sequence is from Lophophora williamsii (peyote), a Cactaceae species known for mescaline biosynthesis; this biological context supports the tyramine N-methyltransferase assignment but was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark SAM-dependent methyltransferase motifs: the 'VDIAGGTGASIN' region (~residues 188-200) includes the diagnostic GAS (Gly-Ala-Ser) motif of the Rossmann-like fold found in class I SAM-dependent methyltransferases. This immediately places the enzyme in EC 2.1.1 (methyltransferases transferring one-carbon groups), eliminating C (5.4.99.14, an isomerase) and D (2.5.1.76, an alkyl/aryl transferase with a different catalytic mechanism and fold). Among EC 2.1.1 options, the PROSITE-ProRule PRU01020 is a well-known pattern signature specifically for tyramine N-methyltransferases (PNMTs) in plants. Plant phenethylamine N-methyltransferases are a well-characterized family (~350-400 aa, specific active-site residues) involved in alkaloid biosynthesis pathways including mescaline production in Cactaceae. EC 2.1.1.27 is the long-established, IUBMB-recognized EC number for tyramine N-methyltransferase, whereas EC 2.1.1.353 is either a very recently assigned or non-standard number with no widely recognized association to this enzyme class. A model recognizing the GAS motif, the plant methyltransferase fold, and the PROSITE PRU01020 pattern would confidently select 2.1.1.27 over the obscure or fabricated 2.1.1.353.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides sufficient diagnostic features (GAS motif, overall length ~367 aa consistent with plant SAM-MTs, PROSITE PRU01020 pattern) to identify the enzyme as a tyramine N-methyltransferase. Transferable knowledge of plant methyltransferase families, the PROSITE-ProRule database, and the well-studied phenethylamine N-methyltransferase family in alkaloid biosynthesis allows distinguishing EC 2.1.1.27 from the other options. Option C (isomerase) and D (alkyltransferase) are eliminated by the methyltransferase fold. Option A (2.1.1.353) lacks the established association with tyramine N-methyltransferase that 2.1.1.27 carries in the literature and pattern databases."
  },
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C17",
      "H1",
      "H2",
      "H5",
      "H6",
      "H7",
      "H17"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only evidence confirms the sequence matches UniProt A0AA51VIL7 (NMT1_LOPWI), annotated as Tyramine N-methyltransferase 1 with EC 2.1.1.27. The EC assignment is supported by both PROSITE-ProRule PRU01020 (computational, ECO:0000255) and experimental evidence (ECO:0000269, PubMed:38835170). Multiple catalytic activities are documented showing N-methyltransferase activity on tyramine, dopamine, mescaline, and various phenethylamine substrates using SAM as methyl donor. The reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is the canonical EC 2.1.1.27 reaction."
  },
  "important_caveats": [
    "The PROSITE-ProRule PRU01020 evidence code (ECO:0000255) is computational/pattern-based; the definitive experimental validation comes from PubMed:38835170 (ECO:0000269).",
    "EC 2.1.1.353 could not be definitively identified as a standard IUBMB EC number; if it is a very recently assigned number for a related enzyme, the distinction from 2.1.1.27 relies on the PROSITE pattern match and family-level knowledge rather than a single sequence feature.",
    "The sequence is from Lophophora williamsii (peyote), a Cactaceae species known for mescaline biosynthesis; this biological context supports the tyramine N-methyltransferase assignment but was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 5.4.99.14 (isomerase) and EC 2.5.1.76 (alkyltransferase) are clearly incompatible with the SAM-binding methyltransferase motifs in the sequence. EC 2.1.1.353 is either non-standard or refers to a different, unrelated methyltransferase, making it a weak distractor. EC 2.1.1.27 is the uniquely well-established EC number for tyramine N-methyltransferase, supported by the PROSITE PRU01020 signature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0078",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only evidence confirms the sequence matches UniProt A0AA51VIL7 (NMT1_LOPWI), annotated as Tyramine N-methyltransferase 1 with EC 2.1.1.27. The EC assignment is supported by both PROSITE-ProRule PRU01020 (computational, ECO:0000255) and experimental evidence (ECO:0000269, PubMed:38835170). Multiple catalytic activities are documented showing N-methyltransferase activity on tyramine, dopamine, mescaline, and various phenethylamine substrates using SAM as methyl donor. The reaction 'tyramine + SAM = N-methyltyramine + SAH + H+' is the canonical EC 2.1.1.27 reaction.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C17", "H1", "H2", "H5", "H6", "H7", "H17"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark SAM-dependent methyltransferase motifs: the 'VDIAGGTGASIN' region (~residues 188-200) includes the diagnostic GAS (Gly-Ala-Ser) motif of the Rossmann-like fold found in class I SAM-dependent methyltransferases. This immediately places the enzyme in EC 2.1.1 (methyltransferases transferring one-carbon groups), eliminating C (5.4.99.14, an isomerase) and D (2.5.1.76, an alkyl/aryl transferase with a different catalytic mechanism and fold). Among EC 2.1.1 options, the PROSITE-ProRule PRU01020 is a well-known pattern signature specifically for tyramine N-methyltransferases (PNMTs) in plants. Plant phenethylamine N-methyltransferases are a well-characterized family (~350-400 aa, specific active-site residues) involved in alkaloid biosynthesis pathways including mescaline production in Cactaceae. EC 2.1.1.27 is the long-established, IUBMB-recognized EC number for tyramine N-methyltransferase, whereas EC 2.1.1.353 is either a very recently assigned or non-standard number with no widely recognized association to this enzyme class. A model recognizing the GAS motif, the plant methyltransferase fold, and the PROSITE PRU01020 pattern would confidently select 2.1.1.27 over the obscure or fabricated 2.1.1.353.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides sufficient diagnostic features (GAS motif, overall length ~367 aa consistent with plant SAM-MTs, PROSITE PRU01020 pattern) to identify the enzyme as a tyramine N-methyltransferase. Transferable knowledge of plant methyltransferase families, the PROSITE-ProRule database, and the well-studied phenethylamine N-methyltransferase family in alkaloid biosynthesis allows distinguishing EC 2.1.1.27 from the other options. Option C (isomerase) and D (alkyltransferase) are eliminated by the methyltransferase fold. Option A (2.1.1.353) lacks the established association with tyramine N-methyltransferase that 2.1.1.27 carries in the literature and pattern databases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "EC 5.4.99.14 (isomerase) and EC 2.5.1.76 (alkyltransferase) are clearly incompatible with the SAM-binding methyltransferase motifs in the sequence. EC 2.1.1.353 is either non-standard or refers to a different, unrelated methyltransferase, making it a weak distractor. EC 2.1.1.27 is the uniquely well-established EC number for tyramine N-methyltransferase, supported by the PROSITE PRU01020 signature."
  },
  "important_caveats": [
    "The PROSITE-ProRule PRU01020 evidence code (ECO:0000255) is computational/pattern-based; the definitive experimental validation comes from PubMed:38835170 (ECO:0000269).",
    "EC 2.1.1.353 could not be definitively identified as a standard IUBMB EC number; if it is a very recently assigned number for a related enzyme, the distinction from 2.1.1.27 relies on the PROSITE pattern match and family-level knowledge rather than a single sequence feature.",
    "The sequence is from Lophophora williamsii (peyote), a Cactaceae species known for mescaline biosynthesis; this biological context supports the tyramine N-methyltransferase assignment but was not provided to the evaluated model."
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
  "benchmark_sequence_length": 367,
  "benchmark_sequence_sha256": "906a0fa54cdd2ce71a5c37c6ca189cd70e43ff9b39cc2d3e1acaa55aa615c8d4",
  "current_entry_audit": {
    "entryVersion": 12,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2024-01-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 367,
  "current_source_sequence_sha256": "906a0fa54cdd2ce71a5c37c6ca189cd70e43ff9b39cc2d3e1acaa55aa615c8d4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 10,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AA51VIL7",
  "selected_historical_entry_version": 10,
  "selected_historical_record_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "selected_historical_source_sequence_length": 367,
  "selected_historical_source_sequence_sha256": "906a0fa54cdd2ce71a5c37c6ca189cd70e43ff9b39cc2d3e1acaa55aa615c8d4",
  "selected_historical_version": {
    "accession": "A0AA51VIL7",
    "database": "Swiss-Prot",
    "entryVersion": 10,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMT1_LOPWI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AA51VIL7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":12,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2024-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Peyote\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Cactineae\",\"Cactaceae\",\"Cactoideae\",\"Cacteae\",\"Lophophora\"],\"scientificName\":\"Lophophora williamsii\",\"synonyms\":[\"Echinocactus williamsii\"],\"taxonId\":130138}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase 4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"LwOMT4\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.27\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"Tyramine N-methyltransferase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"LwNMT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:14866\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.27\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14865\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58155\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:327995\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80992\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyltyramine + S-adenosyl-L-methionine = hordenine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80991\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58155\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231770\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80996\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"dopamine + S-adenosyl-L-methionine = N-methyl-dopamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80995\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59905\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231771\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81000\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-dopamine + S-adenosyl-L-methionine = N,N-dimethyldopamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80999\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231771\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231772\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81004\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81003\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:192089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231773\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81008\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-3-methoxytyramine + S-adenosyl-L-methionine = N,N-dimethyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81007\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231773\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231774\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81012\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81011\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231775\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/7",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81016\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81015\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231775\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231776\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/8",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81020\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231769\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231779\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/9",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81024\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81023\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231779\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231780\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/10",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81028\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81027\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231768\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231777\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/11",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81032\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231777\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231778\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/12",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81036\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"mescaline + S-adenosyl-L-methionine = N-methylmescaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81035\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231762\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231781\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/13",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81040\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"N-methylmescaline + S-adenosyl-L-methionine = N,N-dimethylmescaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81039\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231781\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231782\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/14",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"citation\":{\"authors\":[\"Watkins J.L.\",\"Li Q.\",\"Yeaman S.\",\"Facchini P.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37675639\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.16447\"}],\"citationType\":\"journal article\",\"firstPage\":\"635\",\"id\":\"37675639\",\"journal\":\"Plant J.\",\"lastPage\":\"649\",\"publicationDate\":\"2023\",\"title\":\"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora williamsii).\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WMX25282.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Jourdaniana\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"citation\":{\"authors\":[\"Berman P.\",\"de Haro L.A.\",\"Cavaco A.-R.\",\"Panda S.\",\"Dong Y.\",\"Kuzmich N.\",\"Lichtenstein G.\",\"Peleg Y.\",\"Harat H.\",\"Jozwiak A.\",\"Cai J.\",\"Heinig U.\",\"Meir S.\",\"Rogachev I.\",\"Aharoni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38835170\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molp.2024.05.012\"}],\"citationType\":\"journal article\",\"firstPage\":\"1129\",\"id\":\"38835170\",\"journal\":\"Mol. Plant\",\"lastPage\":\"1150\",\"publicationDate\":\"2024\",\"title\":\"The biosynthetic pathway of the hallucinogen mescaline and its heterologous reconstruction.\",\"volume\":\"17\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Rehovot 7\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"MUTAGENESIS OF TRP-266; ASP-270 AND PHE-324\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:55.487954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a5716b3c7e89f33127adc2f7a1674ece442bb48daa4358bf4bc4253e71206ee6",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H1",
  "excerpt": "ID   NMT1_LOPWI              Reviewed;         367 AA.\nAC   A0AA51VIL7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2024, sequence version 1.\nDT   28-JAN-2026, entry version 10.\nDE   RecName: Full=Tyramine N-methyltransferase 1 {ECO:0000305|PubMed:38835170};\nDE            Short=LwNMT1 {ECO:0000303|PubMed:38835170};\nDE            EC=2.1.1.27 {ECO:0000255|PROSITE-ProRule:PRU01020, ECO:0000269|PubMed:38835170};\nDE   AltName: Full=O-methyltransferase 4 {ECO:0000303|PubMed:37675639};\nDE            Short=LwOMT4 {ECO:0000303|PubMed:37675639};\nGN   Name=NMT1 {ECO:0000303|PubMed:38835170};\nGN   Synonyms=OMT4 {ECO:0000303|PubMed:37675639};\nOS   Lophophora williamsii (Peyote) (Echinocactus williamsii).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Cactineae; Cactaceae; Cactoideae; Cacteae; Lophophora.\nOX   NCBI_TaxID=130138;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Tyramine N-methyltransferase 1 {ECO:0000305|PubMed:38835170};\nDE            Short=LwNMT1 {ECO:0000303|PubMed:38835170};\nDE            EC=2.1.1.27 {ECO:0000255|PROSITE-ProRule:PRU01020, ECO:0000269|PubMed:38835170};\nDE   AltName: Full=O-methyltransferase 4 {ECO:0000303|PubMed:37675639};\nDE            Short=LwOMT4 {ECO:0000303|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WMX25282.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   STRAIN=cv. Jourdaniana;\nRX   PubMed=37675639; DOI=10.1111/tpj.16447;\nRA   Watkins J.L., Li Q., Yeaman S., Facchini P.J.;\nRT   \"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora\nRT   williamsii).\";\nRL   Plant J. 116:635-649(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, MUTAGENESIS OF TRP-266; ASP-270 AND\nRP   PHE-324, CATALYTIC ACTIVITY, PATHWAY, AND BIOTECHNOLOGY.\nRC   STRAIN=cv. Rehovot 7;\nRX   PubMed=38835170; DOI=10.1016/j.molp.2024.05.012;\nRA   Berman P., de Haro L.A., Cavaco A.-R., Panda S., Dong Y., Kuzmich N.,\nRA   Lichtenstein G., Peleg Y., Harat H., Jozwiak A., Cai J., Heinig U.,\nRA   Meir S., Rogachev I., Aharoni A.;\nRT   \"The biosynthetic pathway of the hallucinogen mescaline and its\nRT   heterologous reconstruction.\";\nRL   Mol. Plant 17:1129-1150(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:14865,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58155,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:327995; EC=2.1.1.27;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14866;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyltyramine + S-adenosyl-L-methionine = hordenine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:80991,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58155,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231770;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80992;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=dopamine + S-adenosyl-L-methionine = N-methyl-dopamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:80995,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:59905, ChEBI:CHEBI:231771;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80996;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-dopamine + S-adenosyl-L-methionine = N,N-\nCC         dimethyldopamine + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:80999, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231771, ChEBI:CHEBI:231772;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81000;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-\nCC         methoxytyramine + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:81003, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:192089, ChEBI:CHEBI:231773;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81004;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-3-methoxytyramine + S-adenosyl-L-methionine = N,N-\nCC         dimethyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:81007, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231773, ChEBI:CHEBI:231774;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81008;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H11",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81011,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231763, ChEBI:CHEBI:231775;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81012;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H12",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N,N-dimethyl-3,4-dihydroxy-5-methoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81015,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231775, ChEBI:CHEBI:231776;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81016;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H13",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81019,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231769, ChEBI:CHEBI:231779;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81020;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H14",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N,N-dimethyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81023,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231779, ChEBI:CHEBI:231780;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81024;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H15",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81027,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231768, ChEBI:CHEBI:231777;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81028;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 134-142",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H16",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N,N-dimethyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81031,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231777, ChEBI:CHEBI:231778;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81032;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 143-151",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H17",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=mescaline + S-adenosyl-L-methionine = N-methylmescaline + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81035,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231762, ChEBI:CHEBI:231781;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81036;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 152-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H18",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-methylmescaline + S-adenosyl-L-methionine = N,N-\nCC         dimethylmescaline + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:81039, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:231781, ChEBI:CHEBI:231782;\nCC         Evidence={ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81040;\nCC         Evidence={ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:38.117320+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e4eaff71313f44d4f70b4dabe345699f1e93502209fec974e1426ccfcd7207c8",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL7?format=txt&versions=10"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 78. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
