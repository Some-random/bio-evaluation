# EC_number_0106

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0106.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.3.1.193

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVNKEQFYDQIRKALEDGNTRYYRNLIYIERDDYFDHVKEIISLFLNFKSNPSVAYGFVPWASGSKERMRTIKEYFSKFDDIDYANAEYYLGNTYDLVILDTVDNFQPINIGRLVDLARGGGLIIIYTNNLIKDKTFRTSIMRNGLILDEYEKRFKRKLYEHEGIFIIDVNEYIPKPFSGNTMPKAEKKVPRNPLMPKEIHELSLSEDQNRVIESFTYLLSGGQRALVLTAARGRGKSAATGLSIAGLIEKLRERKEKSIRIIVTAPSIASASQVMSFAKLGLEALGEELSVKVSDTGHIKSLRGDYFKLEYVPPDAAIEDEGELLIIDEAAALGINYIDLALRAWKKVALVTTVHGYEGSNKAFLRYLRRLIESKRIRVKWVNMEQPLRYAKGDPIEKWLYDALLLDAEPSEPQYLNDTMIYEDVDKSELANDDNRLRAIYGIMVTAHYKNNPDDLMIMLDGIHHKIKAIRIGENSYIAACQIAEEGELSDNMVDIALKGGTFDGDLIPDRIIKHVRIKDFAKLRGWRIVRIAVAPELQDKGFGSELLKMIYEEARDKGVDWVGSSFMSDQKVLNFWIKNGFIPVHISPKKNEKLGDYPVVVIRPISDIATKIVKISAYMLKEKLLNTLHDVYFNMNPEVVRLMLTSTKIVSKTINVSPIILDKTISFLQGVSPYESSADGIHMLTLKYFWDGERDWSLTQDEELVLIAKVLQGKPWSYVSTVLSSNRTHIYELIYSAISKLMKKYYNLTADSKVGLTLKDVMNSQQYD

[Multiple Choices]
A. 2.3.1.319
B. 2.3.1.193
C. 4.3.1.24
D. 3.1.26.3
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

> The exact sequence matches the UniProt entry annotated as tRNA(Met) cytidine acetyltransferase TmcA2 with EC 2.3.1.193. The annotation cites both a HAMAP computational rule and a PubMed reference; this supports the key, though the annotation is not itself independent experimental validation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the large, multidomain TmcA/TmcA2 family of ATP-dependent RNA cytidine acetyltransferases. Transferable family knowledge links TmcA proteins to tRNA(Met) cytidine acetylation, making EC 2.3.1.193 (B) a meaningful choice over the unrelated lyase and nuclease alternatives, and more likely than a different acetyltransferase EC. This is a family-level inference, not a direct demonstration of the precise substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the TmcA-family sequence provides a credible basis to select B from these choices without recalling this exact protein's database record. The closest alternative is another acetyltransferase, so the exact EC distinction is less certain than the broad family assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-family inference favors B among the offered choices; the other acetyltransferase is a possible source of uncertainty but is not equally supported by the family assignment.


### Important caveats

- The reviewer-only source annotation is computationally and literature-supported; it should not be treated as independently verified experimental evidence here.
- The source sequence matches the supplied sequence, but the original data source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the large, multidomain TmcA/TmcA2 family of ATP-dependent RNA cytidine acetyltransferases. Transferable family knowledge links TmcA proteins to tRNA(Met) cytidine acetylation, making EC 2.3.1.193 (B) a meaningful choice over the unrelated lyase and nuclease alternatives, and more likely than a different acetyltransferase EC. This is a family-level inference, not a direct demonstration of the precise substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the TmcA-family sequence provides a credible basis to select B from these choices without recalling this exact protein's database record. The closest alternative is another acetyltransferase, so the exact EC distinction is less certain than the broad family assignment."
  },
  "case_id": "EC_number_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as tRNA(Met) cytidine acetyltransferase TmcA2 with EC 2.3.1.193. The annotation cites both a HAMAP computational rule and a PubMed reference; this supports the key, though the annotation is not itself independent experimental validation."
  },
  "important_caveats": [
    "The reviewer-only source annotation is computationally and literature-supported; it should not be treated as independently verified experimental evidence here.",
    "The source sequence matches the supplied sequence, but the original data source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference favors B among the offered choices; the other acetyltransferase is a possible source of uncertainty but is not equally supported by the family assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as tRNA(Met) cytidine acetyltransferase TmcA2 with EC 2.3.1.193. The annotation cites both a HAMAP computational rule and a PubMed reference; this supports the key, though the annotation is not itself independent experimental validation.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the large, multidomain TmcA/TmcA2 family of ATP-dependent RNA cytidine acetyltransferases. Transferable family knowledge links TmcA proteins to tRNA(Met) cytidine acetylation, making EC 2.3.1.193 (B) a meaningful choice over the unrelated lyase and nuclease alternatives, and more likely than a different acetyltransferase EC. This is a family-level inference, not a direct demonstration of the precise substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the TmcA-family sequence provides a credible basis to select B from these choices without recalling this exact protein's database record. The closest alternative is another acetyltransferase, so the exact EC distinction is less certain than the broad family assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference favors B among the offered choices; the other acetyltransferase is a possible source of uncertainty but is not equally supported by the family assignment."
  },
  "important_caveats": [
    "The reviewer-only source annotation is computationally and literature-supported; it should not be treated as independently verified experimental evidence here.",
    "The source sequence matches the supplied sequence, but the original data source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q97U12 (TMCA2_SACS2) annotates this 770-aa protein as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA 2). The annotation is supported by both HAMAP-Rule (MF_01886, computational) and experimental evidence from PubMed:32555463 (Nature 2020, Sas-Chen et al.). The catalytic reaction (cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O → N(4)-acetylcytidine(34) + ADP + Pi + CoA + H+) is consistent with EC 2.3.1.193. The benchmark sequence matches the UniProt sequence exactly (SHA-256 identical, 770 aa).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C9](#evidence-c9), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features allow narrowing among the four options. (1) The sequence contains multiple acetyl-CoA-binding GNAT-fold motifs: 'LLSGGQRALVLTAARGRGK' (the canonical Q/RxxGxG/A acetyl-CoA binding motif) and 'ARGGGLIIIY' (a second glycine-rich nucleotide-binding stretch). These are hallmarks of acyltransferases (EC 2.3.1.x), which immediately disfavors C (4.3.1.24, a carbon-nitrogen lyase) and D (3.1.26.3, ribonuclease III, a hydrolase), neither of which possesses GNAT motifs or the multi-domain architecture seen here. (2) The protein is ~770 aa with a large, multi-domain architecture including a Rossmann-like region and a putative RNA-binding domain, a combination characteristic of the TmcA/MiaB-like tRNA acetyltransferase family found across archaea and bacteria. Recognizing this family from shared sequence features (size, domain arrangement, GNAT + RNA-binding module) is legitimate transfer knowledge from other TmcA homologs. (3) Within the TmcA family the canonical EC number is 2.3.1.193. Option A (2.3.1.319) would represent a different acyltransferase with a different substrate class; the RNA-binding architecture and tRNA-recognition features visible in the sequence are inconsistent with a protein-substrate acetyltransferase. Thus family-level recognition of the TmcA fold, combined with the GNAT motifs, meaningfully distinguishes B from A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the GNAT acetyl-CoA-binding motifs to restrict to EC 2.3.1.x (eliminating C and D), then use the large multi-domain architecture with RNA-binding features to recognize the TmcA family, whose canonical EC number (2.3.1.193) is part of family-level knowledge shared across homologs. The distinction between 2.3.1.193 and 2.3.1.319 rests on recognizing the RNA-substrate architecture versus a protein-substrate acetyltransferase, which is a legitimate family-level inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (lyase) and D (hydrolase) are clearly inconsistent with the GNAT motifs and multi-domain architecture. The main challenge is A vs B (both 2.3.1.x acyltransferases), but the TmcA family architecture with RNA-binding domains provides a basis for selecting B over A. No two options are equally defensible given the sequence features.


### Important caveats

- The distinction between EC 2.3.1.193 (option B) and EC 2.3.1.319 (option A) is the finest discrimination in this question. If 2.3.1.319 is a recently assigned or obscure EC number, a model unfamiliar with it might default to B simply because TmcA is well-known, rather than through explicit exclusion of A.
- The UniProt annotation combines HAMAP computational inference (ECO:0000255) with experimental evidence (ECO:0000305, PubMed:32555463). The experimental evidence from the 2020 Nature paper supports the tRNA acetyltransferase activity, but the initial EC assignment was rule-based.
- The reviewer-only evidence confirms sequence identity to Q97U12, but this accession was not available to the evaluated model; the model must rely on sequence features and family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features allow narrowing among the four options. (1) The sequence contains multiple acetyl-CoA-binding GNAT-fold motifs: 'LLSGGQRALVLTAARGRGK' (the canonical Q/RxxGxG/A acetyl-CoA binding motif) and 'ARGGGLIIIY' (a second glycine-rich nucleotide-binding stretch). These are hallmarks of acyltransferases (EC 2.3.1.x), which immediately disfavors C (4.3.1.24, a carbon-nitrogen lyase) and D (3.1.26.3, ribonuclease III, a hydrolase), neither of which possesses GNAT motifs or the multi-domain architecture seen here. (2) The protein is ~770 aa with a large, multi-domain architecture including a Rossmann-like region and a putative RNA-binding domain, a combination characteristic of the TmcA/MiaB-like tRNA acetyltransferase family found across archaea and bacteria. Recognizing this family from shared sequence features (size, domain arrangement, GNAT + RNA-binding module) is legitimate transfer knowledge from other TmcA homologs. (3) Within the TmcA family the canonical EC number is 2.3.1.193. Option A (2.3.1.319) would represent a different acyltransferase with a different substrate class; the RNA-binding architecture and tRNA-recognition features visible in the sequence are inconsistent with a protein-substrate acetyltransferase. Thus family-level recognition of the TmcA fold, combined with the GNAT motifs, meaningfully distinguishes B from A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GNAT acetyl-CoA-binding motifs to restrict to EC 2.3.1.x (eliminating C and D), then use the large multi-domain architecture with RNA-binding features to recognize the TmcA family, whose canonical EC number (2.3.1.193) is part of family-level knowledge shared across homologs. The distinction between 2.3.1.193 and 2.3.1.319 rests on recognizing the RNA-substrate architecture versus a protein-substrate acetyltransferase, which is a legitimate family-level inference."
  },
  "case_id": "EC_number_0106",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C9",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q97U12 (TMCA2_SACS2) annotates this 770-aa protein as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA 2). The annotation is supported by both HAMAP-Rule (MF_01886, computational) and experimental evidence from PubMed:32555463 (Nature 2020, Sas-Chen et al.). The catalytic reaction (cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O → N(4)-acetylcytidine(34) + ADP + Pi + CoA + H+) is consistent with EC 2.3.1.193. The benchmark sequence matches the UniProt sequence exactly (SHA-256 identical, 770 aa)."
  },
  "important_caveats": [
    "The distinction between EC 2.3.1.193 (option B) and EC 2.3.1.319 (option A) is the finest discrimination in this question. If 2.3.1.319 is a recently assigned or obscure EC number, a model unfamiliar with it might default to B simply because TmcA is well-known, rather than through explicit exclusion of A.",
    "The UniProt annotation combines HAMAP computational inference (ECO:0000255) with experimental evidence (ECO:0000305, PubMed:32555463). The experimental evidence from the 2020 Nature paper supports the tRNA acetyltransferase activity, but the initial EC assignment was rule-based.",
    "The reviewer-only evidence confirms sequence identity to Q97U12, but this accession was not available to the evaluated model; the model must rely on sequence features and family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (lyase) and D (hydrolase) are clearly inconsistent with the GNAT motifs and multi-domain architecture. The main challenge is A vs B (both 2.3.1.x acyltransferases), but the TmcA family architecture with RNA-binding domains provides a basis for selecting B over A. No two options are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0106",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q97U12 (TMCA2_SACS2) annotates this 770-aa protein as EC 2.3.1.193 (tRNA(Met) cytidine acetyltransferase TmcA 2). The annotation is supported by both HAMAP-Rule (MF_01886, computational) and experimental evidence from PubMed:32555463 (Nature 2020, Sas-Chen et al.). The catalytic reaction (cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O → N(4)-acetylcytidine(34) + ADP + Pi + CoA + H+) is consistent with EC 2.3.1.193. The benchmark sequence matches the UniProt sequence exactly (SHA-256 identical, 770 aa).",
    "evidence_ids": ["C1", "C4", "C5", "C9", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features allow narrowing among the four options. (1) The sequence contains multiple acetyl-CoA-binding GNAT-fold motifs: 'LLSGGQRALVLTAARGRGK' (the canonical Q/RxxGxG/A acetyl-CoA binding motif) and 'ARGGGLIIIY' (a second glycine-rich nucleotide-binding stretch). These are hallmarks of acyltransferases (EC 2.3.1.x), which immediately disfavors C (4.3.1.24, a carbon-nitrogen lyase) and D (3.1.26.3, ribonuclease III, a hydrolase), neither of which possesses GNAT motifs or the multi-domain architecture seen here. (2) The protein is ~770 aa with a large, multi-domain architecture including a Rossmann-like region and a putative RNA-binding domain, a combination characteristic of the TmcA/MiaB-like tRNA acetyltransferase family found across archaea and bacteria. Recognizing this family from shared sequence features (size, domain arrangement, GNAT + RNA-binding module) is legitimate transfer knowledge from other TmcA homologs. (3) Within the TmcA family the canonical EC number is 2.3.1.193. Option A (2.3.1.319) would represent a different acyltransferase with a different substrate class; the RNA-binding architecture and tRNA-recognition features visible in the sequence are inconsistent with a protein-substrate acetyltransferase. Thus family-level recognition of the TmcA fold, combined with the GNAT motifs, meaningfully distinguishes B from A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the GNAT acetyl-CoA-binding motifs to restrict to EC 2.3.1.x (eliminating C and D), then use the large multi-domain architecture with RNA-binding features to recognize the TmcA family, whose canonical EC number (2.3.1.193) is part of family-level knowledge shared across homologs. The distinction between 2.3.1.193 and 2.3.1.319 rests on recognizing the RNA-substrate architecture versus a protein-substrate acetyltransferase, which is a legitimate family-level inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (lyase) and D (hydrolase) are clearly inconsistent with the GNAT motifs and multi-domain architecture. The main challenge is A vs B (both 2.3.1.x acyltransferases), but the TmcA family architecture with RNA-binding domains provides a basis for selecting B over A. No two options are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The distinction between EC 2.3.1.193 (option B) and EC 2.3.1.319 (option A) is the finest discrimination in this question. If 2.3.1.319 is a recently assigned or obscure EC number, a model unfamiliar with it might default to B simply because TmcA is well-known, rather than through explicit exclusion of A.",
    "The UniProt annotation combines HAMAP computational inference (ECO:0000255) with experimental evidence (ECO:0000305, PubMed:32555463). The experimental evidence from the 2020 Nature paper supports the tRNA acetyltransferase activity, but the initial EC assignment was rule-based.",
    "The reviewer-only evidence confirms sequence identity to Q97U12, but this accession was not available to the evaluated model; the model must rely on sequence features and family knowledge."
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
  "benchmark_sequence_length": 770,
  "benchmark_sequence_sha256": "4c8973d7468158c8175a67ed07434d008aaf57307a621aab360cc26d615ada85",
  "current_entry_audit": {
    "entryVersion": 123,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 770,
  "current_source_sequence_sha256": "4c8973d7468158c8175a67ed07434d008aaf57307a621aab360cc26d615ada85",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 122,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q97U12",
  "selected_historical_entry_version": 122,
  "selected_historical_record_sha256": "44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e",
  "selected_historical_source_sequence_length": 770,
  "selected_historical_source_sequence_sha256": "4c8973d7468158c8175a67ed07434d008aaf57307a621aab360cc26d615ada85",
  "selected_historical_version": {
    "accession": "Q97U12",
    "database": "Swiss-Prot",
    "entryVersion": 122,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "TMCA2_SACS2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q97U12\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:36.729149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "url": "https://rest.uniprot.org/uniprotkb/Q97U12.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":123,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:36.729149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "url": "https://rest.uniprot.org/uniprotkb/Q97U12.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Sulfolobus solfataricus\",\"lineage\":[\"Archaea\",\"Thermoproteota\",\"Thermoprotei\",\"Sulfolobales\",\"Sulfolobaceae\",\"Saccharolobus\"],\"scientificName\":\"Saccharolobus solfataricus (strain ATCC 35092 / DSM 1617 / JCM 11322 / P2)\",\"taxonId\":273057}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:36.729149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "url": "https://rest.uniprot.org/uniprotkb/Q97U12.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.193\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"}],\"value\":\"tRNA(Met) cytidine acetyltransferase TmcA 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:36.729149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "url": "https://rest.uniprot.org/uniprotkb/Q97U12.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.193\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_01886\",\"source\":\"HAMAP-Rule\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:43788\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10693\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:36.729149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "url": "https://rest.uniprot.org/uniprotkb/Q97U12.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in RNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:82211\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15704\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19834\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:32:36.729149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "url": "https://rest.uniprot.org/uniprotkb/Q97U12.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:53876\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13670\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:13671\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:32:36.729149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "url": "https://rest.uniprot.org/uniprotkb/Q97U12.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"32555463\",\"source\":\"PubMed\"}],\"name\":\"a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58480\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15145\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:74900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82748\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:32:36.729149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "url": "https://rest.uniprot.org/uniprotkb/Q97U12.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97U12.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Sas-Chen A.\",\"Thomas J.M.\",\"Matzov D.\",\"Taoka M.\",\"Nance K.D.\",\"Nir R.\",\"Bryson K.M.\",\"Shachar R.\",\"Liman G.L.S.\",\"Burkhart B.W.\",\"Gamage S.T.\",\"Nobe Y.\",\"Briney C.A.\",\"Levy M.J.\",\"Fuchs R.T.\",\"Robb G.B.\",\"Hartmann J.\",\"Sharma S.\",\"Lin Q.\",\"Florens L.\",\"Washburn M.P.\",\"Isobe T.\",\"Santangelo T.J.\",\"Shalev-Benami M.\",\"Meier J.L.\",\"Schwartz S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32555463\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-020-2418-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"638\",\"id\":\"32555463\",\"journal\":\"Nature\",\"lastPage\":\"643\",\"publicationDate\":\"2020\",\"title\":\"Dynamic RNA acetylation revealed by quantitative cross-evolutionary mapping.\",\"volume\":\"583\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 35092 / DSM 1617 / JCM 11322 / P2\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:36.729149+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "59aca13bc726397aae7e1b35530edb9a9c0e76c8b9e6dbb660ab8b1265f7e7ff",
  "url": "https://rest.uniprot.org/uniprotkb/Q97U12.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H1",
  "excerpt": "ID   TMCA2_SACS2             Reviewed;         770 AA.\nAC   Q97U12;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2001, sequence version 1.\nDT   28-JAN-2026, entry version 122.\nDE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA 2 {ECO:0000255|HAMAP-Rule:MF_01886};\nDE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000305|PubMed:32555463};\nGN   Name=tmcA2 {ECO:0000255|HAMAP-Rule:MF_01886};\nGN   OrderedLocusNames=SSO3214 {ECO:0000312|EMBL:AAK43310.1};\nOS   Saccharolobus solfataricus (strain ATCC 35092 / DSM 1617 / JCM 11322 / P2)\nOS   (Sulfolobus solfataricus).\nOC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;\nOC   Saccharolobus.\nOX   NCBI_TaxID=273057;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:38.813381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e",
  "url": "https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=tRNA(Met) cytidine acetyltransferase TmcA 2 {ECO:0000255|HAMAP-Rule:MF_01886};\nDE            EC=2.3.1.193 {ECO:0000255|HAMAP-Rule:MF_01886, ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:38.813381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e",
  "url": "https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRC   STRAIN=ATCC 35092 / DSM 1617 / JCM 11322 / P2;\nRX   PubMed=32555463; DOI=10.1038/s41586-020-2418-2;\nRA   Sas-Chen A., Thomas J.M., Matzov D., Taoka M., Nance K.D., Nir R.,\nRA   Bryson K.M., Shachar R., Liman G.L.S., Burkhart B.W., Gamage S.T., Nobe Y.,\nRA   Briney C.A., Levy M.J., Fuchs R.T., Robb G.B., Hartmann J., Sharma S.,\nRA   Lin Q., Florens L., Washburn M.P., Isobe T., Santangelo T.J.,\nRA   Shalev-Benami M., Meier J.L., Schwartz S.;\nRT   \"Dynamic RNA acetylation revealed by quantitative cross-evolutionary\nRT   mapping.\";\nRL   Nature 583:638-643(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:38.813381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e",
  "url": "https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O =\nCC         N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate +\nCC         CoA + H(+); Xref=Rhea:RHEA:43788, Rhea:RHEA-COMP:10693, Rhea:RHEA-\nCC         COMP:10694, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         EC=2.3.1.193; Evidence={ECO:0000255|HAMAP-Rule:MF_01886,\nCC         ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:38.813381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e",
  "url": "https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in RNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in RNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:82211, Rhea:RHEA-COMP:15704, Rhea:RHEA-COMP:19834,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:38.813381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e",
  "url": "https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in tRNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:53876, Rhea:RHEA-COMP:13670, Rhea:RHEA-COMP:13671,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:38.813381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e",
  "url": "https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-\nCC         acetylcytidine in mRNA + ADP + phosphate + CoA + H(+);\nCC         Xref=Rhea:RHEA:58480, Rhea:RHEA-COMP:15145, Rhea:RHEA-COMP:15146,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57287, ChEBI:CHEBI:57288,\nCC         ChEBI:CHEBI:74900, ChEBI:CHEBI:82748, ChEBI:CHEBI:456216;\nCC         Evidence={ECO:0000305|PubMed:32555463};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:38.813381+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "44fcd9d29bab44259f01fffb7c9d00c1c46307afcc45117c02ef309532fcb63e",
  "url": "https://rest.uniprot.org/unisave/Q97U12?format=txt&versions=122"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 106. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
