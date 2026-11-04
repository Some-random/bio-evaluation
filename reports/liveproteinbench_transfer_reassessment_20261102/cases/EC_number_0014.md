# EC_number_0014

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0014.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 4.3.3.9

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTLQETSVLEPTLQGTTTLPGLLAQRVAEHPEAIAVAYRDDKLTFRELASRSAALADYLEHLGVSADDCVGLFVEPSIDLMVGAWGILNAGAAYLPLSPEYPEDRLRYMIENSETKIILAQQRLVSRLRELAPKDVTIVTLRESEAFVRPEGTEAPAARSARPDTLAYVIYTSGSTGKPKGVMIEHRSIVNQLGWLRETYAIDRSKVILQKTPMSFDAAQWEILSPANGATVVMGAPGVYADPEGLIETIVKHNVTTLQCVPTLLQGLIDTEKFPECVSLQQIFSGGEALSRLLAIQTTQEMPGRALINVYGPTETTINSSSFPVDPADLDEGPQSISIGSPVHGTTYHILDKETLKPVGVGEIGELYIGGIQLARGYLHRDDLTAERFLEIELEEGAEPVRLYKTGDLGQWNNDGTVQFAGRADNQVKLRGYRVELDEISLAIENHDWVRNAAVIVKNDGRTGFQNLIACIELSEKEAALMDQGNHGSHHASKKSKLQVKAQLSNPGLRDDAELAARPAFDLEGAEPTPEQRARVFARKTYRFYEGGAVTQADLLGLLGATVTAGYSRKAADLAPAELGQILRWFGQYISEERLLPKYGYASPGALYATQMYFELEGVGGLKPGYYYYQPVRHQLVLISEREATGKATAQIHFIGKKSGIEPVYKNNILEVLEIETGHMVGLFEQILPAYGLDIHDRAYEPAVKDLLDVADEDYYLGTFELVPHAGARDDQAEVYVQTHGGKVAGLPEGQYRYENGELTRFSDDIVLKKHVIAINQSVYQAASFGISVYSRAEEEWLKYITLGKKLQHLMMNGLNLGFMSSGYSSKTGNPLPASRRMDAVLGANGVDSAPMYFFVGGRISDEQIGHEGMREDSVHMRGPAELIRDDLVSFLPDYMIPNRVVVFDRLPLSANGKIDVKALAASDQVNAELVERPFVAPRTETEKEIAAVWEKALRRENASVQDDFFESGGNSLIAVGLVRELNARLGVSLPLQSVLESPTIEKLARRLEREVAQESSRFVRLHAETGKARPVICWPGLGGYPMNLRSLAGEIGLGRSFYGVQSYGINEGETPYETITEMAKKDIEALKEIQPAGPYTLWGYSFGARVAFETAYQLEQAGEKVDNLFLIAPGSPKVRAENGKVWGREASFANRGYTTILFSVFTGTISGPDLDRCLETVTDEASFAEFISELKGIDVDLARRIISVVGQTYEFEYSFHELAERTLQAPISIFKAVGDDYSFLENSSGYSAEPPTVIDLDADHYSLLREDIGELVKHIRYLLGE

[Multiple Choices]
A. 4.3.1.12
B. 4.3.1.24
C. 4.2.3.1
D. 4.3.3.9
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

> The sequence matches the source record, whose EC 4.3.3.9 assignment is supported by cited experimental evidence for the catalytic reaction. This supports the author's key for the supplied protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1,282-residue sequence has features consistent with a large nonribosomal peptide synthetase, including an adenylation-domain signature and a carrier-protein-like module. Transferable knowledge of NRPSs makes a specialized biosynthetic enzyme such as the offered indigoidine-synthase EC 4.3.3.9 substantially more plausible than the other listed lyase or terpene-synthase options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the enzyme's exact product from sequence alone is not certain, but the sequence's NRPS-like architecture meaningfully distinguishes D among these choices without needing the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives represent distinct enzyme classifications, and the sequence's apparent NRPS architecture favors D over the other offered choices.


### Important caveats

- The sequence-based argument supports a meaningful choice among these alternatives, but does not independently establish the precise catalytic reaction or complete EC number.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1,282-residue sequence has features consistent with a large nonribosomal peptide synthetase, including an adenylation-domain signature and a carrier-protein-like module. Transferable knowledge of NRPSs makes a specialized biosynthetic enzyme such as the offered indigoidine-synthase EC 4.3.3.9 substantially more plausible than the other listed lyase or terpene-synthase options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme's exact product from sequence alone is not certain, but the sequence's NRPS-like architecture meaningfully distinguishes D among these choices without needing the exact protein's recorded annotation."
  },
  "case_id": "EC_number_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the source record, whose EC 4.3.3.9 assignment is supported by cited experimental evidence for the catalytic reaction. This supports the author's key for the supplied protein."
  },
  "important_caveats": [
    "The sequence-based argument supports a meaningful choice among these alternatives, but does not independently establish the precise catalytic reaction or complete EC number."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives represent distinct enzyme classifications, and the sequence's apparent NRPS architecture favors D over the other offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the source record, whose EC 4.3.3.9 assignment is supported by cited experimental evidence for the catalytic reaction. This supports the author's key for the supplied protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1,282-residue sequence has features consistent with a large nonribosomal peptide synthetase, including an adenylation-domain signature and a carrier-protein-like module. Transferable knowledge of NRPSs makes a specialized biosynthetic enzyme such as the offered indigoidine-synthase EC 4.3.3.9 substantially more plausible than the other listed lyase or terpene-synthase options.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the enzyme's exact product from sequence alone is not certain, but the sequence's NRPS-like architecture meaningfully distinguishes D among these choices without needing the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives represent distinct enzyme classifications, and the sequence's apparent NRPS architecture favors D over the other offered choices."
  },
  "important_caveats": [
    "The sequence-based argument supports a meaningful choice among these alternatives, but does not independently establish the precise catalytic reaction or complete EC number."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q1MWN4 (Indigoidine synthase, bpsA from Streptomyces lavendulae) is annotated with EC 4.3.3.9 supported by experimental evidence (ECO:0000269, PubMed:17237222). The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O) is experimentally characterized. The benchmark sequence (1282 AA) matches the UniProt entry exactly (SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains multiple hallmark NRPS (non-ribosomal peptide synthetase) domain signatures: the canonical adenylation-domain motif 'TSGSTGKPKG' (~position 200), condensation-domain motifs such as 'YTTILFSVFTGTISGPDLDRCLE' and 'YTFYEGGAVTQADLLGLLGATVTAGYSRK', and a peptidyl-carrier-protein (PCP) domain region. The overall ~1282-residue length is consistent with a single-module NRPS (C-A-PCP architecture). Among the four choices: EC 4.2.3.1 (terpene synthase/copalyl diphosphate synthase) requires a terpene-cyclase fold with DDXXD motifs — completely incompatible with NRPS domains; EC 4.3.1.24 (phenylalanine ammonia-lyase) is a PLP-dependent enzyme with a completely different fold; EC 4.3.1.12 is a specific aminomutase-type lyase, also not an NRPS. Only EC 4.3.3.9 (indigoidine synthase) is a single-module NRPS. Recognizing the NRPS domain architecture is a well-established, transferable family-level feature that meaningfully eliminates A, B, and C and points to D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the TSGSTGKP adenylation-domain signature, condensation-domain motifs, and PCP domain as hallmarks of NRPS enzymes can use this family-level knowledge to eliminate the three non-NRPS options (terpene synthase, ammonia-lyase, aminomutase) and select the only NRPS-type EC number among the choices. This is a legitimate transfer from general knowledge of NRPS domain architecture learned from many other NRPS proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The NRPS domain architecture unambiguously distinguishes option D from options A, B, and C, none of which are NRPS enzymes. No other choice is consistent with the observed domain features.


### Important caveats

- The specific EC number 4.3.3.9 is essentially unique to indigoidine synthase; however, the question only requires distinguishing among four provided choices, and NRPS architecture suffices for that.
- The EC classification of indigoidine synthase under EC 4 (lyases) rather than EC 6 (ligases) is somewhat unusual given the ATP-dependent reaction, but this is the established IUBMB classification.
- The reviewer evidence is from a Swiss-Prot entry first released in 2025-02; the benchmark question may have been constructed from an earlier TrEMBL annotation or the same paper (PubMed:17237222, 2007).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains multiple hallmark NRPS (non-ribosomal peptide synthetase) domain signatures: the canonical adenylation-domain motif 'TSGSTGKPKG' (~position 200), condensation-domain motifs such as 'YTTILFSVFTGTISGPDLDRCLE' and 'YTFYEGGAVTQADLLGLLGATVTAGYSRK', and a peptidyl-carrier-protein (PCP) domain region. The overall ~1282-residue length is consistent with a single-module NRPS (C-A-PCP architecture). Among the four choices: EC 4.2.3.1 (terpene synthase/copalyl diphosphate synthase) requires a terpene-cyclase fold with DDXXD motifs — completely incompatible with NRPS domains; EC 4.3.1.24 (phenylalanine ammonia-lyase) is a PLP-dependent enzyme with a completely different fold; EC 4.3.1.12 is a specific aminomutase-type lyase, also not an NRPS. Only EC 4.3.3.9 (indigoidine synthase) is a single-module NRPS. Recognizing the NRPS domain architecture is a well-established, transferable family-level feature that meaningfully eliminates A, B, and C and points to D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the TSGSTGKP adenylation-domain signature, condensation-domain motifs, and PCP domain as hallmarks of NRPS enzymes can use this family-level knowledge to eliminate the three non-NRPS options (terpene synthase, ammonia-lyase, aminomutase) and select the only NRPS-type EC number among the choices. This is a legitimate transfer from general knowledge of NRPS domain architecture learned from many other NRPS proteins."
  },
  "case_id": "EC_number_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q1MWN4 (Indigoidine synthase, bpsA from Streptomyces lavendulae) is annotated with EC 4.3.3.9 supported by experimental evidence (ECO:0000269, PubMed:17237222). The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O) is experimentally characterized. The benchmark sequence (1282 AA) matches the UniProt entry exactly (SHA256 confirmed)."
  },
  "important_caveats": [
    "The specific EC number 4.3.3.9 is essentially unique to indigoidine synthase; however, the question only requires distinguishing among four provided choices, and NRPS architecture suffices for that.",
    "The EC classification of indigoidine synthase under EC 4 (lyases) rather than EC 6 (ligases) is somewhat unusual given the ATP-dependent reaction, but this is the established IUBMB classification.",
    "The reviewer evidence is from a Swiss-Prot entry first released in 2025-02; the benchmark question may have been constructed from an earlier TrEMBL annotation or the same paper (PubMed:17237222, 2007)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NRPS domain architecture unambiguously distinguishes option D from options A, B, and C, none of which are NRPS enzymes. No other choice is consistent with the observed domain features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q1MWN4 (Indigoidine synthase, bpsA from Streptomyces lavendulae) is annotated with EC 4.3.3.9 supported by experimental evidence (ECO:0000269, PubMed:17237222). The catalytic reaction (2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O) is experimentally characterized. The benchmark sequence (1282 AA) matches the UniProt entry exactly (SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "C8", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains multiple hallmark NRPS (non-ribosomal peptide synthetase) domain signatures: the canonical adenylation-domain motif 'TSGSTGKPKG' (~position 200), condensation-domain motifs such as 'YTTILFSVFTGTISGPDLDRCLE' and 'YTFYEGGAVTQADLLGLLGATVTAGYSRK', and a peptidyl-carrier-protein (PCP) domain region. The overall ~1282-residue length is consistent with a single-module NRPS (C-A-PCP architecture). Among the four choices: EC 4.2.3.1 (terpene synthase/copalyl diphosphate synthase) requires a terpene-cyclase fold with DDXXD motifs — completely incompatible with NRPS domains; EC 4.3.1.24 (phenylalanine ammonia-lyase) is a PLP-dependent enzyme with a completely different fold; EC 4.3.1.12 is a specific aminomutase-type lyase, also not an NRPS. Only EC 4.3.3.9 (indigoidine synthase) is a single-module NRPS. Recognizing the NRPS domain architecture is a well-established, transferable family-level feature that meaningfully eliminates A, B, and C and points to D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the TSGSTGKP adenylation-domain signature, condensation-domain motifs, and PCP domain as hallmarks of NRPS enzymes can use this family-level knowledge to eliminate the three non-NRPS options (terpene synthase, ammonia-lyase, aminomutase) and select the only NRPS-type EC number among the choices. This is a legitimate transfer from general knowledge of NRPS domain architecture learned from many other NRPS proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NRPS domain architecture unambiguously distinguishes option D from options A, B, and C, none of which are NRPS enzymes. No other choice is consistent with the observed domain features."
  },
  "important_caveats": [
    "The specific EC number 4.3.3.9 is essentially unique to indigoidine synthase; however, the question only requires distinguishing among four provided choices, and NRPS architecture suffices for that.",
    "The EC classification of indigoidine synthase under EC 4 (lyases) rather than EC 6 (ligases) is somewhat unusual given the ATP-dependent reaction, but this is the established IUBMB classification.",
    "The reviewer evidence is from a Swiss-Prot entry first released in 2025-02; the benchmark question may have been constructed from an earlier TrEMBL annotation or the same paper (PubMed:17237222, 2007)."
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
  "benchmark_sequence_length": 1282,
  "benchmark_sequence_sha256": "15bb18089a044204b45b7f6a6f05b7d317f19a85a8c8fc99093082e6b56646a0",
  "current_entry_audit": {
    "entryVersion": 88,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-05-30",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1282,
  "current_source_sequence_sha256": "15bb18089a044204b45b7f6a6f05b7d317f19a85a8c8fc99093082e6b56646a0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 86,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q1MWN4",
  "selected_historical_entry_version": 86,
  "selected_historical_record_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "selected_historical_source_sequence_length": 1282,
  "selected_historical_source_sequence_sha256": "15bb18089a044204b45b7f6a6f05b7d317f19a85a8c8fc99093082e6b56646a0",
  "selected_historical_version": {
    "accession": "Q1MWN4",
    "database": "Swiss-Prot",
    "entryVersion": 86,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "INDGS_STRLA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q1MWN4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":88,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-05-30\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces lavendulae\",\"taxonId\":1914}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"value\":\"Blue pigment synthetase-encoding gene A\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"value\":\"Blue-pigment synthetase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"value\":\"4.3.3.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Indigoidine synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81500\"}}],\"reaction\":{\"ecNumber\":\"4.3.3.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"name\":\"2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2 AMP + 2 diphosphate + 2 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81499\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:79296\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81504\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"name\":\"FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-dione + FMNH2 + AMP + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81503\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231893\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456215\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81508\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17237222\",\"source\":\"PubMed\"}],\"name\":\"2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81507\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:79296\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231893\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Takahashi H.\",\"Kumagai T.\",\"Kitani K.\",\"Mori M.\",\"Matoba Y.\",\"Sugiyama M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17237222\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m611319200\"}],\"citationType\":\"journal article\",\"firstPage\":\"9073\",\"id\":\"17237222\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"9081\",\"publicationDate\":\"2007\",\"title\":\"Cloning and characterization of a Streptomyces single module type non-ribosomal peptide synthetase catalyzing a blue pigment synthesis.\",\"volume\":\"282\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAE93896.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 11924 / 8197-20\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"DOMAIN\",\"PHOSPHOPANTETHEINYLATION AT SER-972\",\"MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:19.982445+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193",
  "url": "https://rest.uniprot.org/uniprotkb/Q1MWN4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H1",
  "excerpt": "ID   INDGS_STRLA             Reviewed;        1282 AA.\nAC   Q1MWN4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   30-MAY-2006, sequence version 1.\nDT   28-JAN-2026, entry version 86.\nDE   RecName: Full=Indigoidine synthase {ECO:0000305};\nDE            EC=4.3.3.9 {ECO:0000269|PubMed:17237222};\nDE   AltName: Full=Blue pigment synthetase-encoding gene A {ECO:0000303|PubMed:17237222};\nDE   AltName: Full=Blue-pigment synthetase {ECO:0000303|PubMed:17237222};\nGN   Name=bpsA {ECO:0000303|PubMed:17237222};\nOS   Streptomyces lavendulae.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=1914;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Indigoidine synthase {ECO:0000305};\nDE            EC=4.3.3.9 {ECO:0000269|PubMed:17237222};\nDE   AltName: Full=Blue pigment synthetase-encoding gene A {ECO:0000303|PubMed:17237222};\nDE   AltName: Full=Blue-pigment synthetase {ECO:0000303|PubMed:17237222};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAE93896.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, DOMAIN, PHOSPHOPANTETHEINYLATION AT\nRP   SER-972, AND MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608.\nRC   STRAIN=ATCC 11924 / 8197-20;\nRX   PubMed=17237222; DOI=10.1074/jbc.m611319200;\nRA   Takahashi H., Kumagai T., Kitani K., Mori M., Matoba Y., Sugiyama M.;\nRT   \"Cloning and characterization of a Streptomyces single module type non-\nRT   ribosomal peptide synthetase catalyzing a blue pigment synthesis.\";\nRL   J. Biol. Chem. 282:9073-9081(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 FMN + 2 L-glutamine + 2 ATP + O2 = indigoidine + 2 FMNH2 + 2\nCC         AMP + 2 diphosphate + 2 H2O; Xref=Rhea:RHEA:81499, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:30616, ChEBI:CHEBI:33019,\nCC         ChEBI:CHEBI:57618, ChEBI:CHEBI:58210, ChEBI:CHEBI:58359,\nCC         ChEBI:CHEBI:79296, ChEBI:CHEBI:456215; EC=4.3.3.9;\nCC         Evidence={ECO:0000269|PubMed:17237222};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81500;\nCC         Evidence={ECO:0000269|PubMed:17237222};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-\nCC         dione + FMNH2 + AMP + diphosphate; Xref=Rhea:RHEA:81503,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57618,\nCC         ChEBI:CHEBI:58210, ChEBI:CHEBI:58359, ChEBI:CHEBI:231893,\nCC         ChEBI:CHEBI:456215; Evidence={ECO:0000305|PubMed:17237222};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81504;\nCC         Evidence={ECO:0000305|PubMed:17237222};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)

```json
{
  "entry_version": 86,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 3-amino-1,5-dihydropyridine-2,6-dione + O2 = indigoidine + 2\nCC         H2O; Xref=Rhea:RHEA:81507, ChEBI:CHEBI:15377, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:79296, ChEBI:CHEBI:231893;\nCC         Evidence={ECO:0000305|PubMed:17237222};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81508;\nCC         Evidence={ECO:0000305|PubMed:17237222};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:29.129628+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f",
  "url": "https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
