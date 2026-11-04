# EC_number_0150

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0150.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 4.3.1.12

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFMREIELKGHIIDSFILAKVFDRTLELGGDYKVLEFDIGKKKIDTSYAKLLISGDTQQHLDQILEELQNVGANIPEIENANLKPALKDSVLPDGFYSTTNHPTHVKVNDEWIEVANPKMDAVIVVYPEEKRAETKVIRKVKKGDFVLIGHNGIRVMPPEKSREAGQLFEFMNSEVSSEKPKEAIIKRIAKEMHEIREEYKKTGTGGIAIVGGPAIIHTGGGPALAKMVELGYIQAILAGNALATHDIESALYGTSLGVNIKTAKPVTGGHKHHIYAINAINDAGNIKNAVESGVLKEGIMYQCIKNNIPYVLAGSIRDDGPIPDVITDSMVAQDKMRTTVMDKKMVIMLSTLLHSVATGNLMPSYIKTVCVDIQPSTVTKLMDRGTSQAIGVVTDVGVFLVLLLKELERLELQE

[Multiple Choices]
A. 4.2.3.1
B. 1.1.1.122
C. 4.4.1.11
D. 4.3.1.12
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

> The sequence-matched UniProt record assigns EC 4.3.1.12 and gives the reaction L-ornithine = L-proline + NH4(+), with experimental-evidence codes. This supports choice D for the supplied sequence, though the cited study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is compatible with the NAD-dependent ornithine cyclodeaminase family: its enzyme-sized sequence and glycine-rich region are consistent with a nucleotide-cofactor-binding enzyme, and family-level sequence-profile recognition can distinguish this family from the other offered enzyme classes. Ornithine cyclodeaminases convert ornithine to proline with ammonia release, matching EC 4.3.1.12.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence patterns and transferable knowledge of related enzymes gives a meaningful basis for choosing D over the offered alternatives. The cofactor-related feature alone is not uniquely diagnostic, so confidence in an exact EC assignment is less than experimental confirmation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The provided evidence supports D, and no other offered choice is comparably supported.


### Important caveats

- The annotation supports the key for the sequence-matched record; the author’s exact source snapshot is unknown.
- A glycine-rich cofactor-binding-like region is not, by itself, sufficient to establish the full EC number.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with the NAD-dependent ornithine cyclodeaminase family: its enzyme-sized sequence and glycine-rich region are consistent with a nucleotide-cofactor-binding enzyme, and family-level sequence-profile recognition can distinguish this family from the other offered enzyme classes. Ornithine cyclodeaminases convert ornithine to proline with ammonia release, matching EC 4.3.1.12.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence patterns and transferable knowledge of related enzymes gives a meaningful basis for choosing D over the offered alternatives. The cofactor-related feature alone is not uniquely diagnostic, so confidence in an exact EC assignment is less than experimental confirmation."
  },
  "case_id": "EC_number_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 4.3.1.12 and gives the reaction L-ornithine = L-proline + NH4(+), with experimental-evidence codes. This supports choice D for the supplied sequence, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The annotation supports the key for the sequence-matched record; the author’s exact source snapshot is unknown.",
    "A glycine-rich cofactor-binding-like region is not, by itself, sufficient to establish the full EC number."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The provided evidence supports D, and no other offered choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 4.3.1.12 and gives the reaction L-ornithine = L-proline + NH4(+), with experimental-evidence codes. This supports choice D for the supplied sequence, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is compatible with the NAD-dependent ornithine cyclodeaminase family: its enzyme-sized sequence and glycine-rich region are consistent with a nucleotide-cofactor-binding enzyme, and family-level sequence-profile recognition can distinguish this family from the other offered enzyme classes. Ornithine cyclodeaminases convert ornithine to proline with ammonia release, matching EC 4.3.1.12.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence patterns and transferable knowledge of related enzymes gives a meaningful basis for choosing D over the offered alternatives. The cofactor-related feature alone is not uniquely diagnostic, so confidence in an exact EC assignment is less than experimental confirmation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The provided evidence supports D, and no other offered choice is comparably supported."
  },
  "important_caveats": [
    "The annotation supports the key for the sequence-matched record; the author’s exact source snapshot is unknown.",
    "A glycine-rich cofactor-binding-like region is not, by itself, sufficient to establish the full EC number."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q6LXX7 (AOCD_METMP, Methanococcus maripaludis) is annotated as Ornithine cyclodeaminase with EC 4.3.1.12, supported by experimental evidence (ECO:0000269, PubMed:30636068, Burnat et al. 2019). The catalytic activity is explicitly stated as L-ornithine = L-proline + NH4(+), which corresponds to EC 4.3.1.12 (carbon-nitrogen lyase). The sequence in the question matches the UniProt entry (415 aa, SHA256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold nucleotide-binding motif ('GGPAIIHTGGGPALAKM', i.e. GG-x-G-x-x-G pattern), indicating a nucleotide-dependent enzyme. The overall fold architecture (~415 aa, Rossmann fold, specific loop patterns) is characteristic of the histidine ammonia-lyase (HAL) superfamily, which includes well-known members such as histidine ammonia-lyase (EC 4.3.1.23), phenylalanine ammonia-lyase (EC 4.3.1.24), and ornithine cyclodeaminase (EC 4.3.1.12). All HAL-superfamily members are carbon-nitrogen lyases (EC 4.3.1.x). Among the four options, only D (4.3.1.12) falls in the 4.3.1.x class (C-N lyases). Option B (1.1.1.122, oxidoreductase) is inconsistent because the sequence lacks the canonical catalytic residues (e.g., Tyr-X-X-X-Lys or Ser-Tyr-Lys triad) of dehydrogenases despite having a Rossmann fold. Option C (4.4.1.11, C-S lyase) is inconsistent as no sulfur-transfer chemistry or Cys/Ser nucleophile motifs are apparent. Option A (4.2.3.1, hydro-lyase) does not match the HAL-superfamily C-N lyase mechanism. Thus, recognizing the HAL superfamily fold from sequence and knowing that its members are EC 4.3.1.x lyases meaningfully distinguishes D from the other three alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the Rossmann-fold motif, overall fold architecture, and knowledge of the HAL superfamily (learned from histidine ammonia-lyase, phenylalanine ammonia-lyase, and related enzymes) to infer that this enzyme belongs to the carbon-nitrogen lyase class (EC 4.3.1.x). Among the offered choices, only D is in this class. The other options represent different EC classes (oxidoreductase, hydro-lyase, C-S lyase) whose catalytic mechanisms and sequence signatures do not match the observed architecture. This is a legitimate family-level inference from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct EC classes (4.2.3.x hydro-lyase, 1.1.1.x oxidoreductase, 4.4.1.x C-S lyase, 4.3.1.x C-N lyase). The HAL-superfamily fold architecture and Rossmann motif point specifically to the C-N lyase class, leaving only D as consistent. The other options are not defensible alternatives given the fold and motif evidence.


### Important caveats

- The HAL-superfamily recognition from sequence alone is non-trivial; the Rossmann fold (GGxGxxG) is shared with many dehydrogenases. The argument relies on the broader fold architecture and the absence of dehydrogenase catalytic residues, not solely on the Rossmann motif.
- The specific assignment to ornithine cyclodeaminase (EC 4.3.1.12) rather than another HAL-superfamily member (e.g., EC 4.3.1.23 or 4.3.1.24) is not fully derivable from sequence alone; however, among the offered choices, only D is in the 4.3.1.x class, so the superfamily-level inference suffices to select D.
- Some distractor EC numbers (e.g., 4.2.3.1, 1.1.1.122) may not correspond to well-established or commonly encountered enzymes, potentially making them easier to eliminate, but the core reasoning does not depend on this.
- The enzyme was experimentally characterized in 2019 (PubMed:30636068); before that date, it would have been an uncharacterized protein, making this a relatively recent annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold nucleotide-binding motif ('GGPAIIHTGGGPALAKM', i.e. GG-x-G-x-x-G pattern), indicating a nucleotide-dependent enzyme. The overall fold architecture (~415 aa, Rossmann fold, specific loop patterns) is characteristic of the histidine ammonia-lyase (HAL) superfamily, which includes well-known members such as histidine ammonia-lyase (EC 4.3.1.23), phenylalanine ammonia-lyase (EC 4.3.1.24), and ornithine cyclodeaminase (EC 4.3.1.12). All HAL-superfamily members are carbon-nitrogen lyases (EC 4.3.1.x). Among the four options, only D (4.3.1.12) falls in the 4.3.1.x class (C-N lyases). Option B (1.1.1.122, oxidoreductase) is inconsistent because the sequence lacks the canonical catalytic residues (e.g., Tyr-X-X-X-Lys or Ser-Tyr-Lys triad) of dehydrogenases despite having a Rossmann fold. Option C (4.4.1.11, C-S lyase) is inconsistent as no sulfur-transfer chemistry or Cys/Ser nucleophile motifs are apparent. Option A (4.2.3.1, hydro-lyase) does not match the HAL-superfamily C-N lyase mechanism. Thus, recognizing the HAL superfamily fold from sequence and knowing that its members are EC 4.3.1.x lyases meaningfully distinguishes D from the other three alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the Rossmann-fold motif, overall fold architecture, and knowledge of the HAL superfamily (learned from histidine ammonia-lyase, phenylalanine ammonia-lyase, and related enzymes) to infer that this enzyme belongs to the carbon-nitrogen lyase class (EC 4.3.1.x). Among the offered choices, only D is in this class. The other options represent different EC classes (oxidoreductase, hydro-lyase, C-S lyase) whose catalytic mechanisms and sequence signatures do not match the observed architecture. This is a legitimate family-level inference from other proteins."
  },
  "case_id": "EC_number_0150",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q6LXX7 (AOCD_METMP, Methanococcus maripaludis) is annotated as Ornithine cyclodeaminase with EC 4.3.1.12, supported by experimental evidence (ECO:0000269, PubMed:30636068, Burnat et al. 2019). The catalytic activity is explicitly stated as L-ornithine = L-proline + NH4(+), which corresponds to EC 4.3.1.12 (carbon-nitrogen lyase). The sequence in the question matches the UniProt entry (415 aa, SHA256 match confirmed)."
  },
  "important_caveats": [
    "The HAL-superfamily recognition from sequence alone is non-trivial; the Rossmann fold (GGxGxxG) is shared with many dehydrogenases. The argument relies on the broader fold architecture and the absence of dehydrogenase catalytic residues, not solely on the Rossmann motif.",
    "The specific assignment to ornithine cyclodeaminase (EC 4.3.1.12) rather than another HAL-superfamily member (e.g., EC 4.3.1.23 or 4.3.1.24) is not fully derivable from sequence alone; however, among the offered choices, only D is in the 4.3.1.x class, so the superfamily-level inference suffices to select D.",
    "Some distractor EC numbers (e.g., 4.2.3.1, 1.1.1.122) may not correspond to well-established or commonly encountered enzymes, potentially making them easier to eliminate, but the core reasoning does not depend on this.",
    "The enzyme was experimentally characterized in 2019 (PubMed:30636068); before that date, it would have been an uncharacterized protein, making this a relatively recent annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct EC classes (4.2.3.x hydro-lyase, 1.1.1.x oxidoreductase, 4.4.1.x C-S lyase, 4.3.1.x C-N lyase). The HAL-superfamily fold architecture and Rossmann motif point specifically to the C-N lyase class, leaving only D as consistent. The other options are not defensible alternatives given the fold and motif evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0150",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q6LXX7 (AOCD_METMP, Methanococcus maripaludis) is annotated as Ornithine cyclodeaminase with EC 4.3.1.12, supported by experimental evidence (ECO:0000269, PubMed:30636068, Burnat et al. 2019). The catalytic activity is explicitly stated as L-ornithine = L-proline + NH4(+), which corresponds to EC 4.3.1.12 (carbon-nitrogen lyase). The sequence in the question matches the UniProt entry (415 aa, SHA256 match confirmed).",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold nucleotide-binding motif ('GGPAIIHTGGGPALAKM', i.e. GG-x-G-x-x-G pattern), indicating a nucleotide-dependent enzyme. The overall fold architecture (~415 aa, Rossmann fold, specific loop patterns) is characteristic of the histidine ammonia-lyase (HAL) superfamily, which includes well-known members such as histidine ammonia-lyase (EC 4.3.1.23), phenylalanine ammonia-lyase (EC 4.3.1.24), and ornithine cyclodeaminase (EC 4.3.1.12). All HAL-superfamily members are carbon-nitrogen lyases (EC 4.3.1.x). Among the four options, only D (4.3.1.12) falls in the 4.3.1.x class (C-N lyases). Option B (1.1.1.122, oxidoreductase) is inconsistent because the sequence lacks the canonical catalytic residues (e.g., Tyr-X-X-X-Lys or Ser-Tyr-Lys triad) of dehydrogenases despite having a Rossmann fold. Option C (4.4.1.11, C-S lyase) is inconsistent as no sulfur-transfer chemistry or Cys/Ser nucleophile motifs are apparent. Option A (4.2.3.1, hydro-lyase) does not match the HAL-superfamily C-N lyase mechanism. Thus, recognizing the HAL superfamily fold from sequence and knowing that its members are EC 4.3.1.x lyases meaningfully distinguishes D from the other three alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the Rossmann-fold motif, overall fold architecture, and knowledge of the HAL superfamily (learned from histidine ammonia-lyase, phenylalanine ammonia-lyase, and related enzymes) to infer that this enzyme belongs to the carbon-nitrogen lyase class (EC 4.3.1.x). Among the offered choices, only D is in this class. The other options represent different EC classes (oxidoreductase, hydro-lyase, C-S lyase) whose catalytic mechanisms and sequence signatures do not match the observed architecture. This is a legitimate family-level inference from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct EC classes (4.2.3.x hydro-lyase, 1.1.1.x oxidoreductase, 4.4.1.x C-S lyase, 4.3.1.x C-N lyase). The HAL-superfamily fold architecture and Rossmann motif point specifically to the C-N lyase class, leaving only D as consistent. The other options are not defensible alternatives given the fold and motif evidence."
  },
  "important_caveats": [
    "The HAL-superfamily recognition from sequence alone is non-trivial; the Rossmann fold (GGxGxxG) is shared with many dehydrogenases. The argument relies on the broader fold architecture and the absence of dehydrogenase catalytic residues, not solely on the Rossmann motif.",
    "The specific assignment to ornithine cyclodeaminase (EC 4.3.1.12) rather than another HAL-superfamily member (e.g., EC 4.3.1.23 or 4.3.1.24) is not fully derivable from sequence alone; however, among the offered choices, only D is in the 4.3.1.x class, so the superfamily-level inference suffices to select D.",
    "Some distractor EC numbers (e.g., 4.2.3.1, 1.1.1.122) may not correspond to well-established or commonly encountered enzymes, potentially making them easier to eliminate, but the core reasoning does not depend on this.",
    "The enzyme was experimentally characterized in 2019 (PubMed:30636068); before that date, it would have been an uncharacterized protein, making this a relatively recent annotation."
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
  "benchmark_sequence_length": 415,
  "benchmark_sequence_sha256": "355b4d824ba114e0b6eb06dbc86bbba020b6e400b3af07fafa23ce7ab0b5684b",
  "current_entry_audit": {
    "entryVersion": 102,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 415,
  "current_source_sequence_sha256": "355b4d824ba114e0b6eb06dbc86bbba020b6e400b3af07fafa23ce7ab0b5684b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 100,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6LXX7",
  "selected_historical_entry_version": 100,
  "selected_historical_record_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "selected_historical_source_sequence_length": 415,
  "selected_historical_source_sequence_sha256": "355b4d824ba114e0b6eb06dbc86bbba020b6e400b3af07fafa23ce7ab0b5684b",
  "selected_historical_version": {
    "accession": "Q6LXX7",
    "database": "Swiss-Prot",
    "entryVersion": 100,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AOCD_METMP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6LXX7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":102,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanococci\",\"Methanococcales\",\"Methanococcaceae\",\"Methanococcus\"],\"scientificName\":\"Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL)\",\"taxonId\":267377}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"Archaeal ornithine cyclodeaminase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"Mls2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"4.3.1.12\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"Ornithine cyclodeaminase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"OCD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"4.3.1.12\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"name\":\"L-ornithine = L-proline + NH4(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24368\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:28938\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:46911\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60039\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Burnat M.\",\"Picossi S.\",\"Valladares A.\",\"Herrero A.\",\"Flores E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30636068\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14203\"}],\"citationType\":\"journal article\",\"firstPage\":\"883\",\"id\":\"30636068\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"897\",\"publicationDate\":\"2019\",\"title\":\"Catabolic pathway of arginine in Anabaena involves a novel bifunctional enzyme that produces proline from arginine.\",\"volume\":\"111\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H1",
  "excerpt": "ID   AOCD_METMP              Reviewed;         415 AA.\nAC   Q6LXX7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 100.\nDE   RecName: Full=Ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE            Short=OCD {ECO:0000305};\nDE            EC=4.3.1.12 {ECO:0000269|PubMed:30636068};\nDE   AltName: Full=Archaeal ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE   AltName: Full=Mls2 {ECO:0000303|PubMed:30636068};\nGN   OrderedLocusNames=MMP1218 {ECO:0000312|EMBL:CAF30774.1};\nOS   Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2\nOS   / LL).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanococci; Methanococcales; Methanococcaceae; Methanococcus.\nOX   NCBI_TaxID=267377;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE            Short=OCD {ECO:0000305};\nDE            EC=4.3.1.12 {ECO:0000269|PubMed:30636068};\nDE   AltName: Full=Archaeal ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE   AltName: Full=Mls2 {ECO:0000303|PubMed:30636068};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL;\nRX   PubMed=30636068; DOI=10.1111/mmi.14203;\nRA   Burnat M., Picossi S., Valladares A., Herrero A., Flores E.;\nRT   \"Catabolic pathway of arginine in Anabaena involves a novel bifunctional\nRT   enzyme that produces proline from arginine.\";\nRL   Mol. Microbiol. 111:883-897(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-ornithine = L-proline + NH4(+); Xref=Rhea:RHEA:24368,\nCC         ChEBI:CHEBI:28938, ChEBI:CHEBI:46911, ChEBI:CHEBI:60039; EC=4.3.1.12;\nCC         Evidence={ECO:0000269|PubMed:30636068};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 150. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
