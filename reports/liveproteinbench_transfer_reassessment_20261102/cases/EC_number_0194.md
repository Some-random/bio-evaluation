# EC_number_0194

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0194.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MHLASSLFLLATLPFGFAAGKGKGKGKDNSDVGLDVLAKKAGLKYFGAATDTPGQRERAGLEDKYPEYDRIMWHSPEFGSTTPTNGQKWLFVEPERGVFNFTEGDVVASKARQHGKLLRCHALVWHSQLAPWVEETEWTPEELRKVIVDHITAVAGHYKGQCYAWDVVNEALNEDGTYRESVFYKVLGEEYIKLAFETAAKVDPKAKLYYNDYNLEWPSAKTEGAKRIVKLLKDAKIPIHGVGLQAHLIAEQHPTLDDHIAAIRGFTQLGVEVALTELDIRLKTPATEENLALQREAYKNVVGACVQVCGCVGVTIWDFYDPFSWVPYFFEGEGAPLLWFEDFSKHPAYYGVVEALTNKTRRSKRSISDRRAKLLA

[Multiple Choices]
A. 3.2.1.105
B. 3.2.1.8
C. 2.7.7.80
D. 2.7.7.43
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

> The sequence matches the referenced UniProt entry, which assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans. The annotation links this function to ECO:0000269 evidence and PubMed 23306124, so the key is supported by an experimentally attributed source, although the paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, and the remaining roughly 350-residue enzyme sequence is consistent with a fungal extracellular glycoside hydrolase such as a xylanase. Transferable sequence-family and catalytic-domain patterns can support xylan hydrolysis, favoring EC 3.2.1.8 over the nucleotide-transferase choices C and D and the alternative hydrolase A. This is a family-level probabilistic inference, not proof of the exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence supplies features that can support a secreted fungal glycoside-hydrolase/xylanase inference without recalling this protein's database record. That inference meaningfully distinguishes the keyed choice among the offered alternatives, though an exact EC assignment would remain less certain than the family-level prediction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is established by the supplied information as equally defensible as EC 3.2.1.8.


### Important caveats

- The source evidence is reviewer-only and is used to assess the key, not as an input to the transferability judgment.
- The cited experimental evidence is present in the database annotation, but the primary publication was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the remaining roughly 350-residue enzyme sequence is consistent with a fungal extracellular glycoside hydrolase such as a xylanase. Transferable sequence-family and catalytic-domain patterns can support xylan hydrolysis, favoring EC 3.2.1.8 over the nucleotide-transferase choices C and D and the alternative hydrolase A. This is a family-level probabilistic inference, not proof of the exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence supplies features that can support a secreted fungal glycoside-hydrolase/xylanase inference without recalling this protein's database record. That inference meaningfully distinguishes the keyed choice among the offered alternatives, though an exact EC assignment would remain less certain than the family-level prediction."
  },
  "case_id": "EC_number_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the referenced UniProt entry, which assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans. The annotation links this function to ECO:0000269 evidence and PubMed 23306124, so the key is supported by an experimentally attributed source, although the paper was not independently reviewed here."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and is used to assess the key, not as an input to the transferability judgment.",
    "The cited experimental evidence is present in the database annotation, but the primary publication was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is established by the supplied information as equally defensible as EC 3.2.1.8."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the referenced UniProt entry, which assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans. The annotation links this function to ECO:0000269 evidence and PubMed 23306124, so the key is supported by an experimentally attributed source, although the paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and the remaining roughly 350-residue enzyme sequence is consistent with a fungal extracellular glycoside hydrolase such as a xylanase. Transferable sequence-family and catalytic-domain patterns can support xylan hydrolysis, favoring EC 3.2.1.8 over the nucleotide-transferase choices C and D and the alternative hydrolase A. This is a family-level probabilistic inference, not proof of the exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "The sequence supplies features that can support a secreted fungal glycoside-hydrolase/xylanase inference without recalling this protein's database record. That inference meaningfully distinguishes the keyed choice among the offered alternatives, though an exact EC assignment would remain less certain than the family-level prediction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is established by the supplied information as equally defensible as EC 3.2.1.8."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and is used to assess the key, not as an input to the transferability judgment.",
    "The cited experimental evidence is present in the database annotation, but the primary publication was not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry M4MGK7 (XYNA_HUMIN) is annotated with EC 3.2.1.8 (Endo-1,4-beta-xylanase) with experimental evidence code ECO:0000269 from PubMed:23306124, which reports catalytic activity and substrate specificity. The sequence in the question matches the canonical entry (SHA-256 identical). The annotation is experimentally verified, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Two layers of transferable knowledge distinguish the options. (1) The N-terminal hydrophobic stretch (MHLASSLFLLATLPFGFAAGKGKGKGK…) is a classic fungal signal peptide indicating a secreted enzyme. Secreted proteins in fungi are overwhelmingly hydrolases (cell-wall-degrading enzymes), whereas nucleotidyltransferases/polymerases (EC 2.7.7.x, options C and D) are intracellular and lack signal peptides. This eliminates C and D. (2) Among the remaining hydrolases, the catalytic domain displays multiple hallmarks of Glycoside Hydrolase family 10 (GH10) endo-xylanases: a (β/α)8 TIM-barrel–type sequence architecture, an unusually high density of tryptophan residues in conserved positions (WHSPEF, WLFVEP, WVEETEWTPEEL, WDVVNE, WPSAK, WDFYDP, WVPYFF, WVEAL), and the signature WDF motif (WDFYDPFSWVPYFFEGEGAPLLWFEDFSKHP) that is a well-known catalytic-domain fingerprint of GH10 xylanases across many fungal species (Trichoderma, Aspergillus, Humicola homologs). Arabinofuranosidases (EC 3.2.1.105, option A) belong to GH43, GH51, GH54, GH62, GH67, etc., which adopt β-propeller folds with entirely different sequence motifs and do not carry the WDF/TIM-barrel pattern. Thus, recognizing the GH10 family signature—learned from other xylanases—meaningfully selects B over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal peptide eliminates the polymerase options (C, D) by a general secreted-vs-intracellular principle. The GH10-specific WDF motif, TIM-barrel sequence architecture, and tryptophan-dense catalytic domain are conserved features shared across many fungal GH10 xylanases (e.g., Trichoderma, Aspergillus, other Humicola entries) and are absent in arabinofuranosidase families. A knowledgeable model can use these family-level sequence signatures to select 3.2.1.8 over 3.2.1.105 without memorizing this particular protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GH10 WDF/TIM-barrel signature is distinctive enough to separate B (xylanase) from A (arabinofuranosidase), and the signal peptide clearly excludes the polymerase options C and D. No alternative option is equally defensible given the sequence features.


### Important caveats

- The UniProt annotation is experimentally supported (ECO:0000269, PubMed:23306124), providing strong ground-truth confidence for EC 3.2.1.8.
- The GH10 motif recognition argument is probabilistic: a model trained on diverse GH10 sequences would recognize the WDF and tryptophan-dense pattern, but a model unfamiliar with GH family signatures might struggle to separate B from A purely on sequence.
- The sequence is a precursor (376 AA including signal peptide); the catalytic domain is the C-terminal ~300 residues, consistent with typical GH10 xylanase domain sizes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two layers of transferable knowledge distinguish the options. (1) The N-terminal hydrophobic stretch (MHLASSLFLLATLPFGFAAGKGKGKGK…) is a classic fungal signal peptide indicating a secreted enzyme. Secreted proteins in fungi are overwhelmingly hydrolases (cell-wall-degrading enzymes), whereas nucleotidyltransferases/polymerases (EC 2.7.7.x, options C and D) are intracellular and lack signal peptides. This eliminates C and D. (2) Among the remaining hydrolases, the catalytic domain displays multiple hallmarks of Glycoside Hydrolase family 10 (GH10) endo-xylanases: a (β/α)8 TIM-barrel–type sequence architecture, an unusually high density of tryptophan residues in conserved positions (WHSPEF, WLFVEP, WVEETEWTPEEL, WDVVNE, WPSAK, WDFYDP, WVPYFF, WVEAL), and the signature WDF motif (WDFYDPFSWVPYFFEGEGAPLLWFEDFSKHP) that is a well-known catalytic-domain fingerprint of GH10 xylanases across many fungal species (Trichoderma, Aspergillus, Humicola homologs). Arabinofuranosidases (EC 3.2.1.105, option A) belong to GH43, GH51, GH54, GH62, GH67, etc., which adopt β-propeller folds with entirely different sequence motifs and do not carry the WDF/TIM-barrel pattern. Thus, recognizing the GH10 family signature—learned from other xylanases—meaningfully selects B over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide eliminates the polymerase options (C, D) by a general secreted-vs-intracellular principle. The GH10-specific WDF motif, TIM-barrel sequence architecture, and tryptophan-dense catalytic domain are conserved features shared across many fungal GH10 xylanases (e.g., Trichoderma, Aspergillus, other Humicola entries) and are absent in arabinofuranosidase families. A knowledgeable model can use these family-level sequence signatures to select 3.2.1.8 over 3.2.1.105 without memorizing this particular protein's record."
  },
  "case_id": "EC_number_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry M4MGK7 (XYNA_HUMIN) is annotated with EC 3.2.1.8 (Endo-1,4-beta-xylanase) with experimental evidence code ECO:0000269 from PubMed:23306124, which reports catalytic activity and substrate specificity. The sequence in the question matches the canonical entry (SHA-256 identical). The annotation is experimentally verified, not merely computational."
  },
  "important_caveats": [
    "The UniProt annotation is experimentally supported (ECO:0000269, PubMed:23306124), providing strong ground-truth confidence for EC 3.2.1.8.",
    "The GH10 motif recognition argument is probabilistic: a model trained on diverse GH10 sequences would recognize the WDF and tryptophan-dense pattern, but a model unfamiliar with GH family signatures might struggle to separate B from A purely on sequence.",
    "The sequence is a precursor (376 AA including signal peptide); the catalytic domain is the C-terminal ~300 residues, consistent with typical GH10 xylanase domain sizes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH10 WDF/TIM-barrel signature is distinctive enough to separate B (xylanase) from A (arabinofuranosidase), and the signal peptide clearly excludes the polymerase options C and D. No alternative option is equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry M4MGK7 (XYNA_HUMIN) is annotated with EC 3.2.1.8 (Endo-1,4-beta-xylanase) with experimental evidence code ECO:0000269 from PubMed:23306124, which reports catalytic activity and substrate specificity. The sequence in the question matches the canonical entry (SHA-256 identical). The annotation is experimentally verified, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Two layers of transferable knowledge distinguish the options. (1) The N-terminal hydrophobic stretch (MHLASSLFLLATLPFGFAAGKGKGKGK…) is a classic fungal signal peptide indicating a secreted enzyme. Secreted proteins in fungi are overwhelmingly hydrolases (cell-wall-degrading enzymes), whereas nucleotidyltransferases/polymerases (EC 2.7.7.x, options C and D) are intracellular and lack signal peptides. This eliminates C and D. (2) Among the remaining hydrolases, the catalytic domain displays multiple hallmarks of Glycoside Hydrolase family 10 (GH10) endo-xylanases: a (β/α)8 TIM-barrel–type sequence architecture, an unusually high density of tryptophan residues in conserved positions (WHSPEF, WLFVEP, WVEETEWTPEEL, WDVVNE, WPSAK, WDFYDP, WVPYFF, WVEAL), and the signature WDF motif (WDFYDPFSWVPYFFEGEGAPLLWFEDFSKHP) that is a well-known catalytic-domain fingerprint of GH10 xylanases across many fungal species (Trichoderma, Aspergillus, Humicola homologs). Arabinofuranosidases (EC 3.2.1.105, option A) belong to GH43, GH51, GH54, GH62, GH67, etc., which adopt β-propeller folds with entirely different sequence motifs and do not carry the WDF/TIM-barrel pattern. Thus, recognizing the GH10 family signature—learned from other xylanases—meaningfully selects B over A.",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide eliminates the polymerase options (C, D) by a general secreted-vs-intracellular principle. The GH10-specific WDF motif, TIM-barrel sequence architecture, and tryptophan-dense catalytic domain are conserved features shared across many fungal GH10 xylanases (e.g., Trichoderma, Aspergillus, other Humicola entries) and are absent in arabinofuranosidase families. A knowledgeable model can use these family-level sequence signatures to select 3.2.1.8 over 3.2.1.105 without memorizing this particular protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GH10 WDF/TIM-barrel signature is distinctive enough to separate B (xylanase) from A (arabinofuranosidase), and the signal peptide clearly excludes the polymerase options C and D. No alternative option is equally defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt annotation is experimentally supported (ECO:0000269, PubMed:23306124), providing strong ground-truth confidence for EC 3.2.1.8.",
    "The GH10 motif recognition argument is probabilistic: a model trained on diverse GH10 sequences would recognize the WDF and tryptophan-dense pattern, but a model unfamiliar with GH family signatures might struggle to separate B from A purely on sequence.",
    "The sequence is a precursor (376 AA including signal peptide); the catalytic domain is the C-terminal ~300 residues, consistent with typical GH10 xylanase domain sizes."
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
  "benchmark_sequence_length": 376,
  "benchmark_sequence_sha256": "099e0d9d31b95aad01d9114eec635a5ba258509622920c5ebd279553304abc33",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 376,
  "current_source_sequence_sha256": "099e0d9d31b95aad01d9114eec635a5ba258509622920c5ebd279553304abc33",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "M4MGK7",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "selected_historical_source_sequence_length": 376,
  "selected_historical_source_sequence_sha256": "099e0d9d31b95aad01d9114eec635a5ba258509622920c5ebd279553304abc33",
  "selected_historical_version": {
    "accession": "M4MGK7",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNA_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MGK7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase A\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase A\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MGK7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:05.622631+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0eb386047796a4c6d2cf2618df1e68195ff8e1f1d846dddec1115d408f18e15",
  "url": "https://rest.uniprot.org/uniprotkb/M4MGK7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   XYNA_HUMIN              Reviewed;         376 AA.\nAC   M4MGK7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Endo-1,4-beta-xylanase A {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase A {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynA {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Endo-1,4-beta-xylanase A {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase A {ECO:0000305};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:23306124};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:07.720781+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7ec5a9552d4e5401ddcbb6f19ae0b5460a5e468847c5025d55b7f1a6cab2cd96",
  "url": "https://rest.uniprot.org/unisave/M4MGK7?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 194. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
