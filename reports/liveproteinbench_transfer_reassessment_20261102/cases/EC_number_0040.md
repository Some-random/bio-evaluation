# EC_number_0040

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0040.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.8.1.7

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKFLQIIKHLKLQNKKNALDNFVNCRTYEHISNINKLFLNNFSSTKEHSEHGQVKHENFLNSTLKYEENSQNGSTNNLKNGKYNMYVSEGNVNINEEKYKDNNISSNNTQYNNNSSNSGSLNDEGPLWKEHIDDVVNENKKKKMNRFYLDSQATTMIDPRVLDKMLPYMTYIYGNAHSRNHFFGWESEKAVEDARTNLLNLINGKNNKEIIFTSGATESNNLALIGICTYYNKLNKQKNHIITSQIEHKCILQTCRFLQTKGFEVTYLKPDTNGLVKLDDIKNSIKDNTIMASFIFVNNEIGVIQDIENIGNLCKEKNILFHTDASQAAGKVPIDVQKMNIDLMSMSGHKLYGPKGIGALYIKRKKPNIRLNALIHGGGQERGLRSGTLPTHLIVGFGEAAKVCSLEMNRDEKKVRYFFNYVKDYLTKHLDYIVFNGCQINRYYGNMNISFLFVEGESLLMSLNEIALSSGSACTSSTLEPSYVLRSIGISEDIAHTSIRIGFNRFTTFFEVQQLCINLVKSVERLRSISPLYEMELEKKNPSNDDIPKFIWT

[Multiple Choices]
A. 2.8.1.11
B. 2.8.1.7
C. 3.2.1.20
D. 2.4.1.391
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

> The sequence-matched UniProt annotation identifies the protein as cysteine desulfurase IscS and assigns EC 2.8.1.7. The catalytic-activity annotation gives the corresponding sulfur-transfer reaction and cites experimental evidence (ECO:0000269); thus choice B is supported, not merely computationally inferred.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conserved enzyme-sized core following a low-complexity N-terminal region, with features consistent with the NifS/IscS family of PLP-dependent cysteine desulfurases, including its conserved catalytic cysteine region. Transferable knowledge of this family links it to sulfur mobilization from cysteine (EC 2.8.1.7), distinguishing B from the glycosidase and glycosyltransferase choices and from the other sulfurtransferase option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition from the sequence provides a meaningful basis for selecting the cysteine-desulfurase EC option. It is a probabilistic inference from conserved sequence and family-function regularities, rather than reliance on the exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level inference points specifically to the cysteine-desulfurase option among those offered.


### Important caveats

- The reviewer-only source identifies the exact protein and records experimental support, but those target-specific annotations were not part of the original input.
- The cited experimental evidence is represented here through the curated annotation; the primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conserved enzyme-sized core following a low-complexity N-terminal region, with features consistent with the NifS/IscS family of PLP-dependent cysteine desulfurases, including its conserved catalytic cysteine region. Transferable knowledge of this family links it to sulfur mobilization from cysteine (EC 2.8.1.7), distinguishing B from the glycosidase and glycosyltransferase choices and from the other sulfurtransferase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition from the sequence provides a meaningful basis for selecting the cysteine-desulfurase EC option. It is a probabilistic inference from conserved sequence and family-function regularities, rather than reliance on the exact protein's database entry."
  },
  "case_id": "EC_number_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as cysteine desulfurase IscS and assigns EC 2.8.1.7. The catalytic-activity annotation gives the corresponding sulfur-transfer reaction and cites experimental evidence (ECO:0000269); thus choice B is supported, not merely computationally inferred."
  },
  "important_caveats": [
    "The reviewer-only source identifies the exact protein and records experimental support, but those target-specific annotations were not part of the original input.",
    "The cited experimental evidence is represented here through the curated annotation; the primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference points specifically to the cysteine-desulfurase option among those offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as cysteine desulfurase IscS and assigns EC 2.8.1.7. The catalytic-activity annotation gives the corresponding sulfur-transfer reaction and cites experimental evidence (ECO:0000269); thus choice B is supported, not merely computationally inferred.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conserved enzyme-sized core following a low-complexity N-terminal region, with features consistent with the NifS/IscS family of PLP-dependent cysteine desulfurases, including its conserved catalytic cysteine region. Transferable knowledge of this family links it to sulfur mobilization from cysteine (EC 2.8.1.7), distinguishing B from the glycosidase and glycosyltransferase choices and from the other sulfurtransferase option.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition from the sequence provides a meaningful basis for selecting the cysteine-desulfurase EC option. It is a probabilistic inference from conserved sequence and family-function regularities, rather than reliance on the exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference points specifically to the cysteine-desulfurase option among those offered."
  },
  "important_caveats": [
    "The reviewer-only source identifies the exact protein and records experimental support, but those target-specific annotations were not part of the original input.",
    "The cited experimental evidence is represented here through the curated annotation; the primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IBI5 (ISCS_PLAF7, 553 aa, sequence matched) is annotated as Cysteine desulfurase IscS with EC 2.8.1.7, supported by experimental evidence (ECO:0000269, PubMed:34032321, Sadik et al. 2021 Mol Microbiol). The catalytic reaction (sulfur carrier)-H + L-cysteine = (sulfur carrier)-SH + L-alanine is confirmed. The expected answer B (2.8.1.7) is experimentally validated.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish EC 2.8.1.7 from the other three options using transferable enzyme-family knowledge. (1) EC 3.2.1.20 (alpha-galactosidase) and EC 2.4.1.391 (glycosyltransferase) belong to entirely different enzyme classes with characteristic glycosidase/glycosyltransferase folds and motifs (e.g., GT-B fold, conserved Asp/Glu catalytic residues, beta-propeller or TIM-barrel glycosidase architectures) that are absent from this sequence. (2) EC 2.8.1.11 (lipoate synthase) is a radical SAM enzyme (~350 aa) with a hallmark CxxxCxxC cluster motif; this 553-aa sequence lacks any radical SAM motif and is too large. (3) The remaining candidate EC 2.8.1.7 (cysteine desulfurase IscS/NifS) is a PLP-dependent enzyme of the class I aminotransferase fold, one of the most ubiquitous and well-characterized enzyme families. The sequence length (~553 aa, consistent with eukaryotic IscS with an N-terminal mitochondrial targeting extension), the presence of a potential PLP-binding lysine in a 'GKGIGALYIKRKK'-type region, and a catalytic cysteine in a 'GSACTSST'-type motif in the C-terminal half are consistent with IscS/NifS family architecture learned from bacterial and other eukaryotic homologs. The AT-rich composition is a general Plasmodium feature but does not obscure the family-level fold signatures. Thus, family-level recognition of the NifS/IscS clan and elimination of the other three structurally and mechanistically unrelated classes provides a credible, transferable path to EC 2.8.1.7.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The discrimination relies on well-established family-level knowledge: the NifS/IscS clan is one of the most studied enzyme families, and the three distractors (radical SAM lipoate synthase, glycosidase, glycosyltransferase) are mechanistically and structurally distinct enough that their absence can be inferred from the sequence's overall architecture, length, and absence of their signature motifs. No fact specific to this exact Plasmodium protein beyond its amino acid sequence is required to make the distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (2.8 sulfurtransferases, 3.2 glycosidases, 2.4 glycosyltransferases) and within 2.8, two very different sub-families (PLP-dependent cysteine desulfurase vs. radical SAM lipoate synthase). The sequence features clearly exclude C and D, and the size and absence of radical SAM motifs exclude A. Only B remains as a defensible choice.


### Important caveats

- The AT-rich composition of Plasmodium falciparum proteins can reduce sequence-similarity-based recognition; however, the structural/fold-level reasoning and elimination of the three mechanistically unrelated distractors remain robust.
- The reviewer evidence confirms experimental validation (ECO:0000269) of EC 2.8.1.7 for this protein, but this annotation was not available to the evaluated model.
- The N-terminal ~50-60 residues likely constitute a mitochondrial targeting sequence, which is common for eukaryotic IscS and accounts for the slightly longer length compared to bacterial homologs (~420 aa).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish EC 2.8.1.7 from the other three options using transferable enzyme-family knowledge. (1) EC 3.2.1.20 (alpha-galactosidase) and EC 2.4.1.391 (glycosyltransferase) belong to entirely different enzyme classes with characteristic glycosidase/glycosyltransferase folds and motifs (e.g., GT-B fold, conserved Asp/Glu catalytic residues, beta-propeller or TIM-barrel glycosidase architectures) that are absent from this sequence. (2) EC 2.8.1.11 (lipoate synthase) is a radical SAM enzyme (~350 aa) with a hallmark CxxxCxxC cluster motif; this 553-aa sequence lacks any radical SAM motif and is too large. (3) The remaining candidate EC 2.8.1.7 (cysteine desulfurase IscS/NifS) is a PLP-dependent enzyme of the class I aminotransferase fold, one of the most ubiquitous and well-characterized enzyme families. The sequence length (~553 aa, consistent with eukaryotic IscS with an N-terminal mitochondrial targeting extension), the presence of a potential PLP-binding lysine in a 'GKGIGALYIKRKK'-type region, and a catalytic cysteine in a 'GSACTSST'-type motif in the C-terminal half are consistent with IscS/NifS family architecture learned from bacterial and other eukaryotic homologs. The AT-rich composition is a general Plasmodium feature but does not obscure the family-level fold signatures. Thus, family-level recognition of the NifS/IscS clan and elimination of the other three structurally and mechanistically unrelated classes provides a credible, transferable path to EC 2.8.1.7.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on well-established family-level knowledge: the NifS/IscS clan is one of the most studied enzyme families, and the three distractors (radical SAM lipoate synthase, glycosidase, glycosyltransferase) are mechanistically and structurally distinct enough that their absence can be inferred from the sequence's overall architecture, length, and absence of their signature motifs. No fact specific to this exact Plasmodium protein beyond its amino acid sequence is required to make the distinction."
  },
  "case_id": "EC_number_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IBI5 (ISCS_PLAF7, 553 aa, sequence matched) is annotated as Cysteine desulfurase IscS with EC 2.8.1.7, supported by experimental evidence (ECO:0000269, PubMed:34032321, Sadik et al. 2021 Mol Microbiol). The catalytic reaction (sulfur carrier)-H + L-cysteine = (sulfur carrier)-SH + L-alanine is confirmed. The expected answer B (2.8.1.7) is experimentally validated."
  },
  "important_caveats": [
    "The AT-rich composition of Plasmodium falciparum proteins can reduce sequence-similarity-based recognition; however, the structural/fold-level reasoning and elimination of the three mechanistically unrelated distractors remain robust.",
    "The reviewer evidence confirms experimental validation (ECO:0000269) of EC 2.8.1.7 for this protein, but this annotation was not available to the evaluated model.",
    "The N-terminal ~50-60 residues likely constitute a mitochondrial targeting sequence, which is common for eukaryotic IscS and accounts for the slightly longer length compared to bacterial homologs (~420 aa)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (2.8 sulfurtransferases, 3.2 glycosidases, 2.4 glycosyltransferases) and within 2.8, two very different sub-families (PLP-dependent cysteine desulfurase vs. radical SAM lipoate synthase). The sequence features clearly exclude C and D, and the size and absence of radical SAM motifs exclude A. Only B remains as a defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IBI5 (ISCS_PLAF7, 553 aa, sequence matched) is annotated as Cysteine desulfurase IscS with EC 2.8.1.7, supported by experimental evidence (ECO:0000269, PubMed:34032321, Sadik et al. 2021 Mol Microbiol). The catalytic reaction (sulfur carrier)-H + L-cysteine = (sulfur carrier)-SH + L-alanine is confirmed. The expected answer B (2.8.1.7) is experimentally validated.",
    "evidence_ids": ["C4", "C5", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish EC 2.8.1.7 from the other three options using transferable enzyme-family knowledge. (1) EC 3.2.1.20 (alpha-galactosidase) and EC 2.4.1.391 (glycosyltransferase) belong to entirely different enzyme classes with characteristic glycosidase/glycosyltransferase folds and motifs (e.g., GT-B fold, conserved Asp/Glu catalytic residues, beta-propeller or TIM-barrel glycosidase architectures) that are absent from this sequence. (2) EC 2.8.1.11 (lipoate synthase) is a radical SAM enzyme (~350 aa) with a hallmark CxxxCxxC cluster motif; this 553-aa sequence lacks any radical SAM motif and is too large. (3) The remaining candidate EC 2.8.1.7 (cysteine desulfurase IscS/NifS) is a PLP-dependent enzyme of the class I aminotransferase fold, one of the most ubiquitous and well-characterized enzyme families. The sequence length (~553 aa, consistent with eukaryotic IscS with an N-terminal mitochondrial targeting extension), the presence of a potential PLP-binding lysine in a 'GKGIGALYIKRKK'-type region, and a catalytic cysteine in a 'GSACTSST'-type motif in the C-terminal half are consistent with IscS/NifS family architecture learned from bacterial and other eukaryotic homologs. The AT-rich composition is a general Plasmodium feature but does not obscure the family-level fold signatures. Thus, family-level recognition of the NifS/IscS clan and elimination of the other three structurally and mechanistically unrelated classes provides a credible, transferable path to EC 2.8.1.7.",
    "missing_item_specific_fact": "",
    "reason": "The discrimination relies on well-established family-level knowledge: the NifS/IscS clan is one of the most studied enzyme families, and the three distractors (radical SAM lipoate synthase, glycosidase, glycosyltransferase) are mechanistically and structurally distinct enough that their absence can be inferred from the sequence's overall architecture, length, and absence of their signature motifs. No fact specific to this exact Plasmodium protein beyond its amino acid sequence is required to make the distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (2.8 sulfurtransferases, 3.2 glycosidases, 2.4 glycosyltransferases) and within 2.8, two very different sub-families (PLP-dependent cysteine desulfurase vs. radical SAM lipoate synthase). The sequence features clearly exclude C and D, and the size and absence of radical SAM motifs exclude A. Only B remains as a defensible choice."
  },
  "important_caveats": [
    "The AT-rich composition of Plasmodium falciparum proteins can reduce sequence-similarity-based recognition; however, the structural/fold-level reasoning and elimination of the three mechanistically unrelated distractors remain robust.",
    "The reviewer evidence confirms experimental validation (ECO:0000269) of EC 2.8.1.7 for this protein, but this annotation was not available to the evaluated model.",
    "The N-terminal ~50-60 residues likely constitute a mitochondrial targeting sequence, which is common for eukaryotic IscS and accounts for the slightly longer length compared to bacterial homologs (~420 aa)."
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
  "benchmark_sequence_length": 553,
  "benchmark_sequence_sha256": "d59f0501df32d187044d3d8f803b0f8f28d948df60bbe0a9f56e20ddbe5b3b43",
  "current_entry_audit": {
    "entryVersion": 129,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 553,
  "current_source_sequence_sha256": "d59f0501df32d187044d3d8f803b0f8f28d948df60bbe0a9f56e20ddbe5b3b43",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 127,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IBI5",
  "selected_historical_entry_version": 127,
  "selected_historical_record_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "selected_historical_source_sequence_length": 553,
  "selected_historical_source_sequence_sha256": "d59f0501df32d187044d3d8f803b0f8f28d948df60bbe0a9f56e20ddbe5b3b43",
  "selected_historical_version": {
    "accession": "Q8IBI5",
    "database": "Swiss-Prot",
    "entryVersion": 127,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ISCS_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IBI5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":129,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"2.8.1.7\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cysteine desulfurase IscS\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"PfIscS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:43893\"}}],\"reaction\":{\"ecNumber\":\"2.8.1.7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"name\":\"(sulfur carrier)-H + L-cysteine = (sulfur carrier)-SH + L-alanine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:43892\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:14737\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:14739\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29917\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35235\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57972\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64428\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IBI5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Sadik M.\",\"Afsar M.\",\"Ramachandran R.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34032321\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14735\"}],\"citationType\":\"journal article\",\"firstPage\":\"606\",\"id\":\"34032321\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"623\",\"publicationDate\":\"2021\",\"title\":\"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\",\"INTERACTION WITH ISD11 AND ISCU\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:06.723158+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "dee0fef0d1ba02eb0ea344f9e6225c156791bfc0aa144562d73d96e9bfcb50dd",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IBI5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H1",
  "excerpt": "ID   ISCS_PLAF7              Reviewed;         553 AA.\nAC   Q8IBI5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 127.\nDE   RecName: Full=Cysteine desulfurase IscS {ECO:0000305};\nDE            Short=PfIscS {ECO:0000303|PubMed:34032321};\nDE            EC=2.8.1.7 {ECO:0000269|PubMed:34032321};\nGN   Name=IscS {ECO:0000303|PubMed:24086138, ECO:0000303|PubMed:34032321};\nGN   Synonyms=NFS1 {ECO:0000305};\nGN   ORFNames=PF3D7_0727200 {ECO:0000312|EMBL:CAD51015.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cysteine desulfurase IscS {ECO:0000305};\nDE            Short=PfIscS {ECO:0000303|PubMed:34032321};\nDE            EC=2.8.1.7 {ECO:0000269|PubMed:34032321};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   SUBCELLULAR LOCATION.\nRX   PubMed=24086138; DOI=10.1371/journal.ppat.1003655;\nRA   Gisselberg J.E., Dellibovi-Ragheb T.A., Matthews K.A., Bosch G.,\nRA   Prigge S.T.;\nRT   \"The suf iron-sulfur cluster synthesis pathway is required for apicoplast\nRT   maintenance in malaria parasites.\";\nRL   PLoS Pathog. 9:e1003655-e1003655(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, AND INTERACTION WITH ISD11\nRP   AND ISCU.\nRX   PubMed=34032321; DOI=10.1111/mmi.14735;\nRA   Sadik M., Afsar M., Ramachandran R., Habib S.;\nRT   \"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the\nRT   Plasmodium falciparum mitochondrion.\";\nRL   Mol. Microbiol. 116:606-623(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(sulfur carrier)-H + L-cysteine = (sulfur carrier)-SH + L-\nCC         alanine; Xref=Rhea:RHEA:43892, Rhea:RHEA-COMP:14737, Rhea:RHEA-\nCC         COMP:14739, ChEBI:CHEBI:29917, ChEBI:CHEBI:35235, ChEBI:CHEBI:57972,\nCC         ChEBI:CHEBI:64428; EC=2.8.1.7;\nCC         Evidence={ECO:0000269|PubMed:34032321};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:43893;\nCC         Evidence={ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:12.658506+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1ca62d2b3db1f49395cf1cf37dcbb4a4bf53cc8c99d3d8a38c959bf07ee05d63",
  "url": "https://rest.uniprot.org/unisave/Q8IBI5?format=txt&versions=127"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 40. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
