# cofactor_0000

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0000.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — Fe(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKYAHVGLNVTNLEKSIEFYSKLFGAEPVKVKPDYAKFLLESPGLNFTLNLRDEVNGNQVGHFGIQVESTEEVVAHKNRLAENGILSQYDEINTTCCYALQDKFWIHDPDGNEWEFFYTKTTVEENSTHPPTCCVNEPNVEKAECCSPTASSNKDTSNCCS

[Multiple Choices]
A. pyridoxal 5'-phosphate
B. [4Fe-4S] cluster
C. Fe(2+)
D. FAD
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

> The source record matches the supplied sequence and annotates Fe(2+) as the cofactor, with experimental evidence codes citing two papers. The excerpts support the key as a database annotation backed by cited experimental evidence, although the papers were not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has histidines and acidic residues that could support a non-heme iron-binding site; such His/carboxylate coordination is characteristic of many Fe(2+)-dependent enzymes. That is a meaningful fit for Fe(2+) over PLP or FAD, which often have recognizable cofactor-binding features. The cysteine-rich tail makes an Fe-S alternative worth considering, but it does not by itself establish a canonical Fe-S binding site.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable metal-binding pattern provides a plausible basis for selecting Fe(2+) among these choices without knowing this protein’s recorded annotation. The sequence evidence is suggestive rather than conclusive.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence leaves some uncertainty, especially given its cysteine-rich region, but the offered choices do not yield a second equally supported answer.


### Important caveats

- Sequence motifs alone do not prove which cofactor is required; the answerability judgment is about a credible inference, not certainty.
- The reviewer-only source identity and annotations were not part of the original input and are not used as the basis for the transferable inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has histidines and acidic residues that could support a non-heme iron-binding site; such His/carboxylate coordination is characteristic of many Fe(2+)-dependent enzymes. That is a meaningful fit for Fe(2+) over PLP or FAD, which often have recognizable cofactor-binding features. The cysteine-rich tail makes an Fe-S alternative worth considering, but it does not by itself establish a canonical Fe-S binding site.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable metal-binding pattern provides a plausible basis for selecting Fe(2+) among these choices without knowing this protein’s recorded annotation. The sequence evidence is suggestive rather than conclusive."
  },
  "case_id": "cofactor_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The source record matches the supplied sequence and annotates Fe(2+) as the cofactor, with experimental evidence codes citing two papers. The excerpts support the key as a database annotation backed by cited experimental evidence, although the papers were not independently reviewed here."
  },
  "important_caveats": [
    "Sequence motifs alone do not prove which cofactor is required; the answerability judgment is about a credible inference, not certainty.",
    "The reviewer-only source identity and annotations were not part of the original input and are not used as the basis for the transferable inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence leaves some uncertainty, especially given its cysteine-rich region, but the offered choices do not yield a second equally supported answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The source record matches the supplied sequence and annotates Fe(2+) as the cofactor, with experimental evidence codes citing two papers. The excerpts support the key as a database annotation backed by cited experimental evidence, although the papers were not independently reviewed here.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has histidines and acidic residues that could support a non-heme iron-binding site; such His/carboxylate coordination is characteristic of many Fe(2+)-dependent enzymes. That is a meaningful fit for Fe(2+) over PLP or FAD, which often have recognizable cofactor-binding features. The cysteine-rich tail makes an Fe-S alternative worth considering, but it does not by itself establish a canonical Fe-S binding site.",
    "missing_item_specific_fact": "",
    "reason": "A transferable metal-binding pattern provides a plausible basis for selecting Fe(2+) among these choices without knowing this protein’s recorded annotation. The sequence evidence is suggestive rather than conclusive."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence leaves some uncertainty, especially given its cysteine-rich region, but the offered choices do not yield a second equally supported answer."
  },
  "important_caveats": [
    "Sequence motifs alone do not prove which cofactor is required; the answerability judgment is about a credible inference, not certainty.",
    "The reviewer-only source identity and annotations were not part of the original input and are not used as the basis for the transferable inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A059WI14, ARSI_BACX0) annotates Fe(2+) as the cofactor with experimental evidence codes ECO:0000269 from two independent publications (PubMed:24821808, 2014 PNAS; PubMed:28936873, 2017 Environ. Sci. Technol.). The sequence matches the benchmark input exactly (161 aa, SHA-256 match). The cofactor annotation is backed by mutagenesis of His-5, His-62, Cys-96, Cys-97, and Glu-115, and by biochemical characterization of the C-As lyase activity (EC 1.13.11.-).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 161-aa sequence contains a pattern consistent with the 2-His-1-carboxylate facial triad, one of the most well-characterized metal-binding motifs in bioinorganic chemistry: His at position 5 (MKYAH), His near position 62 (GHFGIQ), and Glu near position 115 (EWEFFY). This triad is the hallmark of mononuclear Fe(II)-dependent dioxygenases and related oxidoreductases (EC 1.13.11 class). Additionally, the HDP motif around position 103 reinforces an Fe(II) coordination environment. Critically, the sequence lacks any Rossmann-fold or FAD-binding motifs (no GxGxxG, no typical FAD-binding loops), ruling out FAD (D). It also lacks the conserved lysine in a PLP-binding context and the aminotransferase fold, ruling out pyridoxal 5'-phosphate (A). While the Cys-Cys pairs (TTCC at ~96-97, CC at ~143-144, CC at ~159-160) might superficially suggest a &#91;4Fe-4S&#93; cluster (B), canonical &#91;4Fe-4S&#93; sites require four cysteines in a CxxCxxC…C spacing pattern within a structured domain, which is not clearly present here; moreover, the dominant His/acidic-residue pattern is diagnostic of mononuclear Fe(II) rather than cluster-type iron. A model familiar with the 2-His-1-carboxylate triad from other Fe(II) dioxygenases (e.g., extradiol dioxygenases, phytanoyl-CoA dioxygenase, prolyl hydroxylase) could credibly infer Fe(2+) over the three alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The 2-His-1-carboxylate facial triad is a broadly transferable bioinorganic motif recognized across many Fe(II)-dependent enzyme families. Its identification from the sequence (H5, H62, E115 plus the HDP motif) meaningfully distinguishes Fe(2+) from FAD, PLP, and &#91;4Fe-4S&#93; among the offered choices. The absence of FAD/PLP-binding motifs and the non-canonical Cys spacing for Fe-S clusters further narrow the alternatives. This does not require recalling the specific ArsI annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The 2-His-1-carboxylate facial triad pattern strongly favors Fe(2+) over the other three options. FAD and PLP are excluded by the absence of their characteristic binding motifs. &#91;4Fe-4S&#93; is disfavored because the cysteine spacing does not match a canonical cluster-binding site and the dominant His/Glu pattern is inconsistent with cluster-type iron. No alternative choice is comparably supported by the sequence features.


### Important caveats

- ArsI is a novel enzyme class (C-As lyase); the 2-His-1-carboxylate triad inference is based on general bioinorganic principles rather than a large family of closely related homologs.
- The Cys-96/Cys-97 residues were shown by mutagenesis to be important for activity but are not the primary metal ligands; their presence could mislead a model toward &#91;4Fe-4S&#93;.
- The EC number 1.13.11.- (dioxygenase class) is not directly derivable from the sequence alone but is consistent with the Fe(II) inference.
- The reviewer-only evidence confirms the annotation with experimental evidence codes (ECO:0000269), but this was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 161-aa sequence contains a pattern consistent with the 2-His-1-carboxylate facial triad, one of the most well-characterized metal-binding motifs in bioinorganic chemistry: His at position 5 (MKYAH), His near position 62 (GHFGIQ), and Glu near position 115 (EWEFFY). This triad is the hallmark of mononuclear Fe(II)-dependent dioxygenases and related oxidoreductases (EC 1.13.11 class). Additionally, the HDP motif around position 103 reinforces an Fe(II) coordination environment. Critically, the sequence lacks any Rossmann-fold or FAD-binding motifs (no GxGxxG, no typical FAD-binding loops), ruling out FAD (D). It also lacks the conserved lysine in a PLP-binding context and the aminotransferase fold, ruling out pyridoxal 5'-phosphate (A). While the Cys-Cys pairs (TTCC at ~96-97, CC at ~143-144, CC at ~159-160) might superficially suggest a [4Fe-4S] cluster (B), canonical [4Fe-4S] sites require four cysteines in a CxxCxxC…C spacing pattern within a structured domain, which is not clearly present here; moreover, the dominant His/acidic-residue pattern is diagnostic of mononuclear Fe(II) rather than cluster-type iron. A model familiar with the 2-His-1-carboxylate triad from other Fe(II) dioxygenases (e.g., extradiol dioxygenases, phytanoyl-CoA dioxygenase, prolyl hydroxylase) could credibly infer Fe(2+) over the three alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The 2-His-1-carboxylate facial triad is a broadly transferable bioinorganic motif recognized across many Fe(II)-dependent enzyme families. Its identification from the sequence (H5, H62, E115 plus the HDP motif) meaningfully distinguishes Fe(2+) from FAD, PLP, and [4Fe-4S] among the offered choices. The absence of FAD/PLP-binding motifs and the non-canonical Cys spacing for Fe-S clusters further narrow the alternatives. This does not require recalling the specific ArsI annotation."
  },
  "case_id": "cofactor_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A059WI14, ARSI_BACX0) annotates Fe(2+) as the cofactor with experimental evidence codes ECO:0000269 from two independent publications (PubMed:24821808, 2014 PNAS; PubMed:28936873, 2017 Environ. Sci. Technol.). The sequence matches the benchmark input exactly (161 aa, SHA-256 match). The cofactor annotation is backed by mutagenesis of His-5, His-62, Cys-96, Cys-97, and Glu-115, and by biochemical characterization of the C-As lyase activity (EC 1.13.11.-)."
  },
  "important_caveats": [
    "ArsI is a novel enzyme class (C-As lyase); the 2-His-1-carboxylate triad inference is based on general bioinorganic principles rather than a large family of closely related homologs.",
    "The Cys-96/Cys-97 residues were shown by mutagenesis to be important for activity but are not the primary metal ligands; their presence could mislead a model toward [4Fe-4S].",
    "The EC number 1.13.11.- (dioxygenase class) is not directly derivable from the sequence alone but is consistent with the Fe(II) inference.",
    "The reviewer-only evidence confirms the annotation with experimental evidence codes (ECO:0000269), but this was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 2-His-1-carboxylate facial triad pattern strongly favors Fe(2+) over the other three options. FAD and PLP are excluded by the absence of their characteristic binding motifs. [4Fe-4S] is disfavored because the cysteine spacing does not match a canonical cluster-binding site and the dominant His/Glu pattern is inconsistent with cluster-type iron. No alternative choice is comparably supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A059WI14, ARSI_BACX0) annotates Fe(2+) as the cofactor with experimental evidence codes ECO:0000269 from two independent publications (PubMed:24821808, 2014 PNAS; PubMed:28936873, 2017 Environ. Sci. Technol.). The sequence matches the benchmark input exactly (161 aa, SHA-256 match). The cofactor annotation is backed by mutagenesis of His-5, His-62, Cys-96, Cys-97, and Glu-115, and by biochemical characterization of the C-As lyase activity (EC 1.13.11.-).",
    "evidence_ids": ["C5", "C6", "C7", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 161-aa sequence contains a pattern consistent with the 2-His-1-carboxylate facial triad, one of the most well-characterized metal-binding motifs in bioinorganic chemistry: His at position 5 (MKYAH), His near position 62 (GHFGIQ), and Glu near position 115 (EWEFFY). This triad is the hallmark of mononuclear Fe(II)-dependent dioxygenases and related oxidoreductases (EC 1.13.11 class). Additionally, the HDP motif around position 103 reinforces an Fe(II) coordination environment. Critically, the sequence lacks any Rossmann-fold or FAD-binding motifs (no GxGxxG, no typical FAD-binding loops), ruling out FAD (D). It also lacks the conserved lysine in a PLP-binding context and the aminotransferase fold, ruling out pyridoxal 5'-phosphate (A). While the Cys-Cys pairs (TTCC at ~96-97, CC at ~143-144, CC at ~159-160) might superficially suggest a [4Fe-4S] cluster (B), canonical [4Fe-4S] sites require four cysteines in a CxxCxxC…C spacing pattern within a structured domain, which is not clearly present here; moreover, the dominant His/acidic-residue pattern is diagnostic of mononuclear Fe(II) rather than cluster-type iron. A model familiar with the 2-His-1-carboxylate triad from other Fe(II) dioxygenases (e.g., extradiol dioxygenases, phytanoyl-CoA dioxygenase, prolyl hydroxylase) could credibly infer Fe(2+) over the three alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The 2-His-1-carboxylate facial triad is a broadly transferable bioinorganic motif recognized across many Fe(II)-dependent enzyme families. Its identification from the sequence (H5, H62, E115 plus the HDP motif) meaningfully distinguishes Fe(2+) from FAD, PLP, and [4Fe-4S] among the offered choices. The absence of FAD/PLP-binding motifs and the non-canonical Cys spacing for Fe-S clusters further narrow the alternatives. This does not require recalling the specific ArsI annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 2-His-1-carboxylate facial triad pattern strongly favors Fe(2+) over the other three options. FAD and PLP are excluded by the absence of their characteristic binding motifs. [4Fe-4S] is disfavored because the cysteine spacing does not match a canonical cluster-binding site and the dominant His/Glu pattern is inconsistent with cluster-type iron. No alternative choice is comparably supported by the sequence features."
  },
  "important_caveats": [
    "ArsI is a novel enzyme class (C-As lyase); the 2-His-1-carboxylate triad inference is based on general bioinorganic principles rather than a large family of closely related homologs.",
    "The Cys-96/Cys-97 residues were shown by mutagenesis to be important for activity but are not the primary metal ligands; their presence could mislead a model toward [4Fe-4S].",
    "The EC number 1.13.11.- (dioxygenase class) is not directly derivable from the sequence alone but is consistent with the Fe(II) inference.",
    "The reviewer-only evidence confirms the annotation with experimental evidence codes (ECO:0000269), but this was not available to the evaluated model."
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
  "benchmark_sequence_length": 161,
  "benchmark_sequence_sha256": "630a5e1022193a240664c838cafc0c7d8aba4c00729a8de18bb80e3a504feff9",
  "current_entry_audit": {
    "entryVersion": 23,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-09-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 161,
  "current_source_sequence_sha256": "630a5e1022193a240664c838cafc0c7d8aba4c00729a8de18bb80e3a504feff9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 22,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A059WI14",
  "selected_historical_entry_version": 22,
  "selected_historical_record_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "selected_historical_source_sequence_length": 161,
  "selected_historical_source_sequence_sha256": "630a5e1022193a240664c838cafc0c7d8aba4c00729a8de18bb80e3a504feff9",
  "selected_historical_version": {
    "accession": "A0A059WI14",
    "database": "Swiss-Prot",
    "entryVersion": 22,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "ARSI_BACX0",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A059WI14\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":23,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-09-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Bacillaceae\",\"Bacillus\"],\"scientificName\":\"Bacillus sp. (strain MD1)\",\"taxonId\":1501233}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"value\":\"Arsenic inducible gene ArsI\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24821808\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28936873\",\"source\":\"PubMed\"}],\"value\":\"C-As lyase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"value\":\"Methylarsonous acid demethylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"value\":\"MAs(III) demethylase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28936873\",\"source\":\"PubMed\"}],\"value\":\"1.13.11.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"24821808\",\"source\":\"PubMed\"}],\"value\":\"Trivalent organoarsenical cleaving enzyme\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29033\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24821808\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28936873\",\"source\":\"PubMed\"}],\"name\":\"Fe(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yoshinaga M.\",\"Rosen B.P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24821808\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1403057111\"}],\"citationType\":\"journal article\",\"firstPage\":\"7701\",\"id\":\"24821808\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"7706\",\"publicationDate\":\"2014\",\"title\":\"A C-As lyase for degradation of environmental organoarsenical herbicides and animal husbandry growth promoters.\",\"volume\":\"111\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"MD1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A059WI14.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Pawitwar S.S.\",\"Nadar V.S.\",\"Kandegedara A.\",\"Stemmler T.L.\",\"Rosen B.P.\",\"Yoshinaga M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28936873\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.est.7b03180\"}],\"citationType\":\"journal article\",\"firstPage\":\"11115\",\"id\":\"28936873\",\"journal\":\"Environ. Sci. Technol.\",\"lastPage\":\"11125\",\"publicationDate\":\"2017\",\"title\":\"Biochemical Characterization of ArsI: A Novel C-As Lyase for Degradation of Environmental Organoarsenicals.\",\"volume\":\"51\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"MD1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"3D-STRUCTURE MODELING\",\"MUTAGENESIS OF HIS-5; HIS-62; 96-CYS-CYS-97 AND GLU-115\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:23:54.040783+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8f03a35522b3d82d736a708e66977d0e99c44951c0c098514a18248bc8c22f4e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A059WI14.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H1",
  "excerpt": "ID   ARSI_BACX0              Reviewed;         161 AA.\nAC   A0A059WI14;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-SEP-2014, sequence version 1.\nDT   28-JAN-2026, entry version 22.\nDE   RecName: Full=Trivalent organoarsenical cleaving enzyme {ECO:0000305|PubMed:24821808};\nDE            EC=1.13.11.- {ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};\nDE   AltName: Full=Arsenic inducible gene ArsI {ECO:0000303|PubMed:24821808};\nDE   AltName: Full=C-As lyase {ECO:0000303|PubMed:24821808, ECO:0000303|PubMed:28936873};\nDE   AltName: Full=Methylarsonous acid demethylase {ECO:0000303|PubMed:24821808};\nDE            Short=MAs(III) demethylase {ECO:0000303|PubMed:24821808};\nGN   Name=arsI {ECO:0000303|PubMed:24821808, ECO:0000312|EMBL:AIA09488.1};\nOS   Bacillus sp. (strain MD1).\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae; Bacillus.\nOX   NCBI_TaxID=1501233;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Trivalent organoarsenical cleaving enzyme {ECO:0000305|PubMed:24821808};\nDE            EC=1.13.11.- {ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};\nDE   AltName: Full=Arsenic inducible gene ArsI {ECO:0000303|PubMed:24821808};\nDE   AltName: Full=C-As lyase {ECO:0000303|PubMed:24821808, ECO:0000303|PubMed:28936873};\nDE   AltName: Full=Methylarsonous acid demethylase {ECO:0000303|PubMed:24821808};\nDE            Short=MAs(III) demethylase {ECO:0000303|PubMed:24821808};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=MD1;\nRX   PubMed=24821808; DOI=10.1073/pnas.1403057111;\nRA   Yoshinaga M., Rosen B.P.;\nRT   \"A C-As lyase for degradation of environmental organoarsenical herbicides\nRT   and animal husbandry growth promoters.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 111:7701-7706(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, 3D-STRUCTURE\nRP   MODELING, AND MUTAGENESIS OF HIS-5; HIS-62; 96-CYS-CYS-97 AND GLU-115.\nRC   STRAIN=MD1;\nRX   PubMed=28936873; DOI=10.1021/acs.est.7b03180;\nRA   Pawitwar S.S., Nadar V.S., Kandegedara A., Stemmler T.L., Rosen B.P.,\nRA   Yoshinaga M.;\nRT   \"Biochemical Characterization of ArsI: A Novel C-As Lyase for Degradation\nRT   of Environmental Organoarsenicals.\";\nRL   Environ. Sci. Technol. 51:11115-11125(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22)

```json
{
  "entry_version": 22,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Fe(2+); Xref=ChEBI:CHEBI:29033;\nCC         Evidence={ECO:0000269|PubMed:24821808, ECO:0000269|PubMed:28936873};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:23:56.065730+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 79-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "64b679b08c78f78bd0eefc397743cd9c2b8ee062794e951deec5c900823833d7",
  "url": "https://rest.uniprot.org/unisave/A0A059WI14?format=txt&versions=22"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
